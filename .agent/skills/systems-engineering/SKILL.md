---
name: systems-engineering
description: ALWAYS use this when the request sounds like a platform, robotics stack, digital twin, telemetry-heavy system, operator workflow, simulation-first program, or any software effort that is bigger than normal app delivery.
---

# Systems Engineering

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/mission-software-playbook.md`
- `references/simulation-first-delivery.md`

Read when needed:

- `references/interface-control-checklist.md` for subsystem contracts, operator boundaries, telemetry, and safety checks

## Purpose

Turn big system ideas into disciplined software programs that can be planned, prototyped, simulated, verified, and expanded in stages.

This skill is for work that touches the physical world, operators, mission constraints, or multiple interacting subsystems.

## Use This Skill When

- the idea sounds like a platform, vehicle, mission system, robotics stack, digital twin, or industrial control support system
- the request needs more than a normal web-app architecture
- the software must reason about telemetry, state machines, interfaces, failure modes, or staged verification
- simulation or prototype boundaries matter more than shipping a UI quickly

## Do Not Use This Skill For

- weapon guidance, targeting, ballistic optimization, or kill-chain support
- malware, intrusion, stealth, or exfiltration
- covert surveillance or non-consensual human monitoring
- impossible financial claims such as guaranteed wins

## Core Workflow

1. Frame the mission.
   - users, operators, environment, success criteria, constraints
2. Define the verification boundary.
   - concept, simulator, prototype, lab, staging, field, production
3. Decompose the system.
   - operator layer
   - control plane
   - data and telemetry
   - subsystem interfaces
   - safety and fallback behaviors
4. Define the first software slice.
   - simulator
   - dashboard
   - telemetry pipeline
   - interface contract
   - operator workflow
5. Route to support skills.
   - `architecture`, `api-patterns`, `database-design`, `frontend-design`, `closed-loop-delivery`
6. Deliver with evidence.
   - simulation traces, test matrix, runtime proof, or interface validation

## Output Standard

A good result should leave the team with:

- a mission or system brief
- a subsystem map
- an explicit prototype or simulation boundary
- a first delivery slice
- a verification plan
- a realistic next-step program sequence

## Related Skills

- `workspace-operating-system` for overall routing and governance
- `architecture` for system shape and tradeoffs
- `app-builder` when the systems work still resolves into a product or app surface
- `closed-loop-delivery` when the first slice should be driven to proven completion
