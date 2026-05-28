# Real Estate World Framework

## What A World Is

A real estate world is a persistent creative database for a property universe. It is not just a style, not just a prompt, and not just a moodboard.

It contains:

- strategic promise: why the property matters to the audience;
- aspect ratio strategy: `9:16` for Reels/social/mobile or `16:9` for presentation/horizontal;
- visual DNA: architecture, light, materials, landscape, palette, camera;
- spatial continuity: how places connect and repeat across outputs;
- human behavior: believable residents, visitors, staff, investors, and rituals;
- scene library: repeatable moments for stills, videos, storyboards, and social;
- prompt system: reusable prompts and guardrails for multiple AI models;
- production handoff: the decisions another skill needs to create storyboards or video prompts without losing the world identity.

## Real Estate World Types

Use one or combine several:

**Luxo Tropical Brasileiro**
High-end Brazilian residential world with tropical landscape, natural stone, warm wood, shaded terraces, water reflections, soft ventilation, and understated luxury.

**Vertical Urbano Premium**
Residential tower world focused on skyline, arrival experience, lobby, rooftop, wellness, city views, night lighting, and cosmopolitan lifestyle.

**Casa Contemporanea Cinematografica**
Single-family home world with clean geometry, tactile materials, garden transitions, intimate routines, controlled sunlight, and warm domestic realism.

**Resort Residencial**
Property world where home and hospitality merge: pool, spa, restaurant, beach/mountain access, service rituals, leisure, privacy, and weekend rhythm.

**Wellness And Slow Living**
World centered on calm, body, silence, nature, water, morning light, spa, yoga, recovery, organic materials, and low-noise luxury.

**Familia Premium Realista**
Family-oriented world with school-day routines, children using amenities naturally, meals, pets if appropriate, safety, storage, comfort, and everyday elegance.

**Investimento E Status Discreto**
World for investors and high-income buyers: arrival, concierge, meeting room, view, material close-ups, city access, exclusivity, and long-term value.

**Hospitality / Hotel / Branded Residence**
World driven by service, arrival sequence, suite, gastronomy, pool, staff gestures, nighttime ambience, and brand ritual.

## World Database Schema

Use this schema when creating the database:

**World ID**
Short codename for reuse.

**World Name**
Memorable campaign/world name.

**Logline**
One sentence that captures the promise.

**Project Anchor**
The real project, typology, location, architectural references, and constraints.

**Audience**
Buyer/user profile, income level, lifestyle, anxieties, aspirations, and objections.

**Emotional Target**
The feeling the world should create: calm prestige, urban command, protected family life, resort escape, future-facing design, etc.

**Aspect Ratio**
The selected output format. Use `9:16` for Reels, Instagram, TikTok, Stories, Shorts, and mobile social content. Use `16:9` for sales decks, websites, YouTube, client presentations, and horizontal cinematic films.

**Spatial Network**
Exterior, arrival, lobby, circulation, apartment/house, amenities, landscape, view, neighborhood/city/nature.

**Visual DNA**
Architecture, materials, palette, landscape, light, climate, camera language, movement, texture, depth, atmosphere.

**Continuity Anchors**
Elements that must repeat: facade lines, signature stone, wood tone, railing type, pool color, skyline, garden species, furniture language, wardrobe palette, time of day.

**Human System**
Personas, gestures, wardrobe, movement, social behavior, family dynamics, staff behavior, visitor behavior.

**Scene Library**
Repeatable scenes with purpose, not random beauty.

**Negative Space**
What must never appear: fake luxury, fantasy styling, wrong climate, impossible views, generic furniture, plastic render look, irrelevant people, visual clutter.

**Output Map**
How the world supports hero images, social videos, sales film, carousels, pitch decks, interactive scenes, and future world-model prompts.

**Storyboard Handoff Map**
How the world should be handed to storyboard production: approved images, scene priorities, aspect ratio, platform, duration, camera language, technical/detail opportunities, and non-negotiable continuity anchors.

## Visual DNA Fields

Define each field concretely:

- architecture style: contemporary, tropical modern, minimalist, brutalist-soft, resort, urban premium, hospitality;
- massing/proportions: vertical, horizontal, low-slung, courtyard, tower, pavilion, terrace;
- material hierarchy: primary, secondary, accent, tactile detail;
- palette: neutrals, warm/cool bias, metal tones, vegetation, water, sky;
- light logic: morning, golden hour, blue hour, overcast, night, interior warm light, realistic sun direction;
- landscape: tropical, coastal, urban, dry garden, mountain, courtyard, rooftop, native species;
- camera language: lenses, movement, height, distance, framing, depth of field;
- human tone: candid, observational, refined, everyday, family, investor, hospitality, wellness;
- realism rules: scale, reflections, shadows, material wear, human posture, furniture use.

## Spatial Continuity

Force outputs to feel like the same property.

Use:

- route logic: street -> arrival -> lobby -> elevator/circulation -> unit -> balcony/view -> amenities;
- repeated anchors: same stone, same wood, same skyline, same garden, same pool edge, same lobby desk;
- time continuity: morning lifestyle, afternoon amenity, blue-hour facade, nighttime city view;
- camera continuity: same lens family and composition habits;
- environmental continuity: same climate, vegetation, season, water behavior, cloud type.

Avoid:

- each image looking like a different project;
- inconsistent city/nature views;
- conflicting material palettes;
- people dressed for the wrong climate;
- impossible sun direction or scale;
- swapping architectural style between prompts.

## Persona Design

Real estate personas are not fantasy characters. They are believable human anchors that make the property feel lived-in.

Persona fields:

- name or role label;
- age range;
- socioeconomic and lifestyle context;
- wardrobe palette;
- posture and movement;
- relationship to the property;
- where they appear;
- what they should never do.

Useful persona types:

- resident couple;
- family with one or two children;
- architect/designer host;
- investor visiting the property;
- concierge or hospitality staff;
- wellness user;
- chef/host at dining area;
- friend group in social amenity;
- solo resident using balcony, office, or spa.

Rules:

- Keep people secondary to architecture unless the scene is explicitly lifestyle.
- Avoid catalog posing.
- Use natural gestures: opening curtains, setting a glass down, walking barefoot near pool, reading by the balcony, greeting concierge, entering elevator, touching a material sample.
- Match wardrobe to market, climate, time of day, and property value.

## Scene Design

Each scene needs a job. Use these emotional functions:

- arrival prestige;
- daily comfort;
- spatial reveal;
- material trust;
- lifestyle proof;
- family safety;
- hospitality service;
- investment confidence;
- calm retreat;
- city command;
- nature connection;
- nighttime desirability.

Scene fields:

- scene title;
- location;
- camera/lens/movement;
- subject/action;
- light/weather;
- recurring anchors;
- emotional function;
- output formats;
- prompt seed.

## World Expansion Levels

Use levels depending on user need:

**Level 1: Prompt Seed**
Master prompt plus 5 scenes.

**Level 2: Campaign World**
World bible, personas, 15 scenes, prompt pack, guardrails.

**Level 3: Production Bible**
Everything in Level 2 plus shot sequencing, media plan, variations by day/night, vertical/horizontal versions, approval checklist.

**Level 4: Future World Model Database**
Everything in Level 3 plus spatial map, interaction prompts, object affordances, route logic, state changes, and continuity IDs.

**Level 5: Production Handoff**
Everything in Level 3 plus a clean handoff for `archviz-storyboard`: approved-image index, room/space priorities, architectural detail opportunities, mood/material anchors, film sequence intent, video motion notes, and revision risks for the next generation round.
