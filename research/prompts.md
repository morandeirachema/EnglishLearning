# Claude prompt templates for English exam prep

Replace the parts in [brackets]. Turn **off** the "Learning" style for mocks and marking (T1, T2, T10).

## T12 – Project custom instructions (paste once into your Claude Project)
> I am an adult native Spanish speaker preparing for [exam] on [date]; my current level is about [B2]. Always reply in British English unless I ask for Spanish. Correct my errors at the end of each reply, not inline, and label each one "error" or "style". When I make an error, first ask me to self-correct before giving the answer. Never inflate scores; if unsure, give a range. Base scoring only on the descriptor files in this Project. You cannot hear my pronunciation, so never score it.

## T1 – Mock speaking test (voice mode on the Pixel)
> Act as a certified [IELTS / Cambridge C1 Advanced] Speaking examiner. Run a full Part [1/2/3] test following the official format and timings. Ask one question at a time, stay in role, and give no feedback or help during the test. When I say "END TEST", give me: an estimated band per criterion (excluding pronunciation), 3 strengths, the 5 most costly errors quoted from my transcript with corrections, and 5 higher-level phrases I could have used.

## T2 – Essay marking against descriptors
> Mark this [IELTS Task 2 / B2 First essay / C1 Advanced report] strictly against the attached official assessment scales. For each criterion: score, the descriptor line that justifies it (quoted), and evidence from my text. Then list errors in a table (quote | correction | type: grammar/lexis/cohesion/register | error or style). Correct only genuine errors. Do not rewrite my essay. Finally, name the top 2 changes that would raise my score by one band.
> Task: [paste]
> My answer ([word count] words): [paste]

## T3 – Error log extraction
> From this conversation or transcript, extract every language error I made. Output CSV with header: date,original,correction,category,l1_interference,explanation,source. Quote any field that contains a comma. category is one of: grammar, tense, article, preposition, word-order, vocabulary, collocation, false-friend, register, spelling, listening, reading, pronunciation. l1_interference is yes or no. explanation is 15 words or fewer. source is [voice / tutor / essay name]. Then list my top 5 recurring patterns.
> (These columns match `log/errors.csv`, so the rows can be pasted straight in.)

## T4 – Anki cards (file import)
> Create [20] Anki cloze cards at CEFR [B2/C1] on [topic] for [exam] writing and speaking. Output a plain-text file that starts with exactly these lines:
> `#separator:Semicolon` / `#html:true` / `#notetype:Cloze` / `#deck:English::Exam` / `#tags column:3`
> Then one card per line: Text;Back Extra;Tags. Text = a full English sentence with the target as {{c1::word}}. Back Extra = definition, 2 collocations and a Spanish gloss separated by <br>. Flag false friends. Tags = level and topic, separated by spaces.

## T5 – Reading comprehension at CEFR level
> Write an original [C1] text (~[550] words) on [topic] in the style of [Cambridge C1 Reading Part 5 / IELTS Academic passage]. Then write [6] questions in that exact task type. Hide the key until I say "KEY"; the key must quote the line that proves each answer and explain why each distractor is wrong.

## T6 – Listening script
> Write a [B2 First Listening Part 4] interview script (~[600] words, 2 speakers, natural features: hesitation, reformulation) with [7] multiple-choice questions and a hidden key. Mark speaker turns clearly so I can play it with text-to-speech.

## T7 – Shadowing script
> Create a [2-minute] shadowing script at [B2/C1] on [topic] in natural spoken English. Split into chunks of 1–2 lines. Mark stressed syllables in CAPITALS, pauses with "/" and linking with "‿". Under each chunk, add one note on a likely Spanish-speaker problem (vowel length, schwa, final consonants, /v/–/b/, "es-" before s+consonant).

## T8 – Grammar diagnosis for Spanish L1 errors
> I am a Spanish speaker at about [B2]. Diagnose my grammar from these samples: [paste]. Check especially: articles with general nouns, present perfect vs past simple, missing subjects, make/do, false friends, prepositions, adverb position, gerund vs infinitive, "people is". For each problem: rule, my example, the fix, and 3 practice items with answers hidden.

## T9 – Drill from the error log
> Using the attached errors.csv, build a 10-minute drill: 10 mixed items (gap-fill, transformation, error correction) on my 3 most frequent categories. Interleave the categories. Give one item at a time and wait for my answer.

## T10 – Key word transformation (Cambridge Use of English)
> Generate [8] [B2 First / C1 Advanced] Part 4 key word transformations on [passives / inversion / reported speech]. Exact format: key word in bold, 3–6 words (B2: 2–5). Mark my answers 0/1/2 as Cambridge does and explain lost marks.

## T11 – Flashcard Artifact
> Build an interactive Artifact: a spaced-repetition flashcard app for this CSV [paste]. Flip cards, Again/Good/Easy buttons, simple SM-2 scheduling, progress saved in localStorage, CSV export, mobile-friendly for Android.

## T13 – Recorder transcript review (Pixel Recorder → Claude)
> This is a transcript of me speaking for 2 minutes about [topic] (machine-transcribed, so ignore obvious transcription glitches). Assess fluency and coherence, vocabulary range and grammar at CEFR level. Extract errors as in T3. Then give me a better version at [target level] that keeps my ideas, so I can shadow it.
