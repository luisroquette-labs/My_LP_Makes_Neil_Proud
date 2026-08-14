#!/usr/bin/env python3
"""Calculate Neil Patel LP adherence score and supplied performance metrics."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


WEIGHTS = {
    "objective_intent": 10,
    "offer": 15,
    "message_aida": 15,
    "cta_focus": 10,
    "form_friction": 10,
    "proof_trust": 10,
    "visual_ux": 10,
    "mobile_performance": 5,
    "seo_channel": 5,
    "data_privacy": 4,
    "measurement": 3,
    "aftercare": 3,
}


def ratio(numerator: float | None, denominator: float | None, scale: float = 1.0) -> float | None:
    if numerator is None or denominator is None or denominator <= 0:
        return None
    return round(numerator / denominator * scale, 2)


def number(value: Any, name: str) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"Metric {name} must be a number")
    value = float(value)
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"Metric {name} must be finite and non-negative")
    return value


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError("Input must be a JSON object")
    scores = payload.get("scores", {})
    if not isinstance(scores, dict):
        raise ValueError("scores must be a JSON object")
    unknown = sorted(set(scores) - set(WEIGHTS))
    if unknown:
        raise ValueError(f"Unknown score keys: {', '.join(unknown)}")

    not_applicable_raw = payload.get("not_applicable", [])
    if not isinstance(not_applicable_raw, list) or not all(isinstance(key, str) for key in not_applicable_raw):
        raise ValueError("not_applicable must be a list of criterion IDs")
    not_applicable = set(not_applicable_raw)
    unknown_na = sorted(not_applicable - set(WEIGHTS))
    if unknown_na:
        raise ValueError(f"Unknown not_applicable keys: {', '.join(unknown_na)}")
    overlap = sorted(not_applicable & {key for key, value in scores.items() if value is not None})
    if overlap:
        raise ValueError(f"Criteria cannot be scored and N/A: {', '.join(overlap)}")

    points = 0.0
    scored_weight = 0
    applicable_weight = sum(weight for key, weight in WEIGHTS.items() if key not in not_applicable)
    detail: dict[str, Any] = {}
    for key, weight in WEIGHTS.items():
        if key in not_applicable:
            detail[key] = {"weight": weight, "score": None, "points": None, "state": "not_applicable"}
            continue
        value = scores.get(key)
        if value is None:
            detail[key] = {"weight": weight, "score": None, "points": None, "state": "unscored"}
            continue
        if isinstance(value, bool):
            raise ValueError(f"Score for {key} must be numeric")
        value = float(value)
        if not math.isfinite(value) or not 0 <= value <= 5:
            raise ValueError(f"Score for {key} must be finite and between 0 and 5")
        if not math.isclose(value * 2, round(value * 2)):
            raise ValueError(f"Score for {key} must use 0.5 increments")
        earned = weight * value / 5
        points += earned
        scored_weight += weight
        detail[key] = {"weight": weight, "score": value, "points": round(earned, 2), "state": "scored"}

    adherence_raw = ratio(points, scored_weight, 100)
    adherence = round(adherence_raw, 1) if adherence_raw is not None else None
    metrics = payload.get("metrics", {})
    if not isinstance(metrics, dict):
        raise ValueError("metrics must be a JSON object")
    visitors = number(metrics.get("unique_visitors"), "unique_visitors")
    views = number(metrics.get("page_views", visitors), "page_views")
    visits = number(metrics.get("total_visits", metrics.get("visits", views)), "total_visits")
    leads = number(metrics.get("valid_leads", metrics.get("leads")), "valid_leads")
    spend = number(metrics.get("attributable_spend", metrics.get("spend")), "attributable_spend")
    bounces = number(metrics.get("visits_without_action", metrics.get("bounces")), "visits_without_action")
    conversions = number(metrics.get("conversions", leads), "conversions")
    clicks = number(metrics.get("cta_clicks"), "cta_clicks")
    if bounces is not None and visits is not None and bounces > visits:
        raise ValueError("visits_without_action cannot exceed total_visits")
    performance = {
        "unique_visitors": visitors,
        "conversion_rate_pct": ratio(conversions, visitors, 100),
        "cta_ctr_pct": ratio(clicks, views, 100),
        "cpl": ratio(spend, leads),
        "bounce_rate_pct": ratio(bounces, visits, 100),
    }
    return {
        "adherence_score": adherence,
        "coverage_pct": ratio(scored_weight, applicable_weight, 100),
        "scored_weight": scored_weight,
        "applicable_weight": applicable_weight,
        "excluded_weight": 100 - applicable_weight,
        "provisional": adherence is None or scored_weight < applicable_weight,
        "earned_points": round(points, 2),
        "criteria": detail,
        "performance_metrics": performance,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="JSON file path or '-' for stdin")
    args = parser.parse_args()
    if args.input == "-":
        import sys
        payload = json.load(sys.stdin)
    else:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    try:
        result = calculate(payload)
    except (TypeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
