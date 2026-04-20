# Layering And Boundaries

Use this before changing backend structure.

## Default Shape

- controllers handle transport concerns
- services hold business rules
- repositories isolate persistence details
- middleware handles cross-cutting request concerns

## Guardrails

- do not leak ORM or HTTP details across every layer
- validate inputs at clear boundaries
- keep side effects explicit and testable
