# Quality Audit

Use this checklist before calling broad repository work, bundle work, or release-facing work complete.

## Evidence Bar

- Re-run every generated catalog or manifest that could be stale.
- Verify the files mentioned in SKILL bodies actually exist.
- Confirm any new scripts run successfully on at least one realistic target.
- Prefer generated metrics over hand-written claims.

## Skill Bundle Audit

- descriptions trigger the right skills aggressively and specifically
- large skills point to `references/`, `scripts/`, or `assets/` instead of forcing everything into `SKILL.md`
- important skills have `agents/openai.yaml`
- reports and summaries match the current bundle, not a previous snapshot

## Repo Audit

- no accidental deletion of upstream or source material
- no claims of verification without commands or artifacts
- no stale counts, broken links, or missing referenced files
- no hidden dependence on unavailable external services

If any item is uncertain, say so explicitly and fix the highest-leverage gap first.
