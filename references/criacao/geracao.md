# Generation

Two entry points produce a blueprint. Both land in a draft for human review — **generation never saves or publishes on its own.**

## Entry points

### From URL (extraction)

1. Fetch the page safely (SSRF-guarded: allowlisted hosts, no private-network targets, no credentials).
2. The LLM assembles the blueprint from the **real page content only**.
3. **Anti-fabrication:** price, deadline, credential, or any claim not present in the source → omit the section. Never invent.
4. Slug auto-suggested from the URL path, percent-decoded — `%C3%AD` must become `í`, never a literal hex slug. An invalid percent-encoding (URIError on decodeURIComponent) fails the extraction, it never falls back to the raw hex.
5. **SSRF redirects:** fetching follows redirects only if the allowlist/private-IP guard is re-run on every hop — otherwise redirects are not followed.

### From instruction (free text)

A brief in natural language: offer, audience, model, goal. The LLM proposes a blueprint; anything the instruction does not state is omitted, not guessed.

## Quick decisions (not extractable)

Five fields are decisions of the creator, not facts of the page. Collect them **before or above** the blueprint editor, never buried in JSON:

1. `objetivo`
2. `evergreen`
3. `tema`
4. `comprimento`
5. `riscoOferta`

## Cascading gates

Every blueprint passes these gates in order. A blocking failure stops the flow.

| # | Gate | Scope | When blocking |
|---|---|---|---|
| 1 | `validar-estrutura` | JSON **form**, field by field, array element by array | always |
| 2 | `validar-<modelo>` | model rules (object presence, enum values, layout contract) | always |
| 3 | `validar-seo` | `metaTitle` 30–65 chars, `metaDescription` 120–160 | only when `evergreen: true` |
| 4 | `validar-contraste` | WCAG AA on visual tokens — one retry with adjusted tokens, then report to the creator | only when `visual` is present |

`scripts/validar-blueprint.py` implements gate 1 deterministically (no LLM). Gates 2–4 are instructional — the agent applies them and reports evidence.

## Draft vs. publication

- A **draft may be incomplete**. That is its purpose.
- **Publication may not.** Once a slug is published, saving a partial blueprint over it must be refused before any write (a published page that serves a half-filled blueprint renders a 500 — real production bug).
- Re-saving a published LP keeps its status; every intermediate save is still `published`, so the gate that matters is the structural one: a published LP must always satisfy gate 1 at minimum.

## Form rule (pétrea)

Every LP has a form connected to the correct funnel — see `modelos.md`. A generator that produces an LP with a CTA pointing at a nonexistent form or checkout is a blocking bug, not a style choice.
