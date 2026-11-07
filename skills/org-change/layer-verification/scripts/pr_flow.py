#!/usr/bin/env python3
"""Measure review flow from GitHub pull-request history.

Read-only. Standard library only. Reads the JSON produced by:

    gh pr list --state merged --limit 500 \
      --json number,createdAt,mergedAt,additions,deletions,changedFiles,author,reviews \
      > prs.json

Usage:
    python3 pr_flow.py prs.json [--weeks 12] [--large 400]
    gh pr list ... | python3 pr_flow.py -

Reports time to first review, time to merge, change size, the share of
changes merged without review by anyone other than the author, reviewer
concentration, and a weekly trend. Output is Markdown.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def percentile(values: list[float], pct: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    rank = (len(ordered) - 1) * pct / 100
    low = int(rank)
    high = min(low + 1, len(ordered) - 1)
    return ordered[low] + (ordered[high] - ordered[low]) * (rank - low)


def fmt_hours(hours: float | None) -> str:
    if hours is None:
        return "n/a"
    if hours < 48:
        return f"{hours:.1f} h"
    return f"{hours / 24:.1f} d"


def fmt_num(value: float | None) -> str:
    return "n/a" if value is None else f"{value:,.0f}"


def login(person: dict | None) -> str | None:
    if not person:
        return None
    return person.get("login") or person.get("name")


def analyze(prs: list[dict], weeks: int, large: int) -> str:
    rows = []
    reviewer_counts: Counter[str] = Counter()

    for pr in prs:
        created = parse_time(pr.get("createdAt"))
        merged = parse_time(pr.get("mergedAt"))
        if not created or not merged:
            continue
        author = login(pr.get("author"))
        size = (pr.get("additions") or 0) + (pr.get("deletions") or 0)

        independent_times = []
        for review in pr.get("reviews") or []:
            reviewer = login(review.get("author"))
            submitted = parse_time(review.get("submittedAt"))
            if reviewer and reviewer != author:
                reviewer_counts[reviewer] += 1
                if submitted:
                    independent_times.append(submitted)

        first_review = min(independent_times) if independent_times else None
        rows.append(
            {
                "created": created,
                "merged": merged,
                "size": size,
                "files": pr.get("changedFiles") or 0,
                "hours_to_merge": (merged - created).total_seconds() / 3600,
                "hours_to_first_review": (
                    (first_review - created).total_seconds() / 3600 if first_review else None
                ),
                "reviewed": bool(independent_times),
            }
        )

    if not rows:
        return "No merged pull requests with timestamps were found in the input."

    rows.sort(key=lambda r: r["merged"])
    to_merge = [r["hours_to_merge"] for r in rows]
    to_review = [r["hours_to_first_review"] for r in rows if r["hours_to_first_review"] is not None]
    sizes = [float(r["size"]) for r in rows]
    unreviewed = sum(1 for r in rows if not r["reviewed"])
    large_count = sum(1 for r in rows if r["size"] > large)

    out = []
    out.append("# Review flow")
    out.append("")
    out.append(
        f"{len(rows)} merged pull requests, "
        f"{rows[0]['merged']:%Y-%m-%d} to {rows[-1]['merged']:%Y-%m-%d}."
    )
    out.append("")
    out.append("| Measure | Median | 75th pct | 90th pct |")
    out.append("|---|---|---|---|")
    out.append(
        f"| Time to first independent review | {fmt_hours(percentile(to_review, 50))} "
        f"| {fmt_hours(percentile(to_review, 75))} | {fmt_hours(percentile(to_review, 90))} |"
    )
    out.append(
        f"| Time to merge | {fmt_hours(percentile(to_merge, 50))} "
        f"| {fmt_hours(percentile(to_merge, 75))} | {fmt_hours(percentile(to_merge, 90))} |"
    )
    out.append(
        f"| Change size (lines added + deleted) | {fmt_num(percentile(sizes, 50))} "
        f"| {fmt_num(percentile(sizes, 75))} | {fmt_num(percentile(sizes, 90))} |"
    )
    out.append("")
    out.append(
        f"- Merged with no review from anyone other than the author: "
        f"**{unreviewed / len(rows):.0%}** ({unreviewed} of {len(rows)})"
    )
    out.append(f"- Changes larger than {large} lines: **{large_count / len(rows):.0%}** ({large_count})")

    total_reviews = sum(reviewer_counts.values())
    if total_reviews:
        ranked = reviewer_counts.most_common()
        top_n = max(1, round(len(ranked) * 0.1))
        top_share = sum(c for _, c in ranked[:top_n]) / total_reviews
        top3_share = sum(c for _, c in ranked[:3]) / total_reviews
        out.append(
            f"- Reviewers: {len(ranked)} people gave {total_reviews} independent reviews. "
            f"The top 10% ({top_n}) gave **{top_share:.0%}**; the top 3 gave **{top3_share:.0%}**."
        )
    else:
        out.append("- No independent reviews found. Check that the `reviews` field was requested.")

    # Weekly trend
    end = rows[-1]["merged"]
    start = end - timedelta(weeks=weeks)
    buckets: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        if r["merged"] < start:
            continue
        year, week, _ = r["merged"].isocalendar()
        buckets[f"{year}-W{week:02d}"].append(r)

    if buckets:
        out.append("")
        out.append(f"## Weekly trend (last {weeks} weeks; the first and last weeks may be partial)")
        out.append("")
        out.append("| Week | Merged | Median size | Median time to merge | Unreviewed |")
        out.append("|---|---|---|---|---|")
        for key in sorted(buckets):
            week_rows = buckets[key]
            med_size = statistics.median(r["size"] for r in week_rows)
            med_merge = statistics.median(r["hours_to_merge"] for r in week_rows)
            unrev = sum(1 for r in week_rows if not r["reviewed"]) / len(week_rows)
            out.append(
                f"| {key} | {len(week_rows)} | {med_size:,.0f} | {fmt_hours(med_merge)} | {unrev:.0%} |"
            )

    out.append("")
    out.append("## How to read this")
    out.append("")
    out.append(
        "- Volume rising while time to merge rises: a capacity limit at review (Little's law). "
        "More generation will lengthen the queue."
    )
    out.append("- Size rising: batch size is growing; reviews get slower and less accurate.")
    out.append("- Unreviewed share rising: the boundary is failing open; treat it as a tripwire.")
    out.append("- High top-reviewer share: review depends on a few people's attention.")
    out.append(
        "- Caveats: merged changes only (abandoned work is invisible); bots count as reviewers "
        "unless filtered; time includes nights and weekends."
    )
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", help="Path to the gh JSON output, or - for stdin")
    parser.add_argument("--weeks", type=int, default=12, help="Weeks to show in the trend (default 12)")
    parser.add_argument("--large", type=int, default=400, help="Line threshold for a large change (default 400)")
    args = parser.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    try:
        prs = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"Could not parse JSON input: {exc}", file=sys.stderr)
        return 1
    if not isinstance(prs, list):
        print("Expected a JSON array of pull requests.", file=sys.stderr)
        return 1

    print(analyze(prs, args.weeks, args.large))
    return 0


if __name__ == "__main__":
    sys.exit(main())
