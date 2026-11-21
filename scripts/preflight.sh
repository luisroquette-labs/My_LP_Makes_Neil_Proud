#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_comments.py
python3 scripts/validar-blueprint.py --input examples/example-briefing-input.json
python3 scripts/calculate_score.py --input examples/example-audit-input.json >/dev/null
