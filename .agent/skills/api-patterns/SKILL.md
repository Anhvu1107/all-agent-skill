---
name: api-patterns
description: ALWAYS use this when the task involves API shape, contracts, auth, versioning, response structure, error handling, or service boundary design.
---

# API Patterns

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`


Start with the file that answers the current design question:

- `references/contract-playbook.md` for senior-level contract design and review
- `references/api-review-checklist.md` for final review before implementation
- `api-style.md` for REST vs GraphQL vs tRPC
- `rest.md` for REST endpoint and resource design
- `graphql.md` for GraphQL fit and schema considerations
- `trpc.md` for TypeScript-first monorepo APIs
- `response.md` for envelopes, pagination, and error contracts
- `versioning.md` for API evolution
- `auth.md` for authentication and caller identity
- `rate-limiting.md` for abuse protection
- `documentation.md` for API docs and discoverability
- `security-testing.md` when reviewing API risk

## Purpose

Choose an API style that fits the consumers, the team, and the product boundary.

An API is a contract. Changing it later is expensive, so design for clarity and operational reality early.

## Use This Skill When

- picking between REST, GraphQL, and tRPC
- shaping new endpoints or procedures
- normalizing responses, errors, pagination, or filtering
- deciding auth and versioning strategy
- reviewing whether an API is too leaky, inconsistent, or hard to evolve

## Core Workflow

1. Identify the consumers.
   - web client, mobile app, internal service, public integrators, same-repo frontend
2. Choose the transport and contract style.
   - REST, GraphQL, or tRPC based on usage patterns and team reality
3. Define resource or procedure boundaries.
4. Standardize responses.
   - success shape, errors, pagination, identifiers, timestamps
5. Decide control concerns.
   - auth, rate limiting, idempotency, versioning, observability
6. Document the contract in a way implementation can follow.

## Heuristics

- Use REST when resources and cacheable operations dominate.
- Use GraphQL when the client truly needs flexible graph traversal and multiple consumer views.
- Use tRPC when TypeScript-first internal velocity matters more than public portability.
- Keep error shapes consistent across the surface.
- Avoid exposing internal storage structure as public API design.

## Review Questions

- Can a new consumer understand the contract quickly?
- Are identifiers, status codes, and error shapes consistent?
- Is pagination stable and predictable?
- Can the API evolve without breaking common callers?
- Are auth and authorization boundaries obvious?

## Related Skills

- `architecture` for broader system-boundary decisions
- `database-design` when endpoint shape is being distorted by schema issues
- `mcp-builder` when the API surface is being adapted for tool-based LLM use
- `verification-before-completion` before claiming an API contract is ready
