# Selector Strategy

Use this before writing or repairing browser automation.

## Priority Order

1. roles and accessible names
2. labels and visible text
3. stable `data-testid` hooks
4. structural CSS selectors only as a last resort

## Rules

- inspect the real DOM before choosing selectors
- prefer selectors tied to user behavior, not styling implementation
- if a selector feels brittle during authoring, it will be worse in CI
