---
name: portfolio-reallocation-review
description: Review the allocation of capacity across every initiative a team runs at once by constructing the portfolio you would authorize from scratch today — same total capacity, same option set — before looking at the one you actually have, and treating the gap as the finding. Refuses to run if the hypothetical was built with the current allocation in view, if any initiative lacks a dated forward-looking case, or if a no-change outcome is not justified item by item. Exists to catch the portfolio that is the residue of accumulated past decisions rather than one anyone would choose today, which no per-initiative review can detect because each initiative returns a defensible answer. For three or more initiatives at once. Trigger phrases include portfolio review, bet allocation, what should we stop doing, are we spread too thin, nothing ever gets killed, planning cycle allocation.
---

# Portfolio Reallocation Review

Ask whether the allocation across all current initiatives is coherent given what
you know now — not whether each one can be defended on its own.

"Would we fund this today if we were starting fresh?" is a well-known question.
What this enforces is the part that makes it work: the hypothetical is built
**blind**, before the actual allocation is consulted, and a review that skipped
that ordering is rejected rather than caveated. Asking the inversion question with
the current numbers on screen produces a hypothetical that resembles what already
exists, and drift becomes invisible.

Output is a **reallocation review**: a per-initiative decision, a decision on every
unfunded candidate, and an explicit drift report. Every initiative in a drifted
portfolio was individually justified at some point. That is exactly why
per-initiative review cannot detect the problem.

## Use when

- A planning cycle is closing and allocation is up for review
- The team runs three or more initiatives and has a backlog of unfunded candidates
- A specific candidate is being considered and the question is what it displaces
- Nothing has been stopped in six months and the total keeps rising
- Everyone can defend every initiative individually and the whole still feels wrong

## Don't use when

- There is one initiative. Cross-initiative allocation has no meaning at N=1, and
  the question is whether that initiative's premise still holds — a thesis review
- You need to know whether one initiative's premise holds. Run that first; this
  consumes its output as the initiative's current case
- The question is *how* to execute a reallocation you have already decided on.
  That is designing an operating change
- A specific irreversible consequence is queued — a termination, a public
  announcement, releasing staff. Gate that action before it fires
- You are ranking submissions to an open call against each other. Different job
- The caller wants confirmation the current allocation is healthy

## Inputs

Ask for these. Don't infer them.

```yaml
review_period:        # quarter | half | year | other, named
total_capacity:       # integer, in one comparable unit
capacity_unit:        # what the integer means — people-quarters, dollars, FTE

initiatives:          # every currently funded initiative
  - id:
    name:
    period_allocation:     # capacity consumed this period
    cumulative_allocation: # capacity consumed since it started
    age_in_periods:
    current_case:          # REQUIRED. A documented, dated, forward-looking case
                           # that this is still worth doing, from this period or
                           # the last
    latest_goal_assessment:
    cumulative_variance:   # signed aggregate variance from recurring reviews
    materialized_risks:    # risks from the authorizing document that happened
    originator:            # who proposed it, and their seniority relative to
                           # the reviewer. Used only for the masked ranking

candidates:           # unfunded initiatives in the backlog
  - id:
    name:
    documented_case:
    estimated_need:        # in capacity_unit
    why_not_funded:        # the honest reason. "No capacity" is a claim this
                           # review tests
    expected_return:       # the case for funding now, cited

context:
  market_shifts:           # external change since the last review
  organizational_shifts:   # capacity changes, priority changes
  prior_stop_decisions:    # what was stopped before, so it is not quietly refunded
prior_review:              # the last reallocation review, if one exists
```

**If `total_capacity` is qualitative — "we have some capacity" — stop.** Without a
defined budget every comparison is a preference and the zero-based check has nothing
to allocate.

**If any initiative's `current_case` is missing or older than two periods, stop.**
Get one, or wind it down; those are the two options. Carrying it on the strength of
the case that funded it two years ago is the failure this review exists to detect.

## Gates

| Gate | Passes when | If it fails |
|---|---|---|
| Current case per initiative | Every initiative has a dated case from this period or the last | Get the missing ones first. Do not proceed |
| Zero-based built blind | The hypothetical was generated before the actual allocation was consulted | Re-do it. This is the mechanism, not a preference |
| Allocations reconcile | Allocations sum to within 5% of total capacity | Reconcile. Unallocated capacity is itself a decision; name it |
| Candidates documented | Every candidate has a documented case | An undocumented candidate cannot be honestly compared against a funded one |
| Status quo justified | If nothing changes, the zero-based check passed item by item and the justification names each initiative | A no-change review with no passing item-by-item check is theater |
| Stop candidate exists | At least one wind-down or pivot, **or** a documented argument that the whole portfolio survives zero-based authoring | A review producing neither is the canonical instance of drift. Reject it |
| Every candidate decided | Every candidate gets fund, park, or reject. "No decision" is unavailable | Force a decision |
| Stops considered | The list of initiatives considered for wind-down is non-empty even when none is recommended | Populate it |

## Process

1. **Collect inputs.** If any initiative lacks a current case, stop here.

2. **Build the zero-based portfolio without looking at the actual allocation.**
   Given the full option set — funded initiatives and candidates together — and
   `total_capacity`, what would you authorize starting today? Rank using the current
   cases, goal assessments, materialized risks, and expected returns.

3. **Run the ranking a second time with origins masked.** Strip who proposed each
   initiative and how senior they are. An initiative that holds its allocation in
   the open ranking but not the masked one is the finding.

4. **Diff the actual against the zero-based.** For every gap, name the reason.
   "Sunk cost" and "nobody wants to make the call" are legitimate answers and must
   be written down as such — they are the substance of the finding, not an
   embarrassment to be paraphrased.

5. **Match the gaps against the drift patterns** in `reference/drift-patterns.md`,
   attaching the citation: which initiative, and which evidence.

6. **Decide each initiative:** continue, wind down, amplify, hold, or pivot. Each
   needs a new allocation and cited triggering evidence. What each decision commits
   to is in `reference/decisions-and-review-shape.md`.

7. **Decide each candidate:** fund, park, or reject. A `fund` decision names what it
   draws from — including when the answer is unallocated capacity, in which case name
   the initiative that did not get it.

8. **Write the narrative.** Three to five sentences that surface the stops and the
   amplifications rather than the totals.

9. **Run the integrity check.** If nothing changed, compare actual against
   zero-based item by item and certify they match. If they don't, the recommendation
   has to change.

## Hard rules

Each of these prevents a failure that produces a plausible-looking review. That is
why they are rules rather than advice — nothing downstream signals that one was
violated.

```text
The zero-based portfolio is built before the actual allocation is consulted.
"Continue at current allocation" carries the same evidentiary burden as "wind down"
  or "amplify". Status-quo defense is not free.
A review that changes nothing must pass a zero-based check item by item.
An initiative with a stale case cannot be carried. Refresh it or stop it.
A candidate cannot be parked indefinitely. Carrying it forever is drift.
Name the reason for every gap, including the socially awkward ones.
```

These exist because reallocation reviews fail in three predictable ways: anchoring
on the status quo, so the hypothetical is built to resemble what exists; the social
cost of stopping things, so nobody proposes it; and quiet parking, so the backlog
grows while the portfolio never moves. Each rule forces one of them to the surface.

## Stop instead of guessing

- **Any initiative's current case is missing or older than two periods** → stop.
  Refresh it, or wind the initiative down. A review on stale premises inherits
  whatever the old case assumed.
- **`total_capacity` is undefined or qualitative** → stop and ask.
- **The candidate list is empty** → proceed, but say plainly that this is a
  stop-review rather than a reallocation review. With nothing to fund, the
  opportunity-cost comparison has no external reference and the check can only
  shrink the portfolio, never redirect it.
- **The team restructured mid-period so allocations are not comparable** → surface
  it and ask whether to proceed with caveats or defer. Do not silently compare
  incomparable numbers.
- **Asked to validate that the current allocation is right** → refuse, and offer the
  zero-based check instead.
- **The zero-based portfolio comes out identical to the actual one** → possible, and
  a real finding, but check first that it was genuinely built blind. An identical
  result is far more often anchoring than coincidence.

## Further reading in this folder

- `reference/drift-patterns.md` — seven ways a portfolio drifts, what each looks
  like, and the check that exposes it
- `reference/decisions-and-review-shape.md` — what each initiative, candidate, and
  severity decision commits to, and the review template
- `reference/failure-modes.md` — the portfolio drift this exists to catch, and how
  the zero-based check itself fails
