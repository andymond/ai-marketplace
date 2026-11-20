---
name: debugging
description: Diagnose a software defect from a symptom or report by reproducing it, narrowing the cause with evidence, and making a focused fix.
---

# Debugging

Use this skill when asked to investigate a bug, failure, or unexpected behavior. Prefer a verified explanation and a small corrective change over speculative edits.

## Establish the failure

- Read repository instructions and inspect the affected code, recent changes, configuration, and available logs or error output.
- Clarify the expected behavior, observed behavior, and conditions that trigger it. Ask only for missing information that blocks a useful reproduction; investigate independently while waiting.
- Reproduce the failure with the narrowest safe steps available. Preserve the relevant environment and input, and avoid actions that could damage user data or live systems.
- If it cannot be reproduced, state what is known and what evidence is missing. Do not describe a hypothesis as the root cause.

## Narrow the cause

- Trace the failing path from its inputs through relevant state and dependencies.
- Form a small number of testable hypotheses and choose checks that distinguish among them.
- Change one relevant variable at a time. Prefer existing logs, focused inspection, or a minimal reproduction over broad instrumentation or unrelated refactoring.
- Separate the root cause from symptoms and identify any assumptions about environment, timing, data, or permissions.

## Fix and verify

- Make the smallest change that corrects the cause while preserving intended behavior.
- Add or update a regression test when the project has an appropriate test pattern and the user has requested implementation or verification. Keep the test tied to the observed failure.
- Run the narrowest relevant checks when requested or needed to establish the fix. Do not claim resolution when the original conditions were not exercised.
- If investigation reveals a broader design issue or multiple plausible fixes with different product consequences, explain the options and ask before expanding scope.

## Report

Summarize the triggering conditions, root cause and evidence, the change made (if any), and verification results. Distinguish confirmed facts from remaining uncertainty, and state clearly when the issue could not be reproduced or verified.
