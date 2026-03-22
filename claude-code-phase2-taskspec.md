# Claude Code Task Spec: CXR Phase 2 — cxr-bootstrap

## Context

You are working on Continuum XR (CXR), an open-source, privacy-first XR operating
system. The repo is at https://github.com/ender9492/continuum

Phase 2 goal: build a bootable AOSP-based system image that boots into CXR Shell
instead of stock Android launcher.

Read these docs before writing any code:
- docs/vision.md
- docs/architecture.md
- docs/phase2-implementation-plan.md

## Principles (non-negotiable)

- Minimal delta from AOSP. Do not modify framework code unless absolutely necessary.
- SELinux enforcing. Never set permissive.
- No GMS, no telemetry, no cloud dependencies.
- Kotlin for CXR Shell.
- Reproducible builds from documented steps.
- 2-space indent, UTF-8, LF line endings (see .editorconfig).

## Environment setup

Host: Ubuntu 22.04 LTS
Storage: 400GB+ available
RAM: 64GB recommended

Required packages (install before starting):
```bash
sudo apt-get install -y git-core gnupg flex bison build-essential \
  zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev \
  libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils \
  xsltproc unzip fontconfig python3 python3-pip openjdk-21-jdk
```

## Task sequence

### Task 1: AOSP source setup

```bash
mkdir -p ~/cxr/aosp && cd ~/cxr/aosp

# Install repo tool
mkdir -p ~/.bin
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
chmod a+x ~/.bin/repo
export PATH=~/.bin:$PATH

# Init AOSP
repo init -u https://android.googlesource.com/platform/manifest \
  -b android-latest-release --depth=1

# Sync (this takes hours — run overnight)
repo sync -c --no-clone-bundle --no-tags -j$(nproc)
```

Verify: `source build/envsetup.sh && lunch aosp_x86_64-userdebug` succeeds.

### Task 2: Vanilla AOSP build verification

Before adding any CXR customization, verify the base builds and boots:

```bash
source build/envsetup.sh
lunch aosp_x86_64-userdebug
m -j$(nproc)
emulator
```

Verify: stock Android boots in emulator. This confirms the build environment works.
Do NOT proceed until this succeeds.

### Task 3: CXR product definition

Create the CXR product makefile that inherits from `aosp_x86_64` and adds
CXR-specific configuration.

Files to create (relative to AOSP root):

`device/cxr/cxr_x86_64/AndroidProducts.mk`:
```makefile
PRODUCT_MAKEFILES := \
    $(LOCAL_DIR)/cxr_x86_64.mk

COMMON_LUNCH_CHOICES := \
    cxr_x86_64-userdebug \
    cxr_x86_64-eng
```

`device/cxr/cxr_x86_64/cxr_x86_64.mk`:
```makefile
$(call inherit-product, $(SRC_TARGET_DIR)/product/aosp_x86_64.mk)

PRODUCT_NAME := cxr_x86_64
PRODUCT_DEVICE := generic_x86_64
PRODUCT_BRAND := ContinuumXR
PRODUCT_MODEL := CXR Emulator (x86_64)
PRODUCT_MANUFACTURER := ContinuumXR

# CXR Shell
PRODUCT_PACKAGES += CxrShell

# Remove stock launcher if needed
PRODUCT_PACKAGES += \
    -Launcher3

# System properties
PRODUCT_SYSTEM_PROPERTIES += \
    ro.cxr.version=0.1.0-dev \
    ro.cxr.build_phase=2
```

Verify: `lunch cxr_x86_64-userdebug` appears in lunch menu and succeeds.

### Task 4: CXR Shell (minimal launcher)

Create a minimal Android application that:
- Is a HOME activity (launcher replacement)
- Displays "Continuum XR" with build version
- Shows basic device info (model, Android version, CXR version)
- Has a placeholder for runtime status (Phase 3)
- Responds to back/home/recents correctly

Location: `packages/apps/CxrShell/`

Structure:
```
packages/apps/CxrShell/
├── Android.bp                    # Build definition (Soong)
├── AndroidManifest.xml
├── res/
│   ├── layout/
│   │   └── activity_main.xml
│   ├── values/
│   │   ├── strings.xml
│   │   └── themes.xml
│   └── drawable/                 # Minimal icon
└── src/org/continuumxr/shell/
    └── CxrShellActivity.kt
```

Key AndroidManifest.xml requirements:
```xml
<activity android:name=".CxrShellActivity"
    android:exported="true"
    android:launchMode="singleTask"
    android:stateNotNeeded="true">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.HOME" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

Use Soong (Android.bp) build system, NOT Gradle, since this is a system app
built as part of the AOSP image.

Verify: builds as part of `m`, appears in the system image, launches as home.

### Task 5: Build and boot CXR image

```bash
source build/envsetup.sh
lunch cxr_x86_64-userdebug
m -j$(nproc)
emulator
```

Verify:
- Emulator boots
- CXR Shell is the home screen (not stock Android launcher)
- "Continuum XR" and version string are visible
- Back/home/recents buttons work
- `adb shell getprop ro.cxr.version` returns `0.1.0-dev`

### Task 6: Performance validation

After boot, measure:

```bash
# Boot time
adb logcat -d | grep -E "boot_progress|CxrShell"

# Idle wakeups (wait 10 minutes, then)
adb shell dumpsys batterystats

# SELinux status
adb shell getenforce  # Must return "Enforcing"

# Running services
adb shell dumpsys activity services | grep -c "ServiceRecord"
```

Document results in `docs/phase2-results.md`.

### Task 7: ARM build target

Create the ARM variant:

`device/cxr/cxr_arm64/AndroidProducts.mk` and `cxr_arm64.mk`
(same pattern as x86_64 but inheriting from `aosp_arm64`).

Verify: `lunch cxr_arm64-userdebug && m` completes.
Note: ARM emulator is slower. Hardware testing comes in Phase 5.

### Task 8: Documentation and CI

- Update `README.md` with build instructions
- Create `docs/phase2-results.md` with boot time and performance data
- Create `docs/build-guide.md` with step-by-step environment setup
- Add `.github/workflows/ci.yml`:
  - Profile validation (Python)
  - Lint checks for CXR Shell code
  - (Full AOSP build is too heavy for CI — document manual build verification)

## Definition of done

All eight tasks complete:
- `lunch cxr_x86_64-userdebug && m` builds cleanly
- Emulator boots into CXR Shell
- SELinux enforcing
- No GMS present
- ARM target builds
- Build steps documented
- Performance baseline documented

## What NOT to do

- Do not modify AOSP framework code.
- Do not add an XR runtime. That is Phase 3.
- Do not add 3D rendering, tracking, or OpenXR. That is Phase 4+.
- Do not add Rust, C++, or NDK code. Phase 2 is Kotlin only.
- Do not add a custom kernel. CXR uses vendor kernels.
- Do not add Google services or any cloud dependency.
- Do not optimize the shell UI. Functional correctness only.
- Do not add features not described in this spec.
