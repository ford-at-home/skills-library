---
name: demo-production
description: Use when building a scripted terminal-UI demo program whose output is entirely fixtures (no live backend) and which must serve three consumers at once — a human driving it live, a screen recorder driving a real PTY, and CI running it headless. Covers the runtime contracts that program must satisfy — a fast mode that stays deterministic, replay-safe beats, exit-code-only smoke testing, and a disclosure block. Not about the recorder, tape files, or output encoding.
---

# Demo production: the program-side contracts

A fixture-backed demo is a program that lies convincingly about a system it is
not connected to. That is legitimate — a live backend on stage is a liability —
but it puts the whole burden of trustworthiness on the program.

This skill is about the demo binary, not the recorder. The recorder is dumb: it
opens a PTY, types a command, sleeps, captures frames. Everything that goes
wrong in a way you will not notice lives in the program, and **every failure
below is silent.** The demo still runs and the recording still looks right; what
breaks is determinism, or honesty, and neither one raises an error.

## Shape: beats, not a script

Model the demo as a list of **beats**. A beat is one discrete dramatic unit:
`durationMs` (how long to hold before advancing) and `apply()` (fired once when
the beat starts). A runner walks the list on a single timer and exposes pause,
play, step one beat, fast-forward the rest of the act, replay from zero.

```ts
interface Beat {
  durationMs: number;
  apply: () => void;
}
```

Worth the indirection for one reason: it puts every timer behind a single
multiplier. Nothing below works if sleeps are scattered through component code.

## 1. A fast mode is only useful if it is also deterministic

Two settings, and the interaction between them is the point. A **speed
multiplier** scales every beat's `durationMs` — a representative pair is `2.2`
for a live or recorded run (authored durations are deliberately stretched) and
`0.04` under `--fast`, collapsing a ~140s walkthrough to under 5s. **Pacing
jitter** then multiplies each dwell by a random ±15%, because uniform holds read
as a metronome and look synthetic on video.

The non-obvious part: **jitter must be suppressed in fast mode**, gated on the
multiplier rather than on the flag, so any caller that dials the speed down for
its own reasons gets determinism without knowing the flag exists.

```ts
const JITTER_PCT = 0.15;
const jitter = speedMultiplier > 0.05
  ? 1 + (Math.random() * 2 - 1) * JITTER_PCT
  : 1;
const dwell = Math.max(1, Math.round(beat.durationMs * speedMultiplier * jitter));
```

Collapse any per-character reveal or typewriter effect below the same threshold
too — emit text fully revealed instead of animating it.

**The failure it prevents:** a jittered fast run varies in wall-clock length
between invocations. A ~1.8s collapsed run drifts by a few hundred milliseconds,
enough that a CI timeout tuned to the observed duration fails once a week for no
reason anyone can reproduce locally. Nothing is logged, and it works every time
you try it by hand.

**Trap:** the threshold gets defined twice — once in the runner, once in
whatever module animates text reveal — with the flag's value (`0.04`) set in a
third place. Define the threshold and the fast value once and import both.

**Second-order:** authored `durationMs` values are not real milliseconds; real
time is their sum times the multiplier. Budget a recorder's capture window from
the multiplier, not by summing the beat list, or the capture cuts off mid-scene.

## 2. Assert the exit code. Do not parse the output.

The CI smoke test should run the demo end-to-end in fast mode under a wall clock
and check exactly three things — and nothing about the content of stdout:

- the process exited `0`
- it was not killed by a signal (a timeout kill is a distinct failure)
- stdout was non-empty (byte count only — proof it rendered at all)

This looks like weak testing and is a deliberate call: **a terminal UI's bytes
are not a stable test surface.** The stream is full-screen redraws interleaved
with cursor-positioning and color escapes; it changes when a layout box gets one
column wider, when the palette is retuned, when the renderer's diffing changes
between minor versions. None of those are regressions; all of them break a
content assertion.

**The failure it prevents:** not an escaped bug — an abandoned test. A smoke
test that fails on every cosmetic edit gets marked skipped within two weeks, and
then nothing catches the crash-on-launch that the exit code would have caught
for free. Weak-but-durable beats strict-but-ignored.

The exit code still covers most of what actually breaks: a throw during mount,
an unhandled rejection, a hang, a beat list that never completes. Keep the
timeout well above the fast-mode budget (10s for a sub-5s run) — it is a hang
detector, not a benchmark.

## 3. `apply()` must be safe to call again

Fast-forward loops the remaining `apply()` calls immediately so side effects
accumulate as if the act had played; replay resets the index to zero and plays
forward again. During a live demo someone will press fast-forward and then
replay, in that order. So every `apply()` must tolerate re-entry:

**Absolute writes, never relative ones.** `setStep(i, 'done')` and
`setShowPayoff(true)` are safe at any multiplicity; `count => count + 1` is not.
This rules out counters and toggles inside beats — derive displayed numbers from
the beat index or from a value that is assigned outright.

**A cursor in a ref, bounds-checked.** For a beat that emits the next scripted
line, hold the position in a mutable ref rather than reactive state (where a
re-render re-runs the beat and duplicates the emission) and no-op past the end:

```ts
const cursor = useRef(0);
const emitNext = () => {
  const entry = lines[cursor.current];
  if (!entry) return;          // past the end: no-op, do not throw, do not wrap
  cursor.current += 1;
  emit(entry);
};
```

**The failure it prevents:** duplicated log lines, double-counted totals, a
progress list that reads 7/5 — surfacing only in the fast-forward-then-replay
path, which no test exercises and which you will hit for the first time in front
of an audience.

Also wrap `apply()` in try/catch inside the runner and log to stderr: a demo
should not crash mid-scene over one bad beat, and stderr keeps the trace off the
canvas the recorder is capturing.

## 4. Ship a "what this is not" block, in two places

State plainly, in the README **and** repeated in `--help`, what the demo is not
connected to. Enumerate rather than summarize:

> **What this is not.** A real instance. A connection to any cloud provider. A
> connection to anything. There are no network calls, no cloud SDK calls, no
> model/LLM calls, no credentials used, no files written. Every line of output
> is a hardcoded fixture; every transition is a local timer. Nothing on screen
> reflects real system state.

The itemization is the mechanism. "This is a demo" is compatible with a viewer
believing there is a real backend behind it; "no credentials used, no files
written" is not. Name each capability a reasonable person might assume. It goes
in `--help` because that is what a colleague who finds the binary on their
`PATH` six months from now will read; the README is for whoever was pointed at
the repo.

**The failure it prevents:** the honest-mistake demo. Someone clips your
recording into a deck, a stakeholder reads it as a live system, and a commitment
gets made against capability that does not exist — with you not in the room. It
also stops a fixture demo from becoming the thing everyone believes is tested.

## 5. Branch on the TTY, not on a flag

The same binary serves three consumers, and only one of them can type: a live
operator on a TTY (full pace, prompts, keyboard control); the recorder, also on
a real PTY, typing actual keystrokes — so a scripted-input mode is unnecessary
and would only add an untested second code path; and CI with no TTY, which must
never block on input. Key the degradation off `stdin.isTTY`, not off an env var
someone has to remember:

```ts
const skipPrompt = args.fast || !process.stdin.isTTY || args.team !== undefined;
const exitOnComplete = args.fast || args.singleAct;
```

**The failure it prevents:** a hang in CI that reads as a timeout, on an
interactive prompt nobody remembers is there. The reverse also matters — exiting
immediately on the last beat truncates the final frame in the recording, so end
the beat list with a short trailing dwell before teardown.

Expose per-scene entry (`--act N`) that exits when that scene ends. Re-shooting
one 30s scene should not mean re-running a 140s movie.

## Checklist

- [ ] Every timer routes through one multiplier
- [ ] Jitter and character-reveal suppressed below the fast threshold
- [ ] Fast threshold and fast value defined in one place
- [ ] Smoke test asserts exit code, signal, non-empty stdout — nothing else
- [ ] No relative-increment state inside `apply()`
- [ ] Script cursors in refs, bounds-checked, no-op past the end
- [ ] `apply()` wrapped in try/catch, errors to stderr
- [ ] "What this is not" in README and `--help`, itemized
- [ ] Runs to a clean exit with no TTY
- [ ] Trailing dwell before teardown
- [ ] Per-scene entry point
