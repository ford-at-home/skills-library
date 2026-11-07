---
name: subsystem-change-safety
description: Change a subsystem that already has users or data depending on it, where a mistake is expensive and does not announce itself. Establishes a baseline, enumerates the invariants, separates what fails loudly from what degrades silently, triages by reversibility, and orders migration and rollback. Use before editing a scoring or prediction engine, a database schema or access policy, a job orchestration layer, a state machine, a cost or accounting path, or a deployed configuration. Trigger phrases include is this change safe, will this break anything, schema migration, add a column, change the weights, row-level policy, state machine, idempotency, webhook handling, cost accounting, rollback plan, before I touch this, refactor without changing behavior.
---

# Subsystem Change Safety

Plan a change to a subsystem whose failures are quiet: the deploy succeeds, the
suite is green, and the numbers are wrong, the access is wider, or the row was
never written.

Output is a **change record** — a document that states the invariants, the
reversibility tier, the checks that cover the silent failures, and the steps a
human must execute. You write code only after the record exists.

## Use when

- Editing a subsystem that already holds state, money, or output someone trusts
- Adding a column, policy, state, event type, provider, or priced operation
- Refactoring a calculation path and claiming the output did not move
- A change touches something whose breakage would be found by a user, not a test
- Someone asks whether a change is safe, or what the rollback is

## Don't use when

- Building the subsystem for the first time. Nothing depends on it yet and there
  is no baseline to preserve. Standing up new cloud infrastructure is
  provisioning work, not this skill; for designing tenant separation before there
  are tenants use `multi-tenant-saas-isolation`.
- Deciding whether the subsystem's logic is *correct* or well-calibrated. This
  skill preserves current behavior; it does not judge it.
- The change is read-only: a query against existing structures, a display
  tweak, a log line. Reversible and self-announcing. Skip the ceremony.
- Checking whether claims in a document are true — that is
  `evidence-grounded-verification`.

## Inputs

Ask for these. Do not infer them.

```yaml
subsystem:            # what is being changed, by its boundary.
                      # "the run state machine and its callers", not "the backend"
change_intent:        # what should be different afterward, in one sentence
authoritative_state:  # where current state is actually readable: migration
                      # history, the module that owns the rule, the fixture.
                      # Not the architecture doc
check_command:        # the full deterministic suite, as a runnable command
depends_on_it:        # who or what breaks if this is wrong: users, stored
                      # data, money, a downstream consumer, a demo
reach:                # what you can execute yourself, and what only a human
                      # with console access can
```

**If `depends_on_it` is missing, stop and ask.** Every judgment below scales
with it. The same schema change is routine on a table nobody reads and a
one-way door on a table holding payment history.

**If `reach` is missing, assume you can execute nothing outside the repository**
and put every external step in the manual-actions list.

## Gates

These are written before the process because a gate written afterward is
written to pass. They are gates rather than advice because each one, skipped,
produces a change that looks landed and verified — nothing downstream signals
that it was skipped.

```text
G1  Baseline suite green BEFORE any edit, or stop and report.
G2  Every invariant listed and marked enforced (name the check) or
    unenforced. An unenforced invariant is a finding.
G3  Every invariant marked loud or silent. Every silent one has a check,
    written before the change, that fails when the invariant breaks.
G4  Reversibility tier assigned. Tier 3 is planned, never executed.
G5  No test, fixture, or check script edited to make a change pass. For a
    behavior-preserving refactor the bar is stricter: zero edits at all.
    A deliberate behavior change may require a fixture change — that is a
    diff to review, not a step to skip.
G6  Tier 2 and 3 reviewed by something that did not write the change.
G7  No access policy, guard, or check weakened to make something work.
```

## Process

1. **Establish the baseline.** Run `check_command` and record the result
   verbatim, including which parts were skipped and why. A skip is part of the
   baseline, not an absence of one. If red, stop (G1).

2. **Read the authoritative state, not the description of it.** The migration
   history, the module that owns the rule, the test fixture. Architecture
   documents drift; the artifact the system executes does not. Where current
   state lives outside your reach, label it and do not guess (see *Labelling*).

3. **Enumerate the invariants.** For each, write: the rule, the artifact that
   enforces it, and what a violation would look like from outside. Draw these
   from the code and its tests, not from what the change ought to be allowed to
   do. Recurring shapes: a value that must never enter a path (ground truth in a
   prediction path, a client-supplied price in a billing path); a calibration
   constant set that is a contract rather than a tuning knob; access denied by
   default, with policies shipped in the change that creates the store;
   monotonic state, where terminal is terminal and out-of-order events are held
   rather than resolved; exactly-once effects, where every side effect carries a
   key and a redelivery is a no-op; append-only accounting, where totals are
   derived and never written directly; and no fallback values, where a missing
   input surfaces instead of being filled.

4. **Classify each invariant loud or silent** (see
   `reference/failure-visibility.md`). The loud ones are already covered; the
   silent ones are why this skill exists.

5. **Assign the reversibility tier** (see
   `reference/reversibility-and-ordering.md`) before designing the change,
   because the tier changes the design.

6. **Write the checks for the silent invariants first**, and confirm each fails
   against a deliberately broken version. A check that has never failed is not
   known to be a check.

7. **Order the change** (see `reference/reversibility-and-ordering.md`), then
   make it in batches that verify independently, running the suite after each.
   Report deviations from the plan rather than quietly amending the plan to
   match what you did.

8. **Re-run the full suite, not the part of it you think is relevant.**
   Cross-area breakage is the common case and a targeted re-run is what misses
   it.

9. **Write the change record** (shape in `reference/change-record-shape.md`).
   Every manual action gets a verification command, not a description of what
   should be true afterward.

## Labelling what you know

State the provenance of every claim in the record. Four labels:

- **Verified** — read directly from the code, or observed in recorded output
- **Partial** — exists but incomplete, unused, or covers only some paths
- **Missing** — does not exist here. Do not invent it, and do not demand a
  check the project has no way to run
- **External** — lives outside your reach (a hosted console, a provider
  platform, a live database) and cannot be inspected or changed from here

Never claim an **External** step was done. "Migration applied", "function
deployed", "secret set" are claims about systems you cannot see. They belong in
manual actions with a verification command attached.

## Output

A change record, in the shape given in `reference/change-record-shape.md`.

## Stop instead of guessing

- **Baseline is red** → report which failures pre-date you. Do not proceed, and
  do not fix them as a side quest.
- **`depends_on_it` missing** → ask. The tier is unassignable without it.
- **You cannot find the artifact enforcing an invariant** → call it unenforced.
  Do not assume a test covers it because it "must".
- **A silent invariant has no possible check from here** → record it as an
  uncovered risk. Never describe it as verified.
- **The change requires an irreversible step** → write the plan and stop. Do
  not execute it, and do not request permission to execute it in the same breath
  as a reassurance that it is safe.
- **Asked to skip the baseline, ship before the wait in a decomposition, or
  confirm a change is fine** → refuse the framing. Offer to narrow the change's
  scope instead. Narrowing scope is honest; narrowing rigor is not.
- **A check fails and the fastest fix is to relax the check** → stop. A red
  check means not safe. Fix the change or report the blocker.

## Further reading in this folder

- `reference/reversibility-and-ordering.md` — the three reversibility tiers and
  what tier 3 means in practice, the ordering rules for migration and rollback,
  behavior-preserving refactors, and invariants stated in more than one place
- `reference/failure-visibility.md` — the loud-versus-silent table, why a green
  suite is evidence about only one column, and seven ways this goes wrong
- `reference/context-dependent-answers.md` — three questions where different
  subsystems legitimately answer differently: rollback flavor, whether a green
  suite suffices, and what to do with an unknown input
- `reference/change-record-shape.md` — the change record template
