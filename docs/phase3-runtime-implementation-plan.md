# Phase 3 Implementation Plan: Runtime Scaffolding

This document defines Phase 3 of Continuum XR — the first runtime code running
inside the CXR system image built in Phase 2.

## Prerequisites

Phase 2 must be complete:
- AOSP-based system image boots into CXR Shell
- Build system produces `cxr_x86_64-userdebug` and `cxr_arm64-userdebug` images
- CXR Shell is the default home activity

## Goal

Build the runtime scaffolding that will eventually host the OpenXR surface:
- Provider interfaces and status model
- Stub providers for all capability types
- Profile loader and validator
- Runtime orchestrator with dependency-ordered provider lifecycle
- Diagnostics and status reporting
- Integration into CXR Shell for status display

## Language and build

- Language: Kotlin (see ADR 0002)
- Build: integrated into AOSP build system as system app/service
- Location: `packages/services/CxrRuntime/` in AOSP tree
- Package namespace: `org.continuumxr.runtime`

Runtime code ships as a system service in the CXR image.
It is NOT a standalone APK distributed via sideloading.

## Deliverables

### 1. Provider contract (interfaces and data classes)

In `org.continuumxr.runtime.providers`:

- `Provider` — interface with `init(config)`, `start()`, `stop()`, `shutdown()`, `status()`
- `ProviderType` — enum: TIMING, DISPLAY, POSE, TRACKING, INPUT, HAPTICS, OTHER
- `ProviderState` — enum: UNINITIALIZED, INITIALIZING, READY, DEGRADED, FAILED, STOPPED
- `ProviderStatus` — data class matching `docs/providers.md` status contract
- `ProviderConfig` — thin wrapper around `Map<String, Any>`
- `Health` — enum: OK, DEGRADED, ERROR, UNKNOWN
- `Issue` — data class: code, summary, detail, hint, requires, scope, severity
- `IssueCodes` — object with string constants for standard codes

All data classes must be serializable to JSON (kotlinx.serialization).

### 2. Stub providers

Seven stubs, one per capability type:

1. **TimingStub** — state: READY (uses `System.nanoTime()`), warning: STUB_IMPLEMENTATION
2. **DisplayStub** — state: FAILED, blocker: NOT_IMPLEMENTED
3. **PoseHeadStub** — state: FAILED, blocker: NOT_IMPLEMENTED
4. **TrackingWorldStub** — state: FAILED, blocker: NOT_IMPLEMENTED
5. **InputControllersStub** — state: FAILED, blocker: NOT_IMPLEMENTED
6. **InputHandsStub** — state: FAILED, blocker: NOT_IMPLEMENTED
7. **HapticsStub** — state: FAILED, blocker: NOT_IMPLEMENTED

Each stub:
- Implements `Provider` interface
- Has `provider_id` matching profile.json naming (e.g. `timing.stub`)
- Transitions states correctly through lifecycle
- Returns truthful status at every point
- Tolerates repeated stop/shutdown calls

### 3. Profile loader

In `org.continuumxr.runtime.profiles`:

- `Profile` — data classes for profile format (matching `docs/profiles.md`)
- `ProfileLoader` — loads profile JSON, validates, returns `Result<Profile, List<Issue>>`
- `ProviderRegistry` — maps provider_id strings to Provider constructors

Validation (from `docs/profiles.md`):
- Required fields exist
- Capability keys are known (unknown → warning, not failure)
- Provider references resolve
- No duplicate provider IDs
- Required capabilities are explicit

### 4. Runtime orchestrator

In `org.continuumxr.runtime`:

- `Runtime` — top-level orchestrator
- `RuntimeState` — enum: STARTING, RUNNING, DEGRADED, FAILED, STOPPING
- `RuntimeStatus` — aggregate status matching `docs/capability-status-schema.md`
- `CapabilityStatus` — per-capability status block
- `ProviderOrchestrator` — dependency-ordered init/start/stop

State derivation:
- RUNNING if all required capabilities have READY providers
- DEGRADED if non-critical providers are degraded/failed
- FAILED if any critical provider is FAILED or profile load fails

### 5. CXR Runtime Service

Android foreground service (`CxrRuntimeService`):
- Starts at boot (or on shell launch)
- Loads profile from system partition
- Runs orchestrator
- Exposes status via bound service interface
- Logs status JSON to logcat (tag: `CXR`)

### 6. Shell integration

CXR Shell (from Phase 2) gains:
- A status panel showing runtime state
- Per-provider status display
- Blocking issues listed with hints
- Runtime version and profile identity

### 7. Profile validator tool

Standalone Python script in `tools/validate-profile.py`:
- Validates profile JSON against schema
- Runs without Android (for CI and local dev)
- Exits 0 if valid, 1 if errors

## Correctness note

The example stub profile marks `pose.head` as required and assigns `pose.head.stub`,
which reports FAILED/NOT_IMPLEMENTED. Therefore the runtime state with the stub
profile will be FAILED. This is correct behavior — the system is honestly reporting
that a required capability is unavailable. The first time you see
`{"state":"failed"}` in logcat, the architecture is working as designed.

## Testing

### Unit tests
- Provider lifecycle: state transitions, status truthfulness
- Profile loader: valid/invalid profiles, edge cases
- Runtime state derivation: correct aggregation
- Issue model: serialization round-trips

### Integration tests
- Full boot with stub profile on emulator
- Status JSON matches schema
- Shell displays runtime status correctly

### CI
- Profile validator runs against all `profiles/` entries
- Kotlin tests run via AOSP build system or Gradle
- Lint checks

## Definition of done

Phase 3 is complete when:

1. Runtime service starts inside the CXR system image
2. Loads example stub profile
3. Initializes all seven stub providers in dependency order
4. Derives aggregate state correctly (FAILED for stub profile)
5. Status JSON in logcat matches `docs/capability-status-schema.md`
6. CXR Shell displays runtime status
7. Profile validator passes on all committed profiles
8. Unit and integration tests pass

## What Phase 3 does NOT include

- OpenXR runtime exposure (Phase 4)
- Real tracking or rendering (Phase 4+)
- Hardware access (Phase 4+)
- Running on a headset (Phase 4+)
