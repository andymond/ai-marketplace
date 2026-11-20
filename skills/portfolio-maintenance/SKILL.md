---
name: portfolio-maintenance
description: Update a personal software portfolio or career site while keeping its claims accurate, its design intentional, and its project documentation current.
---

# Portfolio maintenance

Use this skill when editing a personal or professional portfolio, résumé site, or career-history page. Keep the site grounded in the owner's current goals and verified experience.

## Work from the real source of truth

- Inspect the current site, repository structure, and relevant README before editing. Check actual files and references; do not assume the README describes the current implementation accurately.
- Use the owner's explicit corrections as authoritative. Compare résumé and site claims where useful, and resolve conflicts before publishing rather than guessing.
- Describe contribution precisely: distinguish building or owning a system from participating in its design, operating it, or being familiar with it.
- Keep copy specific to the person's work and motivations. Avoid generic positioning, repeated claims across sections, and language that turns past assignments into personal preferences.
- When employment status, role progression, dates, or job search status may have changed, verify them with the owner or current source material before presenting them as current.

## Make focused site changes

- Learn the existing structure and design before introducing a framework, dependency, or broad redesign. For a static site, prefer semantic HTML and existing CSS when they meet the request.
- Use native browser features such as `<details>` and `<summary>` for simple disclosure when they provide the needed interaction accessibly.
- Treat image placement and crop as part of the design. Keep imagery proportionate to nearby content, preserve useful focal areas, provide intrinsic dimensions and appropriate alt text, and lazy-load below-the-fold images.
- For visual changes, compare against the intended reference and inspect the actual rendered page at relevant viewport sizes when preview tools are available. Revise mismatched crops, spacing, or hierarchy before calling the change done.
- Keep keyboard access, readable contrast, responsive layout, and reduced-motion preferences in mind when the change affects them.

## Keep documentation truthful

- After a change, compare the README with the actual pages, assets, tooling, local preview steps, and publishing setup. Update any statements made inaccurate by the change.
- Verify package or build claims from manifests and code references. A leftover or unused vendored directory does not by itself mean the site needs that package to build or run.
- Document stable workflows that help the next editor: where content and styles live, how to preview, how résumé links are maintained, and what action publishes the site. Avoid documenting temporary branch or pull request details as permanent project facts.

## Review and delivery

- Read the final diff for factual drift, duplicated copy, unintended asset churn, and changes outside the requested scope.
- Follow the repository's established branch and review workflow. Confirm the intended base and whether to update an existing review or open a new one; do not infer permission to publish, merge, or make external changes from permission to edit locally.
- Summarize what changed and what was checked, including any unresolved factual question or preview limitation.
