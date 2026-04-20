---
name: dispatching-parallel-agents
description: ALWAYS use this when there are two or more independent investigations, failures, or implementation slices that can be worked in parallel without shared-state collisions.
---

# Dispatching Parallel Agents

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/independence-checklist.md`
- `references/prompt-template.md`

Use the checklist first. Only dispatch after you can name what stays local, what goes parallel, and what file or problem boundary each agent owns.

## Purpose

Use parallelism to create momentum, not chaos.

## Use This Skill When

- several failures clearly belong to different subsystems
- multiple research questions can be answered independently
- isolated test files or implementation slices do not share writes
- your next local step is still clear while sidecar work happens elsewhere

## Core Rule

Do the immediate blocking step locally. Parallelize only the bounded sidecar work.

## Workflow

1. Identify the local critical path.
2. Group sidecar tasks by failure domain or write scope.
3. Confirm independence.
4. Write a tight task packet for each agent.
5. Keep working locally while they run.
6. Integrate, verify, and resolve conflicts explicitly.

## Good Targets

- isolated failing test files
- repo exploration for a specific question
- one-module patches with clear ownership
- review passes that do not block immediate coding

## Bad Targets

- the very answer you need before you can continue
- overlapping write surfaces
- vague asks like "figure out the task"
- duplicate analysis you are already doing locally
