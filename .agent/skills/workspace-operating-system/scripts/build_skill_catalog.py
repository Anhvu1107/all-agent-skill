from __future__ import annotations

import re
from pathlib import Path


CATEGORY_ORDER = [
    "Operating System And Workflow",
    "Architecture And Delivery",
    "Frontend And Experience",
    "Backend And Data",
    "Quality And Verification",
    "Documents And Artifacts",
    "Creative And Brand",
    "Specialized Domains",
]

CATEGORY_MAP = {
    "Operating System And Workflow": [
        "workspace-operating-system",
        "behavioral-modes",
        "brainstorming",
        "closed-loop-delivery",
        "executing-plans",
        "finishing-a-development-branch",
        "intelligent-routing",
        "parallel-agents",
        "plan-writing",
        "skill-creator",
        "using-git-worktrees",
        "verification-before-completion",
        "documentation-templates",
    ],
    "Architecture And Delivery": [
        "app-builder",
        "architecture",
        "deployment-procedures",
        "clean-code",
        "server-management",
    ],
    "Frontend And Experience": [
        "frontend-design",
        "web-design-guidelines",
        "tailwind-patterns",
        "nextjs-react-expert",
        "mobile-design",
        "seo-fundamentals",
        "theme-factory",
        "web-artifacts-builder",
    ],
    "Backend And Data": [
        "api-patterns",
        "database-design",
        "mcp-builder",
        "nodejs-best-practices",
        "python-patterns",
        "rust-pro",
        "claude-api",
        "powershell-windows",
        "bash-linux",
    ],
    "Quality And Verification": [
        "code-review-checklist",
        "receiving-code-review",
        "testing-patterns",
        "tdd-workflow",
        "webapp-testing",
        "lint-and-validate",
        "performance-profiling",
        "systematic-debugging",
        "vulnerability-scanner",
        "red-team-tactics",
    ],
    "Documents And Artifacts": [
        "doc-coauthoring",
        "internal-comms",
        "slack-gif-creator",
    ],
    "Creative And Brand": [
        "brand-guidelines",
        "canvas-design",
        "algorithmic-art",
    ],
    "Specialized Domains": [
        "game-development",
        "geo-fundamentals",
        "i18n-localization",
    ],
}


def parse_frontmatter(skill_file: Path) -> tuple[str, str]:
    text = skill_file.read_text(encoding="utf-8", errors="ignore")
    name_match = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
    desc_match = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
    name = name_match.group(1).strip() if name_match else skill_file.parent.name
    desc = desc_match.group(1).strip() if desc_match else ""
    return name, desc


def build_catalog(skills_root: Path) -> str:
    entries: dict[str, tuple[str, str]] = {}
    for skill_file in skills_root.glob("*/SKILL.md"):
        name, desc = parse_frontmatter(skill_file)
        entries[name] = (skill_file.parent.name, desc)

    assigned: set[str] = set()
    lines = [
        "# Skill Catalog",
        "",
        "Generated from the current unified skill library.",
        "",
        f"Total skills: {len(entries)}",
        "",
        "Use this file when the correct skill is unclear and you need exhaustive coverage.",
        "",
    ]

    for category in CATEGORY_ORDER:
        lines.append(f"## {category}")
        lines.append("")
        for name in CATEGORY_MAP.get(category, []):
            if name not in entries or name in assigned:
                continue
            _, desc = entries[name]
            lines.append(f"- `{name}`: {desc}")
            assigned.add(name)
        lines.append("")

    remaining = sorted(set(entries) - assigned)
    if remaining:
        lines.append("## Unsorted")
        lines.append("")
        for name in remaining:
            _, desc = entries[name]
            lines.append(f"- `{name}`: {desc}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    skills_root = skill_dir.parent
    output_path = skill_dir / "references" / "skill-catalog.md"
    output_path.write_text(build_catalog(skills_root), encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
