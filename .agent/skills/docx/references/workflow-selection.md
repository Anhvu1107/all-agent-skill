# Workflow Selection

Use this file to choose the safest DOCX path before touching the document.

## Choose The Path

- New document from scratch: prefer `docx-js` generation.
- Existing document with formatting you must preserve: unpack, edit the XML surgically, then repack.
- Tracked changes or comments: inspect with `pandoc` or XML first, then use the bundled scripts instead of ad-hoc text replacement.
- Image replacement or structural cleanup: unpack first so you can confirm the package layout before editing.

## Default Order

1. Inspect or extract.
2. Choose generation vs unpack/edit/repack.
3. Validate the output with `scripts/office/validate.py`.
4. Convert to PDF or images only after the DOCX itself is sound.
