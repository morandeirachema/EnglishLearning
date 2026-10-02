#!/usr/bin/env python3
"""Summarise the error log and the study-hours log.

Usage:
    python3 scripts/stats.py            # full report
    python3 scripts/stats.py --days 30  # error window for "recent" (default 30)
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
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f) if any(r.values())]


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
    allc = Counter(r["category"].strip() or "?" for r in rows)
    recent = Counter(r["category"].strip() for r in rows if (d := parse_date(r["date"])) and d >= recent_start)
    prev = Counter(r["category"].strip() for r in rows if (d := parse_date(r["date"])) and prev_start <= d < recent_start)
    print(f"  {'category':<14}{'all':>5}{f'last {days}d':>10}{'before':>8}  trend")
    for cat, n in allc.most_common():
        r, p = recent[cat], prev[cat]
        trend = "new" if p == 0 and r else ("down" if r < p else "up" if r > p else "flat")
        print(f"  {cat:<14}{n:>5}{r:>10}{p:>8}  {trend}")
    l1 = sum(1 for r in rows if r.get("l1_interference", "").strip().lower() == "yes")
    print(f"  Spanish-interference errors: {l1}/{len(rows)}")
    top = [c for c, _ in (recent or allc).most_common(3)]
    print(f"  Focus next drills on: {', '.join(top)}\n")


def study_report(rows):
    print(f"STUDY TIME  ({len(rows)} sessions)")
    if not rows:
        print("  none yet. Add rows to log/study.csv: date,minutes,strand,activity\n")
        return
    mins = Counter()
    for r in rows:
        try:
            mins[r["strand"].strip()] += int(r["minutes"])
        except ValueError:
            continue
    total = sum(mins.values())
    for s in STRANDS + sorted(set(mins) - set(STRANDS)):
        if mins[s]:
            print(f"  {s:<8}{mins[s] / 60:6.1f} h  {mins[s] * 100 // total:3d}%  {bar(mins[s], total)}")
    week_start = date.today() - timedelta(days=6)
    week = sum(int(r["minutes"]) for r in rows if (d := parse_date(r["date"])) and d >= week_start and r["minutes"].strip().isdigit())
    hours = total / 60
    print(f"  Total {hours:.1f} h | last 7 days {week / 60:.1f} h (target ~6.5 h)")
    print(f"  Progress toward next CEFR level (~{HOURS_PER_LEVEL} h): {hours * 100 / HOURS_PER_LEVEL:.0f}%\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    args = ap.parse_args()
    error_report(read(ERRORS), args.days)
    study_report(read(STUDY))


if __name__ == "__main__":
    main()
