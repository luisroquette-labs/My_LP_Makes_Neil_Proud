# My_LP_Makes_Neil_Proud

**The full landing-page cycle: brief, create, edit by command, audit, and publish — evidence-backed at every stage.**

Create a landing page from a URL or a brief in one of six strategies, edit it with natural-language commands, audit it against a 12-criterion conversion rubric derived from three Neil Patel landing-page guides, and publish it under a pluggable tracklink contract.

[Download the skill](https://github.com/luisroquette/My_LP_Makes_Neil_Proud/archive/refs/heads/main.zip) · [Install for Codex](#install) · [See the rubric](references/auditoria/rubric.md) · [Changelog](CHANGELOG.md)

> Independent open-source implementation. The audit score and weights are an operationalization of the cited guides, not an official Neil Patel or NP Digital methodology. This project is not affiliated with or endorsed by Neil Patel or NP Digital.

## The cycle

| Stage | What it does | Reference |
|---|---|---|
| 1. Briefing | Extracts facts from a URL (or a free-text brief), collects the five creator decisions, classifies the model — without fabricating anything | `references/briefing/` |
| 2. Creation | Builds the blueprint for one of 6 LP models, gated in cascade: form → model → SEO → WCAG contrast | `references/criacao/` |
| 3. Editing (Mini-Lovable) | Applies free-text commands surgically by section path, with an autosaved edit brief | `references/edicao/` |
| 4. Audit | Scores the page 0–100 on 12 weighted criteria, readiness, P0/P1/P2 fixes with evidence | `references/auditoria/` |
| 5. Publication | Verifies the published-LP obligations and connects [My_UTMs_Make_Me_Proud](https://github.com/luisroquette/My_UTMs_Make_Me_Proud) by contract (recommended standard) | `references/publicacao/` |

The dashboard of issued LPs is defined as a pluggable contract (`references/dashboard/`) that now consumes the exposure contract shipped in [My_UTMs_Make_Me_Proud](https://github.com/luisroquette/My_UTMs_Make_Me_Proud) (`nucleo/metricas.md`) — the dashboard implementation still arrives with the dashboard itself.

## Why it holds up

Every important claim answers four questions:

| Question | What the cycle returns |
|---|---|
| What is actually wrong? | A specific, observable finding |
| How serious is it? | `P0`, `P1`, or `P2` priority |
| What should change? | A concrete correction |
| Why does it matter? | A traceable source identifier |

Plus the invariants that make the system robust:

- **Anti-fabrication** — no invented price, deadline, credential, or testimonial; absence is `Not verified`, never zero.
- **Form clause** — every LP has a form connected to the right funnel (name + phone + email minimum).
- **Gates before publication** — structural form, model rules, SEO, WCAG AA contrast, each blocking when applicable.
- **Never promise lift** — historical examples, hypotheses, and observed results stay distinct.

## Install

### Codex

```bash
git clone https://github.com/luisroquette/My_LP_Makes_Neil_Proud.git ~/.codex/skills/my-lp-makes-neil-proud
```

Then ask:

```text
Use $my-lp-makes-neil-proud to create a landing page from https://example.com.
```

Or audit without creating:

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

## Files

```text
SKILL.md                          Cycle orchestrator and output contracts
references/briefing/              Stage 1: context and creator decisions
references/criacao/               Stage 2: blueprint schema, 6 models, generation gates, copy profiles
references/edicao/                Stage 3: Mini-Lovable commands and visual tokens
references/auditoria/             Stage 4: 12-criterion rubric, framework, metrics (v1, intact)
references/publicacao/            Stage 5: published-LP obligations + tracklink contract (pluggable)
references/dashboard/             Dashboard contract (pluggable)
references/versionamento.md       SemVer policy for the skill
scripts/calculate_score.py        Deterministic score and metric calculator
scripts/validar-blueprint.py      Deterministic blueprint form validator (no LLM)
scripts/verify_sources.py         Optional SHA-256 source snapshot check
examples/                         Example inputs for both scripts
CHANGELOG.md                      Keep a Changelog
```

The skill loads only `references/` and `scripts/` during execution. `docs/` holds internal specs and plans as an audit trail.

## Versioning

Versioned with [Semantic Versioning 2.0.0](https://semver.org/): MAJOR when the skill's contract changes, MINOR for new compatible stages or references, PATCH for corrections. Current release: **2.1.0** — the tracklink contract implemented by [My_UTMs_Make_Me_Proud](https://github.com/luisroquette/My_UTMs_Make_Me_Proud) v1.0.0. v1.0.0 (audit only) remains tagged. See `references/versionamento.md` and `CHANGELOG.md`.

## Safe by default

The skill never submits a form, buys, publishes, or changes a page without explicit authorization. Missing analytics or integration access is labeled `Not verified`; it is never silently scored as failure. Generation never saves or publishes on its own — it always lands in a draft for human review.

## Sources

The audit rubric was derived from these Portuguese-language guides:

- [Landing Page: the beginner's guide](https://neilpatel.com/br/blog/landing-page/)
- [The definitive guide to high-converting landing pages](https://neilpatel.com/br/blog/o-guia-definitivo-para-criar-landing-pages-super-convertedoras/)
- [Landing pages: what they are, how to create them, and examples](https://neilpatel.com/br/blog/landing-page-o-que-e/)

The repository contains summaries and a source map, not copies of the original articles. Source content can change; recheck live guidance before revising the rubric.

## License

MIT. Use it, adapt it, and make landing-page work accountable.
