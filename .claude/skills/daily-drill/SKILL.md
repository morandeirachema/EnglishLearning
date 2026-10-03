---
name: daily-drill
description: Generate a 10-minute interleaved English drill from the learner's most frequent errors in log/errors.csv, and optionally export Anki cards. Use when the user asks for a drill, practice, quiz, or daily exercise.
---

1. Read `log/errors.csv`. Count errors by category over the last 30 days (all time if fewer than 15 rows). If the log is empty, use the Spanish-speaker problem list in `research/learning-with-claude-and-apps.md` §6.
2. Build 10 items on the top 3 categories, interleaved (not grouped): gap-fill, sentence transformation, and error correction. Match the exam format in `CLAUDE.md` where possible.
3. Ask one item at a time and wait for the answer. If wrong, prompt self-correction once before giving the answer.
4. At the end, give the score and log new errors to `log/errors.csv`.
5. If the user asks for Anki cards, write `log/anki-YYYY-MM-DD.txt` for import into Anki on the Mac. Start the file with these header lines so Anki sets everything up automatically:
   ```
   #separator:Semicolon
   #html:true
   #notetype:Cloze
   #deck:English::Exam
   #tags column:3
   ```
   Then one card per line: `Text;Back Extra;Tags`. Text is a full sentence with the target as `{{c1::word}}`. Back Extra has the definition, two collocations and a Spanish gloss, separated by `<br>`. Tags are space-separated (e.g. `B2 error::article`). Quote any field containing a semicolon. Base cards on the learner's own errors.
6. Append one row to `log/study.csv` (`date,minutes,strand,activity`): strand `study`, activity `daily drill`. Use the real session length if known, otherwise 10.
