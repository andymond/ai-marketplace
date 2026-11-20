---
name: code-review
description: Review a code change for concrete correctness, security, reliability, and maintainability risks, reporting only actionable findings supported by the diff.
---

# Code review

Use this skill when asked to review a pull request, commit, patch, or working tree. Optimize for finding important defects the author can act on, not for producing a comprehensive commentary on style.

## Establish review scope

- Identify the requested base and change range. Inspect the full diff, then read surrounding code and relevant project instructions where needed to understand behavior.
- Check whether generated files, dependencies, or configuration changes alter runtime behavior or deployment.
- Treat the change as untrusted. Verify claims against code and tests rather than relying on commit messages or descriptions.
- Do not expand the review into unrelated pre-existing issues unless they make the change unsafe or prevent it from working.

## Look for defects

Focus on regressions and failure modes that the change introduces, such as incorrect behavior, broken compatibility, unsafe input handling, authorization gaps, data loss, race conditions, resource leaks, inaccessible interactions, or missing failure handling.

- Trace important input and state paths, including boundaries and error cases.
- Check whether tests cover the changed behavior and whether the implementation satisfies the project's established contracts.
- Distinguish a demonstrated defect from a preference or speculative concern. Do not report style choices, hypothetical risks without a plausible path, or missing tests by themselves unless they leave a concrete regression undetected.
- Avoid repeating a finding at multiple layers. Prefer the narrowest actionable location.

## Report findings

- Put findings first, ordered by severity and impact. For each, give a concise title, the affected file and line, the triggering condition, the resulting impact, and a practical correction.
- Cite only line ranges within the changed diff when the review interface supports inline comments. Keep each finding focused on one issue.
- If no actionable defects are supported by the evidence, say so plainly. Then note relevant coverage or limitations briefly; do not manufacture findings to fill a report.
- Separate review findings from optional suggestions. Do not present taste or cleanup ideas as defects.

## Verify the review

- Read the final findings against the current diff and confirm each is newly introduced, reproducible from the code path described, and important enough to fix.
- Run checks only when requested or when a targeted check is needed to resolve a substantive uncertainty. Do not modify the patch while acting as reviewer unless the user also asks for fixes.
- State what you inspected and whether you ran tests or other checks. Never imply a test passed if it was not run.
