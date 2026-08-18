# Blueprint Schema

The `LpBlueprint` is the single JSON document that describes a landing page through the whole cycle: it is generated in the creation stage, edited by Mini-Lovable commands, audited before publication, and consumed by the published page.

One LP = one blueprint. A thank-you page is an LP with its own blueprint.

## Universal fields (all models)

| Field | Type | Required | Notes |
|---|---|---|---|
| `slug` | string | yes | URL path. Auto-suggested from the source URL, percent-decoded (accents must survive). Never a placeholder. |
| `modelo` | enum | yes | `universal` \| `curso` \| `evento` \| `captura` \| `squeeze` \| `lancamento` |
| `objetivo` | enum | yes | `captura` \| `venda`. Decision of the creator — not extractable from the page. `lancamento` uses `captura`: it inherits the 3-field contract and the lead machine. |
| `headline` | string | yes | Above the fold, never empty. |
| `subheadline` | string | yes | Always rendered — a component that receives only the model object silently drops this field. |
| `publicoAlvo` | string | yes | One clear persona and intent. |
| `beneficios` | string[] | yes | Non-empty array of strings. |
| `cta` | object | yes | `{ texto: string }`. Points at the model's form anchor, never at a dead link. |
| `tema` | enum | yes | `claro` \| `escuro`. Fallback for dark mode; ignored when `visual` carries real colors. |
| `comprimento` | enum | yes | `curta` \| `media` \| `longa`. Creator decision. |
| `evergreen` | boolean | yes | When true, SEO gate becomes blocking. |
| `riscoOferta` | enum | yes | `baixo` \| `medio` \| `alto`. Creator decision; drives how much proof is required. |
| `provaSocial` | object | no | `{ depoimentos: [{ texto, autor }], metricas: [{ valor, rotulo }] }`. Omit when there is none — never invent testimonials. |
| `lgpd` | object | yes | `{ consentimento: true }`. Legal consent checkbox is mandatory; the CTA must not look disabled before it is checked. |
| `seo` | object | conditional | See SEO section. Blocking when `evergreen: true`. |
| `thankYou` | object | no | `{ slug: string }`. Points to the thank-you LP; both slugs must exist and stay in sync. |
| `rastreamento` | object | no | `{ ga4: string?, metaPixel: string? }`. Omit when unknown — absence is `Not verified`, never a fake zero. |
| `visual` | object | no | See Visual section. Absent = default theme; present = tokens must pass contrast gate. |

## Per-model objects

Exactly one of the following objects applies, matching `modelo`. Wrong or missing object is a form error.

### `evento` (modelo: evento)

| Field | Type | Required | Notes |
|---|---|---|---|
| `dataInicio` | ISO string | yes | Must parse with `Intl.DateTimeFormat`. A placeholder like "[INFORMAR DATA]" must be rejected or rendered as null — never "NaN days". |
| `formato` | enum | yes | `presencial` \| `online` \| `hibrido` |
| `local` | string | only presencial/hibrido | |
| `acesso` | string | only online/hibrido | |
| `beneficiosParticipar` | string[] | yes | Never `undefined` — the renderer joins it. |
| `agenda` | object[] | no | `[{ horario, titulo }]` |
| `palestrantes` | object[] | no | `[{ nome, papel }]` |

### `captura` (modelo: captura)

| Field | Type | Required | Notes |
|---|---|---|---|
| `recompensa` | object | yes | `{ tipo, titulo, descricao }` |
| `entregaveis` | string[] | yes | |
| `imagemRecompensa` | string | no | |

### `lancamento` (modelo: lancamento)

| Field | Type | Required | Notes |
|---|---|---|---|
| `nomeProduto` | string | yes | |
| `dataLancamento` | ISO string | yes | Must parse. |
| `teaser` | string | no | |

`squeeze` and `universal` have no per-model object. If the generator omits `modelo` (or a model-less generation), the orchestrator pins `modelo` to the requested model after parsing — a silent fallback to `universal` is a bug, not a feature.

## Visual (optional)

```json
{
  "cores": { "fundo": "#hex", "texto": "#hex", "destaque": "#hex", "acento": "#hex" },
  "fonte": "string",
  "raio": "string",
  "hero": "arranjo do hero — até 4 opções"
}
```

- Applied inline only when `visual` is present; the no-visual fallback must stay intact.
- Dark text/badge color derives from the **real luminance of the background** (`fundo`), never from `tema`.
- Contrast must pass WCAG AA before publication (see `geracao.md`).

## SEO

| Field | Type | Notes |
|---|---|---|
| `metaTitle` | string | 30–65 chars when `evergreen: true` (blocking gate). |
| `metaDescription` | string | 120–160 chars when `evergreen: true` (blocking gate). |
| `openGraph` / `twitter` | object | Per-LP cards — never the site's generic card. |

## Contracts

1. **Absence is never zero.** A missing field is omitted or `Not verified` — it is never treated as 0, false, or ok. This pattern has caused real production bugs four times across three repos.
2. **Form before publication.** Every LP has a form. Minimum three fields: name + phone + email. Reversing this requires explicit owner approval.
3. **Form validation covers shape, not just presence.** Any field the renderer consumes needs a shape check (`string[]` joins, parseable dates) — a present-but-malformed field crashes a published page.
4. **Anti-fabrication.** Nothing is invented: missing price, deadline, or credential means the section is omitted, never made up.
