---
name: layer-platform
description: Interviews and diagnoses the Platform and Infrastructure layer (CI/CD platform, runtime, cloud, internal developer platform, golden paths, model gateway, evaluation suites, and shared agent tooling). Use when teams route around the platform, every team runs its own AI or agent stack, swapping models is hard, platform changes break teams, or a pace-layers session identifies Platform as the goal or lever layer.
---

# Layer 4: Platform and Infrastructure

**Natural clock:** weeks to months. **Reform horizon:** 1–2 years. **Changes by:** paving. **Typical steward:** CTO or head of platform.

This is the "services" layer in Frank Duffy's building model: the plumbing and wiring that every team uses and that can be replaced every few years without rebuilding the structure. It includes CI/CD, runtime and cloud, the internal developer platform and its golden paths, observability, identity and secrets, and now the model gateway, evaluation suites, and shared agent tooling.

In an AI-era stack this layer has a special job: it is the **shock absorber for the frontier**. Models and tools change monthly. The core systems and governance below cannot. A good platform lets teams swap a model at frontier speed while the contracts and controls underneath change at their own speed.

## If you arrived here directly

If no brief or goal exists yet, ask three questions first:

1. What is happening that made you want to change something here?
2. In one sentence, what do you want to be true that isn't now?
3. What is your role, and what can you decide on your own?

## Interview

Four passes, 2–4 questions per turn. ★ marks the short set.

### Pass 1: What exists

- ★ What does a team get "for free" from the platform today, and what must it build itself?
- ★ How do teams access AI models and agent tooling: a shared gateway, direct vendor accounts, personal accounts?
- What golden paths or templates exist, and how current are they?
- Is there an evaluation suite the organization owns for AI behavior on its own tasks?

### Pass 2: Topology

- ★ Is the platform run as a product (roadmap, users, feedback) or as a ticket queue?
- How do teams interact with the platform team: self-service, collaboration, or requests?
- Who decides what goes on the paved road, and how do new patterns get there?
- Which teams use the platform least, and why?

### Pass 3: Under the hood

- ★ Where do teams route around the platform, and what does that tell you about what it lacks?
- How long does it take to provision what a new service or experiment needs?
- If the organization had to switch its primary model provider next quarter, what would break and how long would it take?
- How are platform changes rolled out to teams? Do they break things?
- What does a typical change cost in compute and inference, and does anyone know?

### Pass 4: Forces

- **From faster layers:** What are product and engineering teams asking for that the platform can't provide?
- **From slower layers:** What constraints come from the core systems, security, data residency, or vendor contracts?
- **From the frontier:** How tightly is the platform coupled to a single vendor or model's specific features?

## Look before you ask

If you can read the relevant repositories, check:

- Shared pipeline templates and how many repositories use them versus custom pipelines.
- Infrastructure-as-code modules and their reuse.
- Where model or AI API calls are made: through a shared client or gateway, or scattered direct calls with separate credentials.

## Reading the answers

| If you hear | It usually means | Ask or check next |
|---|---|---|
| "Teams build their own pipelines and agent setups" | The paved road is missing or worse than going alone (shear S3) | What would make the paved road the easiest path? |
| "Switching models would take months" | Frontier coupling is too tight; no shock absorber | Gateway plus evaluation suite as a joint (H12) |
| "Platform changes keep breaking us" | The platform is moving at a faster clock than its consumers can absorb | Versioned interfaces; deprecation windows |
| "We file a ticket and wait" | The platform is a queue, not a product | Self-service; platform product management |
| "Nobody knows what AI costs us" | A Nature-layer constraint (compute economics) is invisible | Add cost per change as an indicator |
| "The platform can't touch the core system" | Shear S4 is unowned | Run `shear-check` S4 and `layer-domain` |

## Moves that work here

- **Pave.** Make the right way the easiest way: templates, defaults, and self-service that beat the alternatives.
- **Run the platform as a product.** A roadmap, a user research habit, and a named product owner.
- **Build joints for the frontier.** A model gateway plus evaluation suites the organization owns, so models can be replaced on evidence rather than vendor claims.
- **Version the interfaces.** Teams should be able to upgrade on their schedule within a window.
- **Harvest from the fast layer.** Turn successful team-level patterns (agent harnesses, context files, checks) into paved-road defaults.

## Moves that fail here

- Mandating the platform while it is still worse than the alternative.
- Building for the current model's quirks.
- Platform rewrites that freeze every team for a year.

## Failure modes

- **Pushed too fast:** churn that breaks paved roads; teams lose trust and fork.
- **Held too slow:** teams route around it; fragmentation; every team pays for its own plumbing.

## Leading indicators

- Golden-path adoption across repositories.
- Lead time to provision a new service or experiment.
- Time to swap a model behind the gateway.
- Evaluation coverage of AI behavior on internal tasks.
- Inference and compute cost per change.
- Platform satisfaction from its users.

## Who belongs in the room

- **Steward:** the head of platform or CTO.
- **Platform product manager**, or whoever acts as one.
- **A team that routes around the platform** and can say why.
- **Shear S3 owner:** the person who connects product needs to the paved road.
- **Shear S4 owner:** a domain or enterprise architect if the change touches core systems.
- **Finance partner** if compute cost is material.

## Write to the brief

Append under "3. Layer briefs":

```markdown
### Platform and Infrastructure
- Exists: what teams get free; AI access path; golden paths; owned evaluation suite
- Topology: product vs. queue; interaction mode; who decides the paved road; low-adoption teams
- Under the hood: route-arounds; provisioning time; model-swap time; rollout breakage; cost per change
- Forces: unmet demand from teams; core/security/residency/contract constraints; vendor coupling
- Diagnosis: (2–4 lines, with evidence)
- Unknowns → who would know
- Candidate room seats: ...
```
