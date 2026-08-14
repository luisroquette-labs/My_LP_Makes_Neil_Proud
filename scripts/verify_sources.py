#!/usr/bin/env python3
"""Verify the local Neil Patel source snapshots used to derive the skill."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED = {
    "landing-page.md": "ba1d787cec526a47b011ffab95120451dcbf5ad382e5ed8a85a23abbc45614e1",
    "o-guia-definitivo-para-criar-landing-pages-super-convertedoras.md": "9596e9a64b24a5a630425a6a782045935c5f7238ac4ff5ca75628a46cfc7462b",
    "landing-page-o-que-e.md": "6e79b82a5bc8f88325e28b11e0c4c764b10400990ce3f3b5983388f7cc753e2e",
}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=Path.home() / "Downloads")
    args = parser.parse_args()

    result = {}
    mismatch = False
    for filename, expected in EXPECTED.items():
        path = args.source_dir / filename
        if not path.is_file():
            result[filename] = {"status": "missing", "expected_sha256": expected}
            continue
        actual = digest(path)
        status = "match" if actual == expected else "mismatch"
        mismatch = mismatch or status == "mismatch"
        result[filename] = {
            "status": status,
            "expected_sha256": expected,
            "actual_sha256": actual,
        }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if mismatch else 0)


if __name__ == "__main__":
    main()
