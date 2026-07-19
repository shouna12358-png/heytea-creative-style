#!/usr/bin/env python3
"""Composite F/coarse and I/fine title layers onto one poster base in one process."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops


def measure(value: str, total: int) -> int:
    if value.endswith("%"):
        return round(float(value[:-1]) / 100 * total)
    return round(float(value))


def extract_ink(path: Path, threshold: int) -> Image.Image:
    rgba = Image.open(path).convert("RGBA")
    red, green, blue, source_alpha = rgba.split()
    gray = Image.merge("RGB", (red, green, blue)).convert("L")
    darkness = gray.point(lambda px: 255 if px < threshold else 0, mode="L")
    alpha = ImageChops.multiply(darkness, source_alpha)
    bbox = alpha.getbbox()
    if not bbox:
        raise ValueError(f"No dark title ink found in {path}")
    alpha = alpha.crop(bbox)
    ink = Image.new("RGBA", alpha.size, (0, 0, 0, 255))
    ink.putalpha(alpha)
    return ink


def composite(base: Image.Image, title_path: Path, out: Path, x: str, y: str, width: str, threshold: int) -> None:
    title = extract_ink(title_path, threshold)
    target_width = measure(width, base.width)
    target_height = round(title.height * target_width / title.width)
    title = title.resize((target_width, target_height), Image.Resampling.LANCZOS)
    result = base.copy()
    result.alpha_composite(title, (measure(x, base.width), measure(y, base.height)))
    out.parent.mkdir(parents=True, exist_ok=True)
    result.convert("RGB").save(out, quality=95, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--title-f", required=True, help="F title layer; coarse crayon family")
    parser.add_argument("--title-i", required=True, help="I title layer; fine hard-pencil family")
    parser.add_argument("--out-f", required=True)
    parser.add_argument("--out-i", required=True)
    parser.add_argument("--x", default="8%")
    parser.add_argument("--y", default="7%")
    parser.add_argument("--width", default="42%")
    parser.add_argument("--threshold", type=int, default=210)
    args = parser.parse_args()

    base = Image.open(args.base).convert("RGBA")
    composite(base, Path(args.title_f), Path(args.out_f), args.x, args.y, args.width, args.threshold)
    composite(base, Path(args.title_i), Path(args.out_i), args.x, args.y, args.width, args.threshold)
    print(Path(args.out_f).resolve())
    print(Path(args.out_i).resolve())


if __name__ == "__main__":
    main()
