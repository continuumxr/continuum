# Claude Code Task Spec: CXR Phase 3 — Runtime Scaffolding

## Context

You are working on Continuum XR (CXR), an open-source, runtime-first XR platform.
The repo is at https://github.com/ender9492/continuum

Phase 3 builds on the Phase 2 system image. The AOSP-based CXR image is already
bootable with CXR Shell as the default launcher.

Phase 3 goal: build the runtime scaffolding — provider interfaces, stub providers,
profile loader, orchestrator, diagnostics — and integrate it into the running system.

Read these docs before writing any code:
- docs/architecture.md — system design philosophy
- docs/providers.md — provider contract (the most important document)
- docs/capability-status-schema.md — status output schema
- docs/runtime-lifecycle.md — boot sequence and state model
- docs/profiles.md — profile format and validation rules
- docs/phase3-runtime-implementation-plan.md — full Phase 3 spec
- profiles/example/profile.json — reference profile

## Prerequisites

Phase 2 must be complete:
- `lunch cxr_x86_64-userdebug && m` builds cleanly
- Emulator boots into CXR Shell
- CXR Shell is the default home activity

## Principles (non-negotiable)

- Providers never lie about status. A stub that reports NOT_IMPLEMENTED is correct.
  A stub that reports READY for a capability it doesn't provide is a bug.
- Status is the primary interface. If something breaks, the status report explains why.
- No magic defaults. Configuration is explicit.
- No global mutable state in providers.
- Tests are not optional. Every deliverable includes tests.
- 2-space indent, UTF-8, LF line endings (see .editorconfig).

## Build integration

Runtime code is a system service built as part of the AOSP image.

Location: `packages/services/CxrRuntime/`
Build: Soong (Android.bp), NOT Gradle
Package: `org.continuumxr.runtime`

The runtime service is added to the CXR product makefile:
```makefile
PRODUCT_PACKAGES += CxrRuntime
```

## Task sequence

### Task 1: Provider contract (interfaces and data classes)

Create the provider interface and all supporting data types in
`packages/services/CxrRuntime/src/org/continuumxr/runtime/providers/`.

See `docs/phase3-runtime-implementation-plan.md` Deliverable 1 for the full spec.

All data classes must serialize to JSON. Use kotlinx.serialization if available
in the AOSP tree, or manual JSON construction via `org.json` (always available).

Verify: compiles as part of `m`.

### Task 2: Stub providers

Create seven stubs in `providers/stubs/`.

See `docs/phase3-runtime-implementation-plan.md` Deliverable 2 for the full spec.

Key: TimingStub is READY (System.nanoTime). All others are FAILED with NOT_IMPLEMENTED.

Write unit tests for each stub.

### Task 3: Profile model and loader

Create profile data classes and loader in
`packages/services/CxrRuntime/src/org/continuumxr/runtime/profiles/`.

See `docs/phase3-runtime-implementation-plan.md` Deliverable 3 for the full spec.

Place the example `profile.json` in the system partition (via the product makefile)
so the runtime can load it at boot.

Write unit tests for loader validation.

### Task 4: Runtime orchestrator

Create the core runtime in
`packages/services/CxrRuntime/src/org/continuumxr/runtime/`.

See `docs/phase3-runtime-implementation-plan.md` Deliverable 4 for the full spec.

Key correctness check: with the stub profile, runtime state must be FAILED
(because pose.head is required but pose.head.stub reports FAILED).

Write unit tests for state derivation.

### Task 5: CXR Runtime Service

Create `CxrRuntimeService` as a foreground Android service.

- Starts at boot or on CXR Shell launch
- Loads profile from system partition
- Runs orchestrator
- Logs status JSON to logcat (tag: CXR)
- Exposes status via bound service interface

Add to product makefile. Add to CXR Shell's startup path.

### Task 6: Shell integration

Update CXR Shell (from Phase 2) to:
- Bind to CxrRuntimeService
- Display runtime state (Starting/Running/Degraded/Failed)
- Show per-provider status
- List blocking issues with hints
- Show runtime version and active profile name

No fancy UI. A scrollable text view or simple list is sufficient.

### Task 7: Profile validator tool

Create `tools/validate-profile.py` (Python 3, stdlib only).

- Takes profile JSON path(s) as arguments
- Validates against the schema
- Prints issues to stdout
- Exits 0 if valid, 1 if errors

### Task 8: Tests and CI

- Unit tests for all deliverables
- Integration test: boot CXR image, verify status JSON in logcat
- Update `.github/workflows/ci.yml`:
  - Profile validation
  - Python linting for validator tool
  - (Kotlin tests run via AOSP build, may need manual verification)

## Definition of done

All eight tasks complete:
- Runtime service starts in the CXR system image
- Loads example stub profile
- Initializes all seven providers in dependency order
- Status JSON in logcat matches schema
- Runtime state is FAILED (correct for stub profile)
- CXR Shell displays runtime status
- Profile validator passes on all committed profiles
- Tests pass

## What NOT to do

- Do not add OpenXR headers or Monado integration. That's Phase 4.
- Do not add real tracking, rendering, or hardware access. That's Phase 4+.
- Do not use Gradle. This is a system service built with Soong/Android.bp.
- Do not add dependency injection frameworks. Constructor injection is sufficient.
- Do not add network calls, analytics, or external service communication.
- Do not add Rust, C++, or NDK. Pure Kotlin for Phase 3.
- Do not add features not described in this spec.
