# Domain-driven design and Packwerk

Use this when defining a package, moving business rules, or changing how packages collaborate. Start with the domain model and its consistency requirements, then use Packwerk to enforce the dependency decisions that follow.

## Model the domain

- **Ubiquitous language.** Work from the terms domain experts use. Carry those terms through requirements, methods, and examples. When two areas mean different things by the same word, name the difference and translate at their boundary. Refine the model when a real example exposes a mismatch.
- **Subdomains and bounded contexts.** Identify the core business capability and where supporting or generic capabilities suffice. A bounded context defines where a model and its terms apply. Let cohesive responsibilities determine package boundaries. A context may use multiple packages, and a package can exist for infrastructure or shared application concerns.
- **Context mapping.** For each cross-context interaction, identify who owns the data and rule, who consumes it, and where translation belongs. Use a small public operation or result with explicit inputs. Keep a provider's persistence model and external vendor vocabulary behind the boundary.
- **Entities, value objects, and aggregates.** Use identity for things that remain the same as their attributes change. Use value equality for concepts described by their attributes, such as a measured quantity. Define an aggregate around rules that must hold together on a write. Route changes through the aggregate root and use a transaction and database constraints where appropriate. A set of associated Rails models may contain more than one consistency boundary.
- **Use tactical patterns as needed.** Active Record can express domain behavior. Give a policy or domain operation its own type when that makes the rule, transaction, or collaboration easier to understand. Introduce domain events when another part of the application needs a meaningful committed fact.

For example, Recipes might own the rules for publishing a recipe version, while Tenancy owns current membership state. A recipe publisher can ask a public authorization API for a decision using tenant and user IDs. Recipes owns the publish transaction and its version invariants. Authorization can depend on Tenancy's public API without gaining direct access to its models.

## Enforce package boundaries

1. Read the project's package configuration and locked Packwerk version. Declare direct dependencies in the consuming package's `package.yml` and enable dependency checks where the project expects them. For Packwerk 3 with `packwerk-extensions`, confirm that the privacy checker is loaded before relying on `enforce_privacy`. Use the project's public path, which defaults to `app/public` for that checker.
2. Keep public APIs narrow. Export the operation or data needed by the caller. Keep Active Record models, scopes, and writable relations private by default so callers use the owner's rules. Prefer an explicit adapter at a model boundary. If two packs need to depend on each other, revisit ownership or put coordination in a caller that can depend on both.
3. Fix violations at the boundary. For a legitimate dependency on a public API, declare the edge. For private access, move work to the owning package or find an existing public operation. Treat `package_todo.yml` as a legacy baseline with a removal plan. Avoid adding exclusions, reflective lookups, or new TODO entries to get a green check.
4. Run the repository's Zeitwerk check and Packwerk `validate` and `check` through its normal entry points. If changing enforcement configuration, verify that a deliberate forbidden reference fails using the project's existing probe or a disposable checkout. Add behavioral coverage for ownership, scoping, and cross-package contracts where the change needs it. Packwerk analyzes static constant references. SQL, strings, and dynamic dispatch can still cross a boundary, so review those paths and verify runtime invariants in tests.

The DDD principles are adapted from Eric Evans. The Rails placement examples and package review workflow are marketplace guidance.

[Eric Evans on DDD](https://www.youtube.com/watch?v=lE6Hxz4yomA) · [Packwerk usage](https://github.com/Shopify/packwerk/blob/main/USAGE.md) · [Packwerk limitations](https://github.com/Shopify/packwerk#limitations) · [Packwerk privacy checker](https://github.com/rubyatscale/packwerk-extensions#privacy-checker)
