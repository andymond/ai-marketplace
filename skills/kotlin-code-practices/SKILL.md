---
name: kotlin-code-practices
description: Write, refactor, or review Kotlin code for readability and maintainability. Use for Kotlin control flow, nullability, collection pipelines, public APIs, Java interop, or coroutine changes.
---

# Kotlin code practices

Read the repository instructions, nearby Kotlin code and tests, and the module's build and lint configuration. Follow its Kotlin version and conventions. Preserve caller-visible behavior during refactors, including ordering, exception behavior, mutation, and cancellation.

## Make the next reader's job easy

- Read the call site first. Use names that say what a value represents or what an operation does. Use named arguments for positional booleans and same-typed parameters when their meaning would otherwise be unclear.
- Choose the flow that makes decisions and side effects easiest to follow. A short `map` or `filter` pipeline works well for transformations. Use a loop when several exits, state updates, or effects need to stay visible. Check whether changing a pipeline would change evaluation order, allocation, or consumption of its input.
- Use scope functions for one clear job. Use `let` for a small nullable transformation and `apply` for configuring an object. Introduce a named local when nested receivers, `it`, or a long chain make ownership hard to see. Add an extension when the receiver makes the call more natural.
- Extract a helper when its name conveys a useful decision or hides stable mechanics. Keep related logic together and avoid renames or formatter churn outside the requested change.

## Make types and boundaries carry intent

- Model legitimate absence with nullable types and handle it where the policy belongs. Validate Java platform types and external input at the boundary. Reserve `requireNotNull` and `checkNotNull` for argument and state invariants. Avoid `!!`, unchecked casts, and fallback values that hide invalid input.
- Use a sealed result or a named domain type when callers must distinguish outcomes or values that are easy to mix up. Use an exhaustive `when` when new variants should require a caller decision. Keep simple operations simple.
- Prefer `val` and read-only collection interfaces when mutation is unnecessary. A read-only view can still share mutable backing data. Copy at an ownership boundary when the contract promises an independent snapshot.
- Keep implementation details private or internal. Give public library functions explicit return types and document ownership, effects, and failure behavior when callers need them. Review Kotlin and Java call sites before changing a published API, including overloads and default arguments.

## Keep coroutine behavior visible

- Launch work in a scope owned by the operation or application lifecycle. Make start and shutdown behavior clear. A `suspend` function can still block a thread, so move blocking I/O to the appropriate dispatcher at the boundary that owns it.
- Preserve cancellation when translating failures, including in broad catches and `runCatching` recovery. Rethrow `CancellationException` when caught. Keep resource cleanup tied to ownership with `use` or `finally`.

## Verify the change

Run the repository's focused tests and configured Kotlin formatting or analysis tasks. Cover changed behavior at the call boundary, such as absent input, collection order, mutation of shared data, or cancellation. In review, explain the readability impact with a concrete call site and distinguish a behavioral issue from a style preference.

Sources

[Kotlin coding conventions](https://kotlinlang.org/docs/coding-conventions.html), [scope functions](https://kotlinlang.org/docs/scope-functions.html), [collection types](https://kotlinlang.org/docs/collections-overview.html), [Java interop](https://kotlinlang.org/docs/java-interop.html), [API readability](https://kotlinlang.org/docs/api-guidelines-readability.html), [API compatibility](https://kotlinlang.org/docs/api-guidelines-backward-compatibility.html), and [coroutine cancellation](https://kotlinlang.org/docs/cancellation-and-timeouts.html).
