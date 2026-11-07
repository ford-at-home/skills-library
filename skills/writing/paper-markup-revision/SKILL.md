---
name: paper-markup-revision
description: Apply edits marked by hand on a printed draft back into the source file, resolving every positional reference to an exact block or refusing to guess. Covers printing with deterministic S{n}P{m} margin anchors, the mark vocabulary, the resolution order, and an unresolved file no instruction can be dropped from silently. Use after marking up a printout, dictating changes against a paper copy, or transcribing red-pen edits. Trigger phrases include apply my edits, I marked up the printout, merge my dictated changes, here are my markup notes, v2 with my edits, apply the red pen. Not for rewriting a draft in a voice and not for proofreading.
---

# Paper Markup Revision

Get hand-marked paper edits into a file without retyping them, and without the
agent inventing where they go.

Two channels, and the split is the whole method:

- **Paper carries the address and the intent type.** Marks are cheap: a symbol,
  a short uppercase token, a circled number.
- **Speech or typed notes carry the content.** Anything longer than two words
  belongs there, not on the page.

The agent never sees the page. Marks reach it as text — typed out, or read aloud
in the dictation. Everything below is about making that text resolve to an exact
location.

## Use when

- A printout has been marked up and the changes have to land in the file
- Edits were dictated against a paper copy while walking, driving, or away from
  a keyboard
- Someone else's red pen has to be applied to your draft
- Several marked-up sources are being pulled into one new piece

## Don't use when

- No marks exist and the request is "make this better". That is a voice and
  structure pass — use `voice-faithful-drafting`.
- The message is operational and needs to get shorter before it ships. Use
  `operational-message-friction`.
- The dictation is a full rewrite of a passage. Just replace the passage.
- Claims need checking. This skill applies instructions; it does not verify them.

## Inputs

```yaml
draft:           # path to the file that was printed. Required
printed_version: # git SHA, timestamp, or "unchanged since printing". Required
marks:           # list of "<mark> at <location>", typed or read aloud. May be empty
dictation:       # the spoken or typed instructions, verbatim. Required
voice:           # path to a voice file, or "none". Needed only by prose-generating
                 # directives (DEEPEN, HOOK, LAND, ASIDE, SCENE, CLAIM)
output:          # path for the new version. Default: <draft>.v2.md, auto-incrementing
```

**If `draft` is missing, stop and ask for the path.** Do not work from a pasted
excerpt; positional references resolve against the whole document or not at all.

**If `printed_version` says the file changed since printing, stop.** Every anchor
on that paper refers to the version that was printed. One inserted paragraph
shifts every anchor after it, and the resulting edits look successful.

**If `marks` is empty and the dictation contains no positional references,** this
is a rewrite request, not a markup pass. Say so.

## Printing and the anchor rule

`assets/print-anchors.css` is authoritative: it carries the counting rule an
agent must reproduce to resolve `S4P3`, and the pandoc command that produces the
printable page. Both are in `reference/print-anchors.md`.

If your count and the printed labels disagree, stop and report the discrepancy.
Do not renumber to make an instruction fit.

## What is verified

The counting rule and page geometry come from a print implementation with an
automated fidelity suite that reads anchors back out of a real PDF. The standalone
adaptations here — unscoped selectors, OS fonts, pandoc's title blocks and
figures — were not rendered while they were written. Which parts are which, and
how to check them yourself, is in `reference/print-anchors.md`.

Page breaks are machine-dependent because OS fonts drive line breaking. Anchors
are not: the counters never reference the page number, so `S4P3` means the same
block everywhere. Only "page two" style references depend on which machine
printed.

## Mark vocabulary

Six symbols (`✓ ✗ ~ ★ → ?`), numbered handles, one highlighter colour, and the
uppercase directives. Paper carries the mark; dictation carries the content.
Which marks need dictated content, and which directives need a voice file, is in
`reference/mark-vocabulary.md`.

## Resolution order

For each instruction, try these in order and stop at the first that matches:

1. **Block anchor** — "section 4 paragraph 3", "S4P3", "section 4" for a heading.
2. **Numbered handle** — "mark three", "item 3".
3. **Symbol class** — "all the strikethroughs", "the question marks".
4. **Content** — "the bit about ownership". Fuzzy match against the prose.

Tie-breaks:

- **Same reference plausible under two methods** ("mark three" could be `S2P3` or
  handle ③) → take the block anchor, and say so in the change log.
- **One clearly best candidate under a method** → apply it and name the runner-up
  in the change log, so the next pass can override.
- **Two candidates equally plausible** → do not choose. Both go to
  `unresolved.md` with the instruction and both candidates.

## Process

1. **Confirm the draft is unchanged since printing.** If not, stop.
2. **Read the whole draft and build the block index** — every block in document
   order with its `S{n}P{m}` label. Build it once, before applying anything.
3. **List every instruction** from the marks and the dictation before applying
   any of them. One line per instruction. This is the checklist the run is
   audited against.
4. **Resolve each instruction** by the order above. Record the method that
   matched.
5. **Apply surgically.** Only what was asked. Do not restructure, re-voice, or
   fix an adjacent sentence that is bothering you.
6. **Handle contradictions by surfacing both** ("keep mark three" and "cut mark
   three") — never by picking the later one.
7. **Handle unaddressed marks.** A symbol with no dictation gets its default
   action if it has one (`✓`, `✗`). A `~` or `★` with nothing said about it goes
   to `unresolved.md`. A handle the dictation never mentioned goes there too.
8. **Write the new version to a new file.** Never edit the printed draft.
9. **Write `unresolved.md` even when it is empty.**
10. **Reconcile.** Every instruction from step 3 appears exactly once in either
    the change log or `unresolved.md`.

## Output

Two files: `<draft>.v2.md` (auto-incrementing) and `unresolved.md`, written every
run even when empty. The report format is `reference/output-shape.md`.

## Hard rules

These are rules rather than advice because each failure they prevent produces a
clean v2 with a plausible change log — nothing downstream signals that one was
violated.

```text
Never modify the file that was printed.
Every instruction lands in the change log or in unresolved.md. There is no
  third outcome.
unresolved.md is written even when empty.
Never renumber blocks to make an instruction fit.
Never invent an example, source, or accent layer.
Never resolve a contradiction by preferring one side.
Anchors belong to the printed version. A changed draft invalidates the paper.
Apply only what was marked.
```

## Stop instead of guessing

- **Draft changed since printing** → stop. Re-print and re-mark, or have the user
  confirm the anchors still hold. Applying shifted anchors produces edits in the
  wrong paragraphs that read as successful.
- **Your block count disagrees with a cited anchor** (dictation says `S7P2`,
  the document has six sections) → stop and report the mismatch. Do not fall back
  to content matching to rescue it.
- **Two equally plausible targets** → unresolved, both named. Do not pick.
- **A symbol with no referent** — a floating `~` in a margin with nothing
  underlined → ask one question naming the page.
- **Prose-generating directive with no voice file and no dictated content** →
  unresolved. `DEEPEN` with nothing said is not an invitation to choose a style.
- **Dictation is garbled at the point of an instruction** → unresolved, quoting
  the garbled span. Do not reconstruct intent from the surrounding words.
- **Asked to apply the obvious ones and skip the rest** → apply them, and still
  write every skipped instruction into `unresolved.md`. Skipping quietly is the
  failure this skill is built to prevent.

## Further reading in this folder

- `reference/print-anchors.md` — the pandoc command and print settings, and the
  authoritative block-counting rule the `S{n}P{m}` labels follow
- `reference/mark-vocabulary.md` — the six symbols, numbered handles, and the
  full directive table with which ones require a voice file
- `reference/output-shape.md` — the v2 report format, and why every change log
  line names the resolution method that matched
- `reference/failure-modes.md` — seven ways this produces a clean v2 that is
  wrong, including the one it exists to catch
- `assets/print-anchors.css` — the print stylesheet. Authoritative for the
  counting rule; do not edit it to make a count fit
