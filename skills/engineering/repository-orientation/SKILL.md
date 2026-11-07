---
name: repository-orientation
description: Build an accurate working model of a codebase you have not seen before, treating its documentation as claims to verify against code rather than as ground truth. Labels every fact Verified, Partial, Missing, or External, so the model you edit from distinguishes what you confirmed from what you assumed. Prevents reading a README, believing it, and then editing the wrong layer or rebuilding something that already exists. Use before any task touching more than one file or an unfamiliar area, before creating a new file, helper, or component, and when asked where something lives. Trigger phrases include where does X live, how does this repo work, orient me, unfamiliar codebase, before I start, does this already exist, what layer should this go in, onboard to this repo.
---

# Repository Orientation

Produce a written, labelled model of a repository before editing it. The model
is the deliverable — no code changes during orientation.

The governing assumption: **documentation is a claim about the code, not a
description of it.** Documents drift, describe intentions that were never built,
and survive the removal of what they describe. Read them to form hypotheses, then
check the hypotheses against code, configuration, and deployment artifacts.

## Use when

- Starting any task that touches more than one file, or any unfamiliar area.
- The task says add, fix, or change something and you don't yet know where it
  lives.
- You are about to create a new file, helper, hook, component, or table.
- You need to know how to validate a change before you make it.
- Someone asks where something lives, or whether something already exists.

## Don't use when

- You already oriented for this task in this session.
- The change is one line in a file you have already read end to end.
- **You are clearing claims in a document for an outside reader.** That is
  `evidence-grounded-verification`. The technique overlaps — both verify claims
  against sources — but the consumer and the stopping point differ. That skill
  produces a fact base for someone who can independently check the document, and
  it does not modify the document. This skill produces a working model for your
  own next edit, stops as soon as the model is good enough to act on, and does
  not attempt completeness. If the deliverable is a corrected document, use that
  skill. If the deliverable is a safe change, use this one.
- **You are writing documentation from raw thinking** rather than reading it.
  That is `architecture-note-routing`.
- **You are recording a choice you have made.** That is decision-record work —
  write the record with whatever ADR practice the repository already uses.
- **You are provisioning or scaffolding new infrastructure.** Orientation is
  read-only; that is provisioning work. For designing tenant separation see
  `multi-tenant-saas-isolation`.

## Inputs

```yaml
repository:    # path
task:          # what you are about to change, in one sentence
entry_docs:    # README, AGENTS.md/CLAUDE.md, docs/ — whatever exists
depth:         # "task-scoped" (default) or "full map"
```

Default to task-scoped. A full map is worth building once per repository, and
worth writing to a file when you do.

## The labelling scheme

Every statement in your model carries one of four labels. Nothing goes unlabelled
— an unlabelled fact is an assumption wearing a disguise.

| Label | Meaning |
|---|---|
| **Verified** | Read directly from code, configuration, or a deployment artifact in this repository. |
| **Partial** | Exists but is incomplete, unused, or only wired on one path. Say which part. |
| **Missing** | Documented or assumed, but verifiably absent from this repository. Do not invent it. |
| **External** | Lives outside the repository — a hosting dashboard, a managed database console, a deployed function, a cron schedule, a provider platform. Cannot be inspected or changed from here. |

`Missing` and `External` carry the most weight. `Missing` prevents you calling a
function that does not exist. `External` prevents you claiming work was completed
that in fact requires someone to click something.

## Process

1. **Inventory the documentation and extract its claims as a list.** README,
   agent-instruction file, architecture docs, runbooks. Do not yet believe any of
   it. Write down the specific, checkable assertions: counts, file paths, table
   names, framework and version, what is tested, what is deployed. Note each
   document's date and whether anything says when it was last verified.

2. **Verify the load-bearing claims against the code.** Load-bearing means your
   change is wrong if the claim is false. `reference/checking-claims.md` gives
   the cheap check for each shape of claim.

   Label each claim. When a document and the code disagree, **the code wins and
   the disagreement is a finding you report.**

3. **Map the layers and place the task.** Name every layer the repository
   actually has and which directory holds it — routes, shared UI, client data
   access, server functions, server-only helpers, background jobs, schema and
   migrations, infrastructure definitions, generated output. Then state which
   layer or layers your task belongs to, and why. Most bad changes are
   wrong-layer changes, and they happen before a line is written.

4. **Find the existing pattern and copy its shape.** Locate a sibling that
   already does the same class of work and name it. Follow it rather than
   inventing a second convention. A repository with two conventions for the same
   job is worse off than one with a convention you dislike.

5. **Check whether what you are about to add already exists.** Grep for the
   concept, not the name you would have given it. If it exists, extend it. Never
   create a parallel second implementation.

6. **Establish the hands-off list.** Generated files (routers, type definitions,
   API clients, lockfiles — anything a build step rewrites), vendored contracts,
   and files owned by an external tool. Hand-editing generated output is silently
   reverted on the next build, which makes it an expensive way to lose an hour.

7. **Separate External from doable.** Anything the repository cannot reach
   becomes a *manual actions* list, never a completion claim.

8. **Name the validation commands** the change will require, from the manifest's
   scripts and any check scripts in the repository — lint, typecheck, tests,
   build, plus any repository-specific checks (migration ordering, secret
   scanning, contract sync). Confirm each command exists before naming it.

9. **Report the model before editing,** in the shape given in
   `reference/output-shape.md`. If the repository has a skill router or specialist
   guidance for the layers you identified, name the ones that apply and read them
   before touching code.

## Hard rules

Each of these prevents a model that reads as complete while being wrong. That is
why they are rules rather than advice — a fabricated fact and a verified one look
identical on the page.

```text
No documentation claim is Verified until read against code.
Never invent a Missing thing to make the model coherent.
Never claim External work was done. List it as a manual action.
Never hand-edit generated files.
```

## Stop instead of guessing

- **A load-bearing claim cannot be verified** → label it Unverified, say what
  would settle it, and do not build on it. If the change depends on it, stop and
  ask.
- **Documentation and code disagree materially** → stop and report before
  editing. You have found either a stale document or a removed feature, and
  which one it is changes the task.
- **You cannot find where a layer lives** → say so. Do not assume the
  conventional location from a framework the repository does not use.
- **The task requires touching something External** → stop and list what someone
  must do outside the repository. Never simulate it, stub it, or report it done.
- **No tests, no lint, no typecheck exist** → say so plainly. Do not invent a
  validation story, and do not claim a change is safe on the strength of reading
  it.
- **The repository is large enough that a task-scoped model is not achievable in
  the budget** → narrow the task, and say which areas you did not examine. A
  partial model with honest edges beats a complete-looking one with guesses.

## Further reading in this folder

- `reference/checking-claims.md` — the cheap check for each shape of
  documentation claim, in rough order of value returned
- `reference/output-shape.md` — the orientation report template, and why the
  Unverified section may not be empty by default
- `reference/failure-modes.md` — nine ways an orientation produces a confident
  wrong model, and which rule above catches each
