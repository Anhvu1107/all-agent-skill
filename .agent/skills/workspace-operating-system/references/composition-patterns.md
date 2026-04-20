# Composition Patterns

Use this file when one skill is not enough.

## Common Multi-Skill Stacks

### New Product Surface

- `brainstorming`
- `architecture`
- `frontend-design`
- `api-patterns`
- `database-design`
- `testing-patterns`

Use for new features, dashboards, landing pages with backend logic, or app shells.

### Full App Delivery

- `app-builder`
- `architecture`
- `frontend-design`
- `database-design`
- `deployment-procedures`
- `closed-loop-delivery`
- `testing-patterns`

Use when the request is "build the app" rather than "improve one slice."

### Idea To Program

- `workspace-operating-system`
- `brainstorming`
- `architecture`
- `plan-writing`
- `closed-loop-delivery`

Use when the user brings a big idea, rough vision, or half-formed concept and the first job is to turn it into a real program with milestones.

### Ambitious Systems Program

- `systems-engineering`
- `architecture`
- `api-patterns`
- `database-design`
- `frontend-design`
- `closed-loop-delivery`

Use for mission software, telemetry platforms, digital twins, robotics support systems, or simulation-first programs that span operators, subsystems, and verification boundaries.

### Plan Execution

- `plan-writing`
- `executing-plans`
- `using-git-worktrees`
- `verification-before-completion`

Use when the strategy is agreed and the main risk is drift, skipped steps, or weak verification.

### Closed-Loop Feature Delivery

- `closed-loop-delivery`
- relevant domain skill
- `receiving-code-review`
- `verification-before-completion`

Use when the user expects end-to-end completion, including review response and proof of behavior.

### UI Polish With Real Quality Control

- `frontend-design`
- `web-design-guidelines`
- `performance-profiling`
- `webapp-testing`

Use for redesigns, landing pages, or component-system polishing where both aesthetics and execution matter.

### Backend Feature Delivery

- `architecture`
- `api-patterns`
- `database-design`
- `testing-patterns`

Use for new endpoints, auth flows, or business logic that crosses API and schema boundaries.

### Bug Hunt

- `systematic-debugging`
- relevant domain skill
- `webapp-testing` or `testing-patterns`
- `lint-and-validate`
- `verification-before-completion`

Use when behavior is failing and root cause is not yet obvious.

### Review Response

- `receiving-code-review`
- relevant domain skill
- `verification-before-completion`

Use when the work is mostly about understanding feedback, making the right fixes, and proving the comments are resolved.

### Security Pass

- `vulnerability-scanner`
- `red-team-tactics`
- relevant domain skill
- `testing-patterns`

Use for authentication, exposed APIs, secrets handling, or risky integrations.

### Document And Messaging

- `doc-coauthoring`
- `internal-comms`
- `brand-guidelines`
- `canvas-design` when visual polish matters

Use for written deliverables, stakeholder-facing documents, briefs, and polished communication artifacts.

### Skill Bundle Maintenance

- `workspace-operating-system`
- `skill-creator`
- `plan-writing`
- `documentation-templates`

Use when adding, upgrading, or standardizing skills inside this repository.

## Composition Rules

- Name the primary skill first.
- Add only support skills that materially reduce risk or rework.
- Keep the sequence explicit: plan -> build -> verify, or reproduce -> fix -> verify.
- Prefer `using-git-worktrees` when isolation reduces branch or workspace risk.
- When two skills overlap, prefer the one closest to the actual deliverable.
