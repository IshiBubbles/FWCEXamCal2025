# Company research dossiers

Compiled from **20 August 2026**. One file per tier, mirroring `state/employers.json`.

These exist for one purpose: so that when Fraser fills in an application form or sits in an
interview, he can demonstrate that he has actually researched the company. Every entry is
written to be quotable more or less straight into an application.

| File | Covers | Status |
|---|---|---|
| `browser-checks.md` | **Start here.** The prioritised action list — what to open in a real browser, and which decision it unblocks | live |
| `tier1-civil.md` | Civil and infrastructure — his #1 discipline | ✅ 50 of 50 |
| `tier2-chemical.md` | Heavy process and refining, plus the two local sub-degree options | ✅ 16 of 16 |
| `tier2-electrical.md` | Power, grid, energy | ✅ 22 of 22 |
| `criteria-index.md` | Every stated person-spec criterion, ranked by how many employers ask for it | 88 employers |
| `tier3-mechanical.md` | Mechanical, automotive, aerospace, defence | ✅ 29 of 29 |
| `tier2-pharma-food.md` | Pharma, food and FMCG manufacturing | ✅ 21 of 21 |
| `nuclear.md` | Nuclear sector | ✅ 14 of 14 |
| `other.md` | Defence science, military, civil service, diversified | ✅ 20 of 20 |

**The master list is complete — every non-cut employer has a dossier.** 160 entries across seven
files, 494 stated criteria indexed. Three new employers were found incidentally during the final
round and are the only ones still to research: **ABP Southampton**, **DP World Southampton** and the
**University of Portsmouth / BAE Systems Space Systems Engineering** degree apprenticeship. All
three are local, which is why they matter.

**The headline finding across all four rounds:** local, degree-level and hands-on almost never
coexist — but they do in two, possibly three, places.

| Confirmed near-local Level 6 | Distance | Note |
|---|---|---|
| **Airbus Defence & Space, Portsmouth** | ~20mi | Electromechanical route; Airbus covers all fees |
| **Dstl, Portsdown West** | ~20mi | Four named Level 6 programmes; entry requirement a literal match |
| *University of Portsmouth / BAE Systems, Space Systems* | ~20mi | Newly found, not yet researched |

Everything else local is Level 3/4 or desk work: WSP Southampton, Arup, ExxonMobil Fawley, SETA,
SSEN, Siemens Southampton, Roke, Colas Rail Eastleigh, Leonardo Southampton, Boeing Middle Wallop,
CooperVision Eastleigh. **SETA turns out to be the provider behind several of them**, which makes
registering with SETA worth more than its craft-level billing suggested.

Two other things the research changed: **Babcock Devonport** is the best hands-on-plus-degree
combination found anywhere (BEng via Warwick, but only four weeks a year at university), and the
**Royal Navy Accelerated Apprentice** bar is 48 UCAS points, not the 120 previously assumed.

The 43 companies marked `cut` in `employers.json` are deliberately not researched. IChemE is a
professional body rather than an employer, so it has no dossier.

## How to use an entry

**What they do** and **What they're working on now** are the "I've researched you" content —
the second one especially, because named live projects are what separate a real application
from a template. Dates matter: a project that was live in August 2026 may have finished by the
time Fraser applies, so re-check before quoting.

**Stated criteria** is the bridge to the STAR bank. These are the employer's own person-spec
bullets, and the wording is the point — see the provenance note below. `criteria-index.md`
aggregates them across all employers so you can see which qualities are in demand everywhere
and bank evidence for those first.

**Why them — the hook** is one specific detail for a covering letter's closing paragraph. Each
one is written to fail a swap test: dropped into another company's letter it should read as
obviously wrong.

**Work setting** records whether the role is genuinely site-based, because Fraser wants to be
on site rather than at a desk.

## Provenance tags — read this before quoting any criterion

Every bullet under **Stated criteria** carries a tag, and it changes what you can do with it:

| Tag | Meaning | Use |
|---|---|---|
| `[verbatim]` | The employer's actual quoted wording | Safe to mirror in an application |
| `[paraphrased — snippet only]` | The gist, from a search snippet; wording unconfirmed | Treat as a hint. **Do not quote back at them** |
| `[not found — needs a browser check]` | Could not be established | Open the page and paste the real bullets in |

An untagged bullet is a bug, not a formatting slip — untagged means unknown origin, and unknown
origin is indistinguishable from invented.

## The method, and its limit

Research is by web search only. The network proxy in this environment blocks direct page loads
for essentially every corporate careers domain, so everything here comes from search-result
snippets quoting those pages rather than from reading the pages themselves. Snippets can be
cached and stale.

This bites hardest on **Stated criteria**, because person-spec bullets live on the
apprenticeship page itself. Each tier file therefore ends with a **Browser-check list**: pages
worth opening in a normal browser to paste the real wording in. Ten minutes of copying is worth
more than a hundred paraphrases.

Two rules were applied throughout:

- **Nothing is invented.** No project, contract, partner university, salary or entry
  requirement appears here unless it was actually found. A wrong specific is worse than a
  missing one, because it gets quoted into an application and then probed at interview.
- **"Not found" is a real answer.** Several smaller employers have little findable presence and
  may run no apprenticeship at all. Those entries say so, with what was searched. That is
  useful — it tells Fraser where not to spend his time.
