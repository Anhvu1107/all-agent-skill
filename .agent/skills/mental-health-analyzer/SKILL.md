---
name: mental-health-analyzer
description: 'ALWAYS use this when the request matches Mental Health Analyzer: 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。'
---

# 心理健康分析技能

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
