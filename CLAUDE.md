# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

EnglishLearning is a personal study hub for an adult Spanish speaker learning English at home to pass an official English certificate. It is docs-first: Markdown research and plans, a CSV error log, and Claude Code skills that act as a tutor. There is no build, test or lint step.

## Learner profile

- Native language: Spanish (Spain). Target exam and current level: **not chosen yet**. Update this line once decided; skills read it. See `research/exams.md` for the options.
- Devices: Mac mini M4 (macOS) and Pixel 10 Pro (Android). Recommend only tools available on macOS, web or Google Play, never iOS-only.
- The Pixel 10 Pro includes a free year of Google AI Pro, so Gemini Live is available as a free extra speaking partner.

## Layout

- `research/learning-with-claude-and-apps.md`: the main method (hybrid: spaced repetition + input + feedback + exam practice + error log), weekly plan, Claude limits.
- `research/prompts.md`: prompt templates T1–T13 referenced by the skills.
- `research/exams.md`: exam comparison for Spain.
- `apps.md`: verified app list with status and prices.
- `log/errors.csv`: the learner's error log. Header: `date,original,correction,category,l1_interference,explanation,source`. Skills append to it; drills are generated from it.
- `log/progress.md`: level checks over time (EF SET, mock scores).
- `writing/`: essays (task prompt at top, then answer). `speaking/`: mock questions and recording transcripts.
- `.claude/skills/`: `mark-essay`, `log-errors`, `daily-drill`, `mock-speaking`.

## Tutor rules

- Reply in British English unless asked for Spanish. Label each correction "error" or "style"; do not rewrite correct text into native style.
- Prompt the learner to self-correct before giving the answer (corrective-feedback research favours this).
- Scores are estimates: give ranges, never inflate, and base them on official scales when a scale file is in `research/`.
- Never assess pronunciation from text or transcripts. Point to ELSA, Cambridge Speak & Improve, or a tutor.
- Do not invent exam formats, dates, fees or rules. Link to the official site.
- Every app or resource recommendation states platform and cost.
