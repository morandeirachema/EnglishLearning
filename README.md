<div align="center">

# 🇬🇧 EnglishLearning

**Learn English at home and pass an official certificate, using Claude + the right apps.**

Mac mini M4 🖥️ · Pixel 10 Pro 📱 · Spanish speaker 🇪🇸 · Target: B2 / C1

[The method](research/learning-with-claude-and-apps.md) · [Prompts](research/prompts.md) · [Which exam?](research/exams.md) · [Full app list](apps.md)

</div>

---

## ⚡ The system in one picture

```
   INPUT                OUTPUT               FEEDBACK              MEMORY
 (listen/read)   →   (speak/write)   →   (Claude, tutor,   →   (error log →
  Language Reactor     Claude voice         ELSA, Write &          Anki cards
  Podcasts, YouGlish   Pixel Recorder       Improve)               + daily drill)
        ↑                                                              │
        └────────────────────── repeat every week ─────────────────────┘
```

Every mistake you make ends up in [`log/errors.csv`](log/errors.csv). Your drills and flashcards come from that file, so you practise **your** weak points, not random ones.

---

## 🚀 Start here: week 0

| Day | Do this | Time |
|---|---|---|
| 1 | Free level tests: **EF SET** (efset.org) and Cambridge **Test your English**. Write the results down | 1 h |
| 2 | Baseline: one **Speak & Improve** test and one essay in **Write & Improve** | 1 h |
| 3 | Choose your exam and date in [exams.md](research/exams.md). In Claude Code run `/set-goal` with the exam, date and test results | 30 min |
| 4 | Install: Claude app, Anki + AnkiDroid (+ AnkiWeb sync), ELSA, LanguageTool, Language Reactor. Activate the free **Google AI Pro** year on the Pixel | 45 min |
| 5 | Create the Claude Project (section 1 below) and download your exam's scales ([assessment-scales.md](research/assessment-scales.md)) | 30 min |
| 6 | Book trial lessons with 2–3 exam tutors on italki or Preply | 15 min |
| 7 | First `/weekly-review`: it plans week 1 from your results | 15 min |

---

## 🧰 The apps and how to use them

Legend: 🆓 free · 💶 paid · 🖥️ Mac · 📱 Pixel · 🌐 web

### 🤖 1. Claude: your tutor &nbsp;💶 Pro ~US$20/mo · 🖥️📱🌐

**Setup (once)**
1. Install the Claude app on the Pixel (Google Play) and the desktop app on the Mac.
2. Create a Project called **English exam**. Paste prompt **T12** from [prompts.md](research/prompts.md) into its instructions.
3. Upload the official writing and speaking assessment scales for your exam to the Project. [assessment-scales.md](research/assessment-scales.md) lists the criteria and where to download them.
4. In Settings, set the voice language to **English**.

**Daily use**
- 🎙️ **Speaking mock:** on the Pixel, open voice mode inside the Project and paste prompt **T1**. Say "END TEST" to get feedback.
- ✍️ **Essays:** save the essay in `writing/`, then in Claude Code on the Mac run `/mark-essay`.
- 🧠 **Grammar questions:** turn on the *Learning* style so Claude makes you think instead of just answering.
- 🔁 **Drill:** run `/daily-drill` in Claude Code for 10 minutes on your top 3 error types.

> ⚠️ Claude cannot hear your accent and its band scores are estimates (±0.5–1). Use it for grammar, vocabulary and structure. Use ELSA or a tutor for pronunciation.

---

### 🗂️ 2. Anki + AnkiDroid: vocabulary &nbsp;🆓 · 🖥️📱

**Setup**
1. Install **Anki** on the Mac (apps.ankiweb.net) and **AnkiDroid** on the Pixel (Google Play).
2. Create a free **AnkiWeb** account and log in on both to sync.
3. Create a deck called `English::Exam`.

**How to use**
- ⏱️ **15 minutes every day** on the Pixel (commute, coffee). Never skip reviews: that is where the memory happens.
- ➕ Add cards from **your own** mistakes and reading, not random lists. Run `/daily-drill` and ask for Anki cards; it writes `log/anki-DATE.txt`.
- 📥 Import in Anki on the Mac: *File → Import*, pick the file. The file tells Anki the deck, card type and separator, so just press **Import**. Then *Sync*; the cards appear on the Pixel.
- 💡 Use whole sentences (cloze cards), not single words: you learn collocations at the same time.

---

### 📝 3. Cambridge Write & Improve: writing feedback &nbsp;🆓 · 🌐

1. Sign up at **writeandimprove.com** (works in the Mac browser).
2. Pick a task at your level, or paste the same essay you gave Claude.
3. Rewrite the highlighted parts and resubmit until the CEFR level stops rising.
4. **Use it as a second opinion** on Claude's score. If they disagree, trust the trend over several essays.

### 🗣️ 4. Cambridge Speak & Improve: speaking level &nbsp;🆓 · 🌐

1. Open **speakandimprove.com** on the Mac (use a headset mic).
2. Do one test per month and write the result in [`log/progress.md`](log/progress.md).

---

### 🎯 5. ELSA Speak: pronunciation &nbsp;💶 ~US$75–130/yr · 📱

1. Install from Google Play, take the assessment test.
2. Focus on the classic Spanish-speaker sounds: **ship/sheep**, **/v/ vs /b/**, **schwa**, **"es-peak"**, final **-ed/-s**.
3. 10 minutes a day, 4 days a week. Wait for the frequent 50% offers before paying.

### 🎙️ 6. Pixel Recorder: record yourself &nbsp;🆓 · 📱

The loop that turns speaking into data:
1. Open **Recorder**, talk for **2 minutes** about any exam topic.
2. Copy the English transcript.
3. Paste it into Claude with prompt **T13**, or in Claude Code run `/log-errors`.
4. Shadow the improved version Claude gives you. Record again next week and compare.

### ✨ 7. Gemini Live: free extra conversation &nbsp;🆓 1 year · 📱

Your Pixel 10 Pro includes **1 year of Google AI Pro**. Activate it in the Google One / Gemini app.
- Long-press the power button → Gemini Live → "Let's practise English conversation at B2 level. Correct me at the end."
- Use it for **extra minutes** (walks, cooking). Keep Claude for marking and planning.

---

### 🎬 8. Language Reactor: series and YouTube &nbsp;🆓 · 🖥️

1. Install the extension in **Chrome** on the Mac.
2. Watch Netflix or YouTube with **English subtitles on top** and Spanish below (hide the Spanish once you can).
3. Click any word to see its meaning; save useful phrases to Anki.

### 🔊 9. YouGlish: real pronunciation &nbsp;🆓 · 🌐📱

Type a word or phrase you're not sure how to say → hear it in dozens of real YouTube clips. Filter by **UK** or **US** accent.

### 🎧 10. Podcasts: daily listening &nbsp;🆓 · 📱

- **BBC 6 Minute English** (B1–B2) → **BBC Global News** / **Luke's English Podcast** (B2–C1).
- Listen once normally, once with the transcript, and shadow one minute of it.
- ℹ️ The BBC Learning English *app* closed in 2023; the podcasts and website still work.

---

### ✅ 11. LanguageTool: everyday writing &nbsp;🆓 · 🖥️📱

1. Install the Mac app and the browser extension; on the Pixel, enable the LanguageTool keyboard.
2. Write emails, messages and notes in English; read **why** each fix is suggested.
3. Alternative: Grammarly (company now called Superhuman).

### 👩‍🏫 12. italki / Preply: a human tutor &nbsp;💶 per lesson · 🌐📱

1. Search for an **exam-specialised** tutor (e.g. "Cambridge C1" or "IELTS"). Book a cheap trial lesson with 2–3 tutors.
2. Book **one 45–60 min lesson per week**: speaking mock + pronunciation.
3. Ask: *"Please make me self-correct before you give me the answer."*
4. Paste the lesson notes into `/log-errors`.

### 🏛️ 13. Official exam practice &nbsp;🆓/💶 · 🌐

| Exam | Use this |
|---|---|
| Cambridge B2 / C1 | Free sample papers on cambridgeenglish.org · Test & Train (via exam centres) |
| IELTS | British Council **IELTS Ready** (free tier) · **IELTS by IDP** app |
| TOEFL | **Official TOEFL Practice** app (ETS) |
| Aptis | Free British Council practice tests |

In the **last 6–8 weeks**, do one **full timed paper per week**.

### 🔈 14. Mac voices: exam-style listening audio &nbsp;🆓 · 🖥️

Claude writes the listening script; your Mac turns it into audio with British, Irish and Australian voices, played twice like the real exam.
1. In Claude Code run `/listening-practice` (or write your own script in `listening/`, one `A:` / `B:` turn per line).
2. It runs `python3 scripts/listening.py listening/FILE.txt --twice` and creates an `.m4a`.
3. Play it on the Mac, or drop it in Google Drive and play it on the Pixel. Answer the questions **before** opening the key.
4. Slow it down below B2 with `--rate 150`.

### 📖 15. Dictionaries: aim at the right level &nbsp;🆓 · 🌐

- **Cambridge Dictionary**: your default dictionary. Listen to the 🇬🇧 audio for every new word.
- **Oxford Learner's Dictionaries**: download the **Oxford 3000/5000** lists; the B2 and C1 words are your vocabulary syllabus.
- **Ozdic** (collocations): before using a word in an essay, check what goes with it (*make* a decision, *do* research). Fixes the *make/do* trap.
- **English Vocabulary Profile**: check whether a word meaning is B2 or C1, so your essays show the level examiners want.
- **Text Inspector**: paste a finished essay to see its vocabulary level.

---

## 🗓️ Weekly routine (~7 h)

| When | What | App | Time |
|---|---|---|---|
| Every day | Flashcard review | AnkiDroid 📱 | 15 min |
| Mon | Listening + shadowing | Podcasts / Language Reactor | 30 min |
| Tue | Speaking mock or tutor | Claude voice / italki | 45 min |
| Wed | Exam-style listening or reading task (alternate weeks) | `/listening-practice` · `/reading-practice` | 30 min |
| Thu | Essay + rewrite | Claude `/mark-essay` + Write & Improve | 45 min |
| Fri | Mixed grammar drill | Claude `/daily-drill` | 20 min |
| Sat | Series / reading for fun | Language Reactor, Kindle | 1 h |
| Sun | Record 2 min → log errors | Pixel Recorder + `/log-errors` | 15 min |
| Daily, short | Pronunciation | ELSA | 10 min |

📊 **Track it:** the Claude Code skills log their own minutes to [`log/study.csv`](log/study.csv). For everything else (podcasts, Anki, tutor, series), tell Claude Code what you did, e.g. `/log-study 30 min podcast, 15 min Anki`. Strands: `input`, `output`, `study`, `fluency`, `exam`.

🔄 **Every Sunday:** run `/weekly-review` in Claude Code. It runs `python3 scripts/stats.py`, shows your hours, strand balance and which error types are going down, then plans next week.

📈 **Every 3 months:** take the free **EF SET** test (efset.org) and note the score in `log/progress.md`.

---

## 💡 Quick wins

- 📱 Switch your **Pixel and Mac to English**: free input dozens of times a day.
- 🔁 Never study the same thing twice in a row: **mix** grammar points (interleaving works better).
- 🙊 Ask every corrector to make you **self-correct first**.
- 🚫 Don't rely on Duolingo alone; fine as a habit, not enough for B2+.
- 🏫 Check your local **Escuela Oficial de Idiomas** for a cheap official certificate.

---

## 🔒 Privacy

This repository is **public** on GitHub. Your essays, speaking transcripts and error log will be readable by anyone once pushed.
- Don't write names, employers, addresses or health details in essays or transcripts; invent them for exam tasks.

---

## 📁 Repo map

| Path | What it is |
|---|---|
| [`research/`](research/) | The method, prompt templates, exam comparison |
| [`apps.md`](apps.md) | Full verified app list with prices |
| [`log/errors.csv`](log/errors.csv) | Your error log (skills write here) |
| [`log/study.csv`](log/study.csv) | Minutes studied per strand |
| [`log/progress.md`](log/progress.md) | Weekly reviews and level checks |
| `writing/` · `speaking/` | Your essays and speaking transcripts |
| `listening/` | Listening scripts and generated audio |
| `reading/` | Reading and Use of English tasks |
| `scripts/` | `listening.py` (audio from scripts) · `stats.py` (progress report) |
| `.claude/skills/` | `/mark-essay` · `/log-errors` · `/daily-drill` · `/mock-speaking` · `/listening-practice` · `/reading-practice` · `/log-study` · `/weekly-review` · `/set-goal` |

<div align="center">

**Next step:** do [week 0](#-start-here-week-0). 🚀

<sub>App status and prices checked 2026-10-02. They change; check before paying.</sub>

</div>
