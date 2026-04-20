# Root-Cause Tracing

When the failure is deep in the stack:

1. Start at the bad output.
2. Ask what input produced it.
3. Move one boundary upstream at a time.
4. Stop at the first bad value, missing assumption, or wrong state transition.

Fix at the source boundary whenever possible, not at every downstream symptom.
