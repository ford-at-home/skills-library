---
name: defensible-submission-scoring
description: Score human submissions to a themed call so the result survives a losing team asking why. Reads the problem statement before the submission, runs disqualifying checks before any scoring, scores desirability and survivability on two separate rubrics it carries, and refuses to collapse them into one ranking number because the useful finding lives in the gap between them. For human entries, not model output. Use when judging a hackathon, an innovation competition, a grant round, an internal proposal review, or when aggregating multiple judges' scores into a defensible total. Trigger phrases include judge the submissions, score the demos, apply the rubric, weighted totals, pick the winner, rank the proposals, why did we lose, tie-break, judging tracker.
---

# Defensible Submission Scoring

Score each submission against the problem it was supposed to solve, on two
rubrics that answer different questions, and report where they disagree.

Output is a **scorecard set** — one scorecard per submission, plus a divergence
list. You never produce a single overall ranking number. Two numbers that
disagree are the finding; one number that averages them is the loss of it.

The scoring bands for both rubrics are in `rubrics.md` in this folder. Read it
before scoring anything.

## Use when

- Judging submissions to a themed call, with awards or funding attached
- Aggregating several judges' scores into a total someone will publish
- A team asks why they lost and you need the answer on paper
- Deciding which of many prototypes is worth investing in after the event

## Don't use when

- Statements aren't written yet. Scoring depends on having something to score
  against; produce the statements first.
- You want feedback for builders rather than a defensible verdict. Feedback is
  cheaper and doesn't need the aggregation discipline.
- You're stress-testing one idea from several viewpoints. That's deliberation,
  and it runs on one proposal, not a field. Use `multi-persona-roundtable`.
- What is being scored is model output rather than human submissions. Build the
  rubric with `anchored-rubric-design` and run it with `llm-behavior-benchmark`.
- The question is whether a submission's claims are *true* rather than whether
  the work is good. Use `evidence-grounded-verification`.
- Nothing is at stake. This is expensive and its value scales with how badly
  someone wants to contest the result.

## Inputs

Ask for these. Don't infer them.

```yaml
submissions:          # path or list. What each team actually submitted
problem_statements:   # the statements submissions were built against.
                      # THE SOURCE OF TRUTH for every alignment judgment
awards:               # award name -> per-category weight. Published before build
judges:               # named, and which submissions each one scores
closed_systems:       # named platforms in this environment with no usable API or
                      # export, which structurally block integration. Or "none known"
cached_totals:        # any pre-computed totals to validate against, or "none"
```

**If `problem_statements` is missing, stop and ask.** Without them you are
scoring craft, which is a different and much weaker claim. A submission cannot be
misaligned with a statement that does not exist.

**If `awards` weights are missing, stop.** Weights decided after submissions
close are indefensible on their face, and you will be asked when they were set.

**If `closed_systems` is "none known",** you can still score desirability.
Survivability's integration dimension becomes unresolved — record it as
unresolved. Do not score it 5 because nothing is known to block it.

**If a judge's scores are missing,** the cell is null. Not the mean of the other
judges, not a substituted value. See the aggregation rules.

## Gates

Run these before any scoring. A submission that trips one is not dead — it is
classified, and the flag tells you what must be fixed before it can compete.

| Flag | Condition |
|---|---|
| `MISALIGNED` | Solves something other than the stated problem |
| `SYNTHETIC_DATA` | Depends on mock, placeholder, or hand-entered data with no named real acquisition path |
| `NO_DATA_OWNER` | Names a data source but not who controls it or how access is obtained |
| `NO_PRIOR_ART_SCAN` | No evidence the team checked what already exists |
| `NO_IMPLEMENTATION_PATH` | No believable route from current state to a pilot |
| `UNVERIFIED_FEASIBILITY` | Turns on an operational claim no practitioner has confirmed |

A flagged submission is scored and reported *with* its flag. Flags are not
deductions applied twice — do not also lower category scores for the same
reason, or the penalty compounds invisibly.

## Process

1. **Read the problem statement first and write down what it requires** — user,
   operating environment, constraints, success condition — before opening the
   submission. This ordering is the whole method. Read the demo first and your
   alignment score becomes a rationalization of an impression you already formed.

2. **Run the six gates.** Record flags.

3. **Score desirability**: six categories, 1–5, per the bands in `rubrics.md`.
   One sentence of evidence per category, citing what in the submission supports
   it. A score with no sentence is not defensible and will be the one you're
   asked about.

4. **Apply the award weights.** Weighted total is arithmetic:
   `Σ (category score × category weight)`. Compute it; never estimate it.

5. **Score survivability**: five dimensions, 1–5, per `rubrics.md`. Sum to a
   tier. Survivability asks whether it can ship, which is orthogonal to whether
   it should — a superb idea can be structurally blocked.

6. **Report divergence explicitly.** Any submission in the top desirability
   quartile and the bottom two survivability tiers, or the reverse, goes on the
   divergence list with the reason. This list is the most useful thing the
   exercise produces and it is invisible in any combined number.

7. **Aggregate across judges.** Mean per category per submission. Recompute every
   weighted total from the raw scores and compare against `cached_totals`. On any
   mismatch, stop and report the discrepancy — do not adopt either figure.

8. **Break ties by the declared sequence** in `rubrics.md`, or the sequence
   published with the awards. Never invent one at the table.

## Aggregation integrity

These come from a real extraction where a spreadsheet's cached totals and its
own raw cells disagreed:

- **Recompute, then compare.** Every weighted total is derived from raw
  per-judge scores. A cached total is a claim to check, not an input to trust.
- **Fail loudly on mismatch.** A cached-total disagreement means the source has
  an arithmetic error. Investigate it. Do not silence the check or pick the
  figure you prefer.
- **Missing means null.** A submission with no second evaluation renders as
  human-only. It does not get an imputed value, and downstream consumers must
  handle the null rather than have it filled for them.
- **Generated tables are not editable.** If an aggregate is wrong, fix the raw
  scores or the computation. Hand-editing the output destroys the only audit
  trail you have.

## Hard rules

Each of these prevents a failure that produces a plausible-looking scorecard.
That is why they are rules rather than advice — nothing downstream signals that
one was violated.

```text
The problem statement is the source of truth at all times.
Work backwards from the statement. Never forward from what was built.
Any submission depending on synthetic, mock, or hand-entered data without a
  named real acquisition path is incomplete, whatever the demo looked like.
Never combine desirability and survivability into a single ranking number.
Weighted totals are computed, never estimated. Recompute and compare.
A missing score is null. Never imputed, never averaged in.
Never change weights after submissions close.
Never apply the same defect as both a flag and a category deduction.
```

The first two rules are why this exists. Everything else is bookkeeping around
them.

## Stop instead of guessing

- **No problem statements** → stop. Offer a craft review with no award attached,
  and say plainly that it cannot support a defensible verdict.
- **Rubric was never published to participants** → refuse to award on it. Offer
  a descriptive review, and fix the publication timing next cycle. Scoring people
  against criteria they could not see is the complaint you will not survive.
- **Weights arrived after submissions closed** → refuse. Say when they were set.
- **A tie with no declared sequence** → stop and ask. Do not resolve it on the
  category that happens to separate them.
- **A judge's scores are missing** → report the gap. Never fill it, including by
  averaging the other judges. A filled cell is indistinguishable from a real one.
- **Cached and recomputed totals disagree** → stop, report both, investigate.
- **Asked for one number, one ranking, or a single winner list across rubrics**
  → refuse the framing. Produce the pair plus the divergence list. Offer a
  per-award ranking, which is honest, instead of a global one, which is not.
- **Asked to confirm a pre-decided winner** → refuse. A score produced to reach a
  known verdict is worth nothing, and someone will reconstruct it.

## Further reading in this folder

- `rubrics.md` — the two scoring rubrics themselves: desirability categories and
  their 1-5 bands, the three award weightings and tie-break sequences,
  survivability's five dimensions and tiers. Read before scoring anything
- `reference/scorecard-shape.md` — the per-submission scorecard, plus the
  divergence and unresolved side files
- `reference/failure-modes.md` — seven ways a judging round reaches a confident
  wrong verdict, including the pillar-wide case this skill was built from
