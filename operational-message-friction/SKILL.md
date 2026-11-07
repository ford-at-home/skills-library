---
name: operational-message-friction
description: Score one unsent operational message against a five-component friction rubric, then compress it only if the score earns a rewrite. Covers the four structural moves every working message needs, per-component bands, channel length targets, and the relationship and audience flags that scoring alone misses. Scores a draft for its reader's cost, not model output or submissions. Use before posting a Slack update, sending an announcement, writing a handoff, or asking for a decision by email. Trigger phrases include score this, friction check, how bad is this, where is the friction, is this too long for Slack, tighten this message, make this Slack-ready, compress this before I send it. Not for essays, posts, or anything where density is the point.
---

# Operational Message Friction

Score a working message, then compress it only if the score justifies it.

The premise: **the cognitive cost of a message is roughly fixed, and it is split
between the sender who edits and the readers who decipher.** Editing is paid
once. Deciphering is paid by everyone, every time. An unedited message to forty
people is a tax.

Scoring first exists so the rewrite has a reason. Rewriting first produces a
shorter message and no argument for why the old one was worse.

## Use when

- A message is about to go to a channel, a mailing list, or someone's inbox
- Someone asks whether a message is too long, too dense, or too buried
- A handoff, announcement, or decision request needs to actually land
- A draft has been through several hands and has grown

## Don't use when

- The piece is an essay, post, or narrative. Density is load-bearing there. Use
  `voice-faithful-drafting`.
- It is a proposal, RFC, or strategy memo that is long by design. Confirm before
  applying this at all, and say plainly that depth may be the point.
- The content is emotionally loaded or personally affecting. That is a
  conversation, not a well-structured message. Say so instead of compressing it.
- A whole rollout needs sequencing across channels and audiences. Use
  `communication-rollout-planning`.

## Inputs

```yaml
message:   # the draft, verbatim. Required
channel:   # where it goes. Inferred and labeled if absent
audience:  # size, whether it is a subset of a known group, and how each segment
           # stands toward the sender: ally, neutral, skeptic, adversary
deadline:  # what the sender needs back, and by when
voice:     # path to a voice file, or "none". Compression preserves voice when given
mode:      # score | score-and-compress. Default: score, then ask
```

**If `channel` is absent, infer it from length and register and label the
inference.** Never score channel fit against an unstated assumption.

**If `audience` is absent,** score the five components anyway, and list the flags
you could not check rather than declaring the message clean. Four of the flags
below are audience-dependent and invisible in the text.

**If `deadline` is absent,** that is usually the finding: an unstated response
expectation is the most common defect in these messages.

## The four moves

Every working message has four. Name them explicitly when scoring.

| Move | Does | Common failure |
|---|---|---|
| **Pulse** | Opening signal: what is new and why it matters | Missing; the message opens with history |
| **Catalyst** | The specific ask | Buried in the last paragraph, or absent |
| **Context** | The minimum needed to act on the ask | Everything the sender knows |
| **Handoff** | The stated response expectation | "Thoughts?" |

Context is the one that inflates. It is not background; it is what a reader needs
in order to do the thing being asked.

## Friction score

Five components, 0–20 each. Lower is better. Sum to 100: **Buried Catalyst**,
**Scent Trail**, **Metabolic Density**, **Handoff Clarity**, **Channel Fit**.
What a 0 and a 20 look like on each, the bands inside each component, and the
channel length targets are in `reference/scoring-bands.md`.

### What the total means, and what to do about it

| Total | Reading | Action |
|---|---|---|
| 0–20 | Clean signal | **Ship it. Refuse the rewrite** and say why |
| 21–40 | Minor friction, usually the ask or the handoff | Targeted fixes only, named individually |
| 41–60 | Meaningful friction | Compress |
| 61–80 | High friction; readers will defer or miss the ask | Compress |
| 81–100 | Signal collapse | The channel is probably wrong. Recommend escalating or moving it before rewriting |

These bands are a convention, not a measurement. They exist so that "too long"
becomes an arguable claim with a number attached, and so two people scoring the
same message land close. Do not present them as validated.

## Flags

Scored separately from the total. The first four are invisible in the text and
require knowing the audience.

- **Cold Signal Risk** — efficient but too lean for the relationship distance.
  One line of warmth fixes it; more is patronizing.
- **Visibility Tax** — a permanent, searchable artifact in a venue larger than
  the content warrants. It gets forwarded and read later out of context.
- **Exclusion Signal** — a subset of a known group is being addressed, and the
  slice carries meaning. Name why this slice, or send the omitted people a note.
- **Valence Mismatch** — the register assumes a warmer or colder relationship
  than exists. A lean message to a reluctant collaborator reads as an order.
- **False Scent** — the Pulse misrepresents the body. Worse than no Pulse; it
  doubles the reader's cost.
- **Duplicate Broadcast** — the same message in several busy channels. Pick one.
- **Terminal Investment** — urgency signalling that reads as frantic rather than
  clear. Usually the sender is overloaded and the message should be deferred.

## Process

1. **Identify the channel.** State it, and whether it was given or inferred.
2. **Locate the four moves** in the draft. Name any that are missing.
3. **Score each component against the bands** in `reference/scoring-bands.md`.
   Quote the passage that drove each score. A score you cannot attach to a
   passage is a guess.
4. **Compute average words per sentence and total word count.** Show both.
5. **Check the flags.** Check the first four explicitly whenever the audience is
   30 or more, is a subset of a known group, or contains anyone who is not an
   ally or neutral. List the ones you could not check.
6. **Sum, band, and diagnose in two to four sentences** naming the single
   dominant source of friction. Not a list.
7. **Decide by band.** At 0–20, stop and say the message is fine. Above it,
   compress per the band's action.
8. **Compress, in this order:** lift the Catalyst to the top and make it visually
   distinct; add a Pulse; break prose into bullets and bold the anchors; cut
   words that do not advance the ask; state the Handoff with a deadline; check
   the length against the channel; add one line of warmth if relationship
   distance warrants it.
9. **Re-score the rewrite** and report both numbers. A rewrite that does not move
   the score has not done anything.
10. **Verify nothing was lost.** Every named person, date, number, commitment,
    and link from the original is present or explicitly flagged as dropped.

## Hard rules

Each of these prevents a failure that produces a plausible-looking score or a
plausible-looking rewrite. That is why they are rules rather than advice —
nothing downstream signals that one was violated.

```text
Score before rewriting. Always report both scores.
Every component score cites a passage.
Metabolic Density and Channel Fit show their numbers.
Never invent context, a deadline, or a decision the sender did not state.
Never drop a named person, date, number, or link without flagging it.
Compress the packaging, never the position. A hedged claim is a changed claim.
Do not double-penalize: a buried ask is not also a Scent Trail failure unless
  the formatting is independently weak.
```

## Stop instead of guessing

- **Score is 0–20 and a rewrite was requested** → refuse and explain. A
  near-identity rewrite that looks like work is worse than no rewrite: it teaches
  the sender that every message needs processing.
- **Score is 81–100** → the problem is usually the channel, not the prose. Say
  which channel it belongs in before compressing.
- **The message is emotionally loaded or personally affecting** → stop. Compressed
  bad news reads as cold. Recommend a conversation and offer to draft the written
  recap that follows it.
- **The ask cannot be found** → do not infer one. Ask what the sender needs back.
  A message with no ask usually should not be sent.
- **Context is missing that the message depends on** — a link, a date, a decision
  that has not been made → leave a `[link]` or `[date]` placeholder, list it, and
  do not fill it.
- **Audience is a subset of a known group and you were not told why** → ask one
  question. This flag cannot be resolved from the text.
- **It is a 1500-word document** → confirm this is the right lens before scoring.
- **Asked for a friction score to justify a rewrite already decided on** → refuse
  the framing. Score it honestly; if it comes back clean, that is the answer.

## Further reading in this folder

- `reference/scoring-bands.md` — the 0 and 20 poles for each of the five
  components, the bands inside each, and the per-channel length targets
- `reference/output-shape.md` — the score table, flags, diagnosis, rewrite, and
  preserved-items sections in full
- `reference/failure-modes.md` — seven ways friction scoring produces a useless
  or damaging result, including symmetric scoring and compressed bad news
