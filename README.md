# Agent Skills VVIP Pro Max Ultra

Clean, deduplicated, validator-backed agent skill bundle built from the merged upstream skill archives and upgraded for strict Codex/Claude review.

## Current Release

- Runtime skill entries: 1462
- Canonical content skills: 1440
- Namespace/path alias skills: 22
- Raw upstream `SKILL.md` files audited: 4547
- Raw upstream entries covered by canonical mapping: 4547 / 4547
- Missing unique upstream slugs: 0
- ZIP compatibility missing slugs: 0 by frontmatter, leaf, and path-derived slug checks
- Invalid skills: 0
- Broken markdown links: 0
- Nested non-runtime `SKILL.md` mirrors in release tree: 0

## What Is Included

- `.agent/skills/` contains the runtime skill tree.
- `CATALOG.md` is the human-readable skill catalog.
- `search-index.json` and `search-index.ndjson` are machine-searchable indexes.
- `reports/` contains validation, upstream coverage, ZIP compatibility, and final verification evidence.
- `scripts/validate_release.py` runs the full release validation pipeline.
- `.github/workflows/validate-skills.yml` validates the bundle in CI.

## Release Policy

The working source can preserve `_upstreams/` locally for audit, but `_upstreams/` is intentionally ignored by git and excluded from clean ZIP/RAR release packages. This prevents simple scanners from counting raw mirror files as duplicate runtime skills while preserving raw coverage evidence in the reports.

## Validation

Run from the repository root:

```powershell
python scripts/validate_release.py
```

Expected result:

- `totalSkills = 1462`
- `withReferences = 1462`
- `withAgents = 1462`
- `withSeniorMasterStandard = 1462`
- `withCodexStrictGate = 1462`
- `withStrictFrontmatter = 1462`
- `withNameMatchingFolder = 1462`
- `withCompactSkillMd = 1462`
- `invalidSkills = []`
- `brokenLinks = []`

## Key Review Files

- `CLAUDE_REVIEW_PACKET.md`
- `VVIP_UPGRADE_REPORT.md`
- `ZIP_COMPATIBILITY_AUDIT.md`
- `UPSTREAM_RAW_SKILL_COVERAGE.md`
- `reports/bundle-health.json`
- `reports/final-verification.json`
