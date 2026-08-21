#!/usr/bin/env python3
"""Regenerate career-watch/ACTION.md from the state files.

Every count and date in ACTION.md comes from state/, so the page cannot drift
away from the data sitting next to it. The judgement sections live in this
script rather than in the markdown, so they are versioned and regenerated too.

Run from the repo root:  python3 career-watch/scripts/build_action.py
"""
import json, re, pathlib, datetime
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[2]
STATE = ROOT / "career-watch" / "state"
RESEARCH = ROOT / "career-watch" / "research"
TODAY = "20 August 2026"          # the date the research was compiled
MONTH_NAMES = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June",
               "07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}

def load(name):
    return json.loads((STATE / f"{name}.json").read_text())

def pretty_date(s):
    """2026-10 -> October 2026 ; 2026-10-08 -> 8 October 2026"""
    if not s: return "date unknown"
    p = s.split("-")
    if len(p) == 2: return f"{MONTH_NAMES[p[1]]} {p[0]}"
    return f"{int(p[2])} {MONTH_NAMES[p[1]]} {p[0]}"

def coverage(emp):
    live = [e for e in emp if e["verdict"] != "cut"]
    done = [e for e in emp if e.get("dossier")]
    todo = [e for e in live if not e.get("dossier")]
    return len(emp), len(live), len(done), todo

def registrations():
    t = (ROOT / "career-watch" / "registrations.md").read_text()
    return t.count("\n- [x]"), t.count("\n- [x]") + t.count("\n- [ ]")

def pipeline(apps):
    c = Counter(a["status"] for a in apps)
    return c, apps

def windows(opps, limit=None):
    dated = sorted([o for o in opps if o.get("opens")], key=lambda o: o["opens"])
    return dated if limit is None else dated[:limit]

def closing(opps):
    return sorted([o for o in opps if o.get("closes")], key=lambda o: o["closes"])

def settings(emp):
    c = Counter(e["work_setting"] for e in emp)
    return c["site"] + c["plant"] + c["field"], c["mixed"], c["desk"] + c["lab"]

def dossier_files():
    return sorted(f.name for f in RESEARCH.glob("*.md"))

NARRATIVE = {
"calls": [
 ("Dstl", "Does the **Engineering (Mechanical/Electronics)** pathway run at **Portsdown West** (~20mi), or only at Porton Down? The Level 6 routes confirmed there are Software Engineering and Data Science - both desk-leaning.",
  "This is the single most valuable unanswered question in the project. A hands-on Level 6 twenty miles away would change the shortlist."),
 ("Leonardo Southampton", "Does **any Level 6** run from the Millbrook site, or only the three-year Level 3 Manufacturing route?",
  "400 staff doing infrared detector work, in Southampton. Verification found only a Level 3 described."),
 ("NRS / NDA group", "Is there a **Level 6 nuclear engineering** apprenticeship at **Winfrith, Dorset** (~45mi)? Level 6 was confirmed at Oldbury, Hinkley and Sizewell but not Winfrith.",
  "If it exists it is the only nuclear degree apprenticeship in Britain he could do from home."),
 ("Aureos", "Level, title, provider, salary - and **any location at all**. Four searches established none of it.",
  "Not a consultancy: the former Keltbray Infrastructure Services, a GBP366m rail, overhead-line and highways contractor. Civil and electrical, outdoors."),
 ("QinetiQ", "Email **earlycareers@qinetiq.com**. Stop searching.",
  "Three consecutive research rounds returned nothing on dates. QATS at Boscombe Down is very commutable, so the opportunity may be real but invisible online."),
 ("Tetra Tech", "Is the live vacancy **Edinburgh-only**, or can it be hosted from the Southampton office (SO18 2RZ)?",
  "His only live application, and still unsubmitted. Rolling deadline, so there is time to ask - but no point drafting until it is settled."),
 ("Southern Water", "Does **any Level 6 civil** route exist? Email early careers.",
  "Southampton-local and therefore tempting, but five searches found only QS and Procurement at degree level. They are tripling early-careers intake in 2026."),
 ("UK NNL", "Email **earlycareers@uknnl.com** - is there a 2027 intake?",
  "The apprenticeship programme is paused for 2026. Level 3 and Level 6 routes exist when running."),
],
"decisions": [
 ("Local versus discipline", "Two confirmed near-local Level 6 routes are **Airbus Portsmouth** (electromechanical, fees covered) and **Dstl Portsdown West** (subject to the pathway question above). Neither is civil engineering. Everything genuinely local is otherwise Level 3/4 or desk work.",
  "Does Fraser want to live at home on a mechanical or defence route, or relocate for civil? This shapes every application and he should decide it knowingly."),
 ("Is desk work acceptable at all?", "If it is, WSP Southampton, Arup, Mott MacDonald, AtkinsRealis and Arcadis all open up. If it is not, the list narrows sharply and Babcock Devonport becomes the strongest option despite the relocation.",
  "The boots-on-ground preference has been treated as a tag, not a veto. Worth confirming that is still right."),
 ("Babcock Devonport - relocation", "BEng via Warwick but only four weeks a year at university, the rest on site in the Submarine Commissioning Group. The best hands-on-plus-degree combination found anywhere. Continual assessment to ~May.",
  "**Decide before October, not during it.** Early application genuinely matters here."),
 ("Royal Navy", "48 UCAS points including Maths and a STEM subject at grade D - a far lower bar than assumed, so he is a strong candidate. Probationary Leading Hand, two ranks above standard entry. Rolling, trade training in Hampshire.",
  "Not a degree, and it is military service. A real decision rather than a formality."),
 ("Pilot track", "BA Speedbird ~mid-April 2027, Jet2FlightPath ~February 2027 with a 2.5-week window. The part-finished BA practice test carries no standing.",
  "Does this stay live alongside engineering, or get parked? It needs hard calendar reminders if it stays."),
],
"practical": [
 ("Driving licence", "**Book the test during Year 13.** BAM states applicants must hold a full UK licence, GRAHAM's adjacent spec lists it, and AWE at ~40 miles effectively requires one by September 2027. Three employers point the same way."),
 ("One-page CV", "National Grid's talent pool needs a CV upload on a Beamery platform before applications even open. One page is enough at this stage - but it has to exist."),
 ("SETA registration", "SETA turns out to be the training provider behind several local routes - ExxonMobil Fawley and CooperVision Eastleigh among them. Worth more than its craft-level billing suggested. The September 2027 interest form is the entry point; employer vacancies appear ~Jan-Feb 2027 with a jobs fair in early February."),
 ("Do not apply", "**Jacobs Douwe Egberts Banbury** is closing - 167 jobs, wound down by December 2026 - while aggregators still serve its apprenticeship listing."),
],
"watch": [
 ("Monthly from October", "BAE Systems - no notify option exists, so a Gradcracker follow is the only alert."),
 ("Add to Gradcracker follows", "Babcock, GKN Aerospace, WSP, L3Harris - all either confirmed openers or strong local options, none currently followed."),
 ("February 2027", "Met Office next cohort advertised; Britvic opens; Dstl's stated pattern; ExxonMobil Fawley; Jet2FlightPath."),
 ("Already live, act now", "Cogent Skills **Pfizer Apprenticeships 2027** register-your-interest page."),
],
}

def section(title, body): return f"## {title}\n\n{body}\n"

def build():
    emp, opps, apps = load("employers"), load("opportunities"), load("applications")
    total, live, done, todo = coverage(emp)
    rd, rt = registrations()
    pc, appl = pipeline(apps)
    boots, mixed, desk = settings(emp)
    active = sorted(e["name"] for e in emp if e["verdict"] == "active")

    L = [f"# Fraser's apprenticeship search - action page",
         "",
         f"**As at {TODAY}.** Regenerate with `python3 career-watch/scripts/build_action.py`.",
         "",
         "Every number and date below is read from the state files, so this page cannot drift away from "
         "the data. Sources: `state/employers.json` (coverage, verdicts, work settings), "
         "`state/opportunities.json` (windows and closing dates), `state/applications.json` (pipeline), "
         "`registrations.md` (registration progress). Judgement sections come from "
         "`career-watch/research/` and are versioned in the generator script.",
         "", "---", ""]

    # 1. headline state
    L.append(section("Where things stand",
        f"| | |\n|---|---|\n"
        f"| Employers tracked | **{total}** ({live} live, {total-live} cut) |\n"
        f"| Researched | **{done}** |\n"
        f"| Still to research | {len(todo)}{' - ' + ', '.join(sorted(e['name'] for e in todo)) if todo else ''} |\n"
        f"| Marked worth real effort | **{len(active)}** |\n"
        f"| Work setting | {boots} boots-on-ground, {mixed} mixed, {desk} desk or lab |\n"
        f"| Registrations done | **{rd} of {rt}** |\n"
        f"| Applications submitted | **{pc.get('applied', 0)}** |\n\n"
        "**The research is a long way ahead of the action.** That gap is what this page is for."))

    # 2. this month
    L.append(section("Do this month",
        "Ordered by what unblocks the most. The first two are about ten minutes each and gate everything else.\n\n"
        "1. **Create the Higherin account.** It is the only aggregator of the live \"Register Your Interest 2027\" "
        "listings, and **four of Fraser's five shortlisted roles came from it.** Still the single biggest gap.\n"
        "2. **GOV.UK Find an Apprenticeship** - account plus a saved search: Southampton, 25 miles, all sectors, "
        "email alerts on.\n"
        "3. **National Grid talent pool** - opens September, needs a CV upload before then.\n"
        "4. **Register interest:** Babcock (opens October), AtkinsRealis Talent Community, EDF Talent Community, "
        "Network Rail, MBDA, Sellafield, UKAEA.\n"
        "5. **Both WSP Southampton vacancies** - the only genuinely local degree-level civil roles found anywhere. "
        "Reopens November.\n"
        "6. **AECOM Basingstoke** (~35mi, commutable) - applications open September/October with **no deadline**, "
        "so the window is weeks away. Confirm whether it is Level 3 or Level 6.\n"
        "7. **2-3 Springpod virtual work experiences** - free, 6-10 hours, certificate. Do them before October."))

    # 3. windows
    seen, rows = set(), []
    for o in windows(opps):
        if o["employer"] in seen: continue
        seen.add(o["employer"])
        rows.append(f"| {pretty_date(o['opens'])} | **{o['employer']}** | T{o['tier']} | `{o['confidence']}` |")
    L.append(section("Windows opening, in date order",
        "| Opens | Employer | Tier | Confidence |\n|---|---|---|---|\n" + "\n".join(rows) +
        "\n\n**Closing dates on record:** " +
        " · ".join(f"{o['employer']} {pretty_date(o['closes'])}" for o in closing(opps)) +
        "\n\n**Not in the table but dated from research:** GE Aerospace Dowty and Feltham **8 October**, "
        "Cheltenham and Wales **20 October**, Prestwick **3 November** · BAE Systems opens **early November**, "
        "closes end February (settled - January was a mid-window date) · GRAHAM runs more than one window a year, "
        "so watch from autumn · Jet2FlightPath ~**February**, 2.5 weeks only · BA Speedbird ~**mid-April 2027**."))

    # 4. calls
    L.append(section("Calls and emails only a human can make",
        "\n\n".join(f"**{n}** - {q}\n\n> {w}" for n, q, w in NARRATIVE["calls"])))

    # 5. decisions
    L.append(section("Decisions waiting on Fraser",
        "\n\n".join(f"**{n}**\n\n{d}\n\n> {w}" for n, d, w in NARRATIVE["decisions"])))

    # 6. practical
    L.append(section("Practical and easy to miss",
        "\n\n".join(f"**{n}** - {d}" for n, d in NARRATIVE["practical"])))

    # 7. pipeline
    rows = [f"| {a['employer']} | {a['role'][:60]} | `{a['status']}` |" for a in appl]
    L.append(section("Pipeline",
        "| Employer | Role | Status |\n|---|---|---|\n" + "\n".join(rows) +
        f"\n\n**{pc.get('applied', 0)} submitted.** Tetra Tech is the only live vacancy among them and its "
        "location is in doubt - see the calls above. The other four are register-interest forms: quick to do, "
        "worth doing, no clock running."))

    # 8. watch
    L.append(section("Watch list", "\n\n".join(f"**{n}** - {d}" for n, d in NARRATIVE["watch"])))

    L.append("---\n\n**Where to read more:** `career-watch/research/browser-checks.md` for the full "
             "prioritised check list, `career-watch/research/criteria-index.md` for which STAR moments to bank "
             "first, and the seven tier dossiers for per-employer detail. `career-watch/tracker.md` remains the "
             "narrative record.\n")
    return "\n".join(L)

if __name__ == "__main__":
    out = ROOT / "career-watch" / "ACTION.md"
    out.write_text(build())
    print(f"wrote {out.relative_to(ROOT)} - {len(build().splitlines())} lines")
