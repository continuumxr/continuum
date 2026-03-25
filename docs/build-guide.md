# CXR Build Guide

Step-by-step instructions for building the CXR system image from source.

## Prerequisites

### Host OS
Ubuntu 22.04 LTS (recommended) or 24.04 LTS.
WSL2 on Windows is supported.

### Hardware
- Storage: 400GB+ available (AOSP source + build artifacts)
- RAM: 64GB recommended (32GB minimum, builds will be slower)
- CPU: modern multi-core (build parallelism scales with cores)

### Required packages

```bash
sudo apt-get update
sudo apt-get install -y git-core gnupg flex bison build-essential \
  zip curl zlib1g-dev libc6-dev-i386 x11proto-core-dev \
  libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils \
  xsltproc unzip fontconfig python3 python3-pip openjdk-21-jdk
```

## Step 1: Install repo tool

```bash
mkdir -p ~/.bin
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
chmod a+x ~/.bin/repo
export PATH=~/.bin:$PATH
```

Add `export PATH=~/.bin:$PATH` to your shell profile (`~/.bashrc` or `~/.zshrc`).

## Step 2: Initialize and sync AOSP

```bash
mkdir -p ~/cxr/aosp && cd ~/cxr/aosp

repo init -u https://android.googlesource.com/platform/manifest \
  -b android-latest-release --depth=1

# This takes several hours — run overnight
repo sync -c --no-clone-bundle --no-tags -j$(nproc)
```

## Step 3: Verify vanilla AOSP builds

Before adding CXR customizations, verify the base builds:

```bash
cd ~/cxr/aosp
source build/envsetup.sh
lunch aosp_x86_64-userdebug
m -j$(nproc)
emulator
```

Verify stock Android boots in the emulator. Do NOT proceed until this succeeds.

## Step 4: Add CXR files to AOSP tree

Copy CXR device definitions and apps from the continuum repo into the AOSP tree:

```bash
# Adjust paths as needed
CXR_REPO=~/continuum

cp -r $CXR_REPO/device/cxr/ ~/cxr/aosp/device/cxr/
cp -r $CXR_REPO/packages/apps/CxrShell/ ~/cxr/aosp/packages/apps/CxrShell/
```

## Step 5: Build CXR image (x86_64 emulator)

```bash
cd ~/cxr/aosp
source build/envsetup.sh
lunch cxr_x86_64-userdebug
m -j$(nproc)
```

## Step 6: Boot CXR in emulator

```bash
emulator
```

### Verify
- Emulator boots
- CXR Shell is the home screen (not stock Android launcher)
- "Continuum XR" and version string are visible
- Back/home/recents buttons work
- `adb shell getprop ro.cxr.version` returns `0.1.0-dev`
- `adb shell getenforce` returns `Enforcing`

## Step 7: Build ARM target (optional)

```bash
source build/envsetup.sh
lunch cxr_arm64-userdebug
m -j$(nproc)
```

Note: ARM emulator is slower. Hardware testing comes in Phase 5.

## Troubleshooting

### Build fails with Java errors
AOSP bundles its own JDK. Ensure you are not overriding `JAVA_HOME` to point
at a system JDK that is incompatible. Unset it and let AOSP use its prebuilt:
```bash
unset JAVA_HOME
```

### Out of disk space
AOSP source is ~100GB, build artifacts can reach 200GB+. Ensure 400GB+ free.

### WSL2 memory limits
By default WSL2 may limit RAM. Create or edit `%USERPROFILE%\.wslconfig`:
```ini
[wsl2]
memory=48GB
swap=16GB
```
Then restart WSL: `wsl --shutdown`

### lunch target not found
Verify `device/cxr/cxr_x86_64/AndroidProducts.mk` exists in the AOSP tree
and contains `COMMON_LUNCH_CHOICES`.
