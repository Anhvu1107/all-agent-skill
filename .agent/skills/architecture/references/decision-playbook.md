# Architecture Decision Playbook

Use this file when an architecture answer must survive scrutiny from experienced engineers, not just sound plausible.

## Outcome First

Start every architecture discussion by writing down:

- user or business outcome
- latency, reliability, and compliance constraints
- team size and skill profile
- delivery horizon
- expected change frequency

If these are missing, the architecture discussion is under-specified.

## Pressure Map

Map the system by pressure, not by technology fashion.

Check these dimensions:

- write-path complexity
- read-path latency and fan-out
- consistency requirements
- failure-isolation needs
- uneven scaling between subsystems
- integration surface with external systems
- operational maturity of the team

## Option Set Rule

Produce 2 or 3 realistic options.

Too few means you are anchoring. Too many means you are avoiding a recommendation.

For each option, capture:

- shape
- why it fits
- main risks
- what would force a change later

## Recommendation Heuristics

Prefer a modular monolith when:

- one team owns most of the system
- transactions span multiple domains
- the domain is still evolving quickly
- operational simplicity matters more than isolated scaling

Prefer distributed boundaries when:

- failure isolation is a first-order concern
- scaling profiles differ materially
- domain ownership is stable across teams
- release cadence must differ by subsystem
- data contracts are already explicit and durable

## Boundary Tests

A proposed boundary is usually good if most of these are true:

- the module changes for a different reason than its neighbors
- it has a coherent data model
- its failure mode is understandable
- it can be tested with clear seams
- ownership can be assigned cleanly

It is usually fake if:

- it exists only because the stack supports it
- it still needs deep cross-boundary transactions everywhere
- the same team will change all parts together anyway
- the domain language is still unstable

## Review Scorecard

Review each option against:

- delivery speed
- maintainability
- operational load
- fault isolation
- scaling headroom
- data consistency cost
- observability complexity
- migration difficulty

Do not collapse these into a single fake score. Use them to explain the tradeoffs.

## Senior-Level Red Flags

- microservices proposed before modular boundaries are stable
- event-driven architecture used to avoid naming synchronous ownership problems
- cache layers added before the source-of-truth path is clear
- "future scale" used without numbers
- "enterprise" used as a synonym for "more moving parts"

## Final Deliverable

A strong architecture recommendation includes:

- recommended option
- rejected options and why
- major tradeoffs
- migration or evolution path
- open questions that would change the decision
