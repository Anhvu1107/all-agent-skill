# Frontmatter Metadata Archive

This file preserves upstream metadata moved out of `SKILL.md` so the runtime frontmatter stays strict: `name` and `description` only.

```yaml
risk: unknown
source: community
version: 2.1.3
author: Francesco Marinoni Moretto
license: CC-BY-4.0
repository: https://github.com/frmoretto/clarity-gate
triggers:
- clarity gate
- check for hallucination risks
- can an LLM read this safely
- review for equivocation
- verify document clarity
- pre-ingestion check
- cgd verify
- sot verify
capabilities:
- document-verification
- epistemic-quality
- rag-preparation
- cgd-generation
- sot-validation
outputs:
- type: cgd
  extension: .cgd.md
  spec: docs/CLARITY_GATE_FORMAT_SPEC.md
spec_version: '2.1'
```
