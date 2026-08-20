---
name: fraser-career
description: Fraser's apprenticeship and pilot-cadet search for a September 2027 start — watch the four job sources for new openings, track application status, and coach personal statements and STAR examples. Use for the career check or digest, to log an application or outcome, to ask what's open or where things stand, or to work on a personal statement or interview answer.
allowed-tools: WebSearch, WebFetch, Read, Write, Edit
---

# Fraser's Career

One skill for the whole search. It replaces three that used to overlap: `fraser-career-watch`,
`southampton-apprenticeship-watch` (an obsolete predecessor whose Excel state store no longer
exists) and `fraser-statement-coach`. If either of those two still appears in a skill list,
they are retired — this file is the current one.

## Who this is for

Fraser is 17, starting Year 13 at Peter Symonds College in September 2026, studying
**Maths, Physics and Chemistry** at A-level, targeting a **September 2027** start.

**Discipline ranking, in his own words (Aug 2026):**

| Rank | Discipline | His framing |
|---|---|---|
| **1** | Civil | Roads, bridges, railways, skyscrapers, stadiums, shopping centres |
| **2** | Chemical | Turning raw materials into fuel, plastic, food; safety and environment |
| **3** | Electrical | Electric cars, smartphone circuits, integrating renewables into the grid |
| **4** | Mechanical | Fuel-efficient aircraft, nuclear power plants, robotic surgery |

**Tier 1 (civil) and Tier 2 (chemical/electrical) lead.** Mechanical and aerospace stay
tracked as breadth and as genuinely strong local options, but they do not get equal
attention when time is short. This matters because the employer list was historically
built around Airbus/BAE/Rolls-Royce/GKN — Fraser's #4.

**Two tracks are priority: engineering apprenticeships and pilot cadet schemes.** British
American Tobacco and Civil Service Career Launch were both investigated and closed out
(see Settled questions below); Dstl and GCHQ survive from that work and are tracked as
engineering opportunities.

**Base:** Southampton. Search a 25-mile radius, not 15 — the old radius missed AECOM at
Basingstoke (~35mi) and Arup's Southampton cycle. Note distance from Southampton on
every result, because relocation versus commute changes whether something is viable.

## Settled questions — do not re-open these

Re-litigating these wastes the digest's most valuable space.

- **Nationality and date of birth both clear the eligibility gates** (confirmed Aug 2026).
  AWE's British-citizenship and 18-by-31-August requirements, Dstl/MOD/GCHQ's no-dual-nationality
  and 5-year-residency rules, and BAE's 5–10 year continuous residency rule are all satisfied.
  Stop flagging these as open risks.
- **Dyson Institute is cut.** Fraser is not interested. Do not re-suggest it.
- **The pilot apprenticeship route does not exist.** Standard ST0523 (First Officer Pilot)
  was **retired on 1 July 2024**. There are no live vacancies against it and structurally
  there cannot be. Airline cadet schemes are the only route to a flight deck.
- **The BA practice test carries nothing forward.** The BA Speedbird window was 14–23 April
  2026 and closed. The test Fraser is part-way through sits on BA's year-round *preparation*
  page — it is not a live application and earns no standing. A fresh application is needed
  in the next window (~mid-April 2027).
- **BAT runs no UK school-leaver apprenticeship** (verified Aug 2026). Its Southampton site
  is an R&D centre offering 12-month *undergraduate placements* requiring existing university
  enrolment. Passive watch only.
- **Civil Service Career Launch is blocked** — eligibility is "16 or older **and not in
  full-time education**", so Fraser cannot apply while at school. It is also only a Level 3
  Business Administrator qualification. Fallback, not a target.

## Data model

Three files, three questions.

| File | Question it answers |
|---|---|
| `career-watch/state/employers.json` | What are all the options? 200 companies with `tier`, `discipline`, `sources`, `verdict`, `last_checked` |
| `career-watch/state/opportunities.json` | What is live, and when does it open and close? |
| `career-watch/state/applications.json` | What has Fraser actually done? |
| `career-watch/state/pilot.json` | The cadet schemes — separate because they carry cost, funding and medical fields |

`career-watch/state/archive/` holds superseded files. Do not read them for current state.

**Field conventions.** `verdict` is `active` · `watch` · `cut` · `not_a_route`. `confidence`
is `confirmed` · `inferred` · `unconfirmed` · `conflicting`, sitting alongside the free-text
`date_confidence` which explains *why*. `status` in `applications.json` is `not_started` ·
`applied` · `rejected` · `offer` · `withdrawn`. `opens` uses `YYYY-MM-DD` when a day is
known and `YYYY-MM` when only a month is — never invent a day to look precise, and never
put a word like "autumn" in a date field; that belongs in `notes`.

`last_checked` on an employer row is what makes "have we ever looked at this one?" answerable
for all 200, not just the researched 50. Update it whenever you check a company, even if
nothing was found.

## Modes

Infer the mode from the request. `watch` is the default.

### watch — the sweep and digest
Full routine below. Writes state files and `career-watch/digests/`.

### status — read-only
Answer "where are we?" from the state files without writing anything. Lead with the
application pipeline, then what is open now, then what opens next, then anything closing
within 14 days. Keep it short — this is a question, not a report.

### log — record an application or outcome
Append to or update `applications.json`. Set `applied_date` and `last_updated`. Touch
nothing else. If the employer is not in `employers.json`, add them there too rather than
creating an orphan.

### coach — statements and STAR examples
Read `references/coaching.md` and follow it. It has five session modes (extraction,
motivation, drafting, review, status check) and its own working file,
`career-watch/prep/star-bank.md`, created from `references/star-bank-template.md` on first
use. Supporting references: `signs-of-ai-writing.md`, `strong-examples.md`,
`statement-research.md`.

Before a coaching session, read `applications.json` — coaching for an employer Fraser is
actually applying to beats coaching in the abstract, and a deadline inside two weeks
changes what is worth working on. This cross-awareness is the reason the coach lives here
rather than in its own skill.

## The watch routine

### 1. Four primary sources
Search all four. The first two are the highest-signal.

1. **Higherin** (higherin.com) — the only aggregator of live "Register Your Interest 2027"
   listings, plus 48,000+ apprentice-written reviews. Absorbed RateMyApprenticeship in
   August 2025, so do not treat that as a separate source.
2. **Gradcracker** (gradcracker.com) — best single source for STEM. Fraser follows 93
   employers with alerts active. **Not yet followed and should be: Babcock, GKN Aerospace,
   WSP, L3Harris.**
3. **GOV.UK Find an Apprenticeship** — the official database, England only. Southampton,
   25 miles, all sectors.
4. **Amazing Apprenticeships** (amapps.uk) — publishes its Higher & Degree Vacancy Listing
   **three times a year: October, January, April**. October is the bumper edition (October
   2025 carried 1,600+ vacancies across 50+ employers). The Vacancy Snapshot subscription
   is how it arrives automatically.

Also check UCAS Apprenticeships (best filtering of any board) and, for nuclear roles that
the general sweep misses, the Destination Nuclear Careers Portal.

### 2. Named employer watch
Prioritise by tier. Check Tier 1 and 2 first: WSP, Thames Water, AECOM, Balfour Beatty,
AtkinsRealis, Arup, Arcadis, Network Rail, TfL, National Grid, NESO, ExxonMobil Fawley.
Then Tier 3 breadth: Airbus, BAE Systems (and BAE Maritime, Portsmouth), GE Aerospace,
Babcock, GKN, Frazer-Nash, L3Harris, MBDA, QinetiQ.

### 3. Pilot watch
BA Speedbird (~mid-April 2027 inferred from four consecutive mid-April openings),
Jet2FlightPath (~February 2027 — the 2026 window was only 2.5 weeks, so this needs a hard
reminder), easyJet/CAE (rolling but ~EUR115,000 self-funded), Ryanair (rolling,
self-funded, 5-year bond). TUI is suspended; Virgin is paused. Do not report a self-funded
scheme without its cost.

### 4. Diff and write
Compare against the state files. Flag (a) anything new and (b) anything closing within 14
days. Append new opportunities with today's date; never delete closed ones — keep the
history, just stop flagging them as new. Update `last_checked` on the employer rows you
touched.

Then write `career-watch/digests/YYYY-MM-DD.md`, `career-watch/digests/YYYY-MM-DD.html`,
and overwrite `career-watch/digests/latest-email.html` with the same HTML. The workflow
emails that fixed path, so its name cannot change. See `references/digest-format.md`.

## Rules that matter more than completeness

- **Never present a placement or graduate scheme as an apprenticeship.** They are different
  things with different entry requirements. BAT's Southampton 12-month Packaging Innovation
  placement is the standing example of the trap — it requires existing university enrolment.
- **Never tick a checkbox in `registrations.md` on Fraser's behalf.** Report its state;
  only Fraser or Adam ticks. An inaccurate tick produces a misleading digest.
- **Say plainly when something was not found.** Absence of search evidence is not evidence
  the scheme does not exist. "Nothing found for QinetiQ" is a useful sentence; implying
  QinetiQ has no scheme is not.
- **Label every unverified date.** The network proxy in this environment blocks direct page
  loads for essentially every careers domain, so dates come from search snippets quoting
  those pages, and snippets can be cached. Say so. The autumn 2026 dates in particular
  should be confirmed in a normal browser before Fraser relies on them.
- **Treat rolling and close-when-full schemes as "apply now".** Airbus states explicitly
  that applications may close at any time without notice; BAE did it in practice in 2026.
  For these, week-one applications matter far more than deadlines.
- **Do not manufacture enthusiasm.** See `references/coaching.md` — Fraser has no
  pre-existing engineering origin story, and inventing one produces exactly the writing
  that assessors discount.

## Current state, August 2026

Phase 2 of the plan in `career-watch/reading-plan.md` starts now. **October 2026 is the
densest month of the cycle.**

The most time-critical items: **National Grid opens September 2026** (talent pool needs a
CV upload — one page is enough), **Airbus opens October 2026** with no closing date,
**Babcock opens October 2026**, **GE Aerospace 8 October** (Dowty and Feltham),
**both WSP Southampton roles** — the only genuinely local degree-level civil matches found.

**Registrations are the weak point: 5 of 65 items are ticked.** Of the four primary
sources only Gradcracker is done. Higherin is not — and `registrations.md` itself calls it
the biggest gap in the setup. The Amazing Apprenticeships subscription is not done either,
which means October's bumper listing has to be remembered manually in the busiest month.
Surface this in every digest with the count and the items that have a clock on them.
