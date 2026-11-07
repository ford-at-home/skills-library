# Reversibility, ordering, and behavior-preserving refactors

## Reversibility

| Tier | What it means | Process |
|---|---|---|
| **1 — Reversible in place** | Effect lives entirely in version-controlled code. Revert restores the prior behavior exactly | Baseline, change, verify, done |
| **2 — Reversible by forward fix** | Deployed code, config, or additive structure. The prior state is gone but the effect is correctable by a new change | Full process. Name the forward fix before shipping. Independent review |
| **3 — Irreversible** | Destroys data, moves money, delivers an external side effect, exposes a secret, or contracts a structure something still reads | **Plan only. A human executes.** See below |

Tier 3 examples: dropping or renaming a column, deleting rows, a backfill that
overwrites, widening an access policy, revoking one that is load-bearing,
rotating a live credential, anything that charges or refunds.

**For tier 3, this skill writes and stops.** Produce the ordered step list, the
pre-condition each step assumes, the verification command after each, and the
compensating action. Then hand it over. Do not execute a destructive migration,
a data deletion, or an infrastructure change, and do not execute them
"unattended but carefully". Read-only inspection of live systems is fine;
mutation needs explicit human permission and human hands.

**A tier 3 change can usually be decomposed into tier 2 changes.** Add the new
structure, dual-write, migrate readers, wait, and only then contract. The wait
is the point — it is what makes the contraction observable rather than
irreversible. Propose the decomposition before proposing the one-way door.

## Ordering

```text
Expand before contract.     Add the new thing, move readers, then remove
                            the old thing — in separate verified steps.
Record before effect.       Write the row that proves the effect is about to
                            happen before causing it. An effect with no
                            record cannot be reconciled.
Behavior-preserving first.  Land and verify the refactor, then the new
                            behavior that depends on it.
Guard with the structure.   Access policies, grants, and indexes ship in the
                            same change as the structure they protect, never
                            a follow-up.
Never edit a landed step.   A shipped migration is history. Fix forward.
Assume replay.              The change mechanism must survive being applied
                            twice, and applied halfway and then again.
The sweep owns correctness. Where a subsystem has a fast path and a sweep
                            that reconciles it, the fast path is an
                            optimization. Never move correctness-critical
                            logic onto it; verify the subsystem still
                            converges with the fast path disabled.
```

## Behavior-preserving refactors

The safest way to add an extension point, and the easiest place to lie to
yourself. To claim behavior is preserved:

- Keep the existing public entry point as a thin wrapper reproducing its old
  result **byte-identically**, including human-readable strings a consumer
  renders verbatim. A reworded explanation string is a breaking change to
  whoever reads it.
- Add a composition test asserting the split pieces recombine to the
  pre-refactor value, and a delegation-equality test for each extracted variant.
- Acceptance is the full suite passing with **zero edits to existing tests**.
  Any diff in an output field means the refactor is wrong, not that the test is
  stale.

## When an invariant is stated in more than one place

Some rules are written twice — once in the code that executes them, once in
prose or a fixture that a human or another agent reads. Those copies drift, and
the drift is silent because each side stays internally consistent. Find every
statement of the rule before changing any of them, change them all in the same
commit or none, and add a mechanical check that greps for the load-bearing
markers on **both** sides so a partial edit fails fast. Such a check cannot
prove the two statements are semantically identical — say so in the check's own
comment — but it catches the actual failure, which is editing one and forgetting
the other.
