# Design Philosophy

This document defines Continuum XR's design identity — what it feels like to use,
how it looks, how it behaves, and why it makes the choices it makes.

CXR is not a clone of visionOS, Horizon OS, Pico OS, or Android XR. It studies
what works across all spatial operating systems and builds something that makes
its own choices, grounded in a coherent set of principles.

## Aether

CXR's design language is called **Aether**.

In classical philosophy, aether was the fifth element — not earth, water, fire,
or air, but the substance that fills the space between everything. The medium
through which light travels. Immaterial but omnipresent. Invisible but essential.

That is what a spatial operating system does. It is the medium between you and
your content, between physical and virtual, between one application and another.
You don't see the aether itself — you see everything *through* it.

**The best interface is the one you don't see — you just see everything through it.**

This principle informs every design decision in CXR. The OS is not a destination.
It is not a spectacle. It is the invisible medium that makes spatial computing
feel like home. Every surface, every motion, every interaction should serve
the user's intent without drawing attention to the system itself.

Three ideas define Aether:

- **The fifth element.** Neither physical nor purely digital — the connective
  substance between states, between realities, between the user and their work.
- **The invisible medium.** The best spatial OS disappears. You feel its presence
  in how naturally everything works, not in how it announces itself.
- **The substance between states.** CXR exists on a continuum — glass to material,
  passthrough to virtual, full motion to minimal. Aether is the smooth gradient
  between all of these, never a hard boundary.

## The first 30 seconds

When you put on a CXR headset and it boots, it should feel like your space
waking up with you.

### Boot sequence

1. **Android boot layer.** The Continuum logotype appears while the OS loads.
   This is structural branding — the last thing before CXR takes over. Brief,
   quiet, functional.

2. **The curtain lifts.** The logotype fades. Black fades up to reveal the
   user's environment — passthrough or the last-used virtual environment —
   like opening your eyes.

3. **The pulse.** A concentric pulse flows outward from the user's center of
   mass — roughly chest height — expanding as a soft sphere into the space.
   The user catches it mid-expansion as it flows past them and into the room.
   This communicates that the OS is *sensing* the space, reaching out to
   understand and connect with the environment. The user is the origin point.

4. **Surfaces resolve.** As the pulse passes over surfaces — physical or
   virtual — they subtly respond. A faint ripple of light, a gentle material
   shift that says "recognized." Windows from the previous session don't pop
   in; they resolve out of the surfaces where the pulse touched them, as
   though they were always there and just became visible. This reinforces
   spatial persistence: the workspace wasn't loaded, it was *remembered*.

5. **Presence.** The system is ready. Nothing demands attention. Nothing asks
   the user to configure anything. They are simply here, and so is their
   workspace.

### Boot principles

- The boot connects the OS to the user and their environment. Whether passthrough
  or virtual, the system should feel like it's emerging into the space *with*
  the user, not loading separately and then presenting itself.
- The sequence reads as three beats: *wake up → sense the space → remember
  the workspace.* No friction, no branding interruption in the lived experience.
- Passthrough and virtual boot paths are siblings, not different experiences.
  Same motion, same timing, same emotional arc — just different scenery
  resolving around the user.
- The feeling is calm but alive. The system arrived before you noticed it
  arriving.

## Motion language

Motion is the connective tissue of Aether. It is what makes the design language
feel like a *system* rather than a collection of static surfaces.

### Core principle: everything has inertia

Nothing in CXR teleports. Elements have mass — not heavy, not sluggish, but
present. They ease into position like objects that exist in a world with soft
physics. This is what separates "alive" from "animated."

### Three motion qualities

**1. Settle** — the default motion. Elements arriving, repositioning, or
responding to layout changes. Think of placing a card on a table: it doesn't
slam down, it settles with a tiny cushion of air. Ease-out curve, slight
overshoot that resolves naturally. This is the motion the user sees most often
and it should be so quiet they barely notice it.

Spatial snapping (windows docking to each other, panels anchoring to surface
edges, apps grouping into stacks) uses the settle motion. When the user drags
an element near a snap point, it finds the alignment and settles into place —
like a drawer closing on soft-close hardware. A moment of magnetic pull, then
a gentle landing. If the user keeps dragging past, it releases. This behavior
is always on; the precision of snapping with the organic feel of Aether.

**2. Flow** — transitions between states. Opening an app, switching modes,
passthrough-to-virtual transitions. These are longer, more deliberate, and use
the full depth of the space. An app opening doesn't just scale up — it unfolds
from its icon position into its spatial footprint, materials shifting as it
moves. Flow motions respect the spatial relationship between origin and
destination.

**3. Breathe** — ambient, idle motion. Subtle signs that the system is alive
and present without demanding attention. A panel's shadow shifting as
environmental light changes. A gentle pulse on a notification indicator. The
cursor resting with a barely perceptible idle drift. These should be almost
subliminal — if the user notices them consciously, they're too strong.

### Motion intensity (user preference)

Motion is not one-size-fits-all. CXR provides a motion intensity setting:

- **Full** — default Aether. Settle, flow, and breathe all active. The complete
  organic experience.
- **Reduced** — shorter durations, less overshoot, breathe animations disabled.
  Still organic but quicker. Maps naturally to accessibility preferences for
  reduced motion.
- **Minimal** — near-instant transitions with just enough easing to avoid
  feeling broken. For users who want maximum responsiveness and zero decorative
  motion.

Spatial snapping behavior works the same at every level — just with different
cushion in the landing. The system always feels like CXR regardless of the
motion intensity setting.

### What motion never does in CXR

- **Bounce.** Playful but undermines the grounded quality.
- **Overshoot aggressively.** Draws attention to the animation itself.
- **Block interaction.** No motion should make the user wait.

## Core interaction principles

### 1. The user controls the reality boundary

CXR never decides for you whether you should see the physical world or a virtual
environment. There is no automatic passthrough-to-VR transition. There is no
"the system thinks you should see your room now."

Reality mode is an explicit, user-controlled toggle. Always. The user decides
when they want to see their room, when they want to be in a virtual space, and
when they want something in between. The OS provides the tools and respects the
choice.

The single exception is the safety boundary / guardian system, which may force
passthrough for user safety. This is consistent with all existing platforms and
is a reasonable safety decision — the system protects the user from physical
harm, not from their own choices about reality.

This is both a UX principle and a privacy principle. A system that controls
when you see reality is a system that controls when you *don't* — and CXR
does not make that decision for anyone.

### 2. Spatial multitasking is the foundation

CXR's compositor renders multiple applications — 2D and 3D — coexisting in
the same shared space. This is not "switch between apps." This is "your browser
is floating next to your 3D model viewer next to your chat window, and they're
all live, all interactive, all real."

This follows the visionOS and Pico OS 6 architectural model where the OS
owns the rendering pipeline and composites all content in a unified space,
as opposed to the Horizon OS and Android XR model of "one immersive app
at a time."

Apps can anchor to physical surfaces, float in space, or attach to virtual
furniture. The user arranges their workspace. The system renders it.

### 3. Input is seamless and modeless

CXR supports hands, controllers, eye gaze, keyboard, mouse, and game controllers.
The system adapts to whatever input is active without requiring the user to
"switch modes."

You can be typing on a Bluetooth keyboard, reach up and pinch to move a window,
then grab a controller for a game — all without telling the system what you're
doing. The OS observes and responds. Input methods coexist, not compete.

No peripheral is required. Users must be able to complete setup and use the
system with just hand tracking.

### 4. Your spatial layout persists

When you take the headset off and come back later — hours, days, weeks — your
workspace is where you left it. Windows remember their positions. Apps remember
their spatial anchors. Your room is your room, and your arrangement of tools
within it is yours.

This is powered by persistent spatial anchors tied to the physical environment.
When CXR recognizes your space, it restores your layout. If you move to a
different room, you get a fresh canvas (or can load a saved layout). Different
rooms can maintain different layouts.

On hardware without spatial mapping, persistence degrades gracefully. The
headset itself becomes the anchor point. Layouts persist based on time, distance,
and location relative to the headset. On reboot, all items persist but centering
may reset. The user can re-center manually. Full spatial hardware gets full
spatial persistence. Basic hardware gets headset-relative persistence. The
user always gets their workspace back; the precision depends on capability.

Spatial persistence data is stored locally and encrypted. It never leaves
the device (see `docs/privacy-architecture.md`).

## Visual language: Adaptive Materiality

CXR's visual language — expressed through Aether — changes based on the
relationship between virtual content and physical reality. This is the core
visual concept: the interface adapts to where it is.

### Passthrough mode: Glass

When the user is in passthrough (seeing the physical world), UI elements use
a glassy, translucent material language:

- Frosted glass panels with subtle depth and refraction
- UI elements feel like they exist *in* your space, not pasted on top of it
- Light interaction: panels respond to the lighting in your physical environment
- Content is legible but the room is always visible through the interface
- The effect: your digital tools feel like they belong in your living room

### Virtual mode: Material

When the user is in a virtual environment, UI elements shift to a solid,
material language:

- Clean surfaces with subtle depth, shadows, and dimensionality
- UI elements feel constructed, intentional, part of the virtual world
- Consistent lighting tied to the virtual environment's light sources
- Content is grounded and present, not floating ethereally
- The effect: your tools feel like they were built for this space

### Shared quality: Organic warmth

Both modes share an organic quality that distinguishes CXR from the clinical
precision of visionOS or the utilitarian flatness of Android:

- Soft edges, not hard geometric cuts
- Subtle, natural motion — elements ease into position, they don't snap
- Typography that breathes (generous spacing, readable at XR distances)
- Rounded forms that feel approachable, not sterile
- The system feels warm, not cold. Alive, not mechanical.

### Environmental responsiveness

By default, CXR's UI visually responds to the physical environment:

- Panel materials adapt to ambient lighting (warmer in warm rooms, cooler in
  cool rooms)
- Shadows and reflections are consistent with the real-world light direction
- The UI feels like it inhabits your space rather than ignoring it

This environmental responsiveness can be toggled off by the user for a
consistent appearance regardless of setting.

### Visual fallback strategy

Aether is designed to scale down, not just up. CXR targets everything from
basic Android phones to high-end XR headsets:

- No glass effects → solid panels with transparency
- No environment lighting → consistent flat lighting
- No spatial mapping → headset-relative positioning
- No hand tracking → controller or touchpad input
- No eye tracking → head-gaze or pointer input

Visual and experiential consistency is maintained across capability levels.
The system always *feels* like CXR, even when it can't render the full
Aether aesthetic. The experience degrades, but the identity doesn't.

### Theming

CXR ships with Aether as the default design language, but as an open platform,
the visual layer is themeable:

- Built-in theme options first (color overlays, adjustable edge styles,
  transparency controls)
- Custom theme installation deferred to later roadmap
- Themes can override material properties, colors, motion curves, and
  typography
- The system ensures readability and accessibility regardless of theme
  (minimum contrast ratios, motion sensitivity options)

## What CXR learns from others

### From visionOS
- The OS-level compositor that owns all rendering is architecturally correct
- Frosted glass materials work beautifully in passthrough
- Eye + pinch as an input paradigm is proven
- Spatial audio grounded in real-world positions sells the illusion

### From Horizon OS
- Hand tracking quality and responsiveness set the standard
- The virtual keyboard using surface detection is genuinely useful
- Quick settings and system UI should be instantly accessible
- Passthrough quality (depth-corrected, low-distortion) matters enormously
- Spatial keyboard and trackpad (Horizon OS 2.1) when hardware supports it

### From Pico OS 6
- Unified rendering across 2D and 3D apps is the right architecture
- True spatial multitasking (not single-immersive-app) is the future
- Supporting OpenXR, WebXR, and native Android as equal citizens is correct
- Developer accessibility (emulator, standard tooling) grows ecosystems

### From Android XR
- Cross-device continuity (headset ↔ phone ↔ watch) is valuable long-term
- Gemini-style AI integration shows the potential of always-available assistance
- Open platform licensing enables hardware diversity

### What CXR does differently
- **Aether**: a named design language with adaptive materiality — no other OS
  changes its visual language based on the reality/virtual boundary
- **User-controlled reality boundary**: no automatic passthrough decisions
- **Privacy as architecture**: sensor data reduction, tiered permissions,
  audit logs (see `docs/privacy-architecture.md`)
- **Hardware longevity**: the OS exists to keep devices alive beyond
  vendor end-of-life
- **Persistent spatial layouts**: your workspace survives across sessions,
  stored locally and encrypted
- **Open theming**: the visual language is a default, not a mandate

## What CXR avoids

- **Mimicry**: CXR should never be described as "open-source visionOS" or
  "Horizon OS but private." It is its own thing, informed by the industry
  but not derivative of any single product.

- **Feature parity as a goal**: the goal is not to replicate every feature
  of every competitor. The goal is to build the spatial OS that is correct —
  private, persistent, portable, and built to last.

- **Dark patterns**: no artificial urgency, no notifications that demand
  attention, no "engagement" metrics. The OS serves the user, not the other
  way around.

- **Sensory overload**: spatial computing has more degrees of freedom than
  flat screens. CXR uses restraint. Fewer elements, more space, more quiet.
  The system should feel like a calm workshop, not a Times Square billboard.

- **Forced peripherals**: no "you must have controllers to set up." The system
  works with just hand tracking from first boot.

- **Automatic decisions about reality**: the OS never decides when the user
  should or shouldn't see the physical world (except safety boundaries).

## Open design questions

1. How far do we take non-planar interaction? (Planar windows as default with
   spatial options? A fully spatial shell? App-level freedom?)
2. What does the system menu / quick settings look like spatially?
3. How does notification delivery work in a spatial OS without dark patterns?
4. What does the guardian / boundary setup experience feel like?
5. How do virtual environments (backgrounds/skyboxes) work?
6. What does the "mind palace" concept look like concretely?
7. How do accessibility features work in spatial computing?
8. What does the onboarding / first-time experience look like?
9. How does multi-user / shared space work?
10. App lifecycle in 3D: what happens when you "close" a spatial app?

## Implementation phasing

Phase 2–3: No visual design work. Focus is on boot reliability and runtime
architecture. CXR Shell is functional text, not final UI.

Phase 4–5: Aether prototyping begins alongside real rendering capabilities.
Adaptive Materiality and motion language implemented. Environmental
responsiveness.

Phase X: Full design system. Motion language refinement. Accessibility pass.
Built-in theme options. Advanced spatial interaction models. Community theme
support.

## Relationship to other documents

- `docs/privacy-architecture.md` — the privacy principles that inform design
  choices (user control, local data, audit transparency)
- `docs/architecture.md` — the runtime and provider model that enables
  spatial multitasking and input flexibility
- `docs/vision.md` — the project mission (longevity, portability, ownership)
