# Quality Guardrails

## Approval Checklist

Before finalizing a world or prompt pack, check:

**Architecture**
- Does the style remain consistent across all spaces?
- Are materials plausible and repeated intentionally?
- Does exterior connect logically to lobby, amenities, interiors, and views?
- Are proportions, scale, ceiling heights, furniture, doors, and railings believable?

**Real Estate Strategy**
- Does the world speak to the intended buyer?
- Is the emotional promise clear?
- Does each scene have a commercial function?
- Is the property the hero, even when people appear?

**Visual Continuity**
- Are the same anchors repeated?
- Does the climate match the location?
- Does the light logic make sense?
- Do view directions and city/nature context remain coherent?

**Human Realism**
- Do people behave naturally?
- Does wardrobe match climate, market, and time of day?
- Are gestures subtle and property-related?
- Are people avoiding catalog poses and exaggerated smiles?

**Prompt Quality**
- Is each prompt specific enough to generate?
- Does each prompt include camera, light, material, action, and guardrails?
- Are negative prompts targeted rather than generic?
- Can another session reuse the prompt without needing the whole conversation?

## Common Failure Modes And Fixes

**Generic luxury**
Fix by naming exact materials, service rituals, camera restraint, and audience-specific emotion.

**AI showroom emptiness**
Fix by adding human trace: linen texture, open book, glass condensation, towel fold, shoes near entrance, soft plant movement, breakfast setup.

**Stock-photo lifestyle**
Fix by specifying observational camera, candid posture, no smiling at camera, action tied to property use.

**Over-rendered CGI**
Fix by adding physically plausible material behavior, natural imperfections, subdued contrast, realistic glass, grounded shadows, and restraint.

**Inconsistent architecture**
Fix by defining continuity anchors and repeating them in every prompt.

**Wrong regional feeling**
Fix by naming climate, vegetation, wardrobe, urban context, sun behavior, and cultural rituals.

**Prompt drift**
Fix by adding the Master World Prompt before each scene prompt or embedding 3 to 5 continuity anchors in every prompt.

**Too much decoration**
Fix by giving each object a reason: scale, routine, material proof, hospitality, family, wellness, or sales narrative.

## Brazilian Premium Realism

When appropriate, make Brazilian real estate feel believable:

- shaded balconies and terraces;
- tropical landscaping that fits climate and maintenance;
- natural stone, warm wood, textured walls, good metalwork;
- water as reflection and cooling element, not only spectacle;
- informal but refined social life around dining, pool, balcony, garden, and view;
- family routines that feel lived-in, not theatrical;
- city context that respects the actual market when known;
- daylight that understands heat, shade, glare, and ventilation.

Avoid:

- imported mansion cliches with no local logic;
- fake tropical plants in wrong climates;
- overly cold minimalism for family/lifestyle projects;
- luxury that feels like a hotel lobby when the project is residential;
- people dressed as if in a fashion ad instead of using the property.

## Real Project Reference Fidelity

If the user provides project images, renders, plans, moodboards, or brand guidelines:

- preserve architectural massing, facade rhythm, material palette, windows, balconies, landscape, and key spaces;
- do not invent extra towers, amenities, ocean views, skyline, pools, or furniture unless requested;
- separate "known from reference" from "creative assumption";
- write prompts that explicitly say "preserve the reference architecture";
- use generated additions only to clarify light, atmosphere, human use, or cinematic framing.

## Output-Specific Checks

**Still Images**
Check composition, perspective, material realism, clutter, human scale, and whether the image sells one clear idea.

**Vertical Videos**
Check start/end frame, movement, subject continuity, readable architecture, and whether the scene works without captions.

**Sales Film**
Check sequence: context, arrival, reveal, lifestyle, detail, emotional payoff, brand close.

**Storyboard Handoff**
Check that the handoff names the destination skill, approved anchors, shot variety, continuity rules, camera grammar, emotional progression, and what the storyboard stage must not invent.

**Interactive / World Model**
Check spatial route, persistent object placement, stable geometry, action consequences, and navigation logic.

## Final Response Rule

End with a practical next-generation plan:

- first outputs to generate;
- what each one tests;
- what to add back into the world database after seeing results.
