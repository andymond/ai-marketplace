---
name: multi-repo-rfc-planning
description: Plan a software change across repositories by identifying shared contracts, scoping repository-specific decisions, and coordinating linked RFC reviews.
---

# Multi-repo RFC planning

Use this skill when a feature or epic spans repositories and needs architectural review. Read the accepted product spec, open stories, repository instructions, existing ADRs, and relevant PR discussions before drafting.

## Assign each decision an owner

- Put a decision in the shared docs when a change to it requires another repository to change behavior or when reviewers need to approve an interface between repositories. Typical examples include API semantics, identity boundaries, event schemas, compatibility, and rollout guarantees.
- Keep a decision with the implementing repo when that repo can change it while preserving the shared contract. Typical examples include library selection, internal storage schema, component structure, and local test runners.
- Treat the split as a consequence of the decisions. A feature with one contract and no substantial repo-specific choices may need one RFC. A feature that merely touches several repos may need only local implementation plans.
- Find the existing source of truth for each decision. Follow local ADR formats, numbering and status transitions. Extend an active proposal when appropriate and follow the supersession convention for accepted decisions.

## Draft and review

1. Capture the shared behavior, ownership, constraints, open choices, and how all consumers can verify the contract. Link to the product spec and work items.
2. In each repo RFC, compare viable local options and describe the proposed implementation, consequences, and acceptance checks. Link to the shared RFC and reference its contract without copying it. Keep unresolved implementation choices identified as proposals or spikes.
3. Show which decisions block implementation across repos and which can proceed independently. State the order for approving contracts, publishing them, and implementing or rolling them out. Include a compatibility check when repos release at different times.
4. When asked to open reviews, use existing review PRs where possible to preserve discussion. Link companion reviews and identify the decisions each owns. Read back files and verify PR destinations and links. Keep decisions in proposed status until approved under the project's workflow.

If a review changes a shared interface, update the source decision first and reconcile affected companion RFCs before implementation.
