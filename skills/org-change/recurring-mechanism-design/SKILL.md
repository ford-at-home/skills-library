---
name: recurring-mechanism-design
description: Convert a goal into a recurring mechanism that keeps working after the motivation that set it is gone, by designing against silent decay specifically — the inspector is never the owner, escalation fires on a missed run rather than only on a bad result, and the author must name how the mechanism will fail while still looking healthy. Produces a spec, not a running process. Refuses a team as owner, "as needed" as a cadence, and a run that produces no artifact. Use when a one-off effort needs to become recurring practice, or when the current plan is "we will try harder". Trigger phrases include mechanism, operationalize, cadence, make this stick, process for this, how do we keep doing this, who owns this ongoing, turn this into a habit.
---

# Recurring Mechanism Design

Turn a goal into a mechanism that produces the desired behavior after the
motivation that set the goal is gone. Output is a **spec** — a design, not a
running process.

That goals need mechanisms rather than intentions is well-worn advice, and a
competent agent asked to "make this stick" will produce a cadence, an owner, and
a checklist unprompted. What it will not produce is a design that fails *loudly*.
Mechanisms rarely stop; they decay while continuing to emit their artifact on
schedule. Everything below exists to make that decay visible, and it is the only
part of this worth encoding.

## The four rules against silent decay

1. **The inspector is never the owner.** Owners marking their own homework is the
   default failure of every mechanism ever designed. The objection is always "the
   owner is closest to the work" — which is exactly the problem: they are also
   closest to the reasons a bad week was actually fine.
2. **Escalation fires on a missed run, not only on a bad result.** A mechanism
   that only escalates bad outputs cannot escalate the absence of outputs, and
   cadence drift — weekly to fortnightly to "when we remember" — is how they
   actually die.
3. **The author names how it fails while still looking healthy.** If they cannot,
   the design is not understood yet. That inability is the finding; do not supply
   an answer on their behalf and proceed.
4. **Trial pass and fail criteria are written before the trial starts.**
   Criteria written at review time are written to justify the outcome someone
   already prefers, and nobody wants to retire the thing at the review.

## Use when

- A goal has been set and no recurring practice supports it
- A one-off effort worked once and needs to become routine
- The plan is "we will try harder" or "we will keep an eye on it"
- A metric exists and nobody inspects it on a schedule
- A commitment was made in a document and nothing in anyone's week enforces it

## Don't use when

- The decision hasn't been made yet. This designs how to execute a decision, not
  whether to make it
- The mechanism already exists and needs running rather than designing. This
  produces specs, not meetings
- The mechanism failed and the question is why. That is a post-mortem on the
  mechanism, not a redesign from scratch
- A specific instance is about to fire and you want to know whether to let it.
  That gates one scheduled action rather than designing the recurring pattern
- The output is a one-time sequenced rollout of a message or change rather than a
  repeating cadence

## Inputs

Ask for these. Don't infer them.

```yaml
goal:                 # the outcome this must keep producing, in customer or
                      # system terms
failure_mode_today:   # the specific way it does not happen now. Required
desired_behavior:     # what people or systems do under the mechanism
cadence:              # an interval, or a named triggering event
owner:                # a named individual. Not a team, not a role
inputs:               # data or artifacts each run consumes, and who owns each
outputs:              # artifacts each run produces, and who reads them
inspection_method:    # how someone other than the owner confirms it is working
escalation_path:      # who is notified, when, and what they do
```

**If `failure_mode_today` is missing, stop and ask.** A mechanism designed
without knowing how the goal currently fails addresses the failure the author
found easiest to imagine. "It doesn't happen" is not a failure mode; *how* it
doesn't happen is.

## Process

1. **State the goal in customer or system terms.** Not "improve our process" —
   what does the customer or the system get that it doesn't get today?
2. **Diagnose today's failure mode specifically.** This is the step people skip,
   and skipping it produces a mechanism aimed at a failure that wasn't happening.
3. **Design the mechanism.** Fill in `templates/mechanism.md`. Every step names
   an actor and an artifact; a step with neither is a wish.
4. **Specify inspection.** Name who inspects, on what cadence, and what artifact
   the inspection itself produces.
5. **Specify escalation** concretely: if the mechanism is skipped twice in a row,
   who is told, by whom, within how long, and what they are expected to do.
6. **Pre-mortem it.** Name how it goes wrong, then name the anti-patterns — the
   observable behaviors that signal decay before it has visibly stopped.
7. **Define a 30-day trial** with measurable pass and fail criteria, a review
   date, and a named reviewer. All three review outcomes are legitimate: keep,
   revise, retire. "Ignore the trial" is not one of them.

## Hard rules

The four rules above are the design. These three are rules rather than advice for
a narrower reason: each describes a mechanism that arrives on schedule and reads
as healthy, so nothing downstream reports that it stopped carrying information.

```text
Every run produces an artifact. A run that leaves no trace did not happen.
A meeting with no inputs and no outputs is not a mechanism. It is a meeting.
A mechanism that can only report "everything is fine" is broken by construction.
```

## Output

`templates/mechanism.md`, filled in. Every section is required; a section that
cannot be filled in is a design gap, not a formatting problem.

## Stop instead of guessing

- **Owner is a team, a role, or a rotation with no named individual** → stop and
  ask. "The platform team" cannot be notified, cannot be inspected, and cannot be
  held to a cadence.
- **Cadence is "as needed", "regularly", or "ongoing"** → stop and ask for an
  interval or a triggering event. These three phrases are how a mechanism is born
  already dead.
- **The only proposed inspector is the owner** → stop and ask for a second party.
- **Escalation is "we will discuss it"** → stop. Ask who is notified, within how
  long, and what they are expected to do about it.
- **`failure_mode_today` is missing or restates the goal** → stop and ask.
- **The author cannot name a way the mechanism fails** → stop. Do not supply one
  on their behalf.
- **Asked to design a mechanism that will demonstrate the goal is being met** →
  refuse the framing. A mechanism built to produce reassurance will produce it
  regardless of the underlying state, and its first successful run is the last
  useful thing it does.

## How this goes wrong

**The one it exists to catch.** The mechanism runs on schedule, produces its
artifact, and reports that everything is fine, every single time. Nothing is
technically broken. It has stopped carrying information because it was designed
so that only one outcome was reachable. Check by asking what a bad week's output
would look like, and whether that output has ever appeared.

**Inspection by the same person.** The owner writes the artifact and also
confirms the artifact is good. Easiest defect to miss, because the spec
technically names an inspection step.

**Owner without authority.** The named owner cannot make anyone comply. Change
the owner or change the mechanism; do not ship a spec whose enforcement depends
on goodwill.

## Further reading in this folder

- `templates/mechanism.md` — the mechanism spec to fill in, carrying the owner,
  the cadence, the observable artifact, the second-party inspector, the
  escalation rule, and the trial's pre-written criteria as separate fields
