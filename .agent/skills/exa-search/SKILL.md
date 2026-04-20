---
name: exa-search
description: 'ALWAYS use this when the request matches EXA Search: Semantic search, similar content discovery, and structured research using Exa API.'
---

# exa-search

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Overview
Semantic search, similar content discovery, and structured research using Exa API

## When to Use
- When you need semantic/embeddings-based search
- When finding similar content
- When searching by category (company, people, research papers, etc.)

## Installation
```bash
npx skills add -g BenedictKing/exa-search
```

## Step-by-Step Guide
1. Install the skill using the command above
2. Configure Exa API key
3. Use naturally in Claude Code conversations

## Examples
See [GitHub Repository](https://github.com/BenedictKing/exa-search) for examples.

## Best Practices
- Configure API keys via environment variables

## Troubleshooting
See the GitHub repository for troubleshooting guides.

## Related Skills
- context7-auto-research, tavily-web, firecrawl-scraper, codex-review

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
