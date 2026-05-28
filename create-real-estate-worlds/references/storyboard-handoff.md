# Storyboard Handoff

Use this reference when the world-building phase is finished and the user wants to move into professional storyboard production.

This skill should not create the final storyboard boards. It should prepare a compact handoff that lets `archviz-storyboard` produce the boards, technical annotations, film sequence, clean keyframe plan, and video prompts without losing the project identity.

## Handoff Principle

The handoff is not a summary for humans only. It is an operational packet for the next skill.

It should preserve:

- world name and project promise;
- selected aspect ratio: `9:16` for Reels/social/mobile or `16:9` for presentation/horizontal;
- project type, location, audience, and platform;
- visual DNA and reference DNA;
- approved images or generated image status;
- material, light, camera, and spatial continuity anchors;
- scene priorities and emotional beats;
- constraints, no-copy rules, and missing assets;
- what must be locked before generating storyboard images.

## Handoff Template

```markdown
## Source Skill
create-real-estate-worlds

## Destination Skill
archviz-storyboard

## Inputs
- World/project name:
- Project type:
- Location/climate:
- Audience:
- Platform/aspect ratio: 9:16 or 16:9
- Duration target:
- Approved images/assets:
- References:

## Decisions Already Made
- Strategic promise:
- Visual DNA:
- Material palette:
- Light logic:
- Camera language:
- Human/lifestyle tone:
- Spatial continuity:
- No-go elements:

## Output Needed
- Storyboard plan:
- Production storyboard board prompts:
- Individual scene boards:
- Architectural detail boards:
- 4 to 6 frame film sequence board:
- Clean keyframe plan:
- Seedance/video prompts:

## Constraints
- Approved architecture must not change:
- Reference/copyright safety:
- Missing rooms/angles/assets:
- People/lifestyle limits:
- Technical detail limits:

## Known Risks
- Unsupported reverse angles:
- Invented architecture or furniture:
- Repeated frames:
- Generic luxury language:
- Overly technical or unreadable boards:
- AI-looking materials or impossible camera moves:

## Validation Checks
- Shot variety:
- Continuity:
- Material realism:
- Reference fidelity:
- Architectural readability:
- Clear next generation/evaluation loop:
```

## Short Handoff Rule

When the user is ready to continue immediately with `archviz-storyboard`, keep the handoff concise and actionable. Do not repeat the full world bible unless needed.

## Approved Image Rule

If approved images exist, list them by exact file name whenever possible. If file names are unavailable, create temporary descriptive labels and say they are temporary.

## Aspect Ratio Rule

Every handoff must specify `9:16` or `16:9`.

- Use `9:16` for Reels, Instagram, TikTok, Stories, Shorts, and mobile social content. This is the user's primary format.
- Use `16:9` for sales decks, websites, YouTube, client presentations, and horizontal cinematic films.

If the aspect ratio is not known, ask before preparing final image prompts, storyboard handoff shots, or video prompts.

## Missing Asset Rule

If a requested storyboard shot needs an unseen facade side, hidden room, reverse angle, close-up detail, or technical area that is not visible in the approved images, mark it as a risk for the storyboard skill instead of inventing it.

## Strategic Image Expansion Handoff

When handing off to `archviz-storyboard`, include both image categories:

1. Core approved/generated images.
2. Strategic supplemental images or suggested missing images.

For each supplemental image, state:

- purpose: hook, transition, detail, material proof, technical explanation, location proof, construction progress, lifestyle proof, or final hero;
- source references;
- whether it is approved, generated, requested, or still needed;
- whether it is client-facing, portfolio-facing, social-facing, or production-facing;
- consistency anchors;
- risk level.

For real client projects, the handoff must identify which images are strict derivatives of client assets and which are conceptual/provisional.

For every video/storyboard handoff, name the opening visual hook. The opening hook should be stronger than a normal beautiful render and should be selected to retain attention in the first seconds.

