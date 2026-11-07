---
name: research-corpus-self-indexing
description: Keep a growing Markdown corpus findable by maintaining the layer above individual notes — verify the generated index still matches its generator, that every dated capture has been promoted into a durable typed note, and that the filing taxonomy is still a closed set. Emits a corpus health report and an ordered repair plan. Never deletes a note, never hand-edits a generated index, never invents a taxonomy the corpus does not declare. Works above the note; not per-note frontmatter validity (markdown-memory-schema-maintenance), and never answers a question from the notes (markdown-knowledge-graph-traversal). Use when a note pile has outgrown the folder it started in, after an ingest pipeline has run unattended for weeks, when two indexes disagree, or before restructuring paths that other tools write to. Trigger phrases include is my index stale, rebuild the index, did the ingest miss anything, my notes never got filed, these captures were never promoted, my vault outgrew its structure, reorganize my knowledge base, which index is right, safe to move these folders.
---

# Research Corpus Self-Indexing

Maintain the layer *above* the notes: the index that enumerates them, the
promotion path that turns raw captures into durable notes, and the taxonomy that
decides where anything is allowed to live.

Output is a **corpus health report plus an ordered repair plan**. You do not
edit notes, you do not hand-write indexes, and you do not delete. A corpus is
worth maintaining precisely because it outlives every tool pointed at it.

## Use when

- The corpus has more notes than a person can hold in their head, and finding
  something now depends on an index rather than on memory
- An ingest pipeline (voice memos, clippings, exports, bot writes) has been
  appending unattended and nobody has checked what it produced
- Two artifacts both claim to list the corpus and they disagree
- A restructure is being considered, and other programs write to these paths
- Notes are being added faster than they are being filed

## Don't use when

- **The defect is inside individual notes** — missing frontmatter fields, invalid
  enum values, stale claim caches, broken supersede chains, orphans nothing links
  to. Use `markdown-memory-schema-maintenance`, which validates note-level
  metadata. This skill checks whether the corpus *as a whole* is enumerated,
  promoted, and filed. Run that one first: this skill trusts frontmatter and
  inherits any lie in it.
- **You have a question to answer from the corpus.** Use
  `markdown-knowledge-graph-traversal`. This skill never reads notes for their
  subject matter and never answers a question about it.
- You need a claim cleared for an outside reader — a filing, a grant, a press
  release. Use `evidence-grounded-verification`. Being well-indexed and being
  true are unrelated properties.
- You are running an expensive transformation across every note that must resume
  after a crash. Use `corpus-transform`.
- The corpus is small enough to list by hand. Indexing machinery for forty notes
  costs more than it returns.

## Inputs

Ask for these. Do not infer them.

```yaml
corpus_root:          # path to the corpus
index_artifacts:      # paths of every file claiming to enumerate the corpus,
                      # generated or hand-maintained, or "none"
generator:            # path to the script/command that builds them, or "none declared"
taxonomy_file:        # path to the file declaring legal categories, or "none declared"
promotion_pipeline:   # how raw captures become durable notes, or "manual", or "none"
writers:              # every program, bot, workflow, or command that writes here
sensitivity_policy:   # which values of a sensitivity field mean "metadata only"
```

**If `writers` is missing, stop and ask.** Every finding about layout is
unsafe without it — the folder names are a live API, and this skill's most
destructive available recommendation is a path change.

**If `taxonomy_file` is "none declared", stop and ask.** Do not invent a
taxonomy. A category scheme you inferred from existing folder names will
canonize whatever accident is already there and cannot be told apart from a
deliberate one afterwards.

**If the generator will not run on an untouched copy**, report the index as
unverifiable and continue with the rest. Do not hand-write a replacement.

## Process

1. **Enumerate the ground truth first, from the filesystem, before opening any
   index.** Every content file, its path, its frontmatter, its size. If you
   start from an index you can only find defects the index already admits to.

2. **Regenerate the index into a scratch location and diff it against the
   committed one.** Any difference means the committed index is stale relative
   to its own generator — the exclusion rules, classifier, or category list
   changed and no successful rebuild has happened since. This is the cheapest
   high-yield check available and it is almost never run.

3. **Reconcile every index artifact against ground truth and against each
   other.** Where two disagree, record both answers, which is newer, and which
   one your counts were measured against. Do not pick a winner; disagreement
   between indexes is a finding about the machinery, not a question about one
   file.

4. **Check coverage in both directions.** Every content file appears in the index
   exactly once; every index entry resolves to a file. Then confirm each absence
   is caused by a *stated* exclusion rule, not by a classifier that dropped it.

5. **Classify each capture into the three states** of
   `reference/promotion-and-cadence.md` and list everything below `promoted`.
   This is the promotion backlog. Size it; do not sample it.

6. **Check taxonomy closure.** Flag directories created without a declaration,
   files parked in a category root when that category declares subcategories,
   and categories holding one file — usually a filing decision that was avoided.

7. **Look for duplicate captures by identity, not by name** — upstream id,
   ingest timestamp, or body hash. Two paths for one capture is the normal
   outcome of a naming convention that changed mid-flight.

8. **List duplicate-entity candidates without merging them.** The same referent
   under a role word and a proper name, singular and plural, or with and without
   a qualifier. Propose; never merge on inference.

9. **Inventory writers per path you would recommend moving.** If you cannot
   produce that list, no path change is in scope.

10. **Order the repair plan by retrieval impact**, one defect class per step,
    putting anything preservation blocks in its own deferred section rather than
    dropping it.

## Hard rules

Each of these prevents a corpus in which every artifact is internally consistent
and the enumeration is wrong. That is why they are rules rather than advice —
nothing inside any one index signals that it disagrees with another.

```text
Never delete a note. Unlinked, unfiled, and duplicated are all repairable; deleted is not.
Never hand-edit a generated index. Fix the generator and rebuild.
One generator per index artifact. Two enumerations of one corpus will disagree.
An index rebuild is read-only on note content.
A rebuild must be idempotent and must not trigger itself.
A capture is promoted when a durable note links back to it. Not before.
Declare a category in the taxonomy before creating its directory.
Never restructure paths before inventorying every writer.
Never half-apply a restructure. One pilot file in the new layout is worse than none.
An empty section is written empty. Omitting it loses the difference between checked-and-nothing and never-checked.
Never merge two entity notes on inferred identity. Propose, and let a human confirm.
```

The four conditions under which the owner — not you — may remove a note are in
`reference/preservation.md`.

## Sensitivity

Audit by path and frontmatter; do not read bodies to classify notes. That is a
privacy rule first, and also what keeps a full-corpus sweep cheap enough to run
on a schedule. Where a defect is only knowable by reading a body the sensitivity
policy puts off limits, record it as unknowable. Never quote a body into the
report; cite the path.

If an automated pass may write to the corpus, it writes to a draft or inbox
folder and a human promotes from there. An agent that can overwrite canonical
notes will eventually overwrite one.

## Stop instead of guessing

- **No taxonomy declared** → stop and ask. Do not derive one from whichever
  folders happen to exist.
- **No writer inventory** → report everything else and mark all layout findings
  out of scope. Do not recommend a move you cannot cost.
- **The generator will not run** → report the index as unverifiable. Do not
  reconstruct it by hand; the next reader cannot tell a hand-written index from a
  generated one and will trust it just as much.
- **Two notes may be the same referent, and confirming needs a body you may not
  read** → list it as a candidate with the matching signal, and stop.
- **Asked to clean up, prune, deduplicate, or delete orphans** → refuse the
  deletion and offer the repair instead: file it, link it, or promote it. The
  preservation rule is not overridden by a note looking worthless today.
- **A refactor plan exists describing the corpus** → verify against the
  filesystem before believing a word of it. Report the gap between plan and disk
  as a finding in its own right.

## Further reading in this folder

- `reference/promotion-and-cadence.md` — the three states a capture can be in and
  how each is detected, plus which checks belong on every write, on every ingest
  batch, and on a periodic sweep, and why the sweep is not redundant
- `reference/index-contract.md` — the typed frontmatter the generator classifies
  on, and why the note template and the generator are one contract
- `reference/preservation.md` — the four conditions that must all hold before a
  note may be removed, and the narrow exceptions that are not research deletions
- `reference/report-shape.md` — the corpus health report template, and why empty
  sections are written rather than omitted
- `reference/failure-modes.md` — eight ways a corpus becomes unfindable while
  every individual artifact still looks consistent
