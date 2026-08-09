---
name: fraser-career-watch
description: Daily watch across four tracks for Fraser's post-A-level career search — engineering apprenticeships (Southampton area + named employers), pilot training pathways, British American Tobacco, and Civil Service apprenticeships — for a September 2027 start. Use when running the scheduled daily career check, or whenever asked to refresh/update the career watch, produce a digest, or check reading/registration progress.
allowed-tools: WebSearch WebFetch Read Write Edit
---

# Fraser's Career Watch

## What this skill does
Runs a daily check across four tracks so the family stays aware of new openings without manual searching, and keeps a phased reading -> registering -> applying plan on track. Four jobs:
1. **Engineering apprenticeships** - broad Southampton-area sweep (all industries) + named employer watch (Airbus, BAE Systems, QinetiQ, AWE, Dyson Institute, Network Rail) for their September 2027 cycles.
2. **Pilot pathway** - named airline cadet schemes (BA Speedbird, Jet2FlightPath, TUI) + the "First Officer Pilot" apprenticeship standard (ST0523) as and when it appears on GOV.UK.
3. **British American Tobacco** - BAT's UK careers site + aggregator listings, honestly distinguishing school-leaver apprenticeships from graduate/placement programmes.
4. **Civil Service** - the Career Launch apprenticeship scheme + department-level apprenticeships already surfaced by the general GOV.UK sweep.

Then it writes a digest, updates the state files, and (in the GitHub Actions context) that digest gets emailed and the update committed.

## Inputs / settings
- **Search location:** Southampton, 15-mile radius (covers Eastleigh, Fareham, Hythe, Totton, Romsey, Hedge End, Whiteley; note Portsmouth/Waterlooville and IoW sit ~20 miles out).
- **Start dates of interest:** September 2027 primarily; note anything relevant for 2026 too.
- **State files:** `career-watch/state/{engineering,pilot,bat,civil-service}.json` — one JSON array per track of previously-seen opportunities (employer, role, level, location, closing date, link, first-seen date). Read before the sweep, updated after. This is what drives "NEW" vs "already seen" — it replaces the original design's Excel tracker (git-diff-friendly, no binary-merge risk in daily automation).
- **Reading plan:** `career-watch/reading-plan.md` — the phased plan (Phase 1 research/registration, Phase 2 windows open, Phase 3 applications). Check today's date against the phase boundaries and flag in the digest if the phase has just changed.
- **Registration checklist:** `career-watch/registrations.md` — checklist of accounts/alerts Fraser should have set up. Never mark something done on Fraser's behalf — only reflect what's been explicitly confirmed as done.
- **Digest archive:** `career-watch/digests/YYYY-MM-DD.md` — save each day's digest here regardless of whether email sending is available.

## Daily routine - do these in order
1. **Broad sweep** (Track 1 + general). Search GOV.UK Find an Apprenticeship (`https://www.findapprenticeship.service.gov.uk/apprenticeships`) for the location + radius above, keyword blank, all sectors. Capture employer, role, level, town + distance, wage, **closing date**, start date, and apply link for each result. Separately check UCAS (ucas.com/apprenticeships) and Gradcracker for degree-level engineering listings the local sweep might miss.
2. **Named employer watch** (Track 1). For Airbus, BAE Systems, QinetiQ, AWE, Dyson Institute, and Network Rail: check their early-careers pages for whether the September 2027 cycle is open yet, and capture real open/close dates once confirmed. As of the last full run (Aug 2026): Airbus 2027 applications open Oct 2026–Feb 2027; BAE's 2026 cycle opened early Nov 2025 (2027 likely similar, early Nov 2026); Network Rail's 2026 round is closed, register interest for 2027; QinetiQ and Dyson Institute had no confirmed 2027 date yet. Re-verify rather than assume these hold.
3. **Pilot watch** (Track 2). Check British Airways (careers.ba.com/future-pilots and the separate careers.ba.com/apprentices for BA's engineering apprenticeships), Jet2FlightPath, and TUI's cadet scheme pages for open application windows. Separately check GOV.UK Find an Apprenticeship for any live vacancy against the "First Officer Pilot" (ST0523) standard — this is a real, government-approved Level 6 standard (24 months, funded up to £27,000, backed by BA/easyJet/Virgin/BALPA) but no live employer vacancy against it was confirmed as of Aug 2026. Do not assume one exists; state plainly whether one was found.
4. **BAT watch** (Track 3). Check careers.bat.com/en/early-careers and careers.bat.com/en/search-jobs, plus the Gradcracker/Higherin/RateMyApprenticeship BAT profiles. **Explicitly distinguish** apprenticeships (school-leaver entry) from placements/internships (require existing university enrolment — BAT's Southampton R&D site has offered a 12-month undergraduate placement in Packaging Innovation, which is NOT a school-leaver apprenticeship) and graduate schemes (require a completed degree). Never present a placement or grad scheme as an apprenticeship opening.
5. **Civil Service watch** (Track 4). Check civil-service-careers.gov.uk/apprenticeships/career-launch for whether the next cycle has opened (the 2026 window closed with no 2027 date announced as of Aug 2026 — historically these open in autumn). Department-level Civil Service apprenticeships (HMRC, DVSA, MOD, etc.) already surface from the Track 1 broad GOV.UK sweep — no separate search needed for those. Note the scheme's stated eligibility ("16+, not in full-time education") against Fraser's actual situation when a new window opens, rather than assuming it applies cleanly.
6. **Compare to last run.** Load each track's state file, diff against today's results: flag (a) NEW listings not already in the state file and (b) anything **CLOSING within 14 days**. Append newly-seen opportunities to the state file with today's date; don't delete closed ones — keep the historical record, just stop flagging them as new.
7. **Check the phase.** Compare today's date to the phase boundaries in `career-watch/reading-plan.md` and note in the digest if the phase has just changed (e.g. moving from Phase 1 to Phase 2 in autumn 2026).
8. **Write the digest** (format below) and save it to `career-watch/digests/YYYY-MM-DD.md`. Also write a self-contained HTML version to the fixed path `career-watch/digests/latest-email.html` (same content, converted to simple HTML with headings/lists/links — no external CSS or images) so the GitHub Actions workflow can email it without needing to parse markdown itself. Overwrite `latest-email.html` every run; only the dated `.md` file accumulates as history. In the GitHub Actions context, the workflow sends `latest-email.html` to aconduct@proton.me and commits the state/digest updates — this skill just needs to produce accurate content. In an interactive session, offer to send it via a connected email tool if one is available and the user hasn't said otherwise.

## Relevance & prioritisation
- Fraser studies Maths, Physics, Chemistry (A-level) and is interested in engineering degree apprenticeships, pilot training, British American Tobacco, and the Civil Service — but for Track 1 the user wants to see ALL local apprenticeships regardless of industry, so list everything, just sort it well (Degree/Higher first).
- Flag any role requiring the applicant to be **18 by the September start** — several engineering and pilot routes do, and AWE additionally requires British citizenship for security clearance.
- Treat rolling-deadline schemes as "apply now" - the open date is effectively the deadline.

## Digest format
```
Fraser's Career Watch — {date}
Phase: {current phase name} — {one-line description}

TODAY'S FOCUS
- {one reading/registration nudge in Phase 1, or the top priority action once live}

ENGINEERING APPRENTICESHIPS
- NEW THIS WEEK: {employer} - {role} (Level {n}) - {town}, {distance} mi - closes {date} - {link}
- CLOSING SOON: {employer} - {role} - closes {date} - {link}
- TRACKED EMPLOYERS: {employer}: {what changed}

PILOT PATHWAY
- {cadet scheme status changes / ST0523 vacancy check result}

BRITISH AMERICAN TOBACCO
- {new roles, clearly labelled apprenticeship vs placement vs grad scheme}

CIVIL SERVICE
- {Career Launch status / relevant department apprenticeships from the broad sweep}

REGISTRATION STATUS
- {short summary pulled from career-watch/registrations.md}

RECOMMENDED ACTIONS
- {1-3 concrete next steps}
```

## Caveats to state in the digest when relevant
- Confirmed Sept-2027 open/close dates generally publish from ~autumn 2026; before then, any dates shown are based on the prior cycle and should be labelled as such.
- GOV.UK Find an Apprenticeship is England-only (fine for Southampton).
- The ST0523 pilot apprenticeship standard is new - do not assume a live vacancy exists just because the standard does.
- Only report something as an "apprenticeship" if it's genuinely school-leaver entry; label placements and graduate schemes as such, not as apprenticeships.
- Listings change constantly - the digest is a snapshot at run time.
