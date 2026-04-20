---
name: nextjs-react-expert
description: ALWAYS use this when the work is specifically about modern Next.js or React architecture, data flow, rendering strategy, routing, or performance-sensitive frontend behavior.
---

# Next.js And React Expert

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Pick the narrowest file that matches the current bottleneck:

- `references/performance-investigation-playbook.md` to structure the investigation
- `references/app-router-checklist.md` when reviewing App Router boundaries, fetching, and caching
- `1-async-eliminating-waterfalls.md` for sequential data-fetching and request chains
- `2-bundle-bundle-size-optimization.md` for large bundles and slow interactivity
- `3-server-server-side-performance.md` for SSR and server-route performance
- `4-client-client-side-data-fetching.md` for client cache and request behavior
- `5-rerender-re-render-optimization.md` for excessive re-renders
- `6-rendering-rendering-performance.md` for rendering bottlenecks and large lists
- `7-js-javascript-performance.md` for hot-path JavaScript issues
- `8-advanced-advanced-patterns.md` for advanced React execution patterns
- `9-cache-components.md` for Next.js 16 cache components and partial prerendering

## Purpose

Improve React and Next.js systems by fixing the highest-impact bottlenecks first.

Do not micro-optimize while bigger issues like waterfalls, bundle bloat, or bad boundaries remain.

## Use This Skill When

- a page or flow feels slow and the bottleneck is not yet isolated
- React code re-renders too often
- Next.js data fetching or rendering strategy needs review
- bundle size or client JavaScript volume is harming user experience
- modern Next.js caching choices need to be made deliberately

## Priority Order

1. Eliminate waterfalls.
2. Reduce unnecessary shipped JavaScript.
3. Fix bad server-client boundaries.
4. Tackle rerender and rendering hotspots.
5. Only then consider lower-level JavaScript polish.

## Review Heuristics

- Prefer server work when the client does not need ownership.
- Keep data fetching parallel where dependencies allow.
- Ship less code before trying to execute shipped code faster.
- Measure before and after when possible.
- Do not add memoization by reflex; fix structure first.

## Common Focus Areas

- route-level waterfalls
- oversized client components
- unnecessary client state
- missing streaming or suspense boundaries
- poor cache behavior
- list rendering and virtualization problems

## Good Outcomes

A strong performance pass should end with:

- the main bottleneck identified
- the chosen optimization path explained
- the relevant checks run or recommended
- the codebase left simpler, not just trickier

## Related Skills

- `frontend-design` when UX and implementation quality interact
- `web-design-guidelines` for interface-level audits
- `performance-profiling` for broader measurement strategy
- `api-patterns` when backend shape is creating frontend waterfalls
