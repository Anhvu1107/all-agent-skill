#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from quick_validate import validate_skill


LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER_PATTERN = re.compile(r"^\ufeff?\s*---\s*\r?\n(.*?)\r?\n---\s*(.*)$", re.DOTALL)


def iter_skills(skills_root: Path) -> list[Path]:
    return sorted(
        path for path in skills_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").exists()
    )


def read_description(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
    if not match:
        return ""
    return match.group(1).strip().strip('"').strip("'")


def read_frontmatter(skill_md: Path) -> tuple[dict, str]:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return {}, text
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        data = {}
    if not isinstance(data, dict):
        data = {}
    return data, match.group(2)


def collect_markdown_links(skill_md: Path) -> list[str]:
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    links: list[str] = []
    for raw_target in LINK_PATTERN.findall(text):
        target = raw_target.strip()
        if "://" in target or target.startswith("#"):
            continue
        if target.lower().endswith(".md"):
            links.append(target)
    return links


def resolve_missing_links(skill_dir: Path, links: Iterable[str]) -> list[str]:
    missing: list[str] = []
    for link in links:
        normalized = link.replace("/", "\\")
        target = (skill_dir / normalized).resolve()
        if not target.exists():
            missing.append(link)
    return missing


def parse_catalog_total(catalog_path: Path) -> int | None:
    if not catalog_path.exists():
        return None
    text = catalog_path.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"Total skills:\s*(\d+)", text)
    return int(match.group(1)) if match else None


def count_root_markdown_docs(skill_dir: Path) -> int:
    return len([
        path for path in skill_dir.glob("*.md")
        if path.name.lower() != "skill.md"
    ])


def is_pushy_description(description: str) -> bool:
    lower = description.lower()
    return any(marker in lower for marker in (
        "always use this",
        "always use ",
        "trigger whenever",
        "trigger when",
    ))


def is_trigger_forward_description(description: str) -> bool:
    lower = description.lower()
    return any(marker in lower for marker in (
        "use when",
        "whenever the user",
        "trigger when",
        "trigger whenever",
        "always use",
        "use this skill whenever",
    ))


def build_report(skills_root: Path) -> dict:
    skills = iter_skills(skills_root)
    skill_rows = []
    invalid_skills = []
    broken_links = []

    with_references = 0
    with_reference_legacy = 0
    with_scripts = 0
    with_assets = 0
    with_agents = 0
    with_senior_master_standard = 0
    with_senior_master_link = 0
    with_codex_strict_gate = 0
    with_strict_frontmatter = 0
    with_name_matching_folder = 0
    with_compact_skill_md = 0
    with_agent_implicit_policy = 0
    with_agent_prompt_matching_skill = 0
    pushy_descriptions = 0
    use_when_descriptions = 0
    trigger_forward_descriptions = 0
    root_doc_skills = 0

    for skill_dir in skills:
        skill_md = skill_dir / "SKILL.md"
        description = read_description(skill_md)
        frontmatter, body = read_frontmatter(skill_md)
        name = str(frontmatter.get("name") or "").strip()
        extra_frontmatter_keys = sorted(set(frontmatter) - {"name", "description"})
        name_matches_folder = name == skill_dir.name
        has_strict_frontmatter = set(frontmatter) == {"name", "description"}
        body_lines = len(body.splitlines())
        has_compact_skill_md = body_lines <= 500
        has_references = (skill_dir / "references").exists()
        has_reference_legacy = (skill_dir / "reference").exists() or count_root_markdown_docs(skill_dir) > 0
        has_scripts = (skill_dir / "scripts").exists()
        has_assets = (skill_dir / "assets").exists()
        agent_path = skill_dir / "agents" / "openai.yaml"
        has_agents = agent_path.exists()
        agent_text = agent_path.read_text(encoding="utf-8", errors="ignore") if has_agents else ""
        has_agent_implicit_policy = "allow_implicit_invocation: true" in agent_text
        has_agent_prompt_matching_skill = f"${name}" in agent_text if name else False
        has_senior_master_standard = (skill_dir / "references" / "senior-master-standard.md").exists()
        skill_text = skill_md.read_text(encoding="utf-8", errors="ignore")
        has_senior_master_link = "references/senior-master-standard.md" in skill_text
        quality_path = skill_dir / "references" / "quality-checklist.md"
        has_codex_strict_gate = (
            quality_path.exists()
            and "Codex Strict Review Gate" in quality_path.read_text(encoding="utf-8", errors="ignore")
        )
        root_markdown_docs = count_root_markdown_docs(skill_dir)
        file_count = sum(1 for path in skill_dir.rglob("*") if path.is_file())

        valid, message = validate_skill(skill_dir)
        if not valid:
            invalid_skills.append({"skill": skill_dir.name, "message": message})

        links = collect_markdown_links(skill_md)
        missing = resolve_missing_links(skill_dir, links)
        if missing:
            broken_links.append({"skill": skill_dir.name, "missing": missing})

        if has_references:
            with_references += 1
        if has_reference_legacy:
            with_reference_legacy += 1
        if has_scripts:
            with_scripts += 1
        if has_assets:
            with_assets += 1
        if has_agents:
            with_agents += 1
        if has_senior_master_standard:
            with_senior_master_standard += 1
        if has_senior_master_link:
            with_senior_master_link += 1
        if has_codex_strict_gate:
            with_codex_strict_gate += 1
        if has_strict_frontmatter:
            with_strict_frontmatter += 1
        if name_matches_folder:
            with_name_matching_folder += 1
        if has_compact_skill_md:
            with_compact_skill_md += 1
        if has_agent_implicit_policy:
            with_agent_implicit_policy += 1
        if has_agent_prompt_matching_skill:
            with_agent_prompt_matching_skill += 1
        if is_pushy_description(description):
            pushy_descriptions += 1
        if "use when" in description.lower():
            use_when_descriptions += 1
        if is_trigger_forward_description(description):
            trigger_forward_descriptions += 1
        if root_markdown_docs:
            root_doc_skills += 1

        skill_rows.append({
            "skill": skill_dir.name,
            "fileCount": file_count,
            "hasReferences": has_references,
            "hasLegacyReferenceShape": has_reference_legacy,
            "hasScripts": has_scripts,
            "hasAssets": has_assets,
            "hasAgents": has_agents,
            "hasSeniorMasterStandard": has_senior_master_standard,
            "hasSeniorMasterLink": has_senior_master_link,
            "hasCodexStrictGate": has_codex_strict_gate,
            "hasStrictFrontmatter": has_strict_frontmatter,
            "frontmatterExtraKeys": extra_frontmatter_keys,
            "nameMatchesFolder": name_matches_folder,
            "bodyLines": body_lines,
            "hasCompactSkillMd": has_compact_skill_md,
            "hasAgentImplicitPolicy": has_agent_implicit_policy,
            "hasAgentPromptMatchingSkill": has_agent_prompt_matching_skill,
            "rootMarkdownDocs": root_markdown_docs,
            "description": description,
        })

    skill_rows.sort(key=lambda row: row["fileCount"], reverse=True)

    catalog_path = skills_root / "workspace-operating-system" / "references" / "skill-catalog.md"
    catalog_total = parse_catalog_total(catalog_path)

    report = {
        "skillsRoot": str(skills_root),
        "totalSkills": len(skills),
        "withReferences": with_references,
        "withLegacyReferenceShape": with_reference_legacy,
        "withScripts": with_scripts,
        "withAssets": with_assets,
        "withAgents": with_agents,
        "withSeniorMasterStandard": with_senior_master_standard,
        "withSeniorMasterLink": with_senior_master_link,
        "withCodexStrictGate": with_codex_strict_gate,
        "withStrictFrontmatter": with_strict_frontmatter,
        "withNameMatchingFolder": with_name_matching_folder,
        "withCompactSkillMd": with_compact_skill_md,
        "withAgentImplicitPolicy": with_agent_implicit_policy,
        "withAgentPromptMatchingSkill": with_agent_prompt_matching_skill,
        "pushyDescriptions": pushy_descriptions,
        "useWhenDescriptions": use_when_descriptions,
        "triggerForwardDescriptions": trigger_forward_descriptions,
        "skillsWithRootMarkdownDocs": root_doc_skills,
        "invalidSkills": invalid_skills,
        "brokenLinks": broken_links,
        "catalogTotal": catalog_total,
        "catalogMatchesLiveCount": catalog_total == len(skills) if catalog_total is not None else False,
        "topMissingReferences": [
            row for row in skill_rows if not row["hasReferences"]
        ][:20],
        "topMissingAgents": [
            row for row in skill_rows if not row["hasAgents"]
        ][:20],
        "topMissingSeniorMasterStandard": [
            row for row in skill_rows if not row["hasSeniorMasterStandard"]
        ][:20],
        "topMissingSeniorMasterLink": [
            row for row in skill_rows if not row["hasSeniorMasterLink"]
        ][:20],
        "topMissingCodexStrictGate": [
            row for row in skill_rows if not row["hasCodexStrictGate"]
        ][:20],
        "topExtraFrontmatter": [
            row for row in skill_rows if not row["hasStrictFrontmatter"]
        ][:20],
        "topNameMismatch": [
            row for row in skill_rows if not row["nameMatchesFolder"]
        ][:20],
        "topLongSkillMdBodies": sorted(
            [row for row in skill_rows if not row["hasCompactSkillMd"]],
            key=lambda row: row["bodyLines"],
            reverse=True,
        )[:20],
        "topMissingAgentImplicitPolicy": [
            row for row in skill_rows if not row["hasAgentImplicitPolicy"]
        ][:20],
        "topAgentPromptMismatch": [
            row for row in skill_rows if not row["hasAgentPromptMatchingSkill"]
        ][:20],
    }
    return report


def render_markdown(report: dict) -> str:
    lines = [
        "# Bundle Health Report",
        "",
        "Generated from the current skill tree.",
        "",
        "## Metrics",
        "",
        f"- Total skills: {report['totalSkills']}",
        f"- Skills with references/: {report['withReferences']}",
        f"- Skills with legacy reference shape: {report['withLegacyReferenceShape']}",
        f"- Skills with scripts/: {report['withScripts']}",
        f"- Skills with assets/: {report['withAssets']}",
        f"- Skills with agents/openai.yaml: {report['withAgents']}",
        f"- Skills with senior-master standard: {report['withSeniorMasterStandard']}",
        f"- SKILL.md links to senior-master standard: {report['withSeniorMasterLink']}",
        f"- Skills with Codex strict review gate: {report['withCodexStrictGate']}",
        f"- Skills with strict name/description-only frontmatter: {report['withStrictFrontmatter']}",
        f"- Skills whose frontmatter name matches folder: {report['withNameMatchingFolder']}",
        f"- Skills with compact SKILL.md body (<=500 lines): {report['withCompactSkillMd']}",
        f"- Skills with implicit agent invocation policy: {report['withAgentImplicitPolicy']}",
        f"- Skills with agent prompt matching skill name: {report['withAgentPromptMatchingSkill']}",
        f"- Pushy descriptions: {report['pushyDescriptions']}",
        f"- Trigger-forward descriptions: {report['triggerForwardDescriptions']}",
        f"- Skills with root markdown docs outside references/: {report['skillsWithRootMarkdownDocs']}",
        "",
        "## Integrity",
        "",
        f"- Catalog total matches live count: {'yes' if report['catalogMatchesLiveCount'] else 'no'}",
        f"- Invalid skills: {len(report['invalidSkills'])}",
        f"- Skills with broken markdown links: {len(report['brokenLinks'])}",
        "",
        "## Top Missing references/",
        "",
    ]

    if report["topMissingReferences"]:
        for row in report["topMissingReferences"][:10]:
            lines.append(f"- `{row['skill']}` ({row['fileCount']} files, agents={row['hasAgents']}, root-md={row['rootMarkdownDocs']})")
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Top Missing agents/openai.yaml",
        "",
    ])

    if report["topMissingAgents"]:
        for row in report["topMissingAgents"][:10]:
            lines.append(f"- `{row['skill']}` ({row['fileCount']} files, refs={row['hasReferences']}, root-md={row['rootMarkdownDocs']})")
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Top Missing Senior Master Standard",
        "",
    ])

    if report["topMissingSeniorMasterStandard"]:
        for row in report["topMissingSeniorMasterStandard"][:10]:
            lines.append(f"- `{row['skill']}`")
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Top Missing Codex Strict Review Gate",
        "",
    ])

    if report["topMissingCodexStrictGate"]:
        for row in report["topMissingCodexStrictGate"][:10]:
            lines.append(f"- `{row['skill']}`")
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Top Extra Frontmatter",
        "",
    ])

    if report["topExtraFrontmatter"]:
        for row in report["topExtraFrontmatter"][:10]:
            keys = ", ".join(row["frontmatterExtraKeys"])
            lines.append(f"- `{row['skill']}`: {keys}")
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Top Name/Folder Mismatches",
        "",
    ])

    if report["topNameMismatch"]:
        for row in report["topNameMismatch"][:10]:
            lines.append(f"- `{row['skill']}`")
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Top Long SKILL.md Bodies",
        "",
    ])

    if report["topLongSkillMdBodies"]:
        for row in report["topLongSkillMdBodies"][:10]:
            lines.append(f"- `{row['skill']}`: {row['bodyLines']} lines")
    else:
        lines.append("- none")

    lines.extend([
        "",
        "## Top Agent Metadata Gaps",
        "",
    ])

    agent_gap_count = len(report["topMissingAgentImplicitPolicy"]) + len(report["topAgentPromptMismatch"])
    if agent_gap_count:
        for row in report["topMissingAgentImplicitPolicy"][:10]:
            lines.append(f"- `{row['skill']}`: missing implicit invocation policy")
        for row in report["topAgentPromptMismatch"][:10]:
            lines.append(f"- `{row['skill']}`: agent prompt does not mention skill name")
    else:
        lines.append("- none")

    if report["invalidSkills"]:
        lines.extend([
            "",
            "## Invalid Skills",
            "",
        ])
        for item in report["invalidSkills"]:
            lines.append(f"- `{item['skill']}`: {item['message']}")

    if report["brokenLinks"]:
        lines.extend([
            "",
            "## Broken Links",
            "",
        ])
        for item in report["brokenLinks"][:20]:
            missing = ", ".join(f"`{entry}`" for entry in item["missing"])
            lines.append(f"- `{item['skill']}`: {missing}")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a full skill bundle and emit health reports.")
    parser.add_argument("skills_root", nargs="?", default=None, help="Path to the .agent/skills directory")
    parser.add_argument("--output-dir", default=None, help="Directory for JSON/Markdown reports")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    default_skills_root = script_dir.parent.parent
    skills_root = Path(args.skills_root).resolve() if args.skills_root else default_skills_root
    output_dir = Path(args.output_dir).resolve() if args.output_dir else skills_root.parent.parent / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    report = build_report(skills_root)
    json_path = output_dir / "bundle-health.json"
    md_path = output_dir / "bundle-health.md"

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(report), encoding="utf-8")

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
