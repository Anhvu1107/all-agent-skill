# Interface Control Checklist

Use this checklist for boundaries between subsystems, services, operators, devices, or simulators.

## Contract Basics

- interface name and owner
- source and destination
- request and response shape
- units, coordinate frames, and conventions
- timing expectations
- versioning strategy

## Data Integrity

- required fields
- optional fields and defaults
- range checks
- enum definitions
- checksums, signatures, or integrity markers when needed

## Time And Ordering

- timestamp format and timezone or epoch
- event ordering rules
- idempotency key or dedupe strategy
- retry behavior
- timeout policy

## Failure Handling

- explicit error codes
- degraded-mode behavior
- stale-data behavior
- circuit-break or safe-mode trigger
- operator-visible warning path

## Configuration And Calibration

- configuration source of truth
- calibration values and versioning
- environment-specific overrides
- rollout and rollback behavior

## Observability

- logs
- metrics
- traces or event journal
- alert conditions
- audit trail for critical actions

## Review Questions

- Can another team implement the other side from this contract alone?
- Are units and coordinate frames impossible to misread?
- What happens if the data is delayed, duplicated, or wrong?
- What is the safe default when the interface breaks?
