# Frame Prompt And Motion Notation

Use this reference when creating GPT Image 2 storyboard boards, clean keyframes, frame-by-frame prompts, fallback prompts when image generation is unavailable, or clearer motion/action instructions for Seedance planning.

## Per-Frame Prompt Pipeline

Before generating a storyboard board, create a prompt for each individual frame. Structure each frame prompt using the `gpt-image-2-prompt-generation` skill style.

For each frame, include:

- subject: what the frame shows;
- scene: property type, room, facade, amenity, or site context;
- composition: close-up, wide, foreground reveal, doorway view, aerial, waterline, material detail;
- camera/lens: realistic camera height, lens feel, gimbal/drone/slider/tripod look;
- architecture and material fidelity: what must remain consistent;
- lighting and mood: time of day, light direction, exposure, color grade;
- motion intention: the video movement this frame is designed to support;
- aspect ratio: 9:16 for Reels/mobile, 16:9 for horizontal presentation;
- avoid: repeated frame, wrong aspect ratio, CGI/plastic look, warped architecture, random text, watermark, logo unless provided.

For standalone keyframes, start each prompt in the required GPT Image 2 prompt-generation style:

```text
Generate an image with the following prompt, dont change it(DO NOT CHANGE THIS PROMPT, IT'S ALREADY AN IMPROVED PROMPT) -
```

For storyboard board assembly prompts, do not repeat that prefix inside every visible frame. Instead, use the per-frame prompts as the source specification for each storyboard panel.

## Fallback Output

If image generation inside Codex is unavailable, unreliable, or not requested, return:

1. `Prompts Individuais dos Quadros`: one structured prompt per shot/keyframe.
2. `Prompt de Montagem do Storyboard`: one board prompt that tells GPT Image 2 to arrange the approved frames.
3. `Notas para Seedance`: camera/action notes for later video prompts.

This lets the user generate each frame separately, then create a storyboard board afterward.

## Motion Strip

Each storyboard panel should have a small caption or motion strip below the image. Keep it outside the photographic frame, not over the architecture.

Shot numbering must never appear inside the video image area. Put `SHOT 01`, `SHOT 02`, timecodes, arrows, camera labels, and action notes only in the caption/motion strip below each panel or in the storyboard margin. Clean keyframes for Seedance must have no numbers, labels, arrows, or text.

Use short fields:

```text
SHOT 03
00:04-00:06
CAMERA: SNAP PUSH-IN
PATH: WALL DETAIL -> FINISHED PANEL
ACTION: DESIGN LINES ASSEMBLE
TRANSITION: MATCH CUT BY VERTICAL LINES
```

Use only the fields that matter. Avoid long paragraphs under frames.

## Visual Motion Cues

When useful, ask for subtle diagram cues in the motion strip or margin:

- small arrow showing camera direction;
- `START` and `END` markers for start/end frame planning;
- `A -> B` path notation for camera travel;
- `FOCUS: foreground -> facade` for rack focus;
- `MATCH CUT: light line` for transition logic;
- `SPEED: fast in, slow settle` for speed ramp behavior.

Do not place large arrows, labels, UI graphics, numbers, timecodes, or technical clutter inside the photoreal frame unless the shot is intentionally a technical overlay style. The architecture image should remain clean.

## Storyboard Grid Layout

For 9:16 Reels storyboards, prefer exactly 6 panels arranged as a 2 rows x 3 columns grid. Each panel must remain a readable true 9:16 rectangle.

Avoid:

- five or six panels squeezed into one horizontal row;
- thin vertical strips;
- panels cropped to fit the page;
- square panels;
- mixed aspect ratios;
- motion notes placed inside the image.

If the story has only 5 shots, either add a useful sixth shot or use a balanced layout with enough panel width. Do not compress the frames just to keep all shots in one row.

## Take Clarity Formula

For every shot, write one concise take sentence:

```text
The camera [movement] from [start composition] to [end composition] while [action happens], preserving [continuity anchor].
```

Examples:

```text
The camera performs a fast foreground reveal from tropical leaves to the premium facade while warm interior lights turn on, preserving the same blue-hour exterior and landscaping.
```

```text
The camera glides low across the stone pathway toward the wood entrance door while garden lights create depth, preserving the same facade materials and doorway position.
```

## Board Assembly Prompt Requirements

A storyboard board prompt should say:

- use exactly 6 frames for 9:16 Reels boards when possible, never more than 6;
- arrange 9:16 Reels panels in a 2 rows x 3 columns grid;
- each panel matches the selected aspect ratio;
- use local timecodes starting at `00:00`;
- each panel is based on its frame prompt;
- add a small motion strip under each panel;
- do not repeat frames or compositions;
- keep all numbering and motion text short and outside the main photographic image;
- no random labels, marketing text, watermark, logo, compressed panels, thin strips, one-row layout, or mixed aspect ratios.
