#!/usr/bin/env python3
"""Atomically stage a temporary image, with digest-based cache reuse."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import tempfile
from pathlib import Path

from PIL import Image


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect(path: Path) -> tuple[int, int, str]:
    with Image.open(path) as image:
        image.verify()
    with Image.open(path) as image:
        return image.width, image.height, image.format or "unknown"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--manifest", help="Optional JSON manifest path")
    args = parser.parse_args()

    src = Path(args.src).expanduser().resolve(strict=True)
    out = Path(args.out).expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    source_hash = sha256(src)

    reused = False
    if out.exists() and out.stat().st_size == src.stat().st_size:
        try:
            reused = sha256(out) == source_hash
        except OSError:
            reused = False

    if not reused:
        handle, temp_name = tempfile.mkstemp(prefix=f".{out.stem}-", suffix=out.suffix, dir=out.parent)
        os.close(handle)
        temp = Path(temp_name)
        try:
            shutil.copy2(src, temp)
            inspect(temp)
            os.replace(temp, out)
        finally:
            if temp.exists():
                temp.unlink()

    width, height, image_format = inspect(out)
    manifest = {
        "source": str(src),
        "staged": str(out),
        "sha256": source_hash,
        "bytes": out.stat().st_size,
        "width": width,
        "height": height,
        "format": image_format,
        "cache_reused": reused,
    }
    if args.manifest:
        manifest_path = Path(args.manifest).expanduser().resolve()
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False))


if __name__ == "__main__":
    main()

