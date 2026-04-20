# Architecture Routing

Use this before changing frontend structure.

## Route By Problem

- component complexity: simplify boundaries and props first
- data fetching and mutation: make ownership and loading states explicit
- performance concerns: inspect rendering and bundle behavior before memoizing blindly
- feature growth: prefer clear feature slices over giant shared buckets
