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

if __name__ == "__main__":
    emp, opps, apps, pilot = load("employers"), load("opportunities"), load("applications"), load("pilot")
    total, live, done, todo = coverage(emp)
    reg_done, reg_total = registrations()
    pc, _ = pipeline(apps)
    boots, mixed, desk = settings(emp)
    print(f"employers {total} (live {live}), dossiers {done}, still to research {len(todo)}")
    print(f"registrations {reg_done}/{reg_total}")
    print(f"pipeline {dict(pc)}")
    print(f"boots {boots} mixed {mixed} desk+lab {desk}")
    print(f"active {sum(1 for e in emp if e['verdict']=='active')}")
    print("\nnext windows:")
    for o in windows(opps, 8):
        print(f"  {pretty_date(o['opens']):20} T{o['tier']} {o['confidence']:12} {o['employer']}")
    print("\nclosing dates on record:")
    for o in closing(opps):
        print(f"  {pretty_date(o['closes']):20} {o['employer']}")
    print("\ndossier files:", ", ".join(dossier_files()))
    if todo:
        print(f"\nSTILL TO RESEARCH ({len(todo)}):", ", ".join(sorted(e['name'] for e in todo)))
