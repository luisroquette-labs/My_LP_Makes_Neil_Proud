# Dashboard Contract — PLUGGABLE

**Status: implementation out of scope for v2.0.0.** This reference defines the contract only. The dashboard plugs in together with the tracklink repository, in the phase where the systems are graphed and concatenated.

## What the tracklink system exposes

The dashboard consumes nothing until the tracklink system provides:

| Metric | Granularity |
|---|---|
| Clicks per LP | by slug, by day |
| Origin / channel | UTM source, medium, campaign |
| Period | any date range |
| Conversions | leads that reached the thank-you page after a tracked click |

## What the dashboard consumes

| View | Data |
|---|---|
| Issued LP list | all published LPs: slug, model, objetivo, status |
| Clicks | clicks per LP over the selected period, by origin |
| CPL | cost per lead: spend ÷ conversions, when spend data is connected |
| Per-LP status | published / draft / needs review |

## Pluggable rules

- The dashboard reads the tracklink contract (`../publicacao/contrato-tracklink.md`); it never hardcodes a provider.
- Absence of data renders as `Not verified`, never as zero (the blueprint's absence-≠-zero contract applies here too).
- The dashboard is read-only over LP content: it reports on LPs, it does not edit them.

## How to plug it in (future)

1. Tracklink repo ships and implements its contract.
2. The dashboard consumes the exposed metrics.
3. This reference gains an "Implemented by" section pointing at the dashboard implementation.
4. The publication stage's verification grows one item: every published LP appears in the dashboard with its tracking attached.
