# Changelog

All notable changes to this skill are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-08-18

### Changed

- Publication stage: tracklink contract (b) now implemented by [My_UTMs_Make_Me_Proud](https://github.com/luisroquette-labs/My_UTMs_Make_Me_Proud) v1.0.0 — its `references/integracoes/lp.md` is the source of truth; the plug is the recommended standard, not a mandatory step.
- `references/dashboard/contrato-dashboard.md`: consumes the exposure contract shipped in the tracklink repo (`nucleo/metricas.md`); the dashboard implementation remains out of scope.
- Tracklink contract corrected to the documented reality: no automatic slug-rename propagation — destinations update in the same atomic rename operation (a).1 or on the next bundle save.

## [2.0.0] - 2026-08-18

### Added

- Full landing-page cycle orchestration in `SKILL.md`: Briefing → Creation → Mini-Lovable editing → Audit → Publication.
- Creation stage (`references/criacao/`):
  - `blueprint.md` — schema: ~20 universal fields + per-model objects (evento, captura, lancamento) + visual + seo. Contract: absence is never zero.
  - `modelos.md` — 6 LP models (universal, curso, evento, captura, squeeze, lancamento) with ordered classification heuristic and per-model layout rules.
  - `geracao.md` — generation from URL or instruction with cascading gates: estrutura → modelo → seo → contraste. Generation never publishes on its own.
  - `perfis-copy.md` — copy style profiles (Giveaway, Empiricus) and the format for creating new ones.
- Editing stage (`references/edicao/`):
  - `mini-lovable.md` — free-text command editing, `data-lp-role` element contract, per-model form anchor, edit brief with autosave.
  - `tokens-visuais.md` — visual tokens with WCAG AA contrast gate and luminance-derived dark mode.
- Publication stage: `references/publicacao/contrato-tracklink.md` — tracklink system contract, marked pluggable.
- Dashboard contract: `references/dashboard/contrato-dashboard.md` — pluggable, implementation out of scope for this version.
- `scripts/validar-blueprint.py` — deterministic blueprint form validation (no LLM).
- `examples/example-briefing-input.json` — creation stage example input.
- `references/versionamento.md` — SemVer policy for the skill itself.

### Changed

- v1 audit references moved to `references/auditoria/` without content change.
- `README.md` rewritten for the full cycle.
- `SKILL.md` rewritten as the cycle orchestrator with output contracts per stage.

## [1.0.0] - 2026-08-14

### Added

- Landing-page audit against a 12-criterion rubric derived from three Neil Patel guides: 0-100 adherence score, launch readiness, evidence labels, and P0/P1/P2 prioritized fixes traceable to `[S1][S2][S3]`.
- `references/source-map.md`, `references/framework.md`, `references/rubric.md`, `references/metrics.md`.
- `scripts/calculate_score.py` and `scripts/verify_sources.py`.
- `examples/example-audit-input.json`.
- Codex support via `agents/openai.yaml`.
