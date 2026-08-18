# Design — My_LP_Makes_Neil_Proud v2.0.0

**Data:** 2026-08-18
**Repo:** https://github.com/luisroquette/My_LP_Makes_Neil_Proud
**Estado:** aprovado pelo dono (ondas socráticas 18/08/2026)

## 1. Contexto

O repo é uma skill pública (Claude Code + Codex) que **audita** landing pages contra uma rubrica de 12 critérios derivada de 3 guias do Neil Patel (score 0–100, readiness, fixes P0/P1/P2 com evidência). Único commit `f3ad261` (14/08/2026), sem tags.

Desde então, o sistema real de LPs do CF Gauss (cfgauss-site) evoluiu drasticamente: motor de LP com 6 modelos/estratégias, edição estilo Mini-Lovable, publicação conectada a tracklinks e dashboard de controle (a vir). O objetivo desta atualização é **exportar essa robustez para o repo público** como skill do ciclo completo de LP, versionada conforme SemVer.

## 2. Decisões travadas (ondas socráticas)

| # | Decisão | Escolha |
|---|---------|---------|
| 1 | Papel do repo | **Ciclo completo**: criar → editar (mini-lovable) → auditar (gate de qualidade) → publicar (tracklink) |
| 2 | Relação com o cfgauss | **Metodologia portátil** — o agente aplica o mesmo processo em qualquer projeto/stack; tracklink e dashboard são referências plugáveis |
| 3 | Escopo do estágio de criação | **Motor completo** (blueprint, 6 modelos, heurística, extração de URL/instrução, 5 decisões rápidas, anti-fabricação, gates) **+ perfis de copy** (Giveaway, Empiricus) |
| 4 | Tracklink na publicação | **Contrato + plugável** — a skill define o contrato; o repo do tracklink se conecta depois sem reescrever a skill |
| 5 | Dashboard | **Contrato plugável** — reference própria definindo o que o tracklink expõe e a dashboard consome; implementação fora do escopo desta versão |
| 6 | Versão alvo | **2.0.0** (MAJOR) — tag retroativa `v1.0.0` no commit atual |
| 7 | Artefatos de versionamento | **Tags semver + CHANGELOG.md (Keep a Changelog) + GitHub Release** |
| 8 | Estrutura da skill | **A — Orquestradora**: `SKILL.md` orquestra o ciclo de 5 estágios; cada estágio tem sua pasta em `references/` |

## 3. Visão e versão

- **Nome mantido** (`my-lp-makes-neil-proud`) — URL pública e pasta de instalação não mudam.
- **v2.0.0** = skill do ciclo completo: **Briefing → Criação → Edição (Mini-Lovable) → Auditoria ("Neil Proud") → Publicação (tracklink)**.
- **Idioma:** EN em todo o conteúdo da skill (repo público). Docs internos de processo (este spec, plans) em PT-BR, como no cfgauss.
- **Codex** (`agents/openai.yaml`) mantido.
- **Auditoria continua invocável standalone** (modo direto) além de ser o estágio de qualidade do ciclo.
- MAJOR justificado: o contrato da skill muda de "audita uma LP" para "orquestra o ciclo completo".

## 4. Arquitetura de arquivos (alvo)

```
SKILL.md                          # orquestradora: ciclo, gates, contrato de saída por estágio
README.md                         # reescrito pro ciclo completo + instalação + versionamento
CHANGELOG.md                      # novo — Keep a Changelog
LICENSE · .gitignore              # mantidos
references/
  briefing/contexto-e-decisoes.md     # 5 decisões rápidas + extração de URL + anti-fabricação
  criacao/blueprint.md                # schema: ~20 campos universais + objetos por modelo + visual + seo
  criacao/modelos.md                  # 6 modelos + heurística + quando usar cada
  criacao/geracao.md                  # por URL / por instrução + gates (estrutura→modelo→SEO→contraste)
  criacao/perfis-copy.md              # Giveaway, Empiricus + como criar perfil novo
  edicao/mini-lovable.md              # comandos, data-lp-role, caminho de seção, brief+autosave
  edicao/tokens-visuais.md            # cor/fonte/raio, WCAG AA, .dark por luminância real
  auditoria/                          # v1 movida pra cá INTACTA (source-map, framework, rubric, metrics)
  publicacao/contrato-tracklink.md    # slug↔tracking link, destination_url, thank-you, UTM — plugável
  dashboard/contrato-dashboard.md     # métricas que o tracklink expõe / dashboard consome — plugável
  versionamento.md                    # SemVer do repo + como versionar a skill
scripts/
  calculate_score.py · verify_sources.py   # mantidos (v1)
  validar-blueprint.py                    # novo — espelha validar-estrutura.ts (forma, não conteúdo)
examples/
  example-audit-input.json            # mantido (v1)
  example-briefing-input.json         # novo — entrada do estágio de criação
agents/openai.yaml                   # mantido
```

Notas de decisão aprovadas:
- `references/auditoria/` move os 4 arquivos da v1 de `references/` para a subpasta, **sem mudança de conteúdo** (mudança de path interno, coberta pelo MAJOR).
- `validar-blueprint.py` valida a **forma** do JSON blueprint (determinístico, sem LLM), espelhando `validar-estrutura.ts`. Gates de conteúdo/SEO/contraste ficam **instrucionais** (o agente aplica), não em script.
- `docs/` (specs e plans internos) permanece no repo como trilha de auditoria, mas **nunca é carregada pela skill** em execução — a skill lê apenas `references/` e `scripts/`. Instalação pública continua idêntica.

## 5. Estágio 1 — Briefing

Arquivo: `references/briefing/contexto-e-decisoes.md`

- **Entradas:** URL de página existente (extração) OU instrução em texto livre.
- **Extração de URL:** fetch seguro (anti-SSRF), LLM monta o blueprint **sem fabricar** preço/prazo/credencial ausente — omite a seção sem conteúdo. Slug auto-sugerido a partir da URL, com decodificação de caracteres percent-encoded (bug real de acento já corrigido no motor).
- **5 decisões rápidas** (não extraíveis — decisão de quem cria, não fato da página): objetivo, evergreen, tema, comprimento, riscoOferta.
- **Anti-fabricação** (princípio transversal): dado ausente é omisso/`Not verified`, nunca zero nem inventado.

## 6. Estágio 2 — Criação

Arquivos: `references/criacao/`

### 6.1 `blueprint.md`

Schema `LpBlueprint`:
- ~20 campos universais (headline, subheadline, público-alvo, provaSocial, CTA, seo, thankYou, tema, rastreamento, etc.);
- objetos por modelo: `evento`, `captura`, `lancamento` (squeeze não tem objeto próprio — só campos universais);
- `visual` opcional: tokens de cor/fonte/raio + arranjo de hero;
- `seo`: metaTitle, metaDescription, openGraph/twitter.
- Contrato: **ausência ≠ zero** — campo ausente não pode ser tratado como 0/ok (padrão de bug real medido 4× em 3 repos).

### 6.2 `modelos.md`

6 modelos com heurística de classificação em ordem:
1. **universal** (fallback) — workshop/palestra
2. **curso** — venda de curso/formação
3. **evento** — webinar/meetup/encontro (RSVP presencial/online/híbrido)
4. **captura** — lead magnet (ebook, checklist, planilha, template) — formulário DENTRO do hero
5. **squeeze** — 1 tela, mínima fricção
6. **lancamento** — coming soon/pré-lançamento, 1 tela + faixa legal

Regras por modelo:
- Heurística testada em ordem: curso antes de evento antes de captura ("curso gratuito com ebook" é curso; "webinar com material" é evento).
- squeeze/lancamento: sem header, 1 tela + faixa legal (LGPD).
- **Cláusula pétrea (contrato comercial): toda LP tem formulário, 100% conectado ao funil/Trello certo. Formulário mínimo = nome + telefone + email (3 campos).** Reverter exige aprovação do dono.
- Todo campo que o render consome exige validação de FORMA, não só de presença (`.join()` em undefined derruba página publicada — bug real).

### 6.3 `geracao.md`

Fluxo de geração (por URL ou instrução) + gates em cascata:
1. `validar-estrutura` — forma do JSON, campo por campo (bloqueante, roda antes de tudo);
2. `validar-<modelo>` — regras do modelo (bloqueante);
3. `validar-seo` — bloqueante se `evergreen:true` (título 30–65 chars, descrição 120–160);
4. `validar-contraste` — WCAG AA (bloqueante quando `visual` presente).

Geração NUNCA salva/publica sozinha: sempre preenche o rascunho para revisão humana. Rascunho pode ficar incompleto; publicação não.

### 6.4 `perfis-copy.md`

- Perfis de estilo: **Giveaway** (sorteio/recompensa) e **Empiricus** (análise de mercado, autoridade, urgência editorial).
- Formato canônico de perfil: tom, estrutura de prova, padrões de headline, CTAs — para criar perfis novos.

### 6.5 `scripts/validar-blueprint.py`

Validação determinística da forma do blueprint (estrutura de campos, tipos, allowlist de modelo, seções por modelo). Sem LLM. Saída: lista de erros de forma + exit code.

## 7. Estágio 3 — Edição Mini-Lovable

Arquivos: `references/edicao/`

### 7.1 `mini-lovable.md`

- Edição por **comando de texto livre**: agente recebe o comando → monta plano de edição → resolve o alvo por caminho de seção (`ContextoComandoLovable` / `secaoHero`) → aplica.
- Brief de edição com **autosave**; correção de rascunho gerado (`corrigir-rascunho-gerado`); reclassificação de modelo quando o comando muda a natureza da LP.
- **`data-lp-role`** como contrato obrigatório nos elementos (hero, texto, formulário) — sem ele, comandos de texto não encontram o alvo.
- Âncora de formulário por modelo (`ancoraFormularioLp`) — CTA de header/footer aponta pro formulário real do modelo (bug real de botão morto em LP publicada).

### 7.2 `tokens-visuais.md`

- Tokens de cor/fonte/raio aplicados inline quando `visual` existe; fallback sem visual intacto.
- `.dark` (cor de texto/badge) derivado da **luminância real do fundo** (`fundoEhEscuro`), não do campo `tema` — bug real de texto invisível.
- Contagem regressiva client-only; foco visual tipo imagem vs vídeo; transform de mídia de fundo.

## 8. Estágio 4 — Auditoria ("Neil Proud" como gate de qualidade)

- Arquivos da v1 (`source-map.md`, `framework.md`, `rubric.md`, `metrics.md`) movem para `references/auditoria/` **sem mudança de conteúdo**.
- Papel no ciclo: toda LP criada/editada passa pela rubrica de 12 critérios **antes de publicar** — score 0–100, readiness, até 5 fixes P0/P1/P2 com evidência e rastreabilidade `[S1][S2][S3]`.
- Continua invocável standalone (modo direto, como na v1).
- `calculate_score.py` e `verify_sources.py` mantidos.

## 9. Estágio 5 — Publicação (contrato do tracklink)

Arquivo: `references/publicacao/contrato-tracklink.md`

Duas metades:
- **(a) Obrigações da LP publicada** (portátil, qualquer host): slug canônico, SEO por LP (metaTitle/description, OpenGraph/Twitter — nunca o card genérico do site), schema JSON-LD (Course com precificação / WebPage), LGPD, thank-you page, entrada no sitemap.
- **(b) Contrato do sistema de tracklink** (plugável): slug ↔ `destination_url`, UTM/parâmetros de origem, mapeamento thank-you, atualização atômica de tracking links quando o slug muda. **Estado: aguardando o repo do tracklink** — quando ele subir, preenche este contrato; a skill não se reescreve.

## 10. Dashboard (contrato plugável)

Arquivo: `references/dashboard/contrato-dashboard.md`

- **O tracklink expõe:** cliques por LP, origem/canal, período, conversões via thank-you.
- **A dashboard consome:** lista de LPs emitidas, cliques, CPL, status por LP.
- **Estado explícito no arquivo: implementação fora do escopo da v2.0.0** — pluga junto com o repo do tracklink, na fase de grafiar e concatenar os sistemas.

## 11. Versionamento (SemVer 2.0.0)

Arquivo: `references/versionamento.md`

- MAJOR = contrato da skill muda · MINOR = estágio/reference compatível novo · PATCH = correção.
- Ações desta release:
  1. Tag retroativa **`v1.0.0`** no commit `f3ad261`;
  2. **CHANGELOG.md** (Keep a Changelog) com Unreleased→2.0.0 e 1.0.0;
  3. Tag **`v2.0.0`** no commit final + **GitHub Release** com release notes.

## 12. Verificação

- **Carga real sem o app:** executar o ciclo completo da skill contra uma LP pública real — auditoria (v1 já cobre) + criação (gerar blueprint de uma URL real) + edição (aplicar um comando) + gate de publicação.
- **Scripts determinísticos:** `calculate_score.py` e `validar-blueprint.py` rodando contra os `examples/`.
- **README** reescrito: ciclo completo, instalação Codex/Claude Code, seção de versionamento.

## 13. Fora de escopo (deliberado)

- Implementação da dashboard (contrato apenas).
- Implementação do sistema de tracklink (contrato apenas; repo próprio virá depois).
- Portar o código TS do motor (a skill é metodologia, não fork de sistema).
- CI/automação de release (artefatos de versionamento são manuais).

## 14. Critérios de aceite

1. `SKILL.md` orquestra os 5 estágios com contratos de saída por estágio.
2. Auditoria v1 funcional e invocável standalone com os mesmos arquivos (novo path).
3. Referências de criação cobrem blueprint, 6 modelos, geração, perfis de copy e gates.
4. `validar-blueprint.py` valida forma do blueprint nos `examples/`.
5. Contratos de tracklink e dashboard marcados como plugáveis.
6. Tags `v1.0.0` (retroativa) e `v2.0.0` + CHANGELOG + GitHub Release.
7. README em EN com ciclo completo e instalação.
