# Quality Checklist

Use this before calling a mobile design flow complete.

## Required Checks

- tap targets and spacing feel touch-safe
- safe areas, keyboards, and gesture zones are considered
- the screen hierarchy works on a phone before adding tablet complexity
- loading, empty, error, and offline states are accounted for
- performance assumptions are believable for a real mobile runtime

## Common Regressions

- web-style dense layouts forced onto small screens
- one platform's pattern pasted onto the other without adaptation
- beautiful mockups with no story for loading, error, or offline behavior

## Codex Strict Review Gate

Assume the final result will be inspected by Codex with extreme scrutiny.

- Verify that the output directly satisfies the user's request and this skill's domain.
- Check important claims against local files, commands, source material, or produced artifacts when possible.
- Look for missing edge cases, stale assumptions, broken references, and unsupported promises.
- Do not call the work complete unless it would survive a hostile but fair senior review.
