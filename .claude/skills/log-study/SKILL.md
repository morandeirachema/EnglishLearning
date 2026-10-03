---
name: log-study
description: Record study time in log/study.csv from a plain description of what the learner did (podcasts, Anki, tutor lessons, series, apps). Use when the user says how long they studied or practised, or asks to log study time.
---

1. Parse each activity and its minutes from the user's message. Dates default to today; accept "yesterday" or a weekday and convert to `YYYY-MM-DD`. If minutes are missing for an activity, ask rather than guess.
2. Assign one strand per activity (Nation's Four Strands, plus exam):
   - `input`: listening or reading for meaning (podcasts, series, YouTube, books, news).
   - `output`: speaking or writing for meaning (tutor conversation, Gemini Live or Claude voice chat, essays, messages).
   - `study`: deliberate language work (Anki, ELSA, grammar exercises, dictionary/collocation work).
   - `fluency`: easy, familiar material at speed (rereading, re-listening, repeating a talk faster, shadowing known scripts).
   - `exam`: timed practice under exam conditions (mock papers, official sample tests).
   A mixed activity goes under its main strand; split it into two rows only if the user gives separate times.
3. Append one row per activity: `date,minutes,strand,activity`. Keep `activity` short and without personal details (e.g. `tutor lesson`, not the tutor's name). Quote it if it contains a comma.
4. Run `python3 scripts/stats.py --days 7` and reply with one line: hours this week vs the ~7 h target and the weakest strand.
