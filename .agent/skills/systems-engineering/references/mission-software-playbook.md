# Mission Software Playbook

Use this playbook for software that coordinates operators, missions, vehicles, instruments, or distributed subsystems.

## Frame The Mission

Write down:

- mission objective
- operator or supervising user
- environment and constraints
- major phases or states
- success criteria
- abort or failure criteria

## Model The System

At minimum, define:

- operator interface
- control or coordination layer
- data ingest and telemetry layer
- subsystem interfaces
- persistent state and event log
- alerting and fault handling

## State And Mode Design

Explicitly define modes such as:

- idle
- ready
- active
- degraded
- safe mode
- fault
- recovery

Do not hide critical state in scattered booleans or undocumented side effects.

## Telemetry First

For every meaningful subsystem, decide:

- what is measured
- how often it is sampled
- how it is timestamped
- where it is stored
- how operators see anomalies
- what gets retained for post-incident analysis

## Failure Design

Write down:

- expected faults
- detection signal
- automatic response
- operator notification
- manual override path
- recovery steps

## Human Factors

If an operator is involved:

- reduce ambiguity in UI and status labels
- prefer clear mode transitions and alarms
- show confidence, freshness, and health status
- make unsafe commands hard to trigger accidentally

## Software Deliverable Ladder

Start with the smallest credible slice:

1. mission brief and interfaces
2. simulator or event model
3. telemetry pipeline
4. operator dashboard
5. control workflow
6. integrated validation harness

## Review Questions

- What is the source of truth for mission state?
- What happens when telemetry is stale, noisy, or missing?
- How is time synchronized across subsystems?
- What is the safe fallback mode?
- What evidence would justify the next maturity step?
