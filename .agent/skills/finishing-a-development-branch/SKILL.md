---
name: finishing-a-development-branch
description: ALWAYS use this when branch work looks complete and the next question is whether to push, open a PR, merge, keep, or safely clean up.
---

# Finishing A Development Branch

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Start with `references/branch-closeout-template.md`.

Use it to package the branch summary, validation state, likely base branch, and next-step options before asking the user to choose.

## Purpose

Separate "the diff exists" from "the branch is ready for its next lifecycle decision."

## Workflow

1. Check status, diff, and most relevant validation.
2. Summarize what the branch changed.
3. Identify the likely integration path.
4. Offer explicit options.
5. Execute only the option the user chose.

## Rules

- Never delete branches or worktrees without confirmation.
- Never overstate readiness when verification is incomplete.
- Never hide unrelated changes on the branch.
