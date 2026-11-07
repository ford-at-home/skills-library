# Heuristics for testing a theory of change

Use these in Phase 5. For each one that applies, state whether the user's theory **holds**, **bends**, or **breaks**, and cite evidence from the conversation. Do not recite the list to the user. Surface only the heuristics that change the answer.

## H1. Find the lever, not the symptom

Symptoms surface in fast layers. Levers usually sit slower.

- **Test:** If the user's proposed change succeeded and nothing in any slower layer changed, would the old behavior come back? If yes, the lever is in that slower layer.
- **If it breaks:** Re-aim the plan at the slower layer. Keep the fast-layer change as an experiment that produces evidence for the slow-layer decision.

## H2. Match the move to the clock

Each layer has a natural clock and a reform horizon (see `model.md`).

- **Test:** Compare the plan's timeline with the reform horizon of the layer it must change.
- **If it breaks:**
  - Too fast for a slow layer: expect brittleness, cynicism, or revolt. Brand's examples are revolutions and failed five-year plans. Stretch the horizon, or set a faster waypoint goal that produces evidence.
  - Too slow for a fast layer: expect shadow work, routing around, and talent loss. Release the fast layer, and protect the slow layer with an interface instead of a ban.

## H3. Fast proposes, slow disposes

Fast layers generate options. Slow layers decide which ones last.

- **Test:** Does the plan include a *sifting mechanism*, a defined way for a successful fast-layer experiment to become a slow-layer standard? Who decides, on what evidence, at what cadence?
- **If it breaks:** Add the sifting step and name its owner. Without one, experiments either die unadopted or leak into slow layers unvetted.

## H4. Slow controls fast by constraint and constancy

The binding constraint is usually a slow-layer fact: a data model, a control, a norm, a cognitive limit.

- **Test:** Name the constraint that most limits the goal. Is the plan working within it, changing it, or ignoring it?
- **If it breaks:** Ignoring a binding constraint is the most common fatal flaw. Decide explicitly whether to work within it or change it. Changing it means the plan now has a slower lever and a longer horizon.

## H5. The bottleneck moves downstream

Speeding up one step lengthens the queue at the next constrained step. By Little's law, more work in progress at a fixed capacity means longer waits.

- **Test:** If the change works, where does the work pile up next? Usually review, test, release, approval, or the decision-makers themselves.
- **If it breaks:** Add capacity at the next constraint before or alongside the speedup, or cap the inflow.

## H6. Compute the ceiling before promising gains

By Amdahl's law, speeding up one part of a process improves the whole only in proportion to that part's share of the total.

- **Test:** What share of end-to-end time does the targeted step take? If code generation is 15% of lead time, doubling its speed saves at most about 7.5%.
- **If it breaks:** Re-aim at the step that dominates elapsed time, usually wait states.

## H7. Own the shear

Boundaries between layers fail when nobody owns them.

- **Test:** For each shear the plan crosses, is there a named owner with authority on both sides, or a joint owner?
- **If it breaks:** Make shear ownership an explicit decision in the plan and a seat in the room. Staff-plus engineers, platform product managers, and value-stream managers are natural shear owners.

## H8. Compiled governance is fast and brittle

Policy-as-code makes controls run at pipeline speed and also freezes today's interpretation.

- **Test:** If the plan encodes a slow-layer rule into automation, is the rule's intent versioned and traceable, and who re-interprets it when the rule changes?
- **If it breaks:** Separate stable principles from volatile parameters. Version the parameters. Keep a human path for judgment calls.

## H9. Culture changes by embedding, not announcing

Edgar Schein's primary embedding mechanisms are: what leaders pay attention to, measure, and control; how leaders react to critical incidents; how leaders allocate resources; deliberate role modeling and coaching; how rewards and status are allocated; and how people are recruited, promoted, and removed. Structures, rituals, and statements are secondary and only reinforce.

- **Test:** Which primary mechanism does the plan change? A town hall, a values poster, or a training course on its own changes none of them.
- **If it breaks:** Tie the plan to a measurement change, an incident-response norm, a resource shift, or a promotion criterion.

## H10. Metrics are values

What gets measured is what leaders signal they care about (H9), and measured proxies get gamed (Goodhart's law).

- **Test:** What behavior would the plan's metrics reward if people optimized them literally? Adoption rate, pull-request count, and self-reported time saved all reward volume.
- **If it breaks:** Pair each output metric with a stability or outcome metric: change-failure rate, rework, time in review, outcome per release.

## H11. Respect nature

Human attention, working memory, review stamina, and skill formation are hard limits. So are compute cost and seasonal demand.

- **Test:** Does the plan increase load on any person or role? Does it remove the work through which juniors learn how the system works?
- **If it breaks:** Add caps, rotations, protected learning time, or explicit capacity. Name the comprehension-debt risk.

## H12. The frontier is weather

AI capability changes monthly and unpredictably.

- **Test:** Would the plan still work if the leading model or tool changed next quarter? Is it coupled to one vendor's specific capability?
- **If it breaks:** Put a replaceable joint between the frontier and the slow layers: a gateway, evaluation suites the organization owns, and contracts written against capabilities rather than products.

## H13. Make fast disposable

The fast layer's job is to be prolific, cheap, and mostly thrown away.

- **Test:** Does the plan try to make the fast layer reliable (heavy approvals for experiments, a high bar to try a tool)?
- **If it breaks:** Lower the cost of trying and raise the bar for promotion into slower layers (H3). Reliability belongs at the shear, not in the experiment.

## H14. The first incident teaches the culture

When the change produces its first visible failure, leadership's reaction will teach more than any announcement.

- **Test:** Has the plan decided in advance how leaders will respond to the first serious failure (for example, an AI-generated defect in production): blame the person, ban the tool, or fix the system that let it through?
- **If it breaks:** Write the intended response into the plan and get the decision-makers to agree to it in the room.
