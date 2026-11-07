# How an auditable scoring model goes wrong

**The one it exists to catch.** Someone adds a column to the input schema. The
denylist doesn't name it, because the denylist names the fields that were
obviously leaky when it was written. Every test passes. The validation figure
improves, which reads as progress. The allowlist assertion is the difference
between finding this on the commit that caused it and finding it when a reviewer
asks how the model got so good.

**Leakage through a derived feature.** No forbidden field is present. A ratio,
percentile, rank, or bucket computed from the outcome is, and its name gives no
hint. Rungs 1–4 cannot see it; the value scan and the knowable-at classification
can.

**Editing the test.** A change breaks a contract test, the test is adjusted, the
commit message says "update test for new schema". This is the most common way a
leakage guarantee dies, and it always arrives as maintenance. The specific
variant to watch for is `==` becoming `issubset` or `<=` because a legitimate new
field tripped rung 4: the test still passes, still looks like a leakage guard,
and no longer is one.

**Overfitting one case and calling it calibration.** Constants are nudged until
the one validated case lands inside the band and the reported miss shrinks.
Nothing was learned, and to anyone reading the summary the result is
indistinguishable from leakage.

**The honest weakness fixed by fabrication.** A backtest looks poor because the
source data lacks a field the model needs, so every synthetic case collapses into
one regime. The tempting fix is to populate the field with plausible values. That
converts a documented limitation into an undocumented falsehood, and the
corrected backtest becomes the most confident wrong number in the report.

**Vintage drift on the freeze.** Bounds frozen a year ago still pass because the
tolerance is wide, while calibration moved steadily inside it. Put the freeze date
in the docstring and re-examine on a schedule, not on failure.

**Documented capability that does not exist.** A dormant scaffold gets described
as the active engine, usually in a README rather than in code. Verify which code
path actually runs before repeating any claim about the model's method.
