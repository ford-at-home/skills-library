---
name: prompt-driven-ui-rebuild
description: Build or rebuild a user interface as an ordered sequence of prompts, each starting from verified output rather than accumulated drift. Factors the design system into its own first step, referenced by path thereafter and never restated, and gives every step acceptance criteria and a rejection list that refuses plausible-looking wrong output. Assumes the decision to build has been made — testing whether anyone wants it first is idea-to-landing-page. Works with any prompt-driven builder or a plain coding agent. Use when generating a UI from prompts, rebuilding a front end, restyling an existing app, or recovering a generated codebase that has drifted. Trigger phrases include prompt sequence, rebuild the UI, generate the front end, one-shot the site, restyle the app, the AI keeps changing my styles, design system drift, my generated code is a mess.
---

# Prompt-Driven UI Rebuild

Turn a UI build into an ordered sequence of prompts, each gated on the verified
result of the one before it.

Output is a **prompt ledger** — a document holding the ordered steps, each step's
reference contract, acceptance criteria, rejection list, and verification record.
The ledger is written before any UI prompt is sent and updated after each one.

The differentiator is the rejection list. Acceptance criteria say what good looks
like. A rejection list says what to refuse *even when it looks better than what
you asked for*. Prompt-driven builders fail by being helpful, not by being wrong.

## Use when

- Generating a UI from prompts, in any tool or with a plain coding agent
- Rebuilding or restyling an existing front end
- A generated codebase has drifted and later prompts keep making it worse
- Several people or agents will prompt the same codebase in sequence

## Don't use when

- Nobody has decided the thing is worth building yet. If the goal is one page
  that tests whether anyone wants this, use `idea-to-landing-page` — it commits
  to a pass/fail threshold before the page exists and refuses to build the
  product. Come back here once there's a real interface to build, and it will
  hand you an inventory to sequence.
- The work is backend, infrastructure, auth, payments, or data storage. That is
  server-side work, not this skill. A UI step that adds a backend is a rejected
  step, not a bigger step.
- You are isolating tenants or enforcing per-tenant boundaries — that's
  `multi-tenant-saas-isolation`.
- You need to check whether claims in a README or spec are true. That's
  `evidence-grounded-verification`. This skill catches structure that doesn't
  match its docs only as a side effect.
- You need a scoring rubric for outputs rather than a build sequence. Use
  `anchored-rubric-design`, or `llm-behavior-benchmark` if you are measuring a
  model rather than shipping an interface.
- You are planning how to announce or roll out the result —
  `communication-rollout-planning`.
- It's a single self-contained change to a UI that already has a design system.
  One prompt with a review is cheaper than a ledger.

## Inputs

Ask for these. Don't infer them.

```yaml
target:              # what is being built, in one sentence
design_source:       # what defines the visual system: a token file, a style guide,
                     # a screenshot, an existing app to match — or "none"
existing_codebase:   # path, or "greenfield"
builder:             # what executes the prompts (hosted builder, coding agent, IDE)
observation_method:  # how you will see each step's result: dev server, preview URL,
                     # screenshot, test run, typecheck output
scope_boundary:      # what this sequence will not touch
rejection_seed:      # known-bad patterns already present in this codebase, or "none"
```

**If `observation_method` is missing, stop and ask.** An unobservable step cannot
be verified, and an unverified step contaminates every step after it.

**If `design_source` is `none`,** run step 1 to produce one and stop for sign-off.
Never run component steps against an unapproved design system.

## The four gates

Written before the process, because a gate written after seeing the output is
written to pass.

**Gate 1 — The design system is one artifact, produced first.**
One file holds colors, type scale, spacing, radii, motion, and the names of the
primitives. Nothing else in the sequence defines a visual value.

**Gate 2 — Every later prompt references it by path and does not restate it.**
The prompt says "use the tokens in `<path>`" and lists nothing more. Restating
values in a prompt creates a second source of truth that nothing keeps in sync.

**Gate 3 — Each step depends only on output already verified.**
Order steps so a step's inputs are all recorded as verified in the ledger. If two
steps both need something that doesn't exist yet, that thing is an earlier step.

**Gate 4 — Each step carries acceptance criteria and a rejection list.**
Both written before the prompt is sent. A step missing either does not run.

### Rejection list format

Each entry is a named pattern, a mechanical check, and the action on a hit. Keep
entries checkable — "looks unpolished" is not an entry.

```yaml
- pattern:  <what to refuse>
  check:    <the grep, diff inspection, or file listing that detects it>
  action:   reject; <what to do instead>
```

Eight seed entries are written out with their checks in
`templates/prompt-ledger.md`: raw palette values instead of tokens, a component
duplicating an existing primitive, a second implementation of a concern that
already has one, debug scaffolding on a shipped path, files outside the step's
declared surface, backend or auth added by a UI step, placeholder content, and
docs describing structure that does not exist.

Add anything in `rejection_seed`, plus every pattern the first step produces. The
list only grows. An entry is never removed because a later step wants an exception.

## Process

1. **Write the ledger first.** All steps, in order, with dependencies. No UI
   prompt is sent before the ledger exists.

2. **Step 1 is the design system, alone.** Produce one artifact of tokens and
   primitive names. Its acceptance criterion is that every value the later steps
   need has a name here. Verify by listing the screens ahead and checking each
   needed value resolves to a token.

3. **Get step 1 signed off before anything consumes it.** Every later step
   inherits its mistakes.

4. **Order the remaining steps by dependency, not by importance.** Shell and
   layout, then shared primitives, then screens, then states (loading, empty,
   error), then behavior. Screens before primitives forces every screen to
   improvise, and improvisations don't converge.

5. **Declare each step's surface before prompting.** Which files it may touch.
   This is what makes the out-of-scope rejection checkable.

6. **Write acceptance criteria as observations, not adjectives.** "The form
   shows a field-level error under the email input when it is invalid" is
   checkable. "The form handles errors gracefully" is not. If you cannot state a
   criterion as an observation, the step is not ready to run.

7. **Send the prompt.** It contains: the step's goal, the design-system path, the
   surface it may touch, the acceptance criteria, and the rejection list.

8. **Run the rejection list against the diff before reading the result as a
   whole.** Judging the output first biases you toward accepting it; the checks
   are mechanical for a reason.

9. **Verify against the acceptance criteria using `observation_method`,** and
   record what you observed — not that you were satisfied.

10. **On any rejection, revert to the last verified state and re-prompt with the
    violation named.** Do not patch forward. Patching forward is how a step ends
    up half-verified, and a half-verified step is unverified.

11. **Record the step as verified, rejected, or blocked.** Only verified steps
    can be depended on.

12. **Add each new failure pattern to the rejection list** for all remaining
    steps, and note in the ledger which step it came from.

## Output

The ledger is the output, and `templates/prompt-ledger.md` in this folder is a
blank copy: the header (builder, observation method, design-system path,
out-of-scope boundary), a blocked-first section, the rejection list, one block per
step (dependencies, surface, prompt sent, acceptance criteria, rejection-list
additions, what was observed, what was rejected), a deferred table, and the
declared limits.

Fill in the declared limits before the sequence runs — typically no auth, no
payments, no production data model, no complex backend logic. Anything wanted and
refused goes in **Deferred** with where it belongs. A declared limit is a
boundary; an undeclared one is discovered as a defect.

## Hard rules

These are rules rather than advice because each one, when violated, leaves output
that looks finished and a ledger that reads as if the sequence held.

```text
Never send step N+1 while step N is unverified.
Reject on the rejection list even when the output looks better than what you asked for.
Record what you observed, not that you were satisfied.
```

## Stop instead of guessing

- **No `observation_method`** → stop and ask. You cannot gate what you cannot see.
- **No `design_source`** → run step 1 only, then stop for sign-off.
- **A needed value has no token** → stop and report which value and which step
  needs it. Do not invent a nearby colour or spacing step.
- **A step's acceptance criteria can only be stated as adjectives** → do not run
  it. Split it until each criterion is an observation.
- **Two readings of a requirement are both plausible** → ask one question, stop.
  Do not build both.
- **Asked to skip the design-system step to save time, or to run the remaining
  steps in one prompt** → refuse. One prompt covering four steps has one
  reviewable surface and four sources of drift. Offer to cut scope instead: fewer
  screens, all gated, beats all screens, ungated.
- **A step is rejected twice for the same pattern** → stop prompting. The step is
  underspecified or the design system is missing something. Fix the input.

## Further reading in this folder

- `reference/failure-modes.md` — the seven ways a prompted UI build drifts, read
  out of a shipped generated front end and its fork, and an explicit statement of
  what those two codebases do and do not prove
- `templates/prompt-ledger.md` — a blank ledger, including the eight seed
  rejection entries written out with their checks and actions
