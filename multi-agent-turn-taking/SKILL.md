---
name: multi-agent-turn-taking
description: Decide which agent or persona speaks next in a shared live conversation, running a deterministic blocking gate first and letting a model arbitrate only among the candidates that survive it. Covers the five blocking rules, the bounded arbiter, and where turn state has to live for a correct-looking gate to block anything at all. Use when several bots, personas, or agents share one channel and one of them dominates, two ping-pong, the same prompt gets answered twice, or rate limits are silently exceeded. Trigger phrases include who speaks next, bots talking over each other, agent keeps replying to itself, ping-pong loop, one persona dominates, speaker selection, reply cooldown, turn arbitration, multi-bot channel.
---

# Multi-Agent Turn Taking

Decide which participant speaks next in a shared conversation: a deterministic gate
rejects candidates first, and a model arbitrates only among what is left.

Output is a **turn decision record** — one row per candidate per turn, naming the
rule that blocked it or the score that carried it. The record is the audit trail.
When turn-taking misbehaves, you read the record, not the transcript.

The premise: *who speaks next* is mostly a bookkeeping question — did this
participant just speak, is it waiting on someone, has it used its budget — and
bookkeeping answered by a language model is expensive, unauditable, and agreeable.
The model is useful only for the residual judgment of timing and fit, and only
after the bookkeeping has already narrowed the field.

## Use when

- Two or more agents, bots, or personas post into one shared channel or thread
- One participant dominates, or two lock into alternating replies
- One human message draws several near-identical agent responses
- A per-participant rate limit exists and is being exceeded without anyone knowing why
- You are about to write "ask the model whether it should respond" into a loop that
  runs on every inbound message

## Don't use when

- Personas are run in deliberately isolated turns to evaluate one artifact, with no
  shared live channel. That is `multi-persona-roundtable`, and its turns are
  sequenced by the process, not arbitrated.
- You are measuring how a model behaves across prompts rather than running a
  conversation. That is `llm-behavior-benchmark`.
- You are judging whether a single message is worth sending to humans and how to
  word it. That is `operational-message-friction`.
- There is exactly one agent. Cooldown and rate limiting are still worth having,
  but you do not need arbitration and this skill will overbuild it.
- The conversation is strictly turn-based by construction (a queue, a round-robin,
  a workflow). Nothing is contested, so there is nothing to arbitrate.

## Inputs

Ask for these. Don't infer them.

```yaml
participants:       # named speakers. Humans and agents must be distinguishable
                    # at read time, not by guessing from the name
turn_state_store:   # where cooldowns, last-spoke times and per-period counters
                    # live. "In the process" is an answer, and a problem
transcript_window:  # how many recent turns the gate and arbiter may see
blocking_rules:     # the vetoes, enumerated. See below for the default five
budget:             # turns per participant per period, and the cost ceiling
                    # for arbiter calls per period
human_deference:    # how many turns, or how many seconds, agents stay quiet
                    # after a human speaks
```

**If `turn_state_store` is missing, stop and ask.** Every blocking rule reads that
store. A gate over absent state passes everything while looking correct, and this
is the single most common way this mechanism fails silently. Which stores work,
and the three questions to answer before shipping, are in
`reference/turn-state.md`.

**If humans and agents cannot be told apart in the transcript, stop and ask.**
Deference and self-reply detection both depend on it.

## Gates

These run before any model call, in this order, cheapest first. The first block
ends the decision for that candidate.

| # | Rule | Blocks when |
|---|---|---|
| 1 | **No consecutive self-reply** | The last turn in the channel was this participant's |
| 2 | **Addressed and unanswered** | This participant's last turn addressed another participant by name, and neither that participant nor a third party has spoken since |
| 3 | **Cooldown** | This participant spoke less than N seconds ago |
| 4 | **Period cap** | This participant has used its turns-per-period budget |
| 5 | **Human deference** | A human spoke within the deference window |

Each rule returns a verdict and, on a block, the rule's name. A block with no named
rule is a bug, not a quiet decision.

Rule 2 is the one that stops ping-pong, and it is the one people leave out. Rules
1, 3, and 4 all permit A→B→A→B indefinitely as long as the cooldown is short.

### Overrides are rules, not exceptions

Dead air needs to be breakable or the conversation stalls whenever a human leaves
mid-thread. Express that as a numbered rule with its own threshold — "silence
exceeding T seconds suspends rule 5" — placed in the ordered list. An override
written as a special case in the scoring step is unauditable and will grow.

## Process

1. **Snapshot state once.** Read the turn-state store one time for this decision.
   A gate that re-reads between rules can block on rule 3 using a timestamp that
   rule 4 has already superseded.

2. **Run the blocking rules in order.** On the first block, record the rule name
   and stop. Do not score. Do not call the model.

3. **Score the survivors deterministically.** A base rate per participant, plus
   named modifiers with written-down values: addressed directly, topic match,
   duration since last turn, spoke very recently, currently the dominant speaker,
   currently the quietest participant. Clamp to the range.

4. **Apply a cost gate before the arbiter.** Consult the model only for candidates
   whose deterministic score already clears a threshold. Below it, the arbiter can
   only change a decision that was going to be no anyway, and you pay per inbound
   message per participant for the privilege.

5. **Call the arbiter, bounded.** It sees the transcript window and the current
   score. It returns one scalar in a stated range, under a small token cap. It does
   not return prose, and it does not return a decision.

6. **Blend with a written-down cap.** `final = deterministic × (1 − w) + arbiter × w`
   with `w` small — 0.3 is a defensible starting point. Fix `w` before the first
   run. A weight tuned after you see outputs is a weight tuned to agree with you.

7. **Decide.** Threshold, or sample against the final score if you want variation.
   Sampling is a choice with a cost: it makes the record the only explanation of
   why a specific turn happened.

8. **Write the decision record and the state update together.** If the participant
   speaks, its last-spoke time and period counter must be written in the same step
   that emits the turn. A speak-then-write-later ordering double-posts under
   concurrency.

## Hard rules

These are rules rather than advice because each one, when violated, still yields a
conversation that reads as if turn-taking worked. Nothing in the transcript shows
that a rule was skipped.

```text
The arbiter never unblocks. It only adjusts scores among candidates that passed.
Arbiter failure degrades to the deterministic score, never to "speak".
Turn state is read once and written once per decision.
The state write and the emit happen together or neither happens.
Humans outrank agents, as a blocking rule and not a modifier.
A participant that cannot see its own last turn will double-post.
```

## Output

One row per candidate per turn, with the blocking rule or the scores that carried
it. The table is in `reference/decision-record.md`.

## Stop instead of guessing

- **`turn_state_store` unknown** → stop and ask. Do not build the gate first and
  wire state later; the gate will be tested against absent state and will pass.
- **Humans and agents indistinguishable in the transcript** → stop and ask.
- **Blocking rules cannot be enumerated** → stop. If every constraint is a "should
  probably not," there is no gate, and what you are building is a probability model
  with a gate's name on it.
- **Asked to let the model decide the whole thing** → refuse, and give the two
  reasons: cost scales as participants × inbound messages, and when it misbehaves
  there is no rule to point at, only a prompt to reword.
- **Asked to add a bypass for an important turn** → refuse. A bypass becomes the
  path within a month, and the first thing it bypasses is the rate limit.
- **All candidates blocked, each waiting on another** → emit the no-speaker record
  and let the channel be quiet. Do not relax a rule to fill silence. If silence is
  genuinely unacceptable, add a numbered dead-air rule with a threshold.
- **Asked to tune by lowering base rates** → stop and ask for the target rate in
  turns per hour. Repeated halving of base probabilities is the symptom of a system
  with no stated target.

## Further reading in this folder

- `reference/turn-state.md` — which stores make the gate enforceable, which make
  it inert, and the three deployment questions to answer before shipping
- `reference/decision-record.md` — the per-candidate decision table, and why a
  turn with no speaker still emits a record
- `reference/failure-modes.md` — the stubbed state loader, two replicas with two
  counters, ping-pong, domination, the agreeable arbiter, and two timing traps
