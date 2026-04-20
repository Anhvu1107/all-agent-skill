# Stack Decision Matrix

Use this file when choosing the default stack for a new application surface.

## Web Product Defaults

- Next.js
  - use when product velocity, hybrid rendering, and mainstream hiring matter
- Nuxt
  - use when the team is stronger in Vue and the product shape fits it well
- FastAPI
  - use when Python-native backends and async APIs matter more than frontend coupling
- Express or Hono
  - use when the backend should stay thin and explicit

## Data Layer Defaults

- PostgreSQL
  - default when relational integrity matters
- Prisma
  - default when team ergonomics and schema-driven development matter
- Drizzle
  - prefer when SQL explicitness and lighter abstraction matter more

## Default Questions

- What is the primary developer workflow?
- What is the deployment environment?
- Which part of the stack is most likely to change?
- What would be hardest to migrate later?

If the answer to those questions is unclear, default to the most boring stack that still fits.
