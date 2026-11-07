---
name: report-update-protocol
description: "Safely add or update research reports and keep all metadata, indexes, and navigation files synchronized."
---

> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../../docs/methodology.md) for details.

# report_update_protocol

Purpose: Safely add or update research reports and keep all metadata, indexes, and navigation files synchronized.

## When To Use
- Adding a new research report to the corpus
- Updating an existing report with new findings
- Correcting a factual error in a report
- Moving or renaming a file
- Adding a new section to the research corpus

## Inputs
- New or updated content to add
- Target location (section and filename)
- Any source citations or evidence to track

## Outputs
- Updated or new `.md` file with proper structure
- Updated `research/index.json` entry
- Updated `research/INDEX.md` row
- Updated `CORPUS_GUIDE.md` when navigation, section map, counts, or reading orders change
- Updated `README.md` and `AGENTS.md` when the total research report count changes
- Updated `manifest.json` entry (when the manifest lists that file)
- Optionally: updated `evidence_log.md` if new verified claims

## Process

### Step 1 — Locate or Name the File

For a **new report:**
1. Determine the correct section (A–I, J–Q, or cross-cutting 90–98)
2. Choose the next available number in the section
3. Create the filename: `[SECTION][NUMBER]_[topic_slug].md`
4. Confirm no file with that name already exists

For an **existing report:**
1. Find the file in `research/`
2. Confirm it is the correct file (verify the H1 heading matches)
3. Note its current entry in `research/index.json` for comparison

### Step 2 — Prepare the File Content

Every report must:
- Begin with a clear H1 heading (the full report title)
- Contain only grounded claims (no invented data)
- Cite sources where possible (reference numbers from Parallel.ai are acceptable; include URLs if available)

Recommended frontmatter (add if not present):

```yaml
---
title: "Full Report Title"
pillar: thriving-built-environment
section: [A–I, J–Q, or cross-cutting]
problem_statement: transportation-project-visibility | fleet-operations-visibility | general
tags:
  - [tag1]
  - [tag2]
summary: "1–2 sentence grounded summary of content."
geography: Richmond, VA
date_generated: YYYY-MM-DD
source: parallel-ai-pro | manual | other
status: raw | reviewed | verified
---
```

Only add fields you can fill accurately. Do not fabricate.

### Step 3 — Update `research/index.json`

Locate the file's entry (or create a new one):

```json
{
  "id": "SECTION_NUMBER_topic_slug",
  "section": "SECTION_LETTER",
  "title": "Human-Readable Title",
  "summary": "Accurate 1–2 sentence grounded summary from the actual content.",
  "key_terms": ["term1", "term2", "term3", "term4", "term5", "term6"]
}
```

Rules:
- `id` must match the filename (without `.md`)
- `summary` must reflect the actual content, not an invented description
- `key_terms` should be extractable from the report text
- For new files, insert in the correct section order (not appended to end)

### Step 4 — Update `research/INDEX.md`

Add a row to the correct section:

```markdown
- [`SECTION_N_topic_slug.md`](SECTION_N_topic_slug.md) — Short description matching the report's H1 or frontmatter title
```

For updated files, check whether the description still accurately represents the content.

### Step 5 — Update `CORPUS_GUIDE.md`

Whenever research additions affect **how agents should traverse the corpus**, update `CORPUS_GUIDE.md` in the same change-set:

- **Report count** in the intro and directory description (if the total changed)
- **Research Section Structure** table (if a new section letter or file range was added)
- **Navigation decision tree** and **Question-to-Section mapping** (if new question types apply)
- **Recommended reading orders** (if a new common team scenario is documented)
- **File naming conventions** (if section rules changed)

If the change is a minor edit to one report with no navigation impact, note “no CORPUS_GUIDE change” in your validation checklist.

### Step 6 — Update `manifest.json`

Add or update the entry in the root manifest:

```json
{
  "id": "research/SECTION_N_topic_slug",
  "path": "research/SECTION_N_topic_slug.md",
  "type": "research_report",
  "title": "Human-Readable Title",
  "pillar": "thriving-built-environment",
  "section": "SECTION_LETTER",
  "summary": "Accurate 1–2 sentence summary.",
  "tags": ["tag1", "tag2", "tag3"],
  "recommended_audience": ["describe who should read this and why"],
  "read_after": ["research/prerequisite_file.md"],
  "source_of_truth": true
}
```

### Step 7 — Sync `README.md` and `AGENTS.md` (if report total changed)

If the number of files under `research/*.md` (excluding `INDEX.md`) changed, search for stale **51** / **70** / prior totals and update:

- `README.md` — repo map lines for `research/` and `research/index.json`
- `AGENTS.md` — “What the Research Corpus Contains” and the `index.json` bullet

### Step 8 — Update `evidence_log.md` (If Applicable)

If the report contains a newly verified factual claim (a claim with an official source URL):

Add a new row to `evidence_log.md` (root level):
```
| E-013 | [claim description] | [official URL] | [access date] | Confirmed | [notes] |
```

If the report corrects a previously `Confirmed` claim, update the existing row with a `[CORRECTED]` note rather than deleting it.

### Step 9 — Run the Validation Check

Before committing:

```
[ ] File exists at expected path
[ ] H1 heading is accurate and matches frontmatter title
[ ] Frontmatter fields are grounded (no fabricated values)
[ ] research/index.json entry is accurate and valid JSON
[ ] research/INDEX.md row is present and accurate
[ ] CORPUS_GUIDE.md updated OR explicitly N/A (navigation unchanged)
[ ] README.md / AGENTS.md counts updated OR N/A (total unchanged)
[ ] manifest.json entry is present and valid JSON (or N/A if manifest omits per-report entries)
[ ] Both JSON files pass: python3 -m json.tool [file]
[ ] evidence_log.md updated if new verified claims added
[ ] No broken internal links created
```

### Special Case: Renaming a File

Renaming an existing file requires updating all references. Run:

```bash
grep -r "OLD_FILENAME" . --include="*.md" --include="*.json"
```

Update every reference found before committing the rename. Pay particular attention to:
- `research/index.json` (`id` field)
- `manifest.json` (`id` and `path` fields)
- `research/INDEX.md` (link text and href)
- Any `related_reports` fields in other files' frontmatter
- `AGENTS.md` (if file is named there)
- `CORPUS_GUIDE.md` (if file is specifically referenced)

### Special Case: Removing a File

Before removing, check:
1. Is the file referenced in any navigation artifacts?
2. Is the file's content covered by another file?
3. Would removing it create a gap that agents would encounter?

Prefer deprecating over deleting: add a note to the file and its index entry rather than removing it outright.
