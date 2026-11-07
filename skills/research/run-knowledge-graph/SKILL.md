---
name: run_knowledge_graph
description: Install and run the Knowledge Graph and 3D Funding Explorer visualization
user-invocable: true
allowed-tools: Bash(npm:*), Bash(make:*), Bash(node:*)
metadata:
  author: built-environment
---

> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../../docs/methodology.md) for details.

# Run the Knowledge Graph / 3D Funding Explorer

Bring up the interactive visualization that ships in the `knowledge-graph/` app
(Vite + TypeScript + `3d-force-graph`). Use this whenever someone asks to
"run", "rerun", "start", or "open" the knowledge graph or the funding explorer.

The generated `data/` is committed, so the app runs without re-extraction.

## When To Use
- A team wants to view or demo the 3D funding explorer locally.
- After pulling changes, to confirm the visualization still boots.
- Any pillar repo that contains a `knowledge-graph/` app — the steps are identical.

## Steps

Run from the pillar repo root.

```bash
cd knowledge-graph
make install     # npm install (only needed once, or after dependency changes)
make dev         # dev server at http://localhost:5173
```

Then open http://localhost:5173 in a browser.

## Full command set

```bash
make extract     # regenerate data/ from the repo corpus (deterministic)
make validate    # JSON Schema + referential integrity + financial sanity checks
make test        # vitest suite
make build       # production build (runs extract first)
make preview     # serve the production build
make screenshots # headless Chrome validation + screenshots
```

## Verify it started
The dev server prints `Local: http://localhost:5173/` when ready. To confirm
programmatically:

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:5173/   # expect 200
```

## Troubleshooting
- **`deps missing` / module-not-found**: dependencies aren't installed. Run
  `make install` (i.e. `npm install`) inside `knowledge-graph/` first.
- **Port 5173 already in use**: a server is already running — reuse the existing
  tab, or start on another port with `npm run dev -- --port 5174`.
- **Blank page**: confirm `data/graph.json` exists; if not, run `make extract`.
- **Long-running**: `make dev` and `make preview` do not exit. Start them in the
  background and leave them running; stop with Ctrl-C.

## Porting the app to another pillar repo

The app is identical in every pillar; only `pillar.config.json` and the
generated `data/` differ. From the Built Environment repo's `knowledge-graph/`:

```bash
./scripts/build-pillar.sh <target-repo-dir> "<Short Name>" "<Pillar Name>" [port]
```

That ports the source, installs dependencies, extracts, validates, builds, and
runs a headless smoke check that reports which views survived capability
gating. To port without building, use `./scripts/port-to-pillar.sh` directly.

### What each pillar gets
Extraction is deterministic and reads two files every pillar has:
`admin/evidence_log.md` and `data/source_inventory.csv`. Table dialects differ
between repos (heading levels, column names and order, bullet lists instead of
tables), so the parsers match columns by meaning rather than position.

Claims, gaps, and risks become Evidence, ResearchQuestion, and Risk nodes.
Inventoried sources become Dataset nodes. With `"derive": true`, publishers
named in the corpus become Organization nodes, and claims link to sources when
they share a URL, name the source, or cite the same distinctive domain.

### Views are gated on data, not assumed
Only the Built Environment corpus contains a capital-projects export
(`research/COR_CIP_Dashboard_projects.csv`), which is the sole origin of costs,
phases, and every financial flow. Pillars without one hide Overview, Timeline,
Money Flow, and Needs vs Money rather than render empty dashboards, and the
subtitle reads "Evidence Explorer" instead of "Funding Explorer". Problem Space
and Beneficiary are likewise hidden unless the graph has Problem or population
nodes.

### Curated records stay per-pillar
`extraction/records/*.json` are hand-authored research with excerpt-level
provenance verified at build time. A ported pillar starts with empty records
and builds its graph from the parsers alone; never copy another pillar's.
