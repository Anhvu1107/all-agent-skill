---
name: database-design
description: ALWAYS use this when the hard part is schemas, relationships, constraints, indexes, data integrity, query shape, or migration-safe data modeling.
---

# Database Design

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

> **Learn to THINK, not copy SQL patterns.**

## Supplementary References

Start with:

- `references/senior-master-standard.md`
- `references/schema-routing.md`
- `references/migration-safety.md`

Then load only the root markdown files that match the actual database question.

## đŸ¯ Selective Reading Rule

**Read ONLY files relevant to the request!** Check the content map, find what you need.

| File | Description | When to Read |
|------|-------------|--------------|
| `database-selection.md` | PostgreSQL vs Neon vs Turso vs SQLite | Choosing database |
| `orm-selection.md` | Drizzle vs Prisma vs Kysely | Choosing ORM |
| `schema-design.md` | Normalization, PKs, relationships | Designing schema |
| `indexing.md` | Index types, composite indexes | Performance tuning |
| `optimization.md` | N+1, EXPLAIN ANALYZE | Query optimization |
| `migrations.md` | Safe migrations, serverless DBs | Schema changes |

---

## â ï¸ Core Principle

- ASK user for database preferences when unclear
- Choose database/ORM based on CONTEXT
- Don't default to PostgreSQL for everything

---

## Decision Checklist

Before designing schema:

- [ ] Asked user about database preference?
- [ ] Chosen database for THIS context?
- [ ] Considered deployment environment?
- [ ] Planned index strategy?
- [ ] Defined relationship types?

---

## Anti-Patterns

âŒ Default to PostgreSQL for simple apps (SQLite may suffice)
âŒ Skip indexing
âŒ Use SELECT * in production
âŒ Store JSON when structured data is better
âŒ Ignore N+1 queries
