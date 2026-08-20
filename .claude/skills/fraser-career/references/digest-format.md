# Digest format

Two artefacts per run, plus one fixed-path copy.

| Path | Purpose |
|---|---|
| `career-watch/digests/YYYY-MM-DD.md` | Compressed operational brief. Append-only history |
| `career-watch/digests/YYYY-MM-DD.html` | Dated HTML, so the emailed version has history too |
| `career-watch/digests/latest-email.html` | Same HTML, overwritten each run. **The workflow reads this exact filename — do not rename it** |

## Section order

Pipeline status comes first. The digest's job is to answer "where are we?" before "what's new?".

```
Fraser's Career Watch — {date}
Phase: {phase} — {one line}

PIPELINE
- Applied: {n} · Not started: {n} · Rejected: {n} · Offers: {n}
- Most recent: {employer} — {what happened} ({date})

CLOSING SOON (next 14 days)
- {employer} — {role} — closes {date} — {link}

NEW SINCE LAST RUN
- {employer} — {role} (Tier {n}, {discipline}) — {level} — {town}, {n} mi — {link}

TIER 1 AND 2 — what changed
- {employer}: {what changed}

TIER 3 AND BREADTH — what changed
- {employer}: {what changed}

PILOT
- {scheme}: {status, with cost if self-funded}

REGISTRATIONS — {n} of {n} done
- {named unticked items that have a clock on them}

DO THESE NEXT
1-3 concrete actions, most urgent first
```

Omit a section rather than writing "nothing to report" under it. An empty NEW SINCE LAST
RUN is normal and is not a failure.

## HTML conventions

Match the established house style — this has to survive email clients, so:

- **100% inline CSS.** No `<style>` blocks, no external stylesheets, no images.
- `<body style="font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;line-height:1.55;color:#1a1a1a;max-width:760px;margin:0 auto;padding:16px;">`
- Headings `#0b4f6c` with `border-bottom:3px solid`. Corrections in `#b00020`.
- Callout blocks: `background` plus `border-left:5px solid`. Amber `#fff4e5`/`#e07b00` for
  the headline item, yellow `#fffbe6`/`#d4a000` for unresolved conflicts, blue
  `#e8f4f8`/`#0b4f6c` for open questions, grey `#f6f6f6`/`#999` for the method caveat.
- One date table, `border-collapse:collapse;width:100%;font-size:14px`, header row
  `#0b4f6c` on white, and `background:#ffe5e5` on the most time-critical rows.
- Emoji-prefixed `<h2>`s are the established style — keep them.
- Close with a grey footer line: date of the run and what the next review is for.

## Tone

The existing digests read as a briefing from someone who has actually done the reading, and
they are willing to say "the previous entry was wrong". Keep that. Corrections are the most
valuable thing a digest can carry — three of them in the 17 August run (ST0523 retired, the
BA practice test carrying nothing forward, TUI suspended) each prevented a real mistake.

State uncertainty in the sentence, not in a disclaimer at the bottom.
