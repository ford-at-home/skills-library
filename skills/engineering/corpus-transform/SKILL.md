---
name: corpus-transform
description: Design an expensive, long-running transformation over a large corpus so that a crash loses at most one item, a resume neither duplicates nor skips work, partial output is never mistaken for a complete corpus, and spend stops at a ceiling you chose. Covers checkpoint key design, atomic writes, validate-before-write ordering, and per-item versus run-level failure handling. Use when running a paid model or API over thousands of records, enriching a whole dataset, backfilling a table, or re-running a job that died partway. Trigger phrases include batch process, run over the whole corpus, resume from checkpoint, it died halfway, backfill, bulk enrich, how much will this cost, pick up where it left off, idempotent pipeline.
---

# Corpus Transform

Design a resumable batch transformation before spending money on it.

Output is a **run plan** plus a **run manifest** — the plan is written before the
first item is processed; the manifest is written by the run and is the only thing
downstream code is allowed to trust about completeness.

The failure this exists to prevent is not the crash. It is the corpus that
survives the crash looking complete and being wrong.

## Use when

- A transformation over many items costs real money or real hours per item
- The job is long enough that something will interrupt it
- The output becomes an input to something else — a table, an index, a dataset
- A previous run died and you are about to re-run it
- Corpus size, model, or prompt is about to change on an existing output set

## Don't use when

- The whole job fits in one call and losing it costs nothing. Add a retry.
- The subject is the quality of a single transformation rather than the
  survivability of many. For voice and register fidelity in the output text use
  `voice-faithful-drafting`.
- You are comparing models or prompts over a fixed set to decide which to use.
  That is `llm-behavior-benchmark` — a measurement harness, not a production
  run, and its stopping rules are different.
- You are checking whether the corpus's *claims* are true rather than whether
  its *records* are complete. That is `evidence-grounded-verification`.
- You need the pipeline to exist as deployed infrastructure — queues, workers,
  retries at the platform level. That is provisioning work; use your
  infrastructure tooling. This skill governs the transformation's correctness
  whether it runs in a Lambda or a terminal.

## Inputs

Ask for these. Don't infer them.

```yaml
corpus:            # path or query, and the count of items
item_identity:     # what makes one item distinct, as field names.
                   # "source_id + section", not "each row"
transform_config:  # every value that changes the output: model id, prompt
                   # version, temperature, persona, mode, intensity, max_tokens
per_item_cost:     # estimated USD or tokens per item, and where the estimate
                   # came from
spend_ceiling:     # USD at which the run must stop. Not "monitor it"
output_target:     # where records land, and what reads them next
existing_output:   # path to a prior partial run, or "none"
```

**If `transform_config` is missing, stop and ask.** It is the input everyone
omits and it is half of the checkpoint key. Without it a resume cannot tell
whether a stored item was produced by the configuration you are running now.

**If `spend_ceiling` is missing, stop and ask.** Do not substitute a large
number. Every implementation reviewed for this skill estimated cost up front,
logged the estimate, and then had no mechanism to stop at it.

## Gates before the first item

Written before the process because a gate written after is written to pass.

- [ ] The checkpoint key includes every value in `transform_config`
- [ ] `count(corpus) * per_item_cost` is below `spend_ceiling`, arithmetic shown
- [ ] The transform has run end-to-end on 3 items, one of them known-bad
- [ ] A completeness marker exists and is absent by default
- [ ] Validation runs before the write, not after
- [ ] `existing_output`, if present, has been key-checked against the current
      config — not assumed resumable because the file is there

## Process

1. **Define the checkpoint key.** The key is the item identity *plus* every
   config value that changes the output. Store it as a single string or hash so
   a key mismatch is one comparison, not a review. The record's other fields are
   in `reference/checkpoint-and-writes.md`.

2. **Write the run plan** — item count, key formula, cost arithmetic, spend
   ceiling, and what a single-item failure does versus a batch failure.

3. **Key-check any prior output before resuming.** Compare stored keys against
   the keys the current config generates. Report the three counts separately:
   reusable, present-but-different-config, missing. Never merge the second into
   the first.

4. **Process one item at a time**, and for each: call → validate → write record
   → write checkpoint. In that order. The checkpoint is written after the record,
   never before; a checkpoint that runs ahead of the record turns a crash into a
   silently skipped item. What validation checks, and why it runs before the
   write, is in `reference/checkpoint-and-writes.md`.

5. **Accumulate actual spend** and compare to the estimate every N items. Stop
   at the ceiling. Report the ratio of actual to estimated — a large divergence
   means the estimate was wrong about the whole corpus, not just about the items
   already processed.

6. **On single-item failure**, record the item's key, the error, and the attempt
   count as a failure record. Continue. A failure record is a first-class row,
   not an omission.

7. **On batch-level failure** — auth, quota, billing, rate limit that survives
   backoff — halt the run and do **not** record the in-flight item as failed. It
   did not fail; the run did. Recording it failed makes a future resume skip an
   item that was never attempted.

8. **Write the manifest last**, and only then clear the completeness marker.

9. **Report the manifest counts against the corpus count.** If they don't
   reconcile, say so in the report. Do not reconcile them by adjusting a
   denominator.

## Hard rules

These are rules rather than advice because each one, when violated, leaves a
corpus that reconciles by count and reads as finished. Nothing downstream
signals that one was broken.

```text
The checkpoint key includes every config value that changes the output.
A checkpoint is written after its record, never before.
Never fabricate a record to satisfy a validator. A fabricated record that
  passes validation is permanently indistinguishable from a real one.
Never mark an item failed for a run-level failure.
Never permanently skip a previously-failed item on resume without saying so
  in the manifest.
An estimated cost is labeled estimated, in the record, next to the number.
Partial output is marked by something absent on success.
Never overwrite a completed record with a failure record.
Two config versions in one output set is a reported state, not a merge.
The corpus source is never modified.
```

The first rule is the reason this skill exists. Three independent
implementations of this pattern keyed their checkpoints on item identity alone.
Each of them will, on a resume after a model or prompt change, skip every item
the previous configuration produced — yielding a corpus that is complete by
count, mixed by provenance, and silent about it.

## Stop instead of guessing

- **`transform_config` or `spend_ceiling` missing** → stop and ask. Do not
  default either.
- **Prior output exists but stores no config** → stop. You cannot tell what
  produced it. Offer two honest options: reprocess everything, or key-check on
  identity alone and mark the whole output set mixed-provenance in the manifest.
  Do not pick one silently.
- **Corpus changed shape since the last run** — different item count, or an
  identity that now resolves to two items → stop. An item-count comparison
  catches insertions and deletions and misses edits entirely, so a count that
  matches is not evidence the corpus is the same.
- **Actual spend exceeds the estimate by more than 2x before 10% of the corpus
  is done** → stop. The estimate was wrong about the corpus, not about the
  items. Re-estimate from measured cost, then re-confirm the ceiling.
- **Validation fails on more than a few percent of items** → stop the run. This
  is a prompt or schema problem, and continuing converts it into a large bill
  and a corpus of failure records.
- **Asked to run with validation off, or with a fallback that fills failures
  with generated placeholder content** → refuse. Both convert a countable
  failure into an uncountable one. Offer to widen the schema, or to record
  failures and report the rate.

## Further reading in this folder

- `reference/checkpoint-and-writes.md` — the checkpoint record's fields, the
  completeness marker, the atomic write, and why validation runs before the
  write rather than after
- `reference/report-shape.md` — the run plan and run manifest templates,
  including the resume analysis and the reconciliation table
- `reference/failure-modes.md` — eight ways a batch transformation produces a
  corpus that looks complete, most of them observed in practice
