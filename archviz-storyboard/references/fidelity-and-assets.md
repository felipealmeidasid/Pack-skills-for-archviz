# Fidelity And Assets

Use this reference when the user provides renders, photos, floor plans, site plans, approved images, real project assets, or a `create-real-estate-worlds` handoff.

## Usage Modes

**Finished project images**

- Treat uploaded renders, photos, plans, and project images as strict visual references.
- Preserve exact architecture, massing, materials, layout, furniture, landscape, lighting logic, and scale.
- Build the storyboard from visible image information, safe crops, safe detail inserts, and clean keyframes.
- Do not invent missing rooms, reverse angles, facade sides, furniture, landscaping, views, amenities, or neighboring context.

**Conceptual storyboard from scratch**

- Treat the result as a concept campaign, not strict project documentation.
- Define a consistent design language, material palette, time of day, location, layout logic, and recurring visual anchors.
- State that exact fidelity requires real project images, renders, photos, or plans.

**World handoff**

- Treat the `create-real-estate-worlds` handoff as the creative source of truth for world name, visual DNA, audience, material palette, camera language, scene priorities, and continuity anchors.
- Treat actual renders, photos, plans, and approved images as the visual source of truth for geometry, layout, materials, furniture, landscape, and scale.
- If handoff and real project assets conflict, preserve the real project assets for architectural fidelity and use the handoff only for tone and sequencing.

## Asset Intake

- Use exact file names whenever the interface exposes them. If names are unavailable, create temporary descriptive labels such as `uploaded-facade-render`, `uploaded-site-plan`, or `uploaded-living-room`.
- Classify assets as exterior, facade, aerial, entrance, lobby, amenity, rooftop, pool, gym, social area, apartment interior, suite, kitchen, balcony, view, floor plan, site plan, landscaping, construction detail, or brand/logo.
- Treat floor plans, site plans, and PDFs as spatial logic references by default. Use them for orientation, sequence planning, lot/road/amenity logic, and camera feasibility.
- If an asset is low-resolution, ambiguous, cropped, or inconsistent with another asset, call out the fidelity risk and choose the safest visible shot.

## Architectural Fidelity

Use strict fidelity for real client projects, real estate campaigns, archviz renders, site photos, interior renders, development presentations, floor plans, site plans, loteamentos, and sales assets.

Lock these elements:

- building massing, floor count, roofline, facade rhythm, balcony geometry, openings, window mullions, glass railings, brises, columns, beams, slabs, structural proportions;
- material placement and finish: concrete, stone, wood, metal, glass, marble, ceramic, vegetation, water, lighting, ceiling, flooring, wall panels;
- spatial logic: entrance position, street relation, site orientation, landscape layout, pool position, terrace edges, view, neighboring context;
- interior layout: sofa, table, bed, kitchen island, cabinetry, fixtures, curtains, wall panels, decor, circulation, glass walls, balcony connection;
- plan logic: lots, roads, access, blocks, green areas, amenities, setbacks, water bodies, phase boundaries, orientation markers.

Do not create unsupported reverse angles or unseen sides. If a desired shot needs missing visual information, choose a safer shot or say what extra image is needed.

## Close-Up And Multishot Rules

- If the close-up region is large, visible, sharp, and architecturally simple, use a prompt crop, push-in, or detail insert.
- If the region is small, low-resolution, hidden, reflective, branded, textural, or structurally important, ask for a crop, extra render, close-up reference, or clean GPT Image keyframe.
- If a multishot needs a new angle, unseen side, hidden corner, or movement into a room not shown, ask for additional images or choose a safer visible-angle shot.
- If the same environment appears in several frames, each frame must use a different composition, perspective, crop, focal detail, or action.

## Clean Keyframe Workflow

For high-end video realism, the storyboard board controls idea and timeline, but the main Seedance visual reference should be a clean architectural still whenever possible.

Use this hierarchy:

1. Original client render/photo if realistic and matching the shot.
2. Clean GPT Image photoreal keyframe based on the original render/photo.
3. Storyboard board only as timeline/editing reference, not as the main visual subject.

Clean keyframes must be full-frame images in the final aspect ratio, without labels, arrows, grids, captions, timecodes, watermarks, UI panels, or collage layout.

If a storyboard board contains text or multiple panels, tell Seedance not to film the board, keep labels, or turn panels into a collage. The video must animate the real architectural scene inside the approved frame/keyframe.
