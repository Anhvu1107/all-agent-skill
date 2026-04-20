---
name: test-driven-development
description: ALWAYS use this when implementing or changing behavior that can be defined by a failing test first, including bug fixes, parsing, validation, business rules, state transitions, and regression-prone logic.
---

# Test-Driven Development

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/red-green-refactor-checklist.md`
- `references/test-shape-heuristics.md`

Read `references/test-shape-heuristics.md` before writing the first test when the system has lots of mocking, async behavior, or awkward setup.

## Purpose

Use failing tests to define behavior before implementation makes the answer look obvious.

## Use This Skill When

- a bug fix can be reproduced in a test
- a new rule, parser, validation, or state transition needs precision
- refactoring could quietly change behavior
- confidence matters more than raw typing speed

## Core Law

No production logic before a failing proof.

## Red-Green-Refactor

1. Red.
   - write the smallest realistic test that demonstrates the missing behavior
   - run it and confirm it fails for the right reason
2. Green.
   - implement the smallest change that makes the test pass
3. Refactor.
   - improve names, structure, and duplication while keeping the suite green

## Rules

- Keep each test focused on one behavior.
- Prefer real behavior over mock choreography.
- Run the focused proof first, then widen verification only as needed.
- If a test passes immediately, it did not prove the change you think it proved.

## When Not To Force It

- visual exploration where expectations are not yet stable
- disposable spikes that are intentionally throwaway
- tasks blocked by unresolved architecture decisions

## Deliverable

Report:

- the failing proof you added or tightened
- the implementation change
- the focused test result
- the broader regression checks you ran
