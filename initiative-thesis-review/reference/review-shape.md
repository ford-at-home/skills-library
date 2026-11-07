# The shape of the review

```markdown
# Thesis Review — <initiative>
**Trigger:** <type> — <what specifically changed, cited>
**Period covered:** <span> · **Cost this period:** <quantified>
**Recommendation: <continue | kill | pivot | escalate>**

## Tenets
### <tenet statement>
- Source: <written | synthesized from the authorizing document>
- Needs ratification: <true | false>
- Status: <valid | invalid | unknown>
- External evidence: <cited from external_context_changes — required>
- Do the metrics agree with that evidence? <yes | no | partially>
- Metric satisficing: <true | false> — <if true, what the metrics are missing>

## Drift narrative
<Two paragraphs. How the premise has evolved; what is being shipped versus what
was promised.>

## Rationale
<Cites tenet status and external context. Not sunk cost.>

## Opportunity cost
| Alternative the team could work on | Why it is stronger or weaker | If killed, what replaces this |
|---|---|---|

## If pivot
- New hypothesis: <specific> · Validation needed: <what would confirm it>

## If escalate
- Target: <named individual or role>
- Decision needed: <a specific question, not "what should we do">
- Briefing: <3–5 sentences someone can act on>

## Flags
- Metric satisficing warning: <true | false>
- Authorizing document needs revision: <true | false>
```

Every claim carries one tag: `[fact]` (sourced), `[assumption]` (believed,
untested), `[inference]` (derived from facts above), `[open question]`.
