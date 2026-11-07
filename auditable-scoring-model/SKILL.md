---
name: auditable-scoring-model
description: Audit a statistical prediction — a price, rating, duration, or probability fitted from historical records — so target leakage is caught by a failing assertion rather than by an implausibly good validation score. Installs an allowlist assertion over feature names, structural separation between features and ground truth, a value scan over model outputs, and frozen calibration bounds that make a later accuracy improvement prove it did not come from leakage or from refitting to one case. Concerns fitted predictions, not rubric points awarded by a judge. Use when a validation number looks too good, when adding a feature to a model already calibrated, or when someone asks whether a model could be cheating. Trigger phrases include target leakage, data leakage, train-test contamination, too good to be true accuracy, feature audit, holdout, is the model cheating, backtest, overfitting to one case, calibration drift.
---

# Auditable Scoring Model

Make target leakage a test failure instead of a suspicion.

Output is a **leakage audit** plus a committed **assertion suite**. The audit is
a document. The suite is code that fails loudly in CI when someone widens the
feature set. Neither is optional: an audit without assertions decays on the next
refactor, and assertions without an audit don't say what they are protecting.

## Use when

- Fitting or reviewing a model that predicts a numeric outcome from records that
  also contain that outcome
- A validation number is better than the problem plausibly allows
- Adding a feature, a data source, or a column to a model already calibrated
- The model's credibility is the deliverable — a demo, a proposal, a filing
- Someone asks whether the model could be reading the answer

## Don't use when

- **The thing being scored is model behavior against a rubric.** The word
  "scoring" collides here and the jobs are unrelated. If a judge assigns points
  on named dimensions and your problem is whether the dimensions are anchored and
  the judge is consistent, use `anchored-rubric-design`. If you are measuring how
  a model behaves across prompts or versions, use `llm-behavior-benchmark`. If
  you are ranking submissions against published criteria, use
  `defensible-submission-scoring`. Those three concern *rubric points*. This one
  concerns a *statistical prediction* and whether its features could have seen
  the target.
- You are checking whether stated claims are sourced rather than whether
  features are clean. That is `evidence-grounded-verification`.
- You need the model's numbers argued from several viewpoints before a decision.
  That is `multi-persona-roundtable`.
- The pipeline that *produces* the training corpus is the problem — resumability,
  cost, partial output. That is `corpus-transform`.
- Accuracy doesn't matter and nobody will act on the output. The whole apparatus
  is priced for the cost of being confidently wrong.

## Inputs

Ask for these. Don't infer them.

```yaml
target:              # the quantity predicted, AND the moment its value first
                     # becomes knowable. "accepted price, known at contract"
feature_source:      # path(s) to the data the model reads
ground_truth_source: # where target values live, and how they were obtained
holdout:             # how validation cases are separated, or "none"
calibration_claim:   # the accuracy figure this model will be presented as
                     # achieving, and to whom
known_limits:        # weaknesses already understood, or "none stated"
```

**If `target` has no "becomes knowable when", stop and ask.** Leakage is defined
by time, not by field name. A feature is leaky if its value could only be known
after the target was known. Without the timestamp you are guessing at which
columns to forbid, and guessing at the list is exactly the failure mode this
skill inverts.

**If `calibration_claim` is missing, ask what number will be quoted.** Frozen
bounds have to be frozen around something.

## Gates

Written before the process because a gate written after is written to pass.

- [ ] The target's knowable-at moment is written down
- [ ] Features and ground truth are reachable only through separate functions
- [ ] The allowlist assertion exists and currently passes
- [ ] The value scan runs against model *output*, not only against inputs
- [ ] A holdout exists, or its absence is stated in the audit as a limit
- [ ] Calibration bounds are frozen with the date and the values at freeze

## Process

1. **Write the target's knowable-at moment.** One line. Every later judgment
   depends on it.

2. **Classify every field the model can reach** into: knowable before the target,
   knowable only after, and derived-from-something-knowable-only-after. The third
   class is where leakage actually lives — a ratio, a rank, a bucket, a flag
   computed from the outcome.

3. **Separate structurally, not by discipline.** Two types, two loader
   functions. The feature loader parses a different section of the source and
   constructs a type that has no field for the target. The scoring path imports
   only the feature loader. Discipline is a comment; a type with no such field
   is a mechanism.

4. **Install all six rungs of the assertion ladder** — structural separation,
   constructor rejection, denylist, allowlist over field names, value scan over
   outputs, fixture integrity. Each catches a class the one above it misses; the
   code and the reasoning are in `reference/assertion-ladder.md`. Run it. If a
   rung is already failing, that is the finding — report it before writing any
   model code.

5. **Fit or review the model,** then ask what the validation number would be if a
   leaky feature existed, and whether you could tell the two cases apart. If you
   could not, the number is not evidence yet.

6. **Freeze calibration bounds** with the date, the values at freeze, and a
   tolerance loose enough to survive a seed or library change but tight enough
   that a weight change trips it. See `reference/frozen-calibration.md`.

7. **Write down the known limits and their causes,** including limits that make
   the model look worse. Add a test asserting each known bias remains
   *detectable*, so a later change cannot quietly hide it.

8. **Report the audit,** listing what you could not verify.

## Hard rules

Each of these prevents a failure that produces a plausible-looking model and a
plausible-looking validation figure. That is why they are rules rather than
advice — nothing downstream signals that one was violated.

```text
Leakage is defined by time, not by field name.
The allowlist assertion uses ==, never a subset test.
Features and ground truth are reachable only through separate functions.
Never edit a contract test to make a change pass.
Never fabricate a missing input. No zero-defaults, no "Unknown", no
  population averages standing in for a value the record does not have.
Never rebalance constants to fit one calibration case tighter.
Never hand-edit a generated report. Fix the generator and regenerate.
A cached derived column is re-derived on load.
A validation number without a stated holdout is not a validation number.
Describe the code path that actually runs. A dormant scaffold is not a method.
```

The allowlist rule is the one that carries the skill. `==` is what makes the
assertion catch names nobody anticipated; a subset test degrades it back into a
denylist with extra steps.

The fabrication rule is the leakage-adjacent twin: a fabricated default is not
leakage, but it biases the prediction in a direction nobody chose and it is
invisible in exactly the same way.

## Stop instead of guessing

- **`target` has no knowable-at moment** → stop and ask. Do not infer it from
  field names.
- **No holdout and none possible** → do not invent one. State it as a limit, and
  refuse to present the in-sample figure as validation. Report it as a fit
  statistic with that label.
- **A rung is already failing when you arrive** → stop and report before writing
  model code. The finding is more valuable than the model.
- **A validation figure is implausibly good and you cannot find the leak** →
  report `cannot determine`. Never conclude clean because your search found
  nothing; rungs 1–4 all reason about names and a derived feature has whatever
  name someone gave it. Name the searches you ran.
- **The source data lacks a field the model needs** → surface the gap. Do not
  fill it with zeros, a population mean, or a synthetic value chosen to improve
  coverage. Fabricating an input to make a backtest look better produces a
  number that is worse than having none, because it looks like evidence.
- **Asked to confirm the model is clean, or to get the accuracy number up before
  a deadline** → refuse the framing. An audit run to reach a predetermined
  verdict is worth nothing. Offer to audit the top-N features by influence
  instead, which limits scope honestly rather than limiting rigor.
- **Asked to loosen frozen bounds so a change passes** → stop. A re-freeze is a
  decision with a reason and a date, not a tolerance adjustment.

## Further reading in this folder

- `reference/assertion-ladder.md` — all six rungs with their assertions in code,
  why the allowlist inversion is stronger than the denylist, and why a cached
  derived column is re-derived rather than trusted
- `reference/frozen-calibration.md` — freezing the scorecard, the three rules
  that travel with it, and what this section deliberately leaves out
- `reference/audit-report-shape.md` — the leakage audit's sections, including the
  field classification and ladder tables
- `reference/failure-modes.md` — seven ways leakage survives an audit, with the
  `==`-becomes-`issubset` variant that keeps the test green
