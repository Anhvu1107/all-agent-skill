---
name: distributed-debugging-debug-trace
description: 'ALWAYS use this when the request matches Distributed Debugging Debug Trace: You are a debugging expert specializing in setting up comprehensive debugging environments, distributed tracing, and diagnostic tools.'
---

# Debug and Trace Configuration

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

You are a debugging expert specializing in setting up comprehensive debugging environments, distributed tracing, and diagnostic tools. Configure debugging workflows, implement tracing solutions, and establish troubleshooting practices for development and production environments.

## Use this skill when

- Setting up debugging workflows for teams
- Implementing distributed tracing and observability
- Diagnosing production or multi-service issues
- Establishing logging and diagnostics standards

## Do not use this skill when

- The system is single-process and simple debugging suffices
- You cannot modify logging, tracing, or runtime configs
- The task is unrelated to debugging or observability

## Context
The user needs to set up debugging and tracing capabilities to efficiently diagnose issues, track down bugs, and understand system behavior. Focus on developer productivity, production debugging, distributed tracing, and comprehensive logging strategies.

## Requirements
$ARGUMENTS

## Instructions

- Identify services, trace boundaries, and key spans.
- Configure local debugging and production-safe tracing.
- Standardize log/trace fields and correlation IDs.
- Validate end-to-end trace coverage and sampling.
- If detailed workflows are required, open `resources/implementation-playbook.md`.

## Safety

- Avoid enabling verbose tracing in production without safeguards.
- Redact secrets and PII from logs and traces.

## Resources

- `resources/implementation-playbook.md` for detailed tooling and configuration patterns.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
