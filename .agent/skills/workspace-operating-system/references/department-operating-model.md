# Department Operating Model

Use this reference when a task should feel like a coordinated IT department rather than one generic agent response.

## Department Lanes

### 1. Product

Primary roles:

- `product-manager`
- `product-owner`

Responsibilities:

- frame the business or user problem
- define scope and acceptance criteria
- prioritize milestones and backlog

### 2. Architecture

Primary roles:

- `architecture`
- `project-planner`

Responsibilities:

- system shape
- boundaries and interfaces
- delivery slices
- risk and tradeoff decisions

### 3. Delivery

Primary roles:

- `app-builder`
- domain skills such as `api-patterns`, `frontend-design`, `database-design`

Responsibilities:

- build the smallest credible increment
- keep implementation aligned with the plan

### 4. Quality

Primary roles:

- `testing-patterns`
- `webapp-testing`
- `verification-before-completion`
- `receiving-code-review`

Responsibilities:

- prove behavior
- guard against regressions
- close review loops

### 5. Security

Primary roles:

- `vulnerability-scanner`
- `security-auditor`

Responsibilities:

- threat review
- secrets and auth checks
- supply-chain and exposure review

### 6. Release And Operations

Primary roles:

- `deployment-procedures`
- `using-git-worktrees`
- `finishing-a-development-branch`
- `devops-engineer`

Responsibilities:

- branch strategy
- release path
- rollback awareness
- runtime readiness

### 7. Communication And Continuity

Primary roles:

- `internal-comms`
- `doc-coauthoring`
- `documentation-writer`

Responsibilities:

- handoffs
- summaries
- runbooks
- stakeholder communication

## Handoff Contract

Every lane should hand off:

- what was decided
- what changed
- what evidence exists
- what remains uncertain
- what the next lane should do

## Default Sequence

For most serious work:

1. product framing
2. architecture and planning
3. branch isolation
4. implementation
5. QA and review
6. release decision
7. documentation and handoff

## For Very Ambitious Ideas

Add a systems layer before implementation:

1. mission framing
2. verification boundary
3. interfaces and constraints
4. simulator or prototype path
5. software slice
6. integration and operations
