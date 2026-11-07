---
name: communication-rollout-planning
description: Sequence a multi-channel announcement into an ordered plan of communication moves with draft copy for each, ordered so nobody who matters hears it from a broadcast. Covers audience size bands, composition, how each segment stands toward the sender, which move fits which purpose, and the ordering rules that decide what has to happen before the broadcast. Use when planning a launch, reorg, policy change, decision, migration, or any announcement with stakeholders. Trigger phrases include comm plan, how should I roll this out, plan the announcement, who do I need to tell first, sequence this rollout, launch plan, change management. Not for drafting or scoring one message.
---

# Communication Rollout Planning

Turn one announcement into an ordered set of moves, each with draft copy, ordered
so that the people who will be asked about it are not learning it from a
broadcast.

The output is a plan the sender executes. This skill never sends anything.

## Use when

- An announcement has stakeholders who need to hear it before everyone else
- A change affects specific named people
- A decision needs alignment across teams before it is public
- A launch, migration, or policy change needs more than one message
- Someone asks who to tell first

## Don't use when

- One message to one audience, no stakeholders, nothing sensitive. Do not
  manufacture a plan.
- A single message needs to get shorter or clearer before sending. Use
  `operational-message-friction`.
- The question is only which of two channels to use. Answer it directly.
- The decision being announced has not actually been made. Then the plan is
  fiction; the work is making the decision.

## Inputs

```yaml
topic:            # what is being communicated, 1–3 sentences. Required
outcome:          # awareness | alignment | decision | execution. Required
audience:         # segments, each with size, composition, and valence
                  # (see reference/axes-and-moves.md)
timeline:         # the broadcast date, and when the outcome must land
sensitivity:      # low | medium | high. Political or emotional angles named
subjects:         # people the content is *about*, as opposed to people being
                  # told about it. Empty is a valid answer, but ask
artifacts:        # docs, recordings, decks that already exist
feedback:         # one-way | open comments | live discussion | ongoing channel
profile:          # path to a filled org profile. See templates/comms-profile.md
```

**If `outcome` is missing, stop and ask.** Awareness and decision produce
different plans from the same topic, and the difference shows up in every move.

**If `subjects` was never asked about, ask before planning.** Someone who learns
from a broadcast that a change is about them is the failure this skill exists to
prevent, and it is unrecoverable.

**If `profile` is missing,** run with what the user tells you, name every channel
and segment as unverified in the plan, and say the plan is uncalibrated. Do not
invent an org's channels, meeting cadences, or norms.

## Axes and moves

Every segment is classified on three axes — size band, composition, and valence —
and those three decide which move fits. The bands, the composition and valence
vocabularies, and the sixteen-move library with what each is good for and when to
avoid it are in `reference/axes-and-moves.md`.

## Ordering rules

Apply in this order. The first two override everything else, including cost
ordering.

1. **Subjects first.** Anyone the content is *about* gets a 1:1 conversation
   before any DM or broadcast. Non-negotiable.
2. **Adversaries before the heads-up round.** A sync conversation with an opposed
   segment comes before anything is sent. Broadcasting first to someone whose
   interests you are cutting against is an ambush.
3. **Skeptics get a heads-up DM before the broadcast**, regardless of how low the
   sensitivity scored. A skeptic who learns from a broadcast becomes an adversary.
4. **Stakeholders get heads-up DMs** when sensitivity is medium or high, or when
   the profile says a preview is expected.
5. **The durable artifact exists before anything points at it.** Never schedule a
   meeting before the document it discusses.
6. **Then broadcast**, sized to the audience: ≤20 a channel update; over 20 or
   cross-team a restricted announcement plus a contextualized update in each
   affected team's own channel; external or formal, email.
7. **Then sync reinforcement, only if the outcome needs it.** Awareness needs at
   most a meeting mention. Decision needs a dedicated or follow-up meeting.
   Execution with many unknowns needs office hours.
8. **Close with a named checkpoint** — a feedback channel, a follow-up date, or a
   recap deadline. A plan that ends at the broadcast has no ending.

Three adjustments that are easy to miss:

- **Subset of a known group** → either the copy names why this slice ("sending to
  just the three of you because…"), or the omitted stakeholders get a parallel
  note. Otherwise flag the exclusion in Risks. It will leak.
- **Mixed valence in one audience** → segment the plan. One message to allies and
  skeptics fails for one of them. Different copy, different channels.
- **Audience at `org` or above** → public-record register. Strip casual asides.
  At `huddle` and ally-dominated, skip the warmth ceremony; it reads as padding.

## Process

1. **Read the profile.** Every run, not from memory. State the assumptions you
   are taking from it rather than re-asking.
2. **Ask the intake gaps only.** Topic, outcome, audience with all three axes,
   timeline, sensitivity, subjects, artifacts, feedback loop.
3. **Classify each segment** by size band, composition, and valence. Write the
   classification down; it drives every later choice. See
   `reference/axes-and-moves.md`.
4. **Select moves** by outcome and audience, then **order them by the rules
   above.**
5. **Draft copy for every move.** Each carries the four working moves — what is
   new, the ask, the minimum context, and the stated response expectation —
   except the 1:1 conversation, which opens relationally and gets a script rather
   than a message.
6. **Check the plan against the profile:** no off-limits channel, no invented
   segment, no channel the sender cannot post in.
7. **Name the risks,** including the ones the plan does not solve.
8. **Count the moves.** Three is often right. If you have seven, cut.

## Output

A plan document: header, an at-a-glance table, a move-by-move section carrying
draft copy for each move, why this shape, and risks. The template is
`reference/plan-shape.md`.

## Hard rules

These are rules rather than advice because each failure they prevent produces a
well-formed plan — the defect is invisible in the artifact and surfaces only once
the plan has been executed, when it is no longer recoverable.

```text
Subjects of the content are told in person, first. No exceptions.
Never broadcast first to an adversary or skeptic segment.
Never invent a channel, a segment, a meeting cadence, or an org norm.
Never invent a fact about the topic. Placeholders stay placeholders.
Never use a channel the profile marks off-limits or the sender cannot post in.
```

## Stop instead of guessing

- **Outcome not stated** → stop and ask. It determines the whole shape.
- **Never asked who the content is about** → ask before planning anything.
- **Sensitivity is high and valence is unknown** → ask. The ordering rules are
  entirely valence-driven; a plan built without it is ordered by guess.
- **The decision has not been made** → stop. You cannot sequence the announcement
  of a decision that does not exist. Offer to plan the decision meeting instead.
- **The sender wants to skip the 1:1 and let the broadcast do it** → refuse, and
  say what it costs. This is the one refusal worth spending goodwill on.
- **A channel or segment appears in the intake but not the profile** → flag it
  inline in the plan and ask whether to add it. Do not silently adopt it.
- **The rollout is genuinely one message to one person** → say so and draft the
  message. A three-move plan for a one-move situation trains the user to ignore
  the output.
- **Timeline cannot fit the notice periods the profile requires** → say which
  move gets compressed and what that risks. Do not quietly drop it.

## Further reading in this folder

- `reference/axes-and-moves.md` — the size bands, composition and valence
  vocabularies, and the move library with reach and when to avoid each
- `reference/plan-shape.md` — the plan template, and why draft copy carries
  placeholders rather than plausible values
- `reference/failure-modes.md` — six ways this produces a well-formed plan that
  fails on execution, including the one it exists to catch
- `templates/comms-profile.md` — the org profile the planner reads every run:
  segments, channel map, cadences, conventions, known skeptics
