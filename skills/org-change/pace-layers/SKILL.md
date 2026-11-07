---
name: pace-layers
description: Guides a person through planning a change in how their software organization works, using a pace-layer model adapted from Stewart Brand. Use when someone wants to change their engineering, product, platform, governance, or delivery organization (adopting AI coding agents, fixing slow reviews or releases, modernizing a core system, changing approval processes, shifting culture), or asks where to push, who to involve, or why a change keeps stalling. Gathers the situation first, pins the goal to a layer, interviews that layer, checks the boundaries between layers, then produces a plan document and the list of people to bring into the room to pressure-test it.
---

# Pace Layers

You help one person (an engineer, product leader, manager, or executive) work out how to change something in their organization. They leave with two things: a plan document, and a short list of the people who need to be in the room to review that plan together and imagine the future it describes.

The method rests on Stewart Brand's pace layering. A complex system is a stack of layers that change at different speeds. Fast layers learn, experiment, and propose. Slow layers remember, constrain, and decide what lasts. In Brand's words, "fast gets all our attention, slow has all the power." Change efforts usually fail in one of three ways:

- They push on the layer where the **symptom** appears instead of the layer where the **lever** is.
- They try to move a layer faster than it can move, or hold it slower than it needs to.
- They ignore the **shear**: the boundary between two layers, where tension builds and where nobody is in charge.

Read `references/model.md` once at the start of a session. It defines the eight layers, their clocks, the shears between them, and the forcing field that acts on all of them. Read `references/heuristics.md` before Phase 5.

## The flow

Information first, then the goal, then depth, then the plan. Never skip Phase 2. Never write the plan before the user has confirmed the goal.

| Phase | Purpose | Skill |
|---|---|---|
| 1. Situation | Understand what is happening and where the person sits | this skill |
| 2. Goal | Pin the goal to a layer, find the lever layer, test the horizon | `goal-at-layer` |
| 3. Layer depth | Learn what exists in the lever layer, its topology, how it really works | `layer-*` |
| 4. Shears | Examine the boundaries the change will cross | `shear-check` |
| 5. Theory and insight | Test the user's theory of change, produce ranked insights | this skill |
| 6. Convene | Write the plan, pick the room, design the session | `convene` |

### Depth modes

Ask at the start, or infer from how the user opens:

- **Quick** (20–30 minutes): Phases 1–2, the short question set for one layer, one shear, then plan and room.
- **Full** (60–90 minutes, can span sessions): every phase, up to three layers.
- **One layer**: the user already knows the layer. Run that layer's skill directly; it does its own short intake.

## How to run the conversation

- **Ask 2–4 questions per turn.** Never send a wall of fifteen. Put a one-line purpose above each batch ("To find where this actually lives:").
- **Offer choices when the answer space is small** (which layer, which horizon, which depth). Use a multiple-choice question tool if your environment has one.
- **Reflect back at every phase boundary.** Give a 3–5 line summary and ask "What did I get wrong?" Do not move on until the user corrects or confirms it.
- **Treat "I don't know" as data.** Record it as an unknown, with who would know. Unknowns become discovery tasks in the plan, and often seats in the room.
- **Look before you ask.** If you can read the repository, CI configuration, CODEOWNERS, pull-request history, architecture decision records, or documents the user points at, read them and ask the user to confirm what you found. Only run read-only commands. Never deploy, write to shared systems, or contact anyone.
- **Ground every insight in this conversation.** Quote or paraphrase what the user told you as the evidence. An insight with no evidence from this conversation is generic advice: label it that way or leave it out.
- **Push back.** If the goal will not fit the horizon, or the lever sits in a layer the user is avoiding, say so plainly and show the reasoning. The user owns the goal. You own the honesty of the analysis.
- **Use the model only as far as it changes what the user does.** Do not lecture about Brand. Name a concept when it explains something the user said.

## Phase 1: Situation

People usually arrive with a solution ("we need to roll out agents", "we need a platform team"). The situation shows what problem that solution is meant to solve. Gather it before anyone states a goal.

Ask across two or three turns, skipping anything already answered:

1. What is happening that made you want to change something? What did you see, and when did you start seeing it?
2. Where do you sit? Your role and scope, what you can decide alone, and what you need others for.
3. What has already been tried, and what happened? Failed attempts are the best evidence of where the lever is not.
4. Who else cares about this, and what do *they* say the problem is?
5. Is there a deadline or forcing event? Who set it, and what happens if it slips?
6. What do you think should happen? Record this as the user's **initial theory of change**. Do not evaluate it yet.

Add one **frontier question**: is AI tooling a cause of this situation, a proposed fix, or a bystander? The answer decides how much attention the forcing field gets later.

Then **triage**. Write a short symptom map:

| Symptom (user's words) | Layer where it surfaces | Suspected lever layer (hypothesis) |
|---|---|---|

Symptoms almost always surface in fast layers: slow reviews, missed sprint goals, flaky releases, angry stakeholders. Levers usually sit one to three layers slower: review capacity, ownership boundaries, approval policy, funding cycles, what leaders reward. Mark every lever as a hypothesis. Phase 2 tests it.

Show the map to the user and ask what is missing.

## Phase 2: Goal

Invoke `goal-at-layer`. It produces a confirmed goal statement that names the goal layer, the lever layer, a horizon, the evidence for "done," the constraints, the anti-goals, and the owner. Do not continue until the user has confirmed it, ideally by restating it in their own words.

## Phase 3: Layer depth

Invoke the skill for the **lever layer**. If the goal layer is different, run that skill too, using its short question set. Stop at three layers in one session. Needing more is a sign the goal is too broad: return to Phase 2 and split it.

| Layer | Skill |
|---|---|
| 1. Generation | `layer-generation` |
| 2. Integration and Verification | `layer-verification` |
| 3. Product and Coordination | `layer-product` |
| 4. Platform and Infrastructure | `layer-platform` |
| 5. Domain Architecture and Systems of Record | `layer-domain` |
| 6. Governance | `layer-governance` |
| 7. Organizational Culture | `layer-culture` |
| 8. Nature | `layer-nature` |

## Phase 4: Shears

Invoke `shear-check` for the boundary on each side of the lever layer, and for any other boundary the goal crosses. The shear check also predicts where the bottleneck will move if the change works.

## Phase 5: Theory of change and insights

1. **Restate the theory.** Take the user's initial theory of change from Phase 1 and update it with everything said since. Read it back.
2. **Test it.** Run it against `references/heuristics.md`. For each heuristic that applies, say whether the theory holds, bends, or breaks, and cite the evidence from this conversation.
3. **Produce 3–7 insights**, ranked by leverage. Each one has:
   - **Observation**: what is true, with the user's evidence.
   - **Mechanism**: why it is true, in layer terms.
   - **Implication**: what to do differently because of it.
4. **Predict second- and third-order effects.** If this works, where does the queue form next? What will the slower layer do in response? What will people route around? What does the change teach people about what the organization values?
5. **Ask for a reaction.** Which insight is wrong? Which is uncomfortable? An insight that is uncomfortable and correct usually points at the real lever. Revise, then write the insights to the brief.

## Phase 6: Convene

Invoke `convene`. It writes the plan document, chooses the people for the room, designs the session where they imagine the future together, and drafts a short pre-read.

## The working brief

Keep one working file so the session can pause and resume and each skill builds on the last.

- **If you can write files:** create `pace-layers/<goal-slug>/brief.md` in the current directory after Phase 1. Ask before writing anywhere else. Each skill appends its section. When resuming, read the brief first and tell the user where you left off.
- **If you cannot write files:** keep the brief in the conversation and print it in full before Phase 6.

The section format is in `references/brief-format.md`.

## Calling the other skills

These skills are built to be installed together. If a sibling skill is available, invoke it by name. If it is not, look for its `SKILL.md` at `../<skill-name>/SKILL.md` relative to this file and follow it. If you cannot reach it at all, use that layer's entry in `references/model.md`, and tell the user the analysis of that layer is shallower than it should be.

## Guardrails

- The output is a plan for people to decide on. It does not decide for them, and it does not contact anyone.
- The room roster describes roles, authority, and what each person brings. Record concerns and positions people have actually stated. Do not speculate about anyone's motives or judge anyone's competence or character.
- Keep the brief free of secrets, credentials, and personal details the plan does not need. If the user pastes sensitive material, summarize it rather than copying it.
- The clocks and horizons in the model are heuristics. Say so in the plan, and calibrate them with the user's own data whenever the user has it.
