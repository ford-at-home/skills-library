# Frozen calibration

An assertion suite that can be edited to pass is not a guarantee. Pair it with
bounds that make an accuracy *improvement* prove where it came from.

Freeze the scorecard on a fixed seed and a fixed synthetic or holdout set,
recording the values at freeze and the date in the docstring. Any change to model
math that moves them outside tolerance fails CI and forces a conscious re-freeze
with a stated reason.

```python
class TestRegressionFreeze:
    """Values at freeze (<date>): median APE 1.77%, cov50 0.45, cov80 0.77,
    signed +0.85%. Bounds are loose enough to survive RNG-stream stability
    and tight enough that a weights change trips them."""

    def test_recovers_aligned_generator(self, summary):
        assert summary.median_ape_pct < 3.0
        assert 0.30 <= summary.coverage_50 <= 0.60
        assert 0.60 <= summary.coverage_80 <= 0.90
        assert abs(summary.mean_signed_error_pct) < 2.5
```

Three rules travel with this:

1. **Never edit a contract test to make a change pass.** Fix the change. This is
   the rule that gets broken, because editing the test is always the shorter
   diff and always looks like a test-maintenance commit.
2. **Never rebalance weights or hyperparameters to fit a single calibration case
   tighter.** An honest miss on one case is evidence. A tuned hit on one case is
   nothing, and it is indistinguishable from a leak in the final report.
3. **Assert known biases stay visible.** If the model has a documented
   over-prediction under some regime, write a test asserting that regime still
   shows materially more error than the aligned one. It makes the flaw impossible
   to hide by accident, and it fails if someone "fixes" the symptom without
   understanding it.

**Scope note.** This is the transferable half of a separate change-safety
practice, folded in here because a leakage assertion that can be edited away is
not an assertion. Deliberately left out: byte-identical behavior-preserving
refactor protocols and environment-specific verification commands. Those are
general refactoring hygiene, apply to any codebase, and are not about
auditability.
