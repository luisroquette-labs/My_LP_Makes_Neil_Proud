# My_LP_Makes_Neil_Proud

**Turn any landing page into an evidence-backed conversion audit — scored, prioritized, and ready to act on.**

Audit a live URL, screenshot, HTML file, copy draft, or prototype with a 12-criterion rubric derived from three Neil Patel landing-page guides. Get a 0–100 adherence score, a separate launch-readiness decision, and up to five prioritized fixes.

[Download the skill](https://github.com/luisroquette/My_LP_Makes_Neil_Proud/archive/refs/heads/main.zip) · [Install for Codex](#install) · [See the rubric](references/rubric.md)

> Independent open-source implementation. The score and weights are an operationalization of the cited guides, not an official Neil Patel or NP Digital methodology. This project is not affiliated with or endorsed by Neil Patel or NP Digital.

## Why use it

Most landing-page reviews collapse into taste: change the button color, shorten the page, add testimonials. This skill forces every important claim to answer four questions:

| Question | What the audit returns |
|---|---|
| What is actually wrong? | A specific, observable finding |
| How serious is it? | `P0`, `P1`, or `P2` priority |
| What should change? | A concrete correction |
| Why does it matter? | A traceable source identifier |

## What you get

- **0–100 adherence score** across 12 weighted conversion criteria
- **Launch readiness** kept separate from visual or copy quality
- **Evidence labels:** Confirmed, Inferred, or Not verified
- **Coverage and confidence** so unknown data never becomes a fake zero
- **Metrics calculator** for conversion rate, CTA CTR, CPL, and bounce rate

## The 12-point audit

| Criterion | Weight | Decision |
|---|---:|---|
| Objective, audience, and intent | 10 | Is there one conversion aligned with the visitor? |
| Offer and value proposition | 15 | Is the exchange clear and worth it? |
| Headline, benefits, and AIDA | 15 | Does the message move from attention to action? |
| CTA, focus, and simplicity | 10 | Is one persuasive action dominant? |
| Form and friction | 10 | Is the requested effort proportional? |
| Proof and trust | 10 | Are important claims credibly supported? |
| Visual hierarchy and UX | 10 | Does the interface guide the decision? |
| Mobile and performance | 5 | Can relevant devices complete the flow? |
| SEO and channel continuity | 5 | Does the page match the promise before the click? |
| Privacy, domain, and security | 4 | Is the data exchange legitimate and transparent? |
| Measurement | 3 | Can the conversion be measured reliably? |
| Post-conversion delivery | 3 | Is the promise actually delivered? |

## Example output

```text
Adherence score: 74.5/100 — medium confidence — 92% coverage
Readiness: ready with corrections
Biggest lever: clarify the offer before asking for company data.

P1 — The form asks for six fields before proving value
Evidence: company size and phone are required above the first proof block
Impact: raises friction before trust is established
Correction: move nonessential qualification to the next step
Source: [S1 §5], [S3 form/checklist]
```

The skill does not promise conversion lift. It distinguishes historical examples, hypotheses, and observed results.

## Install

### Codex

```bash
git clone https://github.com/luisroquette/My_LP_Makes_Neil_Proud.git ~/.codex/skills/my-lp-makes-neil-proud
```

Then ask:

```text
Use $my-lp-makes-neil-proud to audit https://example.com without submitting the form.
```

### Claude Code

```bash
git clone https://github.com/luisroquette/My_LP_Makes_Neil_Proud.git ~/.claude/skills/my-lp-makes-neil-proud
```

Claude Code ignores the Codex-specific `agents/openai.yaml` file.

### Manual download

Download the [ZIP archive](https://github.com/luisroquette/My_LP_Makes_Neil_Proud/archive/refs/heads/main.zip), extract it, rename the folder to `my-lp-makes-neil-proud`, and move it into your agent's skills directory.

## How it works

1. The agent identifies the page type, conversion objective, audience, traffic source, and offer.
2. It inspects desktop and mobile without converting or changing the page.
3. It scores each applicable criterion from 0 to 5 in 0.5 increments.
4. `scripts/calculate_score.py` calculates score, coverage, and supplied metrics.
5. The agent returns the evidence table, launch readiness, and prioritized fixes.

## Safe by default

The skill never submits a form, buys, publishes, or changes a page without explicit authorization. Missing analytics or integration access is labeled `Not verified`; it is never silently scored as failure.

It also avoids universal CRO myths: there is no mandatory page length, video, button color, or exact number of form fields. Each choice is evaluated against traffic temperature, risk, offer, audience, and measurable results.

## Files

```text
SKILL.md                    Agent workflow and output contract
references/source-map.md    Traceability to the three source guides
references/framework.md     Strategic principles and contextual rules
references/rubric.md        Criteria, weights, scoring, and readiness
references/metrics.md       Formulas and experimentation rules
scripts/calculate_score.py  Deterministic score and metric calculator
scripts/verify_sources.py   Optional SHA-256 source snapshot check
```

## Sources

The framework was derived from these Portuguese-language guides:

- [Landing Page: the beginner's guide](https://neilpatel.com/br/blog/landing-page/)
- [The definitive guide to high-converting landing pages](https://neilpatel.com/br/blog/o-guia-definitivo-para-criar-landing-pages-super-convertedoras/)
- [Landing pages: what they are, how to create them, and examples](https://neilpatel.com/br/blog/landing-page-o-que-e/)

The repository contains summaries and a source map, not copies of the original articles. Source content can change; recheck live guidance before revising the rubric.

## License

MIT. Use it, adapt it, and make landing-page reviews more accountable.
