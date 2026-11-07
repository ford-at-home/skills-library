# How a behavioral benchmark goes wrong

**The one it exists to catch.** A ranking gets published, a vendor asks how their
model was prompted, and nobody can produce the exact input. Without a pinned
manifest and retained raw artifacts the benchmark cannot answer the first
question anyone asks about it.

**Declared depth the harness never reaches.** The config says five turns, the
runner accepts `max_turns=5`, and the dialogue loop breaks after the first
response because no simulated follow-up was supplied. The stored data has one
turn per unit. Everything downstream — turn-decay metrics, "at which turn does
the behavior degrade" — is computed over a single point and reports a value
anyway. Count turns in the artifact, not in the config.

**Expected scores in the run config.** Each candidate entry carries an
`expected_score` field next to its identifier. Nothing forces confirmation bias
faster than a prior sitting in the file you consult when a result looks wrong.
Priors belong in the analysis, after the run.

**The config's description of itself is not the config.** In the source project:
a file named for 24 models holding 26; a change log recording the addition of a
model identifier that appears nowhere in the candidate list, because the entry
that shipped has a different id; eight scenarios defined in code of which the
production config runs two, with no record of why the other six went. Each is
harmless until someone reasons from the description instead of the list — and
the last one means the published behavior claim is far narrower than the rubric
implies.

**Errors as zeros, then a magic filter.** Failed judgements stored as 0.0 enter
the mean. Someone adds `if score < 0.01: skip` to fix the visible symptom. That
filter also drops genuine near-zero scores, so every published mean improves by
an unrecorded amount and the failure rate becomes invisible.

**Recomputed composites.** In the source codebase a read endpoint recomputes
`overall` as the unweighted mean of three display-scale fields, which is not the
weighted penalty composite the judge stored. Two different numbers named
`overall` are served from one deployment, and whichever a reader hits looks
authoritative. This gets reintroduced by whoever next writes an aggregate
endpoint, because recomputing from parts feels more transparent than reading a
stored number.

**A fallback config that has never run.** The planner falls back to a hardcoded
default when the config object is missing. That default's scenario entries are
strings, while the code that consumes it reads `scenario["id"]` — so the fallback
path cannot execute. A fallback that has never run is not a safety net; it is an
untested branch that fires on your worst day. Fail loudly instead.

**Stale diagnostics.** The tooling written to sanity-check the judge outlives the
rubric. In the source project, the in-repo judge-inspection script still reports
on five rubric fields that were removed and a 0-100 scale that was replaced —
so it prints a clean report about data that no longer exists. When the rubric
changes, the diagnostics change in the same commit.
