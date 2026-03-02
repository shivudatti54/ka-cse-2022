# Introduction to Android OS

## Overview

The Android SDK is the foundational toolkit providing all necessary libraries, APIs, debugging tools, emulators, and documentation for Android app development. Understanding SDK components and build processes is essential for Android developers.

## Key Points

- **Android SDK Components**: Platforms (system images), Build Tools (aapt, d8), System Images (emulator), SDK Tools (adb, fastboot)
- **Android Studio**: Official IDE built on IntelliJ IDEA with intelligent code editor, Gradle build system, and unified development environment
- **SDK Manager**: GUI tool to download and update SDK packages, system images, and essential components
- **AVD Manager**: Creates and manages Android Virtual Devices with hardware profiles and system images
- **Android Emulator**: Simulates Android devices for testing with full device capabilities
- **ADB (Android Debug Bridge)**: Command-line tool for device communication with client-server architecture

## Important Concepts

- Build process flow: Source code → javac → d8 compiler → aapt2 → APK signing
- JDK prerequisite for Java/Kotlin compilation
- Common adb commands: devices, install, logcat, shell, push, pull
- Platform-Tools vs SDK Tools vs Build Tools distinctions

## Notes

- Memorize purpose of adb, aapt, and d8 for exams
- Understand build process from .java/.kt files to final .apk
- Know advantages of testing on both emulators and physical devices
