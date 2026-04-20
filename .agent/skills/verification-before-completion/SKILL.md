---
name: verification-before-completion
description: ALWAYS use this before claiming a fix works, tests pass, code is ready, a PR is ready, or anything is done, merged, or shippable.
---

# Verification Before Completion

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Purpose

Do not claim success from intuition, old output, or partial checks.

The rule is simple: if a statement can be proven, prove it before saying it.

## Use This Skill When

- a fix is about to be described as complete
- tests, lint, build, or runtime behavior are being reported as passing
- a branch is about to be pushed, merged, or handed off
- another agent reported success and you need to trust but verify
- a user asked "is it done?" or "does it work now?"

## Core Law

No completion claim without fresh verification evidence.

Fresh means the evidence was gathered for this exact state of the code or artifact, not for an earlier draft.

## Verification Loop

1. Name the claim.
   - Example: "the bug is fixed" or "all tests pass"
2. Choose the proving action.
   - command, test, browser check, file inspection, diff review, or runtime call
3. Run the smallest complete proof.
   - focused first, broader if risk remains
4. Read the actual result.
   - exit code, failure count, rendered UI, response body, changed lines
5. Report the truth.
   - pass with evidence, or fail with the blocker

## Evidence Patterns

- Test claim
  - Run the relevant test command and report the result.
- Build claim
  - Run the build, not just lint.
- Bug-fix claim
  - Reproduce the old symptom or run the regression test that proves the behavior changed.
- UI claim
  - Open the page, inspect the state, or capture the rendered outcome.
- Delegation claim
  - Review the diff and verify the changed behavior yourself.

## Not Good Enough

- "should work now"
- "looks correct"
- "the code change is straightforward"
- "the subagent said it passed"
- "lint passed so the app is probably fine"
- "I tested something similar earlier"

## Finishing Contract

When closing a task, include:

- what was verified
- how it was verified
- what remains unverified, if anything

If something could not be checked, say that directly instead of implying success.

## Red Flags

Stop and verify if you catch yourself doing any of these:

- celebrating before checking
- using words like "done", "fixed", "clean", or "ready" without evidence
- relying on partial verification for a broader claim
- skipping the final command because "it is obvious"

## Related Skills

- `closed-loop-delivery` for end-to-end execution against acceptance criteria
- `executing-plans` for carrying an approved plan through implementation
- `finishing-a-development-branch` for end-of-branch decision making
