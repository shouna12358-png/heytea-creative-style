---
name: heytea-style
description: Create static 9:16 food promotional posters from uploaded photos using a pure white #FFFFFF field, a photorealistic reference-preserving food subject, one high-coverage childlike black-line narrative across the most expressive food surface, sparse motion doodles elsewhere, and optional exact Chinese copy in exactly two lettering families: F as the coarse non-dominant-hand crayon version and I as the fine earnest-child hard-pencil version. Use for 喜茶感、白底童趣手绘风、实物加小人涂鸦、食品宣传图、灵感小卡, caption-controlled posters, faster repeat generation, stable Chinese titles, or F/I font variants. Treat `/` as no caption. Do not use for GIF, LIVE photo, video, or animation unless explicitly requested.
---

# Food doodle poster

Create an unofficial, static food poster while treating the uploaded photograph as visual truth. Reuse the visual grammar only. Never add an official logo, trademark, endorsement, price, origin, nutrition claim, or unverified product claim.

## Read first

- Read [references/style-spec.md](references/style-spec.md) before designing the poster.
- Read [references/lettering-spec.md](references/lettering-spec.md) for any captioned poster.
- Read [references/prompt-patterns.md](references/prompt-patterns.md) before image generation.

## Fast workflow

### 1. Stage and inspect once

Immediately stage chat-app, cache, or temporary images with `scripts/stage_input.py`. Use only the staged path afterward. Reuse the returned hash and dimensions; do not reopen the unstable source.

Inspect the staged image once and write a compact subject lock:

- food category and container;
- camera angle, crop, silhouette, orientation, and proportions;
- layers, toppings, garnish, sauce, moisture, gloss, and texture;
- distinctive irregularities that identify the exact item;
- uncertain details that must not be invented.

Ignore phone UI, black bars, unrelated tableware, hands, labels, QR codes, watermarks, and background clutter unless the user asks to retain them.

### 2. Resolve exact copy

Use the user's caption verbatim, including punctuation. If no decision exists, ask once:

`请输入海报配文（输入 / 表示不需要配文）：`

Interpret `/` as no caption. Never invent copy after `/`.

### 3. Choose one food-shaped story

Select the most visually forceful food component. Draw one high-coverage black-line narrative across that photographed surface, using its real edges and layers as part of the story. Examples: toast triangles become cats; folded cold-noodle sheets become a train; broccoli becomes a forest.

Keep the real food visible beneath the drawing. Add at most one or two functional micro-workers and only sparse steam, speed, sparkle, wobble, splash, or impact lines elsewhere.

### 4. Launch independent generation branches

After the subject lock, caption, and layout are fixed, start independent generation calls concurrently when the runtime supports it:

1. no-text poster base from the staged food image;
2. title F using [assets/font-f-coarse-reference.png](assets/font-f-coarse-reference.png);
3. title I using [assets/font-i-fine-reference.png](assets/font-i-fine-reference.png).

Use settled/independent results rather than fail-fast aggregation. Preserve every successful branch and retry only the failed branch. Do not regenerate a valid poster base because one title failed.

For `/`, run only branch 1 and deliver one no-text poster.

### 5. Apply the selected lettering mapping

Treat the following names as user-defined labels, not measurements:

- **Coarse version = F**: use only the F reference and its blunt, textured non-dominant-hand crayon structure.
- **Fine version = I**: use only the I reference and its thin, hesitant earnest-child hard-pencil structure.

Do not swap them based on visible stroke thickness. Generate both title layers from the exact caption. They are separate style families and need not share the same glyph skeleton.

### 6. Composite both outputs once

Verify the exact characters before compositing. Then run `scripts/render_variants.py` once to produce the F/coarse and I/fine posters. This local step must not invoke image generation.

### 7. Verify and deliver

Reject or correct an output if:

- the food, container, angle, layers, or topping arrangement changed materially;
- the main doodle is pasted on, unrelated, or fails to use the food geometry;
- doodles hide the food or turn it into a full illustration;
- supporting motion marks are dense or random;
- the caption is wrong or contains extra text;
- F and I were swapped or any unapproved lettering family was used;
- the background is not pure white `#FFFFFF`, is busy, or has cramped whitespace;
- a logo, QR code, watermark, unsupported claim, or invented ingredient appears.

Deliver short labels and direct file links. Report meaningful progress at least once per minute during long generation.

## Efficiency rules

- Stage temporary input before the first expensive call.
- Inspect once; reuse one subject lock and one reserved-title layout.
- Run the poster base and title branches concurrently only after all inputs are stable.
- Use independent settled results; never let one branch discard another.
- Generate one strong base, not one base per font.
- Composite locally in a single process.
- Retry only the failed stage with one targeted correction.
- Never promise an exact duration; distinguish queue time, failed input, active generation, and local processing.
