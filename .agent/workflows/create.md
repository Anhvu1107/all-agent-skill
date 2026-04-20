---
description: Create a new application or product increment from idea to initial verified slice. Use for net-new builds that need discovery, architecture, implementation, and validation.
---

# /create - New Product Or App

$ARGUMENTS

## Purpose

Turn a rough idea into a credible first delivery path.

## Flow

1. Frame the request.
   - who it is for
   - what outcome matters
   - what must be true in the first version
2. Choose the build path.
   - use `app-builder` for shape and stack
   - add `architecture` if the system boundary is unclear
   - add domain skills only when they clearly matter
3. Define the first delivery slice.
   - not the whole fantasy
   - the smallest useful version that proves the direction
4. Isolate the work.
   - create a branch or worktree for non-trivial implementation
5. Implement the first slice.
6. Verify the slice locally with the most relevant checks.
7. Report:
   - what exists now
   - what was proven
   - what the next slice should be

## Notes

- Ambitious ideas should become staged programs, not one-shot promises.
- Prefer a vertical slice that proves value over scaffolding everything at once.
