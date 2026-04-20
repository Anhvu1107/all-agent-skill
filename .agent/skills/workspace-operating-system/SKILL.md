---
name: workspace-operating-system
description: ALWAYS use this for broad, ambiguous, multi-step, or repository-wide work in this bundle, especially when the right skill choice, execution order, or quality bar is not obvious from the request alone.
---

# Workspace Operating System

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`

Then load only the references, scripts, assets, or examples needed for the user's actual task.


## Purpose

Act as the default operating layer for this repository.

Before doing substantial work, classify the task, choose the minimum effective skill set, sequence execution, and enforce the quality bar.

## Mandatory Reading Order

Always read:

1. `references/task-routing.md`
2. `references/quality-bar.md`
3. `references/operating-charter.md`

Read only when needed:

- `references/composition-patterns.md` for cross-domain or multi-phase work
- `references/routing-heuristics.md` when the request wording is vague but the outcome is high-impact
- `references/quality-audit.md` when reviewing whether bundle or repository work is actually ready to ship
- `references/skill-catalog.md` when the right skill is unclear or you need exhaustive coverage
- `references/branch-and-release-policy.md` for code, config, infrastructure, release, or deployment work
- `references/idea-to-program-playbook.md` when the request starts as a vision, pitch, or broad ambition
- `references/department-operating-model.md` when the task should be run like a coordinated team effort

## Runtime Assets

- `scripts/build_skill_catalog.py`
  - Run this after adding, removing, or meaningfully re-categorizing skills so `references/skill-catalog.md` stays synchronized with the live bundle.

## Operating Rules

- Start narrow. Load the fewest skills that can reliably solve the task.
- Prefer one primary skill and only add supporting skills when there is clear value.
- Default to local-first execution. Do not assume external MCP servers, cloud APIs, or provider-specific tooling are enabled unless the user or repo explicitly configures them.
- Preserve existing product patterns before introducing a new visual, architectural, or workflow direction.
- Treat licensing, ownership, and privacy as part of correctness. If a file or asset is restrictive or unclear for public reuse, isolate it or remove it instead of shipping ambiguity.
- Operate like a senior engineering team: clarify the outcome, isolate the work, verify with evidence, and leave a clean handoff trail.
- For speculative or ambitious ideas, convert them into requirements, simulation, prototype, and verification tracks instead of pretending they are instantly production-ready.
- Do not support weaponization, malware, unauthorized access, covert surveillance, or guaranteed-finance claims. Pivot to lawful, defensive, or simulation-first alternatives.
- Convert vague requests into a concrete execution path quickly; ask only when the missing detail changes the outcome materially.
- Move from discovery to action to validation. Do not stop at analysis for executable tasks.

## Execution Ladder

1. Classify the request.
   - Decide whether the task is primarily planning, building, debugging, reviewing, designing, testing, documenting, or shipping.
2. Choose the primary skill.
   - Use `references/task-routing.md` first.
3. Add support skills only if required.
   - Use `references/composition-patterns.md` when multiple skills must work together.
4. Execute.
    - Gather just enough context to avoid blind edits.
    - Implement or analyze with the chosen skill stack.
    - For code changes, prefer a branch or worktree unless the task is truly tiny and the repo policy allows in-place work.
5. Verify.
    - Apply the universal finish criteria from `references/quality-bar.md`.
6. Close clearly.
    - State what changed, what was verified, and any residual risk.

## Routing Heuristics

- For broad product work, start with the task shape rather than the technology.
- For highly regulated or physically grounded ideas, start by separating concept, simulator, prototype, and production scope.
- For mission-style or hardware-adjacent software, route to `systems-engineering` before collapsing the problem into normal app delivery.
- For coding tasks, route by the real bottleneck:
  - architecture unclear -> `architecture`
  - system-of-systems, telemetry, simulation, operator workflows, or interface-heavy scope -> `systems-engineering`
  - implementation heavy -> domain skill such as `app-builder`, `api-patterns`, `frontend-design`, or `database-design`
  - approved plan exists -> `executing-plans`
  - explicit acceptance criteria and end-to-end closure matter -> `closed-loop-delivery`
  - failing behavior -> `systematic-debugging` plus the relevant domain skill
  - validation gap -> `testing-patterns`, `webapp-testing`, `lint-and-validate`, `performance-profiling`, or `verification-before-completion`
- For document and communication work, prefer `doc-coauthoring` or `internal-comms` plus brand and design support rather than opaque one-off scripts.

## Composition Rules

- One-domain request: use one primary skill.
- Two-domain request: use one primary and one support skill.
- Three or more domains: read `references/composition-patterns.md` and actively sequence the work.
- If the task is unclear but high-impact, begin with planning or discovery before implementation.

## High-Value Defaults

- New feature: plan -> design/architecture -> build -> test -> polish
- Bug fix: reproduce -> debug -> patch -> verify -> summarize cause
- Non-trivial code change: branch/worktree -> implement -> verify -> PR/merge recommendation
- Review request: prioritize risks, regressions, and missing validation over style commentary
- Review feedback request: use `receiving-code-review` before making broad changes
- UI request: clarify direction, preserve usability, and avoid generic output
- Infrastructure or deployment request: favor explicit validation and rollback awareness
- Ambitious R&D request: architecture -> simulation/prototype -> verification strategy -> staged delivery plan
- Ambitious systems request: idea framing -> systems-engineering -> architecture -> first simulation or control slice -> verification
- Repository hardening request: audit -> remove restricted material -> neutralize external defaults -> verify -> document

## Relationship To Other Skills

- Use `intelligent-routing` for agent-selection patterns and auto-routing heuristics.
- Use `parallel-agents` for multi-agent decomposition when the environment supports it.
- Use `behavioral-modes` to adapt how you communicate and reason.
- Use `skill-creator` when modifying this bundle or adding new skills.
- Use `using-git-worktrees` when isolated branch work is safer than editing in place.
- Use `finishing-a-development-branch` when a verified branch needs a clean next-step decision.

## Finish Condition

This skill is successful only when the agent can answer:

- Why this skill stack?
- Why this sequence?
- What was verified?
- What still remains uncertain?
