---
name: claude-code-expert
description: 'ALWAYS use this when the request matches Claude Code Expert: Especialista profundo em Claude Code - CLI da Anthropic.'
---

# CLAUDE CODE EXPERT - Potencia Maxima

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, examples, or detailed instructions that match the user's actual task.

## Progressive Disclosure

- Read `references/full-skill-instructions.md` only when the task needs the full original upstream guidance.
- Prefer bundled scripts for deterministic or repetitive operations when they exist.
- Reuse bundled assets instead of inventing substitutes when assets are present.
- Keep final answers aligned with this skill's frontmatter trigger, Senior Master standard, and Codex strict review gate.
