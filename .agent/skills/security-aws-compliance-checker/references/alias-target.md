# Alias Target

`security-aws-compliance-checker` is a namespace-preserving alias for canonical skill `aws-compliance-checker`.

## Why This Exists

Some upstream ZIP scanners derive skill slugs from nested paths instead of frontmatter names. This alias keeps that path-derived slug discoverable without copying the target skill's full content.

## Routing

- Canonical target folder: `.agent/skills/aws-compliance-checker/`
- Canonical display name: AWS Compliance Checker
- Alias display name: Security AWS Compliance Checker
- Use the target skill's bundled scripts, references, and assets for substantive work.
