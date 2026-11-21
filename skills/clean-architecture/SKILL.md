---
name: clean-architecture
description: Design or assess software boundaries using principles from Robert C. Martin's Clean Architecture while keeping the structure proportionate to the system.
---

# Clean architecture

Use this skill when designing or reviewing module, service, or application boundaries. It is informed by Robert C. Martin's [Clean Architecture](https://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494272); apply its dependency and policy-separation ideas without assuming every project needs the same layers.

## Start from the problem

- Inspect the existing system, deployment shape, team needs, and likely axes of change before proposing a structure.
- Identify core policies and use cases separately from delivery mechanisms and infrastructure details where that distinction helps.
- Consider testability, independent change, operational ownership, and deployment constraints alongside code organization.
- Prefer the simplest boundary that isolates a real reason for change. A small application may be clearer as a few cohesive modules than as a full set of architectural layers.

## Shape dependencies deliberately

- Keep volatile details such as frameworks, databases, user interfaces, and external services behind boundaries when that protects stable business rules or allows useful substitution.
- Make source dependencies point toward stable policy where practical. Inner policy should not depend directly on outer framework types or infrastructure-specific data formats.
- Use interfaces, ports, or adapters where they clarify ownership and control flow. Avoid creating interfaces for every class or adding indirection without a concrete boundary benefit.
- Keep data crossing a boundary explicit and owned by the receiving policy. Translate external schemas at the edge rather than allowing them to spread through the core.
- Let use cases express application-specific orchestration; keep entities or domain models focused on business rules that are genuinely shared and stable.

## Validate the architecture

- Trace a representative change through the proposed boundaries. Check whether business rules can be tested without starting infrastructure and whether an outer detail can change without rewriting policy.
- Check that dependency inversion does not create awkward abstractions, duplicated mappings, or excessive ceremony for the scale of the codebase.
- Prefer incremental boundary improvements that preserve observable behavior. Avoid large rewrites solely to make folder names or diagrams match a pattern.
- When evaluating a design, explain the forces and tradeoffs: coupling reduced, complexity added, and the cost of a simpler alternative.

## Report

Describe the relevant policies, boundaries, and dependency direction in concrete terms. Recommend only the structure needed for the problem, note where the current design is already sufficient, and state which assumptions could change the recommendation.
