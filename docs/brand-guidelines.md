# Brand Guidelines

This document defines the naming system, visual identity, and usage rules for
ContinuumXR. It is a living document and will be updated as the visual identity
is finalized.

---

## Naming System

ContinuumXR uses a structured naming system. Each form has a specific, non-interchangeable role.

| Form | Value | Usage |
|---|---|---|
| Legal entity | `ContinuumXR LLC` | Corporate / legal filings |
| Trademark | `CONTINUUMXR` | USPTO standard character mark, Class 009 |
| Formal name / DBA | `ContinuumXR` | All public-facing communications, documentation, press |
| Wordmark | `continuum` | Logotype — visual design contexts only |
| Logomark | CXR infinity mark | Visual mark — in development |
| Shorthand | `CXR` / `cxr` | Code, repositories, internal references, informal use |

### Rationale

The naming system follows the precedent set by LineageOS: a single compound
proper noun as the formal name (`ContinuumXR`), a clean standalone wordmark
(`continuum`), and a derived shorthand (`CXR`). "OS" is intentionally omitted
from the formal name, as it is considered a generic descriptor by the USPTO and
does not add distinctiveness.

### Legal / Entity Name

The following naming decisions have been established:

- **Legal entity:** `ContinuumXR LLC`
- **USPTO trademark:** `CONTINUUMXR` (standard character mark, Class 009)
- **Doing business as / brand:** `ContinuumXR`
- **Formal name:** `ContinuumXR`

"OS" is intentionally omitted from the formal name — it is considered a generic descriptor by the USPTO and does not add distinctiveness.

---

## Logo System

ContinuumXR follows the same structural pattern as LineageOS:

| Brand | Written name | Logomark | Wordmark |
|---|---|---|---|
| LineageOS | `LineageOS` | `∞oo∞` symbol | `LINEAGE` |
| ContinuumXR | `ContinuumXR` | CXR infinity mark | `continuum` |

The `XR` lives in the **logomark**, not the wordmark. The wordmark is always
just `continuum`. When the logomark and wordmark appear together as a lockup,
the full brand identity is expressed — the `XR` is carried by the mark, not
the text.

ContinuumXR uses a two-part logo system: a **wordmark** and a **logomark**.
These can be used together as a standard lockup or independently depending
on context.

### Wordmark

The wordmark is set in lowercase: **`continuum`**

- Always lowercase
- Never includes "XR" — the XR lives in the logomark
- Do not use `ContinuumXR`, `continuumXR`, or any other variant as the wordmark
- Inspired by the approachable, confident lowercase style of consumer XR brands

### Logomark

The logomark is a **CXR integrated mark** designed to resemble an infinity
symbol (∞), with the letters C, X, and R embedded in the form.

- The infinity symbol visually reinforces the "continuum" concept
- The XR component is present but not immediately obvious — intentional
- The mark carries the `XR` so the wordmark does not have to
- The mark is designed to function independently of the wordmark
- Status: **in development**

### Lockup

The standard lockup is: **[CXR infinity mark] + `continuum`**

This is the primary brand expression. Spacing, sizing, and clear space rules
will be defined once the logomark is finalized.

### Placeholder Logotype (Current Use)

Until the final logomark is complete, the site and interim materials use
**`CXR`** as the nav mark and a typographic approximation of the lockup in
the hero. These are interim solutions only.

**Nav mark:**

- `C` — white (`#ffffff`), Outfit weight 800
- `XR` — Aurora Green (`#00E896`), Outfit weight 800
- Letter-spacing: -0.02em

**Hero logotype** (typographic approximation of the eventual lockup):

- `continuum` — white, Outfit weight 500 (the wordmark)
- `XR` — Aurora Green (`#00E896`), Outfit weight 800 (standing in for the logomark)
- Font size: `clamp(2.8rem, 7vw, 5rem)`
- Letter-spacing: -0.02em

Once the CXR infinity mark is finalized, the `XR` text in the hero is replaced
by the actual logomark, and the lockup becomes **[mark] + `continuum`** — exactly
as intended.

---

## Typography

ContinuumXR uses two typefaces: **Outfit** for display and headings, and
**Cabin** for body text. Both are available via Google Fonts.

### Outfit — Display & Headings

Used for all headings, titles, prominent UI labels, and both logotype forms.

- Source: [fonts.google.com/specimen/Outfit](https://fonts.google.com/specimen/Outfit)
- Weights in use: 500 (Medium), 700 (Bold), 800 (ExtraBold)
- Used for: H1–H4, section titles, navigation labels, logotype rendering

### Cabin — Body Text

Used for body copy, descriptions, metadata, and supporting UI text.

- Source: [fonts.google.com/specimen/Cabin](https://fonts.google.com/specimen/Cabin)
- Weights in use: 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold)
- Italic: 400 Italic available for emphasis
- Used for: body paragraphs, captions, labels, buttons, navigation links
- Historical note: Cabin was the original typeface used by Oculus for the Quest
  launch — a deliberate reference to the accessible, human-first XR aesthetic
  ContinuumXR is modeled after

### Google Fonts Import

```html
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;800&family=Cabin:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
```

### Usage Reference

| Context | Typeface | Weight | Notes |
|---|---|---|---|
| Hero logotype (`continuum`) | Outfit | 500 | Letter-spacing: -0.02em |
| Hero logotype (`XR`) | Outfit | 800 | Aurora Green |
| Nav mark (`C`) | Outfit | 800 | White |
| Nav mark (`XR`) | Outfit | 800 | Aurora Green |
| Display headings | Outfit | 500 | Letter-spacing: -0.02em |
| Section headings | Outfit | 600 | |
| Card headings | Outfit | 700 | |
| Body text | Cabin | 400 | Line-height: 1.7 |
| Navigation links | Cabin | 500 | |
| Labels / uppercase tags | Cabin | 700 | Uppercase, letter-spacing: 0.18em |
| Primary buttons | Cabin | 600 | |
| Metadata / tertiary text | Cabin | 400 | Reduced opacity |

---

## Color Palette

### Philosophy

The color system separates two distinct responsibilities:

1. **Aurora** — the expressive, atmospheric identity palette. Used for
   gradients, backgrounds, and Aether-themed visuals. Never used as an
   interactive affordance.

2. **Interactive affordances** — a white-based button system. Kept deliberately
   separate from the Aurora palette so affordances are always immediately
   recognizable.

**The single rule: Aurora colors are atmospheric, never interactive. Green is
identity, not affordance. White signals action.**

### Palette Evolution

The palette evolved through three phases before landing on Aurora:

| Phase | Palette | Reason changed |
|---|---|---|
| V1 | Sky blue `#4a90d9` | Generic, no distinctive identity |
| V2 | Nebula Mono (indigo/violet) | Philosophical: quintessence = violet historically; scrapped because it reads as "void" not "medium" |
| **Current** | **Aurora (green/teal/magenta on night sky)** | Direct physical analogy — aurora is literally light through the aether |

### Aurora Palette — Dark Mode (Only Mode)

ContinuumXR is **dark mode only**. There is no light mode for the OS or the
website. The UI lives inside the night sky behind the aurora.

This is philosophically consistent: aurora only exists against a dark sky.
Light mode would be a contradiction of the core visual metaphor.

#### Surfaces

| Name | Hex | Role |
|---|---|---|
| Night Sky | `#080D1A` | Primary background |
| Aurora Lift | `#0D1429` | Elevated surfaces, card backgrounds |
| Border | `#1A2545` | Default borders |
| Border Hover | `#2A3D60` | Hover state borders |

#### Aurora Accent Ramp — Vivid

Used in gradients, hero backgrounds, card gradients, and large decorative
elements. **Never used as text color or interactive affordance color.**

| Name | Hex | Contrast on `#080D1A` | Role |
|---|---|---|---|
| Aurora Green | `#00E896` | 12.0:1 ✅ AAA | Dominant ribbon — primary brand identity |
| Aurora Teal | `#00D4C8` | 10.4:1 ✅ AAA | Secondary atmospheric accent |
| Aurora Magenta | `#E040B0` | 5.1:1 ✅ AA | Ribbon edge, dramatic accent |

#### Text Hierarchy

| Role | Value | Contrast | Usage |
|---|---|---|---|
| Primary | `#ffffff` | 19.4:1 ✅ AAA | Headings, labels, all UI text |
| Secondary | `rgba(255,255,255,0.80)` | 12.1:1 ✅ AAA | Body text, subtitles |
| Tertiary | `rgba(255,255,255,0.45)` | 4.1:1 ⚠️ Large only | Section labels, metadata |

#### On-Gradient Text (Hero, Cards)

| Role | Value | Min contrast | Usage |
|---|---|---|---|
| Primary | `#ffffff` | 14–19:1 ✅ AAA | Headings, card titles |
| Secondary | `rgba(255,255,255,0.82)` | 10–12:1 ✅ AAA | Card body, subtitles |
| Accent em | `#00E896` | 12.0:1 ✅ AAA | `data` emphasis, decorative highlights |

### Interactive Affordances

#### CTA System — White

ContinuumXR does not use a colored CTA. White is the action color. This keeps
aurora colors as pure identity signals — nothing green, teal, or magenta ever
implies clickability.

The primary button is frosted semi-opaque at rest, resolving to solid white on
hover. The dark label (`#080D1A`) on the white hover state provides 19.4:1
contrast. See the Interactive Element Hierarchy section for full button specs.

> **The rule: green = identity | white = action | underline = link | neither = not interactive**

#### Status Colors

| Name | Hex | Bg | Usage |
|---|---|---|---|
| Confirm / Approve | `#00C882` | `#052818` | Success states |
| Decline / Error | `#E04448` | `#2A0E0E` | Error / destructive states |

---

## Interactive Element Hierarchy

A four-tier system. One rule governs all of it:

> **Border or fill = button | Underline = link | Neither = not interactive**

Green is identity, not affordance. White signals action.

### Tier 1 — Navigation Links

Plain text. No border, no fill, no background. For navigation and in-page
links that take the user somewhere (not trigger actions).

```
Rest:   color rgba(255,255,255,0.60)
Hover:  color #ffffff
```

**Use for:** site nav links (Vision, Roadmap), documentation links, in-page
anchors, any link whose purpose is navigation not action.

### Tier 2 — Primary Button

Frosted semi-opaque at rest. Solid white fill on hover, dark label.
Maximum one per section. Reserved for the most important action.

```
Rest:   background rgba(255,255,255,0.12)
        border 1px solid rgba(255,255,255,0.45)
        color #ffffff
        backdrop-filter blur(8px)
Hover:  background #ffffff
        border-color #ffffff
        color #080D1A
Border-radius: 8px | Font-weight: 600
```

**Use for:** GitHub (nav), "Get CXR", "Download", primary page CTAs.

### Tier 3 — Secondary Button

Ghost outline only at rest. Solid white fill on hover, dark label.
For supporting actions alongside a primary button.

```
Rest:   background transparent
        border 1px solid rgba(255,255,255,0.18)
        color rgba(255,255,255,0.65)
Hover:  background #ffffff
        border-color #ffffff
        color #080D1A
Border-radius: 8px | Font-weight: 500
```

**Use for:** "Read the Docs", "View Changelog", secondary page CTAs.

### Tier 4 — Tertiary Text Link

Underline at rest. No underline on hover, full white. For inline prose
links only — never used as a standalone element.

```
Rest:   color rgba(255,255,255,0.60)
        text-decoration underline
        text-decoration-color rgba(255,255,255,0.25)
        text-underline-offset 3px
Hover:  color #ffffff
        text-decoration-color transparent
```

**Use for:** inline cross-references, footnote links, "Apache 2.0" in footer,
"See also" references in documentation.

**Do not use Aurora Green or any Aurora accent color for text links.** Aurora
Green is identity — if green things are sometimes clickable and sometimes not,
the affordance system breaks down.

---

## Design Language

ContinuumXR's system-level design language is called **Aether**.

Aether is named for the classical philosophical concept of the fifth element —
the invisible medium that fills the space between everything. It is the substance
through which the OS mediates between the physical and virtual worlds.

**Tagline:** "The best interface is the one you don't see — you just see
everything through it."

### Three Defining Ideas

- **The fifth element.** Neither physical nor purely digital — the connective
  substance between states, between realities, between the user and their work.
- **The invisible medium.** The best spatial OS disappears. You feel its presence
  in how naturally everything works, not in how it announces itself.
- **The substance between states.** CXR exists on a continuum — passthrough to
  virtual, full motion to minimal, capable hardware to basic. Aether is the
  smooth gradient between all of these, never a hard boundary.

### Aurora as Aether's Visual Expression

The Aurora Borealis is a visible manifestation of the aether — light moving
through the invisible medium. This is the closest physical analogy to what
Aether describes conceptually, making Aurora the natural visual identity.

- The night sky is the OS — always present, never seen
- The aurora elements are the UI — emerging from nothing, returning to nothing
- The gradients shift and live — atmospheric, never static
- Green and teal dominate because they are the dominant aurora colors, and
  completely unowned in the XR/spatial computing space

### The Aether Material

All UI surfaces use a single, unified material: semi-translucent frosted glass
that fades in and out. Consistent across all reality modes. One material.
One identity.

### Particle Visual Language

Aether has a signature visual language for transitions: particles — fine,
grainy, dust-like — that coalesce into form or disperse back into nothing.
Organic and textural: sand assembling, dust scattering in light.

This is a brand-level visual identity element. It should inform marketing
visuals, motion graphics, video intros, and any brand animation. When CXR
content materializes or dematerializes, it does so through this particle system.

### Reality Modes (Working Names)

- **Grounded** — the user sees their physical space with digital content layered in
- **Unbound** — the user is in a virtual environment

Both modes use the same Aether material. The mode changes; the interface
identity does not.

For full Aether documentation, see `docs/design-philosophy.md`.

---

## Motion & Animation

### Core Principle: Everything Has Inertia

Nothing in CXR teleports. Elements have mass — present but not sluggish.
They ease into position like objects that exist in a world with soft physics.

### Three Motion Qualities

**Settle** — the default motion. Elements arriving, repositioning, responding
to layout changes. Ease-out curve with a slight overshoot. Spatial snapping
(windows docking, panels anchoring) uses settle — magnetic pull, gentle landing.

**Flow** — transitions between states. Opening an app, switching modes,
passthrough-to-virtual. Longer and more deliberate.

**Breathe** — ambient, idle motion. Subtle signs the system is alive.
Almost subliminal — if the user notices it consciously, it is too strong.

### Motion Intensity Levels

| Level | Description |
|---|---|
| **Full** | Default Aether. All three qualities active. |
| **Reduced** | Shorter durations, less overshoot, breathe disabled. Maps to OS reduced-motion preference. |
| **Minimal** | Near-instant transitions. Maximum responsiveness, zero decorative motion. |

### What Motion Never Does

- Bounce — undermines the grounded quality
- Overshoot aggressively — draws attention to the animation itself
- Block interaction — no motion should make the user wait

---

## Website

### Current State

Architecture-phase site: communicating vision, inviting contributors.
Not yet marketing a shipping product.

### Future Reference

When the project ships a first build, the site should evolve toward the
model established by `lineageos.org` — content-first, changelog visible,
device support prominent, community-driven. The Aurora identity will
differentiate CXR significantly from LineageOS's teal/gray aesthetic.

### Current Implementation Notes

- Dark mode only — no toggle
- Nav: `CXR` placeholder (Outfit 800, `XR` in `#00E896`)
- Hero: `continuum` + `XR` display logotype + animated Aurora gradient band
- Principles: four cards with animated Aurora radial gradients
- GitHub → Tier 2 Primary Button
- Vision, Roadmap, Documentation links → Tier 1 Navigation Links

---

## Trademark Status

| Mark | Type | Class | Status |
|---|---|---|---|
| `CONTINUUMXR` | Standard character mark | 009 | Not yet filed — clear on USPTO |
| `continuum` + CXR logomark | Design mark | 009 | Pending — file after visual identity is finalized |

### Filing Sequence

1. Form `ContinuumXR LLC` as the legal entity
2. File `CONTINUUMXR` as a standard character mark (Class 009) at or around
   public launch
3. Finalize the `continuum` wordmark and CXR infinity logomark
4. File the design mark once the visual identity is locked

---

## What's Still TBD

- Logomark final form (CXR infinity mark) and usage rules
- Clear space and minimum size guidelines
- Logo variants (monochrome, reversed, minimum size)
- Spacing / grid system
- Component library beyond the four interactive tiers
- Icon style guide
- Motion timing curves (specific easing values, durations)
- Brand guide designed output (PDF / web) — currently `.md` only
