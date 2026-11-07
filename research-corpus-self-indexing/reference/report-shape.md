# The corpus health report

```markdown
# Corpus Health — <corpus>
**As of:** <date> · **Files on disk:** N · **In index:** N · **Excluded by rule:** N
**Generator:** <path | none declared> · **Fresh rebuild matches committed index:** yes | no | could not run
**Index artifacts reconciled:** <list> · **Bodies read:** none

## Blocking — retrieval is wrong right now
| Defect | Evidence | Affects | Repair |
|---|---|---|---|

## Index integrity
| Artifact | Entries | Agrees with ground truth? | Disagreements |
|---|---|---|---|

## Promotion backlog
| Capture | State | Stuck since | Missing edge |
|---|---|---|---|

## Taxonomy drift
| Path | Problem | Declared? | Repair |
|---|---|---|---|

## Duplicate candidates — proposed, not merged
| A | B | Matched on | Confirm by |
|---|---|---|---|

## Layout coupling
| Path under review | Writers that break | Safe to move? |
|---|---|---|

## Deferred by preservation policy
| Item | Why it looks removable | Why it stays |
|---|---|---|

## Repair plan — ordered, one class per step
1. <class> — <files> — <verification that it worked>

## Unverifiable
- <what could not be checked, and what would settle it>
```

Every section is written even when it is empty. An omitted section loses the
difference between checked-and-found-nothing and never-checked, and the reader
has no way to recover it.

The header carries the file count on disk beside the count in the index because
those two numbers disagreeing is the whole finding, and a report that states only
one of them reads as clean.
