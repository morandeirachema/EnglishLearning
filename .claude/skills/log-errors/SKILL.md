---
name: log-errors
description: Extract English errors from a pasted text or transcript (e.g. Pixel Recorder or Claude voice transcript) and append them to log/errors.csv. Use when the user pastes something they said or wrote and wants it corrected or logged.
---

1. Treat the input as the learner's own English. If it is a speech transcript, ignore likely transcription glitches and do not comment on pronunciation.
2. First list each error and ask the learner to try to self-correct, unless they asked for direct answers.
3. Append rows to `log/errors.csv`: `date,original,correction,category,l1_interference,explanation,source`. Use only the categories listed in `CLAUDE.md`. Quote fields containing commas. Explanation is 15 words or fewer. Afterwards run `python3 scripts/stats.py` and fix any WARNING rows.
4. Within one text, log a repeated error once and note the repeat in the explanation. If the same error was already logged on an earlier date, add a new row with the same `correction` wording as the old one: `scripts/stats.py` uses that to list it as REPEATED.
5. Finish with the top 3 recurring categories in the whole log, and point out any of today's errors that `stats.py` lists as REPEATED.
