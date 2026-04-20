# Quality Checklist

Use this after modifying or generating a PDF.

## Required Checks

- confirm page count, ordering, and rotation
- open the output and extract or inspect the target pages again
- for tables or OCR, verify representative pages rather than trusting one sample
- for forms, confirm field names, values, and appearance streams

## Common Regressions

- invisible text after OCR or bad font embedding
- corrupted page rotations after merge operations
- form values set in data but not visible in the rendered PDF
- extractable text quality too poor to support the promised downstream task

## Codex Strict Review Gate

Assume the final result will be inspected by Codex with extreme scrutiny.

- Verify that the output directly satisfies the user's request and this skill's domain.
- Check important claims against local files, commands, source material, or produced artifacts when possible.
- Look for missing edge cases, stale assumptions, broken references, and unsupported promises.
- Do not call the work complete unless it would survive a hostile but fair senior review.
