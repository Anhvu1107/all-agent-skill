---
name: architecture
description: ALWAYS use this when the hard part is choosing system shape, boundaries, services, modules, tradeoffs, scaling direction, or refactor strategy before implementation starts.
---

# Architecture

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/decision-playbook.md`
- `context-discovery.md`

Read only what the task needs after that:

- `references/adr-checklist.md` for formal decision records and architecture sign-off
- `trade-off-analysis.md` for ADRs, option comparison, and decision records
- `pattern-selection.md` for architecture and service-pattern choices
- `patterns-reference.md` for quick pattern lookup
- `examples.md` when a concrete product shape helps

## Purpose

Use architecture work to reduce future rework, not to make the system look sophisticated on paper.

Good architecture makes the next implementation decisions easier, clearer, and safer.

## Use This Skill When

- requirements are clear enough to design, but the shape of the system is not
- multiple architectures could work and tradeoffs need to be made explicit
- a team needs guidance on boundaries, modules, services, or data flow
- a refactor could change how core parts of the system fit together

## Core Workflow

1. Clarify the real job.
   - user outcome, constraints, scale, team, delivery pressure
2. Identify architecture pressure points.
   - reliability, latency, complexity, change frequency, security, integrations
3. Generate a small option set.
   - usually 2 or 3 realistic paths
4. Compare tradeoffs openly.
   - complexity, speed, cost, operability, learning curve, future flexibility
5. Recommend the smallest architecture that clears the constraints.
6. Capture the decision.
   - ADR, concise rationale, and what would change the recommendation later

## Design Heuristics

- Start with a monolith unless there is a proven reason not to.
- Prefer explicit boundaries over early service sprawl.
- Let change frequency influence module boundaries.
- Optimize first for correctness and maintainability, then for scale that is actually expected.
- Match architecture to team capacity, not just to technical possibility.

## Output Standard

An architecture answer should leave the reader with:

- the recommended shape
- the rejected alternatives and why
- the main tradeoffs
- the next implementation implications

## Related Skills

- `app-builder` when the architecture should flow directly into building the app
- `api-patterns` for service and contract design
- `database-design` for schema and data-boundary decisions
- `deployment-procedures` when runtime topology and release flow matter
