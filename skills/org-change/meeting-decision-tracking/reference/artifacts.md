# The three artifacts

One cycle produces three. The agenda and the sync report are read by the next
cycle, so keep the shapes stable.

## Agenda

```markdown
# Agenda — <meeting> — <date>
Cycle: <window> · Time box: <n> min per person

## Blockers and cross-team dependencies
| Item | Blocked | Waiting on | Tracked as | Age (days) |
|---|---|---|---|---|

## Carried forward
| Item | From cycle | Age (days) | Tracked as | Why still open |
|---|---|---|---|---|

## <owner> — <domains> (<n> min)
### In progress / Ready to start / Blocked / Needs decision
- A1 · #<item> · <title> · <last activity>
- A2 · new · <title>
- A3 · #<item> · blocked on <what> · other side: <who>

## Roster and tracker mismatches
- <domain with no label, handle that did not resolve, or "none">
```

The item IDs (`A1`, `A2`) are assigned here, before anyone knows which lines will
produce actions. That is deliberate: they cannot serve as a binding key if they
are handed out after the fact to the lines that happen to need one.

## Notes

Fill in `templates/meeting-notes.md`. Its load-bearing property: every line sits
under an agenda item ID and carries exactly one tag.

```markdown
## A1 — <agenda line, copied>
- decision · <speaker> · <what was decided> · rules out: <what>
- action · <what> · owner: <name, or UNASSIGNED — ambiguity: "<words used>">
- blocker · <what is stopped> · other side: <who owes the work>
- information · <what>
```

`rules out` is the field people skip. A decision recorded without what it excludes
reads later as a preference rather than a choice, and gets quietly reversed by
someone who never saw the tradeoff.

## Sync report

```markdown
# Sync report — <meeting> — <date>
Applied at <time> · Deadline was <sync_deadline>

## Created
| Item | Title | Agenda ID | Assignee | Labels | Speaker |
|---|---|---|---|---|---|

## Updated
| Item | Agenda ID | Bound by (item ID | stated number) | What changed |
|---|---|---|---|

## Skipped
| Agenda ID | Reason |
|---|---|

## Unresolved — needs a human
| Agenda ID | What is missing | Who can supply it |
|---|---|---|
```

The **Bound by** column exists so that a similarity match becomes visible in the
output rather than invisible in the process. A row that cannot name its binding
key is the defect, printed.

The four buckets are exhaustive by construction. Reconciling every `action` line
in the notes against exactly one of them is what catches a dropped action, which
otherwise leaves no trace anywhere.
