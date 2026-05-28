# Photorealism And Continuity

Use this reference when the user wants professional archviz videos that feel like normal real-camera footage, with photographic stills, consistent environments, and client-ready realism.

## Target

The viewer should feel that the building, room, resort, lot, or development was filmed in the real world. The output may be generated, but it should not look generated.

Prioritize:

- exact architecture and layout;
- photographic realism;
- stable environment continuity;
- physically plausible camera movement;
- simple Seedance actions with strong visual purpose;
- clean keyframes or original renders as the main image-to-video references.

## Asset Quality Bar

For strong results, ask for or prefer:

- high-resolution renders or photos for each main environment;
- matching aspect ratio when possible: 9:16 for Reels/TikTok/Stories, 16:9 for YouTube/web/presentations;
- facade, entrance, exterior leisure, living, kitchen, suite, bathroom, balcony/view, and key amenities when relevant;
- floor plans, site plans, or masterplans for spatial logic;
- material/detail references for stone, wood, glass, metal, water, lighting, vegetation, and furniture;
- day/night references if the story uses both;
- logo or brand files only when final branding is requested;
- character sheets only when identifiable people must appear.

If assets are limited, keep the movement safer and say what the limitation affects:

- one image of a room: use push-in, pull-back, pan, tilt, detail insert, or foreground reveal;
- one facade image: avoid orbiting to unseen sides;
- no floor plan: avoid long walkthrough continuity between rooms;
- no material closeups: avoid extreme macro material shots;
- low-resolution image: avoid large crops and close details;
- inconsistent renders: choose one canonical reference and flag the conflict.

## From-Scratch Concept Mode

When no project references are provided and the user asks for a storyboard from scratch:

- create a conceptual archviz campaign, not an exact real project;
- define the design language before writing shots: property type, location mood, facade language, material palette, lighting, landscape, interior style, target buyer, and story promise;
- generate GPT Image 2 prompts for all required clean keyframes or storyboard frames;
- keep recurring design elements consistent across all images;
- state that exact fidelity requires real project images, renders, photos, or plans later.

## Aspect Ratio

Use only 9:16 or 16:9 unless the user explicitly requests another format.

- Use 9:16 vertical for Reels, TikTok, Stories, Shorts, and mobile-first ads.
- Use 16:9 horizontal for sales decks, websites, YouTube, and client presentations.

Every storyboard panel, clean keyframe, and Seedance clip should match the selected final video format. A Reels storyboard should contain vertical 9:16 panels, not square or horizontal panels. A 16:9 storyboard should contain horizontal 16:9 panels.

## Environment Continuity Map

Before writing the storyboard, define:

- canonical file for each environment;
- fixed time of day and light direction;
- material palette and finishes that must stay identical;
- furniture and decor anchors that must not move;
- landscape, pool, road, lot, view, or neighboring context that must remain stable;
- camera path logic from one shot to the next;
- continuity anchors such as water, facade rhythm, wood ceiling, stone wall, floor line, corridor direction, sunlight, or character action.

Use the continuity map to avoid random room montage. Every shot should feel like it belongs to the same property and the same film.

## No Repeated Images

Never repeat the same frame in a storyboard. The same environment can appear again only if the new frame is visibly different:

- wide view vs close-up;
- front perspective vs provided side perspective;
- material detail vs full room;
- daylight vs night only when approved;
- empty architecture vs requested lifestyle action;
- first frame vs generated clean keyframe with a different composition.

If the source file is reused, label the variation clearly so the model understands that the output frame must be different.

Exception: in continuous start/end frame workflows, the end frame of one clip may be reused as the start frame of the next clip. This is a technical handoff for continuity, not a repeated storytelling frame.

## Local Storyboard Timecodes

Every generated storyboard board starts its visible timecodes at `00:00`, even when it is a continuation board.

Use local board timing inside storyboard prompts:

- Board 1 visible labels: `00:00-00:02`, `00:02-00:04`, etc.
- Board 2 visible labels: `00:00-00:02`, `00:02-00:04`, etc.

Do not put global continuation timecodes like `00:14-00:16` inside Board 2. If global timing is needed, keep it as a separate planning note outside the image prompt.

## Photographic Realism Language

Use phrases like:

- photorealistic architectural photography;
- real camera footage look;
- natural exposure and balanced dynamic range;
- physically plausible sunlight and shadows;
- realistic reflections on glass, water, marble, and metal;
- true material roughness and texture;
- subtle real-world imperfections;
- true-to-scale furniture and architecture;
- natural depth of field, not exaggerated bokeh;
- realistic lens perspective, no warped wide-angle distortion;
- smooth gimbal, slider, tripod, or drone camera movement;
- natural motion blur only during movement;
- calm premium color grade.

Avoid phrases that make the output feel synthetic:

- hyperreal, surreal, fantasy, dreamlike, impossible, glossy CGI, ultra-polished 3D render, game engine look, concept art, illustration, cartoon, plastic, miniature, toy, extreme HDR.

## GPT Image 2 Keyframe Rules

For each important Seedance clip, prefer one clean photoreal keyframe.

A clean keyframe should:

- be full-frame in the final aspect ratio;
- look like a finished architectural photograph;
- preserve exact architecture, materials, furniture, landscape, and scale from the source file;
- include only the visual scene, not the storyboard interface;
- have no text, labels, arrows, grids, timeline, watermarks, UI frames, or collage layout;
- show the starting composition or the most important hero moment of the clip;
- include people only when requested and controlled by a character sheet.

For close-ups and multishots, make a dedicated clean keyframe when the detail is important, small, reflective, branded, textural, or likely to be misread. Do not expect Seedance to invent a reliable close-up from text alone.

Prompt pattern:

```text
Create one clean photorealistic architectural keyframe for Seedance image-to-video.
Use [exact-file-name] as the exact source reference, not as loose inspiration.
Preserve the same architecture, geometry, materials, furniture, landscape, lighting logic, and scale.
Make it look like a real architectural photograph captured with a real camera.
No text, no arrows, no labels, no storyboard panels, no collage, no watermark.
```

## Seedance Real-Camera Rules

For each clip:

- use one primary reference image or clean keyframe;
- use a dedicated crop/keyframe for close-ups when the target detail is small or important;
- define one camera platform: tripod, slider, gimbal, drone, or handheld-inspired;
- use one main movement: slow push-in, pull-back, lateral dolly, tilt, crane, drone approach, path trace, parallax reveal, or static hero;
- add one secondary effect only if it supports the reveal;
- for social pacing, keep normal clips at 1.5-3 seconds and reserve 4-5 seconds for complex transformations or actions;
- start and stop movement naturally;
- keep architecture locked and stable;
- keep people and objects physically plausible;
- avoid asking Seedance to build new rooms, unseen views, new facades, new furniture, or new landscape;
- split complex transformations into separate clips.

## Continuous Start/End Frame Workflow

Use this only when the user requests continuous video, start/end frame, or end-frame-to-start-frame continuity.

For chained Seedance clips:

- define a start keyframe and end keyframe for each clip;
- reuse the exact end keyframe of clip N as the start keyframe of clip N+1;
- keep camera height, lens feel, light direction, architecture, furniture, materials, people, and object placement consistent across the handoff;
- use short connected moves, usually 2-5 seconds per clip for social pacing;
- avoid jumping to unseen architecture unless a transition shot or match cut is planned;
- label shared frames as `handoff frame` so they are not confused with accidental duplicates.

Prompt pattern:

```text
Generate a photorealistic architectural video using start and end frames.
Start frame: [clip-01-start.png].
End frame: [clip-01-end.png].
Camera moves smoothly from the start frame composition to the end frame composition.
Preserve the exact architecture, lighting, materials, furniture, scale, and camera direction.
The end frame must be suitable to become the start frame of the next clip.
```

Seedance prompt pattern:

```text
Generate a photorealistic architectural video that looks like normal real-camera footage.
Use [clean-keyframe.png] as the main visual reference for this clip.
Preserve the exact architecture, furniture, materials, view, lighting direction, and scale.
Camera: [platform], [movement], [speed], [start composition to end composition].
Motion: [one clear action].
Do not film the storyboard page. Do not create text, panels, collage, labels, new rooms, changed materials, warped windows, extra floors, fake reflections, CGI/plastic surfaces, or inconsistent lighting.
```

## Storytelling For Realism

Photorealism alone is not enough. The video should still create desire and retention.

Use a story shape such as:

- arrival: street/site/drone to architecture hero;
- reveal: technical plan, material, or close detail to full space;
- lifestyle: person uses the space naturally, then architecture becomes the hero;
- transformation: empty/under-construction to finished project;
- value: problem, solution, proof, final desirable scene;
- walkthrough: entrance, social area, detail, leisure, private space, final view.

The first 3 seconds should have the strongest visual hook, but it must remain believable:

- drone descent into a facade;
- snap from blueprint/lot marking to real render;
- tactile material closeup revealing the room;
- car/footstep/doorway arrival into the project;
- light turning on across a facade;
- presenter gesture revealing architecture;
- water/pool reflection leading into the leisure area.

## Red Flags And Fixes

If it looks like a CGI render:

- add real architectural photography language;
- reduce saturation and glossy surfaces;
- add natural exposure, realistic reflections, and material roughness;
- create a cleaner photoreal keyframe before Seedance.

If the environment changes between shots:

- reduce camera movement;
- lock the canonical file for each shot;
- use the same time of day and material palette;
- split unrelated rooms into separate clips;
- add continuity anchors.

If Seedance invents architecture:

- use a safer movement;
- remove unseen reverse angles;
- provide another reference angle;
- use a clean keyframe as the main visual reference.

If a character is inconsistent:

- use a character sheet;
- keep one simple action per clip;
- avoid tiny faces, profile-to-front transformations, and many wardrobe changes;
- keep the character secondary to the architecture unless presenter-led.

## Professional Output Gate

Before final approval, check:

- would a normal viewer believe this could be real footage?
- does every shot belong to the same property and same film?
- are the images photographic, not illustrated or plastic?
- did the first 3 seconds create a strong hook?
- does the video tell a story instead of showing random spaces?
- does each Seedance clip have one clear visual reference, one camera move, and one action?
- are the missing assets or fidelity risks clearly stated?
