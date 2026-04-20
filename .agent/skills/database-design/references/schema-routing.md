# Schema Routing

Use this to decide which database-design materials matter for the request.

## Route By Decision

- database choice unclear: read `database-selection.md`
- ORM choice unclear: read `orm-selection.md`
- data model and relationships: read `schema-design.md`
- query or latency risk: read `indexing.md` and `optimization.md`
- rollout or schema change risk: read `migrations.md`

## Default Order

1. Choose runtime and deployment context.
2. Shape entities and relationships.
3. Add indexes for real access patterns.
4. Plan migrations before you call the design stable.
