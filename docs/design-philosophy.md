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
- **The substance between states.** CXR exists on a continuum — passthrough to
  virtual, full motion to minimal, capable hardware to basic. Aether is the
  smooth gradient between all of these, never a hard boundary.

## The Aether material

All UI surfaces in CXR use a single, unified material: semi-translucent frosted
glass that fades in and out. This material is consistent across both reality
modes — it looks and behaves the same whether the user is in their physical
space or a virtual environment.

The material must maintain adequate contrast against any background — a bright
physical room, a dark virtual environment, or anything in between. The frosted
quality provides legibility while preserving the translucent, ethereal character
of Aether. UI elements dissolve into view and fade out using animation language
consistent with the boot experience (see "The first 30 seconds" below).

One material. One identity. The mode changes; the interface doesn't.

## Reality modes: Grounded & Unbound

CXR has two reality modes (working names, subject to refinement):

- **Grounded** — the user sees their physical space. Digital content is layered
  into the real world. The user is *here*, with spatial tools around them.
- **Unbound** — the user is in a virtual environment. The physical room is
  replaced by a constructed space. The user is free from the constraints of
  their physical surroundings.

Both modes use the same Aether material, the same interaction model, and the
same nav system. The difference is the environment, not the interface.

Switching between Grounded and Unbound is always an explicit, user-controlled
action. The OS never decides which mode the user should be in (see "The user
controls the reality boundary" below).

Note: "Grounded" and "Unbound" capture the right intent — one is rooted in
physical space, the other frees you from it — but the final terminology may
be refined. Both terms should feel positive and empowering, with no negative
connotations.

## The first 30 seconds

When you put on a CXR headset and it boots, it should feel like your space
waking up with you.

### Boot sequence

1. **Android boot layer.** The Continuum logotype appears while the OS loads.
   This is structural branding — the last thing before CXR takes over. Brief,
   quiet, functional.

2. **The curtain lifts.** The logotype fades. Black recedes outward from the
   user's center of mass — not a hard circle expanding, but soft, organic
   edges like mist burning off in morning sun. As the black clears from
   surfaces and objects, they are simply *there* — already lit, already
   present. No pop-in, no materialization. Just revelation. The effect is
   like opening your eyes.

3. **Surfaces resolve.** As the environment is revealed, windows from the
   previous session resolve into place — as though they were always there
   and just became visible. The workspace wasn't loaded, it was *remembered*.

4. **Presence.** The system is ready. Nothing demands attention. Nothing asks
   the user to configure anything. They are simply here, and so is their
   workspace.

### Boot principles

- The boot connects the OS to the user and their environment. Whether Grounded
  or Unbound, the system should feel like it's emerging into the space *with*
  the user, not loading separately and then presenting itself.
- The sequence reads as three beats: *wake up → space revealed → workspace
  remembered.* No friction, no branding interruption in the lived experience.
- Grounded and Unbound boot paths are siblings, not different experiences.
  Same motion, same timing, same emotional arc — just different scenery
  resolving around the user.
- The feeling is calm but alive. The system arrived before you noticed it
  arriving.

## New user experience (NUX)

The NUX follows the Super Mario Bros. design principle: introduce one element
and one action at a time. The environment is the teacher. No tutorial text,
no instruction overlays. The user learns by doing.

### NUX sequence

1. **"Is this your first time?"** Before anything else, the user is asked
   whether this is their first time using Continuum. If not, they skip to
   a standard configuration flow. No one is forced through the NUX twice.

2. **Mode choice.** The user chooses Grounded or Unbound. This is their first
   decision — the system respects their agency from the very beginning, and
   they become comfortable in their chosen surroundings from the start.

3. **The switch.** The user is in darkness. A single object appears nearby —
   a switch, a pull-string, something that invites exactly one action: flip
   or pull. This teaches the user's first spatial interaction (grab/pull)
   with zero instruction. When activated, a spotlight illuminates a pedestal.

4. **The clock.** On the pedestal sits a clock. The user picks it up and sets
   the time — a real system configuration step presented as a spatial
   interaction. Moving the hands teaches fine manipulation and rotation.
   Setting the time is a meaningful task wrapped in a spatial experience.

5. **Placement.** Once the clock is set, the user places it somewhere — on a
   wall, on a surface. This teaches spatial anchoring. The clock settles into
   position using the settle motion.

6. **The space reveals.** The darkness recedes as the user looks around.
   Their gaze and movement uncover the space — mapping the room (if hardware
   supports it) while simultaneously orienting the user through natural
   curiosity. The act of looking is what reveals the environment.

7. **Optional setup objects.** Additional spatial objects become available for
   optional system configuration: a globe or wall map for location/region, a
   radio with a tuning dial for Wi-Fi network selection. These are optional —
   a user does not need Wi-Fi, does not need to set location. Each object
   teaches a new interaction type naturally.

8. **The awe moment.** The full environment resolves around the user. In
   Unbound, this is where the virtual space comes alive — ambient light,
   depth, presence. In Grounded, the user sees their physical room with
   digital objects sitting naturally in it. Both should produce a moment
   of genuine wonder.

9. **Seamless transition.** There is no "onboarding complete" screen. The user
   simply has a workspace. They've placed things, they've found their space,
   they've practiced core interactions. The NUX dissolved into use.

### NUX principles

- Experiential, not instructional. The environment teaches through affordance.
- One mechanic at a time, introduced in a safe context, with immediate reward.
- Every system configuration step is a spatial interaction, not a 2D form.
- Not everything is covered in the first session. Advanced features surface
  contextually over the first few days — a single, non-repeating suggestion
  when the user does something that has a more efficient alternative.
- Optional voice assistant (local, private, on-device) can answer questions
  about the OS without breaking immersion. Never forced, never listening
  without explicit activation, transparent about any network access.

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
Grounded-to-Unbound transitions. These are longer, more deliberate, and use
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

## Navigation: The Arc

CXR's system navigation is a curved surface — the Arc — that wraps around the
user at a comfortable distance. The Arc follows a 120-degree curve but only
occupies the space it needs within that curvature.

### Two zones

- **Lower Arc** — apps, launcher, workspaces. The "doing" zone. This is where
  the user goes to open things, switch between things, and arrange their space.
- **Upper Arc** — notifications, quick settings, status (time, battery,
  connectivity). The "awareness" zone. This is where the user glances to
  check on things.

### Behavior

- **Stationary on X/Y, follows on Z.** The Arc stays at a consistent position
  relative to the user's orientation but follows them as they move through
  space on the Z axis.
- **Near-invisible when idle.** A subtle edge or boundary, enough to know
  it's there, not enough to distract.
- **Summoned and dismissed together.** One gesture reveals both arcs, one
  gesture hides both. If the user wants just one, they look at the one they
  need and interact. The other is present but doesn't demand engagement.
- **Consistent across hardware.** The Arc feels the same in 3-DOF and 6-DOF —
  same lag, same movement, same interaction model. In 3-DOF the entire
  environment is head-relative, so the Arc follows naturally. In 6-DOF the
  Arc stays with the user as they move through space.
- **Uses the Aether material.** Semi-translucent frosted glass, consistent
  with all other UI surfaces.

### Summoning

- **With hand tracking:** Palm-up pinch on the dominant hand summons/dismisses
  the Arc. The non-dominant hand uses the same gesture for alt/option select.
- **Without hand tracking:** Controller button press or gaze-dwell on a
  trigger point.
- **Handedness is user-configurable** and set during onboarding.

## Notifications

Notifications in CXR inform without interrupting. They follow three tiers
based on urgency, with delivery designed for accessibility across hearing
and vision capabilities.

### Three tiers

**Tier 1 — Ambient.** Something happened, but it can wait indefinitely. A new
email, an app update, a calendar event in two hours. No immediate signal. The
notification accumulates silently in the notification app, accessible from the
Upper Arc. A subtle indicator on the Upper Arc shifts warmth slightly —
present but completely ignorable.

**Tier 2 — Aware.** Time-relevant but not urgent. A meeting in 10 minutes, a
timer almost done, a download completed. A notification toast fades into view
at top-center of the user's FOV, using the same dissolve-in animation as the
boot experience. A single spatial audio tone accompanies it. Both visual and
audio cues ensure accessibility — hearing-impaired users see the toast,
vision-impaired users hear the tone. The toast fades after a few seconds if
not acknowledged. The notification then moves to the notification app for
later review.

**Tier 3 — Urgent.** Rare by design. An incoming phone call, a critical system
alert, a safety warning. The toast appears at top-center FOV and persists until
acknowledged. A distinct spatial audio cue accompanies it. The user can select
to engage or dismiss with a gesture. Urgent notifications never block what the
user is doing — they persist visually but the user can continue working.

### Defaults and control

All apps default to Tier 1 (Ambient). Apps can request Tier 2 or 3, but the
user approves. This inverts the current industry model where apps assume they
deserve attention and users must manually silence them.

No badge counts. No accumulating red dots. No guilt. Missed notifications live
in the notification app and the user checks when they choose.

## Hardware capability tiers

CXR is designed to run across a wide range of hardware. Features adapt to
capability — the experience scales, the identity stays consistent.

| Tier | Tracking | Cameras | Depth | Eye Tracking | Hand Tracking |
|------|----------|---------|-------|--------------|---------------|
| Basic | 3-DOF (IMU) | None | No | No | No |
| Basic+ | 3-DOF | RGB | No | No | Basic (RGB) |
| Mid | 6-DOF | IR | No | No | Good (IR) |
| Mid+ | 6-DOF | IR + RGB | No | No | Good + passthrough |
| Full | 6-DOF | IR + RGB | ToF/LiDAR | Yes | Excellent + depth |

Additional sensors that may be present: IR illuminators (low-light hand
tracking), magnetometer (heading/drift correction), proximity sensor (auto
wake/sleep), ambient light sensor (environmental responsiveness).

### Hand tracking as baseline

Any device with a camera supports hand tracking. RGB camera hand tracking is
not as precise as IR-based tracking, but it is functional. CXR treats hand
tracking as a standard input method from Basic+ tier onward. Devices with
additional sensors (IR cameras, depth sensors, IR illuminators) get enhanced
tracking fidelity. The input system scales; the interaction model is the same.

### Input fallbacks

- No hand tracking (Basic tier): controller or touchpad input required
- No eye tracking: head-gaze or pointer input
- No spatial mapping: headset-relative positioning
- No depth sensing: RGB-only passthrough (no depth correction)

The system always works. The precision depends on capability.

## Core interaction principles

### 1. The user controls the reality boundary

CXR never decides for you whether you should see the physical world or a virtual
environment. There is no automatic Grounded-to-Unbound transition. There is no
"the system thinks you should see your room now."

Reality mode is an explicit, user-controlled toggle. Always. The user decides
when they want to be Grounded, when they want to be Unbound, and when they want
something in between. The OS provides the tools and respects the choice.

The single exception is the safety boundary / guardian system, which may force
passthrough for user safety. This is consistent with all existing platforms and
is a reasonable safety decision — the system protects the user from physical
harm, not from their own choices about reality. The guardian is only active in
Unbound mode (in Grounded mode, the user can see their physical space). The
boundary follows Aether's visual language — a soft gradient that becomes
visible as the user approaches the edge, not a hard grid wall.

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
system with just hand tracking (Basic+ tier and above).

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

CXR's visual character adapts to the environment, even though the UI material
itself is unified. The Aether material (semi-translucent frosted glass) is
consistent across modes, but the way it interacts with its surroundings changes
based on context.

### Environmental responsiveness

By default, CXR's UI visually responds to the environment it inhabits:

- Panel materials adapt to ambient lighting (warmer in warm rooms, cooler in
  cool rooms)
- Shadows and reflections are consistent with the dominant light direction
- The UI feels like it inhabits the space rather than ignoring it
- In Grounded mode, panels respond to the physical environment's lighting
- In Unbound mode, panels respond to the virtual environment's light sources

This environmental responsiveness can be toggled off by the user for a
consistent appearance regardless of setting.

### Organic warmth

All UI shares an organic quality that distinguishes CXR from the clinical
precision of visionOS or the utilitarian flatness of Android:

- Soft edges, not hard geometric cuts
- Subtle, natural motion — elements ease into position, they don't snap
- Typography that breathes (generous spacing, readable at XR distances)
- Rounded forms that feel approachable, not sterile
- The system feels warm, not cold. Alive, not mechanical.

### Visual fallback strategy

Aether is designed to scale down, not just up:

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

### From Oculus (pre-Meta)
- The Quest NUX demonstrated the power of awe in first-time experiences
- Rift Home proved that interactive, customizable virtual spaces create
  personal connection — users want to inhabit their space, not just view it
- "First Contact" showed that wordless, experiential onboarding is more
  effective than instruction

### What CXR does differently
- **Aether**: a unified design language with one material, adaptive to context
- **User-controlled reality boundary**: no automatic mode switching
- **Privacy as architecture**: sensor data reduction, tiered permissions,
  audit logs (see `docs/privacy-architecture.md`)
- **Hardware longevity**: the OS exists to keep devices alive beyond
  vendor end-of-life
- **Persistent spatial layouts**: your workspace survives across sessions,
  stored locally and encrypted
- **Open theming**: the visual language is a default, not a mandate
- **Experiential onboarding**: learn by doing, not by reading

## What CXR avoids

- **Mimicry**: CXR should never be described as "open-source visionOS" or
  "Horizon OS but private." It is its own thing, informed by the industry
  but not derivative of any single product.

- **Feature parity as a goal**: the goal is not to replicate every feature
  of every competitor. The goal is to build the spatial OS that is correct —
  private, persistent, portable, and built to last.

- **Dark patterns**: no artificial urgency, no notifications that demand
  attention, no "engagement" metrics, no badge counts, no guilt. The OS
  serves the user, not the other way around.

- **Sensory overload**: spatial computing has more degrees of freedom than
  flat screens. CXR uses restraint. Fewer elements, more space, more quiet.
  The system should feel like a calm workshop, not a Times Square billboard.

- **Forced peripherals**: no "you must have controllers to set up." The system
  works with just hand tracking from first boot (Basic+ tier and above).

- **Automatic decisions about reality**: the OS never decides when the user
  should or shouldn't see the physical world (except safety boundaries).

## Open design questions

1. How far do we take non-planar interaction? (Planar windows as default with
   spatial options? A fully spatial shell? App-level freedom?)
2. What specific controls live on the Upper and Lower Arcs?
3. What does the guardian / boundary setup experience feel like in detail?
4. How do virtual environments work? (User-created? Marketplace? Built-in?
   Interactive and customizable like Rift Home?)
5. What does the "mind palace" concept look like concretely?
6. How do accessibility features work in spatial computing?
7. How does multi-user / shared space work?
8. App lifecycle in 3D: what happens when you open, minimize, and close
   a spatial app?
9. How do windows/apps migrate between Grounded and Unbound modes?
10. What is the "awe moment" equivalent for Grounded mode?
11. Final terminology for Grounded / Unbound.

## Implementation phasing

Phase 2–3: No visual design work. Focus is on boot reliability and runtime
architecture. CXR Shell is functional text, not final UI.

Phase 4–5: Aether prototyping begins alongside real rendering capabilities.
Unified material, motion language, and environmental responsiveness implemented.
NUX prototyped.

Phase X: Full design system. Motion language refinement. Accessibility pass.
Built-in theme options. Virtual environment customization. Advanced spatial
interaction models. Community theme support.

## Relationship to other documents

- `docs/privacy-architecture.md` — the privacy principles that inform design
  choices (user control, local data, audit transparency)
- `docs/architecture.md` — the runtime and provider model that enables
  spatial multitasking and input flexibility
- `docs/vision.md` — the project mission (longevity, portability, ownership)
