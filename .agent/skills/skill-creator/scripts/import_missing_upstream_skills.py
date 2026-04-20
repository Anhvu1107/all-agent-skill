#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import yaml


FRONTMATTER_RE = re.compile(
    r"^(?P<prefix>\ufeff?\s*)---\s*\r?\n(?P<frontmatter>.*?)\r?\n---\s*(?P<body>.*)$",
    re.DOTALL,
)


@dataclass(frozen=True)
class RawEntry:
    slug: str
    name: str
    description: str
    skill_md: Path
    source_root: str
    rel_path: str
    content_hash: str
    folder_files: int
    folder_bytes: int


def slugify(value: str) -> str:
    value = (value or "").strip().lower().replace("_", "-")
    value = re.sub(r"[^a-z0-9-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "skill"


def display_name(slug: str) -> str:
    words = re.split(r"[-_\s]+", slug.strip())
    return " ".join(word.upper() if len(word) <= 3 and word.isalpha() else word.capitalize() for word in words if word)


def split_frontmatter(text: str) -> tuple[str, dict, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "", {}, text
    try:
        data = yaml.safe_load(match.group("frontmatter")) or {}
    except yaml.YAMLError:
        data = {}
    if not isinstance(data, dict):
        data = {}
    return match.group("prefix"), data, match.group("body")


def safe_description(value: object, slug: str) -> str:
    desc = str(value or "").strip().strip('"').strip("'")
    desc = re.sub(r"\s+", " ", desc)
    lowered = desc.lower()
    if not desc or "todo" in lowered or "<skill" in lowered or "brief description" in lowered:
        desc = f"Workflow and reference package for {display_name(slug)} imported from upstream skill bundles."
    return desc[:900].rstrip()


def content_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def folder_stats(folder: Path) -> tuple[int, int]:
    files = 0
    size = 0
    for path in folder.rglob("*"):
        if path.is_file():
            files += 1
            size += path.stat().st_size
    return files, size


def source_root_for(path: Path) -> str:
    parts = {part.lower() for part in path.parts}
    lower = str(path).replace("\\", "/").lower()
    if "_upstreams/antigravity/skills/" in lower:
        return "antigravity-skills"
    if "_upstreams/agent-archive/" in lower:
        return "agent-archive"
    if "_upstreams/main/" in lower:
        return "main"
    if "_upstreams/superpowers/" in lower:
        return "superpowers"
    if "plugins" in parts:
        return "antigravity-plugin"
    return "other"


def source_rank(entry: RawEntry) -> tuple[int, int, int, str]:
    rank = {
        "antigravity-skills": 0,
        "main": 1,
        "superpowers": 2,
        "agent-archive": 3,
        "antigravity-plugin": 4,
        "other": 5,
    }.get(entry.source_root, 9)
    return (rank, -entry.folder_files, -entry.folder_bytes, entry.rel_path)


def iter_canonical_skills(skills_root: Path) -> dict[str, Path]:
    skills: dict[str, Path] = {}
    for path in sorted(skills_root.iterdir()):
        if path.is_dir() and (path / "SKILL.md").exists():
            skills[path.name] = path
    return skills


def iter_raw_entries(bundle_root: Path, upstreams_root: Path) -> list[RawEntry]:
    entries: list[RawEntry] = []
    for skill_md in sorted(upstreams_root.rglob("SKILL.md")):
        text = skill_md.read_text(encoding="utf-8", errors="replace")
        _prefix, data, _body = split_frontmatter(text)
        raw_name = str(data.get("name") or skill_md.parent.name).strip()
        slug = slugify(raw_name)
        desc = safe_description(data.get("description"), slug)
        files, size = folder_stats(skill_md.parent)
        entries.append(RawEntry(
            slug=slug,
            name=raw_name,
            description=desc,
            skill_md=skill_md,
            source_root=source_root_for(skill_md),
            rel_path=str(skill_md.relative_to(bundle_root)),
            content_hash=content_hash(skill_md),
            folder_files=files,
            folder_bytes=size,
        ))
    return entries


def copy_missing_skill(entry: RawEntry, skills_root: Path) -> Path:
    target = skills_root / entry.slug
    if target.exists():
        raise FileExistsError(f"Target already exists: {target}")
    shutil.copytree(entry.skill_md.parent, target)
    normalize_imported_skill(target, entry)
    return target


def normalize_imported_skill(skill_dir: Path, entry: RawEntry) -> None:
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    prefix, data, body = split_frontmatter(text)
    data["name"] = entry.slug
    data["description"] = safe_description(data.get("description"), entry.slug)
    if not body.strip():
        body = f"\n# {display_name(entry.slug)}\n\nUse the bundled references and inherited upstream workflow for this skill.\n"
    dumped = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000).rstrip()
    skill_md.write_text(f"{prefix}---\n{dumped}\n---\n\n{body.lstrip()}", encoding="utf-8")


def write_provenance(skill_dir: Path, selected: RawEntry, variants: list[RawEntry]) -> None:
    references = skill_dir / "references"
    references.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Upstream Provenance",
        "",
        f"Canonical skill: `{selected.slug}`",
        f"Selected source copied into this skill: `{selected.rel_path}`",
        "",
        "## Raw Upstream Entries Mapped",
        "",
    ]
    for entry in sorted(variants, key=lambda item: item.rel_path):
        marker = "selected" if entry.rel_path == selected.rel_path else "mapped"
        lines.append(f"- `{entry.rel_path}` ({entry.source_root}, {entry.folder_files} files, {entry.folder_bytes} bytes, {marker})")
    lines.extend([
        "",
        "## Coverage Rule",
        "",
        "This bundle deduplicates raw upstream SKILL.md files by normalized skill slug. Duplicate raw entries stay represented by this canonical skill instead of being inflated into duplicate folders.",
        "",
    ])
    (references / "upstream-provenance.md").write_text("\n".join(lines), encoding="utf-8")

    distinct_variants: dict[str, RawEntry] = {}
    for entry in sorted(variants, key=lambda item: source_rank(item)):
        distinct_variants.setdefault(entry.content_hash, entry)
    if len(distinct_variants) <= 1:
        return

    variant_lines = [
        "# Distinct Upstream Skill Variants",
        "",
        "Use this only when auditing upstream merge fidelity. The active runtime instructions remain in `SKILL.md`; these sections preserve distinct upstream wording for review.",
        "",
    ]
    for idx, entry in enumerate(distinct_variants.values(), start=1):
        text = entry.skill_md.read_text(encoding="utf-8", errors="replace").rstrip()
        variant_lines.extend([
            f"## Variant {idx}: `{entry.rel_path}`",
            "",
            "```markdown",
            text,
            "```",
            "",
        ])
    (references / "upstream-variants.md").write_text("\n".join(variant_lines), encoding="utf-8")


def build_coverage_report(
    bundle_root: Path,
    skills_root: Path,
    raw_entries: list[RawEntry],
    imported: list[dict],
) -> dict:
    canonical = iter_canonical_skills(skills_root)
    grouped: dict[str, list[RawEntry]] = defaultdict(list)
    for entry in raw_entries:
        grouped[entry.slug].append(entry)

    raw_slugs = set(grouped)
    canonical_slugs = set(canonical)
    missing = sorted(raw_slugs - canonical_slugs)
    represented = sorted(raw_slugs & canonical_slugs)
    duplicate_groups = {slug: entries for slug, entries in grouped.items() if len(entries) > 1}
    source_counts = Counter(entry.source_root for entry in raw_entries)
    uncovered_entries = [entry.rel_path for entry in raw_entries if entry.slug not in canonical_slugs]

    return {
        "bundleRoot": str(bundle_root),
        "skillsRoot": str(skills_root),
        "rawSkillMd": len(raw_entries),
        "uniqueRawSlugs": len(raw_slugs),
        "canonicalSkillDirs": len(canonical_slugs),
        "representedRawSlugs": len(represented),
        "missingUniqueRawSlugs": len(missing),
        "missingSlugs": missing,
        "rawEntriesCovered": len(raw_entries) - len(uncovered_entries),
        "rawEntriesUncovered": len(uncovered_entries),
        "uncoveredRawEntries": uncovered_entries[:200],
        "duplicateRawSlugGroups": len(duplicate_groups),
        "duplicateRawEntries": len(raw_entries) - len(raw_slugs),
        "sourceCounts": dict(sorted(source_counts.items())),
        "importedThisRun": imported,
        "canonicalExtraSlugs": sorted(canonical_slugs - raw_slugs)[:200],
        "canonicalExtraSlugCount": len(canonical_slugs - raw_slugs),
        "allRawEntriesMapped": not missing and not uncovered_entries,
        "dedupeRule": "Raw upstream SKILL.md files are deduplicated by normalized frontmatter/folder slug so duplicate marketplace/plugin copies map to one canonical skill.",
    }


def render_coverage_markdown(report: dict) -> str:
    lines = [
        "# Upstream Raw Skill Coverage",
        "",
        "This report proves coverage against the raw upstream archives without inflating duplicate marketplace/plugin copies into fake unique skills.",
        "",
        "## Metrics",
        "",
        f"- Raw upstream `SKILL.md` files: {report['rawSkillMd']}",
        f"- Unique raw skill slugs: {report['uniqueRawSlugs']}",
        f"- Canonical skill folders: {report['canonicalSkillDirs']}",
        f"- Represented raw slugs: {report['representedRawSlugs']} / {report['uniqueRawSlugs']}",
        f"- Missing unique raw slugs: {report['missingUniqueRawSlugs']}",
        f"- Raw entries covered by canonical skills: {report['rawEntriesCovered']} / {report['rawSkillMd']}",
        f"- Duplicate raw slug groups: {report['duplicateRawSlugGroups']}",
        f"- Duplicate raw entries deduplicated: {report['duplicateRawEntries']}",
        f"- All raw entries mapped: {'yes' if report['allRawEntriesMapped'] else 'no'}",
        "",
        "## Source Counts",
        "",
    ]
    for source, count in report["sourceCounts"].items():
        lines.append(f"- `{source}`: {count}")

    lines.extend([
        "",
        "## Import Pass",
        "",
    ])
    if report["importedThisRun"]:
        for item in report["importedThisRun"]:
            lines.append(f"- `{item['slug']}` from `{item['selectedSource']}` ({item['rawEntryCount']} raw entries mapped)")
    else:
        lines.append("- No missing unique slugs remained to import in this run.")

    lines.extend([
        "",
        "## Missing Slugs",
        "",
    ])
    if report["missingSlugs"]:
        for slug in report["missingSlugs"]:
            lines.append(f"- `{slug}`")
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Deduplication Rule",
        "",
        report["dedupeRule"],
        "",
    ])
    return "\n".join(lines)


def import_missing(bundle_root: Path, skills_root: Path, raw_entries: list[RawEntry]) -> list[dict]:
    canonical = iter_canonical_skills(skills_root)
    grouped: dict[str, list[RawEntry]] = defaultdict(list)
    for entry in raw_entries:
        grouped[entry.slug].append(entry)

    imported: list[dict] = []
    for slug in sorted(set(grouped) - set(canonical)):
        variants = grouped[slug]
        selected = sorted(variants, key=source_rank)[0]
        target = copy_missing_skill(selected, skills_root)
        write_provenance(target, selected, variants)
        imported.append({
            "slug": slug,
            "target": str(target),
            "selectedSource": selected.rel_path,
            "rawEntryCount": len(variants),
            "variantSources": [entry.rel_path for entry in sorted(variants, key=lambda item: item.rel_path)],
        })
    return imported


def main() -> int:
    parser = argparse.ArgumentParser(description="Import missing unique upstream skills and emit raw coverage reports.")
    parser.add_argument("--bundle-root", default=None)
    parser.add_argument("--skills-root", default=None)
    parser.add_argument("--upstreams-root", default=None)
    parser.add_argument("--reports-dir", default=None)
    parser.add_argument("--report-only", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    default_skills_root = script_dir.parent.parent
    default_bundle_root = default_skills_root.parent.parent
    bundle_root = Path(args.bundle_root).resolve() if args.bundle_root else default_bundle_root
    skills_root = Path(args.skills_root).resolve() if args.skills_root else default_skills_root
    upstreams_root = Path(args.upstreams_root).resolve() if args.upstreams_root else bundle_root / "_upstreams"
    reports_dir = Path(args.reports_dir).resolve() if args.reports_dir else bundle_root / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    json_path = reports_dir / "upstream-raw-skill-coverage.json"
    md_path = bundle_root / "UPSTREAM_RAW_SKILL_COVERAGE.md"

    previous_imported: list[dict] = []
    if json_path.exists():
        try:
            previous = json.loads(json_path.read_text(encoding="utf-8"))
            if isinstance(previous.get("importedThisRun"), list):
                previous_imported = previous["importedThisRun"]
        except (json.JSONDecodeError, OSError):
            previous_imported = []

    raw_entries = iter_raw_entries(bundle_root, upstreams_root)
    imported = [] if args.report_only else import_missing(bundle_root, skills_root, raw_entries)
    report = build_coverage_report(bundle_root, skills_root, raw_entries, imported)
    if not imported and previous_imported:
        report["importedThisRun"] = previous_imported
        report["importedThisRunPreservedFromPreviousRun"] = True

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_path.write_text(render_coverage_markdown(report), encoding="utf-8")

    print(f"Imported {len(imported)} missing unique upstream skills")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"All raw entries mapped: {report['allRawEntriesMapped']}")
    return 0 if report["allRawEntriesMapped"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
