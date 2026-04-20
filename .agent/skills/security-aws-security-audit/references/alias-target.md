# Alias Target

`security-aws-security-audit` is a namespace-preserving alias for canonical skill `aws-security-audit`.

## Why This Exists

Some upstream ZIP scanners derive skill slugs from nested paths instead of frontmatter names. This alias keeps that path-derived slug discoverable without copying the target skill's full content.

## Routing

- Canonical target folder: `.agent/skills/aws-security-audit/`
- Canonical display name: AWS Security Audit
- Alias display name: Security AWS Security Audit
- Use the target skill's bundled scripts, references, and assets for substantive work.
