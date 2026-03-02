# Configuration of Android Environment

## Overview

Setting up the Android development environment involves installing Android Studio, configuring the SDK, creating virtual devices, and understanding Gradle build system. Proper configuration ensures smooth workflow from coding to testing.

## Key Points

- **System Requirements**: 64-bit OS, minimum 4GB RAM (8GB recommended), 4GB+ disk space
- **JDK Installation**: Java Development Kit bundled with Android Studio (Embedded JDK)
- **SDK Manager Configuration**: Install SDK Platforms (API levels), Build Tools, Platform Tools, and System Images
- **AVD Creation**: Configure virtual devices with device definition, system image, and custom settings
- **Gradle Build System**: Automates compilation, dependency management, and APK packaging
- **Key Gradle Files**: build.gradle (Project and Module levels) specify SDK versions and dependencies

## Important Concepts

- compileSdkVersion: API version for compilation
- minSdkVersion: Minimum Android version supported
- targetSdkVersion: Tested Android version
- applicationId: Unique app identifier
- Dependencies management in build.gradle

## Notes

- Validate setup by creating "Hello World" project
- SDK Manager at Tools → SDK Manager in Android Studio
- AVD Manager at Tools → AVD Manager for emulator setup
