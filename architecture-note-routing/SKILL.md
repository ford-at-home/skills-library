---
name: architecture-note-routing
description: Take raw architectural thinking — a transcript fragment, voice note, research memo, or half-formed idea in chat — and land it in exactly one durable place without inventing detail, duplicating what already exists, or quietly reconciling a contradiction. Classifies the fragment first, then routes it — a term to the glossary, a boundary to an architecture document, a framing to a product document, a closed-off option to a decision record, an unanswered question to the open-questions list. Exists because the default outcome is a new file that overlaps three existing ones. Use when someone drops in raw thinking that needs a home. Trigger phrases include write this up, capture this, where should this live, turn this into a doc, document this idea, synthesise these notes, from this transcript.
---

# Architecture Note Routing

Raw material in, one canonical document out. The job is classification and
placement, not writing at length.

Two things make this hard and both are addressed below: deciding *where* a
fragment belongs, and resisting the urge to fill the gaps the fragment leaves.

## Use when

- A transcript excerpt, voice note, or chat paragraph describes how part of a
  system should work and is load-bearing enough to lose.
- A third-party research memo or analyst note needs capturing.
- Material already sitting in a raw capture file is now developed enough to
  refine upward.
- An existing document needs extending with new thinking rather than replacing.

## Don't use when

- **The fragment is a decision** — it closes off options or is costly to
  reverse. That belongs in a numbered decision record, written with whatever ADR
  practice the repository already uses. Burying a decision inside an architecture
  document is the most common way this skill is misused.
- **You don't know how the system actually works yet.** Writing architecture
  documentation from an unverified model manufactures authoritative-looking
  fiction. Build the model first with `repository-orientation`.
- **The fragment is only a new term.** Add the glossary entry; there is nothing
  to synthesise.
- **The fragment is process guidance for agents or contributors.** That belongs
  wherever the repository keeps its contributor and agent instructions, not in
  the docs tree.
- **You are maintaining the schema of a structured memory or knowledge file.**
  That is `markdown-memory-schema-maintenance`.
- **The material is going to an outside reader and its claims need clearing.**
  That is `evidence-grounded-verification`.

## Inputs

```yaml
fragment:          # the raw material, or a path to it
docs_root:         # directory holding refined documentation
glossary:          # path to the canonical term list, or "none exists"
open_questions:    # where unanswered questions are logged
raw_capture:       # file(s) holding unrefined source material, if any
new_file_policy:   # "confirm first" or "author freely"
```

If `glossary` is "none exists" and the fragment introduces terms, say so before
writing — routing without a canonical term list will produce drift, and the
first synthesis pass is the cheapest time to start one.

## Routing table

Classify before writing. Each fragment lands in exactly one destination; link
from elsewhere rather than duplicating. Destination paths follow whatever layout
`docs_root` already uses; the ones below are the shape, not a mandated tree.

| Fragment shape | Destination |
|---|---|
| A noun or term being defined | The glossary |
| How a layer, boundary, or interaction is shaped | `architecture/<topic>.md` |
| How the product is framed — who it serves, why, positioning | `product/<topic>.md` |
| A choice that closes off options | A numbered decision record — hand off, do not absorb it here |
| A question not yet answered | The open-questions list |
| Third-party analyst or research capture | `research/<name>.md`, with provenance frontmatter |
| Rules for how contributors or agents work | The contributor/agent instructions, not the docs tree |
| Raw, unrefined source material | Leave it in the raw capture file |

If a fragment spans destinations, **split it before writing.** One concept per
file. The most common split: product framing that depends on a technical
affordance becomes two documents that link to each other.

Research captures are **not** adopted into refined documentation until a
decision record consumes them. A memo's recommendation is evidence, not policy.

## Process

1. **Name the fragment's primary shape in one sentence** before opening any
   file. If you cannot, the fragment is too raw — ask for a narrower framing
   rather than guessing at a destination.

2. **Search the docs tree for existing coverage.** Grep for the concept, not
   just the words the fragment used. Three outcomes:
   - Nothing covers it → new file may be justified (step 4).
   - Something partly covers it → **extend in place.**
   - Something **contradicts** it → stop. Do not silently reconcile. Raise it as
     an open question or a decision-record candidate and say which document
     disagrees. Silent reconciliation destroys the record of what was believed
     and when.

3. **Resolve the vocabulary delta first.** Every pass either touches the
   glossary or proves it doesn't need to:
   - New term introduced → add the glossary entry in the same pass.
   - Existing term used differently → fix the glossary *first*, then propagate.
     This is the terminology-drift guard and it only works in this order.
   - A paragraph that implicitly defines a noun without naming it → name it.

   The glossary is the single source of truth. Other documents link to it and
   never redefine.

4. **Choose the target file, preferring an existing one.** Create a new file only
   when the topic teaches one clear thing on its own *and* no existing document
   is its natural home. When torn, extend. Splitting a document later is cheaper
   than consolidating scattered stubs, and far cheaper than the stub that never
   grows. If `new_file_policy` is "confirm first", surface the plan before
   writing.

5. **Draft: link, don't duplicate.** Link the glossary on a term's first use.
   Reference the decision record that pinned a contract rather than restating
   the contract. Open with a short title and a one-sentence purpose line. Use a
   diagram only when it teaches something the prose cannot — a decorative
   diagram is worse than none because it must be maintained.

6. **Write no detail the fragment does not contain.** If the fragment doesn't
   say which runtime a component uses, neither does your document. Route the gap
   to the open-questions list. Invented detail is the failure mode with the
   longest half-life here: it reads as authoritative, gets cited, and nobody
   remembers it was a guess.

7. **Close with what the document deliberately omits.** Name the adjacent topics
   you did not cover, one line each on why, and where they belong or which open
   question tracks them. This is not boilerplate — it is what stops the next
   reader mistaking a scoped document for an incomplete one, and stops the next
   author padding it.

8. **Fix adjacent entropy you noticed, and report it.** Stale terminology a
   rename should have swept; a concept defined in two places (collapse to one
   plus a link); an open question this fragment just answered (promote to a
   decision record or delete if a document already answers it).

The document shape and the report you hand back are in
`reference/output-shape.md`.

## Hard rules

Each of these prevents a document that reads as authoritative and gets cited.
That is why they are rules rather than advice — the defect is not visible in the
document that carries it.

```text
Never invent detail to make a document feel finished. Log the gap.
Never create empty scaffolding for a topic that "should exist".
Never redefine a glossary term inside another document. Link.
A contradiction stops the pass. Never reconcile silently.
Never edit raw capture files to fold refined content back in.
A decision does not go in an architecture document. Hand it off.
A research memo's recommendation is not adopted until a decision consumes it.
```

## Stop instead of guessing

- **You cannot name the fragment's shape in one sentence** → ask for a narrower
  framing. Do not pick the closest-looking directory.
- **The fragment contradicts an existing document** → stop and report both
  versions. Ask which is current. Reconciling silently loses the disagreement.
- **The fragment reads like a decision** → stop and confirm. If it is decided,
  hand off. If not, it goes to open questions.
- **The fragment is too thin to teach anything on its own** → leave it in raw
  capture and say why. A stub file is a liability; it looks like coverage.
- **You would have to assert a technical fact to make the document coherent, and
  you cannot verify it** → log the gap as an open question and write around it.
- **Asked to "just write it up properly" from material you cannot verify against
  the system** → say what is unverified before writing, or orient first.

## Further reading in this folder

- `reference/output-shape.md` — the document template, the report handed back to
  the requester, and which fields have no empty state
- `reference/failure-modes.md` — seven ways a routing pass makes the docs tree
  worse while producing something that reads well
