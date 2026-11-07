---
name: knowledge_graph_pipeline
description: Change the knowledge-graph extractor and publish the result across all seven pillar repos and the rvahacks site. Use when editing anything under knowledge-graph/extraction/, when graph data needs regenerating, when running the release check, or when asked to publish or deploy graph changes to rvahacks.org.
user-invocable: true
metadata:
  author: built-environment
---

> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../../docs/methodology.md) for details.

# Knowledge Graph Pipeline

One extractor feeds eight graphs: seven pillars plus the merged `richmond`
graph, all served by one explorer bundle on rvahacks.org. A change to a parser
is therefore never a one-repo change. This is the order that works, and the
traps that cost time when skipped.

To run the explorer locally or port it to a new pillar, use
`run_knowledge_graph` instead. This skill is about changing and shipping it.

## Repo layout

| What | Where |
|---|---|
| Canonical extractor | `pillar-thriving-built-environment/knowledge-graph/extraction/` |
| Per-pillar copy | the same path in each of the other six pillar repos |
| Generated data | `<pillar>/knowledge-graph/data/` (committed) |
| Site + pipeline scripts | `rvahacks/scripts/` |
| Data the site serves | `rvahacks/public/knowledge-graph/data/<pillar>/` |

The parsers are **byte-identical across all seven repos**. Edit the Built
Environment copy, then copy it out. Never edit a pillar copy directly — the next
sync silently reverts it.

## Order of operations

Copy this checklist and work down it. Steps 3 and 5 are the ones people skip.

```
- [ ] 1. Edit the canonical parser in Built Environment
- [ ] 2. Copy to the other six repos; confirm shas match
- [ ] 3. Export project names (writes INTO the pillar repos, so before extract)
- [ ] 4. Re-extract all seven; run the test suites
- [ ] 5. Sync, promote aliases, merge, regenerate stats, rebuild explorer
- [ ] 6. Build the site; run the release check against a preview server
- [ ] 7. Commit and push all eight repos
- [ ] 8. Publish manually in Lovable — pushing to GitHub does not deploy
```

### 1–2. Edit once, copy out, verify

```bash
cd pillar-repos
SRC=pillar-thriving-built-environment/knowledge-graph/extraction/parsers/<file>.js
for p in pillar-thriving-neighborhoods pillar-thriving-families \
         pillar-city-storytelling pillar-thriving-inclusive-communities \
         pillar-thriving-economy pillar-thriving-city-hall; do
  cp "$SRC" "$p/knowledge-graph/extraction/parsers/$(basename $SRC)"
done
for p in pillar-repos/pillar-*; do shasum -a1 "$p/knowledge-graph/extraction/parsers/$(basename $SRC)"; done
```

All seven hashes must match before going further.

### 3. Project names, before extraction

Display names for the demo projects live in `rvahacks/src/data/ideas.ts` and
`idea-content.ts` and nowhere else. `kg:names` exports them into each pillar
repo as `post-event-research/project-names.json`, which the extractor reads.

```bash
cd rvahacks && npm run kg:names
```

It reports `named/total` per repo. Anything unnamed falls back to rendering the
directory slug, which is worth fixing rather than shipping — see
`graph_entity_naming`.

### 4. Re-extract and test

```bash
cd pillar-repos
for p in pillar-*; do (cd "$p/knowledge-graph" && node scripts/extract.js); done
for p in pillar-*; do (cd "$p/knowledge-graph" && npx vitest run); done
```

Read the extract warnings; they are the early signal. `[demote] N sentence-shaped
Problem/Need nodes moved to the evidence layer` is normal and healthy — those
findings land in `data/evidence.json` as `ev:` records with provenance, not lost.

### 5. Through the site pipeline

```bash
cd rvahacks
npm run kg:sync                     # pillar data -> public/knowledge-graph/data/
node scripts/promote-aliases.mjs    # NOT in kg:refresh; run it before merging
npm run kg:merge                    # builds the richmond graph
npm run kg:stats                    # regenerates src/data/corpusStats.generated.ts
npm run kg:app                      # rebuilds the explorer bundle
```

`npm run kg:refresh` chains sync → merge → stats → app, but **omits
promote-aliases**. Run that separately when entity merging matters.

Every published figure comes from `corpusStats.generated.ts`. Never hand-edit a
count into `civicInventory.ts` or a page — it will drift the next time anyone
re-extracts. Facts reference stats by `metric:` key.

### 6. Release check

The check drives a real browser against a real preview server, so the server has
to already be up:

```bash
cd rvahacks && npm run build
lsof -ti:4173 | xargs kill -9 2>/dev/null   # clear a stale holder
npm run preview                              # start as a true background job
npm run release-check
```

Two traps here, both of which produce a confusing all-red run:

- **`npm run preview` dies with its subshell.** Backgrounding it with `&` inside
  a compound command kills it the moment the command returns, and every check
  fails `ERR_CONNECTION_REFUSED`. Start it as its own long-running background
  process and leave it running.
- **Port 4173 is often still held** by a previous run. Kill it first.

`playwright` is a devDependency of rvahacks. If you add or bump it, update
**both** lockfiles — `package-lock.json` and `bun.lock`. The host may install
with bun, and a stale `bun.lock` breaks its build.

Expect `51/51 checks passed`. What the check actually catches:

| Check | Catches |
|---|---|
| view gating | a pillar page promising a view the explorer hides |
| render | a graph that loads but paints nothing |
| page figures | published counts that no longer match the data |
| stale figures | previously-hardcoded numbers reappearing |
| console | runtime errors in the embedded explorer |

**View gating fails whenever a node type empties out.** Removing the last
`Problem` node from a pillar hides its Problem Space view, and the fix is to
remove that view from `liveViews` in `civicInventory.ts` and reword any copy
that referred to it. That is the check doing its job, not a false alarm.

### 7–8. Push, then publish by hand

Commit the pillar repos and rvahacks separately — they are independently
versioned, and the umbrella `git status` shows them as untracked on purpose.

**rvahacks.org is Lovable-hosted. `git push` does not deploy it.** The site only
updates when someone clicks Publish in the Lovable UI. Say so explicitly rather
than reporting the work as live. To confirm after publishing:

```bash
curl -s https://rvahacks.org/knowledge-graph/data/richmond/graph.json \
  | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>console.log(JSON.parse(s).nodes.length,"nodes"))'
```

Compare against the local count from `kg:stats`. A mismatch means the publish
has not happened yet.

## Working with the merged richmond graph

- Entities merge only on a **hand-approved** table, `scripts/canonical-entities.json`.
  Never merge on string similarity: a wrong merge is worse than a missed one.
- `promote-aliases.mjs` applies vetted aliases and refuses cross-type merges
  (an `Organization` will not absorb a `GeographicRegion`).
- The merge prunes hard for legibility — cited-source nodes, single-claim corpus
  entities, and anything left unconnected. The counts it prints are expected.

## Verify before claiming done

- All seven parser hashes identical
- All seven test suites green
- `release-check` at full pass
- Published figures regenerated, not typed
- Told the user that Lovable Publish is still required
