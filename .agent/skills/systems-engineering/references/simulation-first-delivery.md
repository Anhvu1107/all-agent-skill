# Simulation-First Delivery

Use this playbook when the real-world system is too risky, expensive, slow, or unavailable to treat as the first test environment.

## Principle

Earn confidence in layers.

Do not jump from concept to field-readiness without a simulation or controlled validation step when the system is complex or safety-sensitive.

## Maturity Ladder

1. paper model
   - assumptions, states, interfaces, and major flows
2. software simulator
   - deterministic or scenario-based model of the system
3. integration harness
   - real software connected to mocks or playback
4. hardware-in-the-loop or lab environment
   - where available and lawful
5. staged operational environment
6. production or field deployment

## What To Simulate First

Choose the area with the highest uncertainty:

- control decisions
- interface timing
- failure conditions
- operator workflow
- telemetry and alerting behavior
- degraded or disconnected states

## Scenario Matrix

Every meaningful simulator should cover:

- nominal path
- slow or partial subsystem responses
- stale or missing telemetry
- malformed input
- retry storms or duplicate events
- safety fallback path

## Evidence Standard

Simulation results should produce:

- scenario list
- assumptions
- traces or logs
- observed outcomes
- pass or fail against explicit criteria

## Anti-Patterns

- using simulation as theater with no acceptance criteria
- hiding unrealistic assumptions
- calling a simulator "production proof"
- skipping degraded-state scenarios
