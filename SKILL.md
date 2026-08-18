---
name: my-lp-makes-neil-proud
description: Full landing-page cycle — brief and create (6 LP models, from URL or instruction), edit by natural-language command (Mini-Lovable), audit against a 12-criterion conversion rubric, and publish under a pluggable tracklink contract. Use when creating, editing, auditing, reviewing, approving, or publishing a landing page from a URL, screenshot, HTML, copy, prototype, or brief; covers objective, intent, offer, AIDA, headline, benefits, CTA, form, social proof, UX, mobile, SEO, privacy, tracking, and post-conversion delivery.
---

# Landing-page cycle

Orchestrates the five stages of a landing page: Briefing → Creation → Editing (Mini-Lovable) → Audit → Publication. Each stage has its own references and an output contract. The audit stage also works standalone, exactly as in v1.

Load only the references of the stage being executed.

## Modes

- **Full cycle** — default when asked to create or publish a landing page.
- **Standalone audit** — when asked only to audit/review/approve a page. Execute Stage 4 alone.

## Global hard rules (apply to every stage)

1. **Anti-fabrication.** Never invent price, deadline, credential, testimonial, or claim. A missing datum is omitted or labeled `Not verified` — never zero, never guessed.
2. **Form clause (pétrea).** Every LP has a form connected to the right funnel. Minimum three fields: name + phone + email. Reversing requires owner approval.
3. **Absence is never zero.** Missing data is `Not verified`, never 0/false/ok.
4. **Never publish without gates.** All applicable gates must pass before publication. A published page must always satisfy the structural gate at minimum.
5. **Never promise lift.** Distinguish historical example, hypothesis, and observed result. Never praise without evidence.
6. **Never act on a page without authorization.** Never submit a form, buy, publish, or change a page the user did not authorize.

## Stage 1 — Briefing

Load `references/briefing/contexto-e-decisoes.md`.

**Input:** URL of an existing page or a free-text brief.

**Output contract:**
- A blueprint draft filled only with facts found in the source (extraction) or stated in the brief (instruction) — nothing else.
- The five quick decisions collected explicitly: `objetivo`, `evergreen`, `tema`, `comprimento`, `riscoOferta`.
- The model classified by the heuristic (or explicit selection) from `references/criacao/modelos.md`.
- Declared assumptions, one short question only when the absence prevents useful work.

## Stage 2 — Creation

Load `references/criacao/blueprint.md`, then `references/criacao/modelos.md`, then `references/criacao/geracao.md`. Load `references/criacao/perfis-copy.md` when a copy profile applies.

**Output contract:**
- A blueprint draft matching the schema, model, and profile chosen in Stage 1.
- Gate results, in order: estrutura (form, run `python3 scripts/validar-blueprint.py --input <draft>.json`), modelo, seo (blocking when `evergreen: true`), contraste (blocking when `visual` present).
- The draft is delivered for human review. **Creation never saves or publishes on its own.** A draft may be incomplete; publication may not.

## Stage 3 — Editing (Mini-Lovable)

Load `references/edicao/mini-lovable.md`; load `references/edicao/tokens-visuais.md` when visual tokens are involved.

**Output contract:**
- The command applied surgically: only targeted fields changed, everything else identical.
- The element contract respected: edits target `data-lp-role` elements and the per-model form anchor.
- All gates from Stage 2 re-run and passing after the edit.
- The edit brief autosaved; model reclassification reported when the edit changes the LP's nature.

## Stage 4 — Audit

Load, in this order: `references/auditoria/source-map.md`, `references/auditoria/framework.md`, `references/auditoria/rubric.md`, `references/auditoria/metrics.md`.

**Workflow (unchanged from v1):**
0. If the three original snapshots are available, run `python3 scripts/verify_sources.py`; on `mismatch`, reread the changed source and update the references before auditing.
1. Establish context: page type, single conversion objective, persona, intent, funnel stage, offer, traffic source, pre-click promise, device, deadline, metrics.
2. Inspect without converting (desktop and mobile): promise, content, hierarchy, images, CTA, links, form, post-conversion path, SEO, tracking, HTTPS, data transparency. Never submit a form, buy, publish, or change the page.
3. Score the twelve criteria from 0 to 5 in 0.5 increments; `N/A` only when structurally inapplicable; missing data is `Not verified`, never `N/A` and never zero.
4. Label every finding `Confirmed`, `Inferred`, or `Not verified`.
5. Run `python3 scripts/calculate_score.py --input <json>` for the score and supplied metrics.
6. Keep the adherence score separate from launch readiness.
7. Never require a short/long page, video, a universal color, or an exact field count. Never present article percentages as benchmarks or guarantees.

**Required output:**

```markdown
Adherence score: 00/100 — high|medium|low confidence — 00% coverage
Readiness: ready | ready with corrections | not ready
Biggest lever: one sentence
```

Then: (1) table of all twelve criteria — weight, score, points, evidence state, source; (2) up to five fixes in `P0/P1/P2` format with `problem → evidence → impact → correction → source` (`[S1]`, `[S2]`, or `[S3]`); (3) calculated real metrics and interpretation when provided; (4) up to three unverified items that could change the conclusion; (5) up to three A/B hypotheses only after obvious defects are fixed and measurement is sufficient.

## Stage 5 — Publication

Load `references/publicacao/contrato-tracklink.md`.

**Output contract — every item of section (a) verified before publication:**
1. Canonical slug (never a placeholder; rename is atomic: slug + `seo.urlSlug` + tracking destinations together).
2. Per-LP SEO (metaTitle 30–65, metaDescription 120–160, OpenGraph/Twitter — never the site's generic card).
3. JSON-LD schema (`Course`/`WebPage`), `<` escaped in the serialized output.
4. LGPD consent rendered and required; conversion button disabled only during submission.
5. Thank-you page exists, published, and pointed at from `thankYou.slug`.
6. `/lp/*` routes listed in the sitemap, fail-safe.

The tracklink half (b) is implemented by My_UTMs_Make_Me_Proud (v1.0.0) as the recommended standard — consult the contract; when they disagree, the tracklink repo wins. Portable mode (no tracking system) still publishes: the (a) obligations hold, tracking is absent.

## Versioning

This skill is versioned with SemVer — see `references/versionamento.md` and `CHANGELOG.md`. Report which version you are executing when starting a session that loads this skill.
