# ContinuumXR

**ContinuumXR** is an open-source, privacy-first extended reality operating system built to keep standalone VR and AR hardware usable long after vendor end-of-life.

Modern XR headsets are powerful, expensive devices that become unusable when companies shut down stores, abandon software, or lock hardware behind proprietary services. ContinuumXR exists to break that cycle.

**Website:** [continuumxr.org](https://continuumxr.org)

---

## What ContinuumXR is

- A **runtime-first XR platform** built around OpenXR
- Built on **AOSP** for hardware compatibility, with a clean architecture that allows future evolution
- A **privacy-by-architecture** system where all sensor data stays on your device
- A **portable OS** that installs via standard fastboot on Treble-compliant devices
- A **spatial operating system** targeting true multitasking — multiple 2D and 3D apps coexisting in shared space

## What ContinuumXR is not

- A fork of an existing XR operating system
- A vendor store or account platform
- A telemetry or data-collection system
- A promise of near-term usability
- Dependent on Google services or proprietary cloud APIs

## Project status

CXR is in **Phase 1 (complete) → Phase 2 (next)**.

Phase 1 established the architecture, contracts, and documentation. Phase 2 will produce the first bootable system image (`cxr-bootstrap`) — an AOSP-based image that boots into CXR Shell on the Android emulator.

There are no public builds yet. See the [Roadmap](ROADMAP.md) for the full phase sequence.

## Core principles

**Privacy by architecture** — All sensor data (cameras, eye tracking, hand tracking, microphones, depth sensors) stays on your device by default. No telemetry, no cloud dependency, no account required. Apps receive the minimum processed output needed for their stated purpose — never raw sensor streams. See [Privacy Architecture](docs/privacy-architecture.md).

**Hardware longevity** — Your headset should remain usable without vendor permission. ContinuumXR decouples the OS from vendor lifecycles and delivers device-specific support through installable packs, not baked OS images.

**Runtime-first design** — OpenXR is the application contract. Hardware capabilities are supplied by modular providers. The runtime orchestrates providers, reports status honestly, and fails loudly when something is missing. See [Architecture](docs/architecture.md).

**User ownership** — No vendor store. No mandatory account. No forced controllers for setup. The system boots and functions fully offline. The user controls the reality boundary — CXR never decides when to switch between passthrough and virtual.

## Design direction

ContinuumXR's system-level design language is called **Aether** — named for the classical fifth element, the invisible medium between the physical and virtual worlds. The visual identity is expressed through the **Aurora** palette: green, teal, and magenta on a night sky background. See [Design Philosophy](docs/design-philosophy.md) and [Brand Guidelines](docs/brand-guidelines.md).

## Documentation

| Document | Description |
|----------|-------------|
| [Vision](docs/vision.md) | Project mission and rationale |
| [Architecture](docs/architecture.md) | Runtime-first design, provider model |
| [Privacy Architecture](docs/privacy-architecture.md) | Sensor data handling, permission model, audit system |
| [Design Philosophy](docs/design-philosophy.md) | UX direction, Aether design language, interaction principles |
| [Brand Guidelines](docs/brand-guidelines.md) | Naming system, typography, color palette, visual identity |
| [Providers](docs/providers.md) | Provider contracts and status model |
| [Profiles](docs/profiles.md) | Device profile format and validation |
| [Capability Status Schema](docs/capability-status-schema.md) | Machine-readable status output |
| [Runtime Lifecycle](docs/runtime-lifecycle.md) | Boot sequence and state model |
| [Roadmap](ROADMAP.md) | Phase sequence and guiding principles |
| [Build Guide](docs/build-guide.md) | Step-by-step AOSP build instructions |
| [Phase 2 Plan](docs/phase2-implementation-plan.md) | Bootable AOSP image spec |
| [Phase 3 Plan](docs/phase3-runtime-implementation-plan.md) | Runtime scaffolding spec |

## Repository structure

```
continuum/
├── docs/           Architecture, contracts, decisions, and plans
│   └── adr/        Architecture Decision Records
├── profiles/       Device profiles (provider composition per device)
│   └── example/    Stub-only example profile
├── providers/      Provider interfaces and implementations (future)
├── runtime/        Runtime core (future)
├── tools/          Developer utilities and validators
├── ROADMAP.md      Phase sequence
├── CONTRIBUTING.md  Contribution guidelines
├── STATUS.md       Current project status
└── LICENSE         Apache 2.0
```

## Contributing

ContinuumXR is in early architectural definition. The priority is correctness of structure and contracts — not feature velocity.

See [CONTRIBUTING.md](CONTRIBUTING.md) for what to contribute now and what to wait on.

## License

Apache 2.0
