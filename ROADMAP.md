# Continuum XR Roadmap (Reconciled)

This roadmap unifies decisions from all planning sessions (ChatGPT, Claude, repo docs).
It supersedes the previous `ROADMAP.md` and describes the canonical phase sequence.

Progress is incremental. Phases may pause or reorder as constraints are discovered.
This is not a commitment to timelines or delivery dates.

## Phase 1 — Architecture & charter definition (complete)

- Repository structure and documentation
- Runtime-first architectural definition
- Provider abstraction model (contracts in plain language)
- Capability/status schema definition
- Profile format definition
- ADR practice established

Deliverable: `docs/` directory, skeletal repo structure, example profile.

## Phase 2 — Bootable system image (cxr-bootstrap)

- AOSP source tree setup (`android-latest-release` / `android16-qpr2-release`)
- CXR product makefile and build targets (`cxr_x86_64`, `cxr_arm64`)
- CXR Shell (minimal launcher replacement, Kotlin)
- Resource overlays (branding, launcher replacement)
- Emulator boot validation
- Performance baseline (boot time, idle wakeups)
- Security posture (SELinux enforcing, no GMS)

Deliverable: a system image that boots into CXR Shell on the Android emulator.

See `docs/phase2-implementation-plan.md` for details.

## Phase 3 — Runtime scaffolding

- Provider interfaces and status model (Kotlin)
- Stub providers for all capability types
- Profile loader and validator
- Runtime orchestrator with dependency-ordered lifecycle
- CXR Runtime Service (foreground Android service)
- Diagnostics: status JSON output, shell integration
- Profile validator tool (Python, for CI)
- Unit and integration tests

Deliverable: runtime that starts, loads profiles, orchestrates stub providers,
and reports status honestly. Integrated into CXR Shell.

See `docs/phase3-runtime-implementation-plan.md` for details.

## Phase 4 — OpenXR surface & minimal compositor

- OpenXR runtime exposure (minimal, stubbed where necessary)
- Head pose provider (baseline, IMU-based)
- Display timing and view configuration
- Minimal compositor path sufficient for OpenXR conformance testing
- Timebase validation and synchronization
- First rendering output (test pattern, not production UI)

Deliverable: an OpenXR runtime that applications can connect to,
with honest capability reporting and minimal head pose.

## Phase 5 — Tracking providers & device packs

- Inside-out tracking provider(s)
- Controller input provider
- Hand tracking provider
- Calibration workflows (userland only, per `docs/architecture.md`)
- Continuum Pack system for device-specific support
- Device profiles for XR Elite (XR2 Gen 1) and Quest 3
- First hardware boot and testing via ADB
- Expanded diagnostics

Deliverable: CXR running on physical XR hardware with basic tracking
and input. Device-specific capabilities activated via packs.

## Phase X — Long-term evolution

These items have no fixed phase assignment. They are tracked here
as confirmed long-term goals from planning sessions.

### Android XR layer
- Evaluate Android XR AOSP when/if Google publishes a full platform base
- Layer Android XR APIs over CXR runtime where beneficial
- Maintain CXR independence (Android XR is additive, not a dependency)

### Linux migration
- Evaluate Halium/libhybris for Android driver compatibility on Linux
- Monado integration as OpenXR backend
- Transition from AOSP substrate to Linux where viable
- This is a long-term aspiration, not a near-term goal

### Spatial UI
- XR-native interaction model (not 2D Android UI ported to 3D)
- Visual inspiration: visionOS, Android XR, Horizon OS, Pico OS 6
- Final goal: "what makes sense in XR"
- Deferred until runtime and tracking are stable

### Advanced capabilities
- Eye tracking provider
- Body tracking
- Passthrough AR with scene understanding
- Spatial audio
- Advanced compositor (multi-layer, dynamic lighting)
- Performance tuning and optimization

### Ecosystem
- Developer SDK and documentation
- App distribution model (non-store, sideload-first)
- Community hardware support (additional device packs)

## Guiding principles (across all phases)

- **Boot before beauty**: a system that boots reliably is worth more than one
  that renders beautifully but crashes.
- **Observability before perfection**: status reporting and diagnostics come before
  tracking quality.
- **Honesty over polish**: never fake a capability. Report what works and what doesn't.
- **Portability over optimization**: keep the architecture device-agnostic.
  Device-specific work lives in providers and packs, not in core code.
- **Minimal OS, predictable performance, boring reliability.**
