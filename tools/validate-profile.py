#!/usr/bin/env python3
"""Validate CXR device profile JSON files.

Usage: python3 validate-profile.py <profile.json> [profile2.json ...]

Exits 0 if all profiles are valid, 1 if any have errors.
"""

import json
import sys

KNOWN_CAPABILITY_KEYS = {
    "timing",
    "display",
    "pose.head",
    "tracking.world",
    "input.controllers",
    "input.hands",
    "haptics",
}

KNOWN_PROVIDER_TYPES = {
    "timing",
    "display",
    "pose",
    "tracking",
    "input",
    "haptics",
    "other",
}

REQUIRED_TOP_LEVEL = {"profile_id", "display_name", "device", "capabilities", "providers"}
REQUIRED_CAPABILITY = {"required", "provider"}
REQUIRED_PROVIDER = {"provider_id", "provider_type", "capabilities"}


def validate_profile(path):
    errors = []
    warnings = []

    try:
        with open(path, "r", encoding="utf-8") as f:
            profile = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"], []
    except FileNotFoundError:
        return [f"File not found: {path}"], []

    if not isinstance(profile, dict):
        return ["Profile must be a JSON object"], []

    # Check required top-level fields
    for field in REQUIRED_TOP_LEVEL:
        if field not in profile:
            errors.append(f"Missing required field: {field}")

    # Validate capabilities
    capabilities = profile.get("capabilities", {})
    if not isinstance(capabilities, dict):
        errors.append("'capabilities' must be an object")
        capabilities = {}

    for key, cap in capabilities.items():
        if key not in KNOWN_CAPABILITY_KEYS:
            warnings.append(f"Unknown capability key: {key}")

        if not isinstance(cap, dict):
            errors.append(f"Capability '{key}' must be an object")
            continue

        for field in REQUIRED_CAPABILITY:
            if field not in cap:
                errors.append(f"Capability '{key}' missing required field: {field}")

        if "required" in cap and not isinstance(cap["required"], bool):
            errors.append(f"Capability '{key}.required' must be boolean")

    # Validate providers
    providers = profile.get("providers", [])
    if not isinstance(providers, list):
        errors.append("'providers' must be an array")
        providers = []

    provider_ids = set()
    for i, prov in enumerate(providers):
        if not isinstance(prov, dict):
            errors.append(f"Provider [{i}] must be an object")
            continue

        for field in REQUIRED_PROVIDER:
            if field not in prov:
                errors.append(f"Provider [{i}] missing required field: {field}")

        pid = prov.get("provider_id", "")
        if pid in provider_ids:
            errors.append(f"Duplicate provider_id: {pid}")
        provider_ids.add(pid)

        ptype = prov.get("provider_type", "")
        if ptype and ptype not in KNOWN_PROVIDER_TYPES:
            warnings.append(f"Provider '{pid}' has unknown type: {ptype}")

        pcaps = prov.get("capabilities", [])
        if not isinstance(pcaps, list):
            errors.append(f"Provider '{pid}'.capabilities must be an array")

    # Cross-reference: capability providers must exist
    for key, cap in capabilities.items():
        provider_ref = cap.get("provider")
        if provider_ref and provider_ref not in provider_ids:
            errors.append(
                f"Capability '{key}' references provider '{provider_ref}' "
                f"which is not in providers list"
            )

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: validate-profile.py <profile.json> [...]", file=sys.stderr)
        sys.exit(1)

    any_errors = False

    for path in sys.argv[1:]:
        errors, warnings = validate_profile(path)

        print(f"\n{'=' * 60}")
        print(f"Profile: {path}")
        print(f"{'=' * 60}")

        if warnings:
            for w in warnings:
                print(f"  WARNING: {w}")

        if errors:
            any_errors = True
            for e in errors:
                print(f"  ERROR: {e}")
            print(f"  RESULT: INVALID ({len(errors)} error(s))")
        else:
            print(f"  RESULT: VALID")

    sys.exit(1 if any_errors else 0)


if __name__ == "__main__":
    main()
