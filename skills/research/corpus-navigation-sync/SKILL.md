---
name: corpus-navigation-sync
description: "Keep the research corpus **traversable by AI agents** whenever reports are added, removed, renamed, or grouped under a new section."
---

> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../../docs/methodology.md) for details.

# corpus_navigation_sync

Purpose: Keep the research corpus **traversable by AI agents** whenever reports are added, removed, renamed, or grouped under a new section.

## When To Use

- After generating or importing new `research/*.md` reports (including batch Parallel.ai runs)
- Before merging any PR that touches `research/` or `05_prompts/research/`
- When introducing a **new section letter** (e.g. past `I`) or changing how sections map to questions
- Whenever you suspect `CORPUS_GUIDE.md`, `research/index.json`, and `research/INDEX.md` are out of sync

## Inputs

- List of new/changed/removed report filenames (stems without `.md`)
- Whether the **total report count** changed

## Outputs

- Updated navigation artifacts in a **single atomic change-set** (same commit)
- No orphaned `.md` files without `index.json` + `INDEX.md` entries

## Process

### Step 1 — Run `report_update_protocol`

Follow `skills/report_update_protocol/SKILL.md` for file content, `research/index.json`, `research/INDEX.md`, optional `manifest.json`, and `evidence_log.md`.

### Step 2 — Update `CORPUS_GUIDE.md` (non-optional when navigation changes)

Update `CORPUS_GUIDE.md` whenever the change affects traversal:

| Change | Update in CORPUS_GUIDE |
|--------|-------------------------|
| New report, same section | Bump total count only (if count changed) |
| New section letter | Section table, naming conventions, question mapping, decision tree |
| New common team scenario | Recommended reading orders |
| New cross-domain theme | Short “how this relates to A–I” prose (see sections J–Q as a model) |

If you only fixed typos inside one report and did not change scope, document **CORPUS_GUIDE: N/A** in your PR/commit notes.

### Step 3 — Sync stated totals across the repo

If the count of research reports changed, grep for old totals (e.g. `51`) in:

- `README.md`
- `AGENTS.md`
- `CORPUS_GUIDE.md`
- `research/INDEX.md`
- `skills/research_search/SKILL.md` (if present)

Update every **authoritative** count. Do not leave contradictory numbers.

### Step 4 — Validate

```bash
python3 -m json.tool research/index.json > /dev/null
python3 -m json.tool manifest.json > /dev/null  # if manifest edited
```

Confirm: every `research/*.md` report (except `INDEX.md`, `validation_report.md` if excluded) has an `index.json` entry — or explicitly document exceptions in `MAINTENANCE.md`.

## Rules

1. **Never** add research outputs without updating `research/index.json` and `research/INDEX.md`.
2. **Never** change section structure without updating `CORPUS_GUIDE.md`.
3. Prefer **`corpus_navigation_sync` + `report_update_protocol`** over ad-hoc edits so future agents inherit one process.

## Related

- `MAINTENANCE.md` — full maintenance checklist
- `CORPUS_GUIDE.md` — canonical orientation for humans and agents
- `skills/report_update_protocol/SKILL.md` — per-file metadata steps
