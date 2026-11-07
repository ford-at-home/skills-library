---
name: decision-prose-linting
description: Tighten a decision-bearing draft — memo, brief, proposal, status narrative — without making it more confident than the author was. A removed hedge must be replaced by an explicit uncertainty tag rather than left as a bald assertion, and every removal is logged in a ledger so the author can confirm nothing load-bearing was lost. Never invents a number, an owner, or a date to satisfy its own rules. Use when a draft is going to a reviewer who will ask how you know. Trigger phrases include tighten this, lint this doc, remove the fluff, make this evidence-based, edit this memo, this reads like marketing, cut the weasel words, before I send this to leadership.
---

# Decision Prose Linting

Rewrite a decision-bearing draft so it survives a reviewer asking "how do you
know?", and hand back a ledger of everything you changed.

## The two rules that make this different from editing

Everything else here is ordinary copy-editing. These two are not, and they are
the reason the skill exists.

**1. Removing a hedge strengthens the claim.** "We believe conversion will
improve" becomes "conversion will improve" — cleaner prose asserting something
the author never asserted. Cutting fluff is the default behavior when someone
says "tighten this", and it silently manufactures confidence. Every hedge you
remove is replaced by an explicit tag, not by nothing:

| Tag | Meaning |
|---|---|
| `[fact]` | Verifiable, with a source |
| `[assumption]` | Believed true, untested |
| `[inference]` | Derived from facts already established above |
| `[open question]` | Listed in an explicit Open Questions section |

**2. Nothing leaves without a receipt.** Every removed word or phrase appears in
a Removed Fluff table with its reason. An edit pass that cannot show what it took
out is indistinguishable from one that took out the load-bearing qualifier, and
the author cannot check it by reading the result — the result reads fine. That is
what makes the loss silent.

## Use when

- A draft is about to go to a reviewer, a decision-maker, or a board
- Commitments appear in the prose with no owner and no date
- Someone asks for the fluff to be cut

## Don't use when

- Nothing is drafted yet. This edits prose; it does not structure an argument
- The piece has to sound like a specific named person, governed by a brief
  stating persona, throughline, and channel. Use `voice-faithful-drafting`. That
  skill is loyal to a voice; this one is loyal to a rule set and will flatten a
  voice to enforce it
- The piece is an operational message — chat post, announcement, handoff — and
  the question is whether the reader will act on it. Use
  `operational-message-friction`. This skill does not care how long the document
  is; it cares whether each sentence is defensible
- Claims need sourcing rather than flagging. This skill marks a claim as needing
  evidence; it never researches. Use `evidence-grounded-verification`
- The target is AI-writing tells and register rather than defensibility. That is
  a different rule set
- The draft is a private note or journal. The rules assume a reviewer exists
- The goal is to make the prose more persuasive. Say so and stop

## Inputs

```yaml
draft:        # the raw prose. Required, verbatim
audience:     # who reads this, and what they can check.
              # "the VP who owns the budget line" — not "leadership"
known_facts:  # optional. Facts the rewrite may state without flagging
```

If `audience` is missing, ask. Decision relevance is defined relative to a
reader; without one, "so what?" has no answer.

## The rule set

Fixed. Do not soften or extend it per document.

**Rewrite these.** Vague quantifiers used without a metric (significant,
substantial, meaningful, robust, scalable, seamless, frictionless,
best-in-class). Hedges standing in for evidence (we believe, we think, it seems,
we expect without a number, likely or probably without a probability). Passive
evasions (mistakes were made, issues occurred, the system experienced a
degradation). Unsupported collective claims (customers love, users prefer, the
market wants, everyone agrees). And *simple*, *obvious*, *clear*, *easy* unless
the qualifier — what makes it simple, to whom it is obvious — is present.

Adjectives that carry a measurement are not targets. "Three-week rollout" and
"world-class rollout" are not the same problem.

**Require these.**

| Element | Requirement |
|---|---|
| Every empirical claim | Exactly one assumption tag |
| Every metric | Baseline, target, measurement method, time to evaluate |
| Every commitment | Owner, action, date |
| Every comparative | A baseline — "30% faster" than what? Add it, or mark `[open question]` |
| Every section | A "so what?" sentence naming what the reader should decide or do |

## Process

1. **Read the whole draft once** before changing anything, to find the argument.
   Linting sentence-by-sentence from the top produces locally clean prose that
   has lost the thread.
2. **Classify each sentence**: keep, rewrite, strike, or flag for evidence.
3. **Rewrite, preserving the original meaning.** Where a rule and the meaning
   conflict, the meaning wins and the conflict goes in the ledger.
4. **List every claim that needs evidence**, separately from the rewrites. A
   claim that cannot be supported becomes `[open question]` — never a deletion,
   never an invented number.
5. **Log every removal** with its reason.
6. **Second pass over the rewrite**, not the original: every commitment has an
   owner and a date; every comparative has a baseline; every "we believe" is
   either cited or relabeled; no number appears that was not in the original or
   in `known_facts`.

## Output

Six sections: Rewritten Version, Claims That Need Evidence, Removed Fluff, Rule
Conflicts, Open Questions, Decision-Relevant Summary. The template is
`reference/output-shape.md`.

The Rule Conflicts table is empty in most runs. When it is not, it is the most
useful part of the output.

## Hard rules

These are rules rather than advice because each failure they prevent produces a
cleaner-reading document — nothing in the result signals that one was violated.

```text
Never remove a hedge without leaving a tag or a flagged claim in its place.
Never remove a phrase without listing it in the Removed Fluff table.
Never invent a number to satisfy "metric required". Mark it [open question].
Never add an owner or a date the author did not supply.
Never delete a claim to make it pass. Surface it as needing evidence.
Never modify the source document. Emit the rewrite separately.
```

## Stop instead of guessing

- **Draft is fewer than three sentences** → too little to lint. Say so.
- **Draft is a personal note or journal** → say so and stop.
- **No audience given** → ask once.
- **A claim needs a number nobody has** → `[open question]` with the owner blank
  and the gap named. Never estimate.
- **A commitment has no owner** → flag it. Do not assign one, including to the
  author, and including when the author is obvious.
- **Asked to make the prose more persuasive, more confident, or more exciting**
  → refuse the framing explicitly. That is the inverse of this skill's job.
- **Asked to confirm the draft is already fine** → decline the framing. Run the
  rules and report what they find, including "no violations found" if that is the
  honest result.

## Further reading in this folder

- `reference/output-shape.md` — the six-section output template, and why the
  Removed Fluff and Rule Conflicts tables are the auditable parts of it
- `reference/failure-modes.md` — three ways this produces a document that reads
  better than the one it replaced and is worse
