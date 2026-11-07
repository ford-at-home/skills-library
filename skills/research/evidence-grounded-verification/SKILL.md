---
name: evidence-grounded-verification
description: Clear every load-bearing claim in a document before it reaches someone who can check it. Sorts each claim into do-not-cite, correct-before-use, or cleared; records where you looked; separates measured numbers from derived ones, and unverified from false. Catches claims that feel established only because your own team has repeated them. Use before sending a grant application, board memo, regulatory filing, investor update, press release, conference talk, or README, or when someone asks "are we sure about this?" Trigger phrases include fact check, verify claims, source this, check our numbers, provenance, before we send this, is this actually true.
---

# Evidence-Grounded Verification

Interrogate a document's load-bearing claims until each one is sourced,
corrected, or quarantined.

Output is a **fact base** — a separate document listing claims and their status.
You never edit the source draft. The author does that, using the fact base.

## Use when

- A document goes to someone who can independently check it
- A number, date, status, or attribution is about to be stated publicly
- A figure is about to be presented as measured
- Someone asks whether a claim is safe to use

## Don't use when

- You need to *find* evidence. This skill checks claims; it doesn't research them.
- You're judging whether an idea is good, rather than whether a claim is true.
  Scoring a submission against criteria, or reviewing one proposal from several
  viewpoints, is a different job.
- You're editing prose quality.
- Nothing depends on the document's accuracy. This is expensive and its value
  scales with the cost of being wrong.

## Inputs

Ask for these. Don't infer them.

```yaml
source_document:     # path to the draft being cleared
audience:            # who reads this, and what they can check.
                     # "a program officer who will open our 990" — not "external"
existing_fact_base:  # path, or "none"
scope:               # "everything" or "the top N claims"
```

**If `audience` is missing, stop and ask.** Clearance is meaningless without it:
the same claim can be fine in a blog post and disqualifying in a filing.

## Process

1. **Extract every checkable claim before checking any of them.** A claim is
   load-bearing if the document's argument changes when it's false. Checking as
   you read biases you toward the easy ones, and the hard ones are where the
   problems are.

   Careful with that test on a reference document — a spec, a definitions list,
   a framework summary, a data dictionary. It has no argument to change, so the
   test reads as "nothing here is load-bearing" when in fact everything is.
   Extract all of these:

   - counts, dates, statuses, costs, attributions
   - **definitions of things defined elsewhere** — a named framework, standard,
     statute, metric, or acronym. These are the case where a document is
     perfectly self-consistent and simply wrong, so internal review never
     catches them. Check each against the originating source, not against the
     rest of the document.
   - capability claims: what the thing does, integrates with, or deploys
   - existence claims: that a file, endpoint, test suite, or dataset is there

2. **For each claim, look for a source outside your own organization.** Record
   the search — including where you looked and found nothing. A documented null
   result is a finding, not a hole in your work.

   When the claim is about something built, the outside source is the artifact,
   not more prose: the deployment config, the entrypoint, the config file, the
   test files, the directory itself. Prose written by whoever built the thing
   cannot clear a claim about the thing. **Open the artifact.** A surprising
   number of defects turn out to be a documented file that isn't on disk.

3. **Sort into the three blocks** below.

4. **Propagate parent status.** A claim derived from another inherits the other's
   block. A deadline that exists only because of an unsourced commitment is
   itself unsourced. Do this after sorting, then re-check the blocks.

5. **Tag each cleared claim** with a clearance level and the date you cleared it.
   The levels, and what each one lets you say, are in
   `reference/fact-base-shape.md`.

6. **Separate measured from derived numbers.** For anything derived, state the
   assumption and whether the method was ever checked against measured data.

7. **Record contradictions.** Where two sources disagree, list both. Never
   quietly take the more favorable figure.

8. **Put unresolved items at the top** of the fact base, not the bottom.

## The three blocks

| Block | Meaning | What to do |
|---|---|---|
| **1 — Do not cite** | No source outside your org exists | Remove, or re-anchor to a nearby documented fact. Rewording does not fix this |
| **2 — Correct before use** | Real, but stated wrong or misattributed | Fix to the correction recorded, then use |
| **3 — Cleared** | Holds against a source | Use the exact phrasing recorded |

### Block 1 discipline

These three get argued with every time:

1. **Hedging doesn't rescue a Block 1 claim.** "Reportedly" and "we understand
   that" move the liability, not the evidence.
2. **Don't park a claim in Block 2 because it's probably true.** Block 2 is for
   claims that have a source and a wording problem. No source means Block 1.
3. **Re-anchor rather than delete.** Replace the unsourced framing with the
   nearest documented fact. Deletion loses the author's point; re-anchoring
   keeps it and makes it survivable.

## Hard rules

Each of these prevents a fact base that reads as finished while passing a claim
it should have caught. That is why they are rules rather than advice — a
cleared-looking entry gives no sign that one was violated.

```text
Internal repetition is not corroboration.
Never clear a claim by citing a document your own team wrote.
A null result is a finding. Record the search you ran.
Unverified is not false. A check you were blocked from running is Unresolved.
Derived claims inherit the status of their parent.
Derived numbers never carry the confidence of measured ones.
An undated clearance is not a clearance.
Never adopt the more favorable of two contradicting figures. Record both.
Never edit the source document.
```

The first rule is the reason this skill exists. A claim repeated across three
internal decks looks better sourced each time it's copied, and isn't.

## Currency

Some claims decay between clearance and publication: legislative status, funding
rounds, headcount, pricing, org structure. State at the top of the fact base what
decays first and when it must be re-checked. Date every entry.

## Claims that are true and still shouldn't ship

Naming a private counterparty in a public or government submission is a
relationship risk *independent of whether the claim is verified*. Flag these
separately. They need someone's sign-off, not a better source.

## Output

A fact base, in the shape given in `reference/fact-base-shape.md`.

## Stop instead of guessing

- **No audience given** → stop and ask.
- **Document has no checkable claims** → say so. Don't inflate rhetoric into
  claims to justify the exercise.
- **A source is unreachable** → Unresolved, recording the access failure and
  what would settle it. Don't infer, approximate, or substitute a similar claim
  from elsewhere — and don't file it in Block 1. Block 1 says no source exists;
  "I couldn't get to the source" is a different statement, and collapsing the
  two turns your own blocked access into an accusation against the author.
- **Asked to confirm the document is fine, or to clear it fast before a
  deadline** → refuse the framing. A clearance produced to reach a predetermined
  verdict is worth nothing. Offer to clear the top N claims instead — that
  limits scope honestly rather than limiting rigor.

## Further reading in this folder

- `reference/fact-base-shape.md` — the five clearance levels and how each may be
  attributed, plus the fact base template
- `reference/failure-modes.md` — five ways a clearance passes a claim it should
  have caught, and which rule above catches each
- `examples/architecture-claim.md` — a worked fact base that caught a 7×
  overstatement in a project's own README
