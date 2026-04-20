#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


STANDARD_REFERENCE = """# Senior Master Standard

Use this standard before, during, and after executing this skill.

## Operating Level

Act like a senior/master practitioner of this skill's domain:

- understand the user's real objective before producing output
- choose the smallest responsible workflow that still meets a professional bar
- preserve the skill's domain boundaries and use bundled resources deliberately
- prefer evidence, artifacts, and checks over confident guesses
- surface important uncertainty instead of hiding it behind polished wording

## Codex Strict Review Gate

Assume every completed result will be reviewed by Codex with extreme scrutiny.

Before finalizing:

- check that the answer or artifact directly satisfies the user's request
- verify claims against files, commands, source material, or produced artifacts where possible
- inspect for missing edge cases, stale assumptions, broken references, and unsupported promises
- ensure any generated code, document, design, or analysis is internally consistent
- state what was verified and any meaningful residual risk

## Senior Master Finish Bar

Do not treat the task as complete until the work would survive a hostile but fair review:

- no lazy placeholders unless the user explicitly asked for a scaffold
- no invented facts, fake paths, fake commands, fake tests, or fake validation
- no generic output when the skill's domain requires specialized judgment
- no silent skipping of relevant `references/`, `scripts/`, `assets/`, or examples
- no completion claim without a verification story
"""


QUALITY_GATE = """## Codex Strict Review Gate

Assume the final result will be inspected by Codex with extreme scrutiny.

- Verify that the output directly satisfies the user's request and this skill's domain.
- Check important claims against local files, commands, source material, or produced artifacts when possible.
- Look for missing edge cases, stale assumptions, broken references, and unsupported promises.
- Do not call the work complete unless it would survive a hostile but fair senior review.
"""


def iter_skill_dirs(skills_root: Path) -> list[Path]:
    return sorted(path for path in skills_root.iterdir() if path.is_dir() and (path / "SKILL.md").exists())


def ensure_reference(skill_dir: Path) -> bool:
    target = skill_dir / "references" / "senior-master-standard.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.read_text(encoding="utf-8", errors="replace") == STANDARD_REFERENCE:
        return False
    target.write_text(STANDARD_REFERENCE, encoding="utf-8")
    return True


def insert_after_first_heading(text: str, block: str) -> str:
    heading = re.search(r"(?m)^# .*$", text)
    if heading:
        line_end = text.find("\n", heading.end())
        if line_end == -1:
            return text + "\n\n" + block
        return text[: line_end + 1] + "\n" + block + text[line_end + 1 :]
    return block + text


def ensure_skill_link(skill_md: Path) -> bool:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if "references/senior-master-standard.md" in text:
        return False

    frontmatter = re.match(r"^(?P<prefix>\ufeff?\s*)---\s*\r?\n(?P<frontmatter>.*?)\r?\n---\s*(?P<body>.*)$", text, re.DOTALL)
    if frontmatter:
        head = f"{frontmatter.group('prefix')}---\n{frontmatter.group('frontmatter').rstrip()}\n---\n\n"
        body = frontmatter.group("body").lstrip()
        updated_body = ensure_skill_link_in_body(body)
        skill_md.write_text(head + updated_body, encoding="utf-8")
        return True

    updated = ensure_skill_link_in_body(text)
    skill_md.write_text(updated, encoding="utf-8")
    return True


def ensure_skill_link_in_body(text: str) -> str:
    bullet = "- `references/senior-master-standard.md`\n"
    if "Start with:\n\n" in text:
        return text.replace("Start with:\n\n", "Start with:\n\n" + bullet, 1)
    elif "## Selective Reading Rule" in text:
        return text.replace(
            "## Selective Reading Rule",
            "## Selective Reading Rule\n\nStart with:\n\n" + bullet,
            1,
        )
    else:
        block = (
            "## Selective Reading Rule\n\n"
            "Start with:\n\n"
            f"{bullet}\n"
            "Then load only the references, scripts, assets, or examples needed for the user's actual task.\n\n"
        )
        return insert_after_first_heading(text, block)


def ensure_quality_gate(skill_dir: Path) -> bool:
    target = skill_dir / "references" / "quality-checklist.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        text = target.read_text(encoding="utf-8", errors="replace").rstrip() + "\n"
    else:
        text = f"# Quality Checklist\n\nUse this before calling work with `{skill_dir.name}` complete.\n\n"

    if "Codex Strict Review Gate" in text:
        return False

    target.write_text(text.rstrip() + "\n\n" + QUALITY_GATE, encoding="utf-8")
    return True


def apply_standard(skills_root: Path) -> dict:
    result = {
        "skillsRoot": str(skills_root),
        "skillsSeen": 0,
        "standardReferencesWritten": 0,
        "skillMdLinksInserted": 0,
        "qualityGatesInserted": 0,
        "errors": [],
    }

    for skill_dir in iter_skill_dirs(skills_root):
        result["skillsSeen"] += 1
        try:
            if ensure_reference(skill_dir):
                result["standardReferencesWritten"] += 1
            if ensure_skill_link(skill_dir / "SKILL.md"):
                result["skillMdLinksInserted"] += 1
            if ensure_quality_gate(skill_dir):
                result["qualityGatesInserted"] += 1
        except Exception as exc:
            result["errors"].append({"skill": skill_dir.name, "error": str(exc)})

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply senior/master execution and Codex strict review standards to every skill.")
    parser.add_argument("skills_root", help="Path to .agent/skills")
    parser.add_argument("--output", default=None, help="Optional JSON report path")
    args = parser.parse_args()

    result = apply_standard(Path(args.skills_root).resolve())
    if args.output:
        output = Path(args.output).resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
