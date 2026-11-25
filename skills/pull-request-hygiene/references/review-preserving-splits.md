# Split an existing pull request without losing review context

Before implementation, match the framework and delivery artifacts to the
available guidance. A Rails workflow with a migration, operator entry point,
and an ADR may need the Rails design, accessible documentation, and PR review
skills. Include generated schema, specs, and the ADR in the first size estimate.
Recheck after a substantive review revision or a newly requested artifact.

For example, split a large onboarding change into a persistence prerequisite,
the operator workflow with its behavior specs, and documentation, if each diff
can be reviewed and verified against its intended base. Stack the workflow on
persistence and the documentation on the workflow while those dependencies are
open. Put any decision that must guide the implementation ahead of its dependent
code. Measure each diff against its actual base.

If reviewers have already commented on the original PR, leave its branch and
threads available while preparing replacement branches. Map open findings to
the replacement PRs and link back to the original discussion. Keep the original
PR as the review record if the author prefers. If the author chooses to
supersede it, close it after the replacements are linked. Retarget the next
dependent PR after its base merges and verify its diff again.

## Apply review fixes to a stack

Check the remote head and base of each affected PR before editing. Apply a
shared fix at the earliest layer that owns it, then update its descendants in
dependency order. Check each resulting remote diff and mergeability against
the current base. CI from an older head or base is evidence for that revision.

If tooling cannot update the existing branches, preserve their review threads
and publish clean follow-up branches from a verified base. Link each finding
to the branch that carries its fix, and make clear which revision reviewers
should use. Copying the same change to several branch heads can leave the
merge base stale and produce duplicate diffs or conflicts in nearby edits.

Test that intermediate slices can boot and pass their checks independently.
If a slice installs an authentication adapter before the callback is wired,
defer activation or document the dependency before anyone deploys it.
