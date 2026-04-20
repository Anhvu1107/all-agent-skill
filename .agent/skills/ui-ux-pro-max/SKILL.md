---
name: ui-ux-pro-max
description: ALWAYS use this for UI and UX direction, design-system choices, landing pages, dashboards, component styling, or stack-specific frontend implementation across React, Next.js, Remix, Svelte, SvelteKit, Astro, Vue, Nuxt, Expo Router, React Native, Flutter, SwiftUI, Jetpack Compose, and shadcn.
---

# UI/UX Pro Max

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/stack-routing.md`
- `references/design-review-checklist.md`

Use `references/stack-routing.md` first to choose the most relevant stack data file and avoid loading irrelevant framework guidance.

## Purpose

Turn vague UI requests into an intentional design system plus implementation guidance that matches the actual frontend stack.

## Use This Skill When

- the user asks for any page, component, dashboard, landing page, redesign, polish pass, design system, or frontend visual direction
- the task includes typography, color, spacing, hierarchy, motion, accessibility, or stack-specific UI implementation
- you need to avoid generic AI-looking frontend output while still shipping something practical

## Data Coverage

This skill now includes curated searchable guidance for 16 stacks:

- `html-tailwind`
- `react`
- `nextjs`
- `remix`
- `astro`
- `vue`
- `nuxtjs`
- `nuxt-ui`
- `svelte`
- `sveltekit`
- `shadcn`
- `expo-router`
- `react-native`
- `flutter`
- `swiftui`
- `jetpack-compose`

## Workflow

1. Classify the UI job.
   - landing page, dashboard, app shell, feature surface, component system, or redesign
2. Choose the stack.
   - use `references/stack-routing.md` if the stack is implied but not named
3. Generate the design system.
   - run the bundled search tool with `--design-system`
4. Pull the stack-specific guidance.
   - run a stack search for the framework and product type
5. Review before finalizing.
   - use `references/design-review-checklist.md`

## Commands

From the repository root:

```bash
python .agent/skills/ui-ux-pro-max/scripts/search.py "b2b analytics dashboard" --design-system -p "Northstar"
python .agent/skills/ui-ux-pro-max/scripts/search.py "dashboard tables filters" --stack remix
python .agent/skills/ui-ux-pro-max/scripts/search.py "routing navigation optimistic forms" --stack sveltekit
```

If you are already inside the skill folder, use `python scripts/search.py ...`.

## Rules

- Default to the actual product context, not whatever style looks trendy.
- Match the stack guidance to the framework in use before inventing patterns.
- Prefer accessible, responsive, production-grade UI over pretty-but-fragile demos.
- When working in an existing design system, preserve established patterns before introducing a new direction.
