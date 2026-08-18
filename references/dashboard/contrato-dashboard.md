# Dashboard Contract — PLUGGABLE

**Status: the exposure contract now exists.** [My_UTMs_Make_Me_Proud](https://github.com/luisroquette/My_UTMs_Make_Me_Proud) (v1.0.0) shipped, and its `references/nucleo/metricas.md` defines what the tracking system exposes. The dashboard implementation itself remains out of scope for this repo — it plugs into that contract.

## What the tracklink system exposes

Defined by the tracklink repo (`references/nucleo/metricas.md` of My_UTMs_Make_Me_Proud):

| Metric | Granularity |
|---|---|
| Clicks per link | by slug, by day (daily aggregate + granular events) |
| Origin / channel | UTM source/medium/campaign, snapshot at click time |
| Period | 7/30/90 days, calendar-filled series — absence is never zero |
| Conversions | first/last click ids recorded at lead forms and checkouts |
| Link status | active / paused / expired / broken (health columns) |

## What the dashboard consumes

| View | Data |
|---|---|
| Issued LP list | all published LPs: slug, model, objetivo, status |
| Clicks | clicks per LP over the selected period, by origin |
| CPL | cost per lead: attributable spend ÷ **valid leads** (see auditoria/metrics.md — conversions is a different metric), when spend data is connected |
| Per-LP status | published / draft / needs review |

## Pluggable rules

- The dashboard reads the tracklink contract (`../publicacao/contrato-tracklink.md`); it never hardcodes a provider.
- Absence of data renders as `Not verified`, never as zero (the blueprint's absence-≠-zero contract applies here too).
- The dashboard is read-only over LP content: it reports on LPs, it does not edit them.

## How to plug it in (future)

1. ✅ Tracklink repo shipped (v1.0.0): My_UTMs_Make_Me_Proud — the exposure contract lives in its `references/nucleo/metricas.md`.
2. The dashboard consumes the exposed metrics.
3. This reference gains an "Implemented by" section pointing at the dashboard implementation.
4. The publication stage's verification grows one item: every published LP appears in the dashboard with its tracking attached.
