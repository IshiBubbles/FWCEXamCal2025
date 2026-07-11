# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is not a software project — it is a personal family calendar maintained as
plain-text iCalendar (`.ics`) data under git version control. There is no build
system, no tests, no linter, and no application code. "Development" here means
editing the two `.ics` files by hand and committing the result.

## Files

- `Exam_Timetable_2025.ics` — the master/combined calendar. Contains the full
  shift rotation (Shift A/B/C) plus every other personal event: exams, school
  term dates, birthdays, appointments, trips, flights, coach tickets, sports
  fixtures, etc. This is the file that gets imported into a real calendar app.
- `Shift_Pattern.ics` — a standalone copy of just the work shift rotation
  (`Shift A`, `Shift B`, `Shift C` VEVENTs), covering the same date range as
  the shift entries inside `Exam_Timetable_2025.ics`. It was originally a
  separate calendar and was merged into `Exam_Timetable_2025.ics` (see commit
  `1fe88e0`), but it is kept around as the source record for the shift roster.
  When the shift pattern changes, update both files so they stay in sync.

Both files currently span the same overall date range: **2025-03-21 to
2027-12-30**.

## File format conventions

Follow the existing style exactly when adding or editing events — don't
"clean up" or reformat unrelated parts of the file.

- Each event is a flat `BEGIN:VEVENT` / `END:VEVENT` block with, typically:
  `SUMMARY`, `DTSTART`, `DTEND`, `DESCRIPTION`, and optionally `LOCATION`.
- No `UID` and no `RRULE` are used anywhere in either file. Recurring things
  (like shifts) are **fully expanded**: one `VEVENT` per individual
  occurrence, not a recurrence rule. When adding new shift dates, add
  individual `VEVENT` blocks in the same enumerated style rather than
  introducing an `RRULE`.
- Timed events use `DTSTART;TZID=Europe/London:YYYYMMDDTHHMMSS` /
  `DTEND;TZID=Europe/London:...` (or `Africa/Nairobi` for the Kenya flight
  legs). All-day events use `DTSTART;VALUE=DATE:YYYYMMDD` /
  `DTEND;VALUE=DATE:YYYYMMDD` (end date is exclusive per the iCalendar spec,
  e.g. a trip ending the 29th has `DTEND;VALUE=DATE:20260729`).
- `SUMMARY` is a short human title, often prefixed with the person's name
  (e.g. `Imma - Kenya Trip`, `Dentist - Fraser`, `Parents Evening - Fraser
  Physics`). `DESCRIPTION` repeats/expands the summary in a full sentence and
  is where extra detail lives (ticket numbers, flight routing, venue notes).
- The shift rotation (`Shift_Pattern.ics` and the shift entries in
  `Exam_Timetable_2025.ics`) follows a repeating ~3-week cycle: 7 days of
  Shift A, days off, 5 days of Shift B, days off, 2 days of Shift C, days
  off, then repeats. Each shift day is `08:00–09:00` Europe/London. Preserve
  this cadence when extending the roster into new date ranges.
- Files are plain LF line endings (not CRLF, despite RFC 5545 nominally
  calling for CRLF) — keep it consistent with the rest of the file.
- `Exam_Timetable_2025.ics` has no `PRODID` line; `Shift_Pattern.ics` has
  `PRODID:-//Shift Pattern//EN`. Don't add a `PRODID` to
  `Exam_Timetable_2025.ics` unless asked.

## Validating changes

There is no tooling in this repo to validate `.ics` files — a malformed
`VEVENT` block has previously been committed and had to be fixed later (see
commit `cca3eca`, "Fix malformed VEVENT missing BEGIN:VEVENT line"). Before
committing, sanity-check by hand (or with a quick shell command) that:

- Every `BEGIN:VEVENT` has a matching `END:VEVENT`, and there is exactly one
  `BEGIN:VCALENDAR` / `END:VCALENDAR` pair at the top and bottom of the file.
- New/edited events use plausible, non-overlapping dates and times, and use
  the correct `TZID` for the location involved.

Example check:
```
grep -c 'BEGIN:VEVENT' Exam_Timetable_2025.ics
grep -c 'END:VEVENT' Exam_Timetable_2025.ics
```
These two counts must match.

## Commit conventions

Commit messages are short, imperative, and describe the calendar change in
plain English, usually naming the event and its date/time, e.g.:

- `Add Quinn Kestrels Welcome at Itchen College 5 Sep 2026 12:00-15:30`
- `Fix Springhill School Holidays Begin: 23 Jul -> 17 Jul 2026`
- `Update dentist appointment times`

Follow this style: one commit per logical calendar change (adding an event,
fixing a date/time, merging a source file), with the summary line stating
what changed and, for adds/fixes, the relevant date(s).
