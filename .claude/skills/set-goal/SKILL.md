---
name: set-goal
description: Record or update the learner's target exam, exam date, current level and placement-test results in CLAUDE.md and log/progress.md. Use when the user says which exam they chose, gives a test result or level, or changes their exam date.
---

1. Collect from the user's message: target exam (exact name, e.g. "Cambridge C1 Advanced"), exam date or target month, current level and the evidence (EF SET score, Cambridge "Test your English" result, Speak & Improve / Write & Improve level). Do not guess missing values; write "not set".
2. In `CLAUDE.md`, replace the line under "Learner profile" that starts with `- Native language:` so it reads:
   `- Native language: Spanish (Spain). Target exam: <exam>. Exam date: <date>. Current level: <level> (<evidence>, <today>).`
3. Append one row per test result to the table in `log/progress.md` (columns Date | Check | Result | Notes), e.g. `| 2026-10-05 | EF SET | 58/100 (B2) | baseline |`.
4. Using `research/learning-with-claude-and-apps.md` (§2: ~200 hours per CEFR level), say how many weeks the gap needs at the learner's weekly hours, and whether the exam date is realistic. If it is not, suggest a later date or a multilevel exam from `research/exams.md`.
5. If the exam is not Cambridge or IELTS, remind the learner to download its official scales into `research/scales/` (see `research/assessment-scales.md`).
