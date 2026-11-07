---
name: graph_entity_naming
description: Rules for what a knowledge-graph node may be named after, and an audit script that finds junk labels. Use when writing or reviewing extraction parsers, when a graph shows nonsense node titles, when deciding what becomes an entity versus evidence, or before publishing regenerated graph data.
user-invocable: true
metadata:
  author: built-environment
---

> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../../docs/methodology.md) for details.

# Graph Entity Naming

A node label is the whole interface. Nobody reads provenance for a dot they
cannot identify, so a bad label does not merely look untidy — it removes the
node from use. Every rule below comes from a label that shipped and had to be
fixed at the source.

Run the audit before publishing regenerated data:

```bash
node skills/graph_entity_naming/scripts/audit-labels.mjs                    # this repo
node skills/graph_entity_naming/scripts/audit-labels.mjs <path/to/data>     # any graph dir
```

It exits non-zero when it finds anything, and prints the offending labels with
their pillar and type.

## The rules

### A directory name is not a display name

Title-casing a slug produced `Rva-Plotlines`, `Explorerva`, `Multi-Pillar-Ai`
and `Whats-On-Rva`. Get the real name from wherever humans wrote it down — for
demo projects that is `rvahacks/src/data/ideas.ts` and `idea-content.ts`,
exported into the pillar repos by `npm run kg:names`.

Render the slug only as a fallback, and make the renderer acronym-aware
(`RVA`, `HUD`, `SMS`, `OMBD`, `AI`) so the fallback is at least readable.

### Never name a node after the tooling that produced the research

City Hall's research lives in `_parallel-research/`, named for the AI tool that
generated it. Treating that directory as a project invented a civic proposal
called `" Parallel-Research"` — with a leading space, because title-casing kept
the underscore — that nobody had proposed.

An underscore prefix marks a directory that is **not a project**: `_shared-*`
spans several demos, `_parallel-research` is raw tool output, `_research-answers`
is a different shape entirely.

### Keep the findings, move the anchor

Do not solve a fabricated hub by deleting the directory. `_parallel-research` is
the only post-event research City Hall has, and it contributes twelve real City
services that have no other edge. Dropping it orphans all twelve.

Anchor non-project findings to an `Evidence` node named for **the report**, and
run the edge the other way: a proposal `ADDRESSES` its findings, but a report
only `HAS_EVIDENCE` for them. The weaker claim is the true one.

### A hostname is not an identity

When a citation arrives without a title, falling back to the hostname made
fourteen distinct Open Data URLs render as fourteen identical dots labelled
`data.richmondgov.com`. Include the path. Reserve the bare host for URLs that
genuinely have none.

### Trim after truncating, not before

Slicing a long page title at a fixed width lands mid-word about as often as not
and leaves the label ending in a space. Truncate, then `trimEnd()`, then add the
ellipsis.

### A name field is the subject of a problem, never the problem

A limitations section that led with `Data Source Name` produced a Problem called
`"SeeClickFix Sample Data Aug 2014 to Aug 2015"`. The dataset is what the
problem is *about*; the `limitation` field is the problem.

When choosing a label from a record, prefer the field whose key names the thing
you are modelling (`barrier`, `limitation`, `challenge`, `gap`, `issue`), then
any field that is not a `*_name`, and only then the first value.

### Sentence-shaped findings are evidence, not entities

`"This workaround is highly inefficient, leading to wasted time…"` is a claim,
not a Problem. The extractor demotes sentence-shaped Problem and Need nodes into
`data/evidence.json` as `ev:` records with provenance. That is the right home —
check there before concluding a finding was lost.

The inverse is equally wrong: `"In-Person Visits"` and `"RRHA"` are a workaround
and an organisation, and neither is a problem. If a section yields only subjects
and methods, it is not a problem section.

## Reviewing an extractor change

Ask of every node the parser creates:

1. Would a Richmond resident recognise this name as the thing it points at?
2. Does the name come from a source, or from a filename the pipeline chose?
3. Is the label unique enough to tell two nodes apart?
4. Is this an entity at all, or a sentence that belongs in the evidence layer?
5. If this node disappeared, what would be orphaned?

## Parsing the sources these names come from

Do **not** read structured TypeScript or JSON-ish data with a windowed regex or
a line scanner. Both failed silently here and paired `vecina` with the title of
the next object, shipping `Vecina → "B2GNow CSV Export"` — wrong data that looks
entirely plausible.

Find the anchor, then bound the record by brace matching, and strip nested
objects before reading fields so a child's `title` cannot be mistaken for the
parent's. When a parse yields a suspicious count (89 names for 73 ideas), treat
the arithmetic as the bug report it is.

Better still: key the output off what actually exists on disk — the directories
present in the repo — so a name is only claimed for a project that is really
there, and an unnamed directory is visibly absent rather than quietly guessed.
