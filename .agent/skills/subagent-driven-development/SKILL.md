---
name: subagent-driven-development
description: ALWAYS use this when you already have an implementation plan with mostly independent tasks and want to execute it through fresh, tightly-scoped subagents plus structured review after each task.
---

# Subagent-Driven Development

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Start with `references/task-pack-template.md`.

Use the template before dispatch so every subagent gets a bounded task, a write scope, and a clear completion proof.

## Purpose

Execute a real plan with fresh subagents while keeping quality gates between steps.

## Workflow

1. Confirm the plan is already good enough to execute.
2. Split tasks by ownership and dependency.
3. Send one tight task packet per subagent.
4. Review each returned change for spec compliance first.
5. Run a second pass for code quality or regression risk.
6. Integrate and verify before moving on.

## Rules

- One task packet per coherent slice.
- No overlapping write ownership.
- No delegation of the immediate blocking task if you need its answer now.
- Every returned patch still needs local verification.

## Best Use Cases

- implementing approved milestones
- landing several isolated bug fixes
- parallel test authoring plus implementation
- iterative feature work with review after each slice
