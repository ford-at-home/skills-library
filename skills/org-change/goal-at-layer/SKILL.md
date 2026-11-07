---
name: goal-at-layer
description: Turns a vague change ambition into a precise goal pinned to a pace layer, with the lever layer, a realistic horizon, evidence for done, constraints, anti-goals, and an owner. Use after gathering the situation in a pace-layers session, or on its own when someone says they want to "adopt AI", "go faster", "fix our releases", "modernize", or "change the culture" and the real goal is unclear, set at the wrong layer, or unrealistic for its timeline.
---

# Goal at layer

The goal is the most important artifact in the whole process. A goal set at the wrong layer produces a plan that works on paper and changes nothing. This skill does one job: it leaves the user with a goal statement they have confirmed in their own words.

## Three layers to separate

Every change has up to three layers involved, and they are often different:

- **Surface layer**: where the symptom shows up. ("Reviews take a week.")
- **Goal layer**: whose contents must be different when you are done. ("Changes are reviewed within a day without more incidents.")
- **Lever layer**: what must change for the goal to happen *and stay happened*. (Review capacity and batch size, or who is allowed to approve, or what reviewers are rewarded for.)

Fast layers get the attention; slow layers hold the power. The lever is usually one to three layers slower than the surface. The layer definitions are in `../pace-layers/references/model.md`. If you cannot read that file, use: Generation, Integration and Verification, Product and Coordination, Platform and Infrastructure, Domain Architecture and Systems of Record, Governance, Organizational Culture, Nature, from fastest to slowest.

## If you arrived here directly

If there is no situation summary in the conversation or in a `brief.md`, ask three questions first:

1. What is happening that made you want to change something?
2. What is your role, and what can you decide on your own?
3. What has been tried already?

## The steps

Ask 2–4 questions per turn. Reflect back after steps 3, 5, and 8.

### 1. Get the raw goal in the user's words

"In one sentence, what do you want to be true that isn't true now?" Write it down exactly. You will compare the final goal to it.

### 2. Convert activity into outcome

Most raw goals are activities ("roll out agents", "stand up a platform team", "write an AI policy"). Ask, repeatedly if needed:

- "If that were done, what would be different, and who would notice first?"
- "Why does that matter, and to whom?"

Stop when you reach a state of the world the user actually cares about and could observe. Do not climb past it into corporate abstractions ("increase shareholder value").

### 3. Locate the goal layer

Which layer's contents must be different when you are done? Offer the two or three most likely layers as choices, with one line each on what "done" would mean in that layer. If the user picks more than one, the goal is probably two goals. Split them and ask which comes first.

### 4. Locate the lever layer with the reversion test

Ask: "Suppose you got the outcome next month by heroic effort. Six months later it has slipped back. What pulled it back?"

The force that restores the old state lives in the lever layer. Common answers and where they point:

| What pulled it back | Lever layer |
|---|---|
| "People went back to the old tools" or "the new tool got banned" | Governance or Platform |
| "The queue came back" | Verification capacity, or Nature (human review limits) |
| "Priorities shifted and the work got dropped" | Product, or Governance (funding cycle) |
| "Every change still needed three teams" | Domain Architecture (Conway's law) |
| "The core system wouldn't allow it" | Domain Architecture and Systems of Record |
| "Audit or security said no" | Governance |
| "People stopped caring once leadership moved on" | Culture |
| "The team burned out" | Nature |

### 5. Test the horizon

Ask for the desired timeline, then compare it with the lever layer's reform horizon:

- Generation: weeks
- Integration and Verification: 2–4 quarters
- Product and Coordination: 2–4 quarters
- Platform and Infrastructure: 1–2 years
- Domain Architecture and Systems of Record: 3–7 years
- Governance: 1–3 years
- Culture: 3–7 years
- Nature: not reformable; design within it

These are heuristics. Ask whether the user has evidence of how fast comparable changes moved in their organization, and use that instead if they do.

There are three outcomes:

- **It fits.** Proceed.
- **The timeline is shorter than the horizon.** Do not just accept it. Propose a pair of goals:
  - A **waypoint goal** at a faster layer that produces evidence within the timeline.
  - The **durable goal** at the lever layer with an honest horizon.
  
  Example: "By the end of Q1, one team runs risk-tiered review and halves time in review without a rise in change failures (waypoint). By Q4, risk-tiered review is the default and review capacity is planned like any other capacity (durable)."
- **The timeline is far longer than needed.** The problem may be a fast-layer problem being treated as a transformation. Say so.

### 6. Define "done" with evidence

Ask for 2–4 observable indicators:

- At least one **leading** indicator that moves early (weeks).
- At least one **lagging** indicator that confirms the outcome (quarters).
- At least one **guardrail**: a metric that must *not* get worse. When speed is the goal, the guardrail is usually stability or quality.

For each, ask: "Who measures this today? If no one, who would?"

Watch for proxy goals. If an indicator would reward gaming (adoption counts, pull-request volume, survey-reported time saved), pair it with a guardrail or replace it.

### 7. Constraints, non-negotiables, and anti-goals

- "What must not change, or must not get worse?"
- "What are you deliberately *not* trying to do?" Anti-goals stop scope creep and reassure the slow layers.
- "What budget, people, or political capital do you actually have?"

### 8. Authority and ownership

- "Who has to agree for this goal to be legitimate?" Usually the steward of the lever layer.
- "Who owns this goal: you, or someone you need to recruit?"

If the user does not have authority over the lever layer and does not plan to involve the person who does, flag it plainly. This is the single most predictive failure in organizational change. It also determines the most important seat in the room.

### 9. Write and confirm the goal statement

```text
GOAL
By <horizon>, <observable change> in <goal layer>,
made durable by changing <lever layer>,
evidenced by <leading indicator>, <lagging indicator>, guarded by <guardrail>,
without <constraints>.
Not trying to: <anti-goals>.
Owner: <role or name>.  Needs agreement from: <role or name>.
Waypoint (if any): By <shorter horizon>, <evidence-producing change at a faster layer>.
```

Read it back. Ask the user to restate it in their own words. If their restatement differs, the difference is the next question.

## Quality checks

Before finishing, run these. Fix any that fail.

| Check | Fails when |
|---|---|
| Outcome, not activity | The goal names a tool, a team, or a program instead of a changed state |
| One goal layer | The goal needs two layers to be "done" (split it) |
| Lever named | No slower layer is identified, or the lever equals the surface layer with no reason given |
| Horizon honest | The timeline is shorter than the lever layer's reform horizon and there is no waypoint |
| Observable | No indicator could be checked by someone outside the team |
| Guarded | Nothing stops the goal from being hit by degrading something else |
| Owned | No person owns it, or the owner cannot influence the lever layer |
| "Nothing else changed" test | If only this changed, the user would still be dissatisfied (the real goal is elsewhere) |

## Common goal pathologies

| Pathology | Example | What to do |
|---|---|---|
| Tool goal | "Get everyone using coding agents" | Ask what the tool is for; the outcome is usually at Verification or Product |
| Velocity goal | "Ship twice as fast" | Compute the ceiling (Amdahl), then locate the dominant wait state |
| Culture by decree | "Make us more innovative by Q2" | Culture changes by embedding over years; find the primary mechanism and set a waypoint |
| Everything goal | "Modernize engineering" | Split by layer; pick the one that unblocks the others |
| Proxy goal | "Raise AI adoption to 80%" | Ask what adoption is supposed to cause; make that the goal and keep adoption as a leading indicator only |
| Someone else's layer | An engineer aiming to change funding policy alone | Keep the goal, and make recruiting the lever-layer owner the first move |

## Write to the brief

Append to section 2 of `brief.md`, or print it if you cannot write files:

```markdown
## 2. Goal
- Raw goal (user's words): ...
- GOAL statement: (the block above)
- Surface layer: ... · Goal layer: ... · Lever layer: ...
- Reversion test answer: ...
- Horizon: desired ... vs. reform horizon ... → fits | waypoint added | over-scoped
- Indicators: leading ... / lagging ... / guardrail ... (who measures)
- Constraints: ... · Anti-goals: ...
- Owner: ... · Needs agreement from: ...
- Quality checks: passed | fixed: ...
```

Then return to the `pace-layers` flow (Phase 3), or tell the user which layer skill to run next.
