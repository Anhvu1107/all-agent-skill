---
name: mcp-builder
description: ALWAYS use this when the user wants to build, extend, debug, or wire up an MCP server, tool connector, tool schema, or agent-facing external capability.
---

# MCP Builder

## Selective Reading Rule

Start with:

- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

## Purpose

Create MCP servers that are easy for agents to discover, understand, and use effectively in real tasks.

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/server-design-checklist.md`
- `references/eval-planning.md`

Then load the legacy `reference/` docs that match the implementation language or evaluation task.

## Recommended Process

1. Research the target API or service.
2. Review the MCP specification and framework guidance.
3. Plan tool coverage and resource design.
4. Implement the server with clear schemas and actionable errors.
5. Test the server and build evaluations.

## Design Principles

- Prefer clear, action-oriented tool names.
- Balance broad API coverage with useful workflow tools.
- Keep tools focused on one job each.
- Return predictable structured data when possible.
- Add pagination and filtering so agents can manage context efficiently.
- Write errors that help the agent recover with a concrete next step.

## Core Areas

### Tools

- Validate inputs with strong schemas.
- Describe parameters clearly.
- Mark annotations such as read-only, destructive, idempotent, and open-world behavior when supported.

### Resources

- Use static resources for fixed docs or config.
- Use dynamic resources for generated views.
- Use templates when URI parameters help agents target the right data.

### Transport

- Prefer `stdio` for local servers.
- Prefer stateless HTTP for remote servers unless a stateful transport is clearly needed.

### Security

- Validate all external input.
- Limit resource scope.
- Keep secrets in environment variables.
- Avoid exposing internal implementation details in user-facing errors.

## Testing

- Run build or syntax verification before finishing.
- Test with MCP Inspector when possible.
- Cover unit logic, integration behavior, and schema contracts.

## Evaluations

After implementation, create read-only evaluations that require realistic multi-step reasoning and have stable answers.

## References

Load these as needed:

- `references/server-design-checklist.md`
- `references/eval-planning.md`
- `reference/mcp_best_practices.md`
- `reference/node_mcp_server.md`
- `reference/python_mcp_server.md`
- `reference/evaluation.md`

## Runtime Assets

Use bundled files in `scripts/` for evaluation support and related utilities when they fit the task.
