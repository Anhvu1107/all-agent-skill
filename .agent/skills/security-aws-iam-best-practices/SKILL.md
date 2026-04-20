---
name: security-aws-iam-best-practices
description: ALWAYS use this when the user or an upstream archive refers to `security-aws-iam-best-practices`, the nested skill path form for `aws-iam-best-practices`, or the equivalent slash path. This is a namespace-preserving alias that routes to `aws-iam-best-practices` while retaining strict validation, Senior Master execution, and Codex review standards.
---

# Security AWS IAM Best Practices

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`
- `references/alias-target.md`

Then load the canonical target skill only when the task needs the full implementation guidance.

## Alias Contract

- Treat `security-aws-iam-best-practices` as a compatibility and search alias for `aws-iam-best-practices`.
- Use canonical skill `aws-iam-best-practices` for the substantive workflow.
- Do not duplicate large upstream instructions here; this folder exists to preserve nested ZIP path slugs such as `security/aws/iam/best/practices` while keeping the runtime bundle deduplicated.
- Apply the same Senior Master standard and Codex strict review gate before final output.
