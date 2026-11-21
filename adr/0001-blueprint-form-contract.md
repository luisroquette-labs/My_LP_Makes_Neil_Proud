# Blueprint form contract

## Context

The blueprint validator checks form structure against the documented production model. The production `ArranjoHero` is nested, while this portable skill accepts the allowed arrangement name as a flat string and converts it at integration. Each declared model has its own required object, and optional sections may be omitted.

## Decision

Keep the hero arrangement allowlist aligned with the production type. Treat a missing or wrong per-model object as a form error. Accept absent optional sections, but reject wrong shapes when a section is present.

## Consequences

Integration must convert the flat hero value to the production shape. A new model or hero arrangement requires updates to the contract and validator together.
