# Landing-page adherence rubric

## Scale

| Score | Rule |
|---:|---|
| 0 | Absent or contrary to the source principle |
| 1 | Minimally present and structurally failing |
| 2 | Partial, generic, or materially frictional |
| 3 | Meets the basics with clear losses |
| 4 | Strong, specific, coherent; minor adjustments |
| 5 | Excellent, complete, verifiable, context-appropriate |

Use 0.5 increments. Base every score on an observable page element, supplied data, or labeled inference. This scale and the weights operationalize the guides; they are not an official Neil Patel methodology.

## Criteria and weights

| ID | Criterion | Weight | Primary source | Decision question |
|---|---|---:|---|---|
| `objective_intent` | Objective, audience, intent | 10 | S2 Step 1; S3 types | Is one conversion aligned with persona, intent, funnel, and source? |
| `offer` | Offer and value proposition | 15 | S1 §7; S2 research | Is what the visitor gets, why it matters, and why the exchange is worth it clear? |
| `message_aida` | Headline, benefits, AIDA | 15 | S2 anatomy/AIDA; S3 creation | Does the message progress from attention to action with adequate specificity and objection handling? |
| `cta_focus` | CTA, focus, simplicity | 10 | S1 §3/§6; S2 CTA/KISS | Is one persuasive action clear, visible, and free of competing decisions? |
| `form_friction` | Form and friction | 10 | S1 §5; S3 checklist | Are fields, sensitivity, steps, and feedback minimal, proportional, and functional? |
| `proof_trust` | Proof and trust | 10 | S1 §1; S2 trust | Is available proof real, relevant, and sufficient for the risk? |
| `visual_ux` | Visuals, hierarchy, brand, UX | 10 | S1 §2/§6; S2 design | Does authentic visual design guide attention and reinforce the offer? |
| `mobile_performance` | Mobile and performance | 5 | S2 mobile; S3 SEO | Does the flow work and load adequately on relevant devices? |
| `seo_channel` | SEO and channel continuity | 5 | S2 intent; S3 SEO | Does the page match the click promise and applicable search intent? |
| `data_privacy` | Privacy, domain, security | 4 | S3 privacy/checklist | Do identity, domain, collection, consent, and HTTPS establish legitimacy? |
| `measurement` | Tracking and metrics | 3 | S2 tests; S3 metrics | Can conversion stages be measured with reliable definitions and events? |
| `aftercare` | Delivery and post-conversion | 3 | S3 thank-you/checklist | Is the promise delivered with confirmation and a coherent next step? |

Weights total 100. Offer and message receive the highest weights because the sources treat value and persuasive progression as central. Privacy, measurement, and aftercare remain separate so one strength cannot hide another operational risk.

## Scoring anchors

| Criterion | 0 | 3 | 5 |
|---|---|---|---|
| Objective/intent | No primary action or clear conflict | Action is clear; audience, source, or intent has gaps | Audience, source, intent, stage, and action are aligned and confirmed |
| Offer | The visitor cannot understand what is received | Clear but generic; value or risk is unresolved | Specific, valuable, honest, and strongly matched to the audience |
| Message/AIDA | Headline does not explain benefit or action | Headline and benefit work; desire or objections are weak | Headline, benefits, proof, and action form a complete persuasive progression |
| CTA/focus | CTA is absent, incompatible, or buried | Visible and coherent; copy or hierarchy can improve | One specific action dominates at every key decision point |
| Form | Impossible, deceptive, or disproportionate | Works with avoidable fields, friction, or weak feedback | Requests the proportional minimum with clear validation and feedback |
| Proof/trust | Material claims lack support | Trust signals exist but are generic or remote | Real, specific, proportional proof appears near the decision |
| Visual/UX | Visuals confuse or compete with conversion | Readable and coherent; hierarchy or authenticity can improve | Imagery, brand, contrast, spacing, and direction reinforce action |
| Mobile/performance | Conversion is impossible on a relevant device | Basic use works with speed or ergonomic losses | Fast, readable, and fully functional on relevant devices |
| SEO/channel | Page contradicts the click promise or known intent | Basic match with source or SEO gaps | Source, keyword, title, URL, H1, snippet, and content align when applicable |
| Data/privacy | Collection lacks minimum transparency or serious security fails | HTTPS and identity are clear; consent, policy, domain, or minimization has gaps | Identity, consent, purpose, minimization, policy, domain, and security align |
| Measurement | No reliable way to know conversion occurred | Primary conversion is measured; stages or definitions have gaps | Events, funnel, denominators, and objective are defined and verifiable |
| Aftercare | Success is simulated or the promise is not delivered | Delivery works; confirmation or next step is weak | Delivery, thanks, expectations, and next step are clear and functional |

## Calculation and coverage

```text
points = weight × score / 5
adherence score = 100 × sum(points) / scored weight
coverage = 100 × scored weight / applicable weight
applicable weight = 100 − N/A weights
```

- Use `N/A` only when structurally inapplicable.
- Missing data is `Not verified`, not `N/A` and not zero.
- Leave an applicable item unscored when evidence is insufficient; this reduces coverage.
- Zero requires a confirmed absence or failure.
- Round adherence to one decimal and always show coverage.
- Treat coverage below 100% as provisional.
- Confidence is high when decisive evidence is confirmed, medium with material inferences, and low when screenshots, partial copy, or unknowns dominate.
- Never create A–F bands; the sources define none.

## Operational readiness

Evaluate readiness separately. Do not apply an artificial score ceiling.

### Not ready

Use when any confirmed blocker exists:

- primary CTA is broken, deceptive, or has no useful destination;
- form simulates success, loses the lead, or fails to deliver the offer;
- primary conversion is impossible on a relevant device;
- promise materially conflicts with delivery;
- data is captured without applicable minimum transparency;
- severe security failure or inaccessible page.

### Ready with corrections

The end-to-end flow converts, but meaningful gaps remain in clarity, proof, friction, mobile, measurement, privacy, domain, SEO, or aftercare.

### Ready

The flow delivers a real conversion, has no confirmed blocker, and remaining changes are optimization hypotheses.

## Priority

1. `P0`: broken delivery, false promise, unusable mobile, security, or opaque data collection.
2. `P1`: weak intent, offer, AIDA, CTA, form, or proof.
3. `P2`: visual refinement, domain, SEO, measurement, aftercare, or A/B hypothesis.

Format every fix as:

```text
P0|P1|P2 — Problem
Evidence: exact observed element
Impact: affected conversion stage
Correction: concrete change
Source: [S1 §x], [S2 section], or [S3 section]
```

