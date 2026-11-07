# Printing with anchors, and the counting rule

## Printing with anchors

Copy `assets/print-anchors.css` next to the draft, then:

```bash
pandoc draft.md --standalone --css print-anchors.css -o draft.print.html
```

Open `draft.print.html` and print it. Every addressable block gets a small
`S{n}P{m}` label in the left margin, so nothing has to be written on the page to
point at a block. On screen the document renders as a Letter sheet with the same
margins it will print with, so what you see is where the lines will break.

Print settings: paper size **Letter**, margins **Default** (so the stylesheet's
own page margins apply), browser headers and footers **off**. Background graphics
can stay off — anchors are forced to print regardless, while the shading on code
and table headers drops out, which is what you want on a page you will write on.

Do not pass `--metadata title=…` (emits a title block that would take the `S1`
slot) or `--section-divs` (disturbs the counter scoping).

One pandoc gap: an image alone in a paragraph *with* alt text becomes a figure and
correctly takes no anchor, but with empty alt text (`![](x.png)`) pandoc emits a
bare paragraph that does take one. CSS cannot tell that apart from a paragraph
with an inline image and real prose, so it is not fixable in the stylesheet. Give
standalone images alt text, or count that paragraph as a block.

## The anchor rule

`assets/print-anchors.css` is authoritative. Count blocks the same way its
counters do, in document order, continuous across pages:

- **`S{n}`** increments on every heading, `h1`–`h6`. The heading is labeled
  `S{n}` alone. It *is* the section, not a block inside it.
- **`P{m}`** increments on every non-heading block and resets at each heading, so
  the first block after a heading is `P1`.
- The section counter starts at 0, so the document's first heading is `S1`.
  Content before that first heading is `S0P1`, `S0P2`, …

**Counts as a block:** paragraphs, headings, blockquotes (the whole quote is one
block, however many paragraphs are in it), code blocks, tables.

**Does not count:**

- List items, and anything nested inside one — including the paragraphs that a
  *loose* list item wraps its text in, and including code blocks and tables
  inside an item. A list is addressed by the blocks around it or by content.
- Anything nested inside a blockquote: its paragraphs, code blocks, tables, and
  nested quotes. The quote is one block.
- Block content inside a table cell. The table counts once.
- Images, figures, horizontal rules, inline elements, and a generated title
  block.

If your count and the printed labels disagree, stop and report the discrepancy.
Do not renumber to make an instruction fit.

## What is verified

The counting rule and page geometry in `assets/print-anchors.css` are taken from a
print implementation that has an automated fidelity suite: it renders fixtures in
real Chromium, prints them to PDF, reads the anchors back out of the PDF text
layer, and compares them against an independent reference implementation of the
same rule. Its fixtures cover loose lists, code and quotes nested inside list
items, code and tables nested inside quotes, consecutive headings, content before
the first heading, and a document with no headings.

The distinction matters, so state it precisely:

- **Verified by reading a passing test elsewhere:** the counting rule, the split
  left margin, `counter-set` on headings, the nesting exclusions.
- **Not verified by running anything.** This stylesheet was not rendered by a
  browser or driven through pandoc while it was written. The adaptations —
  unscoped selectors, OS fonts, and pandoc-specific handling of title blocks,
  figures, and table cells — are reasoned, not tested.

To verify it: run the pandoc command above on a draft containing a loose list, a
quote with two paragraphs, a fenced block inside a list item, and at least three
headings; print to PDF; check that labels are continuous, that the first block
after each heading is `P1`, and that nothing nested inside a list item or quote
carries a label.

Using OS fonts makes **page breaks** machine-dependent, since font metrics drive
line breaking. **Anchors are not:** the counters run continuously in document
order and never reference the page number, so `S4P3` means the same block
everywhere. Only "page two" style references depend on which machine printed.
