---
name: clean-code-practices
description: Write or refactor code for simplicity and modularity. Make control flow and responsibilities clear with meaningful method and variable names, and remove redundant logic while preserving behavior.
---

# Clean code practices

Use this skill when writing or refactoring code for clarity and maintainability. It is informed by Robert C. Martin's [Clean Code](https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship-2nd-edition/P200000013239), but apply principles as judgment aids, not mechanical rules.

## Understand the code in context

- Read local instructions, nearby code, and tests. Preserve established conventions unless they obstruct correctness or clarity.
- Identify the behavior that must remain unchanged. Make the smallest useful improvement within the requested scope.
- Prefer code that makes intent easy to understand at the call site and keeps related behavior together.

## Make the normal path easy to read

- Start with direct code in the module that owns the behavior. Read the entry point in execution order. Prefer positive conditions and short guards that keep the main path flat. In Ruby, reserve `unless` for a simple guard that reads naturally.
- Name a compound condition after the decision it represents. Use a local variable when the name helps at one site, and a named method when the operation has a coherent responsibility or the name makes the caller easier to follow. Keep straightforward expressions inline.
- Remove branches, fallback paths, duplicate validation, and state that serve no distinct behavior. When two cases have the same result and require the same caller action, handle them together. Check behavior for missing, invalid, and previously persisted values before simplifying.
- Keep related reads and writes together, particularly when they share a transaction or lock. Extract work behind a focused interface when the caller can use it without knowing the implementation details.

- Use names and encapsulation to communicate purpose and domain meaning. If a comment explains what the next lines do, improve the names or structure first.
- In Ruby, prefer `attr_reader`, `attr_writer`, or `attr_accessor` for instance state, and use those methods inside the class instead of reading or assigning `@instance_variable` directly. Keep accessors private when the state is internal.
- Follow each important value from the public signature to the branch that uses it. Keep the same domain name across layers when the value has the same meaning. If a policy accepts only a user ID, call it `user_id` at the entry point and downstream. Use a broader name only when that boundary actually supports the broader concept.
- Make data flow and side effects visible. At a boundary, trace who produced or validated a value and who consumes it. Use names that make that origin or handoff clear where a framework API hides it. Minimize hidden state, surprising mutation, and functions that appear to answer a question while changing the system. Give a decision an explicit outcome and a separate reason when callers need both.
- Name predicates for the state they examine when several states coexist. Use named arguments when mapping multiple similar values into a value object so the mapping is visible at the call site.
- Handle errors at a level that can make a useful decision. Preserve relevant context, avoid swallowing failures, and do not use exceptions or sentinel values to obscure ordinary control flow.
- Keep formatting consistent and use comments to explain intent, constraints, or non-obvious decisions that the code cannot express directly.
- Keep each new layer accountable for a real responsibility. A forwarding wrapper, a flag with no consumer, or a catch-all configuration object adds work for readers. Use repository conventions and existing interfaces before introducing another abstraction.

## Protect behavior while improving code

- Use or add focused tests appropriate to the requested change and the repository's conventions. For refactoring, check that existing behavior remains intact.
- Make one coherent change at a time when that makes regressions easier to identify. Avoid mixing unrelated cleanup into a feature or fix.
- Treat principles such as small functions, low coupling, and avoiding duplication as tradeoffs. A little duplication can be clearer than a premature abstraction; a small function can still have multiple inseparable steps.
- State expected behavior directly in tests. Use explicit cases or a matrix when testing grants or state transitions. A test should still express the same expectation if unrelated inputs are reordered.
- Before handing off, read the whole diff from its entry points through the relevant tests. Fix unclear names, hidden assumptions, and unnecessary indirection while the change is still focused.

## Report

Summarize the readability or design issue addressed, the behavior preserved, and the checks run. Call out any remaining tradeoff instead of claiming that a style rule makes the code objectively clean.
