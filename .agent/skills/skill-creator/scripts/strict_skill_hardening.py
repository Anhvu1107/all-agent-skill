#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

import yaml


FRONTMATTER_RE = re.compile(
    r"^(?P<prefix>\ufeff?\s*)---\s*\r?\n(?P<frontmatter>.*?)\r?\n---\s*(?P<body>.*)$",
    re.DOTALL,
)

PALETTE = [
    "#0F172A",
    "#1D4ED8",
    "#0F766E",
    "#7C3AED",
    "#B91C1C",
    "#EA580C",
    "#15803D",
    "#374151",
    "#BE123C",
    "#2563EB",
]


def split_frontmatter(text: str) -> tuple[str, dict, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("SKILL.md has no parseable frontmatter")
    data = yaml.safe_load(match.group("frontmatter")) or {}
    if not isinstance(data, dict):
        raise ValueError("Frontmatter is not a mapping")
    return match.group("prefix"), data, match.group("body")


def display_name(name: str) -> str:
    words = re.split(r"[-_\s]+", name.strip())
    return " ".join(word.upper() if len(word) <= 3 and word.isalpha() else word.capitalize() for word in words if word)


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def short_description(description: str, limit: int = 150) -> str:
    description = re.sub(r"\s+", " ", str(description or "").strip())
    first = re.split(r"(?<=[.!?])\s+", description)[0]
    if len(first) > limit:
        first = first[: limit - 1].rstrip(" ,.;:") + "..."
    return first


def brand_color(name: str) -> str:
    digest = hashlib.sha256(name.encode("utf-8")).digest()[0]
    return PALETTE[digest % len(PALETTE)]


def write_openai_yaml(skill_dir: Path, name: str, description: str) -> bool:
    target = skill_dir / "agents" / "openai.yaml"
    target.parent.mkdir(parents=True, exist_ok=True)
    label = display_name(name)
    content = "\n".join([
        "interface:",
        f"  display_name: {yaml_quote(label)}",
        f"  short_description: {yaml_quote(short_description(description))}",
        f"  brand_color: {yaml_quote(brand_color(name))}",
        f"  default_prompt: {yaml_quote(f'Use ${name} to handle this task with the relevant workflow, references, scripts, and quality checks.')}",
        "",
        "policy:",
        "  allow_implicit_invocation: true",
        "",
    ])
    old = target.read_text(encoding="utf-8", errors="replace") if target.exists() else ""
    if old == content:
        return False
    target.write_text(content, encoding="utf-8")
    return True


def safe_reference_name(name: str, used: set[str]) -> str:
    stem = Path(name).stem.lower()
    stem = re.sub(r"[^a-z0-9-]+", "-", stem).strip("-") or "root-doc"
    candidate = f"legacy-{stem}.md"
    index = 2
    while candidate in used:
        candidate = f"legacy-{stem}-{index}.md"
        index += 1
    used.add(candidate)
    return candidate


def replace_markdown_links(text: str, mapping: dict[str, str], prefix: str) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        if "://" in target or target.startswith("#"):
            return match.group(0)
        normalized = target.replace("\\", "/")
        if normalized.startswith("./"):
            normalized = normalized[2:]
        if "/" in normalized:
            return match.group(0)
        replacement = mapping.get(normalized.lower())
        if not replacement:
            return match.group(0)
        return f"({prefix}{replacement})"

    return re.sub(r"\(([^)]+\.md)\)", repl, text)


def move_root_markdown_docs(skill_dir: Path, body: str) -> tuple[str, dict[str, str], int]:
    root = skill_dir.resolve()
    references = (skill_dir / "references").resolve()
    references.mkdir(parents=True, exist_ok=True)
    used = {path.name for path in references.glob("*.md")}
    mapping: dict[str, str] = {}
    moved = 0

    for doc in sorted(skill_dir.glob("*.md")):
        if doc.name.lower() == "skill.md":
            continue
        source = doc.resolve()
        if not str(source).lower().startswith(str(root).lower()):
            raise ValueError(f"Refusing to move outside skill root: {source}")
        target_name = safe_reference_name(doc.name, used)
        target = (references / target_name).resolve()
        if not str(target).lower().startswith(str(references).lower()):
            raise ValueError(f"Refusing to move outside references: {target}")
        shutil.move(str(source), str(target))
        mapping[doc.name.lower()] = target_name
        moved += 1

    if not mapping:
        return body, mapping, moved

    body = replace_markdown_links(body, mapping, "references/")
    for ref in sorted(references.glob("*.md")):
        text = ref.read_text(encoding="utf-8", errors="replace")
        updated = replace_markdown_links(text, mapping, "")
        if updated != text:
            ref.write_text(updated, encoding="utf-8")
    return body, mapping, moved


def write_frontmatter_metadata(skill_dir: Path, extra: dict) -> None:
    references = skill_dir / "references"
    references.mkdir(parents=True, exist_ok=True)
    target = references / "frontmatter-metadata.md"
    content = [
        "# Frontmatter Metadata Archive",
        "",
        "This file preserves upstream metadata moved out of `SKILL.md` so the runtime frontmatter stays strict: `name` and `description` only.",
        "",
        "```yaml",
        yaml.safe_dump(extra, sort_keys=False, allow_unicode=True, width=1000).rstrip(),
        "```",
        "",
    ]
    target.write_text("\n".join(content), encoding="utf-8")


def compact_long_body(skill_dir: Path, name: str, body: str, mapping: dict[str, str]) -> tuple[str, bool]:
    if len(body.splitlines()) <= 500:
        return body, False
    if "references/full-skill-instructions.md" in body and len(body.splitlines()) <= 80:
        return body, False

    references = skill_dir / "references"
    references.mkdir(parents=True, exist_ok=True)
    body_for_reference = replace_markdown_links(body.rstrip(), mapping, "")
    full_path = references / "full-skill-instructions.md"
    full_path.write_text(
        "\n".join([
            "# Full Skill Instructions",
            "",
            f"This file preserves the full pre-compaction `SKILL.md` body for `{name}`.",
            "",
            "Load this file only when the task requires detailed domain guidance beyond the quick routing contract in `SKILL.md`.",
            "",
            "## Preserved Body",
            "",
            body_for_reference,
            "",
        ]),
        encoding="utf-8",
    )

    title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else display_name(name)
    compact = f"""# {title}

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, examples, or detailed instructions that match the user's actual task.

## Progressive Disclosure

- Read `references/full-skill-instructions.md` only when the task needs the full original upstream guidance.
- Prefer bundled scripts for deterministic or repetitive operations when they exist.
- Reuse bundled assets instead of inventing substitutes when assets are present.
- Keep final answers aligned with this skill's frontmatter trigger, Senior Master standard, and Codex strict review gate.
"""
    return compact, True


def harden_skill(skill_dir: Path) -> dict:
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    prefix, data, body = split_frontmatter(text)
    name = str(data.get("name") or skill_dir.name).strip() or skill_dir.name
    description = str(data.get("description") or "").strip()
    if name != skill_dir.name:
        name = skill_dir.name

    extra = {key: value for key, value in data.items() if key not in {"name", "description"}}
    if extra:
        write_frontmatter_metadata(skill_dir, extra)

    body, mapping, moved_docs = move_root_markdown_docs(skill_dir, body)
    body, compacted = compact_long_body(skill_dir, name, body, mapping)

    strict_data = {"name": name, "description": description}
    dumped = yaml.safe_dump(strict_data, sort_keys=False, allow_unicode=True, width=1000).rstrip()
    skill_md.write_text(f"{prefix}---\n{dumped}\n---\n\n{body.lstrip()}", encoding="utf-8")

    agent_changed = write_openai_yaml(skill_dir, name, description)

    return {
        "skill": skill_dir.name,
        "extraFrontmatterArchived": bool(extra),
        "extraFrontmatterKeys": sorted(extra),
        "rootMarkdownDocsMoved": moved_docs,
        "longBodyCompacted": compacted,
        "agentMetadataRefreshed": agent_changed,
    }


def harden(skills_root: Path) -> dict:
    report = {
        "skillsRoot": str(skills_root),
        "skillsSeen": 0,
        "extraFrontmatterArchived": 0,
        "rootMarkdownDocsMoved": 0,
        "longBodiesCompacted": 0,
        "agentMetadataRefreshed": 0,
        "updatedSkills": [],
        "errors": [],
    }
    for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir() and (path / "SKILL.md").exists()):
        report["skillsSeen"] += 1
        try:
            result = harden_skill(skill_dir)
            if result["extraFrontmatterArchived"]:
                report["extraFrontmatterArchived"] += 1
            report["rootMarkdownDocsMoved"] += result["rootMarkdownDocsMoved"]
            if result["longBodyCompacted"]:
                report["longBodiesCompacted"] += 1
            if result["agentMetadataRefreshed"]:
                report["agentMetadataRefreshed"] += 1
            if (
                result["extraFrontmatterArchived"]
                or result["rootMarkdownDocsMoved"]
                or result["longBodyCompacted"]
                or result["agentMetadataRefreshed"]
            ):
                report["updatedSkills"].append(result)
        except Exception as exc:  # noqa: BLE001 - keep bundle-level repair running and report per-skill failures.
            report["errors"].append({"skill": skill_dir.name, "message": str(exc)})
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply strict skill-creator hardening across a skill bundle.")
    parser.add_argument("skills_root", nargs="?", default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    default_skills_root = script_dir.parent.parent
    skills_root = Path(args.skills_root).resolve() if args.skills_root else default_skills_root
    output_path = Path(args.output).resolve() if args.output else skills_root.parent.parent / "reports" / "strict-skill-hardening.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    report = harden(skills_root)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
