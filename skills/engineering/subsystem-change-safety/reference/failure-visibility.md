# Loud versus silent, and how this goes wrong

## Failure visibility

| Fails loudly | Degrades silently |
|---|---|
| Raises, returns an error, fails the build | Returns a plausible wrong number |
| Suite goes red | Suite stays green because nothing asserted it |
| Request 500s | Access is wider than intended and no request fails |
| Type check rejects | A row is never written and the caller gets a null it ignores |
| Migration fails to apply | Migration applies twice and doubles something |
| | A priced operation defaults to zero cost |
| | A generated artifact drifts from its source |
| | A held resource is never released |
| | A human-readable string a consumer displays verbatim changes shape |

**"The tests passed" is evidence about the left column only.** The failure
class this skill exists for lives in the right one: the change appears to
succeed while corrupting data or quietly degrading output. For every silent
invariant, name the check that would have caught it. If none exists, write it
before the change or record it as an accepted, stated risk — never as covered.

## How this goes wrong

**The one it exists to catch.** The change lands, every check is green, and
something is quietly wrong: a priced operation now records zero, a policy is a
little wider than intended, a row is never written and the caller ignores the
null, a distribution assumption was replaced with a more familiar one. Nothing
failed because nothing asserted it. This is why the invariant enumeration comes
before the change and not after.

**Baseline attribution.** Without a recorded baseline, a pre-existing failure
gets attributed to the change and time goes into fixing something that was
already broken — or a real regression hides behind the assumption that the
failure was already there.

**Calibration drift.** Constants get nudged so one case fits better. Each nudge
is defensible and the honest number is gone. Adjustments layer at display time
and restore; they never mutate the shared constant set.

**Tier assigned by size.** An irreversible change is treated as tier 2 because
it is small. Size is not the axis; direction is. A contraction is irreversible
whether it removes one column or ten.

**The optimization becomes load-bearing.** Correctness logic migrates onto the
fast path because that was convenient. The reconciling sweep is no longer
sufficient alone, and nothing notices until the fast path is off.

**Replay.** The change mechanism is applied twice, or halfway and then again,
and doubles something.

**Self-certification.** The agent that made a tier 2 or 3 change is the only
thing that reviewed it, and its verdict reads clean while external steps it
could not reach sit undone.
