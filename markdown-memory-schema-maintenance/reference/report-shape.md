# The audit report

```markdown
# Schema Audit — <corpus>
**Schema:** <declared, or "default, no schema was declared">
**Scope:** <what was scanned> · **Date:** <date>
**Write mode:** report-only | drafts to <path>

## Unresolved decisions (read first)
- <what needs the owner, and what is blocked until they answer>

## Inventory
| Metric | Count |
|---|---|
| Files scanned | |
| With frontmatter | |
| Missing a required field | |
| Illegal enum values | |
| Orphans | |

## Defects by class
### <class> — <n> notes — impact: <high/medium/low>
| Path | Detail | Proposed repair | Needs owner? |
|---|---|---|---|

## Repair plan
### Batch 1 — <class>
- Applies to: <n paths>
- Change: <exactly what is written, and where>
- Reversible by: <how to undo>
- Blocked on: <decision, or "nothing">

## Schema-change requests
| Value found | Count | Legalize, or correct the notes? |
|---|---|---|

## Not repairable without the owner
| Path | What is unknown | Question to ask |
|---|---|---|
```

Inventory comes before Defects because the two situations a reader must be able
to tell apart — a corpus that is 90% untyped and a corpus with three misspelled
values — produce defect lists that look similar and demand different responses.

Each repair batch carries its own reversal because the batches are applied one at
a time by a human who may stop after any one of them.
