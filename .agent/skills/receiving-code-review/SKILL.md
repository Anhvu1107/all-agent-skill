---
name: receiving-code-review
description: ALWAYS use this when review feedback arrives and you need to verify, triage, and implement it carefully instead of agreeing performatively or applying it blindly.
---

# Receiving Code Review

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Start with `references/feedback-triage.md`.

Use it before touching code so you classify each comment as adopt, clarify, or push back with evidence.

## Purpose

Treat review as a technical signal-processing task, not a performance of agreement.

## Workflow

1. Read every comment fully.
2. Restate the technical requirement in your own words.
3. Verify it against the codebase and requirements.
4. Decide: accept, clarify, or push back with evidence.
5. Implement one coherent batch at a time.
6. Re-verify the affected behavior.

## Rules

- Never say a comment is correct before you verified it.
- Never dismiss a comment without technical reasoning.
- Never bundle unrelated review fixes together if they need separate proof.

## Deliverable

For each review item, be able to state:

- what the reviewer is worried about
- whether that concern is real in this codebase
- what changed in response
- how you verified it
