---
name: llm-behavior-benchmark
description: Execute an existing rubric across several models or prompts so the resulting ranking survives being contested. Pins the run to a content-hashed manifest, gives every candidate byte-identical inputs, judges with a pinned judge model at fixed temperature, computes the composite once, keeps errors distinguishable from bad scores, and proves the judge discriminates before anything is published. Consumes a rubric; designing one is `anchored-rubric-design`. Use when comparing models on a behavior rather than an answer key, standing up a recurring eval, or investigating why every candidate scores the same. Trigger phrases include benchmark these models, compare models, model bake-off, LLM as judge, eval harness, leaderboard, our eval shows no difference, weekly eval, which model should we use.
---

# LLM Behavior Benchmark

Execute a rubric against a candidate set and produce a ranking you can defend to
whoever comes last in it.

Output is a **run record** — the manifest, per-unit judgements, the ranking, and
the validity checks that ran before publication. Designing the rubric is a
separate job; this skill consumes one and refuses to invent one.

## Use when

- Two or more candidates (models, prompts, system-prompt variants) must be
  compared on a behavior with no answer key
- A ranking will be published, cited, or used to spend money
- An existing eval reports scores that don't separate candidates
- An eval will recur, and this run must stay comparable to the next one

## Don't use when

- You have no rubric with anchored bands and a deterministic composite. Build one
  first with `anchored-rubric-design`; running an unanchored rubric produces a
  ranking that reverses on rerun
- The candidates are human submissions to a call rather than models or prompts.
  Use `defensible-submission-scoring`
- One candidate. There is nothing to rank; score it and read the justifications
- You are measuring against known-correct answers. That's accuracy on a dataset
- You need to know *why* a candidate behaves a way. Read the transcripts. A
  benchmark tells you the ordering, not the mechanism

## Inputs

Ask for these. Don't infer them.

```yaml
rubric_spec:       # path. Must define fields, types, band anchors, and the
                   # composite as arithmetic. Required
candidates:        # the full list, with the exact identifier used at call time
                   # (versioned model id, not "Claude")
scenario_set:      # the fixed inputs every candidate receives. Required
judge:             # judge identifier and temperature. Required, and pinned
candidate_params:  # temperature, max tokens, applied identically to all
budget:            # spend ceiling, or "unbounded"
publication:       # who sees the ranking, and whether candidates can contest it
```

**If `rubric_spec` is missing or its composite is an LLM output field, stop.**
This skill cannot produce a defensible ranking from an undefined scale, and
substituting one silently is the failure mode it exists to prevent.

**If `scenario_set` is missing, stop and ask.** Identical inputs are the only
reason the comparison means anything.

**If `judge` is unpinned** — a floating alias, or "whatever model we have" — stop.
A judge that changes between runs makes weeks incomparable and the change leaves
no trace in the data.

## Gates

Check all four before spending anything.

1. **Rubric gate.** Bands are numbered with ranges. The composite is arithmetic.
   Field types are declared. If any is absent, return to rubric design.
2. **Identity gate.** Every candidate receives the same scenario text, the same
   candidate parameters, and the same judge. Name any exception now, in the
   manifest, or don't make it.
3. **Reachability gate.** The harness must actually exercise the depth the config
   declares. If the config says five turns, run one unit end to end and count
   the turns in the stored artifact. This one is common and invisible — see
   `reference/failure-modes.md`.
4. **Discrimination gate.** After a pilot of ~10 units, the composite must span
   more than one band. A flat pilot means stop, not scale up.

## Process

1. **Freeze the config and hash it.** Serialize candidates, scenarios, judge, and
   parameters canonically — sorted keys, no incidental whitespace — and take a
   content hash. The manifest id is that hash plus a date. Same config, same id.
   Every stored record carries it.

2. **Enumerate the full cross product.** Every candidate × every scenario. A
   partial matrix is a different benchmark; if you subset, subset in the config
   so the hash changes.

3. **Run a pilot of ~10 units and stop.** Check gates 3 and 4 against real
   artifacts. This is the cheapest place to discover the harness isn't doing
   what the config says.

4. **Execute the matrix.** For each unit, store a raw artifact containing the
   exact input sent, the exact output received, token counts, latency, and the
   manifest id. Store this before judging. The raw artifact is what lets you
   re-judge under a revised rubric without re-running candidates, which is the
   expensive half.

5. **Judge each unit.** One call per judged field, at the pinned judge and fixed
   low temperature. Store the judge's returned justification alongside the score
   — a score without its justification cannot be audited or contested.

6. **Compute the composite once, here, in code.** Store it on the unit. Nothing
   downstream recomputes it. Ever.

7. **Record failures as failures.** A judge error, a refused call, a malformed
   response: store the error text and a null score. Never a zero.

8. **Aggregate with the excluded count visible.** Mean per candidate, plus n,
   plus how many units were excluded and why. A mean over 4 of 12 units is not
   the same finding as a mean over 12.

9. **Run every check in `reference/validity-checks.md`.** Any red result blocks
   publication.

10. **Convert scale once, at the read boundary.** Internal scale everywhere;
    conversion happens on the way out to display and nowhere else. Every
    threshold constant in the system is restated in the internal scale.

11. **Write the run record**, including what you would need to change to make
    this run comparable to the next one.

## Hard rules

Each of these prevents a failure that produces a plausible-looking ranking. That
is why they are rules rather than advice — nothing downstream signals that one
was violated.

```text
Every candidate gets byte-identical scenario text and identical parameters.
The judge identifier is pinned to an exact version and recorded per unit.
Judge temperature is low and fixed. Candidate temperature is separate and
  never silently shared with it.
The composite is computed once, at judgement time, in your code.
An error is null with an error string. Never zero.
Raw artifacts are retained. Judgement is re-runnable without re-running
  candidates.
Never compare results across manifest hashes without saying so.
Convert scale at exactly one boundary. Restate every threshold when the
  internal scale changes.
No fallback config. A missing manifest is a stop, not a default.
Prior expectations do not live in the run config.
```

The composite rule and the fallback rule each cost the source project real money
to learn; `reference/failure-modes.md` has both incidents.

## Stop instead of guessing

- **Rubric has unanchored scales or an LLM-authored composite** → stop. Say which
  is missing. Do not run and caveat the output; a published ranking outlives its
  caveats.
- **Pilot shows no spread** → stop before the full matrix. Report the pilot
  distribution. Scaling a flat pilot buys a precise flat result.
- **Harness reaches less depth than the config declares** → stop and report the
  discrepancy. Do not publish a five-turn benchmark that ran one turn.
- **A candidate errors on every unit** → report it as unmeasured. Not last place.
  Absent capability and failed integration are different findings.
- **Judge and candidate are the same model** → stop and say so. Run it if the
  owner accepts self-preference, but never without naming it in the run record.
- **Asked to rerun until a preferred candidate wins, or to drop scenarios where
  it loses** → refuse. Offer instead to add scenarios that probe the specific
  behavior the requester cares about, in the config, so the hash changes and the
  change is legible.

## Further reading in this folder

- `reference/validity-checks.md` — the seven pre-publication checks, what makes
  each one red, and what a red result means
- `reference/run-record.md` — the shape of the run record, including the
  comparability and "what the ranking does not tell you" sections
- `reference/failure-modes.md` — eight ways a benchmark publishes a confident
  wrong ordering, with the incidents behind the composite and fallback rules
