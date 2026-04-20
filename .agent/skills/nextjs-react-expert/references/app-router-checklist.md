# App Router Checklist

Use this file when reviewing a Next.js App Router codepath.

## Server And Client Boundaries

- Is this component client-only for a real reason?
- Can data fetching happen on the server?
- Is client state used only where ownership truly belongs on the client?

## Data Fetching

- Are independent calls parallelized?
- Are suspense boundaries placed where they help UX?
- Are cache semantics explicit enough to be predictable?

## Bundle Discipline

- Are large libraries or heavy widgets isolated?
- Are client components leaking into parent trees unnecessarily?
- Is the route shipping more JavaScript than the UX requires?

## Rendering

- Are long lists virtualized when needed?
- Are expensive derived values recalculated too often?
- Are layout shifts and loading transitions being handled intentionally?

## Verification

- What metric or observation proves the path improved?
- Was the improvement route-level or only synthetic?
