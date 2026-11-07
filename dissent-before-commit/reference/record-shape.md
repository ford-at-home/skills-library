# What each recommendation means, and what the record looks like

| Recommendation | Meaning |
|---|---|
| **proceed** | Fires on schedule. The record goes into the audit trail |
| **proceed_with_changes** | Does not fire until the named changes are in place; then re-run |
| **pause** | Does not fire. Resume conditions named and watched |
| **escalate** | A named person gets a briefing and makes the call |

## Record template

```markdown
# Pre-Commit Record — <the specific action>
**Fires:** <date and time> · **Authorized:** <date>, in <artifact>
**Time since authorizing:** <span — over 30 days raises stale-dissent risk>
**Reversibility: <one-way door | two-way door | partial reversal>**
<what is recoverable, what is not, time and cost to reverse>

**Recommendation: <proceed | proceed_with_changes | pause | escalate>**

## State changes since authorizing
<Listed, or the positive assertion with its scope named.>

## Prior dissent, re-checked
| Objection | Still applies / No longer applies / New | Why |
|---|---|---|

## Perspectives canvassed
| Perspective | Consulted | Raised concerns | Rubber-stamp risk | Summary |
|---|---|---|---|---|

## Strongest case against firing
<One argument, stated plainly.>
- From: <named function, role, or stakeholder>
- Basis: <the evidence or reasoning, cited>

## Resolution
- Addressed in the action: <true | false>
- If addressed: <cite the specific change>
- If accepted: <the tradeoff> — owned by <named person> — because <rationale>

## If proceed_with_changes
<The specific changes required before it fires.>

## If pause
- Resumes when: <trigger> · Estimated resolution: <when>

## If escalate
- Target: <named individual or role>
- Decision needed: <a specific question, not "what should we do">
- Briefing: <3–5 sentences someone can act on>

## Flags
- Stale-dissent warning: <true | false>
```
