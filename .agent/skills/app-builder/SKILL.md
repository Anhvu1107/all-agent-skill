---
name: app-builder
description: ALWAYS use this when the user mentions any app, website, dashboard, portal, admin panel, internal tool, SaaS product, mobile app, extension, or multi-surface feature, even if they describe it casually as a quick MVP, simple CRUD, or just one page.
---

# App Builder

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Start with the path that matches the job:

- `references/delivery-playbook.md` to choose the right execution mode
- `references/stack-decision-matrix.md` when stack selection is part of the problem
- `project-detection.md` to classify the app request
- `tech-stack.md` to choose the stack
- `scaffolding.md` for greenfield structure
- `feature-building.md` for adding a feature to an existing app
- `agent-coordination.md` when the task spans multiple domains
- `templates/SKILL.md` when the fastest safe path is a template-backed scaffold

## Purpose

Translate a product request into a buildable application path.

This skill is the bridge between "I want an app that does X" and the concrete design, stack, and execution sequence needed to make that real.

## Use This Skill When

- the user is asking to build an app, product surface, or meaningful feature area
- the request spans frontend, backend, data, auth, or deployment concerns
- the team needs help choosing a practical stack for the problem
- a greenfield request needs structure before implementation starts

## Core Workflow

1. Classify the request.
   - greenfield app, major feature, extension, or rescue/refactor
2. Clarify the product surface.
   - core users, core actions, must-have features, delivery constraints
3. Choose the minimum effective stack.
   - do not overbuild
4. Route to the right supporting skills.
   - `architecture`, `frontend-design`, `api-patterns`, `database-design`, `deployment-procedures`, `webapp-testing`
5. Decide the execution mode.
   - plan first, scaffold from a template, or extend the existing repo in place
6. Produce the next actionable move.
   - plan, scaffold, or implementation sequence

## Greenfield Heuristics

- Use a template only when it clearly reduces setup risk.
- Prefer mainstream, maintainable stacks over novelty.
- Match stack complexity to the first release, not the imagined tenth release.
- Keep auth, payments, search, and background jobs honest about real needs.

## Existing-App Heuristics

- Preserve established patterns before introducing new ones.
- Add one coherent slice at a time.
- Let the bottleneck decide the next skill:
  - unclear structure -> `architecture`
  - UI-heavy -> `frontend-design`
  - backend-heavy -> `api-patterns`
  - data-heavy -> `database-design`

## Deliverable Standard

A good `app-builder` outcome should leave the user with:

- a clear app shape
- a justified stack
- a realistic next-step sequence
- the correct support-skill stack for execution

## Related Skills

- `workspace-operating-system` for overall routing and quality control
- `architecture` for system design
- `plan-writing` when the build needs a formal execution plan
- `closed-loop-delivery` when the goal is to drive a feature to proven completion
