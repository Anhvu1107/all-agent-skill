# Alias Target

`security-aws-secrets-rotation` is a namespace-preserving alias for canonical skill `aws-secrets-rotation`.

## Why This Exists

Some upstream ZIP scanners derive skill slugs from nested paths instead of frontmatter names. This alias keeps that path-derived slug discoverable without copying the target skill's full content.

## Routing

- Canonical target folder: `.agent/skills/aws-secrets-rotation/`
- Canonical display name: AWS Secrets Rotation
- Alias display name: Security AWS Secrets Rotation
- Use the target skill's bundled scripts, references, and assets for substantive work.
