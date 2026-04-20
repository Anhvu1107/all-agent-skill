---
description: Test workflow for running the right checks, adding focused tests for changed behavior, investigating failures, and reporting evidence without changing unrelated code.
---

# /test - Focused Testing And Verification

$ARGUMENTS

## Purpose

Use this workflow when the task is to test, verify, or improve coverage around a specific behavior.

## Default Stack

- `testing-patterns`
- relevant domain skill when needed
- `verification-before-completion`

Add `webapp-testing` when browser behavior is part of the proof.

## Modes

- run tests
- add focused tests for a target behavior
- investigate failing tests
- review coverage or missing test areas

## Flow

1. Identify the test target.
   - file, feature, bug, flow, or regression area
2. Choose the right test level.
   - unit, integration, browser, or build/runtime verification
3. Follow existing project patterns.
   - framework, naming, fixtures, mocks
4. Add or run only the relevant tests first.
5. Read the real output.
6. If failures appear, distinguish:
   - broken test
   - broken code
   - stale expectation
7. Report the evidence clearly.

## Guardrails

- Do not generate a broad test suite when the request is narrow.
- Do not change unrelated product logic while "just adding tests."
- Do not treat coverage as proof of correctness by itself.
- Do not say tests pass unless you ran them on the current state.

## Good Output

When closing a testing task, include:

- what was tested
- what command or method was used
- pass or fail result
- new regression coverage added, if any
- anything still unverified
