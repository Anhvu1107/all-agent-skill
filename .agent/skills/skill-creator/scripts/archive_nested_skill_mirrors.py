#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


def mirror_name(relative_path: Path) -> str:
    parts = list(relative_path.parts[:-1])
    stem = "-".join(parts)
    stem = re.sub(r"[^a-zA-Z0-9._-]+", "-", stem).strip("-") or "nested-skill"
    return f"{stem}.md"


def archive_nested_skill_md(skills_root: Path) -> dict:
    report = {
        "skillsRoot": str(skills_root),
        "nestedSkillMdFound": 0,
        "nestedSkillMdArchived": 0,
        "archived": [],
        "errors": [],
    }
    for skill_md in sorted(skills_root.rglob("SKILL.md")):
        rel = skill_md.relative_to(skills_root)
        if len(rel.parts) == 2:
            continue
        report["nestedSkillMdFound"] += 1
        owner = skills_root / rel.parts[0]
        references = owner / "references" / "nested-skill-mirrors"
        references.mkdir(parents=True, exist_ok=True)
        target = references / mirror_name(rel)
        try:
            if target.exists():
                existing = target.read_text(encoding="utf-8", errors="replace")
                incoming = skill_md.read_text(encoding="utf-8", errors="replace")
                if existing != incoming:
                    index = 2
                    while (references / f"{target.stem}-{index}.md").exists():
                        index += 1
                    target = references / f"{target.stem}-{index}.md"
            shutil.move(str(skill_md), str(target))
            report["nestedSkillMdArchived"] += 1
            report["archived"].append({
                "from": str(rel).replace("\\", "/"),
                "to": str(target.relative_to(owner)).replace("\\", "/"),
            })
        except Exception as exc:  # noqa: BLE001 - report all failures.
            report["errors"].append({"path": str(rel), "message": str(exc)})
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Archive nested SKILL.md mirrors so only direct runtime skills remain.")
    parser.add_argument("skills_root", nargs="?", default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    skills_root = Path(args.skills_root).resolve() if args.skills_root else script_dir.parent.parent
    output = Path(args.output).resolve() if args.output else skills_root.parent.parent / "reports" / "nested-skill-mirror-archive.json"
    output.parent.mkdir(parents=True, exist_ok=True)

    report = archive_nested_skill_md(skills_root)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
