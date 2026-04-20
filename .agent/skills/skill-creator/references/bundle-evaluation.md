# Bundle Evaluation

Use this when the task is bigger than one skill and the real deliverable is a healthier bundle.

## Minimum Bundle Pass

1. Validate every touched skill with `scripts/quick_validate.py`.
2. Run `scripts/validate_skill_bundle.py` against the full `.agent/skills` tree.
3. Regenerate any stale catalogs, manifests, or summary files.
4. Spot-check the skills most likely to be sampled by a reviewer.

## Reviewer-Facing Failure Modes

- stale counts in reports or catalogs
- `SKILL.md` mentioning files that do not exist
- big skills with no `references/` or `agents/openai.yaml`
- bundle summaries claiming upgrades that are not reflected on disk
- descriptions that are technically correct but too timid to trigger reliably

## What Good Looks Like

- top routing skills are current and trustworthy
- flagship skills have strong trigger language
- large skills expose optional depth through `references/`
- important skills have UI metadata
- validation artifacts are generated from the current bundle, not manually guessed
