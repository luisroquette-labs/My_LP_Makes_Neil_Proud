# LP Models

Six models cover the LP strategies. A model is a strategy: it decides layout, form position, header presence, and which per-model object the blueprint carries.

## Classification

Classify in this order — the first match wins:

1. **curso** — course/training sale. Explicit markers: curso, formação, treinamento, módulos, mentoria paga. "Curso gratuito com ebook" is still curso.
2. **evento** — RSVP gathering. Explicit markers: webinar, meetup, encontro, workshop with a date and registration. "Webinar with material" is still evento.
3. **captura** — lead magnet. Explicit markers: ebook, checklist, planilha, whitepaper, template gratuito.
4. **squeeze** — no automatic heuristic. Explicit selection only.
5. **lancamento** — coming soon / pre-launch. Explicit selection only.
6. **universal** — fallback for anything else (workshops, palestras, institutional offers). CF Gauss workshops are `modelo: curso` by decision — the universal fallback is for pages with no dedicated model.

Workshop/palestra are deliberately universal/curso — they do not auto-classify as evento.

## Per-model rules

| Model | Object | Layout | Form |
|---|---|---|---|
| `universal` | none | default chrome (header + footer) | standard section form |
| `curso` | none (uses universal fields + course sections: precificação, cronograma, faq, credenciais) | default chrome | lead form when `objetivo: captura`; checkout CTA otherwise — but never without a form |
| `evento` | `evento` | default chrome; RSVP logistics as chips; countdown card | RSVP form |
| `captura` | `captura` | default chrome; **form INSIDE the hero, above the fold** | lead form (`#captura-form`) |
| `squeeze` | none | **one screen, no header** — footer kept as legal strip (LGPD) | 3-field form in hero (`#squeeze-form`) |
| `lancamento` | `lancamento` | **one screen, no header** + legal strip | 3-field form in hero |

## Layout contract

- **One-screen models** (`squeeze`, `lancamento`): no `HeaderLp`. The promised "one screen" must hold on mobile — the page chrome (~180px of header) broke it before this rule existed.
- **Form anchor per model**: header/footer CTAs must point at the form the model actually renders (`ancoraFormularioLp` equivalent). Pointing every model at a nonexistent `#lead-form` left dead buttons on every published LP.
- **Countdown** (evento, lancamento): client-only, updates on an interval, never renders "NaN days". A missing/placeholder date must never assert "Launched!" without a date.

## Commercial contract (pétrea clause)

Every LP has a form, 100% connected to the right funnel. Minimum fields: **name + phone + email** — even for squeeze (the market-standard "email only" was rejected by the owner; the 3-field contract is commercial, not a design choice). Reversing requires owner approval.
