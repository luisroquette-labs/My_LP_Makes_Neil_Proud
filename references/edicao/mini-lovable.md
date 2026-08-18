# Mini-Lovable Editing

The editing stage turns natural-language commands into blueprint changes. The user says what they want in free text; the agent plans the edit, resolves the target section, and applies it — without touching anything else.

## Command flow

1. **Receive the command** in free text ("make the hero darker", "change the price to R$ 97", "add a testimonial").
2. **Plan the edit.** Identify: which blueprint field(s), which section, and whether the change affects the model classification.
3. **Resolve the target by section path** (`ContextoComandoLovable` equivalent): commands reference named sections (hero, prova, preço, faq), not raw JSON paths. A `secaoHero` resolver maps "hero" correctly for every model — including one-screen models where the hero is the whole page.
4. **Apply surgically.** Only the targeted fields change. Everything else stays byte-identical.
5. **Re-validate.** After every edit, re-run the gates from `../criacao/geracao.md`. An edit that breaks a gate is refused with the gate's error — it is never silently applied.

## Editing elements contract

The rendered page marks its editable elements so commands find their target:

- `data-lp-role` on every editable element: `hero`, `texto`, `form`, `cta`, `prova`, `preco`, `faq`.
- **Without `data-lp-role`, text commands have no target** — a page built without it is not editable by command. This is a build contract, not an option.
- The form anchor is per model (`ancoraFormularioLp` equivalent): a header/footer CTA must point at the form the model actually renders. Pointing every model at one hardcoded anchor left dead buttons on every published LP (real bug).

## Edit brief with autosave

- Every editing session keeps a **brief** — the accumulated set of user commands and decisions.
- The brief **autosaves**; an interrupted session resumes from the last saved brief instead of losing the edits.

## Rascunho correction and reclassification

- **Generated-draft correction:** after a generation, the agent repairs small well-known defects in the draft (missing pinned model, placeholder slugs) before the creator reviews it. It never invents content to fill gaps.
- **Model reclassification:** when an edit changes the nature of the LP (a lead magnet becomes a paid course), reclassify the model with the heuristic in `../criacao/modelos.md` and migrate the blueprint to the new model's object. Reclassifying to a model without a heuristic (squeeze, lancamento) requires explicit creator confirmation.

## Hard rules

- Edits never touch the commercial contract: the form and its three fields stay.
- Edits never publish. Publication is a separate stage.
- Edits never fabricate: "add a testimonial" with no provided testimonial asks for one instead of writing a fake.
