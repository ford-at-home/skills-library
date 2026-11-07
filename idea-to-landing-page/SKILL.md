---
name: idea-to-landing-page
description: Take a raw product idea to a live page that tests whether anyone wants it, without building the product. Writes the hypothesis and the pass/fail threshold before the page exists, holds the page to what actually exists so it cannot promise a working product it does not have, and refuses auth, payments, dashboards, and backend logic. Use when you have an idea and want a demand signal, need a waitlist or pre-launch page, are tempted to start building to find out if people care, or someone says just spin up a quick landing page. Trigger phrases include validate my idea, landing page, waitlist, coming soon page, test demand, pre-launch, will anyone use this, should I build this.
---

# Idea to Landing Page

Turn an idea into one live page that produces a real demand signal, and refuse to
build the product while doing it.

Output is a **demand test record** — a document holding the hypothesis, the
pass/fail threshold, the claim inventory, the refusal list, and the result. The
record is written before the page is built. The page is an instrument; the record
is the finding.

Two failures make this necessary and they pull in opposite directions. People
validate by building, which is expensive and answers a question nobody asked.
Then, having built a page instead, they make it promise a product that does not
exist — which measures the promise, not the product, and leaves someone holding
an email address collected against it.

## Use when

- You have an idea and no evidence anyone wants it
- You are about to start building in order to find out if people care
- You need a waitlist, pre-launch, or coming-soon page
- Someone is asking for a "quick landing page" for something unbuilt
- A stalled project needs to know whether to continue

## Don't use when

- The product exists and you are building or restyling its interface. That's
  `prompt-driven-ui-rebuild`. This skill decides whether a page should exist and
  what it may claim; that one sequences the prompts that build it.
- You have decided to build and need the work broken into phased, ordered
  delivery. That is planning work — use your task-breakdown process.
- You need real hosting, a real backend, or a deploy pipeline. That is
  provisioning and deployment work, and out of scope here.
- You are adding accounts or separating customers' data —
  `multi-tenant-saas-isolation`. If you need that, you are past a demand test.
- You want a judgment on whether the idea is *good*. A page measures behavior,
  not merit. For structured critique use `multi-persona-roundtable`; for scoring
  submissions against criteria, `defensible-submission-scoring`.
- You need to check whether claims in an existing document are true. That's
  `evidence-grounded-verification`. Use it on your own page copy if the claims
  are load-bearing.
- Demand is already established. Then you are marketing, not testing, and the
  constraints here will only slow you down.

## Inputs

Ask for these. Don't infer them.

```yaml
idea:              # one sentence, in the form "when <situation>, <who> wants to
                   # <action> so they can <outcome>"
audience:          # who specifically. "freelance bookkeepers with 5-20 clients",
                   # not "small businesses"
exists_today:      # what is actually built and working right now. "nothing" is a
                   # valid and common answer
threshold:         # the number of qualified signups, over what window, that makes
                   # you continue — and the number that makes you stop
capture_target:    # where submissions land, and who can read them
follow_up:         # what you will actually send the person, and when
time_box:          # how long you are spending on this before you stop
```

**If `threshold` is missing, stop and ask.** A result without a pre-committed
threshold gets read as whatever the reader already believed. Nine signups is
encouraging or fatal depending on what you said in advance, and only what you
said in advance is evidence.

**If `exists_today` is missing, stop and ask.** Every honesty constraint is
enforced against it. Without it you cannot tell an overclaim from a description.

## The gate

The refusal table and the honesty constraints are in
`reference/refusals-and-honesty.md`. Read it before writing any page copy. Both
are written before the process, because a scope boundary written afterward is
written to permit whatever already happened, and a claim check written afterward
is written to pass the copy you already like.

## Process

1. **Write the hypothesis and the threshold, before anything else.** State the
   idea as "when *situation*, *who* wants to *action* so they can *outcome*".
   Then decompose it into the separate assumptions it is actually made of — the
   audience feels this pain, current tools fail them, they would pay, they are
   reachable through this channel. Name which single assumption the page tests.
   Record the continue and stop numbers from `threshold`. Do not proceed without
   them.

2. **Look for the problem in the audience's own words.** Before any design, find
   where these people already discuss this work. Collect the frustrations they
   state, the workarounds they have assembled, and phrases like "I wish there
   was". Then look separately for money: hours they name as wasted, complaints
   about a competitor's price, budgets mentioned in passing, people paying
   freelancers to do this by hand. Rate the willingness-to-pay evidence **weak**,
   **moderate**, or **strong**, and say why. Quote sources; do not paraphrase into
   agreement. Weak evidence is a finding — it means the page tests a colder start,
   not that you should describe it warmly.

3. **Inventory the claims and check each one.** List every claim the page will
   make — headline, subhead, feature descriptions, trust signals, pricing, calls
   to action. Mark each supported, needs-rewording, or unsupported against
   `exists_today`, applying the honesty constraints in
   `reference/refusals-and-honesty.md`. Unsupported claims are cut or rewritten to
   intention. This inventory goes in the record; it is the artifact someone can
   audit later.

4. **Map only the path the test needs.** Land, understand, submit, confirm. Write
   it out and stop there. Any route you find yourself adding that is not on that
   path — login, dashboard, settings, account — is refused by the table in
   `reference/refusals-and-honesty.md`.

5. **Build one page.** Sections that carry the test: a clear statement of who it
   is for and what problem it addresses, enough detail to make the promise
   concrete, the capture form, and a footer. Trust and pricing sections are
   optional and only appear with true content. The form takes an email plus at
   most one qualifier, validates client-side, shows inline errors, and on success
   shows a specific confirmation that tells the person what happens next. If you
   are generating this from prompts, hand the section list and the claim
   inventory to `prompt-driven-ui-rebuild` and let it sequence the build.

6. **Wire capture to a durable destination and prove it end to end.** A form that
   shows a success message but stores nothing is the failure mode that survives
   longest, because the page looks correct from the outside. Submit a real
   entry against the live URL — not a preview — and confirm it arrives at
   `capture_target` with the fields intact and a usable timestamp. Then submit a
   malformed one and confirm the person sees a real error rather than a false
   success. Record both results.

7. **Make it findable and shareable without overclaiming.** A page title naming
   the product and what it does, a description under about 160 characters, and
   social preview tags so a shared link renders correctly. Metadata is page copy:
   it goes through the same claim check. A title promising what the page itself
   carefully avoids promising is the same violation in a place nobody rereads.

8. **Take the page live, then record the baseline and the review date.** Note
   what the page says today and when you will read the result. The page is now
   an instrument and changing it mid-test invalidates the comparison. If you must
   change it, say so in the record and restart the window.

9. **Read the result against the threshold you wrote in step 1.** Continue, stop,
   or run a different test. If the number came in below the stop line, say so
   plainly; the record exists to make that sentence possible to write.

## Hard rules

These are rules rather than advice because each one, when violated, leaves a page
and a record that read as a completed test.

```text
The threshold is written before the page. A threshold set after seeing the
  result is not a threshold.
The page may claim only what exists_today supports.
Never state invented social proof, user counts, testimonials, or ratings.
No auth, no payments, no dashboard, no backend logic, no production database.
Collect the minimum fields the follow-up needs. Never payment details,
  government identifiers, health information, or credentials.
Whatever the page promises about the email address is a commitment.
Never quote a conversion or performance benchmark you did not measure.
Test capture against the live URL, not a preview, before announcing it.
Do not change the page mid-test without recording that you did.
```

The first rule is the one that gets argued with, and it bends both directions.
Every unpromising result can be reread as early signal; a decent one gets
dismissed by whoever wanted a different answer. Both happen when the threshold
arrives afterward.

## Output

The record is the finding: hypothesis, evidence, claim inventory, what was
refused, the page and its capture target, the capture verification, and the result
against the threshold. The template is in `reference/record-shape.md`.

## Stop instead of guessing

- **No threshold given** → stop and ask. Do not offer a default; a supplied
  number becomes the finding.
- **No `exists_today` given** → stop and ask. Nothing downstream can be checked
  without it.
- **Asked to make the page describe the product as working when it isn't** →
  refuse. Offer the intention wording instead. This is not a tone preference and
  a hedge in the footer does not resolve it.
- **Asked to add auth, payments, a dashboard, or a real backend** → refuse and
  name what it costs and what signal it adds, which is none. If the requester
  genuinely needs those, the work is a build and belongs elsewhere.
- **Asked for placeholder counts or testimonials "just for the layout"** →
  refuse. Placeholder proof ships. Leave the section empty or remove it.
- **The audience is too broad to find in step 2** → stop. Return the search you
  ran and what it produced. Don't design against a guess; a page aimed at
  everyone tests nothing.
- **Capture cannot be verified end to end** → do not announce the page. An
  unverified form loses submissions silently and you will read the absence as
  disinterest.
- **Asked what a good conversion rate is** → say you don't know for this page and
  that the threshold has to come from what the result would change. Do not supply
  an industry figure.

## Further reading in this folder

- `reference/refusals-and-honesty.md` — the six things a demand test refuses to
  build and why, and the seven constraints governing what the page may claim
- `reference/record-shape.md` — the demand test record template
- `reference/failure-modes.md` — six ways a demand test ends with no usable
  signal, including the silent capture failure that reads as zero demand
