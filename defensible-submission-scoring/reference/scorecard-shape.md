# Scorecard shape

One scorecard per submission, plus the two side files below.

```markdown
## <Submission> — <team>
**Statement:** <which one> · **Flags:** <list or NONE>

### What the statement requires
<Written before the submission was opened. User, environment, constraints, success.>

### Desirability
| Category | Score | Evidence |
|---|---:|---|
| Impact | | |
| Feasibility | | |
| User value | | |
| Execution | | |
| Innovation | | |
| Equity and inclusion | | |

**Weighted:** <award>: N/max · <award>: N/max

### Survivability
| Dimension | Score | Rationale |
|---|---:|---|
| Ownership clarity | | |
| Data readiness | | |
| Tech stack fit | | |
| Integration surface | | |
| Maintenance burden | | |

**Total:** N/25 — Tier <S/A/B/C/D>

### Verdict
- Strongest: <what>
- Weakest: <what>
- What must be fixed first: <one thing>
- Divergence: <desirability vs survivability, or "aligned">
```

Plus one `divergence.md` listing every submission where the two rubrics disagree,
with the structural reason, and one `unresolved.md` for null cells and gates that
could not be checked.
