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
