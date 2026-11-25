---
name: pull-request-hygiene
description: Plan, review, or prepare pull requests that are modular and small, targeting fewer than 250 changed lines and fewer than 7 changed files.
---

# Pull request hygiene

Use this skill when preparing or reviewing a pull request. Aim for one cohesive purpose per PR, with fewer than 250 changed lines and fewer than 7 changed files: at most 249 added plus deleted lines and at most 6 files.

## Plan a reviewable change

- Inspect the repository instructions, current branch, intended base, and existing diff before changing files.
- Define the behavior or maintenance outcome this PR owns. Keep unrelated refactors, formatting sweeps, generated churn, and opportunistic fixes out of it.
- Identify tests, docs, and configuration that are necessary to deliver that outcome; keep them in scope rather than cutting them to meet a size target.
- Estimate changed lines and files early. If the work is likely to exceed either limit, split it into coherent, independently reviewable steps before implementation.
- For dependent changes, use a clear sequence of branches or stacked PRs and target each PR at the branch it depends on. Explain the dependency and how to retarget or rebase after earlier PRs merge.

## Measure the whole PR

- Count the complete diff against the PR's actual base, not just the latest commit. Include additions and deletions across code, tests, docs, and configuration. Count every changed file; binary or renamed files still count toward the file limit.
- Use `git diff --shortstat <base>...HEAD` for a quick total and `git diff --numstat <base>...HEAD` to inspect per-file counts. Confirm the base branch is current and matches the pull request.
- Keep the PR under both limits throughout review. Recheck after each substantial update, including generated files or merge-base changes.
- Do not hide scope by removing needed tests, splitting one logical change into misleading commits, or treating a large unrelated diff as an exception.

## Split when needed

- Choose boundaries that preserve useful behavior and make each PR understandable on its own. Examples include a prerequisite refactor, an isolated feature slice, or documentation that can be reviewed independently.
- Avoid artificial splits that leave every intermediate branch broken or make reviewers reconstruct the whole change. If the work cannot be split cleanly, explain why and ask the user before exceeding the limits.
- When an existing PR already exceeds the limits, report the actual counts and offer a split plan; do not silently expand it further.

When a pull request already has review activity and needs splitting, use the [review-preserving split example](references/review-preserving-splits.md).

## Prepare the review

- Verify the PR diff contains only its intended purpose and stays within the line and file limits.
- For code changes, do a self-review against the full base diff. Trace public inputs through the changed behavior and specs. Use the clean-code guidance and any applicable framework skill if available. Correct concrete readability or convention issues before asking for review.
- Run requested or project-relevant checks, and report what was and was not run. Do not claim unrun checks passed.
- Write a concise title and description covering intent, scope, tests, and dependencies on other PRs. Request review or open the PR when asked; do not merge unless the user asks.
