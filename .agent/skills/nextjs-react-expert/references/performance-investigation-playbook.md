# Performance Investigation Playbook

Use this file when a React or Next.js task needs a disciplined performance investigation rather than random tweaks.

## Investigation Order

1. Reproduce the slow path.
2. Measure the real bottleneck.
3. Classify it.
   - network waterfall
   - client bundle size
   - server latency
   - rerender churn
   - rendering cost
   - cache misuse
4. Fix the highest-impact issue first.
5. Re-measure.

## Measurement Sources

- browser network waterfall
- React Profiler
- Next.js route timings
- bundle analysis
- server logs and timings
- Web Vitals or real-user metrics when available

## Symptom Map

- slow initial page load
  - suspect waterfalls, server latency, or excess client JS
- interaction lag
  - suspect rerender churn or heavy client components
- inconsistent page speed
  - suspect cache misses, unstable data dependencies, or expensive fan-out
- large route bundle
  - suspect broad imports, client boundary spread, or oversized libraries

## Fix Order

- remove sequential fetches
- move work to the server when the client does not need ownership
- trim shipped JavaScript
- tighten cache behavior
- address rerender hotspots
- optimize rendering and hot paths last

## Senior Red Flags

- adding memoization before identifying why rerenders happen
- moving more code client-side to "simplify" data flow
- optimizing isolated helpers while route-level waterfalls remain
- claiming improvement without before-and-after evidence
