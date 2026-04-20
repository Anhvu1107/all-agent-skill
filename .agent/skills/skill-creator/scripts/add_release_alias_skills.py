#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


ALIASES = {
    "app-builder-templates": "templates",
    "game-development-2d-games": "2d-games",
    "game-development-3d-games": "3d-games",
    "game-development-game-art": "game-art",
    "game-development-game-audio": "game-audio",
    "game-development-game-design": "game-design",
    "game-development-mobile-games": "mobile-games",
    "game-development-multiplayer": "multiplayer",
    "game-development-pc-games": "pc-games",
    "game-development-vr-ar": "vr-ar",
    "game-development-web-games": "web-games",
    "libreoffice-base": "base",
    "libreoffice-calc": "calc",
    "libreoffice-draw": "draw",
    "libreoffice-impress": "impress",
    "libreoffice-writer": "writer",
    "security-aws-compliance-checker": "aws-compliance-checker",
    "security-aws-iam-best-practices": "aws-iam-best-practices",
    "security-aws-secrets-rotation": "aws-secrets-rotation",
    "security-aws-security-audit": "aws-security-audit",
    "skills-x402-express-wrapper": "x402-express-wrapper",
    "template": "template-skill",
}


def display_name(slug: str) -> str:
    return " ".join(part.upper() if len(part) <= 3 and part.isalpha() else part.capitalize() for part in slug.split("-"))


def write_alias(skills_root: Path, alias: str, target: str) -> bool:
    target_dir = skills_root / target
    if not (target_dir / "SKILL.md").exists():
        raise FileNotFoundError(f"Alias target does not exist: {target}")
    alias_dir = skills_root / alias
    alias_dir.mkdir(parents=True, exist_ok=True)
    references = alias_dir / "references"
    references.mkdir(parents=True, exist_ok=True)

    alias_label = display_name(alias)
    target_label = display_name(target)
    skill_md = alias_dir / "SKILL.md"
    content = f"""---
name: {alias}
description: ALWAYS use this when the user or an upstream archive refers to `{alias}`, the nested skill path form for `{target}`, or the equivalent slash path. This is a namespace-preserving alias that routes to `{target}` while retaining strict validation, Senior Master execution, and Codex review standards.
---

# {alias_label}

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`
- `references/alias-target.md`

Then load the canonical target skill only when the task needs the full implementation guidance.

## Alias Contract

- Treat `{alias}` as a compatibility and search alias for `{target}`.
- Use canonical skill `{target}` for the substantive workflow.
- Do not duplicate large upstream instructions here; this folder exists to preserve nested ZIP path slugs such as `{alias.replace("-", "/")}` while keeping the runtime bundle deduplicated.
- Apply the same Senior Master standard and Codex strict review gate before final output.
"""
    old = skill_md.read_text(encoding="utf-8", errors="replace") if skill_md.exists() else ""
    changed = old != content
    if changed:
        skill_md.write_text(content, encoding="utf-8")

    alias_ref = references / "alias-target.md"
    ref_content = f"""# Alias Target

`{alias}` is a namespace-preserving alias for canonical skill `{target}`.

## Why This Exists

Some upstream ZIP scanners derive skill slugs from nested paths instead of frontmatter names. This alias keeps that path-derived slug discoverable without copying the target skill's full content.

## Routing

- Canonical target folder: `.agent/skills/{target}/`
- Canonical display name: {target_label}
- Alias display name: {alias_label}
- Use the target skill's bundled scripts, references, and assets for substantive work.
"""
    if (not alias_ref.exists()) or alias_ref.read_text(encoding="utf-8", errors="replace") != ref_content:
        alias_ref.write_text(ref_content, encoding="utf-8")
        changed = True
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Add namespace-preserving alias skills for path-derived ZIP slugs.")
    parser.add_argument("skills_root", nargs="?", default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    skills_root = Path(args.skills_root).resolve() if args.skills_root else script_dir.parent.parent
    output = Path(args.output).resolve() if args.output else skills_root.parent.parent / "reports" / "release-alias-skills.json"
    output.parent.mkdir(parents=True, exist_ok=True)

    report = {
        "skillsRoot": str(skills_root),
        "aliasesDeclared": len(ALIASES),
        "aliasesWrittenOrUpdated": 0,
        "aliases": [],
        "errors": [],
    }
    for alias, target in sorted(ALIASES.items()):
        try:
            changed = write_alias(skills_root, alias, target)
            if changed:
                report["aliasesWrittenOrUpdated"] += 1
            report["aliases"].append({"alias": alias, "target": target, "changed": changed})
        except Exception as exc:  # noqa: BLE001 - report all alias failures.
            report["errors"].append({"alias": alias, "target": target, "message": str(exc)})

    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if not report["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
