---
name: multi-persona-roundtable
description: Stress-test one proposal from several fixed viewpoints that each own a kill criterion, run as separate isolated turns rather than one pass, so you get productive disagreement instead of an averaged opinion. Produces an append-only deliberation log and a verdict of ship, refine, or kill with the specific blocker named. Use when a proposal looks good and you suspect it will die on contact with ownership, funding, operations, or the people it claims to serve. Trigger phrases include roundtable, stress test this idea, red team, evaluate from multiple perspectives, poke holes in this, will this actually ship, pre-mortem, devil's advocate, panel review.
---

# Multi-Persona Roundtable

Interrogate one proposal through several fixed viewpoints, each taking a separate
turn with its own context, until either every kill criterion passes or one fails
with a named blocker.

Output is a **deliberation log** — append-only, one section per turn, ending in a
verdict. The log is the state: a paused roundtable resumes by reading it.

The persona set is in `personas.md` in this folder. Read it before starting.

## Use when

- A proposal reads well and you want to know how it dies
- Several people will need to agree, and you want their objections surfaced before
  the meeting rather than during it
- A scored proposal ranked high and you don't trust the score
- Deciding whether to fund or staff something, where the cost of being wrong is
  real

## Don't use when

- You are comparing many proposals. This runs on one. Score the field first with
  `defensible-submission-scoring`, then run this on the handful that matter.
- You want the idea improved. This finds what kills it. Those are different jobs
  and mixing them produces advocacy.
- The decision is already made. A deliberation run to justify a verdict produces
  seven paragraphs of agreement and no information.
- The decision is made and a specific action is now scheduled to fire — a cut-over,
  a deprecation, a termination. Use `dissent-before-commit`. It differs from this
  skill in what it does with disagreement: this one preserves divergence and is
  forbidden from averaging two personas into one position, because the divergence
  is the product. That one must force-rank down to a single strongest objection and
  then resolve it, by changing the action or by naming a tradeoff someone owns. It
  also re-checks objections raised at authoring time against what has changed
  since, which only means anything once an action has a history and an execution
  date. Run this skill on a Tuesday cut-over and you get a rich log and no decision
  at 14:00.
- Nothing about the proposal is contestable. If no viewpoint can object, there is
  nothing to deliberate.

## Inputs

Ask for these. Don't infer them.

```yaml
proposal:          # path, or the description itself. One proposal, not a set
persona_set:       # "default" (the seven in personas.md) or your own set
prior_evidence:    # existing research, scores, or prior art scan. Or "none"
closed_systems:    # named platforms in this environment with no usable API or
                   # export, which structurally block integration. Or "unknown"
log_path:          # where the deliberation log is written
```

**If `proposal` covers more than one idea, stop and ask which one.** A roundtable
on a bundle produces a verdict on nothing.

**If `prior_evidence` is "none",** proceed, but record
`no prior evidence — every claim requires fresh verification` in the log header,
and the ecosystem and feasibility personas must research more heavily to
compensate.

**If `closed_systems` is "unknown",** the feasibility persona cannot run its
structural-block test. Record that criterion as **unresolved**, not passed. An
unchecked kill criterion is not a passed one.

## The isolation rule

Personas in phase one do not see each other's output. They see the proposal, the
evidence, and their own brief.

This is load-bearing, not ceremony. When one context produces all viewpoints at
once, whichever perspective is articulated first sets the frame, and the rest
arrange themselves around it. You get an averaged opinion wearing seven headings.
Isolation is what makes the disagreement real, and the disagreement is the entire
product.

## Process

**0. Set up.** Load the persona set and check it before turn one. Every kill
criterion in `personas.md` needs a persona who owns it; a criterion with no owner
means the set cannot detect that failure, so name the gap and ask for a persona.
The set must cover ownership, feasibility, day-to-day operations, funding
sustainability, and who gets excluded — the five surfaces that actually kill
proposals, and a set missing one will approve things that die on it. Minimum three
personas, each with a distinct fear: two viewpoints produce a debate, one produces
an essay, and personas that share a fear produce one opinion in two voices. Then
write the log header: proposal, date, what evidence was loaded, what was missing,
and which criteria start unresolved.

**1. Divergence — parallel, blind.** Run the three expansive personas
simultaneously, each isolated. They expand the problem space, scan the ecosystem,
and check who is excluded. Append each turn to the log. Extract every question
directed at another persona and every explicit disagreement.

**2. Convergence — sequential.** Run the four grounding personas in order, each
reading the full log so far plus the questions aimed at it. Sequential because the
dependencies are real: funding cannot be modelled before the integration
assessment exists, and ownership cannot be assigned before the ecosystem scan
says whether someone else already owns it.

**3. Challenge rounds.** Scan the log for contradictions between personas,
directed questions still unanswered, and claims tagged unverified that another
persona can check. Route each to the persona who should answer. Append the
response. Stop when a round raises nothing new, or after three rounds — the cap
exists because unbounded rounds converge on politeness.

**4. Validation.** No subagents here; synthesize from the log.
   - Run every kill criterion against what the log actually says.
   - Tag the proposal appreciating, depreciating, or stable.
   - Build the tension table.
   - Write the verdict.

Pause for the user after each phase. They may continue, inject context the
personas lack, re-run one persona, or stop.

## Claim discipline

Every persona tags each factual claim `[Verified]`, `[Unverified]`,
`[Contradicted]`, or `[Requires SME]`. The tag definitions, and the seven claims
that cannot be asserted untagged at all, are in `reference/log-shape.md`.

## The kill criteria

An idea is dead if **any one** of these fails. This is what gives the set
filtering power. Without kill criteria everything receives "refine" and nothing
is ever cut.

| Criterion | Owned by |
|---|---|
| No identifiable owner | Sponsor + Ecosystem |
| Hits a closed system with no alternative data path | Architect |
| Net negative for the people who operate it | Operator |
| No funding path beyond the pilot | Funder |
| Harms or further excludes the people it claims to serve | Constituent |

A failure is `KILL` with the blocker named specifically. Never softened to
refine. The blocker names what would have to change to revisit.

## Hard rules

Each of these prevents a failure that produces a plausible-looking log. That is why
they are rules rather than advice — nothing downstream signals that one was
violated.

```text
One persona per turn. Never generate several viewpoints in one pass.
Phase-one personas are blind to each other. Phase-two personas read the log.
A persona that agrees with everything has failed its turn. Re-run it.
Every factual claim carries a tag. Untagged assertions do not enter the log.
Any one kill criterion failing means KILL, with the blocker named.
An unchecked kill criterion is unresolved, never passed.
Never resolve a tension by averaging. Record both positions and who held them.
The log is append-only. Corrections are new entries, not edits.
Verdicts come from the log, never from memory of the log.
```

## Stop instead of guessing

- **Fewer than three personas, or a kill criterion with no owner** → refuse. Name
  the missing viewpoint. A set that cannot detect a failure will approve it.
- **Asked to run all personas in one response** → refuse and explain the
  isolation rule. Offer to run them sequentially in one session instead, which is
  slower but preserves the mechanism.
- **The persona set misses ownership, feasibility, operations, funding, or
  exclusion** → name the gap and ask for a persona to cover it.
- **Asked for consensus, or for the personas to agree** → refuse the framing.
  Report the tensions. Absence of tension means the proposal is shallow or the
  personas collapsed into one voice, and both are findings.
- **`closed_systems` unknown and the verdict depends on it** → verdict is
  `Refine`, with the unresolved criterion named as the thing blocking a decision.
  Never `Ship` on an unchecked criterion.
- **A persona produces nothing usable twice** → record
  `<PERSONA> turn failed — manual input needed` in the log and continue. Do not
  write its turn on its behalf.
- **Log exceeds what later personas can read** → summarize earlier turns
  preserving every key claim, challenge, and citation. Never drop a challenge to
  save room; challenges are the payload.

## Further reading in this folder

- `personas.md` — the seven default viewpoints, the fear and kill criterion each
  carries, why the order is what it is, and the tension map. Read before starting
- `reference/log-shape.md` — the four claim tags, the seven claims that cannot be
  asserted untagged, and the log template
- `reference/failure-modes.md` — six ways this produces a log that reads as
  deliberation, starting with the single-pass consensus it exists to catch
