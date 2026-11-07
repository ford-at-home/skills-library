# Mapping a control to conditions

Controls are written as outcomes; infrastructure exposes fields. The gap is where
the judgment is.

Take "backup jobs are monitored, failures alert, and failures are addressed
promptly". Unfalsifiable as written. It decomposes into three checkable
conditions: a snapshot exists within some age; retention is at least some number
of days; the alert topic has at least one confirmed subscriber.

Three calls, three fields, three thresholds — and the thresholds now live in the
registry where a reviewer can argue with them, rather than inside checking code
where nobody will read them.

## The two ways this goes wrong

**The restatement.** "Backups must be monitored" is the control again, not a
check. If it does not name a field, it is not mapped.

**The convenient proxy.** "An alert topic exists" is easy to check and does not
establish that anyone receives the alert. A confirmed subscriber does. Prefer the
condition that would actually fail when the control is violated — a proxy chosen
for checkability produces a passing report about something nobody verified.

## Controls that decompose into nothing

Controls about people, policies, cadence, or approvals usually have no checkable
condition. That is a correct result, not a failure of the mapping. Record them as
`out-of-technical-scope` and let the coverage table carry them.

## What a registry of this kind can cover

Infrastructure state a read-only API can observe. In practice that clusters in
logical access, network boundary, encryption at rest, monitoring, and backup — a
modest slice of any real control set.

It says nothing about control environment, risk assessment, change-management
approvals, personnel controls, or vendor review, which are evidenced by records
rather than API responses.

Report the slice you checked and the size of what you did not. Understating
coverage costs a conversation. Overstating it means someone relies on a control
that was never checked.
