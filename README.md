<p align="center">
  <img src="assets/cover.png" alt="My_LP_Makes_Neil_Proud — the landing-page engine" width="100%">
</p>

<h1 align="center">My_LP_Makes_Neil_Proud</h1>

<p align="center">
  <strong>The landing-page engine that ships evidence-backed pages, not decorated templates.</strong><br>
  A portable, deterministic LP system for Claude Code and Codex — brief, create, edit by command, audit and publish as one auditable cycle.
</p>

<p align="center">
  <a href="./LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-7B2FBE.svg"></a>
  <img alt="No runtime dependencies" src="https://img.shields.io/badge/runtime_dependencies-0-D5A62E.svg">
  <img alt="Claude Code and Codex" src="https://img.shields.io/badge/works_with-Claude_Code_%2B_Codex-17131F.svg">
  <img alt="6 LP models" src="https://img.shields.io/badge/lp_models-6-2E7D32.svg">
  <img alt="Deterministic validator" src="https://img.shields.io/badge/validator-deterministic-681D2A.svg">
  <img alt="v2.1.0" src="https://img.shields.io/badge/version-v2.1.0-D5A62E.svg">
</p>

> **Independent project:** My_LP_Makes_Neil_Proud is not affiliated with, endorsed by, or sponsored by Neil Patel, NP Digital, or their companies. It implements established direct-response publishing patterns — never third-party copy, trademarks, or claims.

---

## Table of contents

- [Em 30 segundos](#em-30-segundos)
- [Para quem é este produto?](#para-quem-é-este-produto)
- [Instalação](#instalação)
- [Início rápido](#início-rápido)
- [Comandos](#comandos)
- [Características](#características)
- [Os seis modelos, em profundidade](#os-seis-modelos-em-profundidade)
- [Os quatro gates, em profundidade](#os-quatro-gates-em-profundidade)
- [As decisões que moldaram este repo](#as-decisões-que-moldaram-este-repo)
- [Em comparação com ferramentas manuais / de agência / comerciais](#em-comparação-com-ferramentas-manuais--de-agência--comerciais)
- [Casos de uso](#casos-de-uso)
- [Exemplo de saída](#exemplo-de-saída)
- [Arquitetura](#arquitetura)
- [Metodologia](#metodologia)
- [Novidades na versão 2.x](#novidades-na-versão-2x)
- [Limitações](#limitações)
- [Requisitos](#requisitos)
- [Desinstalar](#desinstalar)
- [Extensões](#extensões)
- [Ecossistema](#ecossistema)
- [Documentação](#documentação)
- [Perguntas frequentes](#perguntas-frequentes)
- [Colaboradores da comunidade](#colaboradores-da-comunidade)
- [Licença](#licença)
- [Contribuindo](#contribuindo)
- [Autor](#autor)

---

## Em 30 segundos

You paste a URL — or write one sentence — and the engine produces a landing-page blueprint, never inventing a price, a deadline or a credential that is not in the source. You choose one of six models (universal, course, event, capture, squeeze, launch) and five quick decisions (objective, evergreen, theme, length, offer risk). You edit the page with natural-language commands. Four gates — structure, rules, contrast, SEO — audit the result, and the publication gate refuses anything that fails them. Every CTA ships as a tracking link under the sibling tracklink contract, so the page that captures the lead is also the page that attributes it.

That is the entire product. The rest of this README is the terrain: the models, the gates, the contracts, and the exact behavior of each stage. If the thirty-second version already sounds like what you needed, jump to [Início rápido](#início-rápido) and validate the blueprint — it takes ten seconds.

---

## Para quem é este produto?

This skill exists for people who have learned that a landing page is a sales argument, not a decoration. If you ship pages that must convert — and must be able to prove why — this is for you.

**Agencies and consultancies producing pages for clients.** Each client page needs a brief, a model, a copy direction and an audit the client can read. The cycle makes the page reproducible: same brief, same gates, same verdict — and the audit report is the deliverable, not the excuse.

**In-house teams shipping campaigns on a calendar.** Workshop pages, course pages, launch pages, capture pages — every format with its own contract instead of one recolored template. The six models exist so two different campaigns do not look like twins.

**Developers integrating pages into a marketing system.** The page is not the end of the funnel — it is the entry point. The pluggable tracklink contract means the page's CTAs are tracked links, the lead records first-click attribution, and the email engine picks the lead up from there. One system, three repositories, one contract.

If you ship one page a year, this is overkill. This skill earns its weight when pages are a recurring product of your marketing operation.

---

## Instalação

### Option A — Claude Code skill (recommended)

```bash
git clone https://github.com/luisroquette/My_LP_Makes_Neil_Proud.git ~/.claude/skills/my-lp-makes-neil-proud
```

Restart Claude Code — the skill loads as `my-lp-makes-neil-proud`. No API keys, no services, no runtime dependencies: the repository is Markdown contracts plus deterministic Python validators.

### Option B — manual download

```bash
# read before running, as always
curl -L https://github.com/luisroquette/My_LP_Makes_Neil_Proud/archive/refs/heads/main.tar.gz | tar xz
mv My_LP_Makes_Neil_Proud-main my-lp-makes-neil-proud
```

### Option C — Codex

`agents/openai.yaml` loads the same skill under Codex.

**Requirement:** Python 3.10+ for the validators. The contracts are plain Markdown — any agent, any stack, any language.

---

## Início rápido

```bash
# 1. Validate the canonical example (blueprint form gate)
python3 scripts/validar-blueprint.py --input examples/example-briefing-input.json

# 2. Score the canonical audit example
python3 scripts/calculate_score.py --input examples/example-audit-input.json

# 3. Verify the source snapshots
python3 scripts/verify_sources.py --source-dir examples/

# 4. Read the cycle (5 stages, 10 minutes)
cat SKILL.md
```

The canonical example is the contract in JSON form: a course blueprint that passes every gate. If the example fails, the engine is broken — fix that before anything else.

A blueprint in one glance:

```json
{
  "slug": "lp-treinamento",
  "modelo": "curso",
  "objetivo": "venda",
  "headline": "A headline que carrega a promessa",
  "subheadline": "O subtítulo acima da dobra",
  "publicoAlvo": "Quem esta página fala",
  "tema": "claro",
  "comprimento": "media",
  "riscoOferta": "baixo",
  "evergreen": true,
  "beneficios": ["benefício 1", "benefício 2"],
  "cta": { "texto": "Quero participar" },
  "lgpd": { "consentimento": true }
}
```

The shape is not decorative. Every field is validated for form — field by field, array element by element — before any rule gate runs. A malformed blueprint is rejected at the structure gate, never discovered mid-render.

---

## Comandos

The skill is an operating cycle, not a bag of utilities. Five stages, each deterministic.

| Stage | What it does | Contract |
|---|---|---|
| 1. **Briefing** | Free-text instruction or URL extraction — the five quick decisions above the JSON, context and decisions | `references/briefing/` |
| 2. **Criação** | Blueprint assembly from real content only, six models, slug from URL percent-decoded | `references/criacao/` |
| 3. **Mini-lovable** | Natural-language edits by section path, no raw JSON paths | `references/edicao/` |
| 4. **Auditoria** | 12-criterion conversion rubric with scoring and verdicts | `references/auditoria/` |
| 5. **Publicação** | Gate never bypassed, tracklink contract, archive semantics | `references/publicacao/` |

Validators:

```bash
python3 scripts/validar-blueprint.py --input <draft>.json   # structure gate (form)
python3 scripts/calculate_score.py --input <audit>.json     # rubric scoring
python3 scripts/verify_sources.py --source-dir <dir>        # source snapshots
```

One rule crosses all five stages: **anti-fabrication is the highest rule.** Price, deadline, credential or any claim not present in the source page → omit the section entirely. A missing price is a missing price, not an estimated one.

---

## Características

**Six models, one engine.** Universal (fallback), course, event, capture, squeeze and launch — each with its own blueprint object, its own form validation, its own render layout. The course model is a product page; the event model is an RSVP; the squeeze is one screen plus a legal strip. Same engine, different jobs — never ten variations of the same template.

**Anti-fabrication by construction.** URL extraction assembles the blueprint from the real page content only. Free-text briefs state only what the instruction states. Anything not present is omitted, not guessed — and the gates check for it.

**Five quick decisions above the JSON.** Objective, evergreen, theme, length and offer risk are decisions of the person creating the page — not facts extractable from a source. They are selects, not buried JSON fields, because the person who creates the page should never have to edit JSON to express intent.

**Four gates, never bypassed.** Structure (form: field by field, array element by element), rules (model contracts, LGPD consent), contrast (WCAG AA, blocking), SEO (title 30-65 chars, description 120-160, blocking for evergreen pages). A page that fails a gate does not publish — the publication action validates before writing.

**Visual generated per page.** Tokens for colors, fonts, radius and hero arrangement, generated from a real reference and validated for contrast before anything goes live — with a no-visual fallback that stays intact.

**Tracked CTAs by contract.** The plug (v2.1.0) references the sibling tracklink skill: every CTA ships as a tracking link, and the lead records first-click attribution. The page that captures the lead is the page that attributes it.

**Deterministic tooling.** The blueprint validator, the rubric scorer and the source verifier are single-file Python with zero dependencies — same input, same verdict, forever, in your terminal and in CI.

---

## Os seis modelos, em profundidade

### universal — the fallback

No model object, no heuristic trigger. The universal model renders the ~20 universal fields plus the optional sections, and it is what free-text creation falls back to when no model signal is present. It exists so that "I did not detect a model" is a valid page, not an error.

### curso — the product page

The workhorse. `blueprint.curso` reuses the universal fields and adds the course-specific structure: agenda, methodology, instructors, FAQ, credentials and scheduling. The heuristic is order-sensitive on purpose: "curso gratuito com ebook" is still a course, "webinar com material" is still an event — the first strong signal wins, and weaker signals never override it.

### evento — the RSVP

Presencial, online or hybrid — with a countdown, logistics chips, and a layout that respects the venue. The form gate requires a parseable ISO start date and a venue/access string matching the format — the two bugs that made real event pages render "NaN days".

### captura — the lead magnet

Ebook, checklist, whitepaper, template — the reward object plus the universal fields, with the form **inside the hero** (`#captura-form`, above the fold). The capture form contract is a pétrea clause: name + phone + email, three fields, never "email only".

### squeeze — one screen plus a legal strip

The smallest model by design: no blueprint object, no heuristic — only the explicit selector. One rule: `comprimento: "curta"`. One screen (`min-h-svh`), form in the hero, and a legal strip kept for LGPD. The contract keeps the three capture fields even here — reverting that requires owner approval.

### lancamento — the coming soon

`{ nomeProduto, dataLancamento, teaser? }` — one screen plus the legal strip, a countdown reused from the event model, and the hard rule that a missing date renders nothing instead of "Lançado!" — the anti-fabrication principle applied to time itself.

---

## Os quatro gates, em profundidade

### Gate 1 — structure (form)

Runs **before** the rule gates. Checks the shape field by field, array element by array: a blueprint missing a field coming from the admin form must produce a blocking error, never a raw `TypeError`. Wrong-model objects are rejected here — a course blueprint carrying an event object is a form error, not a rule error. The slug gets its own form rules: lowercase, no `%`-encoding, no slashes, no `..`, no spaces, no control characters — the literal-hex slug was a real production bug, and it stays pinned.

### Gate 2 — rules (model contracts)

Model-specific contracts: event format and date, capture reward shape, launch product name and date, LGPD consent always. The consent checkbox the validator demands is the same one the UI renders — a mismatch there was a legal exposure found in review and fixed before merge.

### Gate 3 — contrast (WCAG AA)

Generated visual tokens are validated for contrast **before** anything goes live — blocking. And because the `.dark` class decides text and badge colors, the check derives darkness from the actual painted background luminance, not from a stored theme string. A theme that says "light" while the token paints dark is a text-invisibility bug waiting to ship.

### Gate 4 — SEO

`metaTitle` 30-65 chars, `metaDescription` 120-160 — blocking only for evergreen pages. Regeneration is a single retry, not a loop, because text converges fast. JSON-LD ships `Course` with pricing when the page has pricing, `WebPage` otherwise — and the schema is escaped, because content extracted from arbitrary URLs is not trusted input.

---

## As decisões que moldaram este repo

The engine was extracted from a production motor through owner decisions. They explain *why* the repo looks the way it does:

1. **The cycle is the product.** Briefing → creation → mini-lovable → audit → publication, from the first release.
2. **Six models, not one template.** The taxonomy research (Wix, HubSpot, RD Station, Landingi, Unbounce) confirmed the two axes — objective × model — and each model got its own contract.
3. **Anti-fabrication above everything.** The rule appears in extraction, generation, editing and gates. It is the only rule that overrides a nice-looking result.
4. **The five quick decisions are selects, not JSON.** The person creating the page decides intent; the engine decides structure.
5. **The publication gate is never bypassed.** Not by rascunho, not by admin, not by automation.
6. **The capture form is a pétrea clause.** Name + phone + email. Changing it requires owner approval.
7. **The tracklink owns the tracking contract; the LP references it.** v2.1.0 upgraded the plug to do exactly that.
8. **The dashboard contract is pluggable.** The audit metrics flow to a dashboard contract that any implementation can consume.

---

## Em comparação com ferramentas manuais / de agência / comerciais

| | Página à mão | Agência | Builder comercial | **My_LP_Makes_Neil_Proud** |
|---|---|---|---|---|
| Anti-fabricação garantida | ✗ | Depende do redator | ✗ | **Sim — regra acima de tudo** |
| Seis modelos com contrato | ✗ | Implícito | Templates fechados | **Sim — contratos em Markdown** |
| Auditável por você | ✗ | Só o resultado | ✗ | **Sim — 12 critérios com score** |
| Gate de publicação obrigatório | ✗ | ✗ | ✗ | **Sim — nunca contornado** |
| CTAs trackeados por contrato | ✗ | Manual | Parcial | **Sim — plug tracklink** |
| Funciona offline / sem vendor | Sim | — | ✗ | **Sim — zero dependências** |
| Determinístico | ✗ | ✗ | Parcial | **Sim — validators sem LLM** |
| Portável entre clientes | ✗ | ✗ | Licenças | **MIT — clone por cliente** |

Use the hand-made page when the page is a one-off and your time is free. Use an agency when you are buying copy judgment, not structure. Use a builder when you need drag-and-drop speed and accept its black box. Use My_LP when the page must be *evidence-backed* — audited, gated and attributable — because the page is the entry point of a funnel the other two skills continue.

---

## Casos de uso

### 1. The workshop-to-course funnel

A workshop page (course model), a capture page for the kit (capture model), an RSVP for the live session (event model). Three pages, three models, one engine — and the CTAs of all three feed the same tracking contract, so the funnel report joins on one attribution column.

### 2. The agency producing client pages on a calendar

Each client page goes through the same cycle with a brief the client approves: the audit report is the deliverable. The client can re-run the rubric themselves — the score is deterministic, not a consultant's opinion.

### 3. The product team shipping launch pages

Coming-soon pages (launch model) that never render "Lançado!" without a date, capture pages that keep the three-field contract, and course pages that carry structured data — all from the same engine, without the product team becoming a design team.

---

## Exemplo de saída

Real output, unedited:

```
$ python3 scripts/validar-blueprint.py --input examples/example-briefing-input.json
FORM VALID — modelo=curso

$ python3 scripts/validar-blueprint.py --input /tmp/lp-bad.json
FORM INVALID (5):
  - slug: must be lowercase, no %-encoding, no slashes, no '..', no spaces, no control chars
  - evento: object present but modelo is 'curso'
  - evento.dataInicio: required parseable ISO date
  - evento.formato: must be one of ['hibrido', 'online', 'presencial']
  - evento.beneficiosParticipar: must be a non-empty array of strings
```

![The deterministic blueprint validator in a real terminal](assets/terminal.png)

Every error names the field and the rule. Fix the draft, not the validator.

---

## Arquitetura

```
SKILL.md                     the orchestrating cycle (5 stages)
references/
  briefing/                  context and the five quick decisions
  criacao/                   blueprint, models, generation, anti-fabrication
  edicao/                    mini-lovable command editing by section path
  auditoria/                 the 12-criterion rubric and metrics
  publicacao/                publication gate and archive semantics
  dashboard/                 the pluggable dashboard contract
  integracoes/               the tracklink plug contract
scripts/
  validar-blueprint.py       structure gate (form)
  calculate_score.py         rubric scoring with alias fallbacks
  verify_sources.py          source snapshot verification
examples/                    canonical inputs (blueprint + audit)
agents/                      openai.yaml (Codex loader)
```

Three principles hold the architecture together:

**The blueprint is data, never code.** A page is a JSON document validated by gates and rendered by the engine — never a generated file that drifts from its source.

**Gates before publication, always.** The publication action runs the validators before any write. A published page that fails a gate is a bug; the action exists so that bug cannot happen.

**Contracts are the product.** The models, the gates, the dashboard and the tracking plug are all contracts in Markdown — the reference implementation is the proof, not the definition.

---

## Metodologia

The engine was not written as documentation after the fact. It was extracted from a production motor that shipped real pages, found its failure modes in real reviews, and pinned each lesson as a rule with a test.

**Determinism over cleverness.** Every gate must be executable by a machine with no judgment calls. The validators are the proof: same input, same verdict, forever.

**Anti-fabrication is the highest rule.** It appears in extraction ("only what exists in the page"), generation ("omit, never guess"), editing ("the command does not invent") and gates ("the audit checks for it"). It is the only rule that overrides a good-looking result.

**Every bug class becomes a regression case.** Wrong-model objects, literal-hex slugs, "NaN dias" event dates, consent checkboxes the UI never rendered — each was found in review, fixed, and pinned. The suite can only grow.

**Review finds what per-task checks miss.** The reference motor's history is explicit about it: the whole-branch review caught generated-but-never-rendered tokens, validated-outside-the-gate checks and an XSS composed of two "safe" findings. That is why the gates exist as executable code and not as instructions.

**The page is the entry point of a system.** A page without tracked CTAs, without first-click attribution, without an audit trail, is a decorated template. The contracts exist so the page does the funnel's work from the first visitor.

---

## Novidades na versão 2.x

**v2.0.0 — the complete cycle.** SemVer and CHANGELOG discipline, the creation references (blueprint, models, generation, copy profiles) with the deterministic validator, the briefing with the five quick decisions, mini-lovable editing with visual tokens, the pluggable contracts (tracklink + dashboard), and the orchestrating SKILL.md.

**v2.1.0 — the tracklink plug.** The contracts now reference the sibling tracking skill as the owner of the tracking contract: every CTA ships as a tracked link, the lead records first-click attribution.

Changelog: [CHANGELOG.md](./CHANGELOG.md) · Releases: [GitHub Releases](https://github.com/luisroquette/My_LP_Makes_Neil_Proud/releases)

---

## Limitações

- **The engine is a contract + validators, not a hosted renderer.** The reference implementation renders in production; this repo defines the system and validates the inputs.
- **Slug renames do not propagate** to already-emitted tracking links — by design, documented in the tracklink contract.
- **The five quick decisions are required.** The engine does not infer objective, evergreen status, theme, length or offer risk — those are the creator's calls, and the cycle asks for them explicitly.
- **Model detection is heuristic and order-sensitive.** The first strong signal wins; ambiguous briefs fall back to universal. When the model matters, select it explicitly.

If a limitation blocks you, that is a design conversation — the contracts are explicit precisely so that conversation happens before the page ships.

---

## Requisitos

- Python 3.10+ (validators only)
- Claude Code or Codex
- No API keys, no database, no network access for the core cycle

---

## Desinstalar

```bash
rm -rf ~/.claude/skills/my-lp-makes-neil-proud
```

Nothing is installed outside the skill directory.

---

## Extensões

- **My_UTMs_Make_Me_Proud** — the tracking layer this repo references (plug v2.1.0).
- **My_MailMKT_makes_Neil_Proud** — the email engine that picks up the lead the page captured.
- **Dashboard contract** — `references/dashboard/contrato-dashboard.md`, consumable by any dashboard implementation.

---

## Ecossistema

| Skill | Layer | Relationship |
|---|---|---|
| My_UTMs_Make_Me_Proud | Tracking | Owns the contract — the LP references it |
| **My_LP_Makes_Neil_Proud** (this repo) | Landing pages | First producer of tracked links |
| My_MailMKT_makes_Neil_Proud | Email nurture | Consumes the leads the pages capture |

Capture → nurture → attribution, one contract.

---

## Documentação

- [SKILL.md](./SKILL.md) — the cycle and quick start
- [references/](./references/) — briefing, creation, editing, audit, publication, dashboard, integrations
- [examples/](./examples/) — canonical inputs
- [CHANGELOG.md](./CHANGELOG.md)

---

## Perguntas frequentes

**Is it free?** Yes. MIT.

**Does it generate pages by itself?** It assembles blueprints from real content or briefs — never from thin air. The gates then audit the result. "Generate a page" without a source or a brief is the one thing the engine refuses.

**Why six models instead of templates?** Because a template recolored still looks like the template. The models differ in structure, contract and render layout — a course and a squeeze do not share a hero.

**What does the audit rubric score?** Twelve criteria derived from three Neil Patel landing-page guides: clarity, congruence, specificity, proof, friction, urgency, and the structural checks each model demands.

**Can the gates be skipped?** No. The publication action validates before writing — there is no path from draft to published that bypasses a gate.

**What happens with a page extracted from a URL that has no price?** The price section is omitted. The page ships without a price instead of with an invented one.

**Does the engine keep the capture form contract on every model?** The three fields (name, phone, email) are a pétrea clause. Models that render capture forms inherit it; reverting requires owner approval.

---

## Colaboradores da comunidade

The contributor table is open. The contribution that matters here: a new bug class found in a gate and pinned as a regression case in the same commit.

---

## Licença

MIT — see [LICENSE](./LICENSE).

---

## Contribuindo

**Every validator rule fix lands with its regression case in the same commit.** Run the canonical examples before opening a PR. Contracts change through discussion in the issue first, code second.

---

## Autor

**Luis Roquette** — Anthropic Select Services Partner, building the CF Gauss marketing stack (LP engine → email engine → tracking) as portable, auditable open-source skills.

<p align="center">
  <a href="https://github.com/luisroquette/My_UTMs_Make_Me_Proud">My_UTMs_Make_Me_Proud</a> ·
  <a href="https://github.com/luisroquette/My_MailMKT_makes_Neil_Proud">My_MailMKT_makes_Neil_Proud</a> ·
  <a href="https://github.com/luisroquette/My_LP_Makes_Neil_Proud">My_LP_Makes_Neil_Proud</a>
</p>
