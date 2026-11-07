# The model: pace layers of the software organization

This is an adaptation of Stewart Brand's pace layering (*The Clock of the Long Now*, 1999; republished as "Pace Layering: How Complex Systems Learn and Keep Learning," *Journal of Design and Science*, 2018). It also draws on Frank Duffy's shearing layers of buildings, on Gunderson and Holling's panarchy, and on the 2024–2026 evidence about AI in software delivery.

## The stack

Eight layers, fastest first. Each layer has two clocks:

- **Natural clock**: how often the layer's contents normally change.
- **Reform horizon**: how long it takes to change *how the layer works*.

The two can differ by one or two orders of magnitude. A CI pipeline runs in minutes, but changing how an organization verifies software takes quarters. Confusing these two clocks is the most common planning error this model exists to catch.

| # | Layer | What lives here | Natural clock | Reform horizon | Changes by | Typical steward |
|---|---|---|---|---|---|---|
| 1 | **Generation** | Writing code: people and agents, prompts, context files, local tests, the inner loop | Seconds to hours | Weeks | Explore and discard | Engineering leadership |
| 2 | **Integration and Verification** | Review, CI, tests, merge, release, observability, incident response, rollback | Minutes (CI) to days (review) | 2–4 quarters | Re-capacitate | Platform or quality engineering leadership |
| 3 | **Product and Coordination** | Intent, specs, priorities, roadmaps, intake, sequencing across teams | Weeks to a quarter | 2–4 quarters | Decide and prune | Product and business leadership |
| 4 | **Platform and Infrastructure** | CI/CD platform, runtime, cloud, internal developer platform, model gateway, evaluation suites, agent tooling | Weeks to months | 1–2 years | Pave | CTO or head of platform |
| 5 | **Domain Architecture and Systems of Record** | Domain model, bounded contexts, canonical data, core systems and vendor packages, integration contracts, team boundaries | Years | 3–7 years | Seam and slow | Chief architect and domain owners |
| 6 | **Governance** | Security, compliance, risk, change approval, funding cycles, regulation, AI policy | Instruments: annual cycles. Principles: a decade or more | 1–3 years | Codify controls, preserve judgment | CISO, risk, compliance, finance |
| 7 | **Organizational Culture** | Ownership, trust, craft standards, incident norms, what is rewarded | Years | 3–7 years | Embed | CEO and leadership team |
| 8 | **Nature** | Human cognition and attention, how skills form, the labor market, compute physics and cost, domain seasonality | Generational or fixed | Not reformable | Design within | Shared: people, finance, technology leaders |

The horizons are heuristic ranges, not findings. Calibrate them with the user's data: how long the last comparable change actually took to spread across teams.

### Notes on the ordering

- **Funding** sits in Governance (it moves on the budget cycle), even though people discuss it in product meetings.
- **Dependencies between teams** sit in Domain Architecture. They change at the pace of the org chart and the domain model (Conway's law), not at the pace of the backlog.
- **Platform and Domain are separate layers on purpose.** In Duffy's terms, Platform is *services* (replaceable every few years) and Domain is *structure* (replaceable rarely, at great cost). Treating them as one layer hides the most expensive boundary in any modernization.

## The forcing field: the AI capability frontier

The frontier (model releases, agent tooling, vendor ecosystems) is not a layer. It sits outside the stack, changes monthly, and acts on every layer at once with different strength:

- **Strongest on Generation.** Output becomes cheap and abundant.
- **Strong on Verification.** Volume arrives faster than review capacity. AI review and test generation help, but must themselves be verified.
- **Moderate on Platform and Governance.** New object types (agents, vendor models) need gateways, evaluations, and controls.
- **Weak but persistent on Culture and Nature.** It changes what work is valued and how people form skills.

Treat it like weather: you cannot plan a horizon for it. Build joints that absorb it, such as a model gateway plus evaluation suites the organization owns, so models can be swapped at frontier speed while contracts and controls change at governance speed. Model *capability* moves fast; model *choice* (contracts, data residency, validation, vendor oversight) moves slowly.

## How influence moves

Brand's model works in both directions. Uniform same-direction arrows lose half of it.

- **Inward, from fast to slow: accrued innovation and occasional revolt.** A harness pattern one team invents becomes a platform standard. An agent workflow forces a governance rewrite. Most fast-layer experiments should die. The occasional good one sifts down.
- **Outward, from slow to fast: constraint and memory.** The data model limits what code can do. Controls limit what can ship. Norms about ownership decide who reviews. Cognitive limits cap how much anyone can review.

Panarchy names the two cross-scale connections. **Revolt** is a fast collapse cascading into a slower layer. **Remember** is a slower layer supplying the structure and memory that shape how a faster one reorganizes. A layer can also be locked in a **rigidity trap**: highly connected, efficient, brittle, and resistant to any change. A decades-old core system is the classic example.

## The shears

A shear is the boundary between two adjacent layers. Tension builds there because the two sides move at different speeds. Most observable failures are shear failures, and shears usually have no owner.

| Shear | Between | Tension it carries | Signature failure |
|---|---|---|---|
| S1 | Generation and Verification | Volume versus comprehension ("the review wall") | Review queues, oversized changes, merges with no real review, rising change-failure rate |
| S2 | Verification and Product | Shipped versus valuable | Throughput up, outcomes flat; building the wrong thing faster |
| S3 | Product and Platform | Bespoke versus paved road | Shadow tooling, every team running its own agent stack, unclear AI stance |
| S4 | Platform and Domain | Edge speed versus core integrity | Generated customizations in the core system; growing upgrade debt |
| S5 | Domain and Governance | Decision logic under policy or regulation | Untraceable rule changes, audit findings, failed outcome testing |
| S6 | Governance and Culture | Compliance versus ownership | Checkbox controls, blame after incidents, blanket tool bans |
| S7 | Culture and Nature | Ambition versus human limits | Burnout, skill atrophy, comprehension debt, collapsing junior pipeline |

## Two dynamics that compress the stack

**Compile-down.** Slow-layer intent becomes executable at fast-layer speed: policy-as-code, compliance-as-code, continuous control monitoring, harness constraints. Controls now run at the clock of the layer they constrain, which removes approval queues. The risk is that compiled governance takes on fast-layer brittleness. It encodes today's reading of a rule that may change, loses discretion, and creates a false sense that the slow layer is "handled." The intent still changes at governance speed and must be recompiled, so version it and trace it from rule to control to test.

**Harden-up.** Fast-layer output enters slow layers faster than before: generated code lands in integration contracts, data transformations, and core-system customizations within weeks, often with no person holding the theory of why it works. It is legacy on arrival.

Together these mean layers are increasingly separated only by **interfaces**, not by time. Brand's shock absorption, where fast layers take the shock so slow layers can ignore it, weakens. The pace difference has to be engineered on purpose: batch-size caps, model gateways, clean-core boundaries, risk-tiered release, and deliberate slowness at the core.

## Evidence that anchors the model (as of late 2026)

Use these when the user wants grounding. Flag them as directional, not as laws.

- Coding is roughly 11–16% of developer time across several independent studies (Microsoft developer-time research; Meyer et al., IEEE TSE 2019; IDC 2025). By Amdahl's law, even infinitely fast code generation cuts developer effort by at most about 12–19%, and cuts elapsed lead time by less.
- DORA's 2024 and 2025 research associates AI adoption with persistent delivery *instability*, and in 2025 with modestly higher throughput. DORA frames AI as an amplifier of whatever system it lands in. Survey-based and correlational.
- Vendor telemetry (Faros AI, 2025–2026) shows AI-heavy teams merging far more changes while review time and change size rise sharply. Observational, vendor-published.
- GitClear's code-history analysis shows refactoring falling and duplication rising from 2020 to 2024. Correlational.
- METR's randomized studies show perceived speedups diverging from measured ones, with results that shift as tools change. A warning against survey-based productivity metrics.
- Beane and Leonardi (*Journal of Management Studies*, 2025) describe organizations as pace layers under intelligent technologies, and call for new work to connect the layers. That connecting work is shear ownership.
