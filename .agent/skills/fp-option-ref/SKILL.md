---
name: fp-option-ref
description: 'ALWAYS use this when the user mentions FP Option REF, asks to build, debug, review, document, automate, test, configure, migrate, or make decisions in this domain, or the task clearly depends on FP Option REF; scope: Quick reference for Option type. Apply the bundled workflow, references, scripts, Senior Master standard, and Codex strict review gate before final output.'
---

# Option Quick Reference

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

Option = value that might not exist. `Some(value)` or `None`.

## When to Use
- You need a quick fp-ts reference for nullable or optional values.
- The task involves eliminating null checks, safe property access, or optional chaining with `Option`.
- You want a short reference card rather than a full migration guide.

## Create

```typescript
import * as O from 'fp-ts/Option'

O.some(5)              // Some(5)
O.none                 // None
O.fromNullable(x)      // null/undefined → None, else Some(x)
O.fromPredicate(x > 0)(x) // false → None, true → Some(x)
```

## Transform

```typescript
O.map(fn)              // Transform inner value
O.flatMap(fn)          // Chain Options (fn returns Option)
O.filter(predicate)    // None if predicate false
```

## Extract

```typescript
O.getOrElse(() => default)  // Get value or default
O.toNullable(opt)           // Back to T | null
O.toUndefined(opt)          // Back to T | undefined
O.match(onNone, onSome)     // Pattern match
```

## Common Patterns

```typescript
import { pipe } from 'fp-ts/function'
import * as O from 'fp-ts/Option'

// Safe property access
pipe(
  O.fromNullable(user),
  O.map(u => u.profile),
  O.flatMap(p => O.fromNullable(p.avatar)),
  O.getOrElse(() => '/default-avatar.png')
)

// Array first element
import * as A from 'fp-ts/Array'
pipe(
  users,
  A.head,  // Option<User>
  O.map(u => u.name),
  O.getOrElse(() => 'No users')
)
```

## vs Nullable

```typescript
// ❌ Nullable - easy to forget checks
const name = user?.profile?.name ?? 'Guest'

// ✅ Option - explicit, composable
pipe(
  O.fromNullable(user),
  O.flatMap(u => O.fromNullable(u.profile)),
  O.map(p => p.name),
  O.getOrElse(() => 'Guest')
)
```

Use Option when you need to **chain** operations on optional values.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
