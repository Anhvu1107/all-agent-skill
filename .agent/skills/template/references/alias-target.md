# Alias Target

`template` is a namespace-preserving alias for canonical skill `template-skill`.

## Why This Exists

Some upstream ZIP scanners derive skill slugs from nested paths instead of frontmatter names. This alias keeps that path-derived slug discoverable without copying the target skill's full content.

## Routing

- Canonical target folder: `.agent/skills/template-skill/`
- Canonical display name: Template Skill
- Alias display name: Template
- Use the target skill's bundled scripts, references, and assets for substantive work.
