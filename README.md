# CFA gap deck

499 flashcards for CFA Level I, built from handwritten revision notes — the terms
that were actually missed in practice, kept in the original wording.

**Open it:** https://catalinbondari.github.io/cfa-flashcards/

## How it works

Term on the front, tap to flip, then mark **Got it** or **Missed it**. Missed cards
stay flagged until answered correctly, and **Review missed** drills only those.
Filter by topic, shuffle, undo a mis-tap. Progress is saved in the browser.

Keyboard: `space` flip · `←` missed · `→` got it · `z` undo

## Topics

| Topic | Cards |
|---|---|
| Financial statements | 103 |
| Fixed income | 77 |
| Equity | 62 |
| Quant methods | 55 |
| Portfolio management | 51 |
| Ethics | 45 |
| Alternatives | 36 |
| Economics | 31 |
| Derivatives | 25 |
| Corporate issuers | 14 |

## Editing

Card text lives in `src/batch1.txt`–`src/batch4.txt`, one `Term :: definition`
per line. After editing:

```bash
cd src && python3 build.py     # regenerates cards.json
```

Then rebuild `index.html` from `src/page.html` (the page body) with the new
`cards.json` inlined at the `__CARDS__` placeholder.
