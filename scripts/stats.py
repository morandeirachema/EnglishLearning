#!/usr/bin/env python3
"""Summarise the error log and the study-hours log.

Usage:
    python3 scripts/stats.py                     # full report
    python3 scripts/stats.py --days 30           # error window for "recent" (default 30)
    python3 scripts/stats.py --since 2026-10-05  # count level progress from this date (last level check)
"""
import argparse
import csv
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ERRORS = ROOT / "log" / "errors.csv"
STUDY = ROOT / "log" / "study.csv"
# Nation's Four Strands: aim for roughly a quarter each. "exam" is mock/timed practice.
STRANDS = ["input", "output", "study", "fluency", "exam"]
HOURS_PER_LEVEL = 200  # Cambridge guided-learning-hours estimate per CEFR level


def read(path):
    """Return (rows, problems). Missing fields become "", blank rows are skipped,
    rows with the wrong number of fields are reported and left out."""
    if not path.exists():
        return [], []
    rows, problems = [], []
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        width = len(reader.fieldnames or [])
        for line_no, raw in enumerate(reader, start=2):
            extra = raw.pop(None, None)
            row = {k: (v or "").strip() for k, v in raw.items()}
            if not any(row.values()) and not extra:
                continue
            filled = sum(1 for v in raw.values() if v is not None)
            if extra or filled < width:
                got = filled + len(extra or [])
                problems.append(f"{path.name} line {line_no}: {got} fields, expected {width} (quote fields that contain commas)")
                continue
            rows.append(row)
    return rows, problems


def minutes(row):
    try:
        return max(0, round(float(row["minutes"])))
    except ValueError:
        return None


def parse_date(s):
    try:
        return date.fromisoformat((s or "").strip())
    except ValueError:
        return None


def bar(n, total, width=20):
    return "#" * round(width * n / total) if total else ""


def error_report(rows, days):
    print(f"ERRORS  ({len(rows)} logged)")
    if not rows:
        print("  none yet. Use /log-errors or /mark-essay.\n")
        return
    today = date.today()
    recent_start = today - timedelta(days=days)
    prev_start = recent_start - timedelta(days=days)
    allc = Counter(r["category"] or "?" for r in rows)
    recent = Counter(r["category"] or "?" for r in rows if (d := parse_date(r["date"])) and d >= recent_start)
    prev = Counter(r["category"] or "?" for r in rows if (d := parse_date(r["date"])) and prev_start <= d < recent_start)
    print(f"  {'category':<14}{'all':>5}{f'last {days}d':>10}{'before':>8}  trend")
    for cat, n in allc.most_common():
        r, p = recent[cat], prev[cat]
        trend = "new" if p == 0 and r else ("down" if r < p else "up" if r > p else "flat")
        print(f"  {cat:<14}{n:>5}{r:>10}{p:>8}  {trend}")
    l1 = sum(1 for r in rows if r.get("l1_interference", "").lower() == "yes")
    print(f"  Spanish-interference errors: {l1}/{len(rows)}")
    top = [c for c, _ in (recent or allc).most_common(3)]
    print(f"  Focus next drills on: {', '.join(top)}\n")


def study_report(rows, since):
    print(f"STUDY TIME  ({len(rows)} sessions)")
    if not rows:
        print("  none yet. Add rows to log/study.csv: date,minutes,strand,activity\n")
        return
    mins = Counter()
    bad = 0
    for r in rows:
        m = minutes(r)
        if m is None:
            bad += 1
            continue
        mins[r["strand"] or "?"] += m
    total = sum(mins.values())
    for s in STRANDS + sorted(set(mins) - set(STRANDS)):
        if mins[s]:
            print(f"  {s:<8}{mins[s] / 60:6.1f} h  {mins[s] * 100 // total:3d}%  {bar(mins[s], total)}")
    if bad:
        print(f"  ({bad} row(s) skipped: minutes is not a number)")
    week_start = date.today() - timedelta(days=6)
    week = sum(minutes(r) or 0 for r in rows if (d := parse_date(r["date"])) and d >= week_start)
    print(f"  Total {total / 60:.1f} h | last 7 days {week / 60:.1f} h (target ~7 h)")
    level_mins = sum(minutes(r) or 0 for r in rows if since is None or ((d := parse_date(r["date"])) and d >= since))
    pct = level_mins / 60 * 100 / HOURS_PER_LEVEL
    label = f"since {since}" if since else "all time (pass --since <last level check date>)"
    print(f"  Toward next CEFR level, {label}: {level_mins / 60:.1f} of ~{HOURS_PER_LEVEL} h ({pct:.0f}%)")
    if pct >= 100:
        print("  -> ~200 h reached: take a level test (EF SET, Speak & Improve) and run /set-goal")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--since", type=date.fromisoformat, default=None, help="YYYY-MM-DD of your last level check")
    args = ap.parse_args()
    errors, p1 = read(ERRORS)
    study, p2 = read(STUDY)
    error_report(errors, args.days)
    study_report(study, args.since)
    for msg in p1 + p2:
        print(f"WARNING {msg}")


if __name__ == "__main__":
    main()
