# UI Guardrails

Use this reference when the work touches Tailwind, component systems, layout polish, or interaction quality.

## Structure

- Prefer the project's existing component primitives before introducing a new library.
- Use accessible primitives for focus, keyboard, dialogs, menus, tabs, and popovers.
- Do not mix multiple primitive systems on the same interaction surface unless the repo already does.
- Add an accessible label to icon-only buttons.

## Layout

- Prefer `h-dvh` over `h-screen` for full-height mobile layouts.
- Respect safe-area insets for fixed headers, footers, and bottom actions.
- Use a deliberate z-index scale instead of arbitrary one-off layers.
- Prefer `size-*` for square elements when using Tailwind.

## Motion

- Animate only when the task benefits from it.
- Prefer `transform` and `opacity`; avoid layout-thrashing properties.
- Keep interaction feedback fast and restrained.
- Respect reduced motion when the UI has noticeable animation.
- Avoid large animated blur, glow, or backdrop effects as a default visual crutch.

## Typography

- Keep tracking changes rare and intentional.
- Use balanced headings and readable body copy instead of squeezing text with styling tricks.
- Use tabular numerals for dense numeric UI.
- Clamp or truncate only when the layout truly requires it.

## Interaction

- Use a confirmation dialog for destructive actions.
- Show errors near the action that caused them.
- Do not block paste in inputs and textareas.
- Prefer structural skeletons or clear loading states over blank waiting surfaces.

## Visual Discipline

- Avoid generic glow-heavy SaaS styling.
- Avoid default purple gradients and multicolor noise unless the brand truly calls for it.
- Keep accent color usage intentional; one main accent per view is a good default.
- Use theme tokens or existing design tokens before inventing new raw values.
