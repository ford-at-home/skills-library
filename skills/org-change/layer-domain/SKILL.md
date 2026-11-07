---
name: layer-domain
description: Interviews and diagnoses the Domain Architecture and Systems of Record layer (domain model, bounded contexts, canonical data, core systems and vendor packages, integration contracts, and team boundaries). Use when modernizing or migrating a core or legacy system, when every change needs several teams, when AI-generated code is entering core systems, when only a few people understand a critical system, or when a pace-layers session identifies Domain Architecture as the goal or lever layer. Includes a read-only script that finds knowledge concentration in a git repository.
---

# Layer 5: Domain Architecture and Systems of Record

**Natural clock:** years. **Reform horizon:** 3–7 years. **Changes by:** creating seams and deliberately slowing the core. **Typical steward:** chief architect and domain owners.

This is the "structure" layer in Frank Duffy's building model: the load-bearing walls. It holds the domain model, the boundaries between contexts, canonical data, the systems of record (core platforms, large vendor packages, decades-old home-grown systems), the contracts between systems, and the team boundaries that mirror them (Conway's law).

Gartner's pace-layered application strategy calls these systems of record and gives them the slowest change rate. In panarchy terms, an old core system is often in a **rigidity trap**: highly connected, efficient, brittle, and resistant to change.

AI changes this layer in two opposite ways. It makes *translation* cheap (reading legacy code, drafting migrations, generating characterization tests), which can unlock long-stuck modernization. And it makes customization cheap to *write* but no cheaper to *own*, so generated code can harden into the core within weeks with no person holding the theory of why it works. The critical path shifts to verifying behavioral equivalence and keeping the core clean.

## If you arrived here directly

If no brief or goal exists yet, ask three questions first:

1. What is happening that made you want to change something here?
2. In one sentence, what do you want to be true that isn't now?
3. What is your role, and what can you decide on your own?

## Interview

Four passes, 2–4 questions per turn. ★ marks the short set.

### Pass 1: What exists

- ★ What are the systems of record here, and what does each one own (which data, which decisions)?
- ★ How much has the core been customized compared with its vendor or original baseline?
- What are the main domains or bounded contexts? Are they written down anywhere?
- How do systems integrate: shared databases, APIs, events, files, batch jobs?

### Pass 2: Topology

- ★ Draw the dependency picture in words: which systems and teams are upstream of most others?
- Do team boundaries match domain boundaries? Where do they cut across each other?
- Where are the anti-corruption layers or seams between old and new, if any?
- Who has authority to change the core data model or a shared contract?

### Pass 3: Under the hood

- ★ Who actually understands the core? How many people, and what happens if they leave?
- How long does a change to the core take from idea to production? How long does a vendor upgrade take?
- How much business logic lives inside the core system (rules, configurations, scripts) rather than at its edges?
- Is AI-generated code being added to the core or its integrations? Who reviews it, and against what?
- What would prove that a migrated capability behaves the same as the original? Does that evidence exist today?

### Pass 4: Forces

- **From faster layers:** What are product and platform teams asking the core to do faster than it can?
- **From slower layers:** What governance, regulation, or audit requirements attach to the core's data and decisions?
- **From the frontier:** Is AI being used for legacy analysis, translation, or test generation? How is its output verified?

## Look before you ask

If you can read the repository, find where knowledge is concentrated:

```bash
python3 scripts/theory_holders.py --repo . --months 18 --depth 2
```

The script is in this skill's `scripts/` folder (in a plugin install: `${CLAUDE_PLUGIN_ROOT}/skills/layer-domain/scripts/theory_holders.py`). It runs `git log` read-only and reports, per directory: commit count, distinct authors, the top author's share, how many authors account for more than half the commits, and how recently anyone touched it. It flags areas where one person dominates and areas nobody has touched recently.

Author names come from git history. Use them to find the subject-matter experts for the room. In the brief, record roles rather than names unless the user chooses otherwise.

Also check, read-only: integration code (clients, adapters, event schemas), customization folders in vendor packages, and any architecture decision records.

## Reading the answers

| If you hear | It usually means | Ask or check next |
|---|---|---|
| "Every change needs three teams" | Team and domain boundaries don't match (Conway) | Which boundary would remove the most coordination? |
| "Only two people understand it" | Key-person risk and a verification limit | Who are they; can the room protect their time? |
| "We customized it heavily over the years" | Upgrade debt; the core is absorbing edge logic | Customization delta; what could move to the edge? |
| "Let's rewrite it" | A big-bang temptation; high failure risk at this layer's clock | Strangler fig with characterization tests instead |
| "Agents are writing changes to the core" | Harden-up: generated code becoming legacy on arrival | Who holds the theory; what equivalence evidence exists? |
| "We can't prove the new one does the same thing" | Verification is the critical path, not translation | Characterization tests, parallel runs, outcome comparison |
| "Audit cares about this data" | Shear S5 is live; decision logic is regulated | Run `shear-check` S5 and `layer-governance` |

## Moves that work here

- **Seam and slow.** Create seams (anti-corruption layers, APIs, events) between the core and the edge. Then slow the core on purpose: keep it close to its baseline, and push differentiation to the edge.
- **Strangler fig.** Replace capability by capability behind a stable interface, never all at once.
- **Behavioral equivalence as a release gate.** Characterization tests, parallel runs, and comparison of outcome distributions before any migrated logic goes live.
- **Decision traceability.** For rules that carry policy or regulatory weight, trace each rule to its source and its tests.
- **Protect the theory holders.** Pair them with others and with agents doing archaeology, and record what they know.
- **Align teams to domains.** Move team boundaries toward domain boundaries when coordination cost dominates.

## Moves that fail here

- Big-bang rewrites on an aggressive timeline.
- Letting cheap generated customizations pile into the core.
- Modernizing the code without moving the knowledge.

## Failure modes

- **Pushed too fast:** rewrite failure, data corruption, regulatory exposure, broken downstream consumers.
- **Held too slow:** rigidity trap; every other layer waits on the core; generated workarounds accumulate at the edges.

## Leading indicators

- Customization delta versus the vendor baseline.
- Share of changes that require touching the core.
- Upgrade lead time.
- Coupling between domains (changes that span contexts).
- Number of people who can explain each critical area (from the script, plus interviews).
- Equivalence-test coverage for migrated capabilities.

## Who belongs in the room

- **Steward:** chief or enterprise architect, and the domain owner from the business.
- **Theory holders:** the people who know why the core works, found by asking and by the script.
- **Shear S4 owner:** the person accountable for the boundary between platform and core (often the anti-corruption layer owner).
- **Shear S5 owners:** the business owner of the decision logic plus governance or risk, jointly.
- **A consumer of the core:** a team that depends on it and feels its pace.

## Write to the brief

Append under "3. Layer briefs":

```markdown
### Domain Architecture and Systems of Record
- Exists: systems of record and what each owns; customization delta; domains; integration styles
- Topology: dependency picture; team vs. domain boundary mismatches; seams; who can change shared contracts
- Under the hood: theory holders (count, risk); core change and upgrade lead time; logic inside the core; generated code entering; equivalence evidence
- Knowledge concentration (if script run): ...
- Forces: demands from faster layers; governance and audit attachments; AI in legacy work
- Diagnosis: (2–4 lines, with evidence)
- Unknowns → who would know
- Candidate room seats: ...
```
