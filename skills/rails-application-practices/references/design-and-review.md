# Rails design and review

Use this when a change introduces a workflow, crosses a package boundary, or makes a Rails diff hard to follow. Start with the relevant ADRs, the package's public API, and a nearby feature that demonstrates the intended style.

## Decide where behavior belongs

| Behavior | Start here |
| --- | --- |
| HTTP input, response, and status | Controller or existing request boundary |
| Association, named query, or invariant tied to one record | Owning Active Record model and database constraints where applicable |
| A decision based on several pieces of domain state | Named policy or value object with an explicit result |
| A workflow with several writes, a transaction, or an external side effect | Domain-named operation in the package that owns the outcome |
| Another package needs a decision or operation | The owning package's public API, with a declared dependency |

Keep the normal path readable from its entry point. Introduce a type when it gives a responsibility a useful name, owns an invariant, or makes a dependency explicit. For an operation that changes several records, keep transaction ownership visible and arrange external effects around the commit boundary. Keep a relation in its owning package when returning it would let the caller bypass scope or reach into private records.

For example, a provisioning action can call a Tenancy operation that owns the pending tenant and first-owner invitation transaction. The controller handles the response. A separate Authorization policy can ask Tenancy for current account and membership state through its public API and return a decision. The database models and query shape can stay within Tenancy.

## Review the changed path

1. Trace the request or job through the changed entry point, package API, persistence, and returned result. Follow names and types across each call. A reader should be able to point to where scope is established, where a denial happens, and where a write commits.
2. Inspect package dependencies and public exports. A new dependency should have a clear owner and direction. Before adding an export, identify what the caller needs and expose that behavior or data. Check whether several packages have started implementing the same business rule.
3. Read the examples as scenarios. Verify that setup declares the actor and state, that expected behavior is visible, and that failure and boundary cases exercise the real path. In a persistence change, distinguish an application validation from a guarantee enforced by the database.
4. Run the smallest meaningful spec first, then the project's relevant CI checks. Use the configured linter for style, Zeitwerk for file and constant loading, Packwerk for declared boundaries where installed, and specs for runtime invariants. Packwerk results supplement review of runtime behavior and data ownership.
5. When an agreed convention is missed repeatedly, put a working example or command in project instructions. For a rule a tool can verify reliably, prefer an existing generator, linter, test, or boundary check. Add a new enforcement mechanism only when the failure recurs and the rule is specific enough to check without regular exceptions.

## Sources and adaptation

Thoughtbot's audit skill informed the separate review passes for design, tests, and persistence. Its harness talk informed the use of deterministic feedback for rules tools can check. Rails Agent Skills informed routing to focused Rails guidance. Agent Rails informed keeping local decisions and commands close to their code. The placement table and Packwerk workflow above are this marketplace's adaptation for Rails applications with domain-owned packages.

[Thoughtbot Rails audit](https://thoughtbot.com/agent-skills) · [Harness Engineering on Rails](https://www.youtube.com/watch?v=L6-3a_rwLIg) · [Rails Agent Skills](https://github.com/igmarin/rails-agent-skills) · [Agent Rails](https://github.com/Stanislavskiy/agent-rails) · [Packwerk](https://github.com/Shopify/packwerk)
