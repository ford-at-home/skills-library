# The promotion path, and what to check how often

## The three states of a capture

The promotion path is the mechanism that turns a dated pile into a navigable
graph. Every capture is in exactly one state, and the state must be readable
without opening the body.

| State | Marker | Meaning |
|---|---|---|
| `captured` | Sentinel text in the body (e.g. `_Integration pass pending._`), empty typed-link arrays | Raw input exists. Nothing has been extracted from it |
| `enriched` | Typed fields populated, outbound links declared | Classified and cross-referenced, but no durable note depends on it yet |
| `promoted` | A durable note names it in a `sources`-style field | It has entered the graph. Retrieval can reach it from a concept, not just by date |

A capture is not promoted because it was enriched. It is promoted when a durable
note links **back** to it. Forward-only edges leave the capture reachable only by
its date, which is the one thing nobody searches by.

**Date-partitioned captures are immutable; durable notes are accumulative.** The
dated note keeps its provenance — original artifact path, ingest timestamp,
upstream id, whatever proves where it came from — and is never rewritten. The
durable note is edited repeatedly as more captures land and lists every capture
it draws on. That asymmetry is what keeps promotion one-way and the corpus
append-only in practice.

## What to check, and how often

| Cadence | Check |
|---|---|
| Every write | Index rebuild runs, is idempotent, and does not trigger itself |
| Every write | New file's path is legal under the declared taxonomy |
| Every ingest batch | Captures from this batch reached `enriched`, not just `captured` |
| Periodic sweep | Full-corpus scan for captures stuck below `promoted` |
| Periodic sweep | Committed index still matches a fresh run of its generator |
| Periodic sweep | Index artifacts agree with each other |
| Periodic sweep | Duplicate captures by upstream identity |
| Periodic sweep | Titles and summaries in the index are still human-scannable |
| Periodic sweep | Categories with one file; directories not in the taxonomy |
| Before restructure | Writer inventory per path |
| Before restructure | Whether a previous restructure was left half-applied |

**The periodic sweep is not redundant with the per-write checks. It is the
backstop for them.** Event-triggered promotion loses events: a handler that
retries only files touched by the current push will never revisit a capture
whose enrichment failed once. Those captures are invisible to every per-write
check by construction and stay pending forever. Only a full-corpus sweep finds
them.
