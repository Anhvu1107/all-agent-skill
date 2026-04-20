# ADR Checklist

Use this file when a decision is important enough to deserve a durable record.

## Minimum ADR Structure

1. Title
2. Status
3. Context
4. Decision
5. Options considered
6. Consequences
7. Follow-up triggers

## Context Questions

- What problem are we solving?
- What constraints are non-negotiable?
- What assumptions are we making?
- What current pain or risk does this address?

## Decision Quality Checks

- Is the recommendation specific?
- Does it name what is in scope and out of scope?
- Does it explain why the chosen path beat the alternatives?
- Does it make implementation implications obvious?

## Consequence Checklist

Document both positive and negative consequences:

- delivery speed impact
- operational cost
- ownership impact
- migration cost
- test strategy implications
- observability implications

## Follow-Up Triggers

An ADR should also say what would invalidate it, for example:

- traffic exceeds a defined threshold
- team ownership changes
- compliance scope changes
- latency budget changes
- an external dependency becomes mandatory
