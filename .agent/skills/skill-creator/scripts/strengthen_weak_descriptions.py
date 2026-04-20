#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


FRONTMATTER_RE = re.compile(
    r"^(?P<prefix>\ufeff?\s*)---\s*\r?\n(?P<frontmatter>.*?)\r?\n---\s*(?P<body>.*)$",
    re.DOTALL,
)

PLACEHOLDER_MARKERS = (
    "replace with description",
    "insert instructions below",
    "brief description of the skill",
    "<skill",
)


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


def normalize(value: str) -> str:
    value = value.lower().replace("_", "-")
    value = re.sub(r"[^a-z0-9-]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def description_tail(description: str) -> str:
    match = re.match(r"ALWAYS use this when the request matches [^:]+:\s*(.*)", description, re.IGNORECASE)
    return match.group(1).strip() if match else description.strip()


def is_weak_description(name: str, description: str) -> bool:
    tail = description_tail(description)
    lowered = tail.lower()
    if any(marker in lowered for marker in PLACEHOLDER_MARKERS):
        return True
    if len(tail) < 35:
        return True
    if normalize(tail) == normalize(name):
        return True
    if tail.lower() in {"build", "readme", "base", "calc", "draw", "writer", "impress"}:
        return True
    return False


def scope_sentence(name: str, old_tail: str) -> str:
    label = display_name(name)
    useful_tail = old_tail.strip().strip(".")
    if not useful_tail or len(useful_tail) < 8 or normalize(useful_tail) == normalize(name):
        useful_tail = f"{label} work"
    if any(marker in useful_tail.lower() for marker in PLACEHOLDER_MARKERS):
        useful_tail = f"{label} work"
    return (
        f"ALWAYS use this when the user mentions {label}, asks to build, debug, review, document, automate, test, "
        f"configure, migrate, or make decisions in this domain, or the task clearly depends on {label}; "
        f"scope: {useful_tail}. Apply the bundled workflow, references, scripts, Senior Master standard, and Codex strict review gate before final output."
    )


def strengthen(skills_root: Path) -> dict:
    report = {
        "skillsRoot": str(skills_root),
        "skillsSeen": 0,
        "descriptionsStrengthened": 0,
        "updatedSkills": [],
        "errors": [],
    }
    for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir() and (path / "SKILL.md").exists()):
        report["skillsSeen"] += 1
        skill_md = skill_dir / "SKILL.md"
        try:
            text = skill_md.read_text(encoding="utf-8", errors="replace")
            prefix, data, body = split_frontmatter(text)
            name = str(data.get("name") or skill_dir.name).strip() or skill_dir.name
            description = str(data.get("description") or "").strip()
            if not is_weak_description(name, description):
                continue
            old_tail = description_tail(description)
            data["description"] = scope_sentence(name, old_tail)
            dumped = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000).rstrip()
            skill_md.write_text(f"{prefix}---\n{dumped}\n---\n\n{body.lstrip()}", encoding="utf-8")
            report["descriptionsStrengthened"] += 1
            report["updatedSkills"].append({
                "skill": skill_dir.name,
                "oldTail": old_tail,
                "newDescription": data["description"],
            })
        except Exception as exc:  # noqa: BLE001 - report all per-skill failures for bundle repair.
            report["errors"].append({"skill": skill_dir.name, "message": str(exc)})
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Strengthen weak skill descriptions without touching already-rich triggers.")
    parser.add_argument("skills_root", nargs="?", default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    default_skills_root = script_dir.parent.parent
    skills_root = Path(args.skills_root).resolve() if args.skills_root else default_skills_root
    output_path = Path(args.output).resolve() if args.output else skills_root.parent.parent / "reports" / "weak-description-strengthening.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    report = strengthen(skills_root)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
