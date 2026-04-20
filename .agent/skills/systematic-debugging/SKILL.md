---
name: systematic-debugging
description: ALWAYS use this when the user mentions any bug, flaky behavior, failing test, broken build, regression, runtime error, performance mystery, or unexpected output, especially when guessing at fixes feels tempting.
---

# Systematic Debugging

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/evidence-capture.md`
- `references/root-cause-tracing.md`

Read both before proposing fixes when the problem crosses multiple layers, has already resisted one fix, or could be a symptom instead of the source.

## Purpose

Turn debugging into evidence collection instead of guesswork.

The goal is not to try clever patches quickly. The goal is to isolate root cause, change the smallest thing that matters, and prove the result.

## Use This Skill When

- a test, build, script, or app behavior is failing
- a bug appears intermittent or hard to explain
- the first fix did not work
- a multi-step system could be breaking at more than one boundary

## Core Law

No fix without root-cause investigation first.

## Workflow

1. Reproduce.
   - capture the exact failure, frequency, and boundary conditions
2. Collect evidence.
   - read errors fully, inspect logs, and add instrumentation where signal is missing
3. Trace backwards.
   - walk from the symptom to the first bad value, state transition, config, or side effect
4. Change the narrowest thing.
   - patch the cause, not the surface symptom
5. Verify on purpose.
   - rerun the failing path, then the nearest regression checks

## Non-Negotiables

- Never describe a theory as a fact until the evidence supports it.
- Never hide uncertainty behind big confident language.
- Never stack speculative fixes together when one proving change would teach more.
- If reproduction is missing, say so explicitly and switch to evidence-gathering mode.

## Deliverable

Close with:

- the reproduction or observation path
- the proven root cause
- the fix applied
- the commands or checks used to verify the result
