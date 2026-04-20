# Model Quality Checklist

Use this before shipping a workbook.

## Required Checks

- run workbook recalculation when formulas changed
- confirm there are no `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, or `#NAME?` errors
- spot-check key formulas and ranges after inserting or moving columns
- confirm headers, units, and number formats match the user's context
- verify row counts and totals after any cleanup or import operation

## Common Regressions

- broken references after column insertion
- formulas copied with inconsistent anchors
- pretty formatting hiding bad calculations
- stale cached values when the workbook was never recalculated
