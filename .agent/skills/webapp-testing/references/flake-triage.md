# Flake Triage

Use this when a browser test is intermittent or timing-sensitive.

## Triage Order

1. confirm the app is actually ready before acting
2. verify the server, test data, and auth state are deterministic
3. replace blind sleeps with observable conditions
4. capture screenshots, console output, or traces before guessing

## Anti-Patterns

- adding longer waits without learning anything
- reusing dirty state between tests
- depending on selectors that disappear during animation or hydration
