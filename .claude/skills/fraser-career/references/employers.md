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
| `work_setting` | `site` · `plant` · `field` · `mixed` · `desk` · `lab` (`n/a` for cut) — see below |
| `sources` | Where it is followed: `gradcracker`, `higherin`, `resources.md`, `state-file` |
| `verdict` | `active` · `watch` · `cut` · `not_a_route` |
| `last_checked` | Update whenever checked, **even if nothing was found** |
| `notes` | Verified detail — entry requirements, salary, distance, gates |

## Verdicts

- **`active`** (38) — worth real effort now. A confirmed or strongly inferred route that
  fits Fraser's disciplines and is reachable.
- **`watch`** (120) — plausible but unverified, or verified but distant. Check when time allows.
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

## Work setting — the boots-on-the-ground filter

Fraser wants to be **out on site, not behind a desk** (confirmed Aug 2026). `work_setting`
records that for every employer.

| Value | Means | Fit |
|---|---|---|
| `site` | Construction sites, rail track, roadworks, marine and offshore works | ✅ Target |
| `plant` | Industrial plant, refinery, process operations, factory, shipyard | ✅ Target |
| `field` | Distributed network work — grid, water mains, highways, rail infrastructure | ✅ Target |
| `mixed` | Genuine rotation between site and office | ✅ Acceptable |
| `desk` | Office-based design, consultancy, analysis | ⚠️ Against preference |
| `lab` | Laboratory or R&D bench work | ⚠️ Against preference |

As built: 29 `site`, 55 `plant`, 24 `field`, 12 `mixed`, 29 `desk`, 10 `lab`. So **108 of the
159 live employers are boots-on-ground** — the preference narrows the list usefully without
gutting it.

**Assign from evidence about the role, not the company's sector label.** A contractor can run a
desk-based design apprenticeship and a consultancy can run a genuinely site-based one. Where a
company runs several routes, tag it by the one Fraser would actually take, and say so in the
dossier. The initial pass was assigned by sector and is being corrected company by company as
the research dossiers are written — treat a tag with no dossier behind it as provisional.

**This is a tag, not a veto** (Adam's call, Aug 2026). Tier still leads, and desk-based
employers stay on the list — Arup, Arcadis, Mott MacDonald, AECOM, Stantec, Binnies, Haskoning,
Thornton Tomasetti, Hoare Lea and WSP are all still live options. The tag exists so the split
is visible and a digest can say "this one is design work" rather than presenting everything
neutrally.

### The WSP tension — leave it visible

The preference and the best local option point in opposite directions. WSP's two Southampton
vacancies are the only genuinely local degree-level civil roles found anywhere, and they are
design work. Adam's decision is to keep them a priority but establish how much site time they
actually carry first. **Do not resolve this silently either way** — it is Fraser's call to make
knowingly.

## Open questions carried from the master list

- **RWE** — Higherin showed "RWE Supply & Trading" and "RWEST" as separate followed cards
  with different review counts. Treated as one company. Confirm on the account.
- **Arm** — confirm they run a school-leaver or degree apprenticeship route rather than
  being graduate/PhD-only for chip design.
- **Perenco** — runs a Structural Engineering *graduate* programme, which is closer to
  civil than typical oil and gas. Worth a look if it turns out to have a school-leaver route.
- **Met Office and UK Space Agency** — never checked. Both strong Physics fits.
