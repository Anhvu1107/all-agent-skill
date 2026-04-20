# Alias Target

`app-builder-templates` is a namespace-preserving alias for canonical skill `templates`.

## Why This Exists

Some upstream ZIP scanners derive skill slugs from nested paths instead of frontmatter names. This alias keeps that path-derived slug discoverable without copying the target skill's full content.

## Routing

- Canonical target folder: `.agent/skills/templates/`
- Canonical display name: Templates
- Alias display name: APP Builder Templates
- Use the target skill's bundled scripts, references, and assets for substantive work.
