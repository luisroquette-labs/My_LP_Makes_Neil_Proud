# Visual Tokens

`blueprint.visual` carries the page's visual identity as tokens — color, font, radius, and hero arrangement. Tokens are applied inline only when `visual` exists; a page without `visual` keeps its default theme untouched.

## Token set

| Token | Meaning |
|---|---|
| `cores.fundo` | Page background — the source of truth for light/dark decisions. |
| `cores.texto` | Body text color. |
| `cores.destaque` | Primary accent (CTAs, highlights). |
| `cores.acento` | Secondary accent (badges, focus ring). |
| `fonte` | Typeface family. |
| `raio` | Border radius. |
| `hero` | Hero arrangement (up to 4 named options). |

## The dark-mode rule (real bug, do not regress)

Dark text/badge color (`.dark`) must derive from the **real luminance of the painted background** (`cores.fundo`), never from the `tema` field:

- A page with `tema: "claro"` and a dark painted background rendered invisible text — the class and the actual background disagreed.
- Compute luminance from the background hex; choose light text when the background is dark, dark text when it is light.
- Fall back to `tema` only when `cores.fundo` is missing or unparseable.

## Contrast gate (WCAG AA)

Every token pair used for text must pass WCAG AA contrast **before publication** (`validar-contraste`, gate 4 in `../criacao/geracao.md`):

- `texto` vs `fundo`, and any text rendered over `destaque`/`acento`.
- A failing pair blocks publication. The generator retries once with adjusted tokens; persistent failure is reported to the creator, not papered over.

## Focus and media

- **Visual focus:** the hero's `focoVisual` accepts an image type only; a `video` type rendered as a broken full-screen image is a bug — guard the type before rendering.
- **Background media:** full-bleed background images scale with a transform, not a stretched `<img>`.
- **Countdowns are client-only.** Start the first tick after mount (a synchronous state set inside an effect is forbidden), update on an interval, and never render "NaN days": an unparseable date renders no countdown — never "Launched!" without a date.

## Fallback contract

- No `visual` → default theme, default radius, no tokens. Zero behavior change for pages created before this feature.
- Tokens are additive: they override the named properties only. Everything not specified in `visual` falls back to the theme.
