# Usage Routing

Use this file before doing substantive work with `context-fundamentals`.

## Trigger Summary

Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, tool definitions, retrieved documents, message history, and tool outputs.

## Start Here

- Read `SKILL.md` first for the inherited operating instructions.
- Load only the root docs or bundled resources that match the user's task.
- Root markdown docs found at generation time: No root markdown companion docs were present when this wrapper was generated.
- No bundled scripts were present when this wrapper was generated.
- No bundled assets were present when this wrapper was generated.

## Scope Control

- Keep the skill's original domain boundaries intact.
- Do not turn a narrow tool skill into a general-purpose answer.
- If the request touches legal, medical, security, finance, privacy, or production systems, surface uncertainty and verify with authoritative sources or local evidence.
