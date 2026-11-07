---
name: layer-product
description: Interviews and diagnoses the Product and Coordination layer (intent, specs, priorities, roadmaps, intake, and sequencing work across teams). Use when teams ship a lot but outcomes don't move, priorities churn, specs are the bottleneck, spec-driven or agentic development is shifting work upstream, or cross-team coordination dominates, or when a pace-layers session identifies Product and Coordination as the goal or lever layer.
---

# Layer 3: Product and Coordination

**Natural clock:** weeks (a sprint) to a quarter. **Reform horizon:** 2–4 quarters. **Changes by:** deciding and pruning. **Typical steward:** product and business leadership.

This layer decides what to build and in what order: intent, specifications, priorities, roadmaps, how work enters, and how teams sequence it. When building gets cheap, this layer becomes more important, not less. The scarce act is no longer producing software; it is choosing what *not* to build. DORA's 2025 research found that without a strong focus on users, AI adoption was associated with *worse* team performance.

Spec-driven and agentic development move work upward into this layer. The specification becomes the slow, reviewed artifact, and the bottleneck can relocate here.

Two things people discuss in product meetings belong to slower layers. **Funding** moves on the budget cycle (Governance). **Dependencies between teams** move at the pace of the org chart and domain model (Domain Architecture). If the user's problem is really one of those, say so.

## If you arrived here directly

If no brief or goal exists yet, ask three questions first:

1. What is happening that made you want to change something here?
2. In one sentence, what do you want to be true that isn't now?
3. What is your role, and what can you decide on your own?

## Interview

Four passes, 2–4 questions per turn. ★ marks the short set.

### Pass 1: What exists

- ★ How does work enter the system? Who can put something on a team's plate?
- ★ How are priorities set, at what cadence, and by whom?
- What does a specification look like here: a ticket, a document, a prototype, a prompt? Who writes it now?
- What outcome measures exist for shipped work, if any?

### Pass 2: Topology

- ★ For a typical feature, how many teams must change something? Who sequences them?
- Who can say no to a priority, and who can override that no?
- Where do business stakeholders, product managers, and engineers actually negotiate scope?
- Which teams are upstream of most others?

### Pass 3: Under the hood

- ★ What fraction of work is tied to a user or business outcome someone will check later?
- How often do priorities change mid-cycle, and what triggers the change?
- How much work in progress does each team carry?
- How much of what shipped last quarter is actually used? Is anything ever removed?
- How often is a specification revised after building starts? (High rates mean intent is being discovered during building, which can be fine, but should be deliberate.)

### Pass 4: Forces

- **From faster layers:** Is engineering now producing faster than product can decide? Are prototypes replacing specs?
- **From slower layers:** How do funding cycles, architecture, and governance constrain what can be prioritized?
- **From the frontier:** Are agents drafting specs, stories, or prototypes? Who reviews them?

## Look before you ask

If you can read the issue tracker or planning documents the user points to, check:

- Ratio of work items linked to an outcome or objective.
- Age of open items and size of the backlog.
- Items reprioritized or carried over between cycles.

## Reading the answers

| If you hear | It usually means | Ask or check next |
|---|---|---|
| "We ship a lot, but nothing moves" | The shipped/valuable shear (S2) is unowned | Who checks outcomes after release? |
| "Everything is priority one" | No pruning mechanism; decisions are deferred to engineering | Who is allowed to kill work? |
| "We can't start until three teams agree" | A Domain Architecture problem showing up as coordination | Run `layer-domain`; check Conway alignment |
| "Priorities change every few weeks" | Mismatch with the funding or governance clock, or no stable strategy | Ask what drives the changes |
| "Specs are the bottleneck now" | Building got cheap; deciding did not | Make specs reviewed artifacts with a clear owner and a fast loop |
| "We build what the loudest stakeholder asks for" | Decision rights are unclear | Who formally owns the priority call? |

## Moves that work here

- **Decide and prune.** Maintain an explicit kill list. Make stopping work as visible as starting it.
- **Outcome hypotheses.** Each significant item states what should change and how it will be checked.
- **Smaller bets.** When building is cheap, run more small experiments and keep fewer large commitments.
- **Specs as reviewed artifacts.** If agents build from specs, give specs owners, reviews, and versioning.
- **Name the outcome owner after release.** Connect "shipped" to "used" with a person, not a dashboard.

## Moves that fail here

- More planning ceremonies without decision rights.
- Using faster engineering to absorb indecision: building every option instead of choosing.
- Treating a dependency problem as a scheduling problem.

## Failure modes

- **Pushed too fast:** thrash, priority churn, teams that never finish.
- **Held too slow:** building the wrong thing faster; roadmap theater that nobody follows.

## Leading indicators

- Share of work tied to a checked outcome.
- Mid-cycle priority changes.
- Work in progress per team.
- Feature usage after release, and features removed.
- Specification revision rate after build starts.

## Who belongs in the room

- **Steward:** the product or business leader who owns priorities for the area.
- **A decision-maker from the business** who will judge whether the outcome happened.
- **Shear S2 owner:** product operations or a value-stream manager connecting delivery to outcomes.
- **Shear S3 owner:** a platform product manager, if the change touches tooling or paved roads.
- **An engineer who has felt the churn.**

## Write to the brief

Append under "3. Layer briefs":

```markdown
### Product and Coordination
- Exists: intake; priority-setting cadence and owner; spec form and author; outcome measures
- Topology: teams per feature; who sequences; who can say no; negotiation venue
- Under the hood: outcome-linked share; mid-cycle changes; WIP; usage of shipped work; spec revision
- Forces: engineering throughput vs. decision speed; funding and architecture constraints; AI in specs
- Diagnosis: (2–4 lines, with evidence)
- Misfiled problems (belongs to Governance or Domain?): ...
- Unknowns → who would know
- Candidate room seats: ...
```
