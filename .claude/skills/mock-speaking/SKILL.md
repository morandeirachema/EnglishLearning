---
name: mock-speaking
description: Prepare a speaking mock test, or assess a speaking transcript saved in speaking/. Use when the user wants speaking practice, a speaking exam simulation, or feedback on a recording transcript.
---

1. For a new mock: write the questions for the requested part of the target exam (from `CLAUDE.md`) to `speaking/YYYY-MM-DD-mock.md`, plus the matching voice-mode prompt (research/prompts.md T1) so the learner can run it on the Pixel in Claude voice mode.
2. For an assessment: read the transcript in `speaking/`. Score with the target exam's speaking criteria from `research/assessment-scales.md` (skipping Pronunciation), giving ranges only. State plainly that pronunciation cannot be judged from a transcript, and point to ELSA, Speak & Improve, or a tutor.
3. Log errors to `log/errors.csv` (source = transcript file name).
4. Write an improved version at the target level that keeps the learner's ideas, for shadowing.
