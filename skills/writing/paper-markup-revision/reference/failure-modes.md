# How this goes wrong

Every one of these produces a clean v2 with a plausible change log. That is why
the corresponding rules in SKILL.md are rules and not preferences — nothing
downstream signals that one was violated.

**The one it exists to catch.** An instruction that cannot be matched gets
dropped. The output is a clean v2 with a plausible change log, and the missing
edit surfaces weeks later as something the writer thought they had fixed. This is
why unresolved is a file that is always written, rather than a section that
appears when needed.

**Stale anchors.** The draft was edited after printing. Every anchor past the
insertion point is off by one block. Nothing errors; the edits land one paragraph
away from where they were meant to.

**Miscounting blocks.** A four-paragraph quote counted as four blocks instead of
one. Every anchor after that point is off, and the edits still look applied.

**The loose-list trap.** A list whose items are separated by blank lines is a
*loose* list, and the renderer wraps each item's text in a paragraph
indistinguishable from a body paragraph. Count those and every anchor after the
first loose list is off by one. Same trap for a fenced block or table inside a
list item, or inside a blockquote. Nesting decides addressability, not the tag.

**Scope creep under a `~`.** "Rework this sentence" becomes a rewritten
paragraph, because the surrounding prose was easy to improve. The writer now has
to diff their own draft to find out what happened.

**Invented accents.** `DEEPEN` with silent dictation produces a stylistic choice
the writer never asked for, and it is the most convincing part of the output.

**Contradiction resolved by recency.** The dictation says cut, then later says
keep. Taking the later one is a guess about which one the writer meant, dressed
as a rule.
