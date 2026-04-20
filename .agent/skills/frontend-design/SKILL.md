---
name: frontend-design
description: ALWAYS use this for any page, landing page, dashboard, component system, redesign, UI polish, motion work, typography choice, color system, or frontend visual-direction task, even if the user does not explicitly say design.
---

# Frontend Design

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Always read `references/ux-psychology.md` first.

Read these only when relevant:

- `references/color-system.md` for palette and contrast decisions
- `references/typography-system.md` for font pairing and scale
- `references/visual-effects.md` for depth, gradients, and effects
- `references/animation-guide.md` for motion behavior
- `references/motion-graphics.md` for advanced motion work
- `references/decision-trees.md` for context-specific direction
- `references/ui-guardrails.md` for Tailwind, component, and interaction-quality guardrails

## Core Approach

- Start with purpose, audience, content, brand constraints, and technical context.
- Ask one concise question only when a missing detail will materially change the direction.
- Pick a deliberate aesthetic and carry it through typography, color, layout, surfaces, motion, and copy tone.
- Produce real design decisions or working UI code, not vague mood-board language.

## Workflow

1. Define constraints.
   - Identify the user, key action, content readiness, brand limits, and technical stack.
   - Decide whether this is a new build, a redesign, or a polish pass.
2. Choose a direction.
   - Commit to a point of view such as editorial, brutalist, luxury, playful, industrial, retro-futuristic, or organic.
   - Decide what should feel memorable within a few seconds.
3. Build hierarchy.
   - Set reading order, CTA priority, grouping, and density before styling.
   - Use progressive disclosure when there are many options.
4. Design the system.
   - Define typography, color roles, spacing rhythm, shape language, backgrounds, states, and motion together.
5. Implement and review.
   - Verify responsiveness, accessibility, performance, and distinctiveness before finishing.

## Non-Negotiables

- Preserve the established visual language when working inside an existing product or design system.
- Make the result work on both desktop and mobile.
- Use CSS variables or tokens for core design decisions.
- Design real states: hover, focus, active, loading, empty, success, error, and disabled.
- Keep copy human and specific.

## Avoid Generic Output

- Do not default to Inter, Roboto, Arial, or bland system typography unless the product already uses them.
- Do not default to purple-on-white gradients, dark-neon dashboards, mesh blobs, glassy SaaS cards, or Vercel-like layouts.
- Do not use bento grids, split heroes, or rounded-everything unless the content actually benefits from them.
- Do not reuse the same visual recipe across projects.

## UX Principles

- Apply Hick's Law to reduce simultaneous choices.
- Apply Fitts's Law to make important actions easy to hit.
- Apply Miller's Law to chunk dense information.
- Apply Von Restorff to make the primary action stand out.
- Support visceral, behavioral, and reflective quality:
  - visceral: strong first impression
  - behavioral: obvious and smooth to use
  - reflective: memorable after use

## Implementation Standards

- Produce production-ready UI code rather than pseudo-code.
- Match complexity to the chosen aesthetic.
- Favor a few strong motion moments over constant micro-animation.
- Respect reduced-motion and accessibility needs.
- Use the existing component system first, and use accessible primitives for keyboard or focus-heavy interactions.
- Prefer composited motion, intentional z-index scales, and mobile-safe viewport handling over flashy effects.

## Review Checklist

- Is the visual direction obvious quickly?
- Is the primary action unmistakable?
- Does the layout support the content?
- Does the work feel specific to the context instead of template-like?
- Are typography, spacing, color, and surfaces consistent enough to feel intentional?

## Runtime Scripts

Use these after implementation or during audits:

- `scripts/ux_audit.py`
- `scripts/accessibility_checker.py`
