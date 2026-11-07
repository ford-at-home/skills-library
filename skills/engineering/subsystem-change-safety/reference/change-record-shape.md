# The change record

```markdown
# Change Record — <subsystem>
**Intent:** <one sentence> · **Depends on it:** <who or what>
**Tier:** 1 | 2 | 3 · **Baseline:** <command> → <verbatim result>

## Unresolved (read first)
- <what is not settled, and what would settle it>

## Invariants
| Invariant | Enforced by | Loud/Silent | Covered after this change by |
|---|---|---|---|

## Silent-failure checks added
| Check | Invariant it covers | Confirmed to fail when broken? |
|---|---|---|

## Ordered steps
1. <step> — pre-condition: <what must hold> — verify: <command> — compensate: <action>

## Rollback
<revert, or the named forward fix. Say which flavor applies and why>

## Manual actions (human executes)
| Action | Why it cannot be done here | Verification command |
|---|---|---|

## Provenance
| Claim | Verified | Partial | Missing | External |
|---|---|---|---|---|

## Accepted risks
- <risk, and why it is accepted rather than covered>

**Verdict:** safe to land | safe with manual actions | not safe (blockers listed)
```

Every manual action gets a verification command, not a description of what
should be true afterward.
