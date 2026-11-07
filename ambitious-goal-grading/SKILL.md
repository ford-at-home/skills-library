---
name: ambitious-goal-grading
description: Grade whether a period's goal targets were set at an honest difficulty, not whether they were hit — reconcile every goal the period authorized against the ones submitted, recompute any target that moved mid-period against its original, require named surprise evidence for anything hit at or above 100%, and separate a target set too high from a plan that broke. Exists because a grading submission arrives pre-filtered — only the goals that were hit, with targets already revised, and the misses quietly dropped. Use at quarter or year end, when next period's targets are being set, or when a team keeps hitting everything. Trigger phrases include sandbagged, stretch goal, goal calibration, OKR scoring, grade the goals, were our targets right, did we set the bar too low, we hit 100% of our goals.
---

# Ambitious Goal Grading

Grade the **targets**, not the attainment. One question: were these set at an
honest difficulty, regardless of whether the bet landed or the team executed?

That roughly 0.7 attainment is the healthy norm, and that a clean 1.0 suggests
the target was too low, is well-documented convention. This skill does not
restate it. It exists because the convention is unenforceable against the
submission you are actually handed, which has already been filtered:

- Only the goals that were hit are in it.
- Targets that moved mid-period appear at their revised value, and the original
  is gone.
- Goals tracking toward a miss were dropped late and are not mentioned.

Every one of those looks like a complete submission. Grade what you are given
and you will certify a sandbagged period as well calibrated.

## Use when

- Period-end grading is happening and nobody has asked whether the targets were
  honest before asking whether they were hit
- Next period's targets are being set and calibration history should inform them
- A pattern is emerging — recurring 100% hits, or recurring near-misses

## Don't use when

- You are designing the scale rather than applying it. Building levels, anchors,
  and descriptors is a different job; use `anchored-rubric-design`
- You are judging external submissions against published criteria. Use
  `defensible-submission-scoring`
- A goal missed because something broke. That is a post-incident review, and
  this skill routes those cases out rather than absorbing them as overreach
- The question is whether this period's numbers moved and why. That is a
  recurring metrics review
- The question is whether the underlying bet was right. Grading calibration
  deliberately does not touch it
- The period is not complete. There is nothing to grade. Refuse
- The team wants their hit rate celebrated. Refuse explicitly
- A single isolated goal with no prior periods, no stated difficulty intent, and
  no sibling goals. Calibration is not assessable in isolation

## Inputs

Ask for these. Do not infer them.

```yaml
period:
goal_source:                   # REQUIRED — the written document that recorded
                               # these targets and the rationale for each
authorized_goal_set:           # REQUIRED — every goal the period opened with,
                               # by name. This is the reconciliation baseline
period_goals:                  # REQUIRED
  - goal:
    target:                    # original target, numeric with units
    actual:
    goal_setting_context:      # committed | stretch | aspirational | unstated
    surprise_evidence:         # required when attainment >= 1.0
abandoned_goals:               # REQUIRED, may be []
  - goal:
    dropped_at:
    reason:
mid_period_target_changes:     # REQUIRED, may be []
  - goal:
    original_target:
    revised_target:
    justification:
prior_period_gradings:         # OPTIONAL — for chronic-pattern detection
```

**If `goal_source` is missing, stop.** Grading targets without the document that
set them means grading them against the outcome, which always exonerates.

**If `authorized_goal_set` is missing, stop.** Without it there is nothing to
reconcile against, and survival bias is undetectable by construction.

## Gates

| Gate | Pass criteria | If it fails |
|---|---|---|
| Reconciliation | `period_goals` + `abandoned_goals` + `excluded_with_rationale` accounts for every entry in `authorized_goal_set` | Do not score anything. Demand the missing goals |
| Surprise evidence | Every goal at attainment >= 1.0 carries non-empty `surprise_evidence` that is not effort language | Assess it `sandbagged` |
| Goalpost recompute | Every mid-period change is recomputed against the original target, with both numbers shown | Recompute and disclose |
| Overreach vs execution | Every attainment below 0.5 either carries `overreach` with target rationale, or is routed out as an execution failure | Route or classify |
| Difficulty intent | Every goal carries `goal_setting_context`; `unstated` is recorded as a finding | Demand stated intent for next period |
| Every flag cited | Every assessment names the input field or computed value that triggered it | Cite it or drop the flag |
| No outcome contamination | Nothing in the output argues whether the bet was right, or grades effort | Strip it |

Reconciliation runs first. Survival bias is the first failure mode, not the
last, and no assessment downstream of an unreconciled set means anything.

## What counts as surprise evidence

This is the gate that gets argued with, so it is defined narrowly. Surprise
evidence names something the team did **not** expect that changed the path: a
method that worked when it should not have, a constraint that vanished, a
customer who behaved differently than predicted.

Not surprise evidence: "it was hard but we made it", "the team worked hard", "we
executed well", "delivered as planned", "we always knew we could". Those
describe effort or confirm the plan. A stretch goal hit on plan was not a
stretch goal.

## Calibration table

```text
attainment >= 1.0  AND surprise evidence present         → well_calibrated
attainment >= 1.0  AND surprise evidence absent          → sandbagged
attainment in [0.6, 1.0)                                 → well_calibrated
attainment in [0.3, 0.6) AND an honest plan existed      → well_calibrated
attainment in [0.3, 0.6) AND no honest plan ever existed → overreach
attainment < 0.3   AND execution broke                   → route out as an
                                                           execution failure
attainment < 0.3   AND execution did not break           → overreach
goal_setting_context == unstated                         → unknowable; demand
                                                           stated intent next period
mid-period target change present and not disclosed       → goalpost_moving
                                                           (supersedes all above)
```

Attainment is `actual / target` against the **original** target, clamped to
[0.0, 1.5]. Qualitative goals map `met | partially_met | not_met` to
{1.0, 0.5, 0.0} for pattern math only.

`well_calibrated` is the normal case. The skill detects deviations from it, not
fault in every row.

## Two assessments that are not on the table

**`abandoned_to_protect_hit_rate`** — a goal dropped late in the period, with a
vague or absent reason, no substantive replacement (no new metric, no revised
plan, no concrete reallocation), and it was tracking toward a miss. Carries an
obligation that next period's plan address the dropped commitment.

**Chronic patterns** — the same recurring goal flagged `sandbagged` or
`overreach` across three or more consecutive periods, computable only with
`prior_period_gradings`. Each period individually looked defensible, which is
why this is the finding that requires cross-period data to exist at all.
Chronic sandbagging escalates to whoever owns the thesis: a team that
systematically hits easy targets has converted a falsification mechanism into a
confirmation one.

## Hard rules

Each of these prevents a failure that produces a plausible-looking grading. That
is why they are rules rather than advice — a filtered submission graded on its
own terms reads exactly like a well-calibrated period.

```text
Reconcile before scoring. An unreconciled set produces no valid assessment.
A target hit at 100% with no named surprise is presumptive sandbagging.
Effort language is never surprise evidence.
Recompute every moved target against the original. Disclose both numbers.
Grade the target. Never the effort, never the bet.
```

## Stop instead of guessing

- **No `goal_source` or no `authorized_goal_set`** → refuse. Name which is
  missing and what it is for.
- **The team supplies only the goals it hit** → refuse and name the gate. This is
  the most common failure and it arrives looking like a complete submission.
- **`abandoned_goals` is large relative to `period_goals` with no rationale** →
  do not proceed to scoring. Mark each `abandoned_to_protect_hit_rate` until
  rationale is supplied, and say that is what you have done.
- **The period is not complete** → refuse. Partial-period calibration is
  attainment reporting wearing this skill's name.
- **Asked to confirm that goal-setting was good** → refuse. Offer to establish
  whether the targets were honest.
- **Asked to grade effort, process, or whether the bet was right** → refuse, and
  say why the separation matters: a team can hit a well-calibrated target on a
  doomed bet and miss one on a winning bet. Merging them makes both unknowable.

## Further reading in this folder

- `reference/output-shape.md` — the graded-output schema field by field, plus the
  two constraints on recalibration rationale and `insufficient_data`
