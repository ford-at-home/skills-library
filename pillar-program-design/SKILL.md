---
name: pillar-program-design
description: Turn a public strategic plan into a small set of thematic pillars, each carrying scoped problem statements a team can build against in a weekend. Forces every statement to name a specific user cohort, describe a current-state problem rather than a solution, anchor to a named dataset with an owner and an access path, and carry a named person inside the sponsoring institution who will answer questions. Use when planning a civic hackathon, an internal innovation program, a grant challenge, an ideas competition, or any call for proposals organized around themes. Trigger phrases include define the tracks, hackathon pillars, problem statements, challenge statements, what should teams build, civic program design, scope the themes, turn priorities into projects.
---

# Pillar Program Design

Convert an institution's stated priorities into a small number of pillars, and
each pillar into problem statements that are scoped tightly enough to build
against and grounded well enough to survive contact with the institution.

Output is a **statement set** — a pillar list plus one file per problem
statement plus a dataset inventory. The pillars are the coarse structure that
participants choose between. The statements are what they actually build against.

## Use when

- Standing up a themed call for work: hackathon, innovation sprint, grant round
- Re-running an annual program and deciding whether last cycle's themes still hold
- A sponsor has handed over a strategic plan and asked "what should people build?"
- Statements exist but participants keep building the wrong thing

## Don't use when

- You are evaluating submissions. That is scoring, and it runs after this. Use
  `defensible-submission-scoring`.
- You are running an open call with no themes. Pillars are the mechanism here;
  without them this skill has nothing to organize.
- No institution has committed anything. This produces artifacts that name
  people and datasets. With no sponsor, it produces fiction.
- You are generating solution ideas. This scopes problems. Naming solutions
  before the statement is frozen is the failure mode it exists to prevent.

## Inputs

Ask for these. Don't infer them.

```yaml
strategic_plan:        # path or URL to the public, institution-owned plan being
                       # anchored to. Its named priorities become candidate pillars
sponsor:               # named executive inside the institution, with title, and
                       # the record of their commitment (meeting note, email, statement)
committee_capacity:    # integer — how many pillar committees can actually be staffed
allies:                # per candidate pillar, a named person inside the institution
                       # who will answer data and process questions. Or "unknown"
prior_cycle:           # path to last cycle's pillars and statements, or "none"
freeze_date:           # the date statements stop changing
```

**If `strategic_plan` is missing, stop.** Everything downstream drifts without an
anchor, and an anchor you invented is not an anchor.

**If `sponsor` is missing,** draft the pillar list but write every statement at
status `blocked`, with the blocker recorded as the missing sponsor. Do not
publish. A statement implies someone will answer questions about it.

**If `committee_capacity` is missing, stop and ask.** It is the only real
constraint on pillar count, and the count is the load-bearing decision.

**If more than one candidate strategic plan exists,** list them all and ask which
is canonical. Do not pick.

## Gates

A statement does not ship until all six hold. These are checked per statement,
not per pillar, and a failure blocks that statement alone.

1. **Named user cohort.** "Residents" fails. "First-time entrepreneurs
   registering an LLC" passes. The test: could you find five of these people?
2. **Current-state problem, not a solution.** "Build a dashboard" fails.
   "Residents cannot tell which department handles their request" passes.
3. **At least one named dataset**, with owner, access path, and refresh cadence
   — all three. "The data probably exists" is a blocker, not an anchor.
4. **A named institutional ally.** A department, not a person, fails. Committees
   without a name spend the event guessing.
5. **Prior art checked.** If the problem is substantially solved somewhere
   comparable, the statement must say so and point at adapt-or-integrate rather
   than build. A statement that ignores a working implementation elsewhere wastes
   everyone's weekend.
6. **Explicit out-of-scope list.** At least one entry. Without it, teams build
   the replacement for the system you cannot replace.

## Process

1. **Read the anchor and extract its named priorities.** For each, record the
   priority name, its owner inside the institution, and the plan section. Do not
   yet decide whether it becomes a pillar.

2. **Set the pillar count from committee capacity, not from the plan's
   symmetry.** Cap it at `committee_capacity`. Below that, the working range is
   5–8: fewer and participants cluster, more and choosing becomes paralysis. A
   plan with fourteen priorities does not get fourteen pillars. The formula and
   an illustration of the grain to aim for are in `reference/pillar-grain.md`.

3. **Map priorities to pillars.** A pillar may take one priority, merge two
   related ones, or split a broad one. Record every merge and split with its
   reason — that record is what stops next cycle from relitigating it.

4. **Name each pillar in plain language.** Resident-facing, not internal. Reject
   acronyms and program names. "Maternal Health Data Coordination" beats "MCH
   Data Ops".

5. **Draft two statements per pillar: one practical, one open-ended.** Practical
   means the institution could pilot a solution within a year. Open-ended means
   the problem matters and the path is genuinely unsettled. Resist a third —
   extra statements split attention and thin out every submission.

6. **Run the six gates on each statement.** Statements that fail gate 3 go to
   `blocked` with a row in the dataset inventory at `status: unknown`. They do
   not get published on the strength of "we'll sort the data out later."

7. **Build the dataset inventory** as a single table across all statements. One
   row per dataset. This is where you discover two pillars are quietly depending
   on the same locked system.

8. **Collect what you could not answer** into one questions list, each tagged to
   the office that can answer it, and send it to the sponsor before freeze.

9. **Freeze on `freeze_date`.** After freeze, changes require a recorded
   decision naming who approved it. Statements that drift during the event
   invalidate the scoring that follows.

The statement file and the three roll-up files are in
`reference/statement-shape.md`.

## Hard rules

Each of these prevents a statement that reads as well-grounded and is not. That
is why they are rules rather than advice — the defect does not surface in review,
it surfaces at the event.

```text
The anchor is a public document owned by the institution. Not your summary of it.
A statement with no named dataset is blocked, not published.
Never invent a sponsor, an ally, or a dataset owner.
Prior-cycle statements start at needs-review. Never at approved.
Open-ended statements get latitude on data. They get none on the named user.
Approved sponsor language is preserved verbatim and quoted, never paraphrased.
After the freeze date, changes require a recorded decision naming the approver.
```

## Stop instead of guessing

- **No public strategic plan** → stop. The program is not anchored yet. Offer to
  anchor to a narrower public document (a council resolution, a published
  departmental plan) and say what that costs in authority.
- **Multiple candidate plans** → list all of them with owner and date, and ask.
- **Sponsor willing verbally, nothing on record** → write the statement, status
  `needs-review`, open question: obtain the commitment in writing before publish.
- **A pillar cannot produce two statements** → the pillar is too narrow or the
  committee is under-staffed. Merge it or staff it. Do not publish one statement
  and call the pillar done.
- **A statement's data does not exist** → `blocked`. Do not soften it to
  open-ended to escape gate 3. Open-ended means the path is unsettled, not that
  the data is imaginary.
- **Asked to reuse last cycle's statements unchanged** → refuse `approved`. Last
  cycle's problems may be solved, abandoned, or owned by a department that
  reorganized. Re-confirm each one against the current anchor.
- **Asked to write the statements without the committees** → refuse. A statement
  authored with no ally is a guess wearing a template.

## Further reading in this folder

- `reference/statement-shape.md` — the per-statement file template and the three
  roll-up files: pillar list, dataset inventory, open questions
- `reference/pillar-grain.md` — the count formula, and a real seven-pillar set
  shown for width rather than for wording
- `reference/failure-modes.md` — six ways a statement set fails after it looks
  finished, and which rule above catches each
