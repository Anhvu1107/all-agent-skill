# Full Merge Report

## Goal

Rebuild the bundle as a true full merge that keeps maximum content from the 4 upstream archives instead of a heavily filtered public-only subset.

## Source Skill Counts

- Current bundle canonical skills: 55
- main.zip skills: 17
- superpowers-main.zip skills: 14
- antigravity Claude plugin skills: 1397
- antigravity Codex plugin skills: 1382
- Canonical merged skill tree after rebuild: 1409
- Duplicate skill names across sources: 1384

## Restored High-Value Gaps

- Restored from `main.zip`: docx, pdf, pptx, xlsx
- Preferred from `superpowers-main.zip`: dispatching-parallel-agents, requesting-code-review, receiving-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-superpowers, writing-plans, writing-skills
- Preserved full eval pipeline under the canonical `skill-creator` plus `_upstreams/main/skills/skill-creator`
- Preserved the complete `superpowers` repo under `_upstreams/superpowers`
- Preserved the full `antigravity` repo under `_upstreams/antigravity`

## Provenance Files

- `reports/skill-manifest.csv`
- `reports/duplicate-skills.csv`
- `reports/merge-summary.json`

## Packaging

- Output folder: `D:\skill\skill\agent-skills-full-merge`
- Archive path: `D:\skill\skill\agent-skills-full-merge.rar`
