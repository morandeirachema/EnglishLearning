---
name: weekly-review
description: Review the learner's week from log/errors.csv and log/study.csv, record it in log/progress.md, and plan next week. Use when the user asks for a weekly review, progress report, stats, or "what should I study next".
---

1. If the learner tells you what they studied this week, first append rows to `log/study.csv` (`date,minutes,strand,activity`; strand is one of input, output, study, fluency, exam).
2. Run `python3 scripts/stats.py` and read the output.
3. Report in a few lines: hours this week vs the ~6.5–7 h target, strand balance (aim for roughly a quarter each of input, output, study and fluency; add exam practice in the last 6–8 weeks), error categories going up or down, and percentage toward the next CEFR level (~200 h).
4. Append one row to `log/progress.md`: date, "weekly review", hours, top 3 error categories, one-line note.
5. Plan next week as a short table using the routine in `README.md`, shifting time toward the weakest strand and the top error categories. If the exam date in `CLAUDE.md` is 8 weeks away or less, include one full timed mock paper.
6. Every 3 months, remind the learner to retake EF SET and Speak & Improve and log the results.
