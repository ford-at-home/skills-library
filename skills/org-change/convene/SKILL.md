---
name: convene
description: Turns a pace-layers analysis into a plan document and the roster of people to bring into the room to review it together, plus a facilitated "imagine the future" session and a short pre-read invitation. Use at the end of a pace-layers session, or whenever someone has a change goal and needs a plan with moves sequenced by pace, the decisions that need owners, and the right decision makers, subject-matter experts, and skeptics in one room.
---

# Convene

This skill produces four things:

1. **The plan document**: goal, situation, layer and shear findings, insights, moves sequenced by pace, decisions, risks, indicators.
2. **The room**: the few people who need to review the plan together, why each one, and what each one brings.
3. **The session**: a 90-minute agenda for the room to imagine the future the plan describes, test it, and decide.
4. **The pre-read**: a short invitation each person receives before the session.

The plan is a draft for the room, not a verdict. The goal is the anchor. The room exists to argue about trade-offs openly and to make the decisions that belong to the people in it.

## Step 1: Check readiness

Read the brief (`pace-layers/<slug>/brief.md`, or the conversation). Confirm you have:

- A confirmed goal statement with goal layer, lever layer, horizon, indicators, and owner.
- At least one layer brief for the lever layer.
- At least one shear checked, with a bottleneck prediction.
- Insights the user has reacted to.

If something is missing, tell the user what, and offer either to fill the gap now (a few questions) or to proceed with the gap marked as an open question in the plan. Never invent findings to fill a gap.

## Step 2: Sequence the moves by pace

Group every move into three horizons. Pace, not priority, decides the group.

- **Now** (weeks): fast, reversible moves that produce evidence. Usually experiments in faster layers that test the theory of change, plus measurement that is not yet in place.
- **Next** (one to three quarters): capacity, interface, and ownership changes at the shears and middle layers.
- **Commit** (longer, and requiring the room's decision): changes to the lever layer itself, such as policy, funding, structure, promotion criteria, or core-system boundaries.

For each move, record: what it is; the layer; the mechanism (why it should work, in layer terms); the owner; whether it is a **two-way door** (easy to reverse) or a **one-way door** (hard to reverse); the indicator it should move; the condition for stopping or continuing; and what it depends on.

Then check the sequence:

- Every Commit move has a Now move that produces evidence for it (fast proposes, slow disposes).
- The predicted next bottleneck gets capacity or an inflow cap *before or alongside* the speedup.
- Every shear the plan crosses has an owner, or "assign an owner" is itself a decision.
- At least one move changes a primary embedding mechanism if culture is involved (what is measured, rewarded, or how incidents are handled).
- Load on people does not rise without something being stopped.

## Step 3: List the decisions

The room exists to decide. List each decision the plan needs:

| Field | Content |
|---|---|
| Decision | Phrased as a question with options |
| Recommendation | Yours, with the reasoning, clearly labeled as a recommendation |
| Who decides | The person with the authority, by role or name |
| Door | One-way or two-way |
| By when | Date, or the evidence that triggers it |
| What would change it | The evidence that would reverse the recommendation |

Always include these decisions when they apply:

- Who owns each unowned shear.
- How leaders will respond to the first visible failure caused by the change (blame, ban, or fix the system). Recommend "fix the system."
- What the plan will stop doing to make room for itself.

## Step 4: Choose the room

Use five rights: the **right people**, in the **right room**, at the **right intervals**, with the **right context**, and with the **right ownership** of each decision.

### Seats

Fill these seats. One person can hold more than one. Keep the room to 5–9 people. Everyone else goes on the review list.

| Seat | Who | Why the seat exists |
|---|---|---|
| **Decision makers** | One each from business, product, and technology, with authority over the goal layer or the lever layer. The lever-layer steward is mandatory. | Decisions made without them get unmade later. |
| **The slow seat** | Whoever can say no from the layer just slower than the lever (often governance, architecture, or finance). | Slow layers hold the power. Bring the veto in early, when it can shape the plan, not late, when it can only stop it. |
| **Shear owners** | The owner of each shear the plan crosses, or the person proposed to own it. | Most failures happen at boundaries nobody owns. |
| **Subject-matter experts** | The theory holders found in the layer interviews: people who know how the system works in detail. | They know what will break. |
| **The fast voice** | Someone who will live with the change day to day. | They know what people will route around. |
| **Capacity** | Someone accountable for people's load (an engineering manager or people partner). | Nature does not negotiate. |
| **The skeptic** | Someone who disagrees with the theory of change, chosen on purpose. | Disagreement is the room's best evidence. |
| **The driver** | Whoever holds the thread: maintains the brief, the decision log, and the plan between sessions. Usually the user. An AI assistant can help hold the durable context, but a person owns it. | Without a driver, the room's decisions evaporate. |

### For each person, record

- Name (if the user gives it) or role.
- Seat(s) and layer.
- Why this person specifically.
- What they bring: **context** (what they know), **tools** (systems or access they control), **method** (how their group works), **judgment** (which decisions they have authority over).
- What they decide, and what they could veto.
- Concerns they have actually stated, if known. Do not speculate about motives.
- The one question they should answer before the session.

### Ask the user

- "Who holds each of these seats for you? Give names or roles."
- "Is anyone with veto power missing?"
- "Is anyone on the list only to observe?" Move observers to the review list.
- "Who will be upset not to be invited?" Add them to the review list with a reason.

### Cadence

- **Working sessions** follow the clock of the fastest layer the plan changes (often weekly or biweekly at first).
- **Decision checkpoints** follow the reform horizon of the lever layer (often quarterly).
- Set the date of the next convening before the session ends.

## Step 5: Design the session

Use `templates/session.md`. Adapt the timings to the room and the goal. The core sequence is: frame the goal, imagine success working backward from the future, imagine failure (a pre-mortem), walk the plan by pace, decide, commit.

Two rules matter most:

- **Slow speaks first** in the future-back exercise. Slower layers set the constraints that faster layers have to work within.
- **Recording is off by default.** If anyone wants a transcript, announce it at the start and get everyone's agreement. People argue less openly on the record, and open argument about trade-offs is the point of the room.

## Step 6: Write the files

If you can write files, create them next to the brief:

- `pace-layers/<slug>/plan.md` from `templates/plan.md`
- `pace-layers/<slug>/invite.md` from `templates/invite.md` (one short pre-read, with a per-person question list)

If you cannot write files, print the plan in full and then the invitation.

Writing rules:

- Lead every section with its conclusion.
- Cite evidence from the brief for every finding. Mark hypotheses as hypotheses.
- Mark the horizons as heuristics calibrated (or not yet calibrated) to the organization's own data.
- Keep names out of the plan unless the user asked for them. Roles are enough for a document that may be forwarded.
- No secrets, credentials, or personal details the plan does not need.

## Step 7: Review with the user

Before finishing, read back a five-line summary: the goal, the lever, the biggest insight, the most important decision, and who must be in the room. Then run these checks and fix failures:

- [ ] The goal is an outcome, pinned to a layer, with an honest horizon or a waypoint.
- [ ] The lever layer's steward is in the room.
- [ ] Every crossed shear has an owner or an ownership decision.
- [ ] The next bottleneck is predicted and addressed.
- [ ] Speed metrics are paired with stability or outcome guardrails.
- [ ] The response to the first failure is a decision on the list.
- [ ] Something is being stopped to make room.
- [ ] Every Commit move has evidence from a Now move behind it.

Ask: "What in this plan would embarrass you in front of the room?" Fix that too.

Then tell the user where the files are and suggest one next step, usually sending the pre-read.
