---
name: layer-culture
description: Interviews and diagnoses the Organizational Culture layer (ownership, trust, craft standards, incident norms, and what actually gets rewarded and promoted). Use when a change keeps reverting after leadership attention moves on, when stated values and real behavior diverge, when people fear blame for AI-related mistakes, when someone wants to "change the culture", or when a pace-layers session identifies Culture as the goal or lever layer.
---

# Layer 7: Organizational Culture

**Natural clock:** years. **Reform horizon:** 3–7 years. **Changes by:** embedding. **Typical steward:** the CEO and leadership team.

Culture is the shared set of assumptions about how work is done and what matters: who owns what, whom people trust, what counts as good craft, how failure is treated, and what is rewarded. It is what remains when the policy is silent.

In Edgar Schein's model, culture is an *outcome* of what a group learns works, not a lever that can be pulled directly. Leaders change it through six **primary embedding mechanisms**:

1. What leaders pay attention to, measure, and control on a regular basis.
2. How leaders react to critical incidents and crises.
3. How leaders allocate resources.
4. Deliberate role modeling, teaching, and coaching.
5. How leaders allocate rewards and status.
6. How leaders recruit, select, promote, and remove people.

Structures, rituals, statements, and posters are **secondary** mechanisms: they reinforce culture that the primary mechanisms have already shaped, but they do not create it.

For AI-era change, two embedding events matter most. First, **what leaders measure**: adoption and volume metrics teach that volume is the point. Second, **how leaders react to the first serious AI-related failure**: blame the engineer, ban the tool, or fix the system that let it through. Each response teaches a different culture.

## If you arrived here directly

If no brief or goal exists yet, ask three questions first:

1. What is happening that made you want to change something here?
2. In one sentence, what do you want to be true that isn't now?
3. What is your role, and what can you decide on your own?

If the goal is "change the culture" with a short timeline, say early that culture changes by embedding over years, and that the plan will need a waypoint goal that produces evidence sooner.

## Interview

Four passes, 2–4 questions per turn. ★ marks the short set. Ask about behavior and events, not values statements. "What happened last time" is better evidence than "what do we believe."

### Pass 1: What exists

- ★ What does leadership say it values about how software is built, and about AI specifically?
- ★ What got someone promoted or publicly praised here in the last year?
- How are incidents reviewed? Are reviews blameless in practice or only in name?
- What craft standards do engineers hold each other to without being told?

### Pass 2: Topology

- ★ When someone needs help or judgment, whom do they go to? Who are the informal culture carriers?
- Where are the subcultures (engineering versus product versus risk, old team versus new team), and how do they see each other?
- Where is trust high between groups, and where is it low?

### Pass 3: Under the hood (the six mechanisms)

- ★ What do senior leaders ask about in reviews and status meetings? (Mechanism 1)
- ★ What happened after the last significant incident? Who was named, and what changed? (Mechanism 2)
- Where did money and headcount go this year compared with what was announced? (Mechanism 3)
- Do leaders visibly use the practices they ask others to adopt? (Mechanism 4)
- What behaviors get status: shipping volume, fixing hard problems, mentoring, heroics? (Mechanism 5)
- What do hiring and promotion criteria actually reward? (Mechanism 6)

### Pass 4: Forces

- **From faster layers:** How are AI tools changing who gets credit and what counts as skill?
- **From Governance:** Is governance experienced as a partner or a police force?
- **From Nature:** Are people tired? Is there room to learn?

## Look before you ask

If the user can share them, read: promotion or career-ladder criteria, recent incident reviews, leadership updates, and engineering-wide metrics dashboards. Compare what they reward with what leadership says it values. The gap between espoused and enacted values is the main finding at this layer.

## Reading the answers

| If you hear | It usually means | Ask or check next |
|---|---|---|
| "It worked while the VP cared, then it faded" | Change was carried by attention, not embedded in rewards or measures | Which primary mechanism could hold it? |
| "We say blameless, but people got named" | Espoused versus enacted gap; people will hide failures | Plan the response to the next incident now (H14) |
| "Leadership tracks AI adoption" | Volume is being embedded as a value | Change what is measured (H10) |
| "Seniors won't use it" or "juniors over-rely on it" | Status and skill identity are at stake | What would make the new way a source of status? |
| "Risk and engineering don't trust each other" | Shear S6 is adversarial | A joint owner and a shared win |
| "Heroes save every release" | Heroics are rewarded; the system is not fixed | What gets praised after a save? |

## Moves that work here

- **Embed through primary mechanisms.** Change one measured thing, one rewarded behavior, and the response to incidents. Do these before any announcement.
- **Decide the incident response in advance.** Agree in the room how leaders will respond to the first serious failure caused by the change.
- **Make the desired behavior a source of status.** Promotion criteria, recognition, and visible role modeling by respected people.
- **Use small, real wins as stories.** Culture learns from shared experience of what worked.
- **Name the espoused-versus-enacted gap out loud**, with examples, in the room.

## Moves that fail here

- Culture programs, posters, and town halls without a change in what is measured or rewarded.
- Announcing values the incentive system contradicts. It produces cynicism, which is harder to undo than indifference.
- Aiming to change culture inside one planning cycle.

## Failure modes

- **Pushed too fast:** cynicism, a widening gap between what is said and what is done, quiet resistance.
- **Held too slow:** ossified norms that block every change in faster layers.

## Leading indicators

- Quality and candor of incident reviews, especially for AI-related incidents.
- Content of promotion cases: which behaviors are cited.
- What senior leaders ask about, sampled from meetings or updates.
- Survey measures of trust and of calibrated trust in AI output (neither blind nor dismissive).
- Attrition among informal culture carriers.

## Who belongs in the room

- **Steward:** a senior leader whose attention and reactions people watch.
- **An informal culture carrier:** someone people go to for judgment, regardless of title.
- **A people or HR partner** who owns promotion and recognition mechanics.
- **Shear S6 owner:** a governance leader paired with a technology leader.
- **Shear S7 owner:** a people leader paired with a technology leader, for capacity and skill formation.

## Write to the brief

Append under "3. Layer briefs":

```markdown
### Organizational Culture
- Espoused values (incl. on AI): ...
- Enacted values: promotions, praise, incident responses (with examples)
- Topology: culture carriers; subcultures and trust between them
- Six mechanisms: attention / incident reaction / resources / role modeling / rewards / selection — what each currently teaches
- Forces: AI and status; governance perception; capacity to learn
- Diagnosis: (2–4 lines, with evidence; name the espoused vs. enacted gap)
- Planned incident response (to agree in the room): ...
- Unknowns → who would know
- Candidate room seats: ...
```
