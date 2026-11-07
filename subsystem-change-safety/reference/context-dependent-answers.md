# Where subsystems disagree

These three came out differently in different subsystems, and in each case both
of the competing answers are right in context. Do not average them. Pick the one that matches the subsystem
in front of you and say in the record which you picked.

**Rollback.** For a subsystem whose state lives entirely in code, rollback is a
revert and the acceptance test is that pre-change output is reproducible
exactly. For a subsystem holding state that outlives the deploy, revert is not
available: rollback is a *new forward change*, and a landed migration is never
edited or un-applied. The deciding question is whether the subsystem holds
state that survives the code, not how large the change is.

**Whether a green suite is sufficient.** Where the whole subsystem is in-repo
and deterministic, a green suite with zero test edits is close to sufficient,
and the suite is legitimately treated as the contract. Where the subsystem has
live external state, the suite covers only the in-repo half — access-policy
behavior, concurrency, and accounting invariants need a live system — and those
are named as required manual verification rather than covered by inference from
a green in-repo run.

**What to do with an unknown input.** One discipline says a missing or
unrecognized input must raise — never a zero, an "Unknown", or an average,
because a filled gap is indistinguishable from an answer downstream. Another
says an unrecognized external status must be *held* — mapped to nothing,
retried later — and never resolved to a terminal state "to be safe", because a
premature terminal state is unrecoverable. Both refuse to guess; they differ on
whether the subsystem can safely wait. If it can, hold. If it cannot, raise.
Never fill in a plausible value in either case.
