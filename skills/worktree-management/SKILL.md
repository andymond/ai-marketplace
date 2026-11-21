---
name: worktree-management
description: Manage parallel Git worktrees safely, including resource-aware setup for concurrent agents and cleanup after pull requests finish.
---

# Git worktree management

Use this skill when creating, coordinating, moving, or cleaning up linked Git worktrees. Follow the [official `git worktree` documentation](https://git-scm.com/docs/git-worktree) for version-specific command behavior.

## Before adding parallel work

- Inspect current worktrees with `git worktree list --porcelain` and check each relevant tree's branch and status before assigning work.
- Before starting multiple agents or parallel builds, assess available memory and current memory pressure with tools appropriate to the host OS. On Linux, `free -h` and `/proc/meminfo` can help; on macOS, `vm_stat`, `memory_pressure`, and `sysctl hw.memsize` can help. Use observed headroom and active workload, not a universal RAM cutoff.
- Account for the work itself: worktrees share Git objects, but separate builds, language servers, test processes, dependency installs, and agent contexts can use substantial additional memory. Start with limited concurrency, monitor pressure, and add workers only while the machine remains responsive with adequate headroom.
- If memory pressure is already high, swap is growing, or the workload is heavy, work sequentially or reduce the number of concurrent agents. Do not launch a large batch first and assume the machine will cope.

## Create and use worktrees

- Create a new branch in a linked worktree with `git worktree add -b <branch> <path> <base>`; use a current, intended base rather than guessing. For an existing branch, use `git worktree add <path> <branch>`.
- Use `git worktree add --detach <path> <commit>` for disposable inspection or experiments that do not need a branch.
- Each worktree has its own working directory, `HEAD`, and index, while branches and repository objects are shared. A branch normally cannot be checked out in two worktrees at once. Coordinate branch ownership and commits accordingly.
- Confirm the new tree with `git -C <path> status --short --branch` and `git worktree list` before asking an agent to use it. Keep each agent's scope, branch, and expected deliverable distinct.
- Use `git worktree move` to relocate a linked worktree. If it was moved outside Git, use `git worktree repair` to restore the administrative link. Lock a worktree only when it is intentionally unavailable, such as on removable storage, and provide a reason.

## Clean up when a pull request is merged or closed

- Verify the pull request's final state and identify its branch and worktree. A closed pull request may be unmerged; do not treat closure as proof that its commits are disposable.
- Before removal, inspect the tree with `git -C <path> status --short --branch`, `git -C <path> log`, and its diff against the appropriate base. Ensure wanted work is committed and preserved on the branch or elsewhere.
- Remove the linked worktree with `git worktree remove <path>` after it is clean. This is intentionally refused for modified or untracked content. Do not bypass the safeguard with `--force` to save time; preserve or obtain direction for valuable changes first.
- For a merged PR, delete the local topic branch only after verifying it is merged, it is not checked out in another worktree, and deletion fits the repository workflow. For a closed but unmerged PR, remove the worktree after preserving its branch and commits; do not delete unique work just because the PR is closed.
- If someone manually deleted a worktree directory, inspect `git worktree list` and run `git worktree prune --dry-run` before `git worktree prune`. Prune removes stale administrative records; it does not recover work from the deleted directory.
- Never remove the main worktree as though it were a linked worktree.

## Report

Summarize the worktree paths and branches created or removed, how you preserved work from closed or unmerged PRs, any stale metadata pruned, and any concurrency limit chosen because of machine resource pressure.
