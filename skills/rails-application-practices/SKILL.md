---
name: rails-application-practices
description: Implement or review Rails application changes involving domain placement, Active Record queries, migrations, authorization policy, RSpec setup, or Packwerk boundaries using the application's established conventions.
---

# Rails application practices

Read the application's agent instructions, relevant ADRs, nearby models and specs, and CI commands. Use the Rails version, binstubs, and test runner selected by the repository.

For a new workflow, a change across packs, or a readability review, use [Rails design and review](references/design-and-review.md) to decide where behavior belongs and trace the changed path before handoff.

When designing a bounded context, choosing a package API, or changing enforcement, use [Domain-driven design and Packwerk](references/domain-boundaries.md).

## Model relationships and query from the owning record

- Start with Active Record associations and named scopes. Filter by ownership and record identity before loading rows. For a relationship with its own state, such as a tenant membership with a role and status, query that record by tenant and user. Use an association join when related state must be read in the same database statement.
- Prefer Active Record query methods for joins, predicates, and projections. Consider Arel when Active Record cannot express the query clearly. Use raw SQL only when a concrete database requirement warrants it and the project permits it.
- On a frequently invoked path, check the generated query and its index alignment. Use a representative query plan when performance is in question. For authorization, preserve revocation behavior and any required snapshot consistency while simplifying a query.
- Keep records and query details inside their owning pack. Use public interfaces for dependencies declared in Packwerk. Keep test setup from widening a pack's production API or bypassing its privacy checks.

## Express policy and state explicitly

- Keep an outcome separate from its reason. Preserve relevant domain state across an interface and define predicates such as `blocked?` near that state.
- Put named classes and value objects in their own Zeitwerk-compatible files. Use names and encapsulation to show what code does. Reserve comments for constraints the code cannot communicate.
- When fixed policy is easier to review as a checked-in registry, load it through a Rails initializer using a `Rails.root` path. Validate it at boot and store the normalized, frozen data in application configuration. Keep the initializer independent of reloadable policy classes. Deny unknown roles and capabilities, and read changing membership and block state from the database. Consider database-backed grants when runtime editing warrants an audit and cache invalidation design.

## Verify through Rails

- Use Rails generators for migrations and `bin/rails db:prepare` for ordinary database setup. Use the configured test runner against the real database for constraints, tenant scoping, and persisted policy changes. Keep reusable infrastructure setup in its own change when it falls outside the feature.
- Check both the allow and denial paths. For tenant authorization, cover a different tenant, role changes, revocation, and precedence of tenant or account blocks. Run Zeitwerk and Packwerk checks when the project uses them.

## Keep RSpec setup readable

- Declare scenario data in the closest `context`. Use lazy `let` when the example or subject references the object. Use `let!` when a persisted row must exist before the code under test queries for it. Keep state transitions being tested visible in the example.
- Use FactoryBot factories for the existing models. When the project adopts short factory calls, include `FactoryBot::Syntax::Methods` in shared RSpec configuration and use `create(:factory)` in examples.
- Load `rails_helper` from `.rspec` when the suite expects Rails on every run. Keep explicit requires for Rails specs when the repository also supports fast specs that run without booting Rails.
- Prefer RSpec Rails transactional fixtures for database changes covered by per-example rollback, including records created by factories. Verify isolation before adding Database Cleaner or another cleanup strategy. When an example needs committed data visible to a separate process or an independent connection, choose targeted cleanup for that group and verify the actual visibility and cleanup behavior.

[FactoryBot RSpec setup](https://github.com/thoughtbot/factory_bot/blob/main/GETTING_STARTED.md#rspec) · [Rails test transactions](https://guides.rubyonrails.org/testing.html#transactions)

[Rails association guide](https://guides.rubyonrails.org/association_basics.html) · [Rails query guide](https://guides.rubyonrails.org/active_record_querying.html) · [Rails autoloading guide](https://guides.rubyonrails.org/autoloading_and_reloading_constants.html)
