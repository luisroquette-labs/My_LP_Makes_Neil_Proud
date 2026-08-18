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

## (b) Tracklink system contract — PLUGGABLE

**Status: awaiting the tracklink repository.** When it ships, it fills this contract; this skill does not get rewritten.

The tracklink system must provide:

| Obligation | Details |
|---|---|
| Slug ↔ destination mapping | Every tracking link resolves a short code to the LP's canonical URL (`destination_url`). |
| Parameter passthrough | UTM and origin parameters survive the redirect and reach the LP's tracking. |
| Thank-you mapping | Each main LP maps to its thank-you destination; conversions are counted through it. |
| Atomic slug rename | When an LP slug changes, tracking destinations update in the same operation as the slug (see (a).1). |
| Pluggable interface | The LP side integrates through a single configuration point — the LP itself has no knowledge of the tracklink implementation. |

### How to plug it in (future)

1. The tracklink repo implements the table above.
2. This reference gains an "Implemented by" section naming the repo and its config location.
3. The dashboard contract (`../dashboard/contrato-dashboard.md`) starts consuming the metrics the tracklink exposes.
4. Nothing else in this skill changes.
