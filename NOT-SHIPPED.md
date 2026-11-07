# What we didn't ship

Ten skills were written and then deleted, or rejected before they were written.
This page exists because it is the only honest way to tell you what the bar was.

The test each one failed: **would a competent agent already do this correctly
without the skill?** If yes, the skill is packaging, not capability. A skill named
for a tool or a well-known practice — "CDK", "ADRs", "postmortems" — is usually
restating material that is already in the official docs, in every tutorial, and in
the model's weights. Writing it down again adds nothing, costs a read, and
competes for trigger phrases with the material that *is* novel.

Two things save a skill from that test. It can encode **enforcement the published
prose lacks** — gates, refusal conditions, a required output shape. Or the failure
it prevents can be **silent**, which is the case worth paying for. If neither
applies, it shouldn't exist.

Where we found a public skill that does the job as well or better, it's named
below. Use it. That's a better outcome for you than a worse copy from us.

## Cut against verified public alternatives

**Working-backwards PR/FAQ** and **six-page narrative.** Both are covered by
public skills that gate at least as strictly:
[`borghei/Claude-Skills`](https://github.com/borghei/Claude-Skills) (PR/FAQ with
10–20 Q&A across nine named categories and a five-readers rule),
[`robdefeo/agent-skills`](https://github.com/robdefeo/agent-skills) (seven common
rejection reasons), and
[`bmad-code-org/BMAD-METHOD`](https://github.com/bmad-code-org/BMAD-METHOD) (a
five-stage gated pipeline with a coach that refuses). Ours was 272 lines of
document form protecting one rule about recording dissent.

**Correction of errors / incident postmortem.** At least five public skills encode
this, including
[`github/awesome-copilot`](https://github.com/github/awesome-copilot) and
`SkillMedev/skills/postmortem-writer`. The rule we thought was ours — that a
causal chain ending in a person's name is an unfinished chain — is stated almost
verbatim in the public version, along with classifying every action item as
prevent, detect, or mitigate.

**Weekly business review.** Public WBR skills exist, and the input-versus-output
metric distinction plus the four-category structure are first-page search results.

**Resilience / degraded-state review.** Rejected before extraction. Three public
skills cover it more thoroughly than our source did:
`educlopez/ui-craft` (`state-design.md`, each state with its common mistake named
and required states gated by a craft level), `mblode/agent-skills`
(`ui-audit/states-coverage.md`, a per-state coverage map with detection greps and
the state pairings where "one without the other is the bug that ships"), and
`crouton-labs/crouton-kit` (timeout thresholds, partial-load isolation, retry with
backoff, labelling stale cached data by age).

**Product backlog composer.** Rejected before extraction.
[`jovd83/backlog-story-generator`](https://github.com/jovd83/backlog-story-generator)
does the whole job — epics shaped around business capabilities, one file per
story, export to GitHub Issues and Jira — and already carries the discipline we
would have claimed as our reason to exist: separate evidence from assumptions,
don't pretend unknown details are known, validate before claiming the pack is
ready. `mindaugasnakrosis/mdjira` additionally cites its sources per rule.

## Cut against skills that ship with common agent installs

For these we verified duplication against collections already installed locally
rather than against a specific public repository, so we're citing the capability
rather than a URL. Check what your setup already has before looking for a
replacement — it probably has one.

- **Decision-record / ADR authoring.** Covered by widely distributed ADR skills.
- **Launch readiness review.** Covered by shipping and launch-checklist skills.
- **Phased delivery planning.** Covered by task-breakdown and plan-writing skills.
- **AWS serverless app scaffold.** Covered by the AWS deployment plugin. We also
  found that its supposed non-obvious core — packaging a native dependency as a
  Lambda layer for ARM, and the flag whose omission produces a layer that only
  fails at runtime — is itself well documented.

## One reversal

**Demo production** was deleted here and then restored. The deletion was correct
about its evidence and wrong about its target: public VHS skills do cover
tape-as-code, reproducibility, CI golden files, and GIF size optimization, and our
version was padded with all four. But none of them covered the reason it was
written — that pacing jitter has to be suppressed below the fast-forward threshold
or a CI run stops being deterministic, and that a terminal UI's bytes are not a
stable test surface, so the smoke test asserts an exit code and refuses to parse
output.

It came back trimmed to that core. We're recording the reversal because a bar you
never misapply is a bar you aren't actually using, and because the failure mode
was instructive: the review disproved a claim we had already retracted, and never
tested the one we were making.

## The count

Ten cut and one reversed, against thirty-three kept. We think that ratio is the
most useful number on this page.

The last five to be tested weren't cut, but four of them lost between a quarter
and half their content, and five reference files went away entirely — roughly
2,300 lines down to 1,500. In most of those cases the material we deleted was the
part that sounded most like the skill's purpose. Speaker attribution in a meeting
workflow, dissent capture before an irreversible decision, "would we fund this
today" — all published elsewhere, all cut. What was left in each was one refusal
condition we couldn't find anywhere, which is a less impressive-sounding skill and
a more useful one.

## The second cut: rules, not skills

Anthropic then published guidance for the Claude 5 generation of models, reporting
that they had removed over 80% of Claude Code's system prompt with no measurable
loss. The argument is that rules written to prevent bad judgement can go, because
the judgement is now there, and that overlapping instructions cost the model
reasoning before it can act.

We ran the same test on every skill here. The always-read surface went from about
9,300 lines to about 5,900.

**The largest category was not overconstraint. It was us repeating ourselves.**
Twenty-six skills ended with a "Before returning, check" block that re-listed
their own rules as checkboxes, and several stated the same constraint a third time
in a gate table and a fourth in stop conditions. That was our own authoring
standard's fault: it named gates, hard rules, failure modes, and stop conditions
as required sections and never said a constraint belongs in exactly one of them.
Every section had to be filled, and the same rule fit all four.

**Two rules were not redundant but wrong.** One skill required "zero edits to
existing tests, fixtures, or check scripts. Zero, not few" while its own scope
section listed changes that legitimately require a fixture edit. Another held "one
clarifying question per turn" in the same file as "stop and name all of them in
one message" — two rules that were never compatible, costing reasoning every time
the skill ran.

**Six local conventions had been stated as universal law**, which is worse than
verbose: it is wrong advice. Never passing a profile flag to a cloud CLI. Routing
every write through one vendor's tooling. A commit-granularity policy. A webhook
architecture preference. Five more surfaced on a second reading, including a
skill that offered Postgres as an input and then required an AWS-specific error
type to pass its own audit — so a team doing the right thing on the wrong stack
could not pass.

**Three skills would not have loaded at all.** Their frontmatter descriptions
contained a bare colon followed by a space inside an unquoted YAML scalar, which
terminates a plain scalar and fails the parse. One of them was the skill we had
just examined closely and declared exemplary. We had checked whether its rules
were good and never checked whether it opens.

What survived is narrower and states why. Every remaining block of hard rules now
opens with a sentence saying what makes them rules rather than advice — the
failure produces output that looks correct — because without it, the next person
to read them will reasonably soften them.
