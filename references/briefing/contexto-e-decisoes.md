# Briefing: Context and Decisions

The briefing stage converts an input into a filled blueprint draft. It exists because the LLM must know what is fact (extractable from the source) and what is decision (belongs to the creator).

## Inputs

Two entry points:

1. **URL of an existing page** — extraction. The page is the source of truth for facts.
2. **Free-text instruction** — a brief describing the offer, audience, model, and goal. Anything the instruction does not state is omitted.

## URL extraction

1. **Fetch safely.** SSRF-guarded fetching only: allowlisted public hosts, no private-network targets, no credentials in the URL, size/time limits. A page that cannot be fetched safely fails the extraction — it never falls back to guessing.
2. **Extract only what exists.** Price, deadline, credentials, or any claim not present in the real page → omit the section entirely. Anti-fabrication is the highest rule of extraction: a missing price is a missing price, not an estimated one.
3. **Suggest the slug from the URL path**, percent-decoded. `%C3%AD` must become `í` — a slug with literal hex escapes is a real bug (production confirmed). The creator can override.
4. **Output is a draft only.** Extraction fills the blueprint for human review. It never saves, never publishes, and never marks anything as published.

## Five quick decisions

Five fields are decisions of the creator — they are not facts of the page and must not be silently guessed. Collect them explicitly (a selector above the editor, not buried in JSON):

| Field | Question it answers |
|---|---|
| `objetivo` | What is the single conversion? |
| `evergreen` | Does the SEO gate block publication? |
| `tema` | Light or dark? |
| `comprimento` | Short, medium, or long page? |
| `riscoOferta` | How much proof does this offer require? |

The `modelo` is classified by heuristic or explicit selection — see `../criacao/modelos.md`.

## Anti-fabrication (transversal principle)

Applies to every stage, not just extraction:

- A missing datum is **omitted** or labeled **Not verified** — never zero, never "no data", never a plausible placeholder.
- No invented testimonials, prices, deadlines, or credentials — in any profile, in any model.
- When the source and the instruction disagree, surface the conflict to the creator instead of picking one.
