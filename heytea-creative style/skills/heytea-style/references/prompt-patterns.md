# Prompt patterns

## Poster-base prompt

```text
Use case: ads-marketing
Asset type: static 9:16 food poster base
Input image: staged source food photo; authoritative product reference

Preserve the exact recognizable [food], including [container/rim], [camera angle/crop], [layers/toppings], [colors/textures], and [distinctive irregularities]. Do not replace the product, redesign the container, add ingredients, or rearrange toppings.

Remove only unrelated surroundings. Place the photorealistic subject on a pure white #FFFFFF field with generous negative space and a soft contact shadow. The background must not be cream, beige, warm gray, textured, patterned, or gradient.

Across [chosen component], draw one high-coverage childlike black-line narrative that transforms its real geometry into [story]. Keep the food visible beneath it. Add [functional micro-worker] and only a few low-coverage [steam/speed/spark/wobble] lines.

Reserve [title area] but render no text. No logo, QR code, watermark, phone UI, random text, unsupported claim, busy background, extra ingredient, polished mascot, or animation.
```

## Title F prompt — coarse version

```text
Use case: ads-marketing
Asset type: title-only lettering layer
Input image: assets/font-f-coarse-reference.png as the only lettering style reference
Exact text, verbatim: "[caption]"
Layout: [explicit character-to-column layout]

Transfer F's non-dominant-hand crayon structure: broad dark textured black marks, visible grain, blunt caps, overlaps, ugly joins, compressed radicals, overshoots, uneven sizes, varied tilt, and playful imbalance. Readable but visibly drawn by a young child.

Output only flat black Chinese title ink on white or transparent background. No food, people, doodles, icons, labels, pinyin, English, watermark, extra text, brush calligraphy, commercial font, outline, shadow, gradient, or color.
```

## Title I prompt — fine version

```text
Use case: ads-marketing
Asset type: title-only lettering layer
Input image: assets/font-i-fine-reference.png as the only lettering style reference
Exact text, verbatim: "[caption]"
Layout: [explicit character-to-column layout]

Transfer I's earnest-child hard-pencil construction: thin-to-medium shaky black lines, hesitant pressure, blunt monoline ends, crooked structure, loose spacing, awkward large internal gaps, uneven sizes, varied tilt, and off-grid placement. Readable but visibly copied slowly by a young child.

Output only flat black Chinese title ink on white or transparent background. No food, people, doodles, icons, labels, pinyin, English, watermark, extra text, brush calligraphy, commercial font, outline, shadow, gradient, or color.
```

## Targeted corrections

Food fidelity:

```text
Regenerate only the poster base. Preserve the source silhouette, perspective, container rim, ingredient count, topping placement, sauce distribution, irregularities, and colors. Change only the background and black-line overlay.
```

Doodle strength:

```text
Keep the photo unchanged. Deepen only the narrative across [component] so its existing geometry clearly becomes [story]. Keep all other marks sparse.
```

Title accuracy:

```text
Regenerate only title [F/I]. Preserve its assigned reference style and exact layout. Correct the text to "[caption]". Output no other content.
```
