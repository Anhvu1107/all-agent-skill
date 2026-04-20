---
name: create-pr
description: 'ALWAYS use this when the user mentions Create PR, asks to build, debug, review, document, automate, test, configure, migrate, or make decisions in this domain, or the task clearly depends on Create PR; scope: Alias for sentry-skills:pr-writer. Apply the bundled workflow, references, scripts, Senior Master standard, and Codex strict review gate before final output.'
---

# Alias: create-pr

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

This skill name is kept for compatibility.

## When to Use
- The user explicitly asks for `create-pr` or refers to the legacy skill name.
- You need to redirect pull request creation work to the canonical `sentry-skills:pr-writer` workflow.
- The task is specifically about writing or updating a pull request rather than general git operations.

Use `sentry-skills:pr-writer` as the canonical skill for creating and editing pull requests.

If invoked via `create-pr`, run the same workflow and conventions documented in `sentry-skills:pr-writer`.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
