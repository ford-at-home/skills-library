# The turn decision record

```markdown
# Turn Decision — <channel> · <turn id> · <timestamp>
**State read from:** <store> · **Replicas:** <n> · **Arbiter calls this period:** <n>/<cap>

| Candidate | Blocked by | Det. score | Arbiter | Weight | Final | Spoke |
|---|---|---|---|---|---|---|
| <name> | rule 2 (addressed and unanswered: waiting on <name>) | — | — | — | — | no |
| <name> | — | 0.42 | 0.60 | 0.3 | 0.47 | yes |

**Outcome:** <participant, or "no speaker">
**If no speaker:** <which rules blocked everyone>
```

A turn where every candidate is blocked emits a no-speaker record. That is a
result, not a gap.
