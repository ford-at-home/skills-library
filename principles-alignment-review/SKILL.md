---
name: principles-alignment-review
description: Review a drafted proposal against a principle set the caller supplies — company values, engineering tenets, a funder's criteria, a team charter — and report where it aligns, where it is silent, and where it invokes one principle to excuse skipping another. The principle set is a required input with no default, and the review cannot come back with everything strong. Its distinctive output is the contradictions, found between principles and invisible to a principle-by-principle read. One reader applying one declared set, not several viewpoints arguing. Use when a proposal is about to be submitted, or when a document reads too clean. Trigger phrases include principles review, values review, review against our principles, stress test this proposal, red team this doc, adversarial review, does this hold up, pre-mortem this memo.
---

# Principles Alignment Review

Read a proposal against a stated set of principles and report where it aligns,
where it is silent, and where it invokes one principle to avoid another.

Output is a **review** — findings and recommended revisions. You never edit the
proposal. The author does that, using the review.

This makes a proposal more *honest*, which is frequently the opposite of making
it more persuasive. Callers who wanted the second will be unhappy with the first.

## The three things this enforces

An agent asked to "review this against our values" will score each value
favorably, cite nothing, and return a compliment. These are the corrections.

**1. It cannot pass everything.** If every principle scores strong, the review is
incomplete and gets re-run — not published. A reviewer that never fails anything
is a signature on a document, not a review.

**2. Contradictions are found between principles, never within one.** They are
the findings that change decisions, and a principle-by-principle pass cannot see
them because each principle individually looks satisfied. The recurring shapes:

- Urgency invoked to excuse skipping rigor
- Customer benefit invoked to excuse ignoring cost
- Ambition invoked to excuse the absence of quality gates
- Decisiveness invoked to excuse not seeking disconfirming evidence
- Delivery invoked to excuse not being honest about risk

**3. Silent and weak are different findings.** Collapsing them loses the review's
main result. Silence on a principle that does not bear on this proposal is fine;
silence on a load-bearing one is the finding.

## Use when

- A proposal, memo, or strategy document is drafted and about to be submitted
- A document reads suspiciously clean and you want to know what it is not saying
- A decision needs an adversarial reader before it reaches a decision-maker
- Stated principles exist and nobody has checked a proposal against them in a way
  that could fail

## Don't use when

- The proposal doesn't exist yet. This reviews drafts; it doesn't write them
- The artifact is a post-incident review. Blameless incident analysis has
  different rules and this reviewer's stance will damage it
- The goal is to make the proposal more convincing. Say so and decline
- You want several distinct viewpoints arguing with each other about whether the
  thing survives contact with reality. Use `multi-persona-roundtable`. This skill
  is one reader applying one declared principle set
- The decision is already made and an action is about to execute. That gates a
  scheduled action at execution time rather than reviewing a proposal at
  authoring time
- You are scoring many submissions against each other for a funding or selection
  decision. Use `defensible-submission-scoring`
- You need to design the scoring instrument itself. Use `anchored-rubric-design`
- You are checking whether the document's factual claims are true rather than
  whether its reasoning honors stated principles. Use
  `evidence-grounded-verification`

## Inputs

Ask for these. Don't infer them.

```yaml
proposal:          # the drafted artifact — path or text
proposal_type:     # proposal | strategy memo | design doc | funding request |
                   # business case | other (name it)
principles:        # REQUIRED. The set to review against, as the organization
                   # states them
principles_source: # where the set comes from and who ratified it
known_context:     # what the reviewer should know that isn't in the document
known_dissent:     # objections already raised, so the review doesn't re-derive
                   # them and call them new
```

**If `principles` is missing, stop and ask.** This skill has no default set and
must not supply one. A review against principles the reviewer invented is a
review against the reviewer's preferences wearing the organization's vocabulary,
and the author will correctly ignore it.

**If `principles_source` is unknown**, run the review but record at the top that
the set is unratified. A proposal cannot be held to principles the organization
has not agreed to.

## The four scores

| Score | Meaning |
|---|---|
| **strong** | The document contains cited evidence for it |
| **weak** | Mentioned without evidence, or the evidence in the document runs counter to it |
| **silent** | The document does not address it at all |
| **contradictory** | The document invokes this principle to justify skipping another |

## Gates

| Gate | Passes when | If it fails |
|---|---|---|
| Rubric built first | Every principle has meaning, strong evidence, and weak evidence written before scoring | Build it. Do not score against bare names |
| Every principle scored | Each is strong, weak, silent, or contradictory | Score the unscored |
| At least one weakness | Not every principle scores strong | Re-read. A document that satisfies every principle has not been read adversarially |
| Load-bearing set named | The review names which principles actually decide this proposal | Name them |
| Contradictions surfaced | Cases where one principle excuses another are listed, or their absence is asserted deliberately | Hunt again |
| Every score cited | Each score quotes or points to a passage | Cite it. An uncited score is an impression |
| Missing evidence listed | Claims the reader cannot verify from the document, each with what would resolve it | List them |
| Optimism risks named | At least one risk the document understates or omits | Name it |
| Revisions bounded | Five or fewer, each specific and assignable | Trim or expand |

## Process

The order is the point. Each step below is corrupted by doing it after the next.

1. **Read the whole proposal before scoring anything.** Scoring as you read
   anchors every later principle to the first impression.
2. **Build the rubric** — the three lines each principle needs are in
   `reference/rubric-preparation.md` — then **name the load-bearing subset**:
   typically four to six of any set actually decide the case. Both before any score
   is assigned.
3. **Score every principle**, citing passages.
4. **Hunt contradictions across principle pairs**, using the shapes above. This
   cannot be folded into step 3; a per-principle pass cannot see them.
5. **Then** the missing-evidence list, the risks optimism hides — a risk register
   where everything is low severity is itself the finding — and five or fewer
   revisions, each specific enough that a named person could do it.

## Hard rules

Each of these prevents a failure that produces a plausible-looking review. That is
why they are rules rather than advice — nothing downstream signals that one was
violated.

```text
The principle set is an input. Never review against principles you supplied.
Never score every principle strong. If nothing is weak, read it again.
Silent and weak are different findings. Do not merge them.
An unratified principle set is disclosed at the top of the review.
Treat the principle set as one lens, not as the definition of quality.
```

The last rule matters more than it looks. Any principle set is a partial and
political artifact. A proposal can honor every principle and still be wrong, and
a review that cannot say so has confused a checklist for judgement.

## Stop instead of guessing

- **No principle set supplied** → stop and ask. Do not offer a substitute set;
  a set the reviewer brought is not the organization's.
- **The document contains no decision** → say so. Scoring a status update against
  principles produces findings about nothing.
- **The document is too short to carry the set** — roughly, fewer than a page per
  four principles → offer to review against the load-bearing subset instead. Do
  not manufacture findings to fill a table.
- **Asked to confirm the proposal is good, or to review it favorably before a
  deadline** → refuse the framing. Offer a review of the load-bearing principles
  only; that limits scope honestly instead of limiting rigor.
- **Asked to review against principles the caller is inventing during the
  review** → stop. Principles ratified retroactively to fit a proposal will
  always find it compliant.
- **A principle is stated so vaguely it cannot be converted into strong and weak
  evidence** → say so, review the rest, and report the unreviewable principle as
  a finding about the principle set rather than the proposal.

## How this goes wrong

**The one it exists to catch.** Every principle scores strong, the review reads
as a compliment, and the proposal ships with the hole it always had.

**Dissent laundering.** The document lists objections and the reviewer counts the
list as evidence of rigor. Check whether each objection is answered or merely
displayed. An objections section with no responses is decoration.

## Further reading in this folder

- `reference/rubric-preparation.md` — converting a bare principle name into three
  reviewable lines, and why the weak-evidence line does the most work
- `reference/review-shape.md` — the review template
