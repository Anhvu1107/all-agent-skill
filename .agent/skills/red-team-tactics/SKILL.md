---
name: red-team-tactics
description: 'ALWAYS use this when the request matches RED Team Tactics: Authorized adversary-simulation and detection-engineering patterns for defensive security work.'
---

# Red Team Tactics

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

Use ATT&CK-style thinking to improve defenses, validate detections, and sharpen security reviews.

## Use This Skill When

- mapping threats to detections
- planning an authorized purple-team exercise
- reviewing defensive coverage against likely attack paths
- writing a security report that explains how defenders could have seen the problem sooner

## Do Not Use This Skill For

- exploit walkthroughs
- stealth or evasion techniques
- credential theft
- persistence guidance
- exfiltration playbooks
- unauthorized access advice

## Defensive ATT&CK Model

Use the ATT&CK lifecycle as a detection map:

1. initial access
2. execution
3. privilege escalation
4. lateral movement
5. collection
6. impact

For each stage, ask:

- what preventive control should exist
- what telemetry should exist
- what alert should fire
- what response action should happen

## Exercise Patterns

- tabletop exercise
  - map a realistic attack path and test the team's response decisions
- purple-team validation
  - verify whether detections and controls work as designed
- coverage review
  - compare known threats to current logging and alerting gaps
- post-incident learning
  - explain where visibility, containment, or escalation broke down

## Reporting Pattern

For each finding, include:

- likely attack objective
- exposed surface
- missing or weak control
- missing or weak telemetry
- recommended prevention improvement
- recommended detection improvement
- recommended response improvement

## Senior Standard

- stay authorized
- stay defensive
- prefer control improvements over theater
- prefer detection logic over attack drama
- reduce risk without normalizing offensive misuse
