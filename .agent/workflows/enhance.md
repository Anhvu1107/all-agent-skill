---
description: Improve an existing project through a controlled change flow. Use for feature additions, refactors, fixes, or upgrades on an established codebase.
---

# /enhance - Improve Existing Project

$ARGUMENTS

## Purpose

Change an existing system without losing control of the baseline.

## Flow

1. Read the current state.
   - current behavior
   - impacted area
   - nearby constraints and dependencies
2. Map the change.
   - what will change
   - what could regress
   - what needs verification
3. Pick the skill stack.
   - primary domain skill first
   - add `closed-loop-delivery`, `systematic-debugging`, or `receiving-code-review` when appropriate
4. Isolate the work.
   - use a branch or worktree for meaningful changes
5. Implement the smallest credible increment.
6. Run focused verification.
7. Close with:
   - change summary
   - verification evidence
   - branch and next-step recommendation

## Notes

- Preserve existing patterns unless there is a clear reason to change them.
- Large changes should be split into deliberate slices instead of one opaque diff.
