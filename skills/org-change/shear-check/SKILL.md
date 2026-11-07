---
name: shear-check
description: Diagnoses the boundaries ("shears") between adjacent pace layers, where tension builds because the two sides move at different speeds and where change efforts most often fail because nobody owns the boundary. Use after layer interviews in a pace-layers session, or on its own when work piles up between two groups, a handoff keeps failing, a speedup in one area created a queue somewhere else, or nobody can say who owns a boundary such as code generation vs. review, delivery vs. outcomes, platform vs. core system, or compliance vs. engineering.
---

# Shear check

A **shear** is the boundary between two adjacent pace layers. Because the two sides change at different speeds, tension builds there. Brand saw the shears as where a system learns: fast layers propose across them, slow layers constrain across them. They are also where most visible failures show up, and they rarely have an owner, because every org chart is drawn around layers, not boundaries.

This skill examines the shears a change will cross, names their owners (or their lack of one), and predicts where the bottleneck will move if the change works.

## The seven shears

| Shear | Between | Tension | Signature failure | Natural owner |
|---|---|---|---|---|
| S1 | Generation and Verification | Volume versus comprehension | Review queues, oversized changes, unreviewed merges, rising change failures | Harness or platform lead, often a staff-plus engineer |
| S2 | Verification and Product | Shipped versus valuable | Throughput up, outcomes flat | Value-stream manager or product operations |
| S3 | Product and Platform | Bespoke versus paved road | Shadow tooling, per-team agent stacks, unclear AI stance | Platform product manager |
| S4 | Platform and Domain | Edge speed versus core integrity | Generated customizations in the core, growing upgrade debt | Domain or enterprise architect; seam owner |
| S5 | Domain and Governance | Decision logic under policy or regulation | Untraceable rule changes, audit findings | Business owner of the logic plus risk or compliance, jointly |
| S6 | Governance and Culture | Compliance versus ownership | Checkbox controls, blame, tool bans | Risk or compliance leader with a technology leader |
| S7 | Culture and Nature | Ambition versus human limits | Burnout, skill atrophy, comprehension debt | People leader with a technology leader |

The forcing field (the AI frontier) is not a shear, but it stresses all of them. Ask about it in each check.

## Which shears to check

1. The shear on each side of the **lever layer**.
2. Any shear between the **surface layer** and the **lever layer** (the path the symptom travels).
3. The shear **downstream** of whatever the change speeds up. This is where the next queue forms.

Usually two or three shears. In quick mode, check only the most relevant one.

## If you arrived here directly

Ask which two groups or steps the problem sits between, what crosses between them, and what goes wrong. Map that to one of the seven shears, or describe it as a new boundary if none fits.

## Questions for each shear

Ask 2–4 per turn. Use what the layer interviews already established.

### Ownership

- ★ Who owns this boundary? Not each side: the boundary itself.
- If no one, who comes closest, and do they have authority on both sides?

### What crosses it

- ★ What moves **inward** (from the faster side to the slower)? Proposals, patterns, requests, generated artifacts.
- ★ What moves **outward** (from the slower side to the faster)? Constraints, standards, approvals, refusals.
- Is the interface explicit (a contract, a checklist, an API, a tier definition) or implicit (whoever remembers)?

### Where it binds

- ★ What queues at this boundary, and how long does it wait?
- Which direction is the pressure stronger right now?
- Does the slower side know what is coming from the faster side, and how soon?

### Sifting

- When something useful appears on the faster side, how does it become standard on the slower side? Who decides, on what evidence, how often?
- When the slower side changes a constraint, how do people on the faster side find out?

## Predict where the bottleneck goes next

For the change being planned, write out the chain:

1. "If we speed up ___ (layer), more ___ arrives at ___ (shear)."
2. "Capacity there is set by ___, which changes on a ___ clock."
3. "So the queue will form at ___, within about ___."
4. "Unless we ___ (add capacity, cap inflow, change the interface) first."

Apply Little's law: at fixed capacity, more work in progress means longer waits. Apply the Theory of Constraints: an hour saved anywhere except the constraint is an illusion.

## Reading the answers

| Finding | Meaning | Move |
|---|---|---|
| No owner | The boundary is implicit, and Conway's law predicts the system will mirror that gap | Make ownership an explicit decision in the plan, and a seat in the room |
| Owner exists but has authority on one side only | They can describe the problem but not fix it | Joint ownership, or escalation path named in the plan |
| Interface is implicit | Every crossing depends on memory and goodwill | Write the interface down: tiers, contracts, checklists, encoded checks |
| Only one direction flows | Either innovation never sifts in, or constraints never reach the fast side | Add the missing direction's mechanism |
| Queue growing | Capacity mismatch | Add capacity at the constraint before speeding up the inflow |
| "It fails open" (things pass without real checking) | Risk is accruing silently | Add a tripwire metric and treat a rise as an incident |

## Moves at the shear

- **Name an owner** with authority on both sides, or a pair.
- **Write the interface down.** Make the implicit contract explicit.
- **Encode recurring judgment.** When the same issue crosses the shear twice, turn it into a check on the slower side (humans on the loop).
- **Rate-limit on purpose.** Batch-size caps, work-in-progress limits, and risk tiers keep the pace difference from tearing the boundary.
- **Build the sifting path.** A defined route, cadence, and evidence bar for fast-side patterns to become slow-side standards.

## Write to the brief

Append under "4. Shears":

```markdown
## 4. Shears
### S# <name>
- Owner: <role> | none (closest: ...)
- Crosses inward: ... · Crosses outward: ...
- Interface: explicit | implicit
- Queue: what waits, how long
- Sifting path: exists | missing
- Frontier stress: ...
- Finding: ...
- Proposed owner / move: ...

### Bottleneck prediction
If we speed up ___, the queue forms at ___ within ___, unless ___.
```

Then return to the `pace-layers` flow (Phase 5).
