#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import yaml


TRIGGER_MARKERS = (
    "use when",
    "whenever the user",
    "trigger when",
    "trigger whenever",
    "always use",
    "use this skill whenever",
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


def split_frontmatter(text: str) -> tuple[str, str, str]:
    match = re.match(r"^(?P<prefix>\ufeff?\s*)---\s*\r?\n(?P<frontmatter>.*?)\r?\n---\s*(?P<body>.*)$", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md has no parseable frontmatter")
    return match.group("prefix"), match.group("frontmatter"), match.group("body")


def clean_description(value: object, fallback: str) -> str:
    desc = str(value or "").strip().strip('"').strip("'")
    desc = re.sub(r"\s+", " ", desc)
    if not desc or desc == ">":
        desc = f"Guidance and workflow support for {fallback}."
    return desc


def display_name(name: str) -> str:
    words = re.split(r"[-_\s]+", name.strip())
    return " ".join(word.upper() if len(word) <= 3 and word.isalpha() else word.capitalize() for word in words if word)


def short_description(desc: str, fallback_name: str, limit: int = 150) -> str:
    desc = clean_description(desc, fallback_name)
    first = re.split(r"(?<=[.!?])\s+", desc)[0]
    if len(first) > limit:
        first = first[: limit - 1].rstrip(" ,.;:") + "..."
    return first


def is_trigger_forward(desc: str) -> bool:
    lower = desc.lower()
    return any(marker in lower for marker in TRIGGER_MARKERS)


def is_pushy(desc: str) -> bool:
    lower = desc.lower()
    return "always use this" in lower or "always use " in lower or "trigger whenever" in lower


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def brand_color(name: str) -> str:
    digest = hashlib.sha256(name.encode("utf-8")).digest()[0]
    return PALETTE[digest % len(PALETTE)]


def write_openai_yaml(skill_dir: Path, name: str, desc: str) -> bool:
    target = skill_dir / "agents" / "openai.yaml"
    if target.exists():
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    label = display_name(name)
    short = short_description(desc, label)
    content = "\n".join([
        "interface:",
        f"  display_name: {yaml_quote(label)}",
        f"  short_description: {yaml_quote(short)}",
        f"  brand_color: {yaml_quote(brand_color(name))}",
        f"  default_prompt: {yaml_quote(f'Use ${name} to handle this task with the relevant workflow, references, scripts, and quality checks.')}",
        "",
        "policy:",
        "  allow_implicit_invocation: true",
        "",
    ])
    target.write_text(content, encoding="utf-8")
    return True


def root_markdown_docs(skill_dir: Path) -> list[str]:
    return sorted(path.name for path in skill_dir.glob("*.md") if path.name.lower() != "skill.md")


def write_reference_wrappers(skill_dir: Path, name: str, desc: str) -> bool:
    references_dir = skill_dir / "references"
    references_dir.mkdir(parents=True, exist_ok=True)
    docs = root_markdown_docs(skill_dir)
    has_scripts = (skill_dir / "scripts").exists()
    has_assets = (skill_dir / "assets").exists()

    docs_line = ", ".join(f"`{doc}`" for doc in docs[:12]) if docs else "No root markdown companion docs were present when this wrapper was generated."
    scripts_line = "Use `scripts/` for repeatable or deterministic work when present." if has_scripts else "No bundled scripts were present when this wrapper was generated."
    assets_line = "Use `assets/` as output resources or examples when present." if has_assets else "No bundled assets were present when this wrapper was generated."
    trigger = clean_description(desc, display_name(name))

    changed = False
    usage_path = references_dir / "usage-routing.md"
    quality_path = references_dir / "quality-checklist.md"

    if not usage_path.exists():
        usage_path.write_text(f"""# Usage Routing

Use this file before doing substantive work with `{name}`.

## Trigger Summary

{trigger}

## Start Here

- Read `SKILL.md` first for the inherited operating instructions.
- Load only the root docs or bundled resources that match the user's task.
- Root markdown docs found at generation time: {docs_line}
- {scripts_line}
- {assets_line}

## Scope Control

- Keep the skill's original domain boundaries intact.
- Do not turn a narrow tool skill into a general-purpose answer.
- If the request touches legal, medical, security, finance, privacy, or production systems, surface uncertainty and verify with authoritative sources or local evidence.
""", encoding="utf-8")
        changed = True

    if not quality_path.exists():
        quality_path.write_text(f"""# Quality Checklist

Use this before calling work with `{name}` complete.

## Checks

- Confirm the request actually matches this skill's trigger and domain.
- Load only the supporting files needed for the current task.
- If scripts exist, prefer running or adapting them over recreating fragile logic by hand.
- If assets exist, reuse them rather than inventing substitute assets.
- State what was verified and what remains uncertain.

## Reviewer Traps

- Claiming the skill was used while ignoring its bundled resources.
- Loading every file instead of using progressive disclosure.
- Making broad promises outside the skill's actual scope.
""", encoding="utf-8")
        changed = True

    return changed


def insert_selective_reading(skill_md: Path) -> bool:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if "references/usage-routing.md" in text:
        return False
    prefix, frontmatter, body = split_frontmatter(text)
    body = body.lstrip("\r\n")
    block = (
        "## Selective Reading Rule\n\n"
        "Start with:\n\n"
        "- `references/usage-routing.md`\n"
        "- `references/quality-checklist.md`\n\n"
        "Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.\n\n"
    )
    heading = re.match(r"(# .+?\r?\n+)", body)
    if heading:
        insert_at = heading.end()
        body = body[:insert_at] + block + body[insert_at:]
    else:
        body = block + body
    skill_md.write_text(f"{prefix}---\n{frontmatter.rstrip()}\n---\n\n{body}", encoding="utf-8")
    return True


def normalize_description(skill_md: Path, name: str, data: dict) -> bool:
    desc = clean_description(data.get("description"), display_name(name))
    if is_pushy(desc):
        return False
    short = short_description(desc, display_name(name), limit=720)
    data["description"] = f"ALWAYS use this when the request matches {display_name(name)}: {short}"

    text = skill_md.read_text(encoding="utf-8", errors="replace")
    prefix, _frontmatter, body = split_frontmatter(text)
    dumped = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000).rstrip()
    skill_md.write_text(f"{prefix}---\n{dumped}\n---\n\n{body.lstrip()}", encoding="utf-8")
    return True


def complete_bundle(skills_root: Path) -> dict:
    results = {
        "skillsRoot": str(skills_root),
        "skillsSeen": 0,
        "agentsCreated": 0,
        "referenceWrappersCreated": 0,
        "selectiveReadingInserted": 0,
        "descriptionsNormalized": 0,
        "errors": [],
    }

    for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir() and (path / "SKILL.md").exists()):
        skill_md = skill_dir / "SKILL.md"
        results["skillsSeen"] += 1
        try:
            text = skill_md.read_text(encoding="utf-8", errors="replace")
            _prefix, frontmatter, _body = split_frontmatter(text)
            data = yaml.safe_load(frontmatter) or {}
            name = str(data.get("name") or skill_dir.name)
            desc = clean_description(data.get("description"), display_name(name))

            if write_openai_yaml(skill_dir, name, desc):
                results["agentsCreated"] += 1

            created_refs = write_reference_wrappers(skill_dir, name, desc)
            if created_refs:
                results["referenceWrappersCreated"] += 1

            if created_refs and insert_selective_reading(skill_md):
                results["selectiveReadingInserted"] += 1

            # Re-read frontmatter after body insertion before changing metadata.
            text = skill_md.read_text(encoding="utf-8", errors="replace")
            _prefix, frontmatter, _body = split_frontmatter(text)
            data = yaml.safe_load(frontmatter) or {}
            if normalize_description(skill_md, name, data):
                results["descriptionsNormalized"] += 1
        except Exception as exc:  # Keep the pass auditable instead of stopping halfway.
            results["errors"].append({"skill": skill_dir.name, "error": str(exc)})

    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Complete mechanical progressive-disclosure and metadata gaps across a skill bundle.")
    parser.add_argument("skills_root", help="Path to .agent/skills")
    parser.add_argument("--output", default=None, help="Optional JSON report path")
    args = parser.parse_args()

    result = complete_bundle(Path(args.skills_root).resolve())
    if args.output:
        output = Path(args.output).resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
