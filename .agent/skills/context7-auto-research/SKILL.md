---
name: context7-auto-research
description: 'ALWAYS use this when the request matches Context7 Auto Research: Automatically fetch latest library/framework documentation for Claude Code via Context7 API.'
---

# context7-auto-research

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Overview
Automatically fetch latest library/framework documentation for Claude Code via Context7 API

## When to Use
- When you need up-to-date documentation for libraries and frameworks
- When asking about React, Next.js, Prisma, or any other popular library

## Installation
```bash
npx skills add -g BenedictKing/context7-auto-research
```

## Step-by-Step Guide
1. Install the skill using the command above
2. Configure API key (optional, see GitHub repo for details)
3. Use naturally in Claude Code conversations

## Examples
See [GitHub Repository](https://github.com/BenedictKing/context7-auto-research) for examples.

## Best Practices
- Configure API keys via environment variables for higher rate limits
- Use the skill's auto-trigger feature for seamless integration

## Troubleshooting
See the GitHub repository for troubleshooting guides.

## Related Skills
- tavily-web, exa-search, firecrawl-scraper, codex-review

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
