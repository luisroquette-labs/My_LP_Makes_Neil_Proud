# Null score alias fallback

## Context

The scoring input accepts current metric names and legacy aliases. Some exports include `page_views: null` alongside a populated `unique_visitors` field.

## Decision

Treat an explicit null `page_views` as absent and use `unique_visitors` for that fallback. Keep the metric calculation deterministic.

## Consequences

A null alias cannot erase a valid visitor count. Score changes must preserve this case in a regression check.
