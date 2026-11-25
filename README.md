# AI Marketplace

A growing collection of practical agent skills for contemporary software work. Each skill is a self-contained folder with a `SKILL.md` that explains when to use it and the project-specific guidance that improves the work.

## Install in Claude Code

This repository is a Claude Code plugin marketplace with one plugin, `ai-marketplace`, that contains every skill below. Install it in any project:

```text
/plugin install ai-marketplace --marketplace andymond/ai-marketplace
```

On Claude Code versions before 2.1.275, add the marketplace first:

```text
/plugin marketplace add andymond/ai-marketplace
/plugin install ai-marketplace@andymond
```

Skills load as `ai-marketplace:<skill-name>`, for example `ai-marketplace:code-review`. Run `/plugin marketplace update andymond` to pick up new skills.

## Skills

- [`skills/accessible-technical-documentation`](skills/accessible-technical-documentation/SKILL.md) — write readable technical prose, lists, tables, and diagrams with text equivalents.
- [`skills/multi-repo-rfc-planning`](skills/multi-repo-rfc-planning/SKILL.md) — scope shared contracts and repository decisions, then coordinate linked RFC reviews.
- [`skills/learning-driven-development`](skills/learning-driven-development/SKILL.md) — pair with a developer so implementation builds understanding as well as working software.
- [`skills/pull-request-hygiene`](skills/pull-request-hygiene/SKILL.md) — keep PRs cohesive, under 250 changed lines, and under 7 changed files.
- [`skills/worktree-management`](skills/worktree-management/SKILL.md) — coordinate Git worktrees and parallel agents with resource-aware setup and safe PR cleanup.
- [`skills/clean-code-practices`](skills/clean-code-practices/SKILL.md) — improve clarity and changeability using practical Clean Code principles.
- [`skills/kotlin-code-practices`](skills/kotlin-code-practices/SKILL.md) — write and review readable Kotlin with clear control flow, APIs, and coroutine boundaries.
- [`skills/rails-application-practices`](skills/rails-application-practices/SKILL.md) — use Rails conventions for Active Record, policy, migrations, and package boundaries.
- [`skills/clean-architecture`](skills/clean-architecture/SKILL.md) — shape proportionate boundaries and dependencies informed by Clean Architecture.
- [`skills/domain-probe-observability`](skills/domain-probe-observability/SKILL.md) — express business observations through domain probes while encapsulating instrumentation.
- [`skills/spec-driven-development`](skills/spec-driven-development/SKILL.md) — turn requirements into user stories and acceptance criteria, then tests and implementation.
- [`skills/code-review`](skills/code-review/SKILL.md) — report actionable defects supported by the code change.
- [`skills/debugging`](skills/debugging/SKILL.md) — reproduce failures, identify their cause, and make focused fixes.
- [`skills/architecture-research`](skills/architecture-research/SKILL.md) — compare architecture or dependency choices against project context and current sources.
- [`skills/portfolio-maintenance`](skills/portfolio-maintenance/SKILL.md) — maintain a personal portfolio site, keep its README accurate, and ground design and copy in verified experience.

## Add a skill

Create a descriptively named folder under `skills/` with a `SKILL.md`. Keep each skill focused on a repeatable task, and include only guidance that changes decisions or prevents known mistakes. Add scripts or references when they have a clear use; avoid scaffolding that a skill does not need.

Validate a skill with the Codex skill creator's validator when available:

```sh
python3 /path/to/skill-creator/scripts/quick_validate.py skills/<skill-name>
```

Skills in this repository are source files for review and reuse. Claude Code picks up every folder under `skills/` through the plugin (see [Install in Claude Code](#install-in-claude-code)); for other agents, install or link a skill into the agent's skill directory. After adding a skill, run `claude plugin validate .` and bump `version` in `.claude-plugin/plugin.json` so installed copies update.

## Templates

- [`templates/AGENTS.md`](templates/AGENTS.md) — optional starting point for project-specific agent instructions. Replace the prompts with verified details, remove irrelevant sections, and keep commands and constraints current.
- [`.githooks/pre-commit`](.githooks/pre-commit) — optional interactive learning quiz for staged changes; see [hook setup and privacy notes](.githooks/README.md).
