---
name: mark-essay
description: Mark an English exam essay in writing/ against the learner's target exam scales, then append its errors to log/errors.csv. Use when the user asks to mark, correct, grade or review an essay or writing task.
---

1. Read the essay file the user names (default: newest file in `writing/`). The file should start with the task prompt, then the answer.
2. Read `CLAUDE.md` for the target exam and level. If an official assessment-scale file exists in `research/`, score against it; otherwise say the score is an estimate from general knowledge of the scales.
3. Report per criterion: estimated score (as a range if unsure), the evidence from the text, and the descriptor wording that justifies it. Never score above the evidence.
4. Error table: quote | correction | category | error or style. Correct only genuine errors; do not rewrite the essay.
5. Give the 2 changes that would raise the score most.
6. Append each genuine error to `log/errors.csv` with today's date and `source` = the essay file name. Use the categories from `research/prompts.md` T3.
7. Suggest the learner also submits it to Cambridge Write & Improve for a second opinion.
