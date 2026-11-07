---
name: initiative-thesis-review
description: Decide whether one initiative is still worth pursuing by testing its tenets — the "if we are wrong about X, we should stop" statements — against external evidence consulted before the dashboard, and refusing to return continue while any tenet is invalid. Requires documented external context changes as an input, because without them a tenet check collapses into a metrics check. Exists to catch the case where output metrics sit inside target while the belief the initiative was funded on has quietly collapsed, because the team narrowed what it measures to the part still working. For one initiative, not allocation across several. Trigger phrases include should we still be doing this, is this still the right bet, thesis check, pivot or kill, tenets review, do we still believe this, the numbers look fine but.
---

# Initiative Thesis Review

Test whether the belief an initiative was funded on still holds, using evidence
from outside the initiative.

Writing falsifiable kill criteria, pre-committing to exit conditions, and refusing
sunk-cost arguments are all well-covered ground. What this enforces is narrower:
external evidence is consulted **before** the metrics and wins when they conflict,
`continue` is unavailable while any tenet is invalid, and a tenet the reviewer
wrote rather than the team cannot be the thing that kills an initiative.

A **tenet** is a falsifiable statement of the form *if we are wrong about X, we
should stop*. Without them a team will always find a metric that justifies
continuing, and will always be telling the truth when it does.

Output is a **review** ending in continue, kill, pivot, or escalate. It is
event-driven, not a standing meeting.

## Use when

- External context moved — market, regulation, a competitor, an underlying
  technology — and the question is whether the premise survives
- Someone close to the work has openly questioned whether a tenet still holds
- A metric anomaly has persisted past what an operational review can resolve
- A budget cycle is about to renew the initiative by default

## Don't use when

- The question is last week's operational performance, or what broke in an
  incident. Different reviews
- The initiative was authorized last month and nothing has changed. The
  authorizing document is the contract; don't re-litigate it without a trigger
- The real question is allocation across several initiatives rather than the
  premise of this one. That is a portfolio question and this operates at N=1
- The question is whether the *targets* were set at honest difficulty
- A specific irreversible action is queued and you want to know whether to let it
  fire. That is a commit gate, not a thesis review
- The caller wants confirmation the initiative is still right. Refuse

## Inputs

Ask for these. Don't infer them.

```yaml
tenets:                 # the "if we are wrong about X, stop" statements.
                        # Optional — synthesized and flagged if absent
authorizing_document:   # REQUIRED. What the initiative was funded on, and the
                        # source for tenet synthesis
review_trigger:         # market_shift | competitor_move | regulatory |
                        # technology_shift | metric_anomaly | scheduled_annual |
                        # named_concern
trigger_detail:         # what specifically changed, cited
external_context_changes: # REQUIRED. Documented external shifts since authorizing
metrics_snapshot:       # current state of the success metrics
cost_this_period:       # quantified — headcount, money, opportunity time
competing_priorities:   # named alternatives this team could work on instead
review_period:          # what span this review covers
```

**If `external_context_changes` is empty, stop.** Without external context a tenet
check collapses into a metrics check, and a metrics check cannot detect the failure
this exists to catch. Route the caller to their operational metrics review.

**If both `tenets` and `authorizing_document` are absent, stop.** There is no
thesis on record, so there is nothing to falsify.

## Gates

| Gate | Passes when | If it fails |
|---|---|---|
| Trigger documented | `review_trigger` is one of the named values and `trigger_detail` cites a specific change | Reject. Reviews without triggers become theater, annual ones included |
| Tenets exist or are synthesized | `tenets` is non-empty, or synthesized from the authorizing document and tagged `[inference]` with ratification needed | Synthesize and flag. Never present synthesized tenets as the team's |
| External evidence per tenet | Each status cites `external_context_changes`, not the dashboard | Re-check against external context |
| Satisficing check run | Each tenet carries an explicit check: is the metric agreement consistent with the external evidence? | Run it, and emit the warning when it catches something |
| Recommendation matches tenets | `continue` requires zero invalid tenets | Force the harder recommendation |
| Opportunity cost named | `competing_priorities` names specific alternatives | "Other things" is not a comparison |
| Escalation is actionable | Target, decision needed, and briefing all populated | Populate them |

## Process

1. **Confirm the trigger.** Even a scheduled review must say what prompted asking
   now rather than six months ago. If the honest answer is the calendar, say so —
   that is a weaker trigger and the review carries the label.

2. **Locate or synthesize the tenets.** If written tenets don't exist, derive them
   from the authorizing document's rationale and its "we assume that" statements.
   Tag them `[inference]`, mark them as needing ratification, and say plainly that
   the team did not write them. The shape a tenet needs, and what disqualifies one,
   is in `reference/writing-tenets.md`.

3. **For each tenet, check external evidence first.** What in
   `external_context_changes` supports or contradicts it? Cite the specific change.
   Do this before looking at the metrics, in this order, deliberately.

4. **Then check whether the metrics agree with the external evidence.**

5. **Run the satisficing check.** If external evidence contradicts a tenet while
   metrics look fine, the tenet is **invalid**. The metrics are measuring something
   narrower than the initiative. This is the step the whole skill is built around.

6. **Write the drift narrative.** Two paragraphs: how the premise has evolved, and
   what the team is actually shipping versus what the authorizing document promised.

7. **Assess opportunity cost** against named alternatives.

8. **Derive the recommendation** from the logic below. Do not soften it.

## Tenet status

| Status | Meaning |
|---|---|
| **valid** | External evidence still supports it |
| **invalid** | External evidence contradicts it |
| **unknown** | Insufficient evidence to judge either way |

A status must cite external context. A tenet marked valid on the strength of the
dashboard has not been checked.

## Recommendation logic

```text
all tenets valid                            → continue
some unknown, none invalid                  → continue, with the monitoring named
one or more invalid, scope is local         → pivot
one or more invalid, the premise is broken  → kill
decision authority sits above this review   → escalate
```

| Recommendation | Meaning |
|---|---|
| **continue** | Keep investing. Requires that no tenet is invalid |
| **kill** | Stop investing. The premise doesn't hold |
| **pivot** | The premise has changed and the tenets need restating |
| **escalate** | The decision genuinely sits above this review |

## Hard rules

Each of these prevents a failure that produces a plausible-looking review. That is
why they are rules rather than advice — nothing downstream signals that one was
violated.

```text
External context speaks before metrics. Always in that order.
A tenet is invalid if external evidence contradicts it, whatever the dashboard says.
Synthesized tenets carry needs_ratification and cannot alone drive a kill.
Never narrow a tenet at review time to whatever the evidence happens to support.
```

The last rule is the most common way this review fails while appearing to succeed.
A tenet that said "engineering managers at companies with 25 to 100 engineers will
pay for this" quietly becomes "some managers find this useful", which is true,
unfalsifiable, and passes.

## Stop instead of guessing

- **No tenets and no authorizing document** → stop. No thesis on record.
- **`external_context_changes` is empty** → stop and route to an operational
  metrics review.
- **The trigger is vague — "just checking in", "it felt like time"** → ask what
  prompted the question now. If the honest answer is the calendar, record that.
- **The initiative has not shipped anything the premise could be tested against**
  → stop. A premise that has not met reality cannot be falsified by it, and killing
  an initiative on a check it was never able to pass is not a finding.
- **Asked to confirm the initiative is still right** → refuse, and offer to surface
  the evidence that it isn't.
- **A tenet is unfalsifiable as written** — "customers want better software" → say
  so, mark it unknown, and do not silently substitute something falsifiable you
  invented.
- **Only synthesized tenets are invalid, and they would drive a kill** → escalate
  for ratification instead. Do not kill an initiative on tenets the team never
  agreed to. A kill on unratified tenets is indistinguishable in the artifact from
  a legitimate one, which is why this is a refusal rather than a caution.

## Further reading in this folder

- `reference/writing-tenets.md` — the four fields a tenet needs when the initiative
  is authorized, and what disqualifies one
- `reference/review-shape.md` — the review template and the claim tags
- `reference/failure-modes.md` — six ways this review appears to succeed and does
  not, starting with the metric satisficing it exists to catch
