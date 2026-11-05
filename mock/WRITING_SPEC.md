# Mock G1 — question writing spec

Candidate: Catalin, CFA Level I, exam 13 Nov 2026 (2026 curriculum). Mock G1 = 180 ORIGINAL questions, 2 sessions × 90, built from `analysis/blueprint.json` (topic counts + concept list per topic) and `analysis/patterns.md` (his weak concepts and recurring error types — read sections (c)–(e)).

## Hard rules
- **Original only.** Never copy or closely paraphrase any question from CFA Institute, Mark Meldrum (MM), Kaplan or the transcripts. New scenarios, names, companies, numbers. Concept tags in analysis/ are fine to use.
- Real exam format: standalone multiple choice, exactly three options A/B/C, exactly one unambiguously correct answer. No "all/none of the above". No vignettes/item sets.
- Real exam wording and difficulty: ~15% easy, ~60% medium, ~25% hard. About 15% of stems use LEAST / NOT / EXCEPT / "least likely" (he misses these 64% of the time — include them). "Most likely", "closest to", "best describes" as on the real exam.
- Distractors must be **plausible and specific**: for calculations each wrong option = a named mistake (sign flip, ÷n instead of n−1/n−2, skipped last step like × critical t or e^x or D1 vs D0, wrong period count, annual vs periodic, wrong formula variant). For concepts, use the classic confusions (e.g. V(A) vs V(B), DTA vs DTL direction, Type I vs II, X explains Y direction).
- **Every calculation verified with Python** before writing it in; options rounded consistently; keep the correct value and each distractor's derivation in the explanation.
- Balance answer keys: across your set, A/B/C each ≈ ⅓ (±2). Don't let position give the answer away.
- Notation: σ² variance, σ standard deviation. Currencies: mix (USD, EUR, GBP, JPY, CHF) as the real exam does.
- Ethics: realistic workplace scenarios with named people; the stem never names the Standard; the explanation cites it (e.g. "Standard III(B) Fair Dealing"). Include "best practice vs minimum required" and "count all conflicts" patterns. GIPS/Code basics as blueprint says.

## Schema (JSON array of objects)
```json
{"id":"eth-01","topic":"ethics","concept":"<concept string from blueprint>","difficulty":"easy|medium|hard",
 "stem":"HTML allowed: <p>, <br>, <b>, <i>, <sub>, <sup>, <table> (simple, with <th>/<td>)",
 "options":{"A":"...","B":"...","C":"..."},"answer":"A|B|C",
 "explanation":"HTML. Why the answer is right (with full working); why EACH wrong option is wrong (name the mistake and show its number). For calculations add BA II Plus keystrokes in a <p><b>BA II Plus:</b> ...</p>. Cite the LOS idea / Standard."}
```
Topic codes: ethics, quant, econ, fsa, ci, equity, fi, deriv, alts, pm. IDs: `<topic>-NN`.

## Process
1. Read the blueprint entries for your topics; write exactly that many questions per concept (`n`). If a concept is impossible to test well, swap for a closely related one in the same topic and say so in your report.
2. Write the file `mock/parts/<topic>.json` (create `mock/parts/`).
3. Run a self-check script: valid JSON, schema, count per concept matches blueprint, answer key balance, every calculation recomputed in Python and matching the keyed option, no duplicate stems.
4. Re-read every question once as the candidate: is exactly one option defensible? Fix any ambiguity.
5. Report ≤10 lines: counts, key balance, substitutions, anything uncertain.

Do NOT git commit. Do not edit any file outside `mock/parts/`.
