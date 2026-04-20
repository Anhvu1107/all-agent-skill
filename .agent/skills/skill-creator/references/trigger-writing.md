# Trigger Writing

Descriptions should trigger the skill before the agent drifts into a generic answer.

## Pattern

Use this shape whenever possible:

`ALWAYS use this when ...`

Then list:

- the user language that should trigger the skill
- the real bottleneck or job-to-be-done
- near-miss cases that look casual but still count

## Good Triggers

- broad but concrete
- centered on when to use the skill
- aggressive enough to catch implicit asks
- short enough to read quickly

## Weak Triggers

- process summaries instead of trigger situations
- vague statements like "helps with" or "can be used for"
- hiding the actual trigger language deep in the body
- overfitting to one file extension when the real trigger is the deliverable

## Rewrite Checklist

- Does the first sentence tell another agent when to reach for this skill?
- Would the skill trigger if the user phrased the ask casually?
- Did you remove timid hedges like "may" or "might" when the skill should clearly fire?
