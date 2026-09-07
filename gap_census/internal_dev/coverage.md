# Coverage Report

*Generated 2026-09-06. This file is the answer to "what am I still missing?"*

**Denominator: 279 enumerated ecosystem components.** Every one is accounted for in exactly one status below.

| Layer | none | partial | community | native | n/a | unknown | total |
|-------|---|---|---|---|---|---|---|
| L0 — Silicon, RTOS, Real-Time Control & Functional Safety | 6 | 12 | 3 | 5 | 7 | 2 | 35 |
| L1 — Runtime & Middleware (ROS 2, transport, inference runtime) | 12 | 34 | 2 | 7 | 12 | 0 | 67 |
| L2 — Simulation, Physics & Motion Planning | 8 | 11 | 7 | 0 | 10 | 0 | 36 |
| L3 — Models, Policies & Data (VLA, foundation models, datasets) | 17 | 11 | 4 | 0 | 1 | 2 | 35 |
| L4 — Fleet, MLOps, Observability & Lifecycle | 8 | 8 | 1 | 3 | 25 | 0 | 45 |
| L5 — Certification, Standards & Compliance | 7 | 13 | 0 | 1 | 10 | 1 | 32 |
| L6 — Developer Experience, Distribution & Community | 9 | 12 | 5 | 1 | 2 | 0 | 29 |
| **All** | **67** | **101** | **22** | **17** | **67** | **5** | **279** |

## Status meanings

- `none` — no AMD path
- `partial` — partial / in progress
- `community` — community-maintained only
- `native` — AMD-supported
- `n/a` — not applicable
- `unknown` — UNRESOLVED (coverage debt)

## Completeness: 98.2%

274 of 279 rows resolved to a definite status. 5 remain unknown — listed at the end of `GAP_CENSUS.md`.

Re-running the census means extending `catalog.tsv` with newly shipped components and re-checking `unknown` rows. The denominator grows; the method does not change.

