# Assessment criteria by exam

`/mark-essay` and `/mock-speaking` score against this file. It lists each exam's **criteria names and task facts**, not the official descriptor wording.
For exact band wording, download the official document and put it in your Claude Project (it is free but copyrighted, so `research/scales/` is gitignored; keep local copies there).

## Cambridge B2 First and C1 Advanced

Overall result on the **Cambridge English Scale**:

| Exam | Grade A | Grade B | Grade C (pass) | Level 1 below |
|---|---|---|---|---|
| B2 First | 180–190 → certificate at C1 | 173–179 (B2) | 160–172 (B2) | 140–159 → B1 |
| C1 Advanced | 200–210 → certificate at C2 | 193–199 (C1) | 180–192 (C1) | 160–179 → B2 |

**Writing:** each task is marked on 4 criteria, 0–5 each (20 per task):
1. **Content**: all points of the task covered, reader fully informed.
2. **Communicative Achievement**: register, format and tone right for the task type.
3. **Organisation**: paragraphs, linking, logical flow.
4. **Language**: range and accuracy of grammar and vocabulary.

| | Part 1 (compulsory) | Part 2 (choose 1) | Words |
|---|---|---|---|
| B2 First | Essay | Article, email/letter, report, review | 140–190 each |
| C1 Advanced | Essay (evaluate 2 of 3 points) | Letter/email, proposal, report, review | 220–260 each |

**Speaking** (face to face, in pairs, 4 parts):
- B2 First: Grammar and Vocabulary · Discourse Management · Pronunciation · Interactive Communication, plus a Global Achievement mark.
- C1 Advanced: Grammatical Resource · Lexical Resource · Discourse Management · Pronunciation · Interactive Communication, plus Global Achievement.

**Official source:** the "Handbook for teachers" for each exam at cambridgeenglish.org (search "B2 First handbook for teachers" / "C1 Advanced handbook"). It contains the full writing and speaking assessment scales and sample answers with examiner comments. The examiner comments are the best calibration material for Claude.

## IELTS (Academic and General Training)

Overall band 0–9 in half bands; each skill also gets a band.

**Writing** (Task 2 counts double Task 1):
1. **Task Achievement** (Task 1) / **Task Response** (Task 2)
2. **Coherence and Cohesion**
3. **Lexical Resource**
4. **Grammatical Range and Accuracy**

| Task | Academic | General Training | Words | Time |
|---|---|---|---|---|
| 1 | Describe a chart, table, process or map | Letter | 150+ | ~20 min |
| 2 | Essay | Essay | 250+ | ~40 min |

**Speaking** (11–14 min, 3 parts): Fluency and Coherence · Lexical Resource · Grammatical Range and Accuracy · Pronunciation.

**Official source:** the public band descriptors for Writing (Task 1, Task 2) and Speaking on ielts.org (search "IELTS writing band descriptors"). They were revised in 2023; use the current version.

## Other exams

Aptis, Oxford Test of English, Linguaskill, Trinity ISE and TOEFL publish their own scales. Download them from the provider's site (see [exams.md](exams.md)) into `research/scales/` before asking for scores. Without the official scale, Claude must say its score is a rough CEFR estimate.

## Rules for Claude when scoring

- Never score Pronunciation from text or transcripts.
- Give a range when evidence is mixed (e.g. Language 3–4, Band 6.0–6.5).
- Check word count and task type first: under-length or wrong format costs Content / Task Response.
- Compare with the handbook's sample answers when they are in the Project or `research/scales/`.
