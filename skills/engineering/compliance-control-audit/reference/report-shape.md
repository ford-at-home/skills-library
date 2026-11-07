# What a finding carries, and what the report looks like

## Evidence a finding needs

A finding gets challenged by whoever owns the resource. It must answer "how do you
know" without a re-run.

```yaml
control_ids:    ["CC6.1", "CC6.3"]
condition_id:   public_flag
resource_id:    <identifier>            # exact, never a description
resource_scope: <region / account alias> # never a raw account number
state:          fail                    # pass | fail | not-determined
call:           "rds:DescribeDBInstances"
field:          "DBInstances[].PubliclyAccessible"
observed:       true                    # the value, not "non-compliant"
expected:       "false"
observed_at:    2026-07-27T13:20:00Z
exposure:       internet-reachable      # drives ranking
owner_hint:     <tag, stack, or repo that locates an owner>
recommendation: <text for a human>
first_seen:     2026-04-02              # carried over from prior_report
```

`state: not-determined` additionally records what blocked it — the denied call or
the missing field. A not-determined finding is a real output. It is the one most
often quietly dropped, and the one an auditor asks about.

## Exception or violation

An exception is a decision someone can be held to. It needs all five: the resource
by exact identifier, who approved it, when, when it expires, and a compensating
control **with a record of how that compensating control was verified to exist**.
Missing any one, it is a violation.

- **No expiry** → violation. A permanent exception is a silent standard change.
- **Expired** → violation, flagged as lapsed. Worse than a new finding, because
  someone already agreed to fix it.
- **Compensating control asserted but never verified** → violation. "Handled
  separately" is the usual form, and the separate handling is frequently absent.
- **Matched by pattern rather than identifier** → not an exception. Prefix and
  wildcard exclusions widen every time someone names a resource, so a new resource
  inherits a suppression nobody approved for it. If you inherit patterns, report
  each with the list of resources it currently matches.

## Report template

```markdown
# Compliance Findings — <control set>
**Scope:** <accounts, regions, environments>  ·  **As of:** <timestamp>
**Audience:** <who reads this>  ·  **Read-only. No infrastructure was modified.**
**Filter in effect:** <filter>  ·  **Resources excluded by it:** <count>

## Coverage
| | Count | Control IDs |
|---|---|---|
| In control set | | |
| Checked | | |
| Declared, not implemented | | |
| Out of technical scope | | |

## Not determined (read first)
| Control | Resource | Blocked by | What would settle it |
|---|---|---|---|

## Findings — ranked by exposure
### <control> — <resource>
- Exposure · State · Call · Field · Observed · Expected · Observed at
- First seen <date>, age <n> reports · Owner hint: <tag/stack/repo>
- Recommendation for human review: <text>

## Active exceptions
| Resource | Control | Approved by | On | Expires | Compensating control | Verified |
|---|---|---|---|---|---|---|

## Suppressions that do not hold
| Resource or pattern | Control | Why it no longer suppresses | Currently matches |
|---|---|---|---|

## Passed
| Control | Resources checked | Condition evidence |
|---|---|---|
```

The header carries the scope filter and its exclusion count because the most
common false-clean report is one that ran against an empty scope and said so
nowhere.
