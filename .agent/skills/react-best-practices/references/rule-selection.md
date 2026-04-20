# Rule Selection

Use this to narrow the React rule set before reading dozens of files.

## Route By Bottleneck

- slow first load or heavy bundles: start with bundle and async rules
- wasted renders or jittery interactions: start with rerender and rendering rules
- slow server-side data flow: start with server and async rules
- vague code review request: scan the highest-priority categories first
