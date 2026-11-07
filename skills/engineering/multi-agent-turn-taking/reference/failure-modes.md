# How this goes wrong

**The stubbed state loader.** The gate is written, ordered, and correct. The
function that loads conversation state returns a newly constructed empty object on
every call. Cooldown and per-period counters are always zero, rules 3 and 4 never
fire, and nothing in the logs distinguishes "no violation" from "no state." This is
the failure this skill exists to catch. Test the gate by asserting a block, not by
asserting that a decision was reached.

**Two replicas, two counters.** Counters held as instance attributes, service
configured for one task but permitted to scale to two. At the cap of ten turns per
hour per participant, the observed rate is twenty, and every prompt can draw two
answers. Nothing in the gate is wrong.

**Ping-pong.** Two participants each carry a large "when addressed directly"
modifier. Cooldown and self-reply rules both permit alternation. Only rule 2 stops
it, and rule 2 is the hardest of them to implement because it needs to know who
was addressed and whether anyone has answered.

**Domination.** The participant with the highest base rate and the most matching
modifiers wins nearly every contested turn. A quietest-participant modifier and a
dominant-speaker penalty are the counterweights; both need the transcript window,
not just the last turn.

**The arbiter agrees.** Asked "should you reply here?", a model says yes, most of
the time, for most participants. This is why the weight is capped, why the arbiter
sees only survivors, and why its output is a scalar rather than a verdict. If the
arbiter's opinion changes more than a third of decisions, the deterministic score
is doing no work.

**Local-time arithmetic.** Quiet hours computed by subtracting a fixed offset from
UTC hours is wrong for half the year in any zone with daylight saving, and the
symptom is an hour of unexplained silence or noise at the boundary. Use a timezone
library, and treat quiet hours as a numbered blocking rule.

**Backoff as a cliff.** A participant that hits its cap and then enters a full-hour
backoff goes from present to absent instantly. If the conversation should degrade
rather than stop, taper the score as the budget depletes and keep the cap as the
hard stop.
