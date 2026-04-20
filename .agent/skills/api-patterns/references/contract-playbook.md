# API Contract Playbook

Use this file when designing an API that should be easy to consume, evolve, and operate.

## Consumer Map

List consumers before choosing the contract:

- browser frontend
- mobile app
- internal service
- third-party integrator
- same-repo TypeScript client

The contract should match the hardest real consumer, not the easiest one.

## Style Matrix

Choose the style that best matches the consumer and operational reality.

- REST
  - best for public or multi-client APIs, cacheability, and long-lived portability
- GraphQL
  - best for complex read patterns and multiple client views over connected data
- tRPC
  - best for TypeScript-first internal systems where contract velocity matters most
- gRPC
  - best for internal service-to-service calls where performance and strict contracts dominate

## Resource and Procedure Rules

- Use REST resources when the domain has durable nouns.
- Use procedures when the action is not naturally resource-shaped.
- Do not fake resources just to stay "pure REST."
- Do not expose database joins as if they were the domain model.

## Response Contract Rules

Keep these stable across the surface:

- identifier shape
- timestamp format
- pagination shape
- error envelope
- success envelope, if one is used

If one endpoint returns raw arrays and another returns nested envelopes without reason, the contract is already degrading.

## Error Model

Every error response should answer:

- what failed
- whether the caller can fix it
- whether retry makes sense
- how the caller should classify it

Do not leak stack traces or storage-specific details into public errors.

## Evolution Rules

- Add before you remove.
- Prefer additive changes over behavioral changes.
- Version only when compatibility actually breaks.
- Mark deprecations clearly and early.

## Consistency Checklist

- verbs and nouns are used consistently
- filtering and sorting conventions are shared
- auth model is predictable
- idempotency exists for retry-sensitive write paths
- documentation examples match actual response shapes

## Senior Review Questions

- Can a new engineer predict the next endpoint shape?
- Will this contract still make sense with one more client type?
- Are we optimizing for the producer or the consumer?
- What will be painful to change six months from now?
