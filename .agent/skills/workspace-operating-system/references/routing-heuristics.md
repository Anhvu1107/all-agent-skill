# Routing Heuristics

Use this file when the request sounds broad, the stakes are high, and multiple skills could plausibly fit.

## Route By Bottleneck

- If the main uncertainty is system shape, start with `architecture`.
- If the main uncertainty is execution order, start with `plan-writing` or `executing-plans`.
- If the main uncertainty is why something broke, start with `systematic-debugging`.
- If the main uncertainty is UI direction or implementation style, start with `frontend-design` or `ui-ux-pro-max`.
- If the main uncertainty is schema, integrity, or migrations, start with `database-design`.
- If the main uncertainty is whether the work is truly done, add `verification-before-completion`.

## Route By Deliverable

- App, site, dashboard, or product slice: `app-builder`
- Architecture memo or refactor direction: `architecture`
- Slide deck, spreadsheet, document, or PDF artifact: `pptx`, `xlsx`, `docx`, or `pdf`
- Browser behavior or end-to-end verification: `webapp-testing`
- Skill bundle work: `skill-creator`
- Broad repository coordination: `workspace-operating-system`

## Escalate To Multi-Skill Mode When

- the user asks for both implementation and validation
- the task crosses architecture plus delivery plus review
- the deliverable mixes code and office artifacts
- the same answer needs design, build, and audit layers

Keep one primary skill. Add support skills only when they materially reduce risk.
