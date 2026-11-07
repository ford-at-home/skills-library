---
name: layer-governance
description: Interviews and diagnoses the Governance layer (security, compliance, risk and model risk, change approval, funding cycles, regulation, and AI policy). Use when approvals or audits are the bottleneck, an AI policy is missing or unclear, teams work around controls, policy-as-code or continuous compliance is being considered, regulation is changing, or when a pace-layers session identifies Governance as the goal or lever layer.
---

# Layer 6: Governance

**Natural clock:** instruments move on annual cycles (audits, budgets, exams); principles move over a decade or more. **Reform horizon:** 1–3 years. **Changes by:** codifying controls while preserving judgment. **Typical steward:** CISO, risk, compliance, and finance leadership.

Governance is how the organization constrains itself: security and compliance policy, risk management (including model risk), change approval, architecture review, data governance, the funding cycle, AI policy, and the external rules from regulators and standards bodies.

Governance runs at **two speeds**. Principles (accountability, fairness, explainability, protecting customer data) change slowly. Instruments (specific regulations, control catalogs, guidance documents) can churn quickly. From 2024 to 2026 several high-profile AI rules were delayed, repealed and replaced, or rescinded within two years. Design controls against the stable principles, and treat the volatile specifics as parameters.

Two dynamics matter most here:

- **Compile-down.** Policy-as-code, compliance-as-code, and continuous control monitoring let governance run at pipeline speed and remove approval queues. They also freeze today's interpretation and lose discretion.
- **"Slow has the power."** This layer can veto anything faster than it. A change plan that does not bring Governance in early tends to be disposed of late.

## If you arrived here directly

If no brief or goal exists yet, ask three questions first:

1. What is happening that made you want to change something here?
2. In one sentence, what do you want to be true that isn't now?
3. What is your role, and what can you decide on your own?

## Interview

Four passes, 2–4 questions per turn. ★ marks the short set.

### Pass 1: What exists

- ★ Which policies, controls, and external rules apply to this change? Include industry regulation, security standards, and internal policy.
- ★ Is there an AI policy or stance people can find and understand? Does it cover AI used *in the product* and AI used *to build software*?
- What approval gates does a change pass through, and which are mandatory versus customary?
- How is this work funded: annual project budgets, persistent team funding, or something else?

### Pass 2: Topology

- ★ Who can approve, and who can veto? Who interprets an ambiguous rule?
- Where does evidence for controls come from today: manual attestations, tickets, automated pipeline records?
- Which governance functions talk to each other (security, risk, compliance, legal, finance, architecture), and which do not?
- Who in governance already understands how software is delivered here?

### Pass 3: Under the hood

- ★ How do exceptions work? (The exception process is often the real policy.)
- How long does it take from a policy decision to an enforced control?
- Which gates actually reduce risk, and which are ritual? How would you know?
- What were the last audit or examination findings related to this area?
- Where do teams work around controls, and why?

### Pass 4: Forces

- **From faster layers:** What new things (agents, vendor models, generated code, new data uses) is governance being asked to approve? How quickly?
- **From slower layers:** What cultural norms shape how governance is perceived (partner or police)?
- **From outside:** Which external rules are changing, and on what timeline? What is stable underneath them?

## Look before you ask

If the user points to policy documents, control catalogs, or pipeline configuration, read them and check:

- Which controls are automated with evidence in the pipeline versus attested by hand.
- Whether policy text distinguishes principles from parameters.
- Whether any AI-specific controls exist (model inventory, evaluation, vendor oversight, decision traceability).

Do not provide legal conclusions. Where regulatory interpretation matters, record it as a question for counsel or compliance and make that person a seat in the room.

## Reading the answers

| If you hear | It usually means | Ask or check next |
|---|---|---|
| "Nobody knows if we're allowed to use it" | No clear AI stance; teams either freeze or hide | Who can publish a stance in weeks, not quarters? |
| "We wait weeks for approval" | A slow-layer gate inside a fast pipeline | Compile-down candidate, risk-tiered approval (H8) |
| "Teams work around the controls" | Controls cost more than the risk they reduce, or are misunderstood | Exception volume; which controls are ritual? |
| "We'd have to rewrite everything if the regulation changes" | Controls are coupled to a volatile instrument | Separate principles from parameters; version parameters |
| "Audit found we couldn't explain a decision" | Shear S5: decision logic lacks traceability | Run `shear-check` S5 |
| "Funding is annual and fixed" | The funding clock constrains product and platform | Is persistent team funding possible for this area? |
| "Security said no to AI tools" | A ban at a slow clock against a fast layer; expect shadow use | What would a governed path look like? |

## Moves that work here

- **Codify controls, preserve judgment.** Automate the evidence and the routine checks. Keep a defined human path for the judgment calls.
- **Separate principles from parameters.** Write controls against durable principles. Put volatile specifics (thresholds, lists, jurisdictions) in versioned configuration with an owner.
- **Risk-tier the gates.** Low-risk changes flow; high-risk changes get scrutiny. Publish the tiers.
- **Publish a clear AI stance quickly**, then refine it. A clear interim stance beats a perfect one next year.
- **One program for AI in the product and AI in the build.** The decision logic an agent writes inherits the full exposure of the product it runs in.
- **Fix the exception process.** Make exceptions visible, time-limited, and reviewed.

## Moves that fail here

- Blanket bans on fast-layer tools.
- Encoding today's regulation into pipelines without versioning or ownership.
- Adding gates in response to every incident without removing any.

## Failure modes

- **Pushed too fast:** brittle compiled rules diverging from a rewritten law; whiplash; loss of trust from regulators or auditors.
- **Held too slow:** approval queues, shadow processes, and controls that exist on paper only.

## Leading indicators

- Time from policy decision to enforced control.
- Share of controls automated with evidence.
- Approval wait time by risk tier.
- Exception volume and age.
- Audit or examination findings in the area.

## Who belongs in the room

- **Steward:** the leader who can approve or veto the change (often the CISO, chief risk officer, or compliance head). Bring them early: they hold the power.
- **A governance practitioner who knows delivery:** someone who can translate between control language and pipeline language.
- **Legal or compliance counsel** when external rules are involved.
- **Finance partner** if the funding model is part of the lever.
- **Shear S5 and S6 owners:** the joint owners of regulated decision logic, and of the boundary between compliance and ownership culture.

## Write to the brief

Append under "3. Layer briefs":

```markdown
### Governance
- Exists: applicable rules and policies; AI stance (product and build); approval gates; funding model
- Topology: approvers and veto holders; evidence sources; functions that do/don't coordinate; delivery-literate allies
- Under the hood: exception process; policy-to-control lead time; ritual vs. risk-reducing gates; recent findings; work-arounds
- Principles vs. instruments: what is stable, what is volatile
- Forces: new objects to govern; cultural perception; external rule changes
- Diagnosis: (2–4 lines, with evidence)
- Questions for counsel or compliance: ...
- Unknowns → who would know
- Candidate room seats: ...
```
