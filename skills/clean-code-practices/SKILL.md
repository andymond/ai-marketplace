---
name: clean-code-practices
description: Improve code readability and changeability using practical craftsmanship principles associated with Robert C. Martin's Clean Code, adapted to the project and task.
---

# Clean code practices

Use this skill when writing or refactoring code for clarity and maintainability. It is informed by Robert C. Martin's [Clean Code](https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship-2nd-edition/P200000013239), but apply principles as judgment aids, not mechanical rules.

## Understand the code in context

- Read local instructions, nearby code, and tests. Preserve established conventions unless they obstruct correctness or clarity.
- Identify the behavior that must remain unchanged. Make the smallest useful improvement within the requested scope.
- Prefer code that makes intent easy to understand at the call site and keeps related behavior together.

## Improve clarity

- Use names and encapsulation to communicate purpose and domain meaning. If a comment explains what the next lines do, improve the names or structure first.
- Keep functions and types cohesive around one clear responsibility. Extract a helper when it gives a meaningful name or removes repeated logic; avoid arbitrary size limits and excessive indirection.
- Make data flow and side effects visible. Minimize hidden state, surprising mutation, and functions that appear to answer a question while changing the system. Give a decision an explicit outcome and a separate reason when callers need both.
- Handle errors at a level that can make a useful decision. Preserve relevant context, avoid swallowing failures, and do not use exceptions or sentinel values to obscure ordinary control flow.
- Keep formatting consistent and use comments to explain intent, constraints, or non-obvious decisions that the code cannot express directly.
- Prefer simple designs over speculative generality. Add abstractions when they reduce real coupling or repetition, not to anticipate unsupported future needs.

## Protect behavior while improving code

- Use or add focused tests appropriate to the requested change and the repository's conventions. For refactoring, check that existing behavior remains intact.
- Make one coherent change at a time when that makes regressions easier to identify. Avoid mixing unrelated cleanup into a feature or fix.
- Treat principles such as small functions, low coupling, and avoiding duplication as tradeoffs. A little duplication can be clearer than a premature abstraction; a small function can still have multiple inseparable steps.
- Review the final code as a reader: can the intent, important branches, and failure behavior be followed without reconstructing hidden assumptions?

## Report

Summarize the readability or design issue addressed, the behavior preserved, and the checks run. Call out any remaining tradeoff instead of claiming that a style rule makes the code objectively clean.
