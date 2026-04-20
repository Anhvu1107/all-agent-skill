# Migration Safety

Use this when the schema work affects existing data.

## Guardrails

- prefer additive migrations before destructive ones
- separate data backfills from schema changes when risk is high
- know how the chosen platform handles locks, downtime, and online index creation
- prove rollback or recovery strategy for important tables

## Reviewer Triggers

- renamed columns without a transition plan
- type changes with no data compatibility story
- indexes added with no thought for deploy-time cost
- production assumptions made from local-only testing
