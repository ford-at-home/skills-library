# Where turn state has to live

Turn state is not cache. It is the correctness substrate for every blocking rule.

Any of these makes the gate useless:

- **Process memory with more than one replica.** Each replica keeps its own
  counters, so each independently believes the participant is under its cap. Two
  replicas double the effective rate and answer the same prompt twice.
- **A state loader that returns a fresh empty object.** Rules 3 and 4 read zeros,
  find no violation, and pass. The gate is present, ordered, and inert.
- **Per-channel state keyed only by participant.** Cross-channel rate limits are
  unenforceable, so a capped participant just moves to another channel.

Before shipping, answer these three in writing:

1. How many replicas can run this gate at once? If more than one, the store is
   shared and the counter increment is atomic, or the answer is one replica.
2. What happens to cooldowns and counters on restart? Losing them means a restart
   grants every participant a fresh budget.
3. Is the increment in the same transaction as the emit?

A single-connection consumer — one websocket, one gateway session — that is
horizontally autoscaled is broken independent of turn-taking: the second replica
either duplicates every emit or fights for the connection. If the deployment
declares one desired instance and also permits scaling to two "for availability,"
that is not availability, and turn state is where the damage shows up first.
