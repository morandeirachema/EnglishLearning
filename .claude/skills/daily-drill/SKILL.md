---
name: daily-drill
description: Generate a 10-minute interleaved English drill from the learner's most frequent errors in log/errors.csv, and optionally export Anki cards. Use when the user asks for a drill, practice, quiz, or daily exercise.
---

1. Read `log/errors.csv`. Count errors by category over the last 30 days (all time if fewer than 15 rows). If the log is empty, use the Spanish-speaker problem list in `research/learning-with-claude-and-apps.md` §6.
2. Build 10 items on the top 3 categories, interleaved (not grouped): gap-fill, sentence transformation, and error correction. Match the exam format in `CLAUDE.md` where possible.
3. Ask one item at a time and wait for the answer. If wrong, prompt self-correction once before giving the answer.
4. At the end, give the score and log new errors to `log/errors.csv`.
5. If the user asks for Anki cards, write `log/anki-YYYY-MM-DD.csv` (semicolon-separated: Text;Extra;Tags, cloze format `{{c1::...}}`) for import into Anki on the Mac.
