---
name: spec-driven-development
description: Turn a software request into accepted user stories and observable acceptance criteria, then write tests and implement the smallest change that satisfies them.
---

# Spec driven development

Use this skill for feature work where requirements need to be clarified or behavior should be specified before implementation. Keep the specification proportional to the change: a small, clear request may need only a short checklist.

## Understand the request

- Read relevant project instructions and inspect nearby code, tests, and conventions before proposing a solution.
- Restate the user, goal, and expected outcome in plain language. Identify constraints, assumptions, edge cases, and explicit exclusions that affect behavior.
- Ask focused questions only for decisions that materially change the result. Continue independent discovery and preparation while waiting.
- Do not invent product behavior to fill gaps. Mark assumptions so the user can accept or correct them.

## Specify behavior

- Write user stories in the form “As a [user], I want [capability], so that [outcome]” when that framing adds clarity.
- Express acceptance criteria as observable outcomes, with relevant failure cases and boundaries. Avoid implementation prescriptions unless they are requirements.
- Link each criterion to a verification approach. Prefer tests at the level that demonstrates the user-visible behavior; add lower-level tests where they cover important logic more clearly.
- Keep scope and unresolved questions visible. Do not turn optional ideas into requirements.

## Agree on the spec when needed

- Present a concise spec and wait for acceptance before implementation when the user requested a review checkpoint, when important behavior remains uncertain, or when the change is consequential or broad.
- For a clear, bounded request with no meaningful ambiguity, state the working criteria and proceed without adding an unnecessary approval round.
- Treat the user's corrections as updates to the spec. Revisit affected criteria and tests before continuing.

## Test, implement, and report

- Follow the repository's existing test tools and patterns. Start with the narrowest useful checks; do not add a new test framework just for process conformity.
- Write tests that correspond to acceptance criteria and verify externally meaningful outcomes. Avoid tests that only mirror internal implementation details.
- For net new functionality, run the new targeted tests before implementing and confirm they fail because the required behavior is missing. This red-before-green check is required; if it cannot be run safely or meaningfully, explain why and resolve that limitation before proceeding.
- For bug fixes and other changes, use red-before-green as a preferred check when practical. The failure should demonstrate the reported behavior or missing requirement, not an unrelated setup, import, or test harness problem. Existing tests unrelated to the new behavior should remain passing.
- Implement the smallest coherent change that meets the accepted criteria. If implementation reveals a spec gap, pause to clarify when it changes user-visible behavior; otherwise document a reasonable local assumption.
- Run relevant checks when the user asks for verification or the task calls for it. Report the commands and results accurately, along with criteria not covered by automated checks.
- Summarize the accepted behavior, important implementation choices, and any remaining uncertainty. Do not claim the feature is complete if a required criterion is unimplemented or unverified.
