# Privacy Architecture

This document defines how Continuum XR (CXR) enforces privacy as a system-level
property — not a policy, not a preference, not a checkbox, but an architectural
constraint that is difficult to violate even by mistake.

## Why XR privacy is different

An XR headset is the most intimate computing device ever built. It has:

- Cameras pointed at your living room, your family, your workspace
- Eye trackers that can infer health conditions, cognitive state, sexual orientation,
  and emotional responses
- Hand trackers that observe your gestures, your body language, your physical habits
- Microphones that hear your conversations
- Depth sensors that map the geometry of your private spaces
- IMUs that track your head movement, posture, and physical activity patterns
- The ability to combine all of this data to build an extraordinarily detailed
  profile of who you are, how you behave, and where you live

Every major XR platform today collects some or all of this data and sends it to
the vendor's cloud. Meta's Horizon OS collects spatial data for their mapping
services. Apple's visionOS is better but still opaque about what leaves the device.
Google's Android XR is deeply integrated with Gemini, a cloud AI service.
ByteDance's Pico OS operates under Chinese national security laws that can compel
data sharing.

CXR takes the position that none of this data should leave the device unless the
user explicitly, knowingly, and specifically authorizes it — and even then, the
system should make it easy to say no and hard to accidentally say yes.

## Core privacy principles

### 1. All sensor data is local by default

No sensor data — cameras, eye tracker, hand tracker, microphone, depth sensor,
IMU — leaves the device under any circumstance unless the user explicitly authorizes
a specific data flow to a specific destination for a specific purpose.

This is not a setting. It is the default behavior of the system with no override
at the OS level. There is no "master telemetry switch" because there is no
telemetry to switch on.

### 2. No network required

CXR boots and functions fully without an internet connection. There is no
activation, no account requirement, no license check, no "first-time setup"
that phones home.

The system is complete on the device. Network access is a user choice, not a
system requirement.

### 3. Apps request specific data, not broad categories

Android's permission model is "allow camera access" — a single binary gate for
an entire sensor class. This is insufficient for XR.

CXR's permission model is granular and purpose-specific:

- An app does not request "hand tracking." It requests "hand skeleton joint
  positions at 30Hz for gesture input." The system provides joint positions.
  The app never sees the raw camera feed that produced them.

- An app does not request "eye tracking." It requests "gaze direction vector
  for UI interaction." The system provides the gaze vector. The app never sees
  pupil dilation, saccade patterns, fixation duration, or any other eye movement
  data that could be used for biometric inference.

- An app does not request "passthrough camera." It requests "depth-aware
  environment mesh for surface detection." The system provides the mesh.
  The app never sees the raw camera image.

The principle: apps receive the minimum processed output needed for their
stated purpose, never raw sensor streams.

### 4. Inference is not access

Even when an app has permission to use a sensor capability, the system actively
prevents inference attacks where possible:

- Eye tracking data exposed to apps is stripped of timing information that
  could be used for biometric identification or cognitive state inference.
  Apps receive gaze direction. They do not receive saccade velocity, fixation
  duration, pupil dilation, or microsaccade patterns.

- Hand tracking data exposed to apps is joint positions only. Tremor data,
  grip force estimation, and fine motor patterns are not exposed unless
  explicitly authorized for a medical or accessibility purpose.

- Spatial mapping data exposed to apps is geometric only. Texture data,
  object recognition results, and semantic labels (which could reveal what
  objects are in your room) are available only through explicit additional
  permissions.

### 5. The user can audit everything

CXR maintains a local, on-device audit log of all sensor data access:

- Which app accessed which sensor capability
- When, for how long, at what data rate
- Whether data was transmitted over the network (and to where, if detectable)

This log is:
- Stored locally, never transmitted
- Accessible to the user through a first-party privacy dashboard
- Presented in plain language, not technical jargon
- Retained for a configurable period (default: 30 days)

The user can review this log at any time and revoke permissions based on
what they see.

### 6. Bystander protection

XR headsets observe people who did not consent to being observed. CXR
addresses this at the system level:

- Passthrough camera data used for environment mapping automatically
  processes out human figures before any data is stored or exposed to apps.
  The spatial mesh contains walls, floors, furniture — not people.

- If an app requests camera-level access (rare, explicitly flagged as
  high-privilege), the system displays a persistent, undismissable indicator
  that the camera feed is active. This indicator is rendered by the compositor,
  not the app, and cannot be hidden or obscured.

- No face recognition, person identification, or biometric data about
  bystanders is ever computed, stored, or made available to apps.

### 7. Spatial data stays on device

Room maps, spatial anchors, scene understanding meshes, and environment
reconstruction data are stored locally in encrypted userland storage.

This data is never:
- Uploaded to a cloud service
- Shared between users without explicit action
- Accessible to apps in its raw form (apps receive processed surfaces, not
  full room reconstructions)
- Retained after the user deletes it (deletion is immediate and complete)

The user can view, export, and delete their spatial data at any time through
the privacy dashboard.

### 8. No data collection for "improvement"

CXR does not collect usage data, crash reports, analytics, performance metrics,
or any other telemetry for the purpose of "improving the product."

If the user voluntarily chooses to submit a bug report, the system clearly shows
exactly what data will be included and requires explicit confirmation before
sending.

## Technical implementation

### Sensor access architecture

```
App (userland)
    │
    ▼
Permission Gate (per-capability, per-purpose)
    │
    ▼
Data Reduction Layer
(strips raw data to minimum needed for stated purpose)
    │
    ▼
Provider (runtime)
(produces raw sensor data internally)
    │
    ▼
Hardware Sensor
```

The Data Reduction Layer is the critical privacy enforcement point. It sits
between the provider (which has full access to raw sensor data for its own
processing) and the app-facing API (which exposes only reduced, purpose-specific
data).

This layer is part of the runtime, not part of the app. Apps cannot bypass it.

### Permission model

Permissions in CXR are structured as:

```
{
  "capability": "input.hands",
  "purpose": "gesture_input",
  "data_exposed": ["joint_positions"],
  "data_rate": "30hz",
  "data_withheld": ["raw_camera", "tremor", "grip_force"],
  "duration": "while_app_active",
  "network_allowed": false
}
```

Each permission request is:
- Specific (what data, at what rate, for what purpose)
- Transparent (what is withheld is stated explicitly)
- Scoped (duration and network access are part of the grant)
- Revocable (user can revoke at any time, app must handle gracefully)

### Privilege tiers

Not all sensor access is equal. CXR defines three privilege tiers:

**Tier 1 — Processed output (default)**
Apps receive processed results: gaze direction, joint positions, surface
meshes. No raw sensor data. No timing data that enables inference attacks.
Most apps should only need Tier 1.

**Tier 2 — Extended access (explicit consent)**
Apps receive richer data: semantic scene labels, detailed hand pose with
confidence scores, eye tracking with fixation data. Requires explicit
per-session consent with clear explanation of what additional data is exposed
and why.

**Tier 3 — Raw sensor access (high-privilege, persistent indicator)**
Apps receive raw camera feeds, raw depth data, or raw eye tracking streams.
Reserved for development tools, accessibility applications, and research.
Requires:
- Explicit opt-in with full-screen confirmation dialog
- Persistent, compositor-rendered indicator visible at all times
- Automatic timeout (configurable, default: 1 hour)
- Entry in audit log with elevated visibility

### Encryption

- All stored sensor data (spatial maps, calibration, audit logs) is encrypted
  at rest using device-bound keys.
- The encryption key is derived from user credentials or device hardware,
  not from a remote service.
- If the user performs a factory reset, all sensor data is destroyed.

### App sandboxing

CXR inherits Android's app sandbox model and extends it for XR:

- No app can access another app's sensor permission grants.
- No app can observe which other apps have sensor access.
- Sensor data passed to an app is isolated to that app's memory space.
- An app that has been denied a permission cannot infer whether the capability
  exists on the hardware (the denial looks the same as "capability not present").

## What CXR will never do

- Sell or monetize user sensor data in any form.
- Require an account or login to use the device.
- Collect telemetry or analytics without explicit, per-instance user consent.
- Expose raw eye tracking data to apps by default.
- Build or maintain a cloud-based spatial map from user data.
- Enable remote access to device sensors without the user's knowledge.
- Weaken privacy protections via OTA update without clear changelog disclosure.

## Relationship to other documents

- `docs/architecture.md` — the provider model and runtime design
- `docs/providers.md` — provider contracts (sensor data flows through providers)
- `docs/capability-status-schema.md` — how capabilities are reported
  (privacy metadata should be part of capability status in later phases)

## Implementation phasing

Phase 2–3: Privacy principles are established in documentation and architecture.
No sensor data is accessed (stubs only).

Phase 4: Permission gate and data reduction layer designed alongside the first
real providers (head pose, display). Audit log schema defined.

Phase 5: Full permission model implemented for tracking, hand, and controller
providers. Privacy dashboard integrated into CXR Shell. Bystander protection
implemented in passthrough provider.

Phase X: Formal privacy audit. External review of data flows.
Potential compliance documentation (GDPR, CCPA) for users who need it.
