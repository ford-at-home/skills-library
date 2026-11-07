---
skill_number: "00"
skill_id: plugin-orientation
name: Plugin Orientation
version: 1.0.0
status: initial
lifecycle_stage: meta
estimated_duration: 5-15 minutes
requires_human_review: false
prerequisites:
  required: []
  optional: []
outputs:
  - artifacts/00-plugin-orientation/planning-state.md
  - artifacts/status.md
downstream_skills:
  - 01-civic-alignment
  - 02-event-charter
  - "(any skill the user is resuming)"
templates_used:
  - templates/00-plugin-orientation/planning-state.template.md
  - templates/00-plugin-orientation/status.template.md
search_paths:
  - artifacts/
  - templates/
  - examples/
  - planning-plugin/
  - docs/
  - planning/
  - ../2026-annual-hackathon/
  - root-level markdown files
---

# Skill 00 — Plugin Orientation

## Purpose

Inspect the repository, classify what planning work is present vs.
missing vs. partially normalized, and produce a single snapshot the
user (or any downstream skill) can use to decide what to do next.

This is the entry point for any user who is not starting from a
fully empty repository. Skill 00 never invents planning content; it
only reports on what it finds.

## When to use

- Starting a new planning project and want to confirm the repo is
  empty
- Resuming planning work after a gap and want to know what state
  things are in
- Inheriting a repo from someone else
- About to run any other skill and want a fast sanity check that the
  expected prerequisites exist
- Routine status check during a multi-week planning effort

## Who should use it

Any human or agent. Skill 00 is read-only-ish — it writes only
diagnostic artifacts, never planning content.

## Prerequisites

None. Skill 00 runs against whatever state the repo is in.

## Inputs

- The repository as it currently exists
- Optional: a user-supplied path or URL to an external planning
  document the user wants the skill to consider during inventory

## Outputs

| Path | What it is |
| ---- | ---------- |
| `artifacts/00-plugin-orientation/planning-state.md` | Full diagnostic snapshot |
| `artifacts/status.md` | Rolling per-artifact status summary, updated by every skill that touches an artifact |

## Search behavior

Walk the following paths and catalog what exists:

1. `artifacts/NN-skill-slug/` — for each of the 19 skills, list any
   files present and read their frontmatter status.
2. `templates/NN-skill-slug/` — list templates available. A populated
   template means the toolkit ships a starting point; absence means
   the user will create the template fresh or must adapt one.
3. `examples/*/NN-skill-slug/` — list any worked examples that exist.
   Note which city/year each example is from.
4. `planning-plugin/skills/` — list the skill files themselves; the
   skill names found must equal the canonical set (00–18). Missing
   skill files are reported as plugin gaps.
5. **Parent repository** — if the toolkit lives inside a larger repo,
   walk for likely-relevant material:
   - markdown files at the repo root
   - `docs/`, `planning/`, `notes/`, `research/`
   - any directory named after a hackathon year (e.g.
     `2026-annual-hackathon/`)
   - any file matching `PILLARS.md`, `RUBRIC.md`, `JUDGE_SHEET.md`,
     `CONTACTS.md`, `INDEX.md`, `LIFECYCLE_RUBRIC.md`
6. User-supplied external paths or pasted content.

For every file found, record:

- Path
- Size
- Last-modified date
- Frontmatter status if it is a recognized artifact
- A one-line guess at what skill it might belong to

## Validation behavior

For each file recognized as a plugin artifact:

- Run the schema validation block from
  `planning-plugin/validation/checks.md` (every-artifact section).
- Report any failing fields.

For each file found in the parent repository that **looks like** a
plugin artifact but is not in the canonical path, note it as a
"normalization candidate" and identify the most likely target skill.

Skill 00 does **not** normalize anything itself. It only flags
candidates for downstream skills to handle.

## Normalization behavior

None directly. Skill 00 reports normalization candidates and lets
the relevant downstream skill decide whether to normalize.

## Step-by-step procedure

1. **Walk the repo.** Build a list of every file in `artifacts/`,
   `templates/`, `examples/`, plus the parent repo's likely-relevant
   paths.
2. **Classify each file.** For every file, decide:
   - Is it a canonical plugin artifact? (matches a path in
     `artifact-index.md`)
   - Is it a template? (lives under `templates/`)
   - Is it an example? (lives under `examples/<city-year>/`)
   - Is it a normalization candidate? (looks relevant but is not at
     a canonical path)
   - Is it noise? (unrelated repo content)
3. **Read frontmatter** on every canonical artifact. Capture
   `status`, `human_review_required`, `review_owner`, and any
   `open_questions`.
4. **Build the per-skill status table.** For each of the 19 skills,
   list:
   - Required outputs (from `artifact-index.md`)
   - Which outputs exist and at what status
   - Which outputs are missing
   - Which outputs have normalization candidates available
5. **Compute the resume recommendation.** The recommendation is the
   lowest-numbered skill whose required prerequisites are all
   present (status `draft` or higher) but whose outputs are
   incomplete or missing.
6. **Write `planning-state.md`** with the full snapshot.
7. **Write `artifacts/status.md`** with a compact rolling summary.
   If the file already exists, merge rather than overwrite.
8. **Report to the user** with: counts, the resume recommendation,
   the top three blockers, and any normalization candidates worth
   acting on next.

## User interaction rules

- Skill 00 may run without any user input.
- If normalization candidates are found, ask the user once whether
  they want to surface those to the relevant downstream skill, but do
  not normalize within Skill 00 itself.
- Skill 00 must not change `status` on any existing artifact. It is
  read-only on plugin artifacts.
- If the user provides an external path or URL, include it in the
  inventory but do not fetch external URLs without confirmation.

## Completion criteria

- [ ] `planning-state.md` exists at the canonical path with the
      full snapshot
- [ ] `artifacts/status.md` exists or has been updated
- [ ] Every skill (00–18) has a row in the snapshot
- [ ] Every canonical artifact found has a frontmatter status
      recorded
- [ ] Normalization candidates are listed with their suggested
      target skill
- [ ] A resume recommendation is named

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| `artifacts/` directory does not exist | Create it; report repo as fresh. |
| Plugin skill files (00-18) are missing from `planning-plugin/skills/` | Report missing skills; the user may be looking at a partial plugin install. Do not invent skill files. |
| An artifact file exists but has no frontmatter | List it as a normalization candidate for its likely target skill. Do not auto-add frontmatter. |
| Parent repository is huge and walking it is slow | Bound the walk to the conventional paths listed above; do not recurse into `node_modules/`, `.git/`, `.venv/`, `dist/`, build output. |
| External URL was supplied but cannot be fetched | Report the URL as a pending input; do not block. |

## Templates used

- `templates/00-plugin-orientation/planning-state.template.md` —
  section structure for the snapshot
- `templates/00-plugin-orientation/status.template.md` — compact
  table format for the rolling status

If these templates do not exist yet, Skill 00 creates `planning-state.md`
and `status.md` from minimal in-skill defaults and notes the missing
templates as a plugin gap.

## Downstream skills

Any skill can run after Skill 00. The resume recommendation names
the most likely next skill.

## Example invocation

> "Run plugin orientation. The repo is a fresh clone of the
> toolkit; tell me what's here and what to do first."

Expected response:

```
Walked: 7 paths, 0 canonical artifacts found, 0 normalization
candidates.

State:
  - Repo is empty of plugin artifacts.
  - Templates: present for all 19 skills (or list gaps).
  - Examples: richmond-2026 present (1 example bundle).

Recommendation: run Skill 01 (Civic Alignment) to anchor the event
in a public strategic plan. You will need:
  - A public strategic document from your local government (e.g.
    mayor's action plan).
  - A named executive sponsor inside city government.

Top 3 blockers: (none — fresh repo).
```

> "Run plugin orientation. We have a folder of meeting notes in
> `2026-annual-hackathon/` from last year's event."

Expected response:

```
Walked: 9 paths, 0 canonical artifacts, 14 normalization candidates.

Normalization candidates worth acting on:
  - 2026-annual-hackathon/PILLARS.md → Skill 05 (Track Strategy)
  - 2026-annual-hackathon/RUBRIC.md → Skill 14 (Judging System)
  - 2026-annual-hackathon/JUDGE_SHEET.md → Skill 14 (Judging System)
  - 2026-annual-hackathon/CONTACTS.md → Skill 03 (Stakeholder Map)
  - 2026-annual-hackathon/outreach/ → Skill 09 (Community Outreach)
  - 2026-annual-hackathon/kickoff-emails/ → Skill 09 (Community Outreach)
  - 2026-annual-hackathon/research/ → Skill 06 (Problem Statements)
  - 2026-annual-hackathon/POST_HACKATHON_CONTACTS.csv → Skill 16

Recommendation: run Skill 01 first (no prior-year artifact exists
for civic alignment in the candidate set; the year-1 alignment
needs to be reconfirmed for year 2). After Skill 01, the resume
path proceeds through 02 → 03 (where Skill 03 can normalize
CONTACTS.md and POST_HACKATHON_CONTACTS.csv).
```

## Changelog

- 1.0.0 (initial) — First version. Read-only inventory, no
  normalization, no automated repair.
