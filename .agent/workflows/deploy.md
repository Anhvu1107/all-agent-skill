---
description: Deployment and release workflow with verification gates, branch discipline, rollback awareness, and environment-specific approvals.
---

# /deploy - Release And Deployment

$ARGUMENTS

## Purpose

Handle deployment as an engineering release process, not as a blind push.

## Default Policy

- Deploy from a known branch and commit.
- Do not deploy an unreviewed local diff.
- Do not push directly to `main` or `master` as a casual release shortcut.
- Production deployment requires explicit user approval.

## Recommended Flow

1. Identify the target environment.
   - preview
   - test
   - staging
   - production
2. Identify the release candidate.
   - branch
   - commit
   - expected behavior change
3. Run pre-flight checks.
   - status is clean
   - relevant tests pass
   - build succeeds
   - rollback path is known
4. Deploy to the target environment.
5. Verify runtime health.
   - smoke test
   - key user flow
   - logs or health endpoints if available
6. Report the result.
   - deployed commit
   - environment
   - checks run
   - health status
   - rollback note if needed

## Promotion Path

Prefer:

- feature branch -> PR
- integration branch (`dev` or `test`)
- staging or release candidate
- `main` or `master`
- production

If the repository uses trunk-based delivery, say that explicitly before treating direct promotion as normal.

## Stop Conditions

Stop and escalate if:

- tests or build fail
- the target environment is unclear
- the release candidate is not verified
- production approval was not given
