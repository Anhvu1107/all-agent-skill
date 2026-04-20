# Branch And Release Policy

Use this policy for any meaningful code, config, or infrastructure change.

## Default Rule

Do not push straight to `main` or `master` by default.

The default path is:

1. choose the base branch
2. create a feature, fix, or hotfix branch
3. implement and verify on that branch or in a worktree
4. push the branch
5. open or prepare a PR
6. merge through the repository's integration path
7. promote to `main` or `master` only after verification gates pass

## Recommended Promotion Flow

If the repository uses staged environments, prefer:

- feature branch -> PR
- merge to `dev` or `test`
- verify integration and QA
- promote to staging or release branch
- merge to `main` or `master`
- deploy production from a known reviewed commit

If the repository is trunk-based, the exception still needs to be explicit:

- small scope
- clear ownership
- fresh verification
- user approval before direct protected-branch action

## Branch Naming

Use names that reveal intent:

- `feature/<slug>`
- `fix/<slug>`
- `hotfix/<slug>`
- `chore/<slug>`
- `docs/<slug>`

## Merge Gates

Before recommending merge or release:

- diff is understandable
- relevant tests or checks were run
- reviewer feedback is addressed or explicitly deferred
- docs or runbooks are updated when behavior changed
- rollback or revert path is known for risky changes

## Protected Branch Rules

- Never assume permission to merge or push to a protected branch.
- Never recommend bypassing review because the change "looks small."
- Never hide unverified risk behind urgency.
- Production or release-branch actions need an explicit user confirmation gate.

## Hotfix Exception

Hotfixes can move faster, but they are not exempt from discipline.

Minimum hotfix path:

1. branch from the production base
2. make the smallest possible fix
3. run the tightest useful verification
4. push hotfix branch
5. get approval to merge and deploy
6. back-merge the fix into integration branches

## Reporting Pattern

When finishing code work, state:

- current branch
- base branch
- intended next branch target
- checks run
- whether the change is ready for PR, staging, or production
