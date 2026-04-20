---
name: requesting-code-review
description: ALWAYS use this when a meaningful change is complete enough to need a review pass before merge, especially for major features, risky refactors, or work produced by delegated agents.
---

# Requesting Code Review

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Start with `references/review-request-template.md`.

Use it to package the change so the reviewer sees requirements, scope, validation, and risk instead of reconstructing everything from the diff.

## Purpose

Request review in a way that surfaces useful findings quickly.

## Use This Skill When

- a feature, refactor, or bug fix is ready for a real review pass
- work came back from another agent and needs an independent check
- you are about to merge, push, or ask for sign-off

## Workflow

1. Summarize the requirement.
2. State what changed.
3. Include the validation already run.
4. Call out risky areas or open questions.
5. Give the reviewer a bounded diff or file set when possible.

## Rules

- Do not ask for review with no validation.
- Do not dump an unframed large diff on the reviewer if a tighter slice exists.
- Do not hide known risk; name it directly.

## Deliverable

A review request should include:

- requirement or acceptance criteria
- changed scope
- validation evidence
- specific areas where feedback is most valuable
