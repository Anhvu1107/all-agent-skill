# Usage Routing

Use this file before doing substantive work with `notebooklm`.

## Trigger Summary

Interact with Google NotebookLM to query documentation with Gemini's source-grounded answers. Each question opens a fresh browser session, retrieves the answer exclusively from your uploaded documents, and closes.

## Start Here

- Read `SKILL.md` first for the inherited operating instructions.
- Load only the root docs or bundled resources that match the user's task.
- Root markdown docs found at generation time: `AUTHENTICATION.md`, `CHANGELOG.md`, `README.md`
- Use `scripts/` for repeatable or deterministic work when present.
- No bundled assets were present when this wrapper was generated.

## Scope Control

- Keep the skill's original domain boundaries intact.
- Do not turn a narrow tool skill into a general-purpose answer.
- If the request touches legal, medical, security, finance, privacy, or production systems, surface uncertainty and verify with authoritative sources or local evidence.
