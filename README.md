# skills-library

Thirty-three agent skills that survived a deletion review.

The bar: **would a competent agent already do this correctly without the skill?**
If yes, it's packaging rather than capability, and it isn't here. A skill named
for a tool or a famous practice — "CDK", "ADRs", "postmortems" — is usually
restating what's already in the docs, in every tutorial, and in the model's
weights. It costs you a read, and it competes for trigger phrases with the
material that actually helps.

Two things earn a place. **Enforcement the published prose lacks** — a gate, a
refusal condition, a required output shape. Or **a failure that is silent**, which
is the kind worth paying for.

Ten skills were written and then deleted, or rejected before they were written.
**[Here they are, with the public skill that does each job better.](NOT-SHIPPED.md)**
Read that first — it says more about what's in here than the index does.

The same bar was then applied a second time, to the rules *inside* the surviving
skills. A rule that substitutes for judgement a capable model already has is
noise, and it competes with the rules that matter. What's left is the subset whose
violation produces output indistinguishable from correct output — the case where
better judgement doesn't help, because nothing signals that a judgement was
needed. That pass removed about a third of the text.

## Install

Every folder stands alone. No shared config, no parent files, no install step,
no other skill required.

```bash
npx skills add ford-at-home/skills-library --list               # see what's here
npx skills add ford-at-home/skills-library --skill <skill-name>   # install one
```

The [`skills`](https://www.npmjs.com/package/skills) CLI detects your coding agents and installs into each. Or copy a folder by hand:

```bash
cp -r <skill-name> ~/.claude/skills/     # or ~/.cursor/skills/
```

Skill folders must sit at the top level of `~/.claude/skills/`. Discovery is a
single non-recursive scan, so a skill nested one directory deeper is never found
and never reports an error. That's also why this repository is flat rather than
sorted into category folders — the grouping below is editorial.

## What's in a folder

A `SKILL.md` under about 180 lines, and usually a `reference/` directory holding
what didn't need to be read every time — output templates, failure-mode
catalogues, configuration schemas, extended worked reasoning. `SKILL.md` ends with
a list of those files and what each one holds.

The split is the point. Everything a skill knows used to sit in one file, which
meant every invocation paid for all of it. Now the always-read part carries the
thesis, the inputs, the process, and the rules; the rest loads when the work
actually calls for it. Portability is unaffected — the reference files live inside
the skill folder, so copying the folder still copies everything.

## Skills

### Before you commit

Gates for a decision that is about to lock, or has locked and is about to fire.

| Skill | Purpose |
|---|---|
| [`dissent-before-commit`](dissent-before-commit/) | Gate an action authorized weeks ago and now scheduled to fire, re-checking every prior objection against what has changed since — and, for one-way doors, removing the option to merely accept it |
| [`multi-persona-roundtable`](multi-persona-roundtable/) | Stress-test a proposal from fixed viewpoints that each own a kill criterion, in isolated turns, so you get disagreement rather than an average |
| [`initiative-thesis-review`](initiative-thesis-review/) | Decide whether an initiative is still worth pursuing by testing its tenets against external evidence rather than against its own dashboard |
| [`portfolio-reallocation-review`](portfolio-reallocation-review/) | Review capacity across every initiative at once by first rebuilding, blind, the portfolio you would authorize today — a review that consulted the current allocation first is rejected |
| [`principles-alignment-review`](principles-alignment-review/) | Review a proposal against a supplied principle set, reporting where it is silent and where it invokes one principle to excuse skipping another |

### Judging quality at scale

Turning a judgement you can only make by eye into one that survives being contested.

| Skill | Purpose |
|---|---|
| [`anchored-rubric-design`](anchored-rubric-design/) | Turn a fuzzy quality judgement into a rubric that survives disagreement: anchored bands, fields that trade off against each other, a deterministic composite |
| [`llm-behavior-benchmark`](llm-behavior-benchmark/) | Run a model benchmark whose ranking survives being contested, validating that the judge discriminates before anything is published |
| [`defensible-submission-scoring`](defensible-submission-scoring/) | Score submissions to a themed call so the result survives a losing team asking why, keeping desirability and survivability separate |
| [`auditable-scoring-model`](auditable-scoring-model/) | Build a predictive scoring model where target leakage fails an assertion instead of showing up as an implausibly good validation score |
| [`operational-message-friction`](operational-message-friction/) | Score an operational message against a friction rubric before sending, and compress it only if the score earns a rewrite |
| [`ambitious-goal-grading`](ambitious-goal-grading/) | Audit a period's goal grading for integrity — reconcile every authorized goal, recompute moved targets against their originals, require named surprise evidence for anything hit at 100% |

### Checking whether it's true

For claims that feel established because they've been repeated.

| Skill | Purpose |
|---|---|
| [`evidence-grounded-verification`](evidence-grounded-verification/) | Clear a document's load-bearing claims before it reaches someone who can check them, catching claims that feel established because your own team repeated them |
| [`repository-orientation`](repository-orientation/) | Build a working model of an unfamiliar codebase by treating its documentation as claims to verify against code |
| [`compliance-control-audit`](compliance-control-audit/) | Audit running infrastructure against a named control set, read-only, reporting what was not checked as loudly as what failed |

### Changing systems that already have users

Where the cost of being wrong is paid by someone else's data.

| Skill | Purpose |
|---|---|
| [`subsystem-change-safety`](subsystem-change-safety/) | Change a subsystem that already has users or data depending on it, triaging by reversibility and ordering migration and rollback |
| [`multi-tenant-saas-isolation`](multi-tenant-saas-isolation/) | Enforce tenant boundaries so no single bug leaks another tenant's data, including why tenant context must never travel through a prompt |
| [`corpus-transform`](corpus-transform/) | Run a long, expensive transformation over a large corpus so a crash loses one item, a resume neither duplicates nor skips, and the bill is known before it is spent |
| [`multi-agent-turn-taking`](multi-agent-turn-taking/) | Decide which agent speaks next in a shared channel using a deterministic blocking gate ahead of any model arbitration |

### Building something new

| Skill | Purpose |
|---|---|
| [`prompt-driven-ui-rebuild`](prompt-driven-ui-rebuild/) | Build a UI as an ordered prompt sequence where each step starts from verified output and carries an explicit rejection list |
| [`idea-to-landing-page`](idea-to-landing-page/) | Test demand with a live page that commits to a pass/fail threshold before the page exists and cannot promise a product that does not exist yet |
| [`demo-production`](demo-production/) | Drive a scripted terminal demo from one binary serving a live operator, a screen recorder, and CI — with pacing jitter suppressed below the fast-forward threshold so a CI run stays deterministic |

### Keeping a corpus of notes usable

| Skill | Purpose |
|---|---|
| [`markdown-knowledge-graph-traversal`](markdown-knowledge-graph-traversal/) | Answer a hard question from a Markdown corpus with typed claims scored on confidence and source quality as separate axes |
| [`markdown-memory-schema-maintenance`](markdown-memory-schema-maintenance/) | Audit and repair the metadata layer of a Markdown notes corpus so retrieval and confidence calibration can work |
| [`research-corpus-self-indexing`](research-corpus-self-indexing/) | Keep a growing Markdown corpus findable by verifying the generated index still matches its generator and every capture was promoted |
| [`architecture-note-routing`](architecture-note-routing/) | Land a raw fragment of thinking in exactly one durable document without inventing detail or silently reconciling a contradiction |

### Writing that has to land

| Skill | Purpose |
|---|---|
| [`voice-faithful-drafting`](voice-faithful-drafting/) | Draft long-form in one person's voice from a brief, refusing to infer persona or throughline from the source material |
| [`decision-prose-linting`](decision-prose-linting/) | Tighten a decision-bearing draft without making it more confident than the author was, logging every removal so nothing load-bearing is lost silently |
| [`paper-markup-revision`](paper-markup-revision/) | Apply hand-marked edits from a printout back into the source, resolving every positional reference or refusing to guess |
| [`communication-rollout-planning`](communication-rollout-planning/) | Sequence a multi-channel announcement so nobody who matters hears it from a broadcast |
| [`customer-interview-synthesis`](customer-interview-synthesis/) | Synthesize interviews without laundering the team's prior — the hypothesis going in is a required input, the sample floor downgrades the artifact class rather than bending, and a claim without a quote gets stripped |

### Running a team's cadence

| Skill | Purpose |
|---|---|
| [`meeting-decision-tracking`](meeting-decision-tracking/) | Turn a recurring meeting's decisions into tracked issues within hours, binding each action to its item by agenda ID and refusing to match on title similarity at any confidence |
| [`recurring-mechanism-design`](recurring-mechanism-design/) | Turn a goal into a recurring mechanism designed so its decay is visible — a second-party inspector, escalation on a missed run, trial criteria written first |
| [`pillar-program-design`](pillar-program-design/) | Turn a strategic plan into thematic pillars carrying problems a team can build in a weekend, each with a real dataset and a named human to ask |

## If you only install three

| You are | Start with |
|---|---|
| An engineer inheriting or changing a live system | `repository-orientation`, `subsystem-change-safety`, `evidence-grounded-verification` |
| A product owner running reviews and decisions | `dissent-before-commit`, `initiative-thesis-review`, `anchored-rubric-design` |
| Leading a team and its cadence | `recurring-mechanism-design`, `meeting-decision-tracking`, `ambitious-goal-grading` |

## What these have in common

They refuse rather than guess. Given a missing input, each one stops and says what
it needs instead of inferring a plausible value and producing output that looks
identical to the real thing. Each declares what makes it stop, names how it goes
wrong, and states what it is *not* for so it does not get invoked in place of a
better fit.

## What these are not

None of them has been executed as part of publishing this repository. They are
procedures, not tested programs, and nothing here claims otherwise. Where a skill
cites a defect from a real deployment, it says so and says which parts were
changed.

## License

MIT. See [LICENSE](LICENSE).
