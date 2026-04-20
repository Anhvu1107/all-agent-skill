---
name: template-skill
description: ALWAYS use this when the user asks for a minimal reusable SKILL.md template, official skill scaffold shape, or a starting skeleton for a new skill; treat it as a template artifact, not as a domain execution skill.
---

# Template Skill

Use this as the minimal upstream template shape for creating a new skill. Prefer the full `skill-creator` workflow for production skill authoring, then use this template only when the user explicitly wants the raw skeleton or a compact example of the required `SKILL.md` structure.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Template Usage

When adapting this template:

- Replace the frontmatter `name` with a lowercase hyphenated skill folder name.
- Replace `description` with an aggressive trigger statement that says exactly when the skill must be used.
- Keep the body short and procedural.
- Move detailed examples, policies, schemas, or long domain guidance into `references/`.
- Add scripts only when deterministic repeatability matters.
- Validate the final skill before packaging.

