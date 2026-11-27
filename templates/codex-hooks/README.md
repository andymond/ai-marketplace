# Optional Codex development hooks

Use Python 3 and Git. Run these commands from the root of the project where you
want the hooks, replacing the source path with your AI Marketplace checkout.
If the project already has `.codex/hooks.json`, merge the event entries into
it and copy the script.

```sh
mkdir -p .codex/hooks
cp /path/to/ai-marketplace/templates/codex-hooks/development.py .codex/hooks/
cp /path/to/ai-marketplace/templates/codex-hooks/hooks.json .codex/hooks.json
```

In a new Codex session rooted in the project, use `/hooks` to review and trust
the definitions. See the [Codex hooks guide](https://learn.chatgpt.com/docs/hooks).

- **Session start and resume** report the Git root, branch and upstream status,
  existing changes, and number of worktrees.
- **PR preflight** adds advisory context for standalone `gh pr create` and
  `gh pr edit` commands and matching GitHub MCP calls. Pass the actual base explicitly when
  creating a PR for a measured diff. Edit calls ask you to verify the existing
  PR’s head and base. The script compares committed `HEAD` with the
  merge base of the local `origin/<base>` ref. Use a fresh ref and review
  uncommitted or unpushed work separately. Fetching and opening a PR remain
  ordinary workflow steps.
- **Rails changes** under `app/`, `packs/`, `db/`, or `config/` in a measured PR
  diff add a reminder to consult the repo's documented checks.

The preflight measures the current worktree. For a PR from a different head,
an edit targeting a different PR, or a command wrapped in another shell
command, verify the PR's head, base, and full diff directly.
