---
name: voice-faithful-drafting
description: Draft, rewrite, or weave a long-form piece in one named person's voice, governed by a required brief stating persona, throughline, channel, and stakes. Refuses to run without the brief, and refuses to infer persona or throughline from the source material. Use when rewriting a draft in someone's voice, elevating notes or a transcript into a publishable piece, weaving several sources into one post, or producing one piece for several channels. Trigger phrases include rewrite this in my voice, tighten this draft, refactor this post, elevate these notes, polish this, weave these into a post, compose from these sources, make this publishable. Not for operational messages, proofreading, or fact-checking.
---

# Voice-Faithful Drafting

Turn source material into a finished piece that sounds like a specific person and
lands on a specific reader.

The governing input is a **brief**. Without it, "tighten", "elevate", and "make
this better" are preferences. With it, they are tests you can fail.

**Bullshit, operationally defined:** any sentence that does not move *this
persona* toward *this throughline*. The brief is what makes that judgement
checkable rather than a matter of taste.

## Use when

- A draft, transcript, or pile of notes has to become publishable prose
- Several sources have to become one piece with one argument
- The same piece has to ship to more than one channel
- The substance is settled and the voice and structure are not

## Don't use when

- The message is operational — a Slack post, status update, handoff, or
  announcement. Density is a defect there, not a feature. Use
  `operational-message-friction`.
- The edits were marked by hand on a printed page. Use `paper-markup-revision`.
- Only typos and grammar need fixing. This skill restructures.
- Claims need checking or sourcing. This skill never verifies and never
  researches; it marks gaps and stops there.
- Nobody can say who the reader is or what they walk away with. Then the brief
  is the work, and the drafting is premature.

## Inputs

Ask for these. Never infer them.

```yaml
brief:      # path to a filled brief. Five fields, all required. See templates/brief.md
voice:      # name or path of a voice file, from the brief's Voice field
channels:   # one or more channel definitions, from the brief's Channels field
sources:    # markdown/text files to draw from, or "none"
output_dir: # where the bundle lands. Default: output/<piece>/<channel>/
```

**If `brief` is missing, stop.** Do not assemble one from the sources. The brief
exists to carry the two things source material cannot tell you — who this is for
and what it does to them — and a brief reverse-engineered from the sources agrees
with the sources by construction.

**Voice resolution.** A bare name resolves as `./.voices/<name>.md`, then
`~/.voices/<name>.md`. The paired anti-slop file `<name>.anti.md` beside it is
loaded whenever it exists. A path is used as given.

**Channel resolution.** Same order: `./.channels/<name>.md`, then
`~/.channels/<name>.md`. `templates/channel.md` is the fill-in shape. A channel
carries length as numbers, register, what the platform physically forbids, and the
failure modes specific to that surface — voice belongs to the writer, register
belongs to the channel.

Read all of these on every run. Never work from a remembered voice.

## The brief

| Field | Carries | Failure if vague |
|---|---|---|
| `Voice` | Which voice file to load | Output reads like the model's default register |
| `Persona` | One named human who reads this, not a segment | Prose hedges to survive every possible reader |
| `Throughline` | One sentence: what the persona walks away with | No paragraph can be cut, because nothing can fail |
| `Channels` | Which output formats to produce | Length and register drift to whatever felt natural |
| `Why this persona, why now` | One paragraph of stakes | The piece reads as content rather than as a letter |

The stakes field does the most work and is the one users skip. It is the field
that decides whether the piece needed to exist.

`templates/brief.md` is the fill-in shape.

## Voice is a pair, not a file

A voice is two files that only work together.

- `<name>.md` — identity, piece-level architecture, named signature moves with
  example sentences, named accent layers, cadence, lexicon.
- `<name>.anti.md` — the catalog of tells to scrub: vague authority, hedge
  stacks, throat-clearing, empty connectives, even cadence, and the allergies
  specific to this voice.

Load both every run. The style file alone reliably produces competent generic
prose with the right vocabulary sprinkled on top, because most of voice work is
subtraction. `templates/voice.md` and `templates/voice-anti.md` are the shapes.

Each accent layer needs a name, a trigger, and an example passage. Apply at most
two in a piece, never stacked in one paragraph, and say in the report which ones
you used and where, so the user can recalibrate.

## Process

1. **Read the brief. Validate all five fields have content.** Any empty field →
   stop and name every empty one at once.
2. **Load the voice file and its anti file. Load each channel definition.** Any
   missing → stop, say where it should live, and list what does exist at both
   resolution paths.
3. **Fix the mode from the inputs** and state it: `rewrite` (one draft in),
   `weave` (several sources plus a throughline), `create` (topic only).
4. **Hold persona, throughline, and stakes as the constraint set.** They govern
   every later judgement.
5. **Build the architecture before the prose.** Name the entry, the gap, the
   implication, the closer. If the gap has no name, stop here. See
   `reference/piece-architecture.md`.
6. **Draft, then run the throughline test on every paragraph.** Does this move
   this persona toward this throughline? If not, it is cut, or it becomes a
   question in `tighten.md` — never left in because it reads well.
7. **Scrub against the anti file.** Then check that scrubbing did not flatten a
   deliberate claim into a hedge.
8. **Mark gaps, never fill them.** `[Example needed: …]`, `[Source needed: …]`,
   and one line in `to-research.md` naming where to look.
9. **Write the bundle per channel.** Same persona, throughline, and voice;
   channel supplies length, register, and format. See
   `reference/output-bundle.md` for the directory and the report format.
10. **Leave every input file exactly as it was.**

For `weave` mode, record which paragraph came from which source as you place it.
Reconstructing that afterwards means re-reading every source.

## Hard rules

These are rules rather than advice because each failure they prevent produces a
piece that reads well — nothing downstream signals that one was violated.

```text
No brief, no run.
Never infer persona, throughline, or stakes from the source material.
Never invent an example, quote, statistic, or source. Mark the gap.
Never modify an input file.
Unresolved is a file, not an omission.
Auxiliary files are written even when empty.
A pick the voice file did not specify is reported as a pick.
```

The first two rules are why this exists. Everything else is enforcement.

## Stop instead of guessing

- **No brief** → stop. Hand over the brief template. Do not draft "something to
  react to"; a draft produced without the gate becomes the brief.
- **Empty brief fields** → stop and name all of them in one message, so the user
  fills them in one pass instead of discovering them one at a time.
- **Named voice not found** → stop. Say where it should live, list what exists at
  both paths, and offer two moves: create it from the template, or point the
  brief at a voice that exists.
- **Persona is a segment** ("engineers", "founders", "our customers") → stop and
  ask for one human. This is the most common way a filled-in brief still fails.
- **No nameable gap between public posture and private knowledge** → say so.
  Offer the explainer honestly instead of dressing one up.
- **Source is a PDF, image, URL, or binary** → stop and ask for text. Do not
  fetch, OCR, or approximate.
- **Instructions contradict** ("keep the opening" and "cut the first two
  paragraphs") → surface both, pick neither.
- **Output directory already holds files** → ask before overwriting.
- **Asked to skip the brief just this once** → refuse. A best-effort mode becomes
  the default mode within a month, and then nothing downstream can tell which
  runs were governed.

## Further reading in this folder

- `reference/piece-architecture.md` — the four structural moves a piece needs to
  be doing anything at all, and the two rules that support them
- `reference/output-bundle.md` — the per-channel directory, why the auxiliary
  files are written even when empty, and the report format
- `reference/failure-modes.md` — seven ways this produces a piece that reads
  well and fails anyway, including the one it exists to catch
