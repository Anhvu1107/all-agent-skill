---
name: oral-health-analyzer
description: 'ALWAYS use this when the request matches Oral Health Analyzer: 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。'
---

# 口腔健康分析技能

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
