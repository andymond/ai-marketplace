# Marketplace contributor guidance

These instructions apply when creating or updating skills, templates, and documentation in this repository. Keep the marketplace focused on reusable agent guidance that improves real work.

## Shape skills around a real task

- Give each skill a clear task and a discriminating description that helps an agent know when it applies.
- Put a `SKILL.md` in a descriptively named, lowercase, hyphenated folder under `skills/`. The folder name and YAML `name` must match; include the required `description` in frontmatter.
- Assume the agent is already capable. Include non-obvious context, decision criteria, workflow details, or failure modes that improve the result. Avoid generic advice, repeated platform policies, and rigid steps where judgment is useful.
- Preserve user intent and existing authorization boundaries. A skill should guide the requested task, not broaden it into unrelated work or imply permission for external actions.
- Keep the entrypoint concise. Add scripts, references, or assets only when they have a concrete use, and link supporting files from `SKILL.md` where relevant.
- Avoid placeholders and scaffolding in finished skills. Keep examples only when they materially clarify a decision.

## Use sources responsibly

- When a skill is based on a book, article, standard, or tool documentation, link the source and distinguish its ideas from additional project guidance.
- Summarize ideas in original wording. Do not reproduce substantial copyrighted text or turn an author's prescriptions into universal rules when judgment and context matter.
- Check claims that may have changed against current authoritative documentation. Prefer primary sources for tool behavior and specifications.

## Maintain the marketplace

- Update the root `README.md` when adding or renaming skills or templates. Keep each listing short and accurate about when to use the item.
- Keep this root `AGENTS.md` focused on contributing to the marketplace. `templates/AGENTS.md` is a starter for other projects; it serves a different audience and should remain generic and customizable.
- Validate new or updated skills with the Codex skill creator's `quick_validate.py` when available. If it cannot run because a dependency or tool is missing, report that and use a suitable structural check; do not claim the official validator passed.
- Review links, folder and frontmatter names, placeholders, and README listings. Run new helper scripts when they are part of the change. Do not add test suites to instruction-only changes unless requested.

## Keep reviews focused

- Aim for one coherent outcome per pull request, fewer than 250 changed lines, and fewer than 7 changed files. Count the complete diff against the actual base, including tests, docs, and configuration.
- Split larger work at useful boundaries. Do not omit necessary guidance or validations just to fit the limit; if no clean split exists, explain the tradeoff and ask before exceeding it.
- State dependencies when using stacked pull requests. Keep the target branch and diff clear, and leave merge decisions to the user unless they ask you to merge.
