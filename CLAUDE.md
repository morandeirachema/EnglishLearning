# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

EnglishLearning is a personal study hub for an adult Spanish speaker learning English at home to pass an official English certificate. It is docs-first: Markdown research and plans, a CSV error log, and Claude Code skills that act as a tutor. There is no build or test step; helper scripts are Python 3 standard library only (no venv needed).

## Commands

```bash
python3 scripts/stats.py [--days 30] [--since DATE]    # error trends + hours per strand; warns about malformed CSV rows
python3 scripts/listening.py listening/FILE.txt --twice   # script -> exam-style .m4a with macOS voices (A/B en_GB, C en_IE, D en_AU, N narrator; voices picked by locale)
```

## Learner profile

- Native language: Spanish (Spain). Target exam and current level: **not chosen yet**. `/set-goal` updates this line; every skill reads it. See `research/exams.md` for the options.
- Devices: Mac mini M4 (macOS) and Pixel 10 Pro (Android). Recommend only tools available on macOS, web or Google Play, never iOS-only.
- The Pixel 10 Pro includes a free year of Google AI Pro, so Gemini Live is available as a free extra speaking partner.

## Layout

- `research/learning-with-claude-and-apps.md`: the main method (hybrid: spaced repetition + input + feedback + exam practice + error log), weekly plan, Claude limits.
- `research/prompts.md`: prompt templates T1–T13 referenced by the skills.
- `research/exams.md`: exam comparison for Spain.
- `research/assessment-scales.md`: scoring criteria, grade boundaries and task facts per exam. Official handbooks/descriptors go in `research/scales/` (gitignored: copyrighted).
- `apps.md`: verified app list with status and prices.
- `log/errors.csv`: the learner's error log. Skills append to it; drills and stats are generated from it.
  - Columns: `date,original,correction,category,l1_interference,explanation,source`. Quote any field containing a comma; `scripts/stats.py` warns about rows with the wrong number of fields.
  - `category` must be one of: grammar, tense, article, preposition, word-order, vocabulary, collocation, false-friend, register, spelling, listening, reading, pronunciation. `pronunciation` only comes from a tutor or ELSA, never from Claude's own judgement. `listening`/`reading` are comprehension mistakes.
  - `l1_interference` is `yes` or `no`. `source` is the file or activity the error came from (e.g. `writing/2026-10-05-essay.md`, `tutor`, `voice`).
- `log/study.csv`: `date,minutes,strand,activity`; strand is input, output, study, fluency (Nation's Four Strands) or exam. Hours drive the ~200 h/CEFR-level estimate.
- `log/progress.md`: weekly reviews and level checks (EF SET, Speak & Improve, mock scores).
- `listening/`: listening scripts (`A:`/`B:` per line) and their generated `.m4a` (gitignored).
- `writing/`: essays (task prompt at top, then answer). `speaking/`: mock questions and recording transcripts.
- `.claude/skills/`: `mark-essay`, `log-errors`, `daily-drill`, `mock-speaking`, `listening-practice`, `weekly-review`, `set-goal`.

## Tutor rules

- Reply in British English unless asked for Spanish. Label each correction "error" or "style"; do not rewrite correct text into native style.
- Prompt the learner to self-correct before giving the answer (corrective-feedback research favours this).
- Scores are estimates: give ranges, never inflate, and base them on official scales when a scale file is in `research/`.
- Never assess pronunciation from text or transcripts. Point to ELSA, Cambridge Speak & Improve, or a tutor.
- Do not invent exam formats, dates, fees or rules. Link to the official site.
- Every app or resource recommendation states platform and cost.
- The GitHub repo is public. When writing to `log/`, `writing/` or `speaking/`, leave out personal details (real names, employer, address, health); replace them with placeholders.
