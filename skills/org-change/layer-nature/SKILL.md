---
name: layer-nature
description: Interviews and diagnoses the Nature layer, the slowest pace layer, made of constraints an organization cannot change and must design within (human attention and cognitive load, review stamina, how engineers form skills and system knowledge, the labor market, compute cost and physics, and seasonal demand). Use when a change raises workload or review burden, when burnout, skill atrophy, or comprehension debt are concerns, when juniors are not learning, when compute costs matter, or when a pace-layers session identifies Nature as a constraint or lever.
---

# Layer 8: Nature

**Natural clock:** generational, or fixed. **Reform horizon:** none. You do not reform this layer; you design within it. **Typical steward:** shared between people, finance, and technology leaders, plus operations for seasonal demand.

In Brand's model, nature is the slowest layer and the one that punishes any faster layer that ignores it. His example is commerce pushing nature at commercial speed and destroying fisheries. The software version is agent output pushing human comprehension at machine speed.

For a software organization, nature includes:

- **Human cognition.** Limited working memory, the cost of interruptions and context switching, how review accuracy falls as changes get larger and reviews get faster, how trust in tools gets calibrated, and sustainable pace. Team Topologies treats cognitive load as a first-class design constraint.
- **Skill formation.** How engineers come to hold the theory of a system (Peter Naur's "programming as theory building"), and the junior pipeline that produces future experts. If juniors no longer form that theory by doing the work, the organization's ability to verify and maintain its systems declines years later.
- **The labor market.** Scarce skills, especially people who understand both a legacy core and the business it runs.
- **Physics and economics of compute.** Latency, inference cost, energy, rate limits, context-window limits.
- **Domain seasonality.** Peak periods, change freezes, and demand cycles specific to the business.

## If you arrived here directly

If no brief or goal exists yet, ask three questions first:

1. What is happening that made you want to change something here?
2. In one sentence, what do you want to be true that isn't now?
3. What is your role, and what can you decide on your own?

## Interview

Four passes, 2–4 questions per turn. ★ marks the short set. This layer is often present as a *constraint* on a goal set elsewhere. In that case, use the short set.

### Pass 1: What exists

- ★ How many systems, services, or domains is each team responsible for? Does that feel like too much?
- ★ When are the peak periods or freezes in your business calendar?
- What is on-call like: pages per person per week, night pages?
- What compute or AI budget exists, and is anyone near its limits?

### Pass 2: Topology

- ★ Where does cognitive load concentrate? Which people or roles are carrying too much?
- Who carries invisible load (reviews, mentoring, answering questions) that is not counted anywhere?
- How do new engineers learn how the critical systems work? From whom?

### Pass 3: Under the hood

- ★ Since AI tools arrived, has the load on reviewers gone up, down, or shifted to different people?
- ★ Are newer engineers still building a deep understanding of the systems, or mostly directing tools? How would you know?
- How long does it take a new engineer to make a meaningful change to a core system?
- What signs of burnout or fatigue are visible (attrition, sick leave, people declining work)?
- What does a typical change cost in inference and compute? Is it rising?

### Pass 4: Forces

- **From faster layers:** Which planned changes increase load on people (more review, more context switching, more on-call)?
- **From Culture:** Are hours or heroics rewarded? Is it acceptable to say "I'm at capacity"?
- **From the frontier:** How is AI changing which skills are scarce and how people learn?

## Look before you ask

If you can read team data the user shares, check:

- Reviews per reviewer per week (the verification skill's script reports reviewer concentration).
- On-call pages per person.
- Ramp time for recent hires to their first meaningful change in core areas.

Treat individual-level data with care. Report patterns by role or team, not by named person, unless the user asks otherwise for a legitimate reason such as protecting someone's time.

## Reading the answers

| If you hear | It usually means | Ask or check next |
|---|---|---|
| "Our best reviewers are drowning" | The S1 queue is landing on a few people; a hard human limit | Cap inflow; spread or automate review (H5, H11) |
| "Juniors ship a lot but can't explain it" | Comprehension debt; future verification capacity at risk | Protected learning; explain-before-merge norms |
| "We can't hire people who know the core" | A labor-market constraint on the domain layer | Knowledge capture; pairing; agent-assisted archaeology |
| "Everything happens during peak season" | Seasonality must shape the plan's calendar | Schedule risky moves outside peaks |
| "AI costs are creeping up" | A compute-economics constraint becoming visible | Add cost per change as an indicator |
| "People are tired" | The plan must reduce load before it adds change | What will the plan stop doing? |

## Moves that work here

- **Design within.** Treat attention, review stamina, and learning time as fixed capacity and budget against them.
- **Cap and rotate.** Limit review load per person; rotate on-call and review duty.
- **Protect skill formation.** Deliberate practice, pairing with theory holders, and norms where people can explain what they merge.
- **Budget compute openly.** Track cost per change and set limits before they are hit.
- **Respect the calendar.** Put risky changes outside peak periods and freezes.
- **Stop something.** Any plan that adds load should name what it removes.

## Moves that fail here

- Plans that assume people will absorb more review, more tooling, and more change on top of current work.
- Measuring individual output in ways that punish mentoring and review.
- Treating fatigue as a motivation problem.

## Failure modes

You cannot hold nature "too slow." You can only push against it:

- **Pushed:** burnout, rising error rates, skill atrophy, comprehension debt, loss of the few people who understand the core, and a junior pipeline that stops producing experts. These appear years after the decisions that caused them.

## Leading indicators

- Cognitive-load or workload survey results by team.
- Reviews per reviewer per week.
- Pages per on-call person.
- Ramp time for new engineers on core systems.
- Inference and compute cost per change.
- Attrition among theory holders and senior reviewers.

## Who belongs in the room

- **People partner (HR or engineering operations)** who can see workload and attrition.
- **A finance partner** if compute cost is material.
- **An engineering manager** who carries capacity decisions for the affected teams.
- **A recent hire** who can say how learning actually happens now.
- **Shear S7 owner:** a people leader and a technology leader, jointly.

## Write to the brief

Append under "3. Layer briefs":

```markdown
### Nature
- Cognitive load: systems per team; concentration; invisible load
- Skill formation: how theory is learned; junior ramp time; signs of comprehension debt
- Labor market: scarce skills
- Compute: budget, cost per change, limits
- Seasonality: peaks, freezes
- Forces: planned load increases; cultural norms about capacity; AI and skills
- Diagnosis: (2–4 lines, with evidence)
- Hard limits the plan must respect: ...
- Unknowns → who would know
- Candidate room seats: ...
```
