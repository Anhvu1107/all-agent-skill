# Usage Guide

Vietnamese version: `HUONG_DAN_SU_DUNG.md`

This file is the fast entry point for using `agent-skills-unified` without reading the entire repo first.

## Goal

This bundle is designed so both humans and other AIs can enter the repo, understand what to read first, choose the right skills, follow the right order, and check quality before finishing.

## Fastest Way To Start

If you are not sure which skill to use, start with:

```text
Use $workspace-operating-system to decide the right skill stack for this task.
```

This is the central skill. It helps an AI:

- classify the task
- choose the primary and supporting skills
- decide the execution order
- remember to verify before finishing
- keep coding work on a branch-first, review-first, release-aware flow
- preserve safe and lawful boundaries for sensitive work

## When To Use The Central Skill

Start with `$workspace-operating-system` when:

- the task is still ambiguous
- the task is large or multi-step
- the task spans multiple domains
- you want the AI to choose the best working process
- you want the AI to explain why it chose a given skill

## If The Idea Is Very Large Or Very Far Out

This bundle can still help, but the AI should handle it like a senior engineer:

- split concept, prototype, simulator, and production
- write requirements, a risk register, and a verification plan first
- build in slices that can actually be checked

This bundle can be especially strong for:

- mission software
- telemetry
- digital twins
- simulation
- control-plane and observability systems

If the idea belongs to that class of large systems, invoke:

```text
Use $systems-engineering to turn this system idea into a mission brief, subsystem map, simulation-first plan, and first verifiable software slice.
```

It must not be used to support:

- weapons, missiles, or targeting workflows
- malware, unauthorized data access, or exfiltration
- non-consensual human surveillance
- "always-win" trading promises

## When To Call A Specialist Skill Directly

Call a specialist skill directly when you already know what needs to be done.

Examples:

- UI, landing page, component:
```text
Use $frontend-design to redesign this page and keep the UX clear.
```

- browser testing, web flow verification:
```text
Use $webapp-testing to inspect the app and verify the main user flow.
```

- MCP server implementation:
```text
Use $mcp-builder to design and implement an MCP server for this API.
```

- API design:
```text
Use $api-patterns to design this endpoint and response format.
```

- database schema:
```text
Use $database-design to propose the schema and indexing strategy.
```

- debugging:
```text
Use $systematic-debugging to find the root cause of this issue.
```

- plan already exists and you want strict execution:
```text
Use $executing-plans to follow this plan step by step and verify each stage.
```

- you want true end-to-end completion with clear acceptance criteria:
```text
Use $closed-loop-delivery to finish this task end to end and prove the result.
```

- processing review comments:
```text
Use $receiving-code-review to triage these comments, fix valid issues, and verify them.
```

- code review:
```text
Use $code-review-checklist to review these changes for bugs and risks.
```

## Practical Rules

1. If unsure, start with `$workspace-operating-system`.
2. If the domain is already clear, call the primary skill directly.
3. For larger tasks, let the AI compose multiple skills in order.
4. For code tasks, always require verification or tests after changes.
5. For reviews, prioritize bugs, regressions, and missing tests before style.
6. If a task already has a plan, use `$executing-plans` instead of letting the AI reinvent the plan while executing it.
7. If a task must truly be finished, add `$verification-before-completion` or call `$closed-loop-delivery` directly.
8. Non-trivial coding tasks should usually happen on a dedicated branch or worktree.
9. Before merge or deploy, the AI should clearly say which branch it is on, what it verified, and what the next step is.
10. High-risk tasks should explicitly separate prototype, simulation, and production claims.

## Recommended Flows

### 1. New Task Or Multi-Domain Task

```text
Use $workspace-operating-system to choose the right skills and execution order for building this feature.
```

### 2. UI Task

```text
Use $frontend-design to define the visual direction, hierarchy, and implementation approach for this interface.
```

### 3. Bug Task

```text
Use $workspace-operating-system to route this bug, then use the right debugging and verification skills.
```

### 4. Review Feedback Task

```text
Use $receiving-code-review to process these review comments, apply valid fixes, and verify them.
```

### 5. Review Task

```text
Use $workspace-operating-system to choose the right review stack, then review this code with a risk-first mindset.
```

### 6. Execute An Existing Plan

```text
Use $executing-plans to implement this approved plan without drifting from scope.
```

### 7. Finish A Task Properly

```text
Use $closed-loop-delivery to finish this task end to end and only stop when the acceptance criteria are proven.
```

### 8. Docs, Briefs, Or Clarity-Focused Content

Use writing and coordination skills:

- `$doc-coauthoring`
- `$internal-comms`
- add `$brand-guidelines` if brand voice needs to stay consistent

## Structure To Know

- `.agent/skills/`
  - the primary skill library and the only canonical skill tree
- `.agent/agents/`
  - specialists by role
- `.agent/workflows/`
  - coordination workflows
- `.agent/skills/workspace-operating-system/`
  - the central routing skill
- `.agent/skills/workspace-operating-system/references/task-routing.md`
  - quick map from task type to the right skill
- `.agent/skills/workspace-operating-system/references/composition-patterns.md`
  - ways to combine multiple skills
- `.agent/skills/workspace-operating-system/references/quality-bar.md`
  - minimum completion standard
- `.agent/skills/workspace-operating-system/references/operating-charter.md`
  - senior-team operating model plus ambitious and sensitive-task boundaries
- `.agent/skills/workspace-operating-system/references/branch-and-release-policy.md`
  - branch-first, PR-first, and merge/promotion flow
- `.agent/skills/workspace-operating-system/references/idea-to-program-playbook.md`
  - turns large ideas into briefs, milestones, and verification slices
- `.agent/skills/workspace-operating-system/references/department-operating-model.md`
  - operating lanes for product, architecture, build, QA, security, and ops
- `.agent/skills/workspace-operating-system/references/skill-catalog.md`
  - full list of available skills

## Copy-Ready Prompt Templates

### General Prompt

```text
Use $workspace-operating-system to understand this request, pick the minimum effective skill stack, do the work, and verify the result before finishing.
```

### Feature Build Prompt

```text
Use $workspace-operating-system to build this feature end-to-end, including planning, implementation, and verification.
```

### Ambitious Idea Prompt

```text
Use $workspace-operating-system to turn this ambitious idea into a real engineering program with requirements, architecture, prototype scope, verification strategy, and staged delivery.
```

### Large-System Prompt

```text
Use $systems-engineering to shape this mission-style system into interfaces, telemetry, simulation boundaries, operator workflows, and a first verifiable delivery slice.
```

### Bug-Fix Prompt

```text
Use $workspace-operating-system to route this issue, identify the root cause, patch it, and verify the fix.
```

### UI Prompt

```text
Use $frontend-design to improve this UI with a stronger visual direction and better UX clarity.
```

### Web Verification Prompt

```text
Use $webapp-testing to inspect the app, discover selectors, and verify the key user journeys.
```

## How To Upgrade Later

If you add or update a skill:

1. update that skill's `SKILL.md`
2. if the skill is substantial, add `agents/openai.yaml`
3. rebuild the catalog:

```text
python .agent/skills/workspace-operating-system/scripts/build_skill_catalog.py
```

## Important Notes

- This bundle is ready to use now.
- There is now only one canonical skill tree: `.agent/skills/`.
- This repo has been truly merged; there are no longer two parallel skill libraries.
- The default repo posture is local-first: no external MCP server is enabled by default.
- Serious coding tasks should follow branch/worktree -> verify -> PR/integration -> main.
- Four restrictive office-file skills were removed from the public version of the bundle.
- The newer workflows were rewritten for the current Codex environment and do not import launcher files or app shells from foreign bundles into the primary skill tree.

## Best Single Opening Line

If you only choose one sentence to start with, use:

```text
Use $workspace-operating-system to decide what to do first, which skills to load, and how to verify the result.
```
