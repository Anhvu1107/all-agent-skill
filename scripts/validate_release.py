#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run(command: list[str], cwd: Path) -> None:
    print("+ " + " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and rebuild generated release indexes for the skill bundle.")
    parser.add_argument("--bundle-root", default=".")
    parser.add_argument("--skip-upstream", action="store_true", help="Skip upstream raw coverage when _upstreams is absent.")
    args = parser.parse_args()

    bundle_root = Path(args.bundle_root).resolve()
    py = sys.executable

    if (bundle_root / "_upstreams").exists() and not args.skip_upstream:
        run([py, ".agent/skills/skill-creator/scripts/import_missing_upstream_skills.py", "--report-only"], bundle_root)

    run([py, ".agent/skills/skill-creator/scripts/add_release_alias_skills.py", ".agent/skills", "--output", "reports/release-alias-skills.json"], bundle_root)
    run([py, ".agent/skills/skill-creator/scripts/complete_bundle_polish.py", ".agent/skills", "--output", "reports/completion-pass-release-validation.json"], bundle_root)
    run([py, ".agent/skills/skill-creator/scripts/apply_senior_master_standard.py", ".agent/skills", "--output", "reports/senior-master-pass-release-validation.json"], bundle_root)
    run([py, ".agent/skills/skill-creator/scripts/strict_skill_hardening.py", ".agent/skills", "--output", "reports/strict-skill-hardening-release-validation.json"], bundle_root)
    run([py, ".agent/skills/skill-creator/scripts/archive_nested_skill_mirrors.py", ".agent/skills", "--output", "reports/nested-skill-mirror-archive.json"], bundle_root)
    run([py, ".agent/skills/skill-creator/scripts/strengthen_weak_descriptions.py", ".agent/skills", "--output", "reports/weak-description-release-validation.json"], bundle_root)
    run([py, ".agent/skills/workspace-operating-system/scripts/build_skill_catalog.py"], bundle_root)
    run([py, "scripts/build_release_indexes.py", "--bundle-root", "."], bundle_root)
    run([py, ".agent/skills/skill-creator/scripts/validate_skill_bundle.py", ".agent/skills", "--output-dir", "reports"], bundle_root)

    health = json.loads((bundle_root / "reports" / "bundle-health.json").read_text(encoding="utf-8"))
    required_equal = [
        "withReferences",
        "withAgents",
        "withSeniorMasterStandard",
        "withSeniorMasterLink",
        "withCodexStrictGate",
        "withStrictFrontmatter",
        "withNameMatchingFolder",
        "withCompactSkillMd",
        "withAgentImplicitPolicy",
        "withAgentPromptMatchingSkill",
        "pushyDescriptions",
        "triggerForwardDescriptions",
    ]
    total = health["totalSkills"]
    failures = []
    for key in required_equal:
        if health.get(key) != total:
            failures.append(f"{key}={health.get(key)} expected {total}")
    if health["invalidSkills"]:
        failures.append(f"invalidSkills={len(health['invalidSkills'])}")
    if health["brokenLinks"]:
        failures.append(f"brokenLinks={len(health['brokenLinks'])}")
    if health["skillsWithRootMarkdownDocs"] != 0:
        failures.append(f"skillsWithRootMarkdownDocs={health['skillsWithRootMarkdownDocs']}")
    if not health["catalogMatchesLiveCount"]:
        failures.append("catalogMatchesLiveCount=false")
    if failures:
        for failure in failures:
            print(f"VALIDATION FAILURE: {failure}")
        return 1
    print("Release validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
