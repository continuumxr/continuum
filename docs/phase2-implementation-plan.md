# Phase 2 Implementation Plan: cxr-bootstrap

This document defines Phase 2 of Continuum XR — the first bootable system image.

## Goal

Build and boot a minimal AOSP-based system image (`cxr-bootstrap`) that:
- Boots into CXR Shell (custom launcher) instead of stock Android
- Establishes OS-level control
- Runs on the Android emulator first, then on target hardware
- Contains no XR runtime, tracking, or 3D rendering (those are Phase 3)

Success criterion: "I flashed a device, it booted directly into Continuum XR,
and I control what happens next."

## AOSP base

- Branch: `android-latest-release` (currently `android16-qpr2-release`)
- Tag: `android-16.0.0_r4` or latest stable
- Initial build target: `aosp_x86_64-userdebug` (emulator)
- ARM build target (later): `aosp_arm64-userdebug` (hardware)

Reasoning: `android-latest-release` is Google's recommended branch as of 2026.
It is stable, receives security patches, and is easier to maintain/rebase than
`aosp-main`. QPR2 source code is published and available.

## Development environment

- Host OS: Ubuntu 22.04 LTS (or 24.04 LTS)
- Storage: ~400GB minimum
- RAM: 64GB recommended (32GB minimum, will be slower)
- Core tools: repo, git, Python 3, JDK (bundled in AOSP)

## Architecture: minimal delta from AOSP

CXR Phase 2 modifies as little of AOSP as possible.

### What we add
- CXR Shell: a system app that replaces the default launcher
- CXR system properties: branding, version, build identity
- Minimal overlay: disable stock launcher, set CXR Shell as default home

### What we do NOT modify
- Framework code
- System services
- Init scripts (unless absolutely necessary)
- Kernel (vendor-owned infrastructure — not CXR's responsibility)
- Recovery/bootloader

### What we remove/disable
- GMS (Google Mobile Services) — not included in AOSP base anyway
- Stock launcher (replaced by CXR Shell)
- Unnecessary default apps where possible
- Telemetry and analytics hooks

## CXR Shell (Phase 2 scope)

The shell is intentionally minimal. It is NOT the final XR UI.

### What it does
- Displays system status (build version, device info, runtime status placeholder)
- Provides basic navigation (back/home/recents behavior preserved)
- Exposes a settings surface for developer options
- Serves as the "home" activity — proof that CXR owns the boot experience

### What it does NOT do
- No 3D rendering
- No spatial UI
- No XR runtime integration
- No app store or app management (beyond what Android provides)

### Implementation
- Standard Android Activity/Fragment app
- Kotlin (aligns with Phase 3 runtime language — see ADR 0002)
- Material Design basics for readability — not final aesthetic
- Lives in `packages/apps/CxrShell/` within the AOSP tree

## Performance targets (Phase 2)

### Boot
- Target: ~20–30 seconds to interactive shell
- Measure: `adb logcat` timestamps from kernel start to shell `onResume()`

### Idle
- Near-zero wakeups when inactive
- No polling-based services
- Measure: `dumpsys batterystats` after 10 minutes idle

### Background
- Only essential services remain after boot settles
- No unnecessary system services running

### Principles
- Event-driven architecture, not polling
- Strict limits on jobs, alarms, wake locks
- Lightweight shell (no heavy animations or startup work)

## Security posture (Phase 2)

- SELinux enforcing from the start (never permissive in release builds)
- `userdebug` builds for development, `user` builds for any public artifacts
- Verified boot: respect existing vbmeta, adjust only as needed for GSI
- No default telemetry or cloud dependencies
- Minimal privileged apps
- GrapheneOS-inspired direction: reduce attack surface, harden over time

## Build integration

### Repository structure
```
continuum/
├── aosp/                    # AOSP source tree (gitignored, not committed)
├── packages/
│   └── apps/
│       └── CxrShell/        # CXR Shell application
├── overlay/
│   └── cxr/                 # Resource overlays (launcher replacement, branding)
├── build/
│   └── cxr_product.mk       # Product makefile for CXR builds
├── vendor/
│   └── cxr/                 # CXR vendor partition additions
├── docs/                    # (existing)
├── profiles/                # (existing)
├── providers/               # (existing, Phase 3)
├── runtime/                 # (existing, Phase 3)
├── tools/                   # (existing)
└── README.md
```

### Build flow
```bash
# 1. Init AOSP
repo init -u https://android.googlesource.com/platform/manifest \
  -b android-latest-release --depth=1

# 2. Sync
repo sync -c --no-clone-bundle --no-tags -j$(nproc)

# 3. Apply CXR overlay
# (symlink or copy CXR packages/overlay/vendor into AOSP tree)

# 4. Build
source build/envsetup.sh
lunch cxr_x86_64-userdebug    # emulator target
m                              # or: m -j$(nproc)

# 5. Run emulator
emulator
```

The `cxr_x86_64` and `cxr_arm64` lunch targets are defined by the CXR product
makefile, which inherits from `aosp_x86_64` / `aosp_arm64` and adds CXR-specific
packages and overlays.

## GSI strategy

CXR Phase 2 should produce a system image that can be flashed via standard
`fastboot` on Treble-compliant devices:

```bash
fastboot flash system cxr-system.img
fastboot flash vbmeta vbmeta.img --disable-verity --disable-verification
fastboot reboot
```

Vendor and kernel partitions remain untouched.
Device-specific capabilities are handled by Continuum Packs (Phase 5).

## What Phase 2 explicitly does NOT include

- OpenXR runtime (Phase 3)
- Head tracking or any tracking (Phase 4+)
- 3D rendering or compositor (Phase 4+)
- Spatial UI (Phase 4+)
- Hand tracking, controller input (Phase 5)
- Device packs (Phase 5)
- Android XR integration (Phase X)
- Linux migration (Phase X)

## Definition of done

Phase 2 is complete when:

1. `cxr_x86_64-userdebug` builds cleanly from AOSP source
2. Emulator boots into CXR Shell (not stock launcher)
3. CXR Shell displays system identity (build version, "Continuum XR")
4. Back/home/recents navigation works
5. Boot time is under 30 seconds to interactive shell
6. SELinux is enforcing
7. No Google services or telemetry present
8. Build is reproducible from documented steps
9. `cxr_arm64-userdebug` also builds (hardware flash testing follows)

## Phase 3 bridge

Once Phase 2 is complete, Phase 3 (runtime scaffolding) builds on top of it:
- The CXR runtime service runs inside the CXR system image
- CXR Shell integrates runtime status display
- Provider interfaces and stubs are tested on the booted system
- Profile loading and diagnostics work end-to-end

See `phase3-runtime-implementation-plan.md` for details.
