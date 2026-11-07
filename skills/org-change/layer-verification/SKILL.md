---
name: layer-verification
description: Interviews and diagnoses the Integration and Verification layer (code review, CI, tests, merge, release, observability, incident response, rollback), which is often the binding constraint once AI speeds up code generation. Use when reviews are slow or rubber-stamped, release or change-failure rates are rising, PRs are getting bigger, AI output is outpacing review, or a pace-layers session identifies Verification as the goal or lever layer. Includes a read-only script that measures review flow from GitHub pull-request history.
---

# Layer 2: Integration and Verification

**Natural clock:** minutes (a CI run) to days (a review). **Reform horizon:** 2–4 quarters. **Changes by:** re-capacitating. **Typical steward:** platform or quality engineering leadership.

This layer decides what crosses from "written" to "running." It includes code review, continuous integration, tests, merge rules, environments, release and deployment, observability, incident response, and rollback.

Its pipeline clock is fast, but its **capacity** changes slowly, because capacity is bounded by human review attention and by test infrastructure, both of which take quarters to change. That gap is why this layer has become the binding constraint in many organizations using AI. Generation volume has risen sharply; review capacity has not. The 2024–2026 evidence (DORA, vendor telemetry) consistently shows the queue forming here, and shows AI adoption associated with lower delivery stability.

The healthy shape is "humans on the loop": people improve the harness that checks the work (tests, structural rules, evaluations, risk tiers) rather than inspecting every artifact by hand.

## If you arrived here directly

If no brief or goal exists yet, ask three questions first:

1. What is happening that made you want to change something here?
2. In one sentence, what do you want to be true that isn't now?
3. What is your role, and what can you decide on your own?

## Interview

Four passes, 2–4 questions per turn. Skip what you already know. ★ marks the short set for quick mode.

### Pass 1: What exists

- ★ What has to happen between "code written" and "code in production"? Walk me through the steps.
- ★ What are the review rules: required approvers, code owners, who can merge?
- How long does CI take, and how often does it fail for reasons unrelated to the change (flaky tests)?
- What environments exist, and are any shared and contended?
- How do releases happen: continuous deploy, release trains, a change board? How is a bad release undone?

### Pass 2: Topology

- ★ Who reviews whose code? Are a few people doing most of the reviewing?
- Who owns the pipeline, the test infrastructure, and the release process? Are those the same people?
- Which teams' releases depend on other teams' releases?
- Where does approval come from outside engineering (security, change board, compliance)?

### Pass 3: Under the hood

- ★ Where do changes *wait*? Separate time spent working from time spent waiting.
- ★ What does a reviewer actually check, compared with what the policy says they check?
- How often do changes merge with no meaningful review? Is that known?
- What fraction of changes cause an incident or need a fix afterward (change-failure rate), and is it rising?
- When a test is flaky, what happens? (Tolerated flakiness is a culture signal, not just a tooling one.)
- What evidence does a release require, and who accepts it?

### Pass 4: Forces

- **From Generation (faster):** How much has incoming change volume and size grown? What is the trend?
- **From slower layers:** Which approvals or controls come from Governance? Which limits come from Platform? Which come from people's attention (Nature)?
- **From the frontier:** Is AI used in review or test generation? Who checks the AI's checking?
- **What this layer pushes inward:** What has verification learned that the platform, the architecture, or policy should absorb?

## Look before you ask

If you have read access to the repository and the GitHub CLI is authenticated, measure review flow directly:

```bash
gh pr list --state merged --limit 500 \
  --json number,createdAt,mergedAt,additions,deletions,changedFiles,author,reviews \
  > prs.json
python3 scripts/pr_flow.py prs.json
```

The script is in this skill's `scripts/` folder (in a plugin install: `${CLAUDE_PLUGIN_ROOT}/skills/layer-verification/scripts/pr_flow.py`). It is read-only, uses only the Python standard library, and reports:

- time to first review and time to merge (median, 75th and 90th percentile)
- change size distribution and the share of very large changes
- share of changes merged with no review from anyone other than the author
- reviewer concentration (how much of the reviewing the top reviewers do)
- a weekly trend of volume, size, and time to merge

Also check, read-only: CI configuration files, `CODEOWNERS`, branch protection settings if visible, and test run durations.

Show the user the numbers and ask whether they match their experience. A mismatch between perceived and measured flow is itself a finding.

## Reading the answers

| If you hear or measure | It usually means | Ask or check next |
|---|---|---|
| Review time rising with volume | A capacity limit (Little's law); more generation will lengthen the queue | Add capacity or cap inflow before scaling generation |
| Many merges with no real review | The shear has failed open; risk is accruing silently | Ask what the change-failure rate is doing |
| A few reviewers do most reviews | Concentrated attention (Nature) and possibly status dynamics (Culture) | Who are they? What happens when they are out? |
| Change size growing | Batch size problem; each review gets harder and less effective | Cap size; split work earlier (Product) |
| "We wait on the change board" | A Governance gate running at governance speed inside a fast pipeline | Shear S6, compile-down candidate (H8) |
| Flaky tests tolerated | Normalized deviance; a culture signal | Run `layer-culture` short set |
| "AI reviews it" with no evaluation of the AI reviewer | Verification of verification is missing | Who measures false negatives? |
| Fast pipeline, slow outcomes | The problem is what gets built, not how it ships | Shear S2, run `layer-product` |

## Moves that work here

- **Risk-tiered review.** Not every change needs the same scrutiny. Define tiers by blast radius and route accordingly.
- **Move humans on the loop.** When a reviewer finds the same class of problem twice, encode it as a test, a lint rule, a structural check, or an evaluation, and fix the harness instead of the artifact.
- **Small batches and trunk-based flow.** Smaller changes are reviewed faster and more accurately.
- **Progressive delivery.** Feature flags, canaries, and fast rollback make each release smaller in consequence.
- **Plan review capacity like any capacity.** Make it visible, budget it, and protect it.
- **A tripwire.** Track the share of changes merged without review, and treat a rise as an incident signal.

## Moves that fail here

- Adding reviewers without changing batch size or tiers. It spreads the same overload wider.
- Removing review to clear the queue. It moves the queue to production incidents.
- Buying an AI reviewer and treating its approval as review, with no measurement of what it misses.

## Failure modes

- **Pushed too fast:** rubber-stamping, unreviewed merges, rising instability.
- **Held too slow:** the review wall, long queues, developers batching work to avoid the queue (which makes it worse), and bypasses.

## Leading indicators

- Median and 90th-percentile time in review.
- Change size distribution.
- Share merged without independent review.
- Change-failure rate and rework rate.
- Deployment frequency and lead time for changes.
- Flow efficiency (working time divided by elapsed time).

## Who belongs in the room

- **Steward:** whoever owns delivery capability (platform, developer experience, or quality engineering).
- **The busiest reviewer:** they know where the queue really is.
- **An on-call engineer:** they see what verification missed.
- **Shear S1 owner:** the harness or platform lead who can encode reviewer judgment into checks.
- **Shear S2 owner:** a product operations or value-stream person who can connect "shipped" to "valuable."
- **A governance representative** if any approval gate comes from outside engineering.

## Write to the brief

Append under "3. Layer briefs":

```markdown
### Integration and Verification
- Exists: path to production; review rules; CI duration and flakiness; environments; release and rollback
- Topology: reviewer graph and concentration; owners of pipeline, tests, release; cross-team release coupling; external gates
- Under the hood: wait vs. work; what reviewers actually check; unreviewed merges; change-failure trend; release evidence
- Measured (if run): time to first review ..., time to merge ..., size ..., unreviewed ...%, top-reviewer share ...%
- Forces: inbound volume trend; governance gates; AI in review and who checks it
- Diagnosis: (2–4 lines, with evidence)
- Unknowns → who would know
- Candidate room seats: ...
```
