# Metrics and experimentation

## Operational metrics

| Metric | Formula | Interpretation |
|---|---|---|
| Unique visitors | distinct people in the period | Volume only; not effectiveness |
| Conversion rate | `conversions / unique visitors × 100` | Completion of the primary action |
| CTA CTR | `CTA clicks / page views × 100` | Movement from promise to action |
| CPL | `attributable spend / valid leads` | Lead acquisition cost |
| Bounce rate | `visits without action / total visits × 100` | Possible mismatch, confusion, or performance issue; context required |

S3 includes didactic examples of 1,200 visitors, 28% conversion, 42% CTA CTR, BRL 7 CPL, and 65% bounce. Never use these values as targets or benchmarks.

For `scripts/calculate_score.py`, use `unique_visitors`, `conversions`, `page_views`, `cta_clicks`, `attributable_spend`, `valid_leads`, `visits_without_action`, and `total_visits`. The legacy aliases `spend`, `leads`, `bounces`, and `visits` are also accepted.

```json
{
  "scores": {"offer": 4.5, "cta_focus": 4},
  "not_applicable": [],
  "metrics": {
    "unique_visitors": 1200,
    "conversions": 336,
    "page_views": 1200,
    "cta_clicks": 504,
    "attributable_spend": 2352,
    "valid_leads": 336,
    "visits_without_action": 780,
    "total_visits": 1200
  }
}
```

Omitted score criteria remain unscored. Use `not_applicable` only for structural inapplicability. The script keeps applicable weight, scored weight, and coverage separate.

When available, add form abandonment, lead quality, sales, and revenue. These support the guides' customer-conversion objective but are not explicit metrics in S3's metrics block.

## Combined interpretation

- High CTA CTR and low conversion: inspect form friction, trust, technical error, or post-click mismatch.
- Low CTA CTR: inspect offer, headline, CTA, proof, and hierarchy.
- High conversion and low lead quality: inspect promise, segmentation, and qualification.
- High bounce: inspect channel match, clarity, speed, and mobile.
- CPL matters only alongside quality and business outcomes.

Label these as likely diagnoses, not confirmed causation.

## A/B tests

The guides recommend testing length, templates, CTA wording, position, and color.

1. Fix obvious defects and broken flows first.
2. Tie one hypothesis to one metric.
3. Change one primary variable when possible.
4. Keep audience, source, and offer comparable.
5. Declare a winner only with adequate sample size and duration supplied by the user or platform.

```text
Hypothesis: changing X to Y should improve metric Z because source principle.
Control: current version.
Variation: one concrete change.
Primary metric: conversion or CTA CTR.
Guardrail: CPL, quality, bounce, or sale.
```

## Historical claims

Historical figures in the sources include testimonial, imagery, carousel, page-length, color, and video cases. They come from different third parties, dates, audiences, and traffic sources. Use them only as labeled context: never sum their effects, transfer their lift, or subtract points because a page does not copy the tested element.

## Rules of use

- Separate observed metric, historical example, and hypothesis.
- Report period, denominator, traffic source, and conversion definition when available.
- Never call an article example a Neil Patel benchmark.
- Never claim causation from correlation.
- Never propose A/B tests without functional measurement.

