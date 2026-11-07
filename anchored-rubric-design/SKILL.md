---
name: anchored-rubric-design
description: Design the scale for judging model output — fields that trade off against each other so one cheap trick can't max the score, numbered bands with worked anchors instead of an unanchored 1-10, each field typed rule-computed or LLM-judged, and the composite as deterministic arithmetic rather than an LLM's overall number. Produces a rubric spec; running one across candidates is `llm-behavior-benchmark`. Use before benchmarking, evaluating, or grading any model behavior — review-comment quality, empathy, concision, refusal quality, brand voice, teaching style. Trigger phrases include design a rubric, scoring criteria, LLM as judge, how should we grade this, evaluation dimensions, judge prompt, score the outputs, our scores are all the same.
---

# Anchored Rubric Design

Convert a behavior someone can only recognize by eye into a rubric two people
score the same way.

Output is a **rubric spec** — field definitions, band anchors, judge prompts, and
the composite formula. It is a document, not a running system. Executing it
against candidates is a separate job.

## Use when

- You want to measure a behavior, not a capability. "Does this comment guide
  rather than dictate" and "does this refuse safely" are behaviors; "does this
  pass the test suite" is not
- Scores already exist and cluster in a narrow band, or two reviewers disagree
- You are about to write "rate this 1-10" into a judge prompt
- Someone is about to publish a ranking that a vendor will contest

## Don't use when

- The property is decidable in code. If `endswith("?")` answers it, write the
  function. A rubric on a decidable property is overhead
- You need a single spot verdict on one output. Score it and move on
- You have no sample outputs. Bands written without seeing real outputs anchor
  to nothing — see stop conditions
- You are measuring correctness against a known answer key. That's accuracy,
  and it needs a dataset, not a rubric
- You already have an anchored rubric and need to run it across candidates. Use
  `llm-behavior-benchmark`
- What is being scored is human submissions to a call rather than model output.
  Use `defensible-submission-scoring`, which carries its own rubrics

## Inputs

Ask for these. Don't infer them.

```yaml
behavior:          # the behavior in one sentence, stated as observable output
                   # properties. "Guides by questioning without supplying
                   # answers" — not "is a good tutor"
samples:           # path or inline. 10+ real outputs, deliberately including
                   # ones you consider bad. Required
consumer:          # who acts on the score, and what they can do about it.
                   # "we pick one of 26 models for production" — not "reporting"
existing_rubric:   # path, or "none"
gaming_pressure:   # "none" | "the thing being scored is also being optimized
                   # against this rubric"
```

**If `samples` is missing, stop and ask.** Every band boundary in this skill is
calibrated against real output. Without samples you are writing prose that looks
like a rubric.

**If `consumer` is missing, stop and ask.** It sets how many fields are worth
having. A consumer who can only pick or not-pick needs fewer than one who tunes
a prompt.

## Gates

Check these before writing any band text. A gate written after the rubric is
written to pass.

1. **Tension gate.** Name, for each pair of fields, an output that scores well on
   one by scoring badly on the other. If no such pair exists, the fields are
   measuring one thing and the rubric is one field wearing a costume.
2. **Sample-spread gate.** Your samples must contain at least one output you
   expect to land in the bottom band and one in the top. If they all land in the
   middle, you cannot tell a working rubric from a broken one.
3. **Decidability gate.** For each field, state whether a deterministic function
   can compute it. If yes, it is not an LLM-judged field.

## Process

1. **Decompose the behavior into 3-5 candidate fields.** Fewer than three and a
   single trick maxes the score. More than five and no reviewer holds them in
   mind, and they stop being independent. If an existing rubric was supplied,
   score the samples with it first and record where it fails to separate them —
   that is the evidence for whatever you change.

2. **Apply the tension gate and cut.** Keep the fields that pull against each
   other. This is the step that produces an ungameable rubric, and it is the
   step people skip.

3. **Type each field.** One of:
   - `deterministic` — computed from the output in code. Token count, length,
     presence of a required section
   - `llm-bool` — a judgement a function can't make, answered true or false
   - `llm-scalar` — a judgement on a bounded numeric scale

   Prefer `deterministic`. Escalate to `llm-bool` before `llm-scalar`: a boolean
   forces the judge to commit, and commits are easier to audit than a 0.65.

4. **For every LLM-judged field, write the exclusions before the inclusions.**
   What the field looks like when faked is more useful to a judge than what it
   looks like when genuine. A judge told only what to reward rewards surface
   form.

5. **Anchor every scalar into numbered bands.** Each band gets a range and a
   description of what an output in it actually does. Six bands is a workable
   default: it forces a top band that means "nothing wrong" and a bottom band
   that means "the behavior is absent", with four discriminations between.

6. **Write the composite as arithmetic over the fields.** Penalty form works
   well: start from a perfect score and subtract weighted penalties. Never ask
   the LLM for the overall number — see hard rules.

7. **Check the composite's reachable range per field.** A penalty capped below
   1.0 cannot move the composite by its full weight. Multiply cap by weight and
   confirm the result is the influence you intended.

8. **Score your samples by hand and look at the spread.** If every sample lands
   within 0.15 of the mean, the bands are not discriminating. Widen the band
   descriptions, not the weights.

9. **Run a gaming audit.** For each field, write the cheapest output that scores
   well on it. Then score that output on the whole composite. If it wins, the
   tension gate failed and you go back to step 2. Under real gaming pressure —
   the thing being scored is also being tuned against this rubric — do this for
   every pair of fields as well, since the cheap win is usually a combination.

10. **Declare the scale and the conversion boundary.** State the internal scale
    once, and state the single place where it may be converted for display. This
    line is load-bearing; see hard rules.

Each judged field gets its own judge call, at low fixed temperature, returning
JSON. Do not ask one call for several fields: a single response lets the model
make its numbers agree with each other, which destroys the independence the
tension gate bought you.

## Hard rules

Each of these prevents a failure that produces a plausible-looking score. That
is why they are rules rather than advice — nothing downstream signals that one
was violated.

```text
The composite is arithmetic in your code. Never an LLM output field.
A penalty you instruct the judge to apply is a suggestion. A penalty you
  compute is a guarantee. Do not confuse the two in your own documentation.
An unanchored 1-10 scale is not a rubric. Judges pile onto 7 and 8.
One judge call per judged field.
Declare one internal scale. Convert at exactly one boundary, on the way out.
Thresholds carry a scale. Any constant compared against a score must be
  restated when the scale changes.
An errored judgement is not a zero. It needs its own value.
```

The first rule is the one that gets argued with. An LLM asked for both parts and
an overall will produce an overall that does not follow from its own parts, and
it will not tell you when they diverge. Computing the composite yourself means a
weight change re-scores your entire history without re-running a single judge
call.

## Stop instead of guessing

- **No samples** → stop and ask. Do not write bands from imagination and label
  them calibrated.
- **The behavior can't be stated as observable output properties** → stop. Return
  the question "what would I see in the text if this were present?" A rubric
  cannot be built on an inference about intent.
- **Fields show no tension after two attempts at decomposition** → say so, and
  ship one field. A one-field rubric that admits it is one field is honest; four
  correlated fields imply rigor that isn't there.
- **All samples land in one band** → stop and ask for samples from the range you
  are missing. Do not adjust boundaries until the distribution looks reasonable;
  that is fitting the rubric to the sample you happen to have.
- **Asked to add a dimension because a stakeholder wants it visible** → refuse
  unless it passes the tension gate. Report it as a reported field with weight
  zero instead. A weighted field nobody can define moves the ranking.

## Further reading in this folder

- `reference/rubric-spec-template.md` — the section-by-section shape of the
  document this skill produces
- `reference/failure-modes.md` — seven ways a rubric produces a confident wrong
  ranking, and what skipping the single-conversion-boundary rule cost one project
- `examples/review-comment-rubric.md` — a complete rubric spec: three fields in
  mutual tension, a six-band anchored scale, and a deterministic penalty
  composite, taken from a real deployment along with the four arithmetic and
  error-handling defects it shipped with
