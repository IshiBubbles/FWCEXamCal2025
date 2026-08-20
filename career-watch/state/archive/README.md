# Archived state files

Superseded on 20 August 2026 when the three Fraser skills were consolidated into
`fraser-career` and the data moved to a three-layer model (`employers.json` ->
`opportunities.json` -> `applications.json`).

Kept rather than deleted because each represents real verification work whose
reasoning is worth being able to re-read.

| File | Why it was archived |
|---|---|
| `engineering.json` | Fully migrated into `opportunities.json`, which adds `tier`, `discipline`, `source` and a machine-readable `confidence` field, and normalises the `opens` granularity. |
| `bat.json` | BAT was verified in August 2026 to run no UK school-leaver apprenticeship. It survives as a single `not_a_route` row in `employers.json` with the full reasoning. |
| `civil-service.json` | The two entries that are genuinely engineering apprenticeships (Dstl, GCHQ) plus MOD/SDA and Fast Track moved into `opportunities.json`. Career Launch is blocked by its "not in full-time education" rule and survives as a `watch` row in `employers.json`. |

Do not read these for current state. They are history.
