---
description: Debug workflow for reproducing issues, isolating root cause, applying the minimum relevant fix, and proving the behavior changed.
---

# /debug - Root-Cause Debugging

$ARGUMENTS

## Purpose

Use this workflow when the job is to understand a failure before changing code.

## Default Stack

- `systematic-debugging`
- relevant domain skill for the failing area
- `verification-before-completion`

## Flow

1. Define the symptom.
   - what is failing
   - expected vs actual behavior
2. Reproduce it.
   - steps, environment, frequency
3. Isolate the cause.
   - scope the failing area
   - check recent changes, logs, inputs, and state transitions
4. Prove the root cause.
   - do not stop at a plausible theory
5. Apply the minimum relevant fix.
6. Verify the symptom is gone and nearby behavior still works.
7. Report:
   - root cause
   - fix
   - verification
   - prevention note

## Guardrails

- Do not fix blindly before reproduction or evidence.
- Do not make unrelated UI, logic, or refactor changes while debugging.
- Do not claim success until the old symptom is disproven by fresh evidence.
- If the issue cannot be reproduced, say that clearly and shift to evidence gathering instead of guessing.

## Good Output

A strong debug result includes:

- reproduction path
- root-cause explanation
- minimal fix summary
- exact verification performed
- residual risk if any
