---
name: webapp-testing
description: ALWAYS use this when the task involves browser automation, UI verification, DOM inspection, end-to-end checks, or reproducing a web bug in a running application.
---

# Web App Testing

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Core Rule

Discover first, then automate. Do not guess selectors or page state before checking the rendered application.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/selector-strategy.md`
- `references/flake-triage.md`

Then use `examples/` only for patterns you actually need.

## Decision Tree

- If the target is static HTML, read the file directly to discover likely selectors.
- If the target is a dynamic app, wait for the rendered state before inspecting the DOM.
- If a local server is needed, use `scripts/with_server.py` to manage it instead of hand-rolling startup logic.

## Testing Workflow

1. Map the surface area.
   - Identify routes, important pages, key components, and critical user journeys.
2. Inspect before acting.
   - Wait for `networkidle` on dynamic pages before reading DOM state.
   - Capture screenshots, page content, console logs, or element inventories to discover selectors.
3. Automate critical flows.
   - Cover happy paths first.
   - Then test auth, high-value actions, and important error states.
4. Review failures.
   - Prefer root-cause fixes over adding waits.

## Best Practices

- Test behavior rather than implementation details.
- Prefer stable selectors such as role, text, label, or `data-testid`.
- Keep tests independent and state-aware.
- Use screenshots and traces when failures are hard to explain from logs alone.
- Treat flaky tests as bugs, not noise.

## Runtime Scripts

- `scripts/playwright_runner.py`
  - Use for quick browser checks, screenshots, and lightweight audits.
- `scripts/with_server.py`
  - Run with `--help` first.
  - Use to manage one or more local servers before a Playwright script runs.

## Example Resources

Review examples in `examples/` when you need patterns for:

- element discovery
- static HTML automation
- console logging
