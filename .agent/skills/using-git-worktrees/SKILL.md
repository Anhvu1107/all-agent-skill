---
name: using-git-worktrees
description: ALWAYS use this when the task is risky, parallel, branch-oriented, or likely to mix with unrelated local changes unless it happens inside an isolated worktree.
---

# Using Git Worktrees

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Start with `references/worktree-layouts.md`.

Use it before creating the worktree so path layout, ignore rules, branch naming, and cleanup expectations are decided up front.

## Purpose

Create a clean execution surface without disturbing the current checkout.

## Workflow

1. Inspect repo state and local changes.
2. Choose the base branch and branch name.
3. Create the worktree in an ignored, intentional location.
4. Verify baseline health before editing.
5. Do the task inside the worktree.
6. Hand off to `finishing-a-development-branch` when the work appears complete.

## Rules

- Never create tracked project directories for worktrees.
- Never silently mix unrelated dirty state into a new task.
- Never assume direct-to-main is acceptable.
