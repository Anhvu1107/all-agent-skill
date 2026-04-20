# Usage Routing

Use this file before doing substantive work with `skill-developer`.

## Trigger Summary

Comprehensive guide for creating and managing skills in Claude Code with auto-activation system, following Anthropic's official best practices including the 500-line rule and progressive disclosure pattern.

## Start Here

- Read `SKILL.md` first for the inherited operating instructions.
- Load only the root docs or bundled resources that match the user's task.
- Root markdown docs found at generation time: `ADVANCED.md`, `HOOK_MECHANISMS.md`, `PATTERNS_LIBRARY.md`, `SKILL_RULES_REFERENCE.md`, `TRIGGER_TYPES.md`, `TROUBLESHOOTING.md`
- No bundled scripts were present when this wrapper was generated.
- No bundled assets were present when this wrapper was generated.

## Scope Control

- Keep the skill's original domain boundaries intact.
- Do not turn a narrow tool skill into a general-purpose answer.
- If the request touches legal, medical, security, finance, privacy, or production systems, surface uncertainty and verify with authoritative sources or local evidence.
