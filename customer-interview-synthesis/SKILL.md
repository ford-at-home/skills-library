---
name: customer-interview-synthesis
description: Gate a set of customer interviews before their themes become proposal-grade conclusions. Requires the team's prior hypothesis as an input, enforces a minimum transcript count below which output is forced to exploratory, strips any bias flag that cannot quote the panel or a transcript, and refuses to let an interviewer's notes ground a claim about what a respondent actually did. Use when the risk is that the team's prior comes back dressed as customer signal. Not an interview guide generator and not a theme extractor — it is the check on one. Trigger phrases include is this research actually validated, did the interviews confirm what we already believed, bias check on our research, can we build a proposal on this panel, how many interviews is enough, synthesize our user research.
---

# Customer Interview Synthesis

Turn interviews into structured inputs a proposal can be built on, and refuse when
the panel cannot carry that weight.

Clustering quotes into segments, extracting workarounds, and writing job
statements are things you can already do. This skill exists for the four checks
that get skipped when you do: the prior hypothesis on record, the sample floor,
citations on bias flags, and the line between a transcript and somebody's notes.

Output is a **synthesis packet**, never the proposal. If asked to confirm an idea
is validated, it refuses and offers the disconfirming evidence instead.

## Use when

- A synthesis exists or is about to be written and a proposal is the next artifact
- You suspect the research confirmed what the team already believed
- A draft proposal failed on "who specifically is the customer" or "what do they
  do today instead"

## Don't use when

- No interviews have happened. This does not infer customers from documents
- What's needed is an interview guide, a market analysis, or a competitive
  teardown. Different jobs
- The caller wants reassurance. This is built to find disconfirming evidence

## Inputs

Ask for these. Don't infer them.

```yaml
hypothesis_going_in:  # REQUIRED. What the team believed before the interviews
target_artifact:      # proposal | business case | exploratory
transcripts:          # verbatim records. Weighted high
structured_notes:     # interviewer's notes. Weighted low — these carry the
                      # interviewer's selection bias
survey_responses:     # structured survey data. Weighted medium
interview_count:      # integer, total across all artifact types. Reported as N
transcript_count:     # integer, transcripts only. The floor counts these
survey_count:         # integer, surveys only. Reported beside N, never toward
                      # the floor
sample_floor:         # minimum transcripts for proposal-grade output. Default 8
selection_method:     # how respondents were chosen — cold outreach, existing
                      # customers, friend-of-friend, panel, inbound
interview_method:     # how they were conducted, and by whom
```

**If `hypothesis_going_in` is missing, stop and ask.** It is the only thing that
makes the bias check falsifiable. Without knowing what the team expected to hear,
"the themes match the hypothesis" is unfalsifiable and the exercise is decoration.

**Keep transcripts, notes, and surveys separately tagged throughout.** Merging
them at intake is unrecoverable.

## Gates

Run these before synthesizing. A gate applied afterwards is applied to a
conclusion someone is already attached to.

| Gate | Passes when | If it fails |
|---|---|---|
| Minimum N | `transcript_count >= sample_floor` when `target_artifact` is proposal or business case | Force `target_artifact: exploratory`, set `proposal_ready: false` |
| Sources distinguished | Transcripts, notes, and surveys arrive separated | Re-request the inputs |
| Behavioral claims cited | Every claim about what a respondent *did* has a quoted phrase and a source identifier | Strip it, or relabel it attitudinal |
| Bias flags cited | Every bias flag quotes `selection_method`, `interview_method`, or a transcript | Strip the flag. An uncited flag does not exist |
| Frequency is numeric | Every workaround carries `{count, of_n}` | Replace "common" or "several" with numbers, or strip |
| Attitudinal-only marked | Any segment whose evidence is entirely attitudinal is `[assumption]`, never `[fact]` | Add the tag and the warning |
| Disconfirmation present | `evidence_against` is non-empty, or its emptiness is itself flagged | Flag it |

**The floor is a default, not a law.** It defaults to 8 transcripts, calibrated
for the small qualitative panels this skill is written for, where the
decision-relevant signal is segment heterogeneity: much below that, one
dissenting respondent cannot be told from noise and an absence of dissent says
nothing either way. It is not a statistical threshold and this skill does not
claim one. Set `sample_floor` higher where the population is narrow enough that
each respondent is nearly a segment of its own, lower where the population itself
is smaller than the default — and say which, and why, in the packet header.
Surveys never count toward it. The floor is set at intake, before there is a
conclusion for it to accommodate.

Claim tags, one per claim, no parallel scheme: `[fact]` (sourced),
`[assumption]` (believed, untested), `[inference]` (derived from facts above),
`[open question]`.

**Behavioral** is what a respondent did — switched tools, paid for a workaround,
built a script, churned. **Attitudinal** is what they said they would do. Stated
attitude predicts later behavior positively but weakly, so behavioral
corroboration is required rather than inferred. A segment with no behavioral
evidence is `[assumption]`.

## Bias patterns worth flagging

Seven patterns, each with where to look for it and what it does to the
conclusions: friendly panel, recruited via the problem, single-segment collapse,
solution-first framing, hypothesis pre-loading, missing disconfirmation, ignored
dissenters. They are in `reference/bias-patterns.md`. Only these, only with a
quote, and they compound rather than average.

## Process

1. Collect and keep sources separate, each tagged.
2. Gate-check. If `transcript_count < sample_floor`, drop to `exploratory` now,
   not after producing conclusions that will be hard to walk back.
3. Cluster quotes into candidate segments, each carrying its source identifier.
4. Classify each piece of evidence behavioral or attitudinal, and tag every claim.
5. Quantify workarounds as `{count, of_n}`. Strip any workaround no respondent
   mentioned, including ones you know exist.
6. Hunt the patterns in `reference/bias-patterns.md`. Attach the quote, or drop
   the flag.
7. Preserve conflicts in `conflict_with_segments`. Never average dissent away.
8. State the hypothesis's status strictly against evidence. `evidence_against` is
   a required field.
9. Map to the proposal explicitly: which specific segment becomes the customer, a
   category is not a segment.
10. Set `proposal_ready` only if every gate passed and at least one segment has
    behavioral corroboration.

## Hard rules

These are rules rather than advice because each failure they prevent produces a
packet that reads as evidence — nothing downstream signals that one was violated.

```text
No bias flag without a quoted citation.
No proposal-grade output below the sample floor, counted in transcripts. The floor
  defaults to 8, is set at intake, and is stated in the packet header.
A segment with zero behavioral evidence is [assumption], never [fact].
Notes are not transcripts. An interviewer's summary cannot ground what someone did.
Frequency is a count over a denominator, never a word.
evidence_against is required. Its emptiness is a finding, not a pass.
Never collapse a dissenting respondent into the majority theme.
Never invent a quote, a respondent, or a workaround nobody mentioned.
Refer to respondents by identifier, never by name or employer.
```

The citation rule carries the skill. Bias hunting invites plausible-sounding
pattern matches, and an uncited flag is indistinguishable from a fabricated one.
It is also the first rule softened under time pressure, at which point the flags
become theater.

The identifier rule is not ceremony. This packet circulates further than the
transcripts do and frequently ends up pasted into a proposal. Use `R1`, `R2`;
keep the mapping wherever the transcripts live.

## Output

A synthesis packet: header with N, the floor in effect, and `proposal_ready`, a
"Read first" block, segments, problem, workarounds with counts, hypothesis
status, bias flags, assumptions to resolve, and the map to the proposal. The
template is `reference/packet-shape.md`.

## Stop instead of guessing

- **`interview_count == 0`** → stop. No document substitutes for it.
- **`hypothesis_going_in` missing** → stop and ask.
- **The "transcripts" are summaries a team member wrote** → these are notes. Ask
  for the recordings, or proceed as `exploratory`.
- **Notes only** → run with a prominent warning and never set
  `proposal_ready: true`. Interviewer-filtered records cannot establish what
  respondents did.
- **Fewer transcripts than the floor and the caller asks to proceed anyway** →
  produce `exploratory`. Do not raise the confidence of the conclusions to match
  the intended use.
- **Asked to lower the floor once the synthesis exists** → refuse. A floor moved
  after the conclusions are visible is a gate fitted to what passed it. Setting
  it at intake, with a reason, is the only version that means anything.
- **Asked to confirm the idea is validated** → refuse, and surface the
  disconfirming evidence. This is the request the skill exists to decline.
- **A pattern looks like it applies but nothing can be quoted** → drop it. Do not
  write it with a hedge.

## Further reading in this folder

- `reference/bias-patterns.md` — the seven patterns, where each one shows up in
  the intake fields, and what each does to the conclusions
- `reference/packet-shape.md` — the packet template, why "Read first" exists, and
  why the customer field takes a segment rather than a category
- `reference/failure-modes.md` — four ways this produces a synthesis that reads
  as evidence, including the one it exists to catch
