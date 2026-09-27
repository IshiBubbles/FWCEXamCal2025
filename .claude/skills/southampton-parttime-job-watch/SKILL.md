---
name: southampton-parttime-job-watch
description: Daily watch for new part-time retail, supermarket, and fast-food/hospitality job listings within 15 miles of Southampton SO15, for a student job search. Use when running the scheduled daily job check, or whenever asked to refresh the job tracker or produce a job-alert digest.
---

# Southampton Part-Time Job Watch

## What this skill does
Runs a daily check so Adam (a student in SO15, Southampton) stays aware of new part-time job openings without manually re-checking each employer's careers site. It has two tiers:
1. **Indeed sweep** - the primary daily source, via the connected `mcp__Indeed__search_jobs` tool.
2. **Named-employer watch** - check specific high-street employers' own careers sites directly, for any brand Indeed doesn't cover well.

Then it writes a short daily digest to a markdown file, attempts to email it, and updates the tracker.

**Note on history:** An earlier version of this skill, its tracker, and digests lived under `/root`, outside the git repo, and were lost in a session container reset (2026-09-13). Everything was rebuilt and moved into this project's git repo (`parttime-job-watch/`) on 2026-09-27 so it survives future resets - commit changes to the tracker and digests as part of the normal workflow, the same way `career-watch/` is handled.

## Inputs / settings (defaults - adjust if Adam says otherwise)
- **Tracker file:** `parttime-job-watch/Southampton_PartTime_Jobs_Tracker.xlsx` (relative to the project root).
- **Digest folder:** `parttime-job-watch/digests/Job-Digest-YYYY-MM-DD.md` (relative to the project root).
- **Search location:** SO15, Southampton.
- **Radius:** 15 miles.
- **Role type:** part-time only; no minimum-hours, shift-time, or age filter unless Adam asks for one.
- **Sectors:** retail, supermarkets, fast-food/hospitality, and cinema/leisure (not restricted to the list below - the Indeed sweep should surface others too).
- **Named employers (with URLs, so Adam can check the source himself):**
  - West Quay jobs hub: https://westquayretail.com/jobs/ (index page linking to in-centre vacancies, e.g. https://westquayretail.com/jobs/boots-various-positions/, https://westquayretail.com/jobs/matalan/)
  - Boots: https://www.boots.jobs/
  - Matalan: https://www.matalancareers.co.uk/
  - Asda: https://www.asda.jobs/jobs?postcode=southampton&distance=15
  - Tesco: https://careers.tesco.com/en_GB/careers/SearchJobs
  - Sainsbury's: https://www.sainsburys.jobs/jobs?full_time=&part_time=&filter_by=&location=southampton&keywords=
  - McDonald's: https://careers.mcdonalds.com/uk/
  - Domino's: https://www.dominosjobs.co.uk/
  - Costa: https://www.costa.co.uk/careers
  - Starbucks: https://www.starbucks.co.uk/careers
  - Greggs: https://careers.greggs.co.uk/
  - Showcase Cinemas: https://www.showcasecinemas.co.uk/jobs/ (vacancies list: https://newcareer.showcasecinemas.co.uk/vacancies)
  - Vue Cinemas: https://careers.myvue.com/jobs (South England cinema jobs: https://careers.myvue.com/cinema-jobs-in-south-england)
  - IKEA: https://jobs.ikea.com/en/search-jobs (Southampton store listing: https://jobs.ikea.com/en/location/southampton-england-united-kingdom-jobs/22908/2635167-6269131-2637487/4 - IKEA Southampton is on West Quay Road, right in Adam's area)
  - Lidl: https://careers.lidl.co.uk/search-results
  - Iceland Foods: https://careers.icelandfoods.co.uk/
  - Hollywood Bowl: https://careers.hollywoodbowlgroup.co.uk/job-search?places_position=50.90489%2C-1.40431&places_query=Southampton%2C%20Hampshire%2C%20England#search-results (Southampton pre-filtered)
- **Excluded employers (do not search or list, per Adam's preference):**
  - **KFC** - Adam isn't interested in working there (doesn't like chicken). Skip KFC entirely in both the Indeed sweep and named-employer checks - don't search for it, and don't include any KFC results even if they surface incidentally in a broader search.
- **Coverage tiering (re-check periodically, update this list as Indeed's index changes):**
  - **Required (check the employer's own site every run - Indeed is thin/empty for these):** Boots, Matalan, Sainsbury's, McDonald's, Showcase Cinemas, Vue Cinemas, IKEA, Hollywood Bowl.
  - **Secondary (Indeed shows decent Southampton-area coverage - spot-check the site every few runs instead):** Tesco, Asda, Domino's, Costa, Greggs, Lidl, Iceland Foods.
- **Delivery:**
  - **Primary (always works):** write the digest to a dated markdown file, `parttime-job-watch/digests/Job-Digest-YYYY-MM-DD.md`, every run.
  - **Secondary (best-effort):** also try to email the digest via the Microsoft 365 Outlook mail tools available in this environment (`mcp__Microsoft_365__outlook_create_draft` + `mcp__Microsoft_365__outlook_send_draft`), from the connected mailbox to **aconduct@proton.me**. Before calling the send tool, state the recipient, subject, and a one-line summary in chat first. If the send fails, note that in the digest file and continue - never block the run on the email leg.
  - Runs (and attempts the email) every day regardless of whether anything new was found.

## Daily routine - do these in order
1. **Confirm Indeed is connected and enabled in this chat** before starting (check with the connectors tool) - don't run a partial sweep silently if it's off.
2. **Indeed sweep.** Call `mcp__Indeed__search_jobs` for "part time" roles within 15 miles of SO15 Southampton, across retail/supermarket/fast-food/hospitality, plus one search per named employer (skip KFC). For each result capture: employer, role title, branch/location, distance from SO15, part-time hours if stated, pay if listed, closing/application date if listed, and the apply link.
3. **Named-employer watch.** For each employer flagged as "Required" above, also try to check its careers site directly if network access allows (it has historically been blocked by this environment's egress proxy - if so, note that in the digest rather than silently skipping).
4. **Compare to the tracker.** Diff against the "Tracker" sheet, keyed on employer + role + branch/location (Indeed regenerates a new tracking link on every query, so link alone is not a reliable dedup key). Flag:
   - **NEW** - listings not already in the tracker.
   - **CLOSING SOON** - any listing with a stated closing/application date within 7 days.
5. **Update the tracker** (use the xlsx skill / openpyxl):
   - Append newly seen listings to the "Tracker" tab.
   - Keep a dated log of each day's full sweep on a sheet named `Live Log` (create it if absent; append a new block each day with the run date and a short summary).
   - Do not overwrite any "STATUS (yours)" column Adam maintains himself.
6. **Write the digest** (see format below) to `parttime-job-watch/digests/Job-Digest-YYYY-MM-DD.md`. Then attempt the best-effort email to aconduct@proton.me. Do this every day, even when there is nothing new - on quiet days the digest just says so.

## Digest format
```
Southampton Part-Time Job Watch - {date}

NEW TODAY (within 15 miles of SO15)
- {Employer} - {Role} - {Branch/Town}, {distance} mi - {hours if known} - closes {date or "not stated"} - {link} (source: {Indeed / employer site name})

CLOSING SOON (next 7 days)
- {Employer} - {Role} - {Branch/Town} - closes {date} - {link}

NO NEW LISTINGS TODAY
(shown instead of the above section when the sweep found nothing new)

GAPS THIS RUN
- {employers with zero/thin Indeed results, still needing a direct site check}

RECOMMENDED ACTIONS
- {1-3 concrete next steps, e.g. "Apply to Sainsbury's Burgess Road today - closing soon"}

DELIVERY NOTE
- {confirm whether the email to aconduct@proton.me sent successfully, or note the failure - the md file above is always the source of truth}
```

## Caveats to state in the digest when relevant
- Listings and closing dates can change or be pulled at any time - the digest is a snapshot at run time.
- Some employer sites (e.g. Matalan) may only ever show one or two live roles at a time in Southampton - that's expected, not a search failure.
- If a site blocks automated fetches or requires JavaScript rendering that can't be retrieved, note it in the digest rather than silently omitting that employer.
- If the email leg fails, say so plainly in the digest's DELIVERY NOTE - Adam should always check the md file if the email doesn't arrive.
- The tracker and digests now live in this project's git repo (`parttime-job-watch/`), so commit changes after each run rather than leaving them uncommitted, to protect against session resets.

## Scheduling note
This skill is intended to run daily via a scheduled prompt (e.g. `CronCreate`). In this environment, scheduled jobs are session-bound: they only fire while a Claude session stays open/idle, and auto-expire after 7 days. Treat "daily" as best-effort while a session is active - re-arm the schedule when starting a new session, or use the `/loop` skill to keep it self-pacing during an active session. True always-on scheduling independent of any open session would need an external scheduler outside this environment.
