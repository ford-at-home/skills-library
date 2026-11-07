# skills-library

131 agent skills by Ford Prior, in 8 categories, collected from 15 repositories.

**Find one fast:** every skill has a record in [`index.json`](index.json): name, description, category, tags, source repo and install command.

## Two tiers

**Reviewed (33, marked ★).** These passed a deletion review. The bar: would a competent agent already do this
correctly without the skill? If yes, it is packaging rather than capability, and it was cut. Two things earn a
place: enforcement the published prose lacks (a gate, a refusal condition, a required output shape), or a failure
that is silent. Ten skills failed that bar; [here they are, with the public skill that does each job better](NOT-SHIPPED.md).

**Collected (98).** Skills written inside Ford's projects: the Amazonian suite, Pace Layers, the
civic hackathon toolkit, the RVA Hacks pillar research environments, Hardcopy Draft, OpenClaw and Jungl3. They have
not been through the deletion review yet. Each record names the repo and path it came from.

## Install

```bash
npx skills add ford-at-home/skills-library --list               # see what's here
npx skills add ford-at-home/skills-library --skill <skill-id>     # install one
```

The [`skills`](https://www.npmjs.com/package/skills) CLI (Node 22.20 or newer) detects your coding agents and
installs into each. Or copy one folder by hand; every folder stands alone:

```bash
cp -r skills/<category>/<skill-id> ~/.claude/skills/     # or ~/.cursor/skills/
```

Skill folders must sit at the top level of `~/.claude/skills/`: copy the skill folder, not its category folder.

## What's in a folder

A `SKILL.md`, and often a `reference/` directory holding what does not need to be read every time: output
templates, failure-mode catalogues, configuration schemas. Skills that arrived without frontmatter were given a
`name` and a `description` taken from their own Purpose line; nothing else was changed.

## Categories

| Category | Skills | What's in it |
|---|---:|---|
| [Decisions & governance](#decisions) | 16 | Gates for a decision before it locks, and reviews after it fires. |
| [Evaluation & scoring](#evaluation) | 8 | Rubrics, benchmarks and scoring models that survive being contested. |
| [Research & evidence](#research) | 22 | Finding, verifying and keeping a corpus of evidence usable. |
| [Writing & communication](#writing) | 10 | Prose that has to land: decision docs, outreach, rollouts. |
| [Engineering & operations](#engineering) | 22 | Changing live systems safely, deploying and running agents. |
| [Product discovery & prototyping](#product) | 15 | From problem to tested prototype: JTBD, MVPs, sprints, demos. |
| [Civic programs & hackathons](#civic) | 22 | Planning and running a civic hackathon end to end. |
| [Org change & cadence](#org-change) | 16 | Plan change at the speed each layer moves, and make it stick. |

## Decisions & governance
<a id="decisions"></a>

| Skill | What it does | From |
|---|---|---|
| [`correction-of-errors`](skills/decisions/correction-of-errors/) | Run a blameless post-incident review (Correction of Errors / CoE) covering incident summary, customer impact, timeline, facts, Five Whys, root… | `amazonian` |
| ★ [`dissent-before-commit`](skills/decisions/dissent-before-commit/) | Gate one already-authorized action that is now scheduled to fire, by re-checking every objection raised at authoring time against what has changed… | `skills-library`, `amazonian` |
| ★ [`initiative-thesis-review`](skills/decisions/initiative-thesis-review/) | Decide whether one initiative is still worth pursuing by testing its tenets — the "if we are wrong about X, we should stop" statements — against… | `skills-library` |
| [`launch-readiness-review`](skills/decisions/launch-readiness-review/) | Gate the launch of a feature, product, or initiative by diffing the current build state against the original PRFAQ contract. Emits one of go / no_go… | `amazonian` |
| [`leadership-principles-reviewer`](skills/decisions/leadership-principles-reviewer/) | Evaluate a proposal, project, PRFAQ, or six-page narrative against Amazon-style leadership principles. Surfaces strongest and weakest alignment,… | `amazonian` |
| [`lifecycle-navigator`](skills/decisions/lifecycle-navigator/) | Read governance.yaml, identify the next required Amazonian skill given the bet's current state, and route the operator either through… | `amazonian` |
| ★ [`multi-persona-roundtable`](skills/decisions/multi-persona-roundtable/) | Stress-test one proposal from several fixed viewpoints that each own a kill criterion, run as separate isolated turns rather than one pass, so you… | `skills-library` |
| ★ [`portfolio-reallocation-review`](skills/decisions/portfolio-reallocation-review/) | Review the allocation of capacity across every initiative a team runs at once by constructing the portfolio you would authorize from scratch today —… | `skills-library` |
| [`portfolio-review`](skills/decisions/portfolio-review/) | Stress-test a team's collective portfolio of bets across a period. Asks not "is each bet still right?" (that is `tenets-review`) but "given… | `amazonian` |
| ★ [`principles-alignment-review`](skills/decisions/principles-alignment-review/) | Review a drafted proposal against a principle set the caller supplies — company values, engineering tenets, a funder's criteria, a team charter —… | `skills-library` |
| [`repo-state-import`](skills/decisions/repo-state-import/) | Lift a brownfield repo's current governance state into a structured governance.yaml manifest. Conducts a guided interview over tenets, success… | `amazonian` |
| [`risk-review`](skills/decisions/risk-review/) | Prevent common civic-tech mistakes and enforce guardrails. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`roundtable-facilitator`](skills/decisions/roundtable-facilitator/) | Orchestrate a multi-turn, multi-persona evaluation of a civic innovation idea. Each persona takes a separate turn with real research, writes to a… | `2026-annual-hackathon` |
| [`roundtable-persona`](skills/decisions/roundtable-persona/) | Template for individual persona turns in a roundtable evaluation. Each subagent loads this skill to understand its output format, research… | `2026-annual-hackathon` |
| [`tenets-review`](skills/decisions/tenets-review/) | Stress-test whether a product or initiative is still worth pursuing by checking its tenets ("if we're wrong about X, stop") against current external… | `amazonian` |
| [`working-backwards-prfaq`](skills/decisions/working-backwards-prfaq/) | Turn an idea into a PRFAQ (Amazon Working Backwards) packet — press release, customer FAQ, internal FAQ, MVP boundary, success metrics, risks,… | `amazonian` |

## Evaluation & scoring
<a id="evaluation"></a>

| Skill | What it does | From |
|---|---|---|
| ★ [`ambitious-goal-grading`](skills/evaluation/ambitious-goal-grading/) | Grade whether a period's goal targets were set at an honest difficulty, not whether they were hit — reconcile every goal the period authorized… | `skills-library`, `amazonian` |
| ★ [`anchored-rubric-design`](skills/evaluation/anchored-rubric-design/) | Design the scale for judging model output — fields that trade off against each other so one cheap trick can't max the score, numbered bands with… | `skills-library` |
| ★ [`auditable-scoring-model`](skills/evaluation/auditable-scoring-model/) | Audit a statistical prediction — a price, rating, duration, or probability fitted from historical records — so target leakage is caught by a failing… | `skills-library` |
| ★ [`defensible-submission-scoring`](skills/evaluation/defensible-submission-scoring/) | Score human submissions to a themed call so the result survives a losing team asking why. Reads the problem statement before the submission, runs… | `skills-library` |
| [`innovation-lifecycle`](skills/evaluation/innovation-lifecycle/) | The canonical lifecycle that every hackathon submission must be forced through. Each stage is scored as `COMPLETE`, `PARTIAL`, `MISSING`, or… | `2026-annual-hackathon` |
| ★ [`llm-behavior-benchmark`](skills/evaluation/llm-behavior-benchmark/) | Execute an existing rubric across several models or prompts so the resulting ranking survives being contested. Pins the run to a content-hashed… | `skills-library` |
| ★ [`operational-message-friction`](skills/evaluation/operational-message-friction/) | Score one unsent operational message against a five-component friction rubric, then compress it only if the score earns a rewrite. Covers the four… | `skills-library` |
| [`ralph-loop`](skills/evaluation/ralph-loop/) | A two-pass quality gate that catches the optimism bias inherent in first-pass reviews. Pass 1 checks completeness against source-of-truth artifacts.… | `2026-annual-hackathon` |

## Research & evidence
<a id="research"></a>

| Skill | What it does | From |
|---|---|---|
| ★ [`architecture-note-routing`](skills/research/architecture-note-routing/) | Take raw architectural thinking — a transcript fragment, voice note, research memo, or half-formed idea in chat — and land it in exactly one durable… | `skills-library` |
| [`architecture-note-synthesis`](skills/research/architecture-note-synthesis/) | Turn a rough architecture fragment, transcript excerpt, or voice-note idea about Jungl3 into the right file(s) under docs/ — routed per CLAUDE.md… | `jungl3` |
| [`corpus-navigation-sync`](skills/research/corpus-navigation-sync/) | Keep the research corpus **traversable by AI agents** whenever reports are added, removed, renamed, or grouped under a new section. | `pillar-thriving-built-environment` |
| [`cross-report-synthesis`](skills/research/cross-report-synthesis/) | Synthesize findings from multiple research reports into a coherent answer while preserving source traceability and acknowledging uncertainty. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| ★ [`customer-interview-synthesis`](skills/research/customer-interview-synthesis/) | Gate a set of customer interviews before their themes become proposal-grade conclusions. Requires the team's prior hypothesis as an input, enforces… | `skills-library`, `amazonian` |
| [`dataset-mapper`](skills/research/dataset-mapper/) | Identify usable datasets, schemas, access paths, and gaps. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`evidence-grounded-answering`](skills/research/evidence-grounded-answering/) | Answer user questions using only content actually present in this repository corpus, with explicit grounding and uncertainty marking. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| ★ [`evidence-grounded-verification`](skills/research/evidence-grounded-verification/) | Clear every load-bearing claim in a document before it reaches someone who can check it. Sorts each claim into do-not-cite, correct-before-use, or… | `skills-library` |
| [`graph-entity-naming`](skills/research/graph-entity-naming/) | Rules for what a knowledge-graph node may be named after, and an audit script that finds junk labels. Use when writing or reviewing extraction… | `pillar-thriving-built-environment` |
| [`jtbd-research`](skills/research/jtbd-research/) | After JTBD analysis produces open questions for a pillar, this skill groups them into efficient Parallel AI research queries, fires them, polls for… | `2026-annual-hackathon` |
| [`knowledge-graph-pipeline`](skills/research/knowledge-graph-pipeline/) | Change the knowledge-graph extractor and publish the result across all seven pillar repos and the rvahacks site. Use when editing anything under… | `pillar-thriving-built-environment` |
| ★ [`markdown-knowledge-graph-traversal`](skills/research/markdown-knowledge-graph-traversal/) | Answer a hard question from a corpus of plain Markdown notes without producing confident soup. Two-pass hybrid retrieval, a typed claim-and-evidence… | `skills-library` |
| ★ [`markdown-memory-schema-maintenance`](skills/research/markdown-memory-schema-maintenance/) | Audit and repair the metadata layer of a Markdown notes corpus, one note at a time, so retrieval and confidence calibration can work. Checks… | `skills-library` |
| [`prior-art-regional-research`](skills/research/prior-art-regional-research/) | Research what has already been built — regionally and nationally — before generating solution ideas. Ensures ideas are grounded in what is known to… | `2026-annual-hackathon` |
| [`repo-librarian`](skills/research/repo-librarian/) | Help users navigate repository knowledge quickly. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`repo-memory`](skills/research/repo-memory/) | Reconstruct repository state and current stage. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`report-update-protocol`](skills/research/report-update-protocol/) | Safely add or update research reports and keep all metadata, indexes, and navigation files synchronized. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`research-corpus-navigation`](skills/research/research-corpus-navigation/) | Map a user question to the correct pillar section and specific research reports before attempting to answer. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| ★ [`research-corpus-self-indexing`](skills/research/research-corpus-self-indexing/) | Keep a growing Markdown corpus findable by maintaining the layer above individual notes — verify the generated index still matches its generator,… | `skills-library` |
| [`research-runner`](skills/research/research-runner/) | Execute research prompts and collect findings with sources. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`research-search`](skills/research/research-search/) | Use when answering questions that require facts, evidence, personas, data sources, risks, or prior art from the Thriving Economy pillar research… | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`run-knowledge-graph`](skills/research/run-knowledge-graph/) | Install and run the Knowledge Graph and 3D Funding Explorer visualization | `pillar-thriving-built-environment` |

## Writing & communication
<a id="writing"></a>

| Skill | What it does | From |
|---|---|---|
| [`amazon-writing-linter`](skills/writing/amazon-writing-linter/) | Rewrite docs into clear, evidence-heavy Amazon-style prose. Strips vague adjectives, unsupported claims, passive evasions, and weasel words; demands… | `amazonian` |
| [`annotation-interpretation`](skills/writing/annotation-interpretation/) | Interpret scanned or photographed pages of the printed Hardcopy Draft artifacts — locate marks with S{n}P{m} anchors and Q{n} question ids, classify… | `cozy-core-foundation` |
| ★ [`communication-rollout-planning`](skills/writing/communication-rollout-planning/) | Sequence a multi-channel announcement into an ordered plan of communication moves with draft copy for each, ordered so nobody who matters hears it… | `skills-library` |
| ★ [`decision-prose-linting`](skills/writing/decision-prose-linting/) | Tighten a decision-bearing draft — memo, brief, proposal, status narrative — without making it more confident than the author was. A removed hedge… | `skills-library` |
| ★ [`paper-markup-revision`](skills/writing/paper-markup-revision/) | Apply edits marked by hand on a printed draft back into the source file, resolving every positional reference to an exact block or refusing to… | `skills-library` |
| [`research-grounded-outreach`](skills/writing/research-grounded-outreach/) | Draft SME outreach emails that lead with confirmed research findings and ask only the questions that genuinely remain unanswered. Replaces the… | `2026-annual-hackathon` |
| [`six-page-narrative`](skills/writing/six-page-narrative/) | Convert a strategy, architecture, or major decision into a six-page narrative — a written decision memo with context, problem, current state,… | `amazonian` |
| [`sme-outreach`](skills/writing/sme-outreach/) | Draft a ready-to-send email to a subject matter expert (city staff, nonprofit professional, or community organization) asking specific questions… | `2026-annual-hackathon` |
| [`synthesize`](skills/writing/synthesize/) | The single transformation primitive of Hardcopy Tools' synthesize contract (vendored from markdown-soul). Takes Markdown content + a required… | `cozy-core-foundation` |
| ★ [`voice-faithful-drafting`](skills/writing/voice-faithful-drafting/) | Draft, rewrite, or weave a long-form piece in one named person's voice, governed by a required brief stating persona, throughline, channel, and… | `skills-library` |

## Engineering & operations
<a id="engineering"></a>

| Skill | What it does | From |
|---|---|---|
| [`adr-author`](skills/engineering/adr-author/) | Write a new Architecture Decision Record for Jungl3 under docs/decisions/, matching the Nygard-trimmed format established by ADRs 0001–0003. Use… | `jungl3` |
| [`billing-and-credits`](skills/engineering/billing-and-credits/) | Change anything money-adjacent — credit packs, the credit ledger, reservations, Stripe checkout, the Stripe webhook, purchase records,… | `cozy-core-foundation` |
| ★ [`compliance-control-audit`](skills/engineering/compliance-control-audit/) | Audit running cloud infrastructure against a named control set and produce findings an auditor can re-derive and an engineer can act on. Reports… | `skills-library` |
| ★ [`corpus-transform`](skills/engineering/corpus-transform/) | Design an expensive, long-running transformation over a large corpus so that a crash loses at most one item, a resume neither duplicates nor skips… | `skills-library` |
| [`mobile-ui-polish`](skills/engineering/mobile-ui-polish/) | Refine the existing Hardcopy Draft UI mobile-first without redesigning it — responsive layout, touch targets, safe areas, keyboard behavior,… | `cozy-core-foundation` |
| [`model-selection-and-spend`](skills/engineering/model-selection-and-spend/) | Decide which Cursor model class to use, when to escalate to a premium model, and how to keep spend within policy. Use for tasks mentioning model… | `cozy-core-foundation` |
| [`multi-agent-coordination`](skills/engineering/multi-agent-coordination/) | Coordinate with the Lovable agent through the docs/coordination/ inbox/outbox protocol — reading incoming requests, filing work items with WI-nnnn… | `cozy-core-foundation` |
| ★ [`multi-agent-turn-taking`](skills/engineering/multi-agent-turn-taking/) | Decide which agent or persona speaks next in a shared live conversation, running a deterministic blocking gate first and letting a model arbitrate… | `skills-library` |
| ★ [`multi-tenant-saas-isolation`](skills/engineering/multi-tenant-saas-isolation/) | Enforce tenant boundaries in a multi-tenant application so that no single bug leaks another tenant's data. Covers where tenant identity may come… | `skills-library` |
| [`openclaw-aws-bootstrap`](skills/engineering/openclaw-aws-bootstrap/) | Bootstrap the AWS infrastructure for an OpenClaw deployment — region selection, instance type sizing, Bedrock model selection, IAM role, S3 bucket,… | `openclaw-public` |
| [`openclaw-channel-setup`](skills/engineering/openclaw-channel-setup/) | Connect the deployed OpenClaw instance to a Telegram bot — token configuration, group/topic setup, allowlist gates, the requireMention semantics.… | `openclaw-public` |
| [`openclaw-customize-workspace`](skills/engineering/openclaw-customize-workspace/) | Turn the patterns/*.example.md templates into a real personal workspace for an OpenClaw deployment — fill in identity, user profile, tone, tools,… | `openclaw-public` |
| [`openclaw-deploy`](skills/engineering/openclaw-deploy/) | Deploy a customized OpenClaw workspace to a running EC2 instance via SSM. Covers initial deployment, the auto-sync cron pattern, and how to verify a… | `openclaw-public` |
| [`openclaw-prerequisites`](skills/engineering/openclaw-prerequisites/) | Verify prerequisites before deploying OpenClaw — AWS account access, Bedrock model enablement, SSM plugin, Telegram bot token, optional Parallel AI… | `openclaw-public` |
| [`openclaw-research-pipeline`](skills/engineering/openclaw-research-pipeline/) | Set up the optional deep-research pipeline — Parallel AI for the research engine, a separate GitHub repo as the published research library, and… | `openclaw-public` |
| [`openclaw-troubleshooting`](skills/engineering/openclaw-troubleshooting/) | Diagnose and fix common OpenClaw deployment issues — bot not responding, gateway service crashed, config rejected, deploy failing, voice memos… | `openclaw-public` |
| [`print-artifact-fidelity`](skills/engineering/print-artifact-fidelity/) | Change the print-for-markup pipeline with deterministic US Letter output — page geometry, margins, S{n}P{m} block anchors, pagination, the… | `cozy-core-foundation` |
| [`production-readiness`](skills/engineering/production-readiness/) | Pre-merge and pre-release review of Hardcopy Draft changes — run every required check, verify failure/loading/retry states, confirm no secret… | `cozy-core-foundation` |
| ★ [`repository-orientation`](skills/engineering/repository-orientation/) | Build an accurate working model of a codebase you have not seen before, treating its documentation as claims to verify against code rather than as… | `skills-library`, `cozy-core-foundation` |
| [`run-orchestration-change`](skills/engineering/run-orchestration-change/) | Change the agent-run orchestration and cost-accounting subsystem — dispatch, webhooks, the reconciler, run state machine, idempotency keys,… | `cozy-core-foundation` |
| ★ [`subsystem-change-safety`](skills/engineering/subsystem-change-safety/) | Change a subsystem that already has users or data depending on it, where a mistake is expensive and does not announce itself. Establishes a… | `skills-library` |
| [`supabase-change`](skills/engineering/supabase-change/) | Make safe Supabase backend changes — schema migrations, RLS policies, Edge Functions, config.toml, storage policies, backend secrets. Use for tasks… | `cozy-core-foundation` |

## Product discovery & prototyping
<a id="product"></a>

| Skill | What it does | From |
|---|---|---|
| [`assumption-mapping`](skills/product/assumption-mapping/) | Identify and prioritize risky assumptions to test before building. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`blue-ocean-reframing`](skills/product/blue-ocean-reframing/) | Redefine a problem space by eliminating competition and assumptions. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`continuity-planner`](skills/product/continuity-planner/) | Identify post-hackathon continuation opportunities and next steps. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`demo-coach`](skills/product/demo-coach/) | Help teams present effectively and score against the rubric. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| ★ [`demo-production`](skills/product/demo-production/) | Use when building a scripted terminal-UI demo program whose output is entirely fixtures (no live backend) and which must serve three consumers at… | `skills-library` |
| ★ [`idea-to-landing-page`](skills/product/idea-to-landing-page/) | Take a raw product idea to a live page that tests whether anyone wants it, without building the product. Writes the hypothesis and the pass/fail… | `skills-library` |
| [`jobs-to-be-done-analysis`](skills/product/jobs-to-be-done-analysis/) | Identify the real user need behind a problem using JTBD framing. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`lean-mvp-experimentation`](skills/product/lean-mvp-experimentation/) | Test a hypothesis using the smallest possible implementation. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`mvp-designer`](skills/product/mvp-designer/) | Turn an approved opportunity into a concrete MVP plan. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`opportunity-mapper`](skills/product/opportunity-mapper/) | Translate research into concrete, buildable solution opportunities. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`problem-scoping`](skills/product/problem-scoping/) | Help the team choose a strong, weekend-feasible problem direction. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| ★ [`prompt-driven-ui-rebuild`](skills/product/prompt-driven-ui-rebuild/) | Build or rebuild a user interface as an ordered sequence of prompts, each starting from verified output rather than accumulated drift. Factors the… | `skills-library` |
| [`rapid-design-sprint`](skills/product/rapid-design-sprint/) | Run a compressed design sprint to move from problem → prototype within hours. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`rapid-ideation-crazy8s`](skills/product/rapid-ideation-crazy8s/) | Generate a high volume of ideas quickly to avoid early convergence. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`systems-mapping`](skills/product/systems-mapping/) | Map interconnected systems to identify leverage points for intervention. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |

## Civic programs & hackathons
<a id="civic"></a>

| Skill | What it does | From |
|---|---|---|
| [`ai-assisted-evaluation`](skills/civic/ai-assisted-evaluation/) | Run a structured AI evaluation pass over the full submission corpus | `annual-civic-hackathon-toolkit` |
| [`civic-alignment`](skills/civic/civic-alignment/) | Anchor the event in a real, public, government-owned strategic plan | `annual-civic-hackathon-toolkit` |
| [`civic-alignment-check`](skills/civic/civic-alignment-check/) | Ensure solution aligns with Richmond MAP pillars and real city constraints. | `pillar-thriving-built-environment`, `pillar-thriving-economy` +5 |
| [`community-outreach-plan`](skills/civic/community-outreach-plan/) | Plan and stage the public communications that bring participants, | `annual-civic-hackathon-toolkit` |
| [`data-readiness`](skills/civic/data-readiness/) | For every dataset the problem statements reference, answer four | `annual-civic-hackathon-toolkit` |
| [`event-charter`](skills/civic/event-charter/) | Convert civic alignment into a small set of documents the | `annual-civic-hackathon-toolkit` |
| [`event-operations-plan`](skills/civic/event-operations-plan/) | Resolve everything upstream into the operational artifacts the | `annual-civic-hackathon-toolkit` |
| [`governance-model`](skills/civic/governance-model/) | Define how the event is governed: the organizing body's structure, | `annual-civic-hackathon-toolkit` |
| [`judging-system`](skills/civic/judging-system/) | Define how the event evaluates and recognizes work: rubric, awards | `annual-civic-hackathon-toolkit` |
| [`mentor-volunteer-ops`](skills/civic/mentor-volunteer-ops/) | Recruit, onboard, and schedule the two cohorts that make an event | `annual-civic-hackathon-toolkit` |
| [`open-source-handoff`](skills/civic/open-source-handoff/) | Define how the event's outputs become public, durable artifacts the | `annual-civic-hackathon-toolkit` |
| [`participant-experience-plan`](skills/civic/participant-experience-plan/) | Design what a participant actually goes through: register, arrive, | `annual-civic-hackathon-toolkit` |
| [`partnership-and-sponsor-plan`](skills/civic/partnership-and-sponsor-plan/) | Define how the event raises money, in-kind contributions, and | `annual-civic-hackathon-toolkit` |
| [`pillar-pipeline`](skills/civic/pillar-pipeline/) | A two-pipeline system that (A) evaluates hackathon submissions against the actual problem they were supposed to solve, and (B) independently… | `2026-annual-hackathon` |
| ★ [`pillar-program-design`](skills/civic/pillar-program-design/) | Turn a public strategic plan into a small set of thematic pillars, each carrying scoped problem statements a team can build against in a weekend.… | `skills-library` |
| [`plugin-orientation`](skills/civic/plugin-orientation/) | Inspect the repository, classify what planning work is present vs. | `annual-civic-hackathon-toolkit` |
| [`post-event-pipeline`](skills/civic/post-event-pipeline/) | Convert the event's outputs (submissions + AI evaluation + judging | `annual-civic-hackathon-toolkit` |
| [`problem-statement-development`](skills/civic/problem-statement-development/) | Convert each track into named, scoped, data-grounded problem | `annual-civic-hackathon-toolkit` |
| [`retrospective-and-next-year-plan`](skills/civic/retrospective-and-next-year-plan/) | Close the loop. Compare what actually happened to what was | `annual-civic-hackathon-toolkit` |
| [`stakeholder-map`](skills/civic/stakeholder-map/) | Identify every category of stakeholder, every named partner, and | `annual-civic-hackathon-toolkit` |
| [`technology-setup`](skills/civic/technology-setup/) | Decide and document every tool the event runs on: communications, | `annual-civic-hackathon-toolkit` |
| [`track-strategy`](skills/civic/track-strategy/) | Decide the track structure: how many tracks, what each is called, | `annual-civic-hackathon-toolkit` |

## Org change & cadence
<a id="org-change"></a>

| Skill | What it does | From |
|---|---|---|
| [`convene`](skills/org-change/convene/) | Turns a pace-layers analysis into a plan document and the roster of people to bring into the room to review it together, plus a facilitated "imagine… | `pace-layers` |
| [`goal-at-layer`](skills/org-change/goal-at-layer/) | Turns a vague change ambition into a precise goal pinned to a pace layer, with the lever layer, a realistic horizon, evidence for done, constraints,… | `pace-layers` |
| [`layer-culture`](skills/org-change/layer-culture/) | Interviews and diagnoses the Organizational Culture layer (ownership, trust, craft standards, incident norms, and what actually gets rewarded and… | `pace-layers` |
| [`layer-domain`](skills/org-change/layer-domain/) | Interviews and diagnoses the Domain Architecture and Systems of Record layer (domain model, bounded contexts, canonical data, core systems and… | `pace-layers` |
| [`layer-generation`](skills/org-change/layer-generation/) | Interviews and diagnoses the Generation layer, the fastest pace layer, where people and AI agents write code (tools, context files, prompts, local… | `pace-layers` |
| [`layer-governance`](skills/org-change/layer-governance/) | Interviews and diagnoses the Governance layer (security, compliance, risk and model risk, change approval, funding cycles, regulation, and AI… | `pace-layers` |
| [`layer-nature`](skills/org-change/layer-nature/) | Interviews and diagnoses the Nature layer, the slowest pace layer, made of constraints an organization cannot change and must design within (human… | `pace-layers` |
| [`layer-platform`](skills/org-change/layer-platform/) | Interviews and diagnoses the Platform and Infrastructure layer (CI/CD platform, runtime, cloud, internal developer platform, golden paths, model… | `pace-layers` |
| [`layer-product`](skills/org-change/layer-product/) | Interviews and diagnoses the Product and Coordination layer (intent, specs, priorities, roadmaps, intake, and sequencing work across teams). Use… | `pace-layers` |
| [`layer-verification`](skills/org-change/layer-verification/) | Interviews and diagnoses the Integration and Verification layer (code review, CI, tests, merge, release, observability, incident response,… | `pace-layers` |
| [`mechanism-designer`](skills/org-change/mechanism-designer/) | Convert a goal into a recurring operational mechanism with cadence, inputs, outputs, inspection method, escalation rule, and a 30-day trial. Use… | `amazonian` |
| ★ [`meeting-decision-tracking`](skills/org-change/meeting-decision-tracking/) | Run one cycle of a recurring team meeting as a single unit — agenda, notes, tracker sync — where the agenda gives every line a stable item ID and… | `skills-library` |
| [`pace-layers`](skills/org-change/pace-layers/) | Guides a person through planning a change in how their software organization works, using a pace-layer model adapted from Stewart Brand. Use when… | `pace-layers` |
| ★ [`recurring-mechanism-design`](skills/org-change/recurring-mechanism-design/) | Convert a goal into a recurring mechanism that keeps working after the motivation that set it is gone, by designing against silent decay… | `skills-library` |
| [`shear-check`](skills/org-change/shear-check/) | Diagnoses the boundaries ("shears") between adjacent pace layers, where tension builds because the two sides move at different speeds and where… | `pace-layers` |
| [`weekly-business-review`](skills/org-change/weekly-business-review/) | Generate a Weekly Business Review (WBR) from metrics and operating notes. Connects input metrics, output metrics, week-over-week variance, risks,… | `amazonian` |

## If you only install three

| You are | Start with |
|---|---|
| An engineer inheriting or changing a live system | `repository-orientation`, `subsystem-change-safety`, `evidence-grounded-verification` |
| A product owner running reviews and decisions | `dissent-before-commit`, `initiative-thesis-review`, `anchored-rubric-design` |
| Leading a team and its cadence | `recurring-mechanism-design`, `meeting-decision-tracking`, `ambitious-goal-grading` |

## What these are not

None of them has been executed as part of publishing this repository. They are procedures, not tested programs,
and nothing here claims otherwise.

## License

MIT. See [LICENSE](LICENSE).
