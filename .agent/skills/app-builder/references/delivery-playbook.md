# App Delivery Playbook

Use this file when a product ask needs to become a senior-level build plan instead of a vague "we should make an app."

## Request Shapes

Classify the job first:

- greenfield product
- major feature for an existing app
- internal tool
- rescue or modernization effort

Each shape deserves a different execution path.

## Build Modes

### Template-First

Use when:

- the app shape is standard
- time-to-first-structure matters
- the template avoids boring setup risk

Avoid when:

- the app has unusual boundaries
- the template would be heavily rewritten immediately

### Plan-First

Use when:

- the request spans multiple domains
- risk is mostly in system shape and sequencing
- there are important constraints or integrations

### Extend-In-Place

Use when:

- the repo already has strong patterns
- the ask is a coherent slice, not a net-new system
- preserving local conventions matters more than greenfield speed

## Senior Stack Selection

Choose stacks by operational fit:

- choose boring defaults when the product risk is already high
- choose edge or event-driven patterns only when they solve a real bottleneck
- choose hosted primitives when the team wants product speed more than infrastructure ownership

## First Deliverables

A strong app-building pass usually produces:

- product shape summary
- chosen stack
- domain decomposition
- execution path
- test and verification approach

## Common Overbuild Mistakes

- introducing a monorepo before there is meaningful multi-package pressure
- adding search, background jobs, and event buses "for later"
- picking the stack by hype rather than by team and delivery constraints
- planning auth, billing, and file processing without verifying whether the product really needs them yet
