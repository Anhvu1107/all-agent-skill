# Task Routing

Use this file first. It is the fastest way to map a request shape to the right skill.

## Fast Map

- Broad product or app request
  - Primary: `app-builder`
  - Support: `architecture`, `frontend-design`, `api-patterns`, `database-design`, `deployment-procedures`, `closed-loop-delivery`
- Ambitious or systems-heavy request
  - Primary: `systems-engineering`
  - Support: `architecture`, `app-builder`, `api-patterns`, `database-design`, `closed-loop-delivery`
  - Notes: start by separating simulator, prototype, and production claims
- Architecture or system design
  - Primary: `architecture`
  - Support: `app-builder`, `database-design`, `api-patterns`
- Frontend or UI work
  - Primary: `frontend-design`
  - Support: `web-design-guidelines`, `tailwind-patterns`, `nextjs-react-expert`, `mobile-design`, `performance-profiling`
- API and backend work
  - Primary: `api-patterns`
  - Support: `database-design`, `architecture`, `nodejs-best-practices`, `python-patterns`, `mcp-builder`
- Database schema or data model work
  - Primary: `database-design`
  - Support: `architecture`, `api-patterns`
- Approved implementation plan
  - Primary: `executing-plans`
  - Support: `using-git-worktrees`, `parallel-agents`, `verification-before-completion`
- End-to-end feature or fix with explicit acceptance criteria
  - Primary: `closed-loop-delivery`
  - Support: `executing-plans`, `webapp-testing`, `receiving-code-review`, `verification-before-completion`
- Debugging or broken behavior
  - Primary: `systematic-debugging`
  - Support: domain skill for the failing area, plus `webapp-testing` or `testing-patterns`
- Code review or code quality
  - Primary: `code-review-checklist`
  - Support: `clean-code`, `testing-patterns`, `lint-and-validate`, `vulnerability-scanner`, `verification-before-completion`
- Responding to review comments or requested changes
  - Primary: `receiving-code-review`
  - Support: `code-review-checklist`, `verification-before-completion`, domain skill for the affected area
- Testing and verification
  - Primary: `testing-patterns` or `verification-before-completion`
  - Support: `webapp-testing`, `tdd-workflow`, `lint-and-validate`, `performance-profiling`
- Web app browser automation
  - Primary: `webapp-testing`
  - Support: `frontend-design` or `systematic-debugging`
- Performance and optimization
  - Primary: `performance-profiling`
  - Support: domain skill plus `nextjs-react-expert`, `nodejs-best-practices`, or `web-design-guidelines`
- Security review
  - Primary: `vulnerability-scanner`
  - Support: `red-team-tactics`, `systematic-debugging`, domain skill
- SEO and content discoverability
  - Primary: `seo-fundamentals`
  - Support: `frontend-design`, `web-design-guidelines`, `internal-comms`
- Brand, visual assets, and static art
  - Primary: `brand-guidelines`, `canvas-design`, or `theme-factory`
  - Support: `frontend-design`, `algorithmic-art`
- Document and communication work
  - Primary: `doc-coauthoring` or `internal-comms`
  - Support: `brand-guidelines`, `canvas-design`
- Internal communication artifacts
  - Primary: `internal-comms`
  - Support: `brand-guidelines`, `doc-coauthoring`, `canvas-design`
- MCP or tool integration
  - Primary: `mcp-builder`
  - Support: `architecture`, `api-patterns`, `python-patterns`, `nodejs-best-practices`
- Skill or workflow authoring
  - Primary: `skill-creator`
  - Support: `workspace-operating-system`, `plan-writing`, `verification-before-completion`
- Branch isolation or parallel branch work
  - Primary: `using-git-worktrees`
  - Support: `executing-plans`, `finishing-a-development-branch`
- Wrapping up a verified branch
  - Primary: `finishing-a-development-branch`
  - Support: `verification-before-completion`, `receiving-code-review`

## Intent-First Rules

- If the hardest part is deciding what to build, start with planning or architecture.
- If the hardest part is making something real, start with the implementation skill.
- If the hardest part is uncertainty or failure, start with debugging or testing.
- If the hardest part is proving the work is truly done, start with `verification-before-completion` or `closed-loop-delivery`.
- If the task spans multiple domains, choose one primary skill and only then add support skills.
- If the request touches regulated, safety-critical, or physically grounded systems, define the verification boundary before implementation.
- If the request starts as a bold vision rather than a spec, use the idea-to-program path before picking implementation slices.
