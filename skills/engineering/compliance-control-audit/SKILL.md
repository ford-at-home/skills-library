---
name: compliance-control-audit
description: Audit running cloud infrastructure against a named control set and produce findings an auditor can re-derive and an engineer can act on. Reports what was not checked as loudly as what failed. Read-only; never changes infrastructure. Use before an audit window, after an infrastructure change, or when someone asks how compliant an account is. Trigger phrases include compliance audit, SOC 2 evidence, control gap analysis, are we compliant, findings report, security posture review, check our controls, audit readiness, CIS benchmark check.
---

# Compliance Control Audit

Check what infrastructure actually is against what a control set requires, and
write findings that survive being challenged.

Output is a findings report. This skill reads infrastructure state and writes a
document. It changes nothing.

## Gate: audit-only

```text
Permitted: describe, list, get, and equivalents.
Forbidden: create, update, put, delete, attach, detach, modify, tag, deploy,
           enable, disable, rotate, revoke, apply — and any dry-run of these.
```

Remediation belongs in a `recommendation` field addressed to a human, phrased as
advice rather than as a step taken: "set PubliclyAccessible to false", not
"setting PubliclyAccessible to false". If asked to fix, auto-fix, or "just close
the finding", stop and return the recommendation. A compliance tool with write
access eventually writes to the wrong account. There is no exception for a
low-risk-looking change.

## Use when

- An audit window is opening and you need defensible evidence
- A control set exists and you need to know which controls hold right now
- Infrastructure changed and you need to know what drifted
- Someone asks "are we compliant" and the answer needs coverage, not a percentage

## Don't use when

- You are building or changing infrastructure — that is provisioning work
- The question is whether one tenant can reach another's data. That is a boundary
  design question rather than a control check — use `multi-tenant-saas-isolation`
- You are clearing claims in a document rather than conditions in an account. Use
  `evidence-grounded-verification`
- You are designing the scoring scale itself rather than applying one. Use
  `anchored-rubric-design`
- No control set exists yet. Write one first; auditing against an unwritten
  standard produces opinions labelled as findings

## Inputs

```yaml
control_registry:   # path to the registry (see templates/control-registry.yml)
control_set:        # the named standard and the control IDs in scope
scope:              # accounts, regions, environments — named explicitly
credentials:        # what read access exists, and what it is denied
audience:           # external auditor, engineering lead, board
prior_report:       # path, or "none" — distinguishes new from carried-over
```

**If `scope` or `audience` is missing, stop and ask.** An empty findings list over
an unstated scope means either "compliant" or "we never looked at production", and
the reader cannot tell which.

## The control registry

The registry is the audit's scope statement and the part worth keeping. Edit
`templates/control-registry.yml`, where every field is documented inline.

Its one load-bearing property: the top-level `control_set` lists every control ID
in scope **including ones with no check**. Coverage is measured against that list,
which is what stops a deleted check from improving the numbers.

Adding a control means adding one entry and changing nothing else.

## Process

1. **Load the registry and restate the scope** before reading any infrastructure,
   including the environment filter. Most false-clean reports come from a default
   filter nobody noticed.
2. **Map each control to conditions, or refuse to map it.** A condition needs a
   read-only call, a field, and a comparison with its threshold written out. If
   you cannot name all three, record `out-of-technical-scope` with a reason.
   See `reference/mapping-controls.md`.
3. **Enumerate resources in scope first, then evaluate.** Record the count.
4. **Evaluate each condition to one of three states,** recording the observed
   value rather than the verdict.
5. **Verify, never trust, any marker asserting compliance.** A tag saying
   "compliant" is a claim by whoever wrote it.
6. **Apply exceptions last,** as a separate pass over completed findings. An
   exception moves a finding into the exceptions section; it never prevents the
   check from running.
7. **Rank by exposure** — internet-reachable before internal, production before
   dev, data-bearing before stateless. A report ordered by control number makes
   the reader do the triage.
8. **Diff against `prior_report`,** marking each finding new, carried-over with
   its age, or resolved.
9. **Write the coverage table before the findings.**

## Hard rules

Each of these prevents a failure that produces a plausible-looking report. That
is why they are rules rather than advice — nothing downstream signals that one
was violated.

```text
Read-only. No create, update, delete, deploy, or dry-run of a write.
Three states, never two. An error or denial is not-determined, never pass.
Zero resources found is not-determined, not a pass.
Coverage is counted against the full control set, never the implemented subset.
A compliance marker on a resource is a claim. Verify the condition itself.
Record the observed value and the threshold, never only the verdict.
An exception missing approver, date, expiry, or verified compensating
  control is a violation.
Exclusions match exact identifiers. Patterns get reported, not honoured.
Never emit a single compliance percentage or score.
Never print a raw account identifier. Use an alias.
```

The coverage rule is the one that gets argued with. A pass rate over only the
controls you implemented rises when you delete a failing check, which is exactly
backwards.

## Stop instead of guessing

- **No control set, scope, or audience** → stop and ask, naming every gap at once
- **A control has no checkable condition** → `out-of-technical-scope` with a
  reason. Do not substitute a proxy that happens to be checkable
- **A required call is denied** → `not-determined`, naming the call. Do not infer
  the value from a neighbouring resource or a previous report
- **Asked to remediate** → refuse, return the recommendation
- **Asked for a compliance percentage** → refuse the framing, return the coverage
  table. Compliance is an opinion an auditor issues over a period; this report is
  evidence for that opinion, not a substitute for it
- **Asked to soften findings before a deadline** → refuse, and offer to reduce
  scope explicitly instead. That limits the claim honestly rather than limiting
  the rigour behind it

## Further reading in this folder

- `reference/mapping-controls.md` — decomposing prose controls into checkable
  conditions, the two ways that goes wrong, and what a registry of this kind
  cannot cover
- `reference/report-shape.md` — the fields a finding needs to survive challenge,
  exception-versus-violation, and the report template
- `reference/failure-modes.md` — six ways a compliance audit produces a confident
  wrong answer, and which rule above catches each
- `templates/control-registry.yml` — the registry to copy and edit, every field
  documented inline
