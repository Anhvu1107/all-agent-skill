---
name: fp-either-ref
description: 'ALWAYS use this when the user mentions FP Either REF, asks to build, debug, review, document, automate, test, configure, migrate, or make decisions in this domain, or the task clearly depends on FP Either REF; scope: Quick reference for Either type. Apply the bundled workflow, references, scripts, Senior Master standard, and Codex strict review gate before final output.'
---

# Either Quick Reference

## Selective Reading Rule

Start with:

- `references/senior-master-standard.md`
- `references/usage-routing.md`
- `references/quality-checklist.md`

Then load only the inherited docs, scripts, assets, or examples that match the user's actual task.

Either = success or failure. `Right(value)` or `Left(error)`.

## When to Use
- You need a quick fp-ts reference for typed synchronous error handling.
- The task involves validation, fallible operations, or converting throwing code to `Either`.
- You want a compact cheat sheet rather than a long tutorial.

## Create

```typescript
import * as E from 'fp-ts/Either'

E.right(value)           // Success
E.left(error)            // Failure
E.fromNullable(err)(x)   // null → Left(err), else Right(x)
E.tryCatch(fn, toError)  // try/catch → Either
```

## Transform

```typescript
E.map(fn)                // Transform Right value
E.mapLeft(fn)            // Transform Left error
E.flatMap(fn)            // Chain (fn returns Either)
E.filterOrElse(pred, toErr) // Right → Left if pred fails
```

## Extract

```typescript
E.getOrElse(err => default)  // Get Right or default
E.match(onLeft, onRight)     // Pattern match
E.toUnion(either)            // E | A (loses type info)
```

## Common Patterns

```typescript
import { pipe } from 'fp-ts/function'
import * as E from 'fp-ts/Either'

// Validation
const validateEmail = (s: string): E.Either<string, string> =>
  s.includes('@') ? E.right(s) : E.left('Invalid email')

// Chain validations (stops at first error)
pipe(
  E.right({ email: 'test@example.com', age: 25 }),
  E.flatMap(d => pipe(validateEmail(d.email), E.map(() => d))),
  E.flatMap(d => d.age >= 18 ? E.right(d) : E.left('Must be 18+'))
)

// Convert throwing code
const parseJson = (s: string) => E.tryCatch(
  () => JSON.parse(s),
  (e) => `Parse error: ${e}`
)
```

## vs try/catch

```typescript
// ❌ try/catch - errors not in types
try {
  const data = JSON.parse(input)
  process(data)
} catch (e) {
  handleError(e)
}

// ✅ Either - errors explicit in types
pipe(
  E.tryCatch(() => JSON.parse(input), String),
  E.map(process),
  E.match(handleError, identity)
)
```

Use Either when **error type matters** and you want to chain operations.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
