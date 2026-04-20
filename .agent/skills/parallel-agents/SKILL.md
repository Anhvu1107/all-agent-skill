---
name: parallel-agents
description: ALWAYS use this when the task contains multiple independent research questions, code slices, or verification tracks that can proceed in parallel while the immediate local step continues.
---

# Parallel Agents

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Start with `references/delegation-decision-tree.md`.

Use it before spawning work so delegation helps the critical path instead of blocking it.

## Purpose

Use delegation intentionally: local blocking work stays local, bounded sidecar work goes parallel.

## Workflow

1. Name the immediate local step.
2. Identify candidate sidecar tasks.
3. Remove anything that overlaps writes or blocks the next step.
4. Delegate the remaining isolated work.
5. Keep moving locally.
6. Integrate and verify.

## Rules

- Delegation must materially advance the task.
- Each subagent needs a clear output and ownership boundary.
- Do not wait reflexively.
