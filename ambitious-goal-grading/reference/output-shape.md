# Graded output shape

```yaml
period:
reconciliation:                # pass | fail, with unaccounted goals named
goals_graded:
  - goal:
    target:                    # original
    target_revised:            # only if a mid-period change occurred
    actual:
    attainment_score:          # against the original target
    goal_setting_context:
    calibration_assessment:    # sandbagged | well_calibrated | overreach |
                               # unknowable | goalpost_moving
    surprise_evidence:
    cited_signal:              # the input field or computed value behind the flag
    rationale:                 # cite the calibration table row
    routed_out:                # optional — execution failure, needs incident review
goals_abandoned:
  - goal:
    reason:
    assessment:                # honest_drop | abandoned_to_protect_hit_rate
excluded_with_rationale:       # rationale required per goal
pattern_assessment:            # chronic_sandbagging | chronic_overreach |
                               # well_calibrated | mixed | insufficient_data
pattern_evidence:              # citations from prior_period_gradings
recalibration_recommendations:
  - goal:
    current_target:
    recommended_target:
    rationale:                 # cite the calibration assessment
    stated_difficulty_next_period:  # required
thesis_review_needed:          # bool — true when chronic_sandbagging is present
```

Two constraints on these fields:

Recalibration rationale is never an uncited percentage move such as "stretch by
10%". `insufficient_data` is used only when prior gradings are genuinely absent,
never as a hedge.
