---
name: my-lp-makes-neil-proud
description: Audit third-party landing pages with a 0-100 adherence score, launch-readiness status, evidence, and prioritized fixes strictly traceable to three user-provided Neil Patel guides. Use when auditing, reviewing, approving, rejecting, or comparing a landing page from a URL, screenshot, HTML, copy, prototype, or metrics; covers objective, intent, offer, AIDA, headline, benefits, CTA, simplicity, form, social proof, images, UX, mobile, SEO, privacy, tracking, post-conversion, and A/B tests.
---

# Audit landing pages against the supplied guides

Apply only criteria traceable to the three source documents. Treat the score as an operationalization of the guides, not an official Neil Patel methodology.

## Load the references

Before the first audit in a conversation, read these files completely and in this order:

1. [references/source-map.md](references/source-map.md) — origin and scope of each rule;
2. [references/framework.md](references/framework.md) — principles and contextual decisions;
3. [references/rubric.md](references/rubric.md) — criteria, weights, and readiness;
4. [references/metrics.md](references/metrics.md) — formulas, interpretation, and historical claims.

If the three original snapshots are available, run `python3 scripts/verify_sources.py`. On `mismatch`, reread the changed source and update the references before auditing. A `missing` file does not block use of the documented snapshots in `source-map.md`.

## Establish context

Identify:

- page type: pre-launch, lead capture, sales, or thank-you;
- single conversion objective and expected action;
- persona, pain, intent, funnel stage, and requested commitment;
- offer, traffic source, and pre-click promise;
- primary device, channel, deadline, and available metrics;
- publication domain, responsible identity, and alignment among brand, URL, and offer.

When data is missing, proceed with declared assumptions. Ask one short question only when the absence prevents a useful evaluation.

## Inspect without converting

For a live URL:

1. inspect desktop and mobile;
2. inspect promise, content, hierarchy, images, CTA, links, form, and post-conversion path;
3. verify technical behavior without creating a lead;
4. inspect SEO, tracking, HTTPS, and data transparency when accessible.

Do not submit a form, buy, publish, or change the page without explicit authorization. Label every finding as:

- `Confirmed`: directly observed or tested;
- `Inferred`: contextual conclusion with its basis stated;
- `Not verified`: requires analytics, traffic-source context, credentials, or a real conversion.

## Score adherence

1. Apply the twelve criteria in [references/rubric.md](references/rubric.md).
2. Score each criterion from 0 to 5 in 0.5 increments.
3. Use `N/A` only when structurally inapplicable. Missing data is `Not verified`, not `N/A`.
4. Run `python3 scripts/calculate_score.py --input <json>` to calculate the score and supplied metrics.
5. Report coverage, excluded weight, and confidence. Treat a score below 100% coverage as provisional.
6. Cite at least one source identifier `[S1]`, `[S2]`, or `[S3]` in each priority fix.

Keep the **adherence score** separate from **launch readiness**. A page may follow visual principles and still be unready because the CTA or form does not deliver the conversion.

## Handle contextual rules correctly

- Never require a short or long page by default. Relate length to risk, commitment, and traffic temperature.
- Never require video. Evaluate whether it explains, demonstrates, retains attention, or builds trust.
- Never choose a universal winning color. Evaluate contrast, harmony, brand, and tested results.
- Never require exactly two fields. Ask only for what is necessary and proportional to the offer, persona, and funnel stage.
- Never remove every menu automatically. Reduce pre-conversion distraction; allow useful navigation on thank-you pages.
- Never present article percentages as a benchmark, forecast, or guarantee.

## Required output

Start with:

```markdown
Adherence score: 00/100 — high|medium|low confidence — 00% coverage
Readiness: ready | ready with corrections | not ready
Biggest lever: one sentence
```

Then present, in this order:

1. a table of all twelve criteria: weight, score, points, evidence state, and source;
2. up to five fixes in `P0/P1/P2` format: `problem → evidence → impact → correction → source`;
3. calculated real metrics and interpretation, when provided;
4. up to three unverified items that could change the conclusion;
5. up to three A/B hypotheses only after obvious defects are fixed and measurement is sufficient.

Never promise lift. Distinguish historical example, hypothesis, and observed result. Never praise without evidence.
