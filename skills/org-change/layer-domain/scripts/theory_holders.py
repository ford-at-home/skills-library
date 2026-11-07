#!/usr/bin/env python3
"""Find where knowledge of a codebase is concentrated, from git history.

Read-only: runs `git log` and nothing else. Standard library only.

Usage:
    python3 theory_holders.py --repo . [--months 18] [--depth 2] [--top 25]

For each directory (at the chosen depth) it reports commit count, distinct
authors, the top author's share of commits, how many authors account for more
than half of the commits, and the most recent commit date. It flags:

    CONCENTRATED  one author made 70% or more of the commits
    BUS-1         a single author accounts for more than half of the commits
    QUIET         nobody has committed in the last 90 days of the window

Use the output to find subject-matter experts for the room and to spot
key-person risk. Output is Markdown.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date, timedelta


def git_log(repo: str, months: int) -> str:
    since = (date.today() - timedelta(days=int(months * 30.4))).isoformat()
    cmd = [
        "git", "-C", repo, "log", f"--since={since}", "--no-merges",
        "--format=@@%an|%ad", "--date=short", "--name-only",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise SystemExit(f"git log failed: {result.stderr.strip()}")
    return result.stdout


def bucket(path: str, depth: int) -> str:
    parts = path.split("/")
    if len(parts) <= depth:
        # A file at or above the chosen depth belongs to its parent directory.
        return "/".join(parts[:-1]) or "(root)"
    return "/".join(parts[:depth])


def analyze(log: str, depth: int, top: int) -> str:
    commits: dict[str, Counter[str]] = defaultdict(Counter)
    last_seen: dict[str, str] = {}
    author = day = None
    seen_in_commit: set[str] = set()

    for line in log.splitlines():
        if line.startswith("@@"):
            author, _, day = line[2:].partition("|")
            seen_in_commit = set()
            continue
        path = line.strip()
        if not path or author is None:
            continue
        key = bucket(path, depth)
        if key in seen_in_commit:
            continue
        seen_in_commit.add(key)
        commits[key][author] += 1
        if day and (key not in last_seen or day > last_seen[key]):
            last_seen[key] = day

    if not commits:
        return "No commits found in the window."

    quiet_cutoff = (date.today() - timedelta(days=90)).isoformat()
    ranked = sorted(commits.items(), key=lambda kv: sum(kv[1].values()), reverse=True)[:top]

    out = ["# Knowledge concentration", ""]
    out.append("| Directory | Commits | Authors | Top author share | Authors for >50% | Last commit | Flags |")
    out.append("|---|---|---|---|---|---|---|")
    holders: dict[str, str] = {}

    for key, counter in ranked:
        total = sum(counter.values())
        ordered = counter.most_common()
        top_author, top_count = ordered[0]
        share = top_count / total
        running, needed = 0, 0
        for _, count in ordered:
            running += count
            needed += 1
            if running > total / 2:
                break
        flags = []
        if share >= 0.7:
            flags.append("CONCENTRATED")
        if needed == 1:
            flags.append("BUS-1")
        if last_seen.get(key, "") < quiet_cutoff:
            flags.append("QUIET")
        holders[key] = ", ".join(name for name, _ in ordered[:3])
        out.append(
            f"| `{key}` | {total} | {len(counter)} | {share:.0%} | {needed} "
            f"| {last_seen.get(key, 'n/a')} | {' '.join(flags) or '-'} |"
        )

    out.append("")
    out.append("## Most active contributors by area (candidate subject-matter experts)")
    out.append("")
    for key, names in holders.items():
        out.append(f"- `{key}`: {names}")

    out.append("")
    out.append("## How to read this")
    out.append("")
    out.append("- CONCENTRATED or BUS-1 on a critical area: key-person risk and a limit on verification capacity.")
    out.append("- QUIET on a critical area: the people who knew it may have moved on. Ask who still holds the theory.")
    out.append(
        "- Commit counts measure activity, not understanding. Confirm with the user who can actually "
        "explain each area. In the brief, record roles rather than names unless the user chooses otherwise."
    )
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", default=".", help="Path to the git repository (default: current directory)")
    parser.add_argument("--months", type=int, default=18, help="History window in months (default 18)")
    parser.add_argument("--depth", type=int, default=2, help="Directory depth to group by (default 2)")
    parser.add_argument("--top", type=int, default=25, help="Number of directories to show (default 25)")
    args = parser.parse_args()
    print(analyze(git_log(args.repo, args.months), args.depth, args.top))
    return 0


if __name__ == "__main__":
    sys.exit(main())
