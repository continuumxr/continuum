# ADR 0002: Kotlin as primary language for CXR Shell and runtime core

## Context
Phase 2 requires an implementation language for CXR Shell (the system launcher
replacement). Phase 3 requires a language for the runtime orchestrator, provider
interfaces, profile loader, and diagnostics.

Candidates considered:
- **Kotlin**: native Android language, strong typing, sealed classes, coroutines.
  Aligns with Pico Spatial SDK, Android XR SDK, and Google's platform direction.
- **Java**: functional but Kotlin is strictly superior for new Android projects.
- **Rust**: performance and safety, but requires JNI bridge for Android services.
  Better suited for performance-critical subsystems.
- **C/C++**: traditional for XR runtimes and Monado integration, but poor
  ergonomics for service orchestration and UI work on Android.

## Decision
Kotlin is the primary language for:
- CXR Shell (Phase 2)
- Runtime orchestrator, provider interfaces, profile loader, status reporting (Phase 3)
- Any Android service or system app layer

Rust is reserved for performance-critical provider implementations in later phases
(tracking, compositor) where JNI overhead is acceptable and safety matters.

C/C++ may be used where Monado or OpenXR integration requires it in later phases,
behind clean Kotlin interfaces.

## Scope
This decision applies to the AOSP-based phases of CXR (Phases 2–5).
If the project transitions to Android XR or Linux in later phases,
the language stack will be re-evaluated via a new ADR at that time.
Monado integration (long-term) will likely require C/C++ at the boundary,
but the orchestration layer should remain high-level where possible.

## Consequences
- Phase 2 CXR Shell is Kotlin + standard Android UI framework.
- Phase 3 runtime is pure Kotlin targeting Android.
- Soong (Android.bp) is the build system for CXR system components
  (CXR Shell, CxrRuntime) since they are built into the AOSP image.
  Gradle is reserved for standalone tooling that runs outside AOSP.
- Provider interface is a Kotlin interface, not a C ABI.
- Rust/C++ boundaries are deferred until they are actually needed.
- No premature optimization of the orchestration layer.
