# Server Design Checklist

Use this before implementing tools or resources.

## Tool Design

- one tool should solve one user-visible job
- schemas should be strict enough to prevent ambiguity
- errors should explain the next recovery step
- pagination and filtering should exist before context explodes

## Resource Design

- use resources for durable context, not everything
- prefer templates when the target object varies by ID or path
- make it obvious whether a resource is static, generated, or expensive
