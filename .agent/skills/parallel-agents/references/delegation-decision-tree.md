# Delegation Decision Tree

Ask:

1. What is the immediate local blocking step?
2. What sidecar work can progress without blocking it?
3. Do the sidecar tasks avoid shared writes?
4. Will delegation save meaningful time?

If the next local step depends on the answer, keep that work local.
