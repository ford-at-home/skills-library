---
name: markdown-memory-schema-maintenance
description: Audit and repair the metadata layer of a Markdown notes corpus, one note at a time, so retrieval and confidence calibration can work. Checks required frontmatter fields, enum validity, stale claim caches, supersede chains, broken wikilinks, orphans, and missing uncertainty labels; emits a defect list ranked by retrieval impact plus an append-only repair plan. Never deletes, never backfills a field value it cannot source. Works inside notes; not the corpus-level index or filing scheme (research-corpus-self-indexing), and never answers a question about the notes' subject matter (markdown-knowledge-graph-traversal). Use after a bulk import, before trusting a corpus for grounded answering, or when search keeps missing notes you know exist. Trigger phrases include audit my vault, validate frontmatter, why can't it find that note, my notes are a mess, check my knowledge base for inconsistencies, find orphan notes, fix my metadata, is my schema still valid.
---

# Markdown Memory Schema Maintenance

Keep a Markdown corpus's frontmatter, claim caches, and link graph in a state
where an agent can retrieve from it and calibrate how much to trust each note.

Output is a **defect report plus a repair plan**. You do not silently repair the
corpus. Repairs are proposed, applied one class at a time, and never delete.

The corpus is the source of truth and survives every tool you point at it. That
is the reason to maintain it as metadata rather than as an index.

## Use when

- Retrieval keeps missing notes you know exist
- A bulk import, migration, or merge just landed
- Before relying on the corpus to answer questions that matter
- The enum values in frontmatter have drifted from whatever schema you declared
- You want to know which notes are unreachable from anywhere

## Don't use when

- **You have a question to answer.** Use `markdown-knowledge-graph-traversal`.
  That skill retrieves, builds a claim graph, and answers. This one never
  answers a question about the corpus's subject matter.
- **The problem is above the notes, not inside them.** Generated indexes drifting
  from the generator that writes them, raw dated captures never promoted into
  durable linked notes, a filing taxonomy that has quietly stopped being a closed
  set — that is `research-corpus-self-indexing`. This skill works one note at a
  time on frontmatter and links; that one works on the layer that makes a corpus
  navigable at all. If notes are individually well-typed and still nobody can
  find anything, you want the other skill.
- You want to know whether a claim is **true**, or safe to publish. Use
  `evidence-grounded-verification` — it checks claims against sources outside
  your organization. This skill only checks whether a note's *metadata* is
  well-formed and internally consistent. A perfectly-typed note can be wrong.
- You're improving how the notes read: `voice-faithful-drafting`.
- You're deciding what to build: `pillar-program-design`,
  `communication-rollout-planning`.
- The corpus has no declared schema and nobody will declare one. Then there is
  nothing to validate against; see Stop conditions.

## Inputs

```yaml
corpus_root:      # path to the Markdown tree
schema:           # path to your declared schema, or "use the default"
canonical_paths:  # globs that are human-owned and must not be edited
draft_path:       # where proposed fixes are written, or "report only"
scope:            # "everything", a subtree, or "notes changed since <date>"
```

**If `schema` is missing and no default is accepted, stop and ask.** Validation
without a declared schema invents a standard and then enforces it, which is
worse than no validation. The default schema is in `reference/schema.md`.

**If `canonical_paths` is missing, treat the entire corpus as canonical** and run
in report-only mode. Never guess which files are safe to edit.

## Process

1. **Freeze the schema.** Write out the enum sets you are validating against and
   the required-field list. Everything downstream compares to this text. If the
   schema is new enough that it has not been in real use yet, report defects
   against it but propose no automated backfill — validation added to an unstable
   schema locks in the wrong thing.

2. **Inventory.** Count files, files with frontmatter, files without, and files
   per `type`, `domain`, and `status`. Report the counts before any judgment.
   A schema whose `status` values are 90% absent is a different problem from one
   with three misspelled `type` values.

3. **Check required fields.** Missing `type`, `status`, or `source_quality` is
   the high-impact class: those three drive retrieval filtering.

4. **Check enum validity.** Any value outside the frozen sets is drift. Report
   the value, its count, and every path. Do not map it to the nearest legal
   value on your own — a repeated illegal value is usually a request for a
   schema change, and that decision is the owner's.

5. **Check claim caches.** For notes with a `claims:` array, compare it to the
   body. Flag as stale when the body asserts something material the array
   doesn't, or the array asserts something the body no longer says. Flag as
   malformed when an entry is a paragraph, a summary, or a meta-description
   ("this note discusses X") rather than a discrete falsifiable assertion.

6. **Check supersede chains.** For every `supersedes:` link: the target exists,
   the target's `status` is `superseded`, and the target's body carries
   `[Superseded]` with a link forward. Flag chains that loop, and pairs where
   two notes each claim to supersede the other.

7. **Check link integrity.** Broken `[[wikilinks]]`; `related:` entries pointing
   at nothing; orphans with no inbound link from anywhere; and unlinked
   mentions — notes whose body names a note's title or alias without linking to
   it. Unlinked mentions are the highest-value repair, because they are the
   edges multi-hop traversal is missing.

8. **Check label discipline.** Every `unverified` and `ai-generated` note whose
   body carries no `[Unverified]`. Every note using `[Inference]` phrasing while
   declaring `source_quality: firsthand`. These are calibration defects: they
   cause an agent to overtrust the note later.

9. **Rank by retrieval impact**, not by count — see
   `reference/defect-classes.md`. Then emit the repair plan as ordered batches,
   one defect class per batch, each independently reviewable.

## Hard rules

Each of these prevents a repair that leaves the corpus validating clean and
quietly wrong. That is why they are rules rather than advice — after the fact, a
guessed value is indistinguishable from a confirmed one.

```text
Never delete a note. See the four conditions below.
Never edit a canonical note directly. Write a proposed update to the draft path.
Never invent a field value to make a file pass validation.
Never raise source_quality. Only the owner promotes trust.
Append and supersede. Do not overwrite; mark the old entry superseded with a date.
Never map an illegal enum value to a legal one on your own authority.
An unlinked mention is a proposal. Do not auto-link at scale.
```

**Deletion is permitted only when all four hold**, and even then it is the
owner's action, not yours:

1. **Byte-exact superset.** The destination contains the source text verbatim,
   allowing only an added frontmatter block and a title heading. No paraphrase,
   no summary, no "I rewrote it more clearly."
2. **Different durable location.** A different path in the corpus, not a rename.
3. **Persisted where the loss of this machine cannot take it.** Pushed to a
   remote, or synced and confirmed present at the destination. A copy that
   exists only on this machine does not count.
4. **Audit trail.** The removal is recorded somewhere durable, naming exactly
   where the content went — the removing commit message where the corpus is
   under version control, and otherwise a dated line in a log the corpus keeps.

Verify condition 1 mechanically — strip the destination's frontmatter and
confirm programmatically that the source text is a substring of the body. Do not
eyeball it. If any of the four is not provably true, the file stays.

Refuse these framings: "I'll summarize it and delete the original"; "it's just a
scratch file"; "the new version is better organized"; "it's in the chat history";
"we can recover it from git"; "it will be in the sync history." Clarity is not
preservation, a scratch file becomes a primary source the moment someone cites
it, and the asymmetry is deliberate: keeping a file costs almost nothing, and
losing one is the only genuinely irreversible operation here.

## Stop instead of guessing

- **No declared schema and no default accepted** → stop. There is nothing to
  validate against.
- **`canonical_paths` unknown** → run report-only. Do not infer ownership from
  folder names.
- **An illegal enum value appears in many notes** → stop and ask whether to
  legalize it. A widely-used value is usually a real distinction the schema
  missed, and correcting the notes would destroy it.
- **A required field's value is only knowable by reading content you should not
  read** — private, sensitive, or restricted notes → do not open them. Report the
  path, the missing field, and the question to ask. A metadata audit does not
  need the body.
- **The repair would need the body rewritten** → that is not a schema repair.
  Report it and stop.
- **Asked to auto-fix everything, or to make the validator pass** → refuse. A
  green validator produced by backfilling guesses is worse than a red one,
  because the guesses become indistinguishable from confirmed values.

## Further reading in this folder

- `reference/schema.md` — the default schema, the `source_quality` values and
  what each means, and how an untyped note is treated
- `reference/defect-classes.md` — every defect class with its retrieval impact
  and its repair, ordered by impact rather than by count
- `reference/report-shape.md` — the audit report template, and why inventory
  precedes defects
- `reference/failure-modes.md` — six ways a metadata audit leaves the corpus
  validating clean and worse than before
