# API Review Checklist

Use this file to review an API design before implementation or before calling it ready.

## Shape

- Is the style choice justified?
- Are endpoints or procedures named coherently?
- Is the contract consumer-centric rather than database-centric?

## Safety

- Are authorization boundaries obvious?
- Are error responses safe and actionable?
- Is rate limiting or abuse control addressed where needed?
- Are retry-sensitive operations idempotent?

## Compatibility

- Are additive changes preferred over breaking ones?
- Is versioning strategy explicit if breakage is likely?
- Are pagination and filtering forward-compatible?

## Operability

- Can requests be traced or correlated?
- Are failure cases observable?
- Are timeouts and latency-sensitive fan-outs being considered?

## Documentation

- Are examples realistic?
- Do examples match actual field names and status codes?
- Could another team implement a client correctly from the docs?
