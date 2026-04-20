#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path


EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    "_upstreams",
}

EXCLUDED_SUFFIXES = {
    ".pyc",
    ".pyo",
}


def should_include(path: Path, bundle_root: Path, output_paths: set[Path]) -> bool:
    resolved = path.resolve()
    if resolved in output_paths:
        return False
    rel = path.relative_to(bundle_root)
    if any(part in EXCLUDED_DIRS for part in rel.parts):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    return path.is_file()


def build_zip(bundle_root: Path, output: Path) -> dict:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    output_paths = {output.resolve()}
    root_name = bundle_root.name
    files = 0
    bytes_in = 0
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(bundle_root.rglob("*")):
            if not should_include(path, bundle_root, output_paths):
                continue
            rel = Path(root_name) / path.relative_to(bundle_root)
            archive.write(path, rel.as_posix())
            files += 1
            bytes_in += path.stat().st_size
    return {
        "archive": str(output),
        "format": "zip",
        "files": files,
        "inputBytes": bytes_in,
        "archiveBytes": output.stat().st_size,
        "excludedDirs": sorted(EXCLUDED_DIRS),
    }


def test_zip(output: Path) -> bool:
    with zipfile.ZipFile(output) as archive:
        return archive.testzip() is None


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a clean ZIP release package without raw upstream mirrors.")
    parser.add_argument("--bundle-root", default=".")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    bundle_root = Path(args.bundle_root).resolve()
    output = Path(args.output).resolve() if args.output else bundle_root.parent / f"{bundle_root.name}.zip"
    report = build_zip(bundle_root, output)
    report["zipIntegrityTestPassed"] = test_zip(output)
    reports = bundle_root / "reports"
    reports.mkdir(exist_ok=True)
    (reports / "zip-package-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["zipIntegrityTestPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
