# The employer register

`career-watch/state/employers.json` is the universe of options — 200 rows. It exists so
that "have we ever checked this company?" is answerable for all of them, not just the
~50 that have had real research done.

It is built from Adam's tiered master list of companies followed on Gradcracker and
Higherin, plus 15 organisations that previously sat in `resources.md` as bookmarks with no
state record at all.

## Fields

| Field | Meaning |
|---|---|
| `name` | Canonical name. `opportunities.json` and `applications.json` must match it exactly |
| `tier` | `1` civil · `2` chemical/electrical · `3` mechanical/aerospace · `4` nuclear · `5` other · `0` cut |
| `discipline` | `civil` · `chemical` · `electrical` · `mechanical` · `nuclear` · `other` |
| `sources` | Where it is followed: `gradcracker`, `higherin`, `resources.md`, `state-file` |
| `verdict` | `active` · `watch` · `cut` · `not_a_route` |
| `last_checked` | Update whenever checked, **even if nothing was found** |
| `notes` | Verified detail — entry requirements, salary, distance, gates |

## Verdicts

- **`active`** (38) — worth real effort now. A confirmed or strongly inferred route that
  fits Fraser's disciplines and is reachable.
- **`watch`** (120) — plausible but unverified, or verified-but-distant, or a consultancy
  where the desk-based nature needs confirming with Fraser first. Check when time allows.
- **`cut`** (43) — ruled out. **Do not re-suggest.** Includes the master list's cut list
  and Dyson Institute (Fraser is not interested, Aug 2026).
- **`not_a_route`** (1) — BAT. Investigated properly and found to run no UK school-leaver
  apprenticeship. Kept visible so the conclusion is not lost and the work is not redone.

## Tier discipline, honestly applied

Tier 1 and 2 lead. That is a real constraint, not a label: when the sweep is time-limited,
Tier 1 and 2 get checked and Tier 3 does not. The historical employer list was built around
Airbus, BAE, Rolls-Royce and GKN — all Fraser's #4 — so the pull back toward mechanical is
a real risk worth resisting.

Tier 3 is not dropped, for two good reasons: the strongest *local* options are there
(BAE Maritime at Portsmouth ~20mi, Airbus Defence & Space Portsmouth, GKN on the Isle of
Wight, Frazer-Nash studying at Solent), and several employers run mixed-discipline schemes
where the specialism is chosen after joining.

## Consultancy caveat

Arup, Arcadis, Mott MacDonald, AECOM, Stantec, Binnies, Haskoning and Thornton Tomasetti
are largely **desk-based design work** rather than site work. That is a materially
different job from what Fraser described wanting when he ranked civil first. Worth
confirming with him before pushing these hard.

## Open questions carried from the master list

- **RWE** — Higherin showed "RWE Supply & Trading" and "RWEST" as separate followed cards
  with different review counts. Treated as one company. Confirm on the account.
- **Arm** — confirm they run a school-leaver or degree apprenticeship route rather than
  being graduate/PhD-only for chip design.
- **Perenco** — runs a Structural Engineering *graduate* programme, which is closer to
  civil than typical oil and gas. Worth a look if it turns out to have a school-leaver route.
- **Met Office and UK Space Agency** — never checked. Both strong Physics fits.
