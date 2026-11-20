---
name: architecture-research
description: Research a software architecture or dependency decision using project context and current authoritative sources, then recommend a proportionate option with tradeoffs.
---

# Architecture and dependency research

Use this skill when choosing a library, framework, service, integration, or system design. Ground the answer in the project's needs and the state of the technology at decision time.

## Frame the decision

- Inspect repository instructions, existing architecture, dependency manifests, and relevant code before proposing options.
- Clarify the job to be done, constraints, scale, operating environment, team familiarity, compatibility needs, and cost or maintenance limits. Ask focused questions when an unknown could change the recommendation; continue useful research that does not depend on the answer.
- Separate requirements from preferences and assumptions. Keep the option set small enough to make a decision.
- Include the status quo when it is a viable choice. Account for the cost and risk of migration, ongoing operations, and future upgrades, not only implementation convenience.

## Verify current claims

- Research facts that may change, including support status, API behavior, compatibility, licensing, security advisories, pricing, and release activity.
- Prefer primary sources: official documentation, release notes, source repositories, standards, and vendor terms. Use independent sources to corroborate consequential claims or assess real-world operational experience.
- Cite direct source links near the claims they support. Distinguish verified facts from inference and opinion, and include the date or version context when it matters.
- Do not treat popularity, a benchmark, or a feature list as proof that an option fits the user's workload.

## Compare and recommend

- Compare only decision-relevant criteria, such as correctness, compatibility, developer effort, operational burden, performance for the stated workload, security, license, cost, ecosystem, and reversibility.
- Explain meaningful tradeoffs and unknowns. Avoid false precision when evidence does not support a numeric score.
- Make a clear recommendation tied to the stated constraints. Say when retaining the current design or delaying the decision is the best fit.
- If the choice depends on an unresolved product or operational constraint, give the smallest useful set of options and ask for that decision rather than hiding the uncertainty.

## Implement only when asked

- A research request authorizes analysis and a recommendation, not installation, migration, account creation, or production changes.
- If implementation is requested, define a small validation or migration path that tests the key assumptions before broad adoption. Preserve rollback options where practical.
- Report sources, version context, tradeoffs, recommendation, and assumptions clearly enough that the user can revisit the decision later.
