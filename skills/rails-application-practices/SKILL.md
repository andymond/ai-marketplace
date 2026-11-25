---
name: rails-application-practices
description: Implement or review Rails application changes involving Active Record queries, migrations, authorization policy, or Packwerk boundaries using the application's established conventions.
---

# Rails application practices

Read the application's agent instructions, relevant ADRs, nearby models and specs, and CI commands. Use the Rails version, binstubs, and test runner selected by the repository.

## Model relationships and query from the owning record

- Start with Active Record associations and named scopes. Filter by ownership and record identity before loading rows. For a relationship with its own state, such as a tenant membership with a role and status, query that record by tenant and user. Use an association join when related state must be read in the same database statement.
- Prefer Active Record query methods for joins, predicates, and projections. Consider Arel when Active Record cannot express the query clearly. Use raw SQL only when a concrete database requirement warrants it and the project permits it.
- On a frequently invoked path, check the generated query and its index alignment. Use a representative query plan when performance is in question. For authorization, preserve revocation behavior and any required snapshot consistency while simplifying a query.
- Keep records and query details inside their owning pack. Use public interfaces for dependencies declared in Packwerk. Keep test setup from widening a pack's production API or bypassing its privacy checks.

## Express policy and state explicitly

- Keep an outcome separate from its reason. Preserve relevant domain state across an interface and define predicates such as `blocked?` near that state.
- Put named classes and value objects in their own Zeitwerk-compatible files. Use names and encapsulation to show what code does. Reserve comments for constraints the code cannot communicate.
- Prefer a checked-in, validated registry when fixed policy grants are easier to review as data. Reject malformed entries and deny unknown roles or capabilities. Treat request-time membership and account status as current database state. Add database-backed policy definitions only when policy needs runtime editing, with an explicit audit and cache invalidation design.

## Verify through Rails

- Use Rails generators for migrations and `bin/rails db:prepare` for ordinary database setup. Use the configured test runner against the real database for constraints, tenant scoping, and persisted policy changes. Keep reusable infrastructure setup in its own change when it falls outside the feature.
- Check both the allow and denial paths. For tenant authorization, cover a different tenant, role changes, revocation, and precedence of tenant or account blocks. Run Zeitwerk and Packwerk checks when the project uses them.

[Rails association guide](https://guides.rubyonrails.org/association_basics.html) · [Rails query guide](https://guides.rubyonrails.org/active_record_querying.html) · [Rails autoloading guide](https://guides.rubyonrails.org/autoloading_and_reloading_constants.html)
