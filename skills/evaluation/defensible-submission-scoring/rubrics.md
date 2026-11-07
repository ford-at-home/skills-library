# Scoring bands

Two rubrics. They answer different questions and are never summed together.

- **Desirability** — is this a good idea? Six categories, 1–5, weighted per award.
- **Survivability** — can this actually ship? Five dimensions, 1–5, summed to a tier.

Localize the platform names in the survivability bands to your own environment.
The named examples are illustrative of the *grain* of evidence each band needs,
not a list to match against.

---

## Desirability — the 1-5 scale

| Score | Meaning |
|---|---|
| 1 | Weak |
| 2 | Emerging |
| 3 | Solid |
| 4 | Strong |
| 5 | Exceptional |

Score every category before applying any weight.

### 1. Impact on the targeted problem

Does this address a real public problem in a meaningful way?

- **High:** clearly solves a meaningful problem; supports a named priority or
  measurable outcome; the link between solution and public value is obvious.
- **Low:** loosely connected to a real need; the problem is vague or generic;
  interesting build, not especially useful.

### 2. Feasibility and implementability

Could this realistically be piloted, adopted, or integrated?

- **High:** pilotable in the near term; uses data and systems that plausibly
  exist; the team understands implementation constraints.
- **Low:** depends on data that does not exist or integrations that are not
  possible; requires policy change or procurement with no plan.

### 3. User value

Does this create meaningful value for actual people?

- **High:** specific user group identified; value proposition obvious; measurably
  reduces friction, confusion, delay, or exclusion.
- **Low:** user is abstract; value is theoretical; built for the judges.

### 4. Execution and prototype quality

How well did the team turn the idea into something tangible? Not how pretty the
demo is — whether the prototype supports the claims made about it.

- **High:** demo works; flow from problem to interaction to output is clear;
  prototype substantiates the team's claims.
- **Low:** broken or unclear demo; mostly conceptual; hard to tell what was built.

### 5. Innovation and originality

Is the framing fresh, ambitious, or insightful?

- **High:** reframes the problem usefully; non-obvious use of technology, policy
  logic, or data; real upside if pursued.
- **Low:** small variation on a common app; a chatbot, dashboard, or form wrapper
  with no insight beyond the implementation.

### 6. Equity and inclusion

Does this support fairer outcomes and broader access?

- **High:** the team clearly considered who gets left out; the design improves
  access; it works for more than the easiest users.
- **Low:** equity ignored; assumes high trust, high literacy, or high digital
  access; could widen existing disparities.

---

## Award weights

One scoring framework, three weightings. Judges never learn a second system;
only the weights change to express what each award is for.

| Category | Near-term award | Visionary award | Theme award |
|---|---:|---:|---:|
| Impact | 5 | 4 | 5 |
| Feasibility | 5 | 2 | 3 |
| User value | 4 | 3 | 4 |
| Execution | 3 | 2 | 3 |
| Innovation | 1 | 5 | 3 |
| Equity and inclusion | 3 | 3 | 3 |
| **Maximum** | **105** | **95** | **105** |

`Weighted total = Σ (category score × category weight)`

**Near-term award** — the strongest case for immediate adoption. Feasibility
matches Impact because the entire point is near-term usefulness. Innovation is
weighted lowest deliberately: this is for the most adoptable idea, not the
coolest one.

**Visionary award** — the strongest long-term upside. Innovation leads. User
value and equity stay mid-weight to stop the award becoming gadget worship.
Feasibility is weighted only enough to exclude total fantasy.

**Theme award** — the best answer to one pillar's problem. Impact on that pillar
leads; feasibility and innovation are balanced equally so neither dominates.

### Tie-break sequences

Declare these with the awards, before submissions open.

| Award | Sequence |
|---|---|
| Near-term | Feasibility → Impact → User value |
| Visionary | Innovation → Impact → Equity |
| Theme | Impact → User value → Feasibility |

If a tie survives the full sequence, it goes to whoever the published decision
rules name as the decider. It is never resolved at the table.

---

## Survivability — five dimensions

Each 1–5. Maximum 25. Minimum 5, because every dimension scores at least 1.

### 1. Ownership clarity

*Is there a named unit that would own and champion this?*

| Score | What it looks like |
|:-:|---|
| 5 | Named owner with mandate and capacity; staff already do related work |
| 4 | Right unit obvious, mandate clear, staffing and budget unverified |
| 3 | Plausible owner, but adjacent to their core work rather than central |
| 2 | Requires two or more units to agree on who owns it |
| 1 | No credible owner inside the institution |

Ideas without an owner become orphans. Someone must be able to say "this is
mine" without convening a committee.

### 2. Data readiness

*Does the data already exist, in accessible form, actively maintained?*

| Score | What it looks like |
|:-:|---|
| 5 | Public, API-accessible, actively maintained — confirmed endpoint, recent update |
| 4 | Public but stale or bulk-only: last refreshed months ago, or CSV export only |
| 3 | Exists but needs curation or one-time digitization |
| 2 | Requires a partnership, data-sharing agreement, or records request |
| 1 | Does not exist; no collection process, no habit of recording it |

"If we just had the data" is the most common last words of a failed project.
Data that does not exist today will not exist next quarter.

### 3. Tech stack fit

*Does it run on what the institution already has, or can trivially acquire?*

| Score | What it looks like |
|:-:|---|
| 5 | Only platforms already confirmed in use |
| 4 | Existing platforms plus commodity cloud, no procurement (static hosting, SMS, free tiers) |
| 3 | One new low-cost tool, but no enterprise procurement cycle |
| 2 | New enterprise software, security review, or server infrastructure |
| 1 | Technology the institution has no experience operating |

Anything outside the current platform orbit needs a procurement cycle measured
in quarters, not weeks.

### 4. Integration surface

*How does it connect to existing internal systems?*

| Score | What it looks like |
|:-:|---|
| 5 | Standalone: reads public APIs only, zero internal changes |
| 4 | Standalone now, richer later if one internal feed is added |
| 3 | Needs one informal data-sharing arrangement — a shared spreadsheet or schedule |
| 2 | Needs a formal agreement, security review, or write access to an internal system |
| 1 | Deep integration with a closed system, or one holding regulated personal data |

Closed vendor platforms without public APIs block any idea that depends on
integrating with them, until a procurement or partnership conversation succeeds.
Those conversations run 6–18 months.

### 5. Maintenance burden

*What does it cost to keep running after launch?*

| Score | What it looks like |
|:-:|---|
| 5 | Automated refresh, no staff time, degrades gracefully — shows "last updated" and keeps working |
| 4 | Under two hours a month: link checks, small config updates, flagged-item review |
| 3 | Regular staff attention: weekly updates, content management, user reports |
| 2 | Dedicated technical staff or a managed paid service |
| 1 | Breaks without constant attention; manual data entry for every use |

Teams are understaffed. A tool needing four hours a week of engineering time is
abandoned within ninety days. The durable ones keep working when nobody watches.

### Tiers

| Tier | Total | Meaning | Action |
|---|:-:|---|---|
| **S** | 21–25 | Ship it — launches with minimal friction | Prioritize for immediate pilot |
| **A** | 16–20 | Strong — one or two solvable blockers | Invest in clearing them |
| **B** | 11–15 | Promising — needs real investment or partnerships | Pursue if a champion emerges |
| **C** | 6–10 | Aspirational — significant structural barriers | Park until conditions change |
| **D** | 5 | Does not survive contact with reality | Archive |

---

## Why these stay separate

An idea can score 95/105 on desirability and 8/25 on survivability. That means it
is a good idea that will never ship, and that is a *conclusion*, not a scoring
error to be smoothed away.

There is a tempting formula that scales survivability up and adds it to the
weighted award totals to produce one number. Do not use it. It reproduces exactly
the averaged verdict that hides the finding. Report the pair.
