#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml


FRONTMATTER_RE = re.compile(
    r"^\ufeff?\s*---\s*\r?\n(?P<frontmatter>.*?)\r?\n---\s*(?P<body>.*)$",
    re.DOTALL,
)


def split_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    try:
        data = yaml.safe_load(match.group("frontmatter")) or {}
    except yaml.YAMLError:
        data = {}
    return data if isinstance(data, dict) else {}, match.group("body")


def first_heading(body: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def detect_alias_target(skill_dir: Path) -> str | None:
    alias_ref = skill_dir / "references" / "alias-target.md"
    if not alias_ref.exists():
        return None
    text = alias_ref.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"alias for canonical skill `([^`]+)`", text)
    return match.group(1) if match else None


def infer_category(slug: str, alias_target: str | None) -> str:
    source = alias_target or slug
    if source.startswith(("game-", "2d-", "3d-", "mobile-games", "pc-games", "vr-ar", "web-games", "multiplayer")):
        return "Game Development"
    if source.startswith(("aws-", "security-", "vulnerability", "xss", "idor", "red-team", "penetration", "privilege")):
        return "Security"
    if source.startswith(("libreoffice", "base", "calc", "draw", "impress", "writer", "doc", "pdf", "xlsx", "ppt")):
        return "Documents And Office"
    if any(marker in source for marker in ("react", "vue", "nextjs", "svelte", "astro", "frontend", "ui", "ux", "tailwind", "expo")):
        return "Frontend And UX"
    if any(marker in source for marker in ("python", "node", "api", "database", "postgres", "backend", "rust", "java", "dotnet")):
        return "Backend And Engineering"
    if any(marker in source for marker in ("workflow", "orchestr", "agent", "review", "debug", "tdd", "test", "eval")):
        return "Agent Workflow And Quality"
    if any(marker in source for marker in ("medical", "health", "legal", "law", "seo", "marketing", "finance")):
        return "Specialized Domains"
    return "General"


def build_entries(bundle_root: Path) -> list[dict]:
    skills_root = bundle_root / ".agent" / "skills"
    entries: list[dict] = []
    for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir() and (path / "SKILL.md").exists()):
        data, body = split_frontmatter(skill_dir / "SKILL.md")
        slug = skill_dir.name
        name = str(data.get("name") or slug)
        description = str(data.get("description") or "")
        alias_target = detect_alias_target(skill_dir)
        references = sorted(str(path.relative_to(skill_dir)).replace("\\", "/") for path in (skill_dir / "references").glob("*.md")) if (skill_dir / "references").exists() else []
        scripts = sorted(str(path.relative_to(skill_dir)).replace("\\", "/") for path in (skill_dir / "scripts").rglob("*") if path.is_file()) if (skill_dir / "scripts").exists() else []
        assets = sorted(str(path.relative_to(skill_dir)).replace("\\", "/") for path in (skill_dir / "assets").rglob("*") if path.is_file()) if (skill_dir / "assets").exists() else []
        entries.append({
            "slug": slug,
            "name": name,
            "title": first_heading(body, slug),
            "description": description,
            "category": infer_category(slug, alias_target),
            "path": f".agent/skills/{slug}/SKILL.md",
            "aliasTarget": alias_target,
            "isAlias": alias_target is not None,
            "hasAgents": (skill_dir / "agents" / "openai.yaml").exists(),
            "references": references,
            "scripts": scripts,
            "assets": assets,
            "searchText": " ".join([
                slug,
                name,
                first_heading(body, slug),
                description,
                alias_target or "",
                " ".join(references[:20]),
                " ".join(scripts[:20]),
            ]).lower(),
        })
    return entries


def render_catalog(entries: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        grouped[entry["category"]].append(entry)

    lines = [
        "# Agent Skills VVIP Pro Max Ultra Catalog",
        "",
        "Generated from `.agent/skills`. Use `search-index.json` for machine search and this file for human review.",
        "",
        f"- Total runtime skill entries: {len(entries)}",
        f"- Canonical skills: {sum(1 for entry in entries if not entry['isAlias'])}",
        f"- Namespace/path alias skills: {sum(1 for entry in entries if entry['isAlias'])}",
        "",
        "## Review Notes",
        "",
        "- Alias skills preserve nested ZIP path slugs without duplicating large skill bodies.",
        "- Full long-form instructions, when needed, live in `references/full-skill-instructions.md`.",
        "- Upstream metadata moved out of strict frontmatter lives in `references/frontmatter-metadata.md`.",
        "",
    ]
    for category in sorted(grouped):
        lines.append(f"## {category}")
        lines.append("")
        for entry in sorted(grouped[category], key=lambda item: item["slug"]):
            alias = f" -> `{entry['aliasTarget']}`" if entry["isAlias"] else ""
            desc = entry["description"]
            if len(desc) > 220:
                desc = desc[:217].rstrip(" ,.;:") + "..."
            lines.append(f"- `{entry['slug']}`{alias}: {desc}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build root CATALOG.md and search-index.json for the release package.")
    parser.add_argument("--bundle-root", default=".")
    args = parser.parse_args()

    bundle_root = Path(args.bundle_root).resolve()
    entries = build_entries(bundle_root)
    (bundle_root / "CATALOG.md").write_text(render_catalog(entries), encoding="utf-8")
    (bundle_root / "search-index.json").write_text(json.dumps({
        "bundle": "agent-skills-vvip-pro-max-ultra",
        "total": len(entries),
        "canonical": sum(1 for entry in entries if not entry["isAlias"]),
        "aliases": sum(1 for entry in entries if entry["isAlias"]),
        "entries": entries,
    }, indent=2), encoding="utf-8")
    ndjson = "\n".join(json.dumps(entry, ensure_ascii=False) for entry in entries) + "\n"
    (bundle_root / "search-index.ndjson").write_text(ndjson, encoding="utf-8")
    reports = bundle_root / "reports"
    reports.mkdir(exist_ok=True)
    (reports / "catalog-index-summary.json").write_text(json.dumps({
        "total": len(entries),
        "canonical": sum(1 for entry in entries if not entry["isAlias"]),
        "aliases": sum(1 for entry in entries if entry["isAlias"]),
        "catalogPath": "CATALOG.md",
        "searchIndexPath": "search-index.json",
        "ndjsonPath": "search-index.ndjson",
    }, indent=2), encoding="utf-8")
    print(f"Wrote {bundle_root / 'CATALOG.md'}")
    print(f"Wrote {bundle_root / 'search-index.json'}")
    print(f"Wrote {bundle_root / 'search-index.ndjson'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
