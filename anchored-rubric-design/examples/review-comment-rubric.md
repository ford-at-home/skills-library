# Rubric — non-prescriptive quality of an automated code-review comment

A worked rubric spec for a bot that comments on pull requests. The goal is a
comment that gets the author to *see* the problem, rather than one that hands
them a patch to apply without understanding it.

**Provenance, stated plainly:** the structure, the composite formula, and every
defect described under **Notes** are taken from a real deployed rubric. The
domain has been changed and the fields renamed. Nothing here is invented for
illustration — these are mistakes that shipped — but do not read the field names
as anyone's production code.

**Consumer:** selection of one model for a review-comment bot, from a fixed
candidate list, re-run weekly. Ranking is published internally.
**Internal scale:** 0.00-1.00 · **Converted at:** the read API, on the way out to
the UI, by ×10.
**Calibrated against:** live bot output across three comment families (logic
defect, unclear naming, missing edge case).

## Fields

### token_count
- Type: `deterministic`
- Range: integer ≥ 0. Ideal band 40-100
- Measures: whether the comment leaves the author room to think, rather than
  burying the point under text
- In tension with: `non_prescriptive`. Pointing at a defect without naming the
  fix costs words; the cheapest way to look concise is to just state the patch

### ends_with_open_question
- Type: `llm-bool`
- Range: true | false
- Measures: whether the comment hands the decision back — the last thing the
  author reads is an invitation to reason, not a closing instruction
- In tension with: `token_count`. Appending a question to a prescription
  satisfies this field and inflates the other

### non_prescriptive
- Type: `llm-scalar`
- Range: 0.00-1.00, six bands
- Measures: whether the comment as a whole guides the author to the defect, or
  states the fix with a question attached
- In tension with: `ends_with_open_question`. A comment can end on a genuine
  open question and still have spent four sentences dictating the change

**Notes.** Three fields, and the tension is real in both directions: you cannot
raise all three with one move. Adding a terminal question raises field two and
worsens field one. Trimming to look concise usually flattens field three. That
mutual pull is the whole reason the rubric resists gaming — not the strictness of
the judge prompt.

`ends_with_open_question` is an `llm-bool`, not a string check. `endswith("?")`
would pass "Can you take another look at this?", which is a directive wearing a
question mark and the opposite of the intended behavior. This is the case where
the decidability gate correctly says *no function can do this*.

## Bands — non_prescriptive

| Range | An output here |
|---|---|
| 1.00 | Purely non-prescriptive: only questions about the code's behavior, zero fix stated, zero implementation given |
| 0.80-0.99 | Mostly non-prescriptive: primarily questions with minimal framing, one brief orienting phrase at most |
| 0.60-0.79 | Somewhat non-prescriptive: questions present, but includes hints at the fix, explanations, or multiple context phrases |
| 0.40-0.59 | Mixed: equal parts questioning and prescribing |
| 0.20-0.39 | Mostly prescriptive: primarily states the change, with token questions |
| 0.00-0.19 | Purely prescriptive: dictates the patch, no meaningful questions |

## Judge prompt — ends_with_open_question

Delivered as its own call. Temperature 0.3, max output 150 tokens.

```text
You are evaluating if a code-review comment ends with an open question.

Comment:
{comment}

An open question:
- Genuinely probes the author's reasoning, assumptions, or intent
- Invites explanation, reflection, or exploration of alternatives
- Does NOT seek yes/no confirmation to proceed (e.g., "Can you take a look?"
  "Sound good?")
- Does NOT state the fix disguised as a question (e.g., "Shouldn't this be a
  set?" "Wouldn't a guard clause be cleaner here?")

Task: Does this comment END with an open question?

Return ONLY a JSON object with this exact format:
{
  "ends_with_open_question": true or false,
  "explanation": "1-2 sentence justification"
}
```

**Notes.** Two of the four bullets are exclusions, and they carry most of the
weight. They name the two specific fakes — the procedural confirmation and the
rhetorical question — that a judge given only the positive definition waves
through, because both end in a question mark and read as engagement.

## Judge prompt — non_prescriptive

Its own call. Temperature 0.3, max output 200 tokens. Band table above is inlined
into this prompt.

```text
You are a STRICT evaluator of code-review comments. Be highly critical and
discriminating.

Comment:
{comment}

Context: {diff_context}

A non-prescriptive comment GUIDES the author to find the defect through their
own reasoning. It does NOT dictate the patch, supply the implementation, or
information-dump.

Scoring Scale (0.00-1.00) - BE STRICT:
<the six bands, verbatim>

STRICT Criteria for HIGH scores (0.80+):
- Questions that probe intent, invariants, or the author's mental model
- Reflects the author's own naming or comments back for examination
- Builds on what the diff already establishes
- ZERO implementation, corrected code, or explanations provided
- No more than ONE brief orienting phrase (5 words max)

AUTOMATIC penalties:
- Any corrected code or explanation given: -0.20 minimum
- Multiple context-setting phrases: -0.15
- Rhetorical questions: -0.10
- Leading questions that imply the fix: -0.15

Task: Rate how non-prescriptive this comment is. BE CRITICAL AND STRICT.

Return ONLY a JSON object with this exact format:
{
  "non_prescriptive": 0.65,
  "explanation": "2-3 sentences analyzing the comment and identifying any
   prescriptive elements"
}
```

**Notes.** The four "AUTOMATIC penalties" are instructions to the model. Nothing
in the pipeline verifies they were applied. They are advisory, and a document
describing them as enforced would be wrong. Contrast the composite below, which
is enforced because it is arithmetic.

"BE STRICT" appears three times. Instructions like that shift the whole
distribution down without spreading it. The bands are what spread it. If you are
tempted to add a fourth "be strict", add band text instead.

## Composite

Computed in Python from the three fields, after both judge calls return. As
deployed:

```python
def compute_overall_score(
    token_count: int,
    ends_with_question: bool,
    non_prescriptive: float
) -> float:
    if token_count < 40:
        verbosity_penalty = (40 - token_count) / 40
    elif token_count <= 100:
        verbosity_penalty = 0.0
    else:
        verbosity_penalty = min(1.0, (token_count - 100) / 100)

    question_penalty = 0.0 if ends_with_question else 0.5

    prescription_penalty = (1.0 - non_prescriptive) ** 0.7

    overall = 1.0 - (
        0.2 * verbosity_penalty +
        0.3 * question_penalty +
        0.5 * prescription_penalty
    )

    return max(0.0, min(1.0, overall))
```

| Field | Penalty cap | Weight | Max influence on composite |
|---|---|---|---|
| token_count | 1.00 | 0.2 | 0.20 |
| ends_with_open_question | 0.50 | 0.3 | **0.15** |
| non_prescriptive | 1.00 | 0.5 | 0.50 |

**Notes — read this table before copying the formula.**

Two things fall out of the arithmetic that the original code's own comments got
wrong.

The question field was described in the source as a "Fixed 50% penalty". Its
penalty is 0.5 and its weight is 0.3, so the most it can move the composite is
0.15 — less than the verbosity field, which is nominally weighted lower. If you
intend a binary miss to cost 0.3, the penalty has to be 1.0.

The exponent on `prescription_penalty` was commented as a "gentler curve". It is
harsher than linear, not gentler: for any value strictly between 0 and 1, raising
it to the power 0.7 makes it larger. At `non_prescriptive = 0.5` the penalty is
0.5\*\*0.7 ≈ 0.616, not 0.5. Mid-range comments are punished more than a linear
penalty would punish them. That may well be the right behavior for this rubric —
the point is that the comment asserted the opposite, and nobody checked.

Maximum total penalty is 0.20 + 0.15 + 0.50 = 0.85, so the composite bottoms out
at 0.15 and the clamp to 0.0 is unreachable. A published floor of 0.15 on a
0.00-1.00 scale is a defensible choice, but it should be a stated one.

## Error value

A failed judge call stored an error string and an empty score object. The accessor
then reported the overall as `0.0`.

**This is the defect the skill's error rule exists to prevent.** A pipeline
failure and a maximally prescriptive comment become the same number. The read API
compensated with `if overall_score < 0.01: continue` — a magic threshold that also
silently drops any genuine near-zero score, which improves every published ranking
by an unrecorded amount.

The fix is a distinct value: record `null` with the error text, exclude it from
means, and report the excluded count alongside the score.

## Scale conversion

Internal 0.00-1.00 everywhere: judge output, stored records, aggregates. The read
API multiplies by 10 on the way out. The chart consumes 0-10 and does nothing.

In the project this rubric came from, nine separate commits were scale-conversion
fixes, and several corrected the previous one: one multiplied chart values by 10,
the next by 100 "(10x again)", a later one removed a duplicate conversion because
the API had meanwhile started converting. A separate commit migrated a threshold
from `3.0` to `0.5` when the internal scale changed — a constant compared against
a score is a scale-carrying value and has to move with it.

One further violation went undetected for the life of that deployment: an
aggregate endpoint recomputed its own "overall" as the unweighted mean of the
three fields on the 0-10 scale, which is not the penalty composite above. Two
different numbers called `overall` were served from the same deployment. Compute
the composite once, at judgement time, and never again.
