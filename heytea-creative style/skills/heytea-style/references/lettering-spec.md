# Lettering specification

## Authoritative mapping

The user-defined variant labels are authoritative:

- F is the **coarse version**, controlled by `assets/font-f-coarse-reference.png`.
- I is the **fine version**, controlled by `assets/font-i-fine-reference.png`.

Do not infer or rename variants from visible stroke width.

## Shared requirements

- Render the exact supplied Chinese characters and punctuation.
- Output only flat black title ink on white or transparent background.
- Use loose vertical columns, staggered baselines, irregular scale, tilt, spacing, internal gaps, and centers of gravity.
- Keep every character readable but visibly untrained.
- Reject brush calligraphy, rounded commercial cute fonts, Song/Kai forms, geometric sans serif, perfect grids, outlines, shadows, gradients, pinyin, English, labels, and extra text.

## F — coarse version

Use `assets/font-f-coarse-reference.png` as the only lettering style reference.

Transfer these qualities:

- broad, dark, crayon-like black marks;
- visible grain, ink bumps, blunt caps, overlaps, and ugly joins;
- non-dominant-hand wobble, compressed radicals, overshoots, and energetic imbalance;
- readable forms that feel forcefully and playfully drawn by a young child.

Do not substitute another coarse, rounded, marker, brush, or commercial cute font.

## I — fine version

Use `assets/font-i-fine-reference.png` as the only lettering style reference.

Transfer these qualities:

- thin-to-medium shaky black lines with blunt monoline ends;
- hesitant pressure, crooked structure, loose spacing, and awkward large internal gaps;
- off-grid placement and slowly copied, earnest young-child rhythm;
- readable forms that remain visibly untrained.

Do not substitute another pencil, Kai, Song, geometric, or commercial handwriting font.

## Layout

For four or more characters, prefer two loose vertical columns when the poster allows it. Explicitly assign characters to columns in the prompt. Do not request a generic 2×2 or rectangular title block.

Verify each title layer before local compositing. If one layer is misspelled, regenerate only that layer.
