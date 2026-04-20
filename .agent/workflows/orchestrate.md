---
description: Coordinate multi-domain work as a structured engineering program. Use for broad, high-impact, or cross-functional tasks that need explicit lanes, sequencing, and integration.
---

# /orchestrate - Multi-Domain Delivery

$ARGUMENTS

## Purpose

Use this workflow when the task is too broad for one narrow skill and should be run like a small engineering program.

## Default Model

Think in lanes, not in chaos:

- product framing
- architecture
- implementation
- QA and review
- release or operations

The number of agents or specialists depends on the task. There is no fake minimum.

## Flow

1. Clarify the outcome.
   - user goal
   - constraints
   - acceptance criteria
2. Choose the primary lane owner.
   - usually `workspace-operating-system`, `architecture`, or `app-builder`
3. Define supporting lanes only where needed.
   - frontend
   - backend
   - database
   - QA
   - security
   - devops
4. Decide whether the work needs:
   - planning first
   - isolated branch work
   - end-to-end delivery
5. Execute lane by lane or in parallel where safe.
6. Integrate the results.
7. Verify the final outcome with evidence.

## Branch Policy

- Non-trivial implementation should happen on a dedicated branch or worktree.
- Do not turn orchestration into direct-to-main execution.

## Output

Before implementation, provide:

- task summary
- lanes selected
- primary skill stack
- branch strategy
- verification plan

After implementation, provide:

- what changed
- what was verified
- what remains open
- recommended next step such as PR, staging, or production approval
