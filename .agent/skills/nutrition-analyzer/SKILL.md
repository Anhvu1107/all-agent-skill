---
name: nutrition-analyzer
description: 'ALWAYS use this when the request matches Nutrition Analyzer: 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。'
---

# 营养分析器技能

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
