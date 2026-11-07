# Mechanism — <name>

> Every section is required. A section you cannot fill in is a design gap, not a
> formatting problem.

---

## Goal

<One sentence. The outcome this mechanism keeps producing, in customer or system
terms.>

## Failure mode today

<The specific way this outcome does not happen now. Not "we don't do it" — what
the system actually does instead.>

## Operating cadence

- **Interval:** <daily | weekly | monthly | event-driven>
- **Day and time, if scheduled:** <e.g. "Tuesdays 10:00 ET">
- **Trigger, if event-driven:** <the specific event>

## Inputs

| Input | Source | Owner of source | Format |
|---|---|---|---|
|  |  |  |  |

## Process

1. <Step>
2. <Step>
3. <Step>

> Each step names an actor (who does it) and an artifact (what they read or
> produce). A step with neither is a wish.

## Outputs

| Output | Audience | Where it lives | Retention |
|---|---|---|---|
|  |  |  |  |

## Metrics

| Metric | Input or output | Baseline | Target | How measured | When evaluated |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

> Input metric: a leading indicator the team controls. Output metric: a lagging
> indicator the customer experiences. Both are required. A mechanism with only
> output metrics has nothing to steer with.

## Inspection

- **Inspector:** <named individual, and not the owner>
- **Inspection cadence:** <e.g. monthly>
- **Artifact the inspection produces:** <what the inspector writes or signs>

## Escalation rule

- **If:** <specific condition — include the case where the mechanism is skipped
  twice in a row>
- **Then:** <who notifies whom, within how long>
- **They do:** <the specific action, not "discuss it">
- **Owner of the escalation:** <named individual>

## How this mechanism will fail

- <A way it fails while continuing to look healthy>
- <…>

## Anti-patterns that signal decay

- <Observable behavior, e.g. "the agenda becomes purely informational">
- <…>

## First 30-day trial

- **Start date:** <YYYY-MM-DD>
- **Review date:** <YYYY-MM-DD>
- **Reviewer:** <named individual>
- **Pass criteria:** <measurable>
- **Fail criteria:** <measurable>

> Outcomes available at the review: keep, revise, or retire. All three are
> legitimate. "Ignore" is not.

## Claim tags

Tag every empirical claim above: `[fact]` (verifiable, with a source),
`[assumption]` (believed, untested), `[inference]` (derived from facts stated
above), `[open question]` (unresolved, and listed as such).
