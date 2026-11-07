---
name: dissent-before-commit
description: Gate one already-authorized action that is now scheduled to fire, by re-checking every objection raised at authoring time against what has changed since, then forcing the single strongest current case to be addressed by a change to the action or accepted with a named tradeoff a named person owns. For irreversible actions an accepted tradeoff is not sufficient and the recommendation becomes pause. Catches a team pointing at an old dissent discussion as proof concerns were heard when nobody has rechecked it against current state. Use when a migration cut-over, deprecation, launch, contract termination, staff release, or data deletion is queued and was approved weeks or months ago. Trigger phrases include before we cut over, one-way door, is this still the right call, any last objections, pre-commit review, point of no return, we already discussed the risks.
---

# Dissent Before Commit

Surface the strongest case against firing *this* action *right now*, force it to be
addressed or accepted, and get to commitment.

Eliciting objections, recording who dissented, and treating irreversible decisions
more carefully are all things you can already do. This gates the part that is
routinely skipped: an objection raised when the action was approved is stale, and
the record of it looks identical whether or not anyone rechecked it.

The question is deliberately narrow:

> What is the strongest case against firing this action right now?

Not what the risks are. Not who has concerns. The strongest single case, ranked
above the others, checked against what is true today rather than what was true
when someone approved this.

Output is a **pre-commit record** ending in proceed, proceed with changes, pause,
or escalate. It attaches to the action's audit trail, because the point of
recording an accepted tradeoff is that someone can find it when the tradeoff
materializes.

## Use when

- A migration cut-over, deprecation, or schema change is scheduled
- An irreversible operational action is about to execute — contract termination,
  public announcement, hire or fire, data deletion
- The action was authorized more than a month ago and material things have changed
- Someone said "are we sure?" and the meeting moved on

## Don't use when

- The proposal is still being authored. This gates execution, not drafting
- The action has already executed. Nothing left to gate; run a retrospective
- The action is fully reversible and the stakes are small. The overhead exceeds
  the value
- You want broad risk coverage on a launch. This produces one ranked objection and
  a commitment decision
- You want objections from viewpoints nobody in the room holds, on something still
  under discussion. That is a deliberation exercise; this needs perspectives with a
  real stake in a dated action
- The premise of the whole initiative may be wrong rather than the timing of this
  action. That is a thesis question, not a commit gate
- Someone wants to overturn a readiness gate that returned no-go. That gate is its
  own decision and this is not an appeal route
- The caller wants confirmation the action is fine. Refuse

## Inputs

Ask for these. Don't infer them.

```yaml
proposed_action:            # REQUIRED. This instance, not the class. "The v1.2
                            # to v2 cut-over Tuesday 14:00 UTC", never "the
                            # migration"
authorizing_artifact:       # REQUIRED. What authorized this action
authoring_date:             # when it was approved
proposed_execution_date:    # when it fires
irreversibility_assessment: # REQUIRED. What is recoverable, what is not, and the
                            # time and cost of reversing
state_changes_since_authoring: # REQUIRED, may be empty — but empty must be a
                            # positive assertion with a named scope, never a
                            # blank field
prior_dissent:              # objections already raised upstream
perspectives_canvassed:     # which stakeholders have been consulted for this
                            # action. At least three for anything non-trivial
```

**If `irreversibility_assessment` is missing, stop and ask.** It is the first move
and it sets the bar for everything after it.

**If `state_changes_since_authoring` is blank rather than asserted empty, stop and
ask.** "Nobody filled it in" and "nothing material has changed in the following
scope" are different claims and only one can be relied on.

## Gates

| Gate | Passes when | If it fails |
|---|---|---|
| Action is specific | One instance, with a date | Reject and demand specificity |
| Reversibility assessed | Recoverable versus not, with time and cost | Reject. This gate comes first |
| State changes documented | Non-empty, or a positive assertion with a named scope | Demand one or the other |
| Stale-dissent check | If prior dissent exists and state has changed, every prior item carries a still-applies assessment | Re-canvass against current state |
| Strongest case named | Exactly one argument, ranked above the rest | Force the ranking. Co-equal cases are a hedge |
| Perspective is named | A specific function, role, or stakeholder | Reject "the team", "people", "some folks" |
| Addressed or accepted | `proceed` requires a cited change to the action, or a named tradeoff with a named owner | Force proceed-with-changes, pause, or escalate |
| One-way-door bar | For one-way doors, `proceed` requires the case addressed, not merely accepted | Pause or escalate |
| Coverage | At least three perspectives for a non-trivial action, chosen by stake | Canvass more |

## Process

1. **Pin the action.** "The migration" is not reviewable. "The v1.2 to v2 cut-over
   Tuesday at 14:00 UTC, with the read-replica promotion" is.

2. **Classify reversibility**, before hearing any objection. The three classes and
   the bar each one sets are in `reference/reversibility-and-bars.md`.

3. **Re-canvass prior dissent against current state.** Mark each prior objection
   `still applies`, `no longer applies`, or `new`. Items marked `new` are
   objections the state changes created and nobody has heard yet. These are the
   highest-value findings in the review and the ones a review that reuses the old
   dissent record will never find.

4. **Canvass perspectives by stake** — whoever owns the mechanism, runs it
   afterwards, receives the customer consequence, owns the regulatory or cost
   envelope. Three minimum, chosen because they have a stake in *this* action, not
   worked through as a checklist. Mechanically canvassing a fixed roster on every
   action produces uniform records and teaches everyone the review is a formality.

5. **Check for rubber-stamping.** A perspective that returns "no concerns" about an
   action squarely inside its stake, with no supporting artifact — no runbook for
   the new failure mode, no support brief on a customer-visible change, no review
   record on a change to data handling — was not consulted. Treat it as a finding.

6. **Force-rank to one strongest case.** Rank by: does it point at a cost you
   cannot undo, how likely is it to materialize, and how late would you find out it
   was right. Lowest reversibility, highest likelihood, lowest detectability wins.
   Asking for all dissent produces a list nobody has to act on.

7. **Name the perspective it comes from.** The stake is what makes the objection
   load-bearing.

8. **Determine addressed or accepted.**
   - **Addressed** — the action was modified. Cite the change.
   - **Accepted** — the objection stands, the action fires, and a named person owns
     the named tradeoff publicly.
   - "Heard and considered" is neither, and fails the gate.

## Recommendation logic

```text
strongest case addressed in the action                    → proceed
accepted with a named tradeoff, two-way door              → proceed
accepted with a named tradeoff, one-way door              → pause
neither addressed nor accepted                            → proceed_with_changes
                                                            (the changes are the addressing)
requires information the team does not have               → pause until it exists
the case is that the initiative's premise is wrong        → escalate to a thesis review
decision authority sits above this review                → escalate
```

## Hard rules

Each of these prevents a failure that produces a plausible-looking record. That is
why they are rules rather than advice — nothing downstream signals that one was
violated.

```text
"Heard and considered" is not addressing dissent. Acknowledgement is free;
  addressing costs a change to the action, a publicly owned tradeoff, or a delay.
For proceed, exactly one is true: the case was addressed by a documented change,
  or accepted with a named tradeoff and a named owner.
For one-way doors, the second is not sufficient. Address it or pause.
Reversibility is classified before any objection is heard.
Prior dissent is stale until re-checked against current state.
```

## Stop instead of guessing

- **`proposed_action` is a class** → refuse and ask which one.
- **No authorizing artifact** → stop. There is no contract to dissent against, and
  the review would invent the terms it then checks.
- **`irreversibility_assessment` missing** → stop. First move, not a backfill.
- **The action has already executed** → stop. Route to a retrospective.
- **Asked to confirm the action is fine** → refuse, and offer the strongest case
  against it. This is the request the skill exists to decline.
- **Asked for a general risk review** → refuse and say what this produces instead.
- **Asked to override a readiness gate that returned no-go** → refuse.
- **No perspective raises any concern and the action is material** → a finding, not
  a pass. Check the rubber-stamp signals in step 5.

## Further reading in this folder

- `reference/reversibility-and-bars.md` — the three reversibility classes, the bar
  each sets for proceeding, and why the accept path is removed for one-way doors
- `reference/record-shape.md` — what each recommendation commits the team to, and
  the pre-commit record template
- `reference/failure-modes.md` — seven ways this fails while the record looks
  complete, starting with the stale-dissent reuse it exists to catch
