# Publication and Tracklink Contract

The publication stage has two halves: what every published LP must provide (portable, applies to any host), and what the tracklink system must satisfy (pluggable — this repo connects to it later without rewriting the skill).

## (a) Obligations of the published LP

Before an LP is published, verify all of these. They hold on any host, with or without the tracklink system.

1. **Canonical slug.** The route slug is the canonical identity of the LP. It is never a placeholder. Renaming a slug is an atomic operation that updates the slug, the blueprint's internal `seo.urlSlug`, and every tracking destination together — a half-renamed LP breaks its own links and its thank-you page (real production incident).
2. **Per-LP SEO.** Every LP carries its own `metaTitle` (30–65 chars), `metaDescription` (120–160), OpenGraph and Twitter cards. An LP without them inherits the site's generic card on WhatsApp/social — never acceptable for a page with paid traffic.
3. **JSON-LD schema.** `Course` (with pricing when present) or `WebPage`. Escape `<` in the serialized schema — content comes from scraped pages and a raw interpolation is a stored XSS.
4. **LGPD consent.** The consent checkbox is rendered and required; the conversion button is disabled only during submission — never before consent is checked.
5. **Thank-you page.** The thank-you LP exists, is published, and is pointed at from the main LP's `thankYou.slug`. An orphaned thank-you breaks the conversion journey of every lead.
6. **Sitemap.** `/lp/*` routes are listed in the sitemap. A sitemap failure must never take the site down (fail-safe listing).

## (b) Tracklink system contract — implemented

**Implemented by [My_UTMs_Make_Me_Proud](https://github.com/luisroquette-labs/My_UTMs_Make_Me_Proud) (v1.0.0) — the tracking layer of the marketing suite.** Its `references/integracoes/lp.md` is the source of truth for this integration; its `references/nucleo/` holds the portable tracking cycle (creation, click, attribution, health, metrics). This reference summarizes the contract — when they disagree, the tracklink repo wins.

The tracklink system provides:

| Obligation | Details |
|---|---|
| Slug ↔ destination mapping | Every tracking link resolves a short code to the LP's canonical URL (`destination_url`). |
| Tracked destination | The link resolves to destination + UTMs (`tracked_destination_url`) — the visitor lands on the LP with attribution parameters already in the URL. |
| Thank-you mapping | Each main LP maps to its thank-you destination; conversions are counted through it. |
| Atomic bundle | LP + campaign + tracking link are written in one transaction; collisions are named errors, never silent overwrites. |
| Slug rename propagation | The tracking system has **no automatic rename trigger** (documented absence). Whoever renames an LP slug updates its tracking destinations in the same atomic operation (see (a).1); consistency is also re-established on the next bundle save. |
| Pluggable interface | The LP side integrates through a single configuration point — the LP itself has no knowledge of the tracklink implementation. |

**Recommended, not mandatory.** In portable mode (no tracking system), an LP still publishes — the (a) obligations hold and tracking is simply absent. When both systems exist, apply the production standard: no LP goes live untracked.

### How the plug works

1. The tracklink repo (`references/integracoes/lp.md`) defines the integration contract — it is the source of truth.
2. The dashboard contract (`../dashboard/contrato-dashboard.md`) consumes the metrics the tracklink exposes (`references/nucleo/metricas.md`).
3. Nothing else in this skill changes.
