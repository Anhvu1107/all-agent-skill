# Eval Planning

Use this when the MCP server works locally and now needs a believable evaluation story.

## Good Evaluations

- require multiple tool calls or realistic reasoning
- have stable expected outcomes
- surface whether the agent can recover from API or schema friction

## Avoid

- toy prompts that only prove the happy path
- evaluations whose answers depend on hidden context
- tasks that only measure whether the server compiled
