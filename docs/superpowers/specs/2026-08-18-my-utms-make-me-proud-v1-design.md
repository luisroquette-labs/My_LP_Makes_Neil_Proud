# Design — My_UTMs_Make_Me_Proud v1.0.0 (+ My_LP_Makes_Neil_Proud v2.1.0)

**Data:** 2026-08-18
**Repos:** https://github.com/luisroquette/My_UTMs_Make_Me_Proud (novo) · https://github.com/luisroquette/My_LP_Makes_Neil_Proud (sobe pra v2.1.0)
**Estado:** aprovado pelo dono (ondas socráticas 18/08/2026, 4 seções de design)

## 1. Contexto

O My_LP_Makes_Neil_Proud v2.0.0 (publicado 18/08/2026) exporta o ciclo completo de LPs do CF Gauss como skill pública, com dois contratos plugáveis marcados "aguardando o repo do tracklink": `references/publicacao/contrato-tracklink.md` (metade b) e `references/dashboard/contrato-dashboard.md`.

O sistema real de tracking links do cfgauss-site (worktree `motor-lp-taxonomia-20260815`, em produção desde 13/08/2026) está maduro: criação em 3 modos (individual/massa/todas as LPs), rota `/t/[slug]`, atribuição first/last click até a compra, cron de saúde com detecção de bloqueio de datacenter, analytics diária, bundle atômico LP+campanha+link.

Esta iteração exporta esse sistema como o repo público **My_UTMs_Make_Me_Proud** (skill do ciclo completo do tracking, **canal-agnóstica**) e pluga o resultado no repo do LP (**v2.1.0**). Objetivo de longo prazo declarado pelo dono: wrapper omnichannel de marketing com todas as features do CF Gauss para replicar em outras empresas — o tracklink é a **camada de tracking dessa futura plataforma**; a LP é apenas a primeira integração, não a única produtora de links.

## 2. Decisões travadas (ondas socráticas 18/08/2026)

| # | Decisão | Escolha |
|---|---------|---------|
| 1 | Forma da entrega | **Repo novo + plug no LP** |
| 2 | Papel do repo | **Metodologia portátil + scripts determinísticos** |
| 3 | Fonte da verdade do contrato | **Tracklink dono do contrato** — o LP referencia |
| 4 | Escopo | **Ciclo completo do tracking** (criação → clique → atribuição → saúde → métricas) |
| 5 | Nome do repo | **My_UTMs_Make_Me_Proud** (definido pelo dono) |
| 6 | Versão inicial | **1.0.0** (sistema em produção desde 13/08; sem histórico anterior no repo) |
| 7 | Plug no ciclo do LP | **Recomendado, não obrigatório** → LP sobe MINOR **v2.1.0** |
| 8 | Estrutura interna | **Espelho do LP com fenda núcleo/integrações** — núcleo canal-agnóstico; LP é a 1ª integração |

## 3. Visão e versão

- Repo novo nasce em **1.0.0**: skill pública (Claude Code + Codex) do ciclo completo de tracking links.
- **Núcleo canal-agnóstico:** qualquer sistema da plataforma (LP, e-mail, workshop, anúncio, WhatsApp) produz links que este sistema cria, rastreia, mede e zela.
- `references/integracoes/` acumula canais: cada integração é um arquivo; a skill não se reescreve (mesmo princípio do tracklink no repo do LP, invertido).
- Repo do LP sobe para **v2.1.0 (MINOR)**: contratos plugáveis passam a referenciar o repo novo; estágio de publicação ganha "padrão recomendado" sem virar obrigatório.
- Idioma: EN no conteúdo das skills (repos públicos); docs de processo (este spec, plans) em PT-BR.
- URLs assumidas: ambos na conta GitHub `luisroquette`.

## 4. Arquitetura de arquivos do repo novo

```
SKILL.md                  # orquestradora: ciclo do tracking + regras duras transversais
README.md                 # ciclo completo + instalação + como plugar um canal novo + visão da suite
CHANGELOG.md · LICENSE · .gitignore
references/
  nucleo/criacao.md       # slug, UTMs, destinos, 3 modos, concurrency, trilha, expiração
  nucleo/clique.md        # /t/[slug], exclusão bots/prefetch, dedup 30s, redirect nunca bloqueado
  nucleo/atribuicao.md    # cookie HMAC 90d, first/last click → lead/compra
  nucleo/saude.md         # cron, probe duplo, SSRF guard, datacenter block, alertas
  nucleo/metricas.md      # daily stats + analytics — o que o tracklink EXPÕE (dashboard consome)
  integracoes/lp.md       # contrato LP ↔ tracklink (bundle, gate de publicação, Meta Pixel)
  integracoes/modelo-nova-integracao.md  # como acumular o próximo canal (mailmkt, anúncios…)
  versionamento.md
scripts/validar-tracking-link.py
examples/example-tracking-link.json
agents/openai.yaml
```

## 5. Núcleo — Criação

- **3 modos:** individual / em massa (até 25) / todas as LPs de uma campanha (até 250, via batch atômico).
- **Slug:** obrigatório, único, `^[a-z0-9]+(-[a-z0-9]+)*$`, ≤80; normalização automática (acentos removidos, minúsculas, hífens); hash curto quando estoura 80.
- **UTMs:** source/medium/campaign obrigatórias (≤120); content/term opcionais; inferência de source por hostname do destino e de medium por source.
- **Destino:** `^https?://`, ≤2048, **sem credenciais na URL**, **proibido apontar para outro `/t/`** (loop); `tracked_destination_url` = destino + UTMs (≤4096).
- **Ciclo de vida:** ativo/pausado, soft delete, `expires_at` (expiração bloqueia resolução e contagem).
- **Optimistic concurrency** (`updated_at` esperado) + **trilha de auditoria** em toda mutação.

## 6. Núcleo — Clique

- Rota curta `/t/[slug]`: HEAD não conta; bots e prefetch não contam; dedup 30s por cookie por slug (reusa click_id).
- Ordem: **resolve → registra → redireciona 302**. **Métrica nunca bloqueia o redirect** (falha logada, redirect segue) — regra dura.
- Headers do redirect: `Cache-Control: no-store`, `X-Robots-Tag: noindex, nofollow`, `Referrer-Policy: no-referrer`.
- 404 para slug inválido; 503 "Tracking indisponível" quando nem o fallback resolve.
- Cookie de atribuição HMAC-SHA256 selado, 90 dias, first/last click.

## 7. Núcleo — Atribuição

- Pontos de conversão (formulário de lead, checkout) leem o cookie e gravam `first/last_tracking_click_id` no evento de lead e `first/last_marketing_click_id` na compra.
- Join clique → link → campanha resolve first/last touch.
- Contrato: **o clique é rastreável do link à compra**.

## 8. Núcleo — Saúde

- Cron de health-check: 100 links/run, concorrência 6, probe duplo (HEAD primário + confirmação).
- Estados: `unchecked|healthy|warning|broken` + `health_http_status`, `health_checked_at`, `health_error_code`.
- **SSRF guard:** blocklist IPv4/IPv6 (RFC1918, link-local, multicast) + DNS interceptor rejeitando IP privado.
- **Bloqueio de datacenter (lição de 16/08):** falha sistêmica (≥5 suspeitos em ≥3 hostnames) → links suspeitos PULADOS com estado preservado (não derrubam a run); timeouts 12s/25s.
- Alerta por e-mail **apenas quando o estado piora**; alerta de falha operacional quando `failures>0 || conflicts>0 || truncated`.

## 9. Núcleo — Métricas

- **Contagem:** agregado diário (`daily_stats`, timezone America/Sao_Paulo) + eventos granulares (device_type validado, referrer só hostname, snapshot de UTMs e destino).
- **Analytics** por período 7/30/90: série diária com calendário preenchido — **ausência ≠ zero** (dia sem clique aparece explicitamente, não vira 0 silencioso — padrão de bug real medido 4× em 3 repos), top links, origens, dispositivos, referrers.
- **O tracklink EXPÕE:** cliques por link, origem/canal, período, conversões via pontos de conversão. A dashboard (fora desta iteração) consome isso.
- Export de links CSV/XML (não de cliques individuais).

## 10. Integração LP (`integracoes/lp.md`)

Espelha o vínculo real entre os dois sistemas:

- FK `tracking_links.landing_page_id → landing_pages(id)`.
- **Bundle atômico:** LP principal + thank-you + oferta + campanha + tracking link numa transação única; slug determinístico da campanha; upsert idempotente do link por slug; colisões `campaign_slug_collision` / `tracking_slug_collision` tratadas.
- **Gate de publicação:** LP `published` exige tracking link ativo com campanha — no cfgauss é trigger obrigatório; na skill portátil entra como **padrão recomendado** (decisão 7).
- **Meta Pixel** da LP via join link → campanha → `meta_pixel_id`.
- **Ausência documentada honestamente:** rename de slug da LP NÃO atualiza tracking links automaticamente; a consistência volta no próximo save do bundle. O contrato registra isso como obrigação de quem integra — sem inventar trigger de rename que não existe.

## 11. Scripts e exemplos

- `scripts/validar-tracking-link.py`: espelha as constraints do banco — slug (regex, ≤80), destino (`^https?://`, ≤2048, sem credencial, sem loop `/t/`), UTMs obrigatórias (≤120), `tracked_destination_url` = destino + UTMs. Determinístico, sem LLM, exit 0/1.
- `examples/example-tracking-link.json`: link válido + casos quebrados cobertos em teste do script.

## 12. Plug no repo do LP (v2.1.0)

1. `references/publicacao/contrato-tracklink.md`: metade (b) sai de "aguardando o repo" e **referencia** `My_UTMs_Make_Me_Proud` como fonte da verdade.
2. `references/dashboard/contrato-dashboard.md`: passa a consumir `nucleo/metricas.md` do repo novo.
3. `SKILL.md` estágio 5: ganha "padrão recomendado" apontando pro contrato, sem obrigatoriedade.
4. `CHANGELOG.md`: `[2.1.0] - 2026-08-18`.
5. README do LP: menção ao repo do tracklink na seção de ecossistema.

## 13. Versionamento e artefatos

- **Repo novo:** `[1.0.0] - 2026-08-18` no CHANGELOG (Keep a Changelog), tag `v1.0.0`, GitHub Release com release notes, `references/versionamento.md` (MAJOR = contrato da skill muda · MINOR = estágio/integração compatível novo · PATCH = correção).
- **Repo do LP:** tag `v2.1.0` + CHANGELOG + Release.

## 14. Verificação

1. **Carga real sem o app:** resolver `/t/lp-treinamento-lovable` em produção → 302 para a LP certa com headers corretos.
2. Extrair as constraints reais do banco e validar com `validar-tracking-link.py` → **TRACKING VALID** (análogo ao FORM VALID do LP).
3. Lógica de saúde contra a lista real de links (o cron real classifica 35) → bater estados.
4. Atribuição nos pontos de conversão reais (cookie → first/last ids → compra).
5. Repo do LP pós-plug: 3 scripts verdes + link-checker dos references apontando pro repo novo.

## 15. Fora de escopo (deliberado)

- Implementação da dashboard (contrato apenas).
- Wrapper omnichannel de marketing (próxima iteração; os dois repos saem prontos pra concatenar).
- Portar o código TS real (skill é metodologia + scripts determinísticos, não fork).
- Atualização automática de tracking links em rename de slug de LP (não existe no sistema real; documentado como ausência na seção 10).

## 16. Critérios de aceite

1. Repo `My_UTMs_Make_Me_Proud` no GitHub com a estrutura da seção 4, tag `v1.0.0`, CHANGELOG e Release.
2. `SKILL.md` orquestra o ciclo de 5 estágios com regras duras transversais.
3. `validar-tracking-link.py` valida a forma do link nos `examples/`.
4. `integracoes/lp.md` espelha o vínculo real (bundle, gate, Meta Pixel, ausência documentada).
5. `integracoes/modelo-nova-integracao.md` permite acumular o próximo canal sem reescrever a skill.
6. Repo do LP em `v2.1.0` com os contratos referenciando o repo novo.
7. Carga real executada e documentada (seção 14).
