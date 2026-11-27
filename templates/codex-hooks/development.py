"""Report local Git context and advisory PR checks for Codex hooks."""

import json
import re
import shlex
import subprocess
import sys
from pathlib import Path


def git(cwd, *args):
    return subprocess.check_output(
        ["git", *args], cwd=cwd, encoding="utf-8", errors="replace", stderr=subprocess.DEVNULL
    ).rstrip("\n")


def session_context(cwd):
    root = git(cwd, "rev-parse", "--show-toplevel")
    status = git(cwd, "status", "--short", "--branch", "--untracked-files=normal")
    branches = git(cwd, "worktree", "list", "--porcelain")
    worktrees = sum(line.startswith("worktree ") for line in branches.splitlines())
    return f"Git root: {root}\nWorktrees: {worktrees}\nLocal status:\n{status[:1500]}"


def flag(words, names):
    for index, word in enumerate(words):
        key, separator, value = word.partition("=")
        if key in names:
            return value if separator else (words[index + 1] if index + 1 < len(words) else None)
    return None


def pr_request(payload):
    arguments = payload.get("tool_input", {})
    if not isinstance(arguments, dict):
        return None
    if payload.get("tool_name") == "Bash":
        try:
            words = shlex.split(arguments.get("command", ""))
        except ValueError:
            return None
        if words[:3] == ["gh", "pr", "edit"]:
            return None, None
        if words[:3] != ["gh", "pr", "create"]:
            return None
        return flag(words, {"--base", "-B"}), flag(words, {"--head", "-H"})
    if payload.get("tool_name", "").endswith("update_pull_request"):
        return None, None
    return arguments.get("base"), arguments.get("head")


def pr_context(cwd, base, head):
    if not isinstance(base, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]*", base):
        return "PR preflight: confirm the actual PR base and measure the complete diff against it."
    branch = git(cwd, "branch", "--show-current")
    if head is not None and head != branch:
        return "PR preflight: verify the specified PR head and base before measuring the diff."
    try:
        base_ref = git(cwd, "rev-parse", "--verify", f"refs/remotes/origin/{base}^{{commit}}")
        merge_base = git(cwd, "merge-base", base_ref, "HEAD")
    except subprocess.CalledProcessError:
        return f"PR preflight: origin/{base} is unavailable locally. Fetch or confirm the actual base."
    diff = git(cwd, "diff", "--numstat", "-z", "--no-renames", merge_base, "HEAD", "--")
    rows = [row.split("\t", 2) for row in diff.split("\0") if row]
    changed_files = [(sum(int(count) for count in row[:2] if count != "-"), row[2]) for row in rows]
    lines = sum(count for count, _ in changed_files)
    binary_files = sum(row[0] == "-" for row in rows)
    notes = [f"PR preflight against local origin/{base}: {lines} changed lines across {len(rows)} files."]
    if binary_files:
        notes.append(f"Binary files counted toward the file total: {binary_files}.")
    if lines > 249 or len(rows) > 6:
        notes.append("Above the review target of 249 changed lines and six files. Inspect git diff --stat against the actual PR base and consider a reviewable split.")
        largest = sorted(changed_files, reverse=True)[:3]
        notes.append("Largest files by changed lines: " + ", ".join(f"{path!r} ({count})" for count, path in largest))
    if git(cwd, "status", "--porcelain"):
        notes.append("Working-tree changes are outside this committed diff.")
    paths = [row[2] for row in rows]
    root = Path(git(cwd, "rev-parse", "--show-toplevel"))
    if (root / "bin/rails").is_file() and any(
        path.startswith(("app/", "packs/", "db/", "config/")) for path in paths
    ):
        notes.append("Rails changes detected. Use the README checks. Review PostgreSQL-backed specs for persistence changes and Zeitwerk and Packwerk for class or package boundary changes.")
    return "\n".join(notes)


def main():
    payload = json.load(sys.stdin)
    cwd = payload.get("cwd", ".")
    event = payload.get("hook_event_name")
    try:
        if event == "SessionStart":
            context = session_context(cwd)
        elif event == "PreToolUse":
            request = pr_request(payload)
            if request is None:
                return
            context = pr_context(cwd, *request)
        else:
            return
    except (OSError, subprocess.CalledProcessError):
        return
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": event,
        "additionalContext": context,
    }}))


if __name__ == "__main__":
    main()
