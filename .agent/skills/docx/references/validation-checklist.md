# Validation Checklist

Use this after creating or editing a DOCX.

## Required Checks

- run `python scripts/office/validate.py <file.docx>`
- if tracked changes were involved, confirm whether they should stay or be accepted with `scripts/accept_changes.py`
- reopen or re-extract the document to confirm the expected text is really present
- if layout matters, export to PDF or images and spot-check the rendered result

## Failure Traps

- invalid XML after manual edits
- missing relationships for images, styles, or headers
- accepting tracked changes when the user wanted them preserved
- silent formatting drift after aggressive find-and-replace
