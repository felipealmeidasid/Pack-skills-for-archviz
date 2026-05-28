# Character Reference Rules

Use this reference when the user wants to add people, presenters, clients, residents, workers, guests, family scenes, lifestyle actions, or branded recurring characters to archviz videos.

## Core Rule

Only add characters when the user explicitly requests them or provides character references. For recurring or identifiable characters, require a character sheet or equivalent reference image that shows the same person from multiple angles and includes enough visual detail to preserve identity.

## Character Sheet Intake

For each character, capture:

- exact file name of the character sheet;
- character label, such as `Presenter`, `Resident Woman`, `Construction Worker`, `Buyer`, or the user's chosen name;
- age range, body type, skin tone, hair, facial hair, clothing, accessories, and distinctive features visible in the sheet;
- allowed actions and emotional tone;
- scene role: presenter, scale reference, resident lifestyle, worker, host, guest, buyer, family member, or background extra;
- whether the character must remain consistent across multiple shots.

If a character sheet is missing, do not invent a recurring identifiable person. Use either no people or generic, secondary, non-identifiable silhouettes only if the user approves.

## Prompting Characters

When writing GPT Image 2 or Seedance prompts, reference the character sheet by exact file name and state that it controls identity, face, body, hair, clothing, and proportions.

Use direct action language:

```text
REFERENCES:
- presenter-character-sheet.png: exact identity reference for the male presenter, use the same face, beard, hair, body proportions, black shirt, beige pants, and calm confident expression.

ACTION:
The presenter stands near the entrance, gestures toward the facade, then steps aside without blocking the architecture.
```

For Seedance, describe motion as simple and physically plausible:

- walking slowly through the entrance;
- turning toward the facade;
- pointing to a material detail;
- opening a door;
- touching stone, wood, fabric, countertop, faucet, curtain, or railing;
- sitting calmly;
- drinking coffee;
- preparing food;
- reviewing plans;
- presenting a scale model;
- talking naturally to camera;
- interacting lightly with another character.

## Archviz Priority

Characters must support the architectural story. They should not hide important facade geometry, windows, doors, materials, pool edges, furniture, room layout, technical overlays, logos, or text.

Use people for:

- scale;
- lifestyle atmosphere;
- presenter-led explanation;
- construction process;
- hospitality/resort experience;
- buyer imagination;
- family use;
- hand/detail interactions with materials.

Avoid:

- crowded scenes unless requested;
- characters centered over key architecture;
- exaggerated expressions or theatrical acting;
- random wardrobe changes across shots;
- face changes between clips;
- hand distortions in closeups;
- people appearing when the user asked for pure architecture.

## Character Shot Safety

Safer:

- medium presenter shot;
- walking slowly through a visible path;
- touching a visible material;
- sitting at a table or counter;
- reviewing plans or model;
- lifestyle in a clearly shown room;
- hands interacting with a visible object.

Riskier:

- full-body action with complex movement;
- multiple people interacting;
- closeups of hands doing detailed tasks;
- rapid dancing, running, or sports;
- characters crossing glass reflections;
- character continuity across many separate clips without a strong sheet.

## Output Requirements

When characters are used, include a `Character Map` before the shot plan:

```text
Character Map:
- presenter-character-sheet.png -> Presenter: exact recurring identity, appears in Shots 02 and 06, calm confident host.
- resident-woman-sheet.png -> Resident Woman: exact identity, appears in Shot 04, opens curtain and looks toward the view.
```

Add negative constraints:

```text
Do not change the character's face, hairstyle, body proportions, clothing, skin tone, or accessories. Do not add extra people. Do not let the character block important architecture.
```
