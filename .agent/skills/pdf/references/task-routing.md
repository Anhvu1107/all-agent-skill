# Task Routing

Use this file before choosing a PDF toolchain.

## Route By Job

- Text extraction or tables: prefer `pdfplumber`.
- Page structure edits such as merge, split, rotate, or metadata changes: prefer `pypdf`.
- Form filling: read `forms.md` and preserve field names carefully.
- Scanned documents: plan for OCR before promising searchable text.
- New PDF output: decide whether the real source of truth should stay DOCX, HTML, or another format first.

## Guardrails

- Do not assume a scanned PDF has extractable text.
- Do not flatten or rasterize unless the user actually needs that tradeoff.
- Verify page counts and order after merge or split operations.
