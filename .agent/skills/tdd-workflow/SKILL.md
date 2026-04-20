---
name: tdd-workflow
description: ALWAYS use this when a bug fix or logic change should be locked down by tests first, especially when regression risk is higher than the cost of writing focused tests.
---

# TDD Workflow

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Start with `references/tdd-decision-guide.md`.

Use it to decide whether to stay with focused TDD, shift to broader integration tests, or explicitly avoid forcing TDD on the task.

## Purpose

Keep test-first discipline practical, not ceremonial.

## Workflow

1. Decide whether the behavior is test-definable right now.
2. Write the failing proof.
3. Implement the narrowest passing change.
4. Refactor while staying green.
5. Widen checks only after the focused proof is stable.

## Rules

- If the bug can be reproduced, capture it in a test before fixing it.
- If setup cost is huge, shrink the seam instead of abandoning proof too early.
- If the work is mostly visual exploration, say so and use a different skill.
