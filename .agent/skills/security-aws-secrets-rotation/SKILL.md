---
name: security-aws-secrets-rotation
description: ALWAYS use this when the user or an upstream archive refers to `security-aws-secrets-rotation`, the nested skill path form for `aws-secrets-rotation`, or the equivalent slash path. This is a namespace-preserving alias that routes to `aws-secrets-rotation` while retaining strict validation, Senior Master execution, and Codex review standards.
---

# Security AWS Secrets Rotation

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`
- `references/alias-target.md`

Then load the canonical target skill only when the task needs the full implementation guidance.

## Alias Contract

- Treat `security-aws-secrets-rotation` as a compatibility and search alias for `aws-secrets-rotation`.
- Use canonical skill `aws-secrets-rotation` for the substantive workflow.
- Do not duplicate large upstream instructions here; this folder exists to preserve nested ZIP path slugs such as `security/aws/secrets/rotation` while keeping the runtime bundle deduplicated.
- Apply the same Senior Master standard and Codex strict review gate before final output.
