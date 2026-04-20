---
name: address-github-comments
description: 'ALWAYS use this when the request matches Address Github Comments: Use when you need to address review or issue comments on an open GitHub Pull Request using the gh CLI.'
---

# Address GitHub Comments

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Overview

Efficiently address PR review comments or issue feedback using the GitHub CLI (`gh`). This skill ensures all feedback is addressed systematically.

## Prerequisites

Ensure `gh` is authenticated.

```bash
gh auth status
```

If not logged in, run `gh auth login`.

## Workflow

### 1. Inspect Comments

Fetch the comments for the current branch's PR.

```bash
gh pr view --comments
```

Or use a custom script if available to list threads.

### 2. Categorize and Plan

- List the comments and review threads.
- Propose a fix for each.
- **Wait for user confirmation** on which comments to address first if there are many.

### 3. Apply Fixes

Apply the code changes for the selected comments.

### 4. Respond to Comments

Once fixed, respond to the threads as resolved.

```bash
gh pr comment <PR_NUMBER> --body "Addressed in latest commit."
```

## Common Mistakes

- **Applying fixes without understanding context**: Always read the surrounding code of a comment.
- **Not verifying auth**: Check `gh auth status` before starting.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
