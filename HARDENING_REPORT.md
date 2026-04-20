# Hardening Report

Vietnamese version: `BAO_CAO_HARDENING.md`

Audit date: 2026-04-20

## Goal

Make this bundle safer to publish, easier for other AIs to use immediately, and less ambiguous around ownership, external connectivity, or machine side effects.

## Changes Applied

- Removed 4 restrictive-license skills from the public bundle:
  - `.agent/skills/docx`
  - `.agent/skills/pdf`
  - `.agent/skills/pptx`
  - `.agent/skills/xlsx`
- Cleaned `.agent/mcp_config.json` into an empty config so no external MCP services are enabled by default.
- Normalized `.claude-plugin/marketplace.json`:
  - removed personal owner metadata
  - removed the stale `./skills/...` paths that no longer matched the merged layout
  - updated metadata to the current bundle name
- Hardened `.agent/scripts/auto_preview.py`:
  - removed `shell=True`
  - resolved npm/yarn/pnpm/bun on Windows more explicitly
- Expanded `.gitignore` to ignore runtime files and logs produced during preview flows.
- Updated routing, the quality bar, and the usage guide toward a local-first operating model.
- Audited 2 new community bundles (`superpowers-main.zip`, `antigravity-awesome-skills-main.zip`) before merging.
- Did not import launcher files or app shells from external bundles into the primary skill tree:
  - `superpowers-main/hooks/run-hook.cmd`
  - `antigravity-awesome-skills-main/START_APP.bat`
  - `antigravity-awesome-skills-main/scripts/activate-skills.bat`
- Only absorbed high-value workflows by rewriting them in local-first style inside the current skill tree.

## Audit Results

- No unexpected hidden files were found outside `.git`.
- No leftover junctions or reparse points were found.
- No suspicious executable binaries were found in the repo.
- The remaining skills do not automatically connect outward; skills that use external providers remain opt-in and must be invoked explicitly.
- A custom Windows Defender scan was run on `D:\\skill\\skill\\agent-skills-unified`, and no threats were reported.
- No `.bat`, `.cmd`, web app, or launcher script files from the 2 new bundles were added into the canonical skill library.

## State After Hardening

- The current skill library is strengthened by new workflows for verification, worktrees, plan execution, review handling, branch closeout, and closed-loop delivery.
- The default configuration is local-first, with no external MCP servers enabled by default.
- Plugin/market metadata has been cleaned up to match the current merged bundle.

## Operating Notes

- If you want to use external MCP servers, add that configuration yourself after manual review.
- If you want to restore office-document skills, only add them back from sources you are certain you have the right to use and redistribute.
- Scripts in this repo can still read project files or run subprocesses when you invoke them intentionally, but the bundle does not ship any config that automatically pulls data from the machine.
