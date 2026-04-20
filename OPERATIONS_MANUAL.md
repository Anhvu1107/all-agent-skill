# Operations Manual

Vietnamese version: `SO_TAY_VAN_HANH.md`

This file is the full manual for `agent-skills-unified`.

If you need a quick start, read `USAGE_GUIDE.md`.
If you want the full picture of how this bundle operates, evolves, hardens, and stays maintainable, read this file.

## 1. Goal

This bundle is not just a skill library.

It is an operating system for AI agents:

- it knows what to read first
- it knows which skill to choose
- it knows when to combine multiple skills
- it knows how to verify before finishing
- it knows how to evolve the bundle without letting it drift into clutter, ambiguity, or poor triggerability

### 1.1 Operating Charter

This bundle is meant to operate like a senior engineering team:

- frame the problem correctly
- separate scope and risk
- choose the right architecture and workflow
- work on a branch or worktree when needed
- verify with evidence
- hand off clearly to a human or another AI

If the idea is too ambitious or too large, it must not pretend to be production-ready.

It must separate:

- concept
- prototype
- simulator
- production
- verification and operations

### 1.2 Safety Boundary

This bundle must not be used to support:

- weapon guidance, targeting, or kill-chain workflows
- malware, credential theft, unauthorized access, or exfiltration
- non-consensual human surveillance
- "always-win" trading claims
- fake verification, fake benchmarks, or fake readiness

If a request touches those areas, it should pivot toward a lawful and safer direction:

- simulation
- telemetry
- verification harnesses
- safety analysis
- risk dashboards

## 2. Recommended Mental Model

Think of this bundle as four layers:

1. `workspace-operating-system`
   - the central orchestration layer
2. `skills/`
   - domain knowledge and workflows
3. `agents/`
   - specialist role prompts
4. `workflows/`
   - command-style or procedure-style entry points

Also include:

- `rules/`
  - global constraints
- `scripts/`
  - helpers and validators
- `.shared/`
  - shared assets

## 3. Canonical Structure

Repository root:

- `README.md`
  - explains what the repo is
- `HUONG_DAN_SU_DUNG.md`
  - Vietnamese quick start
- `USAGE_GUIDE.md`
  - English quick start
- `SO_TAY_VAN_HANH.md`
  - Vietnamese full manual
- `OPERATIONS_MANUAL.md`
  - English full manual
- `BAO_CAO_HARDENING.md`
  - Vietnamese hardening history
- `HARDENING_REPORT.md`
  - English hardening history

Runtime tree:

- `.agent/skills/`
  - the single canonical skill library
- `.agent/agents/`
  - 20 agent prompts
- `.agent/workflows/`
  - 11 workflow entry points
- `.agent/rules/`
  - 1 global rule file
- `.agent/scripts/`
  - helper and validation scripts
- `.agent/.shared/`
  - shared assets

Current state:

- `55` skills
- `20` agents
- `11` workflows
- `1` rules file

## 4. Reading Order For A New AI

This is the recommended order for a new AI entering the repo:

1. Read `.agent/skills/workspace-operating-system/SKILL.md`
2. Read:
   - `.agent/skills/workspace-operating-system/references/task-routing.md`
   - `.agent/skills/workspace-operating-system/references/quality-bar.md`
   - `.agent/skills/workspace-operating-system/references/operating-charter.md`
   - if the task is an ambitious idea or pitch: `idea-to-program-playbook.md`
   - if the task needs team-style operating structure: `department-operating-model.md`
3. If the task touches code, infra, release, or deployment:
   - also read `branch-and-release-policy.md`
4. If the task spans multiple domains:
   - also read `composition-patterns.md`
5. If the right skill is still unclear:
   - read `skill-catalog.md`
6. Only then read the primary skill's `SKILL.md`
7. Read `references/` only when they are actually needed
8. If the task needs a specialist role:
   - read the matching agent prompt under `.agent/agents/`
9. If the task maps to an existing command/process style:
   - read the appropriate workflow in `.agent/workflows/`

Guiding principles:

- move from overview -> routing -> primary skill -> deeper references
- do not blindly read every folder
- do not load unnecessary context
- for serious code work, always think in branch/review/release terms

## 5. Default Entry Point

By default, the best opening line is:

```text
Use $workspace-operating-system to decide the right skill stack, sequence the work, and verify the result.
```

Use that entry when:

- the task is ambiguous
- the task is large
- the task spans multiple domains
- the task is high-value
- the task needs an explicit quality bar

## 6. Task Routing

### 6.1 Application Expansion Tasks

Use:

- `app-builder`
- support: `architecture`, `frontend-design`, `api-patterns`, `database-design`, `deployment-procedures`, `closed-loop-delivery`

### 6.2 Architecture Tasks

Use:

- `architecture`

### 6.2b Large Systems, Mission Software, Simulation

Use:

- `systems-engineering`

Also read:

- `references/mission-software-playbook.md`
- `references/simulation-first-delivery.md`
- `references/interface-control-checklist.md`
- `references/decision-playbook.md`
- `references/adr-checklist.md`

### 6.3 API Tasks

Use:

- `api-patterns`

Also read:

- `references/contract-playbook.md`
- `references/api-review-checklist.md`

### 6.4 UI / Frontend Tasks

Use:

- `frontend-design`
- support depends on the task: `web-design-guidelines`, `tailwind-patterns`, `nextjs-react-expert`, `mobile-design`

### 6.5 Debug Tasks

Use:

- `systematic-debugging`
- support: related domain skills
- add verification with `webapp-testing` or `testing-patterns`

### 6.6 Tasks That Must Be Truly Finished

Use:

- `closed-loop-delivery`
- support:
  - `verification-before-completion`
  - `receiving-code-review`
  - `webapp-testing`

### 6.7 Tasks With An Existing Plan

Use:

- `executing-plans`
- support:
  - `using-git-worktrees`
  - `parallel-agents`
  - `verification-before-completion`

### 6.8 Review Feedback Tasks

Use:

- `receiving-code-review`

This is different from:

- `code-review-checklist`
  - use that when you are the one performing the review

### 6.9 React / Next.js Performance Tasks

Use:

- `nextjs-react-expert`

Also read:

- `references/performance-investigation-playbook.md`
- `references/app-router-checklist.md`

## 7. Skill Design Principles

This bundle follows one very important rule:

- `SKILL.md` should stay concise, triggerable, and workflow-oriented
- deeper knowledge should live in `references/`

Why:

- bloated `SKILL.md` files trigger worse
- the AI needs a concise coordination layer it can load quickly
- senior-level depth belongs in playbooks, checklists, and matrices under `references/`

Ideal shape of a skill:

- `SKILL.md`
  - when to use it
  - main workflow
  - related skills
- `references/`
  - playbooks
  - decision matrices
  - review checklists
  - advanced heuristics
- `agents/openai.yaml`
  - metadata for better discovery and invocation

## 8. Primary Skill Catalog

To see the full skill list:

- `.agent/skills/workspace-operating-system/references/skill-catalog.md`

Most important skill groups:

- Operating:
  - `workspace-operating-system`
  - `closed-loop-delivery`
  - `executing-plans`
  - `parallel-agents`
  - `plan-writing`
  - `verification-before-completion`
  - `using-git-worktrees`
  - `finishing-a-development-branch`
- Product and architecture:
  - `app-builder`
  - `architecture`
  - `systems-engineering`
  - `api-patterns`
  - `database-design`
  - `mcp-builder`
- Frontend:
  - `frontend-design`
  - `web-design-guidelines`
  - `tailwind-patterns`
  - `nextjs-react-expert`
  - `mobile-design`
- Quality:
  - `systematic-debugging`
  - `testing-patterns`
  - `tdd-workflow`
  - `webapp-testing`
  - `receiving-code-review`
  - `code-review-checklist`

## 9. Agent Catalog

These are the 20 current agents under `.agent/agents/`:

- `backend-specialist`
  - backend, server, API, auth, database integration
- `code-archaeologist`
  - legacy code, repo analysis, modernization
- `database-architect`
  - schema, migrations, indexing, data modeling
- `debugger`
  - root cause, crash investigation, production issues
- `devops-engineer`
  - deployment, rollback, CI/CD, server operations
- `documentation-writer`
  - documentation when the user explicitly asks for it
- `explorer-agent`
  - deep codebase discovery
- `frontend-specialist`
  - React/Next.js UI architecture
- `game-developer`
  - game logic and engines
- `mobile-developer`
  - React Native, Flutter, mobile patterns
- `orchestrator`
  - multi-agent coordination
- `penetration-tester`
  - offensive security
- `performance-optimizer`
  - profiling, speed, bundle optimization
- `product-manager`
  - requirements, acceptance criteria
- `product-owner`
  - backlog, MVP, strategic prioritization
- `project-planner`
  - planning and breakdown
- `qa-automation-engineer`
  - e2e, regression, automation infrastructure
- `security-auditor`
  - OWASP, auth, supply chain, security review
- `seo-specialist`
  - SEO and GEO
- `test-engineer`
  - tests, TDD, coverage

Agent usage principles:

- use an agent when the role truly matters to the task
- do not substitute agents for skills; they are different layers
- skills provide knowledge and process
- agents provide perspective and role identity

## 10. Workflow Catalog

There are 11 workflows under `.agent/workflows/`:

- `brainstorm.md`
  - structured brainstorming
- `create.md`
  - create a new application
- `debug.md`
  - systematic fault investigation
- `deploy.md`
  - deployment flow
- `enhance.md`
  - upgrade an existing feature
- `orchestrate.md`
  - coordinate multiple agents
- `plan.md`
  - planning flow
- `preview.md`
  - manage preview and local server workflows
- `status.md`
  - status tracking
- `test.md`
  - generate and run tests
- `ui-ux-pro-max.md`
  - UI execution flow

Notes:

- workflows are process-shaped entry points
- skills remain the canonical knowledge layer
- if a legacy workflow conflicts with `workspace-operating-system`, prefer routing from the central skill

## 11. Rules

There is currently one global rule file:

- `.agent/rules/GEMINI.md`

Its role:

- preserve compatibility with some older systems
- describe broad framework-style behavior

But keep this in mind:

- the current canonical runtime should still start from `workspace-operating-system`
- `GEMINI.md` is an inherited legacy file and should not keep growing
- newer rules should stay short, clear, and minimal

Recommended separation:

- keep truly global constraints in `rules/`
- keep routing and execution logic in `skills/workspace-operating-system`
- keep domain knowledge in `skills/*`

## 12. Priority Order

In this repo, think in this order:

1. user request
2. `workspace-operating-system`
3. the task's primary skill
4. the primary skill's references
5. agent role, if an agent is being used
6. workflow, if the task entered through a workflow
7. global rules for compatibility

Simple principle:

- the more specific and task-adjacent rule should take priority
- old or legacy rules that conflict with the new canonical system must be reviewed carefully

## 13. Prompt Templates For Humans

### General Routing

```text
Use $workspace-operating-system to route this task, choose the minimum effective skill stack, and verify the result.
```

### Build App

```text
Use $app-builder to shape this product request, choose the stack, and plan the next implementation steps.
```

### Architecture

```text
Use $architecture to compare realistic system options and recommend the best architecture with tradeoffs.
```

### API

```text
Use $api-patterns to design the API style, response contract, auth, and versioning for this system.
```

### End-To-End Delivery

```text
Use $closed-loop-delivery to finish this task end to end and prove the acceptance criteria.
```

### Review Feedback

```text
Use $receiving-code-review to process these review comments, apply valid fixes, and verify them.
```

### Performance

```text
Use $nextjs-react-expert to find the main bottleneck and optimize this React or Next.js flow deliberately.
```

## 14. Golden Workflows

### 14.1 Building A Large Feature

Recommended sequence:

1. `workspace-operating-system`
2. `app-builder`, `architecture`, or `systems-engineering`
3. `plan-writing`
4. `executing-plans`
5. domain skills
6. `verification-before-completion`
7. `finishing-a-development-branch`

### 14.2 Fixing A Difficult Bug

1. `workspace-operating-system`
2. `systematic-debugging`
3. related domain skill
4. `testing-patterns` or `webapp-testing`
5. `verification-before-completion`

### 14.3 Processing Review Feedback

1. `receiving-code-review`
2. domain skill
3. `verification-before-completion`
4. if true end-to-end closure is needed -> `closed-loop-delivery`

### 14.4 Performance Pass

1. `nextjs-react-expert`
2. `performance-profiling`
3. `frontend-design` if UX is affected
4. `verification-before-completion`

## 15. Adding A New Skill

When adding a new skill:

1. Create a folder in `.agent/skills/<skill-name>/`
2. Create `SKILL.md`
3. If deeper knowledge is needed:
   - add `references/`
4. If richer metadata is helpful:
   - add `agents/openai.yaml`
5. If repeatable helpers are needed:
   - add `scripts/`
6. Rebuild:

```text
python .agent/skills/workspace-operating-system/scripts/build_skill_catalog.py
```

Checklist before commit:

- the folder name and frontmatter `name:` must match
- `description:` must clearly say when to use the skill
- every reference mentioned in `SKILL.md` must exist
- do not mention stale legacy files or paths out of context
- do not import foreign launchers or app shells into the runtime tree
- for larger systems, clearly distinguish concept, simulator, prototype, and production claims

## 16. Upgrading An Older Skill

When an older skill becomes too broad, too vague, or still carries inherited-source residue:

1. Trim down `SKILL.md`
2. Clarify:
   - when to use it
   - the main workflow
   - related skills
3. Move deep knowledge into `references/`
4. Add senior-grade checklists or playbooks
5. Add `agents/openai.yaml` if the skill is important
6. Rebuild the catalog

That is how this bundle itself was upgraded.

## 17. Maintaining Agents

When editing `agents/*.md`:

- describe the role clearly
- explain when it should be used
- do not let an agent become a copy of a skill
- let the skill provide knowledge
- let the agent provide viewpoint, tone, and responsibility

A good agent should:

- have a clear trigger description
- know which skills it works with
- avoid over-indexing on older frameworks when the runtime has changed

## 18. Maintaining Workflows

When editing `workflows/*.md`:

- treat them as procedure entry points, not replacements for skills
- keep the command flow clear
- if the central skill now handles the logic better, simplify the workflow
- avoid letting workflows override the new canonical philosophy without a good reason

## 19. Hardening And Ownership

Current principles:

- local-first
- no external MCP enabled by default
- no sensitive files shipped
- no raw launcher or app shell imports from external bundles into `.agent`
- no workflow should encourage direct-to-main when the repo does not allow it
- when importing from external bundles:
  - audit
  - filter
  - rewrite or cherry-pick
  - do not merge their full runtime tree into the canonical tree

See also:

- `HARDENING_REPORT.md`

## 20. Release Checklist

Before pushing:

1. update the necessary files
2. rebuild the catalog if inventory or descriptions changed
3. check that references do not break
4. run:

```text
git diff --check
```

5. reread:
   - `README.md`
   - `HUONG_DAN_SU_DUNG.md`
   - `USAGE_GUIDE.md`
   - `SO_TAY_VAN_HANH.md`
   - `OPERATIONS_MANUAL.md`
   if the change affects how the bundle is used
6. write a meaningful commit
7. push the working branch
8. open or prepare a PR
9. merge to `dev`/`test`/staging according to the repo flow, if any
10. merge to `main`/`master` only after verification gates pass and approval is given

## 21. Signs The System Is Degrading

Be careful if you see:

- a skill name saying one thing while the folder says another
- `SKILL.md` files bloating and repeating themselves
- too many skills triggering for the same shape of task
- broken or missing references
- inherited old wording leaking into core skills
- workflows, agents, or rules contradicting the canonical flow
- the catalog not being rebuilt after frontmatter changes

## 22. Final Golden Rule

This bundle aims for:

- clear triggers
- rich knowledge
- low ambiguity
- a clear quality bar
- verification before finish
- a real senior-engineering operating style

If you have to choose between:

- long but vague
- and
- concise but clear, with deeper references behind it

choose the latter.
