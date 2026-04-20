# Quality Checklist

Use this before calling work with `daily-news-report` complete.

## Checks

- Confirm the request actually matches this skill's trigger and domain.
- Load only the supporting files needed for the current task.
- If scripts exist, prefer running or adapting them over recreating fragile logic by hand.
- If assets exist, reuse them rather than inventing substitute assets.
- State what was verified and what remains uncertain.

## Reviewer Traps

- Claiming the skill was used while ignoring its bundled resources.
- Loading every file instead of using progressive disclosure.
- Making broad promises outside the skill's actual scope.

## Codex Strict Review Gate

Assume the final result will be inspected by Codex with extreme scrutiny.

- Verify that the output directly satisfies the user's request and this skill's domain.
- Check important claims against local files, commands, source material, or produced artifacts when possible.
- Look for missing edge cases, stale assumptions, broken references, and unsupported promises.
- Do not call the work complete unless it would survive a hostile but fair senior review.
