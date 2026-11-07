# Output shape

```markdown
## Rewritten Version
<the cleaned prose, with assumption tags inline>

## Claims That Need Evidence
- <claim>: <why it needs evidence, and what would settle it>

## Removed Fluff
| Original | Reason removed |
|---|---|

## Rule Conflicts
| Sentence | Rule it violates | Why the original meaning was kept |
|---|---|---|

## Open Questions
- <question>: owner? deadline?

## Decision-Relevant Summary
<3–5 sentences. What is the reader being asked to decide or do?>
```

The Removed Fluff table is what makes the pass auditable: the author cannot check
a rewrite by reading it, because the rewrite reads fine. Every removal appears
there with its reason, or the removal did not happen.

The Rule Conflicts table is where a rule lost to the author's meaning. Where a
rule and the meaning conflict, the meaning wins and the conflict is logged here
rather than resolved silently.
