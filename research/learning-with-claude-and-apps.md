# How to learn English at home with Claude and apps

Research date: 2026-10-02. Learner: adult Spanish speaker, Mac mini M4 + Pixel 10 Pro, goal = an official certificate.
Items marked **[U]** could not be verified on an official page. Prices change; check at checkout.

## 1. The short answer

The best results come from a **hybrid system**, not from one app:

1. **Spaced repetition every day** (Anki on Mac + AnkiDroid on Pixel). Strongest evidence of anything here.
2. **Lots of comprehensible input** (reading and listening you understand 95%+ of).
3. **Speaking and writing with corrective feedback.** Claude is excellent at this for grammar, vocabulary and structure.
4. **Pronunciation from a tool that actually hears you** (ELSA, Speak & Improve, a human tutor). Claude cannot.
5. **Exam-format practice** with official sample tests and timed mocks in the last 6–8 weeks.
6. **An error log** that drives what you drill. This repo is designed to hold it.

Claude's role: **tutor, corrector, content generator and planner**. Not: official examiner, pronunciation judge, or replacement for input.

## 2. What the research says

| Method | Evidence | How to apply it |
|---|---|---|
| Spaced repetition + self-testing | Strong. Kim & Webb 2022 meta-analysis (48 experiments); Dunlosky 2013 rates it "high utility" | 15 min/day of Anki. Cards from your own errors and reading, not random lists |
| Extensive reading/listening | Good. Jeon & Day 2016 (49 studies), largest effects for adults | Graded readers, podcasts, series with English subtitles |
| Output + corrective feedback | Good. Mackey & Goo 2007; Li 2010. Making you self-correct beats just showing the fix | Ask Claude/tutors to **prompt** you to self-correct first |
| Shadowing | Moderate. Helps listening and word recognition more than accent | 10 min sessions with a Claude-made shadowing script |
| Interleaving grammar | Emerging. Nakata & Suzuki 2019 | Mix tenses/structures in one drill instead of one topic per day |
| Timed mocks | Indirect (testing effect) | One full timed paper per week near the exam |
| Duolingo-type apps alone | Weak for B2+. Positive studies mostly company-funded, receptive skills only | Fine as a habit, not as the plan |
| Re-reading notes, highlighting | Low utility | Replace with quizzing yourself |

**How long it takes.** Cambridge estimates ~200 guided hours per CEFR level (B1→B2, B2→C1). At ~6.5 h/week that is roughly 8–10 months per level in the best case; plan 9–15 months for B1→B2 and 12–18 for B2→C1.

Structure your week with Paul Nation's **Four Strands**: about a quarter each of input, output, language study, and fluency practice.

## 3. Using Claude well

### Features that matter (2026)

| Feature | Use for English | Plan |
|---|---|---|
| Voice mode (Android app best) | Conversation, mock speaking tests. Transcripts are saved, so errors can be extracted after | All plans; Free limited to Haiku model |
| Projects (instructions + files) | A permanent "English tutor" with your level, exam, descriptors and error log | Pro (Free availability **[U]**) |
| Memory | Remembers your level and recurring mistakes across chats | All plans since Mar 2026 |
| Learning style | Socratic grammar explanations. **Turn it off** for mocks and marking | All plans |
| Artifacts | Build your own flashcard, quiz or cloze apps | All plans |
| Claude Code (this repo) | Skills that mark essays, log errors and generate drills from your log | Pro and above |
| Scheduled tasks / routines | Daily drill or weekly progress report | Pro and above |
| Google Drive / Calendar connectors | Read essays in Drive, block study time in Calendar | Free availability **[U]** |

**Recommendation:** Claude **Pro** (US$20/mo, about €18 **[U]**) is enough. Max is not needed.

### Known limits, and how to work around them

1. **It does not hear your accent.** Voice mode transcribes speech to text, so mispronounced words usually arrive "corrected". Never ask Claude to score pronunciation. Use ELSA, Speak & Improve or a tutor.
2. **Scores are estimates.** Studies show LLM essay scores vary from good to poor agreement with human raters, and drift with model updates. Treat any band as ±0.5–1 and watch the trend. Cross-check with Cambridge Write & Improve.
3. **Overcorrection.** It may rewrite correct sentences into "native" style. Ask it to label each change "error" or "style".
4. **It can invent exam rules.** Upload the official descriptors to your Project and check formats on official sites.
5. **It may drift into Spanish.** Set the voice language to English.

Ready-to-paste prompts are in [`prompts.md`](prompts.md).

### Setting up the tutor

1. Create a Claude Project called "English exam".
2. Paste the custom instructions from `prompts.md` (T12).
3. Upload: the official writing/speaking assessment scales for your exam, the errors file (`log/errors.csv`), and your best essays.
4. Use voice mode on the Pixel for speaking, and the Mac (desktop app or Claude Code in this repo) for writing.

## 4. Apps that complement Claude

See [`../apps.md`](../apps.md) for the full verified list. The core stack:

| Need | Tool | Cost |
|---|---|---|
| Vocabulary | Anki (Mac) + AnkiDroid (Pixel) | Free |
| Writing feedback in exam format | Cambridge Write & Improve | Free (Test Zone £4.50/mo) |
| Speaking level estimate | Cambridge Speak & Improve | Free |
| Pronunciation scoring | ELSA Speak | ~US$75–130/yr |
| Extra voice practice | **Gemini Live**: your Pixel 10 Pro includes 1 year of Google AI Pro free | Free for 1 year |
| Record yourself | Pixel Recorder (transcribes English) | Free |
| Listening with subtitles | Language Reactor (Chrome on Mac) | Free |
| Hearing real pronunciation | YouGlish | Free |
| Human feedback | italki / Preply tutor, 1 h/week | Pay per lesson |

## 5. Ideas beyond "Claude plus apps"

- **Use the free Gemini AI Pro year on your Pixel.** Gemini Live is a second voice partner at no cost. Use Claude for marking and planning, and Gemini for extra conversation minutes.
- **Record, transcribe, correct.** Speak for 2 minutes into Pixel Recorder → paste the transcript into Claude → extract errors to the log. The log feeds Anki and drills. This closes the loop between speaking and studying.
- **A human tutor is worth it for speaking.** One 45–60 min lesson per week targets what AI cannot do: pronunciation, interaction, nerves.
- **EOI (Escuela Oficial de Idiomas).** Spain's public language schools issue official certificates, and are cheap compared with private exams. They are accepted for oposiciones. Worth checking if your goal is in Spain.
- **Spanish-speaker blind spots.** Drill these deliberately (see §6). They are the errors examiners notice most.
- **Change your phone and Mac to English.** Free daily input in short bursts.
- **Run this repo with Claude Code.** Skills in `.claude/skills/` mark essays, log errors and generate drills from your own error history. Claude can also schedule a daily drill.

## 6. Typical errors for Spanish speakers

**Pronunciation:** sheep/ship and pool/pull vowel length; schwa /ə/; /v/ said as /b/; "espeak" for speak (s+consonant); dropped -ed/-s endings; word stress and English rhythm; silent letters ("island").

**Grammar and vocabulary:** missing subject ("Is important"); "the" with general nouns ("The life is hard"); present perfect with finished time ("I have seen it yesterday"); make/do; false friends (actually, eventually, assist, sensible, carpet, library, embarrassed); prepositions (depend on, married to); "people is"; "I have 30 years".

## 7. Weekly plan (about 6.5 h)

| Block | Time | Tool |
|---|---|---|
| Anki review | 15 min/day | Anki / AnkiDroid |
| Input: reading + listening | 2 h | Podcasts, series, graded readers, Language Reactor |
| Speaking with feedback | 1 h | Tutor or Claude voice mock + Recorder transcript |
| Writing task + rewrite | 45 min | Claude marking + Write & Improve |
| Shadowing / pronunciation | 30 min | Claude script + ELSA |
| Mixed grammar / Use of English drill | 30 min | Claude drill from error log |
| **Last 6–8 weeks** | Replace some input with 1 full timed paper per week | Official sample tests |

**Progress checks:** EF SET (free, 50 min) every 3 months; a 2-minute recorded monologue each month; error-log category counts going down.

## 8. Next decision: which exam

See [`exams.md`](exams.md). Summary: Cambridge for maximum recognition in Spain; Oxford Test of English or Aptis for cheaper and faster; IELTS for studying or moving abroad.

## Sources

- Cambridge guided learning hours: https://support.cambridgeenglish.org/hc/en-gb/articles/202838506-Guided-learning-hours
- Nation, Four Strands: https://www.victoria.ac.nz/__data/assets/pdf_file/0019/1626121/2007-Four-strands.pdf
- Kim & Webb 2022, spaced practice: https://www.researchgate.net/publication/358406370
- Dunlosky et al. 2013: https://www.whz.de/fileadmin/lehre/hochschuldidaktik/docs/dunloskiimprovingstudentlearning.pdf
- Jeon & Day 2016, extensive reading: https://files.eric.ed.gov/fulltext/EJ1117026.pdf
- Li 2010, corrective feedback: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9922.2010.00561.x
- Nakata & Suzuki 2019, interleaving: https://onlinelibrary.wiley.com/doi/10.1111/modl.12581
- Hamada & Suzuki, shadowing: https://journals.sagepub.com/doi/10.1177/00336882221087508
- Claude voice mode: https://support.claude.com/en/articles/11101966-use-voice-mode
- Claude pricing: https://claude.com/pricing
- LLM essay scoring reliability: https://files.eric.ed.gov/fulltext/EJ1457168.pdf , https://files.eric.ed.gov/fulltext/EJ1495977.pdf , https://aclanthology.org/2023.bea-1.49/
- Chatbots for EFL speaking review: https://www.sciencedirect.com/science/article/pii/S2666920X24000316
- Pixel 10 Pro AI Pro perk: https://www.androidauthority.com/pixel-10-pro-google-ai-pro-perk-3588152/
- Pronunciation for Spanish speakers: https://ihworld.com/ih-journal/issues/issue-48/pronunciation-for-spanish-speakers/
- Free level tests: https://www.efset.org/ , https://www.cambridgeenglish.org/test-your-english/
