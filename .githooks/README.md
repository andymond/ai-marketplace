# Learning quiz pre-commit hook

This hook generates a short quiz from staged changes, asks for answers, and uses Codex CLI to give supportive feedback before allowing a commit.

## Run on a commit

Install the [Codex CLI](https://developers.openai.com/codex/cli) and sign in, then configure this checkout to use the tracked hooks directory:

```sh
git config core.hooksPath .githooks
```

After setting the hooks path, request the quiz for a specific commit:

```sh
RUN_LEARNING_QUIZ=1 LEARNING_QUIZ_FOCUS="the transaction boundary" git commit
```

Ordinary commits skip the quiz. Git does not enable repository hooks just because the files exist. This setting is local to your checkout. To disable the hook later:

```sh
git config --unset core.hooksPath
```

To use it in another project, copy `.githooks/pre-commit` into that project's `.githooks/` directory and set `core.hooksPath` there.
If Git is launched from an application that does not inherit the Codex CLI path, set `CODEX_BIN` to the executable path in that application's environment.

## What it does

- Skips commits with no staged changes.
- Shows 2–3 questions about the staged diff, usually covering behavior, tests, and an important implementation concept. Set `LEARNING_QUIZ_FOCUS` before `git commit` to emphasize a topic.
- Asks before sending staged code to Codex. The diff and answers are sent using the signed-in Codex CLI account; review for secrets or private data before consenting.
- Uses a read-only, ephemeral Codex session. It does not modify the index or working tree.
- Gives one coaching round when an answer shows a material gap. It allows the commit when the follow-up demonstrates reasonable alignment; it is not an exam and does not require exact terminology.
- Blocks the commit if Codex is unavailable, there is no interactive terminal, consent is declined, or understanding remains unclear. To bypass once, run `SKIP_LEARNING_QUIZ=1 git commit ...`.

The hook only sees staged changes. Stage the files you intend to ship before committing.

## Open a review-ready PR after a commit

Install and sign in to the [GitHub CLI](https://cli.github.com/). From the
checkout where you want this behavior, run:

```sh
git config core.hooksPath .githooks
git config --local hooks.openReviewPr true
```

After a successful commit, GitHub CLI looks up the current branch's PR and
opens it in your browser if it's open and out of draft. The browser shows the
latest pushed revision. Push your new commit when you're ready to include it
in the review. Draft, closed, and merged PRs are skipped. CI and reviewer
approval use the PR's normal workflow.

To skip the browser for one commit, run
`git -c hooks.openReviewPr=false commit`. To turn off the behavior for the
checkout, run `git config --local hooks.openReviewPr false`.

To use the hook in another project, copy `.githooks/post-commit` into its
hooks directory and apply the opt-in setting there.
