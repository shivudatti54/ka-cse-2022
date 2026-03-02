# Android Architecture

## Overview

Android is built on a layered software stack architecture. Each layer provides services to the layer above it and uses services from the layer below. This modular design allows hardware manufacturers, app developers, and Google to work on different layers independently.

## Android Architecture Stack

The Android platform consists of five main layers (from bottom to top):

```
+-----------------------------------------------+
| System Apps |
| (Phone, Contacts, Browser, Camera, etc.) |
+-----------------------------------------------+
| Application Framework |
| (Activity Manager, Window Manager, |
| Content Providers, View System, etc.) |
+-----------------------------------------------+
| Native C/C++ | Android Runtime |
| Libraries | (ART) |
| (WebKit, OpenGL, | - Core Libraries |
| SQLite, Media, etc)| - AOT/JIT Compilation |
+-----------------------------------------------+
| Hardware Abstraction Layer (HAL) |
| (Camera, Bluetooth, Audio, Sensors, etc.) |
+-----------------------------------------------+
| Linux Kernel |
| (Drivers, Power Mgmt, Memory Mgmt, |
| Process Mgmt, Networking, Security) |
+-----------------------------------------------+
```

## Layer 1: Linux Kernel

The Linux Kernel forms the foundation of the Android platform. Android uses a modified version of the Linux kernel.

### Key Functions

- **Hardware Drivers**: Provides drivers for display, camera, Bluetooth, audio, USB, Wi-Fi, and other hardware components
- **Process Management**: Handles process creation, scheduling, and inter-process communication
- **Memory Management**: Manages virtual memory, paging, and memory allocation
- **Power Management**: Controls device power states, battery management, and wake locks
- **Security**: Provides user-based permissions model, process isolation, and secure IPC
- **Networking**: Implements TCP/IP stack and network protocols

### Why Linux?

- Open source and well-tested
- Built-in security model (user-based permissions)
- Proven driver model for hardware abstraction
- Support for shared libraries and memory management
- Pre-emptive multitasking and multi-threading support

## Layer 2: Hardware Abstraction Layer (HAL)

The HAL provides standard interfaces that expose device hardware capabilities to the higher-level Java API framework. It consists of multiple library modules, each implementing an interface for a specific type of hardware component.

### HAL Modules

| Module        | Purpose                         |
| ------------- | ------------------------------- |
| Camera HAL    | Interface to camera hardware    |
| Audio HAL     | Interface to audio hardware     |
| Bluetooth HAL | Interface to Bluetooth hardware |
| Sensors HAL   | Interface to device sensors     |
| Graphics HAL  | Interface to GPU                |

### How HAL Works

```
Application Framework
 |
 v
 HAL Interface (standard API)
 |
 v
 HAL Module (vendor implementation)
 |
 v
 Hardware Driver (Linux Kernel)
 |
 v
 Physical Hardware
```

When a framework API makes a call to access device hardware, the Android system loads the appropriate HAL library module for that hardware component. The HAL module contains vendor-specific code to interact with the actual hardware through the kernel drivers.

## Layer 3: Android Runtime (ART)

The Android Runtime replaced the older Dalvik Virtual Machine (DVM) starting with Android 5.0 (Lollipop).

### ART Features

- **Ahead-of-Time (AOT) Compilation**: Converts bytecode to native machine code at install time, improving runtime performance
- **Just-in-Time (JIT) Compilation**: Added in Android 7.0, compiles frequently used code at runtime for faster app installation
- **Improved Garbage Collection**: Reduces pauses and memory overhead compared to Dalvik
- **Better Debugging Support**: Enhanced diagnostics and crash reporting

### ART vs Dalvik Comparison

| Feature            | ART                        | Dalvik                    |
| ------------------ | -------------------------- | ------------------------- |
| Compilation        | AOT + JIT                  | JIT only                  |
| App Startup        | Faster                     | Slower                    |
| Install Time       | Slightly longer            | Faster                    |
| Storage            | More (compiled code)       | Less                      |
| Battery Life       | Better (less runtime work) | Worse (more runtime work) |
| Garbage Collection | Concurrent, compacting     | Stop-the-world            |

### Native C/C++ Libraries

Android includes a set of native libraries written in C and C++ that provide core functionality:

- **WebKit/Chromium**: Web browser engine
- **OpenGL ES**: 2D and 3D graphics rendering
- **SQLite**: Lightweight relational database
- **Media Framework**: Audio and video codec support (MPEG4, H.264, MP3, AAC, etc.)
- **libc (Bionic)**: Standard C library optimized for Android
- **SSL**: Secure network communication
- **SGL**: 2D graphics engine
- **FreeType**: Font rendering

## Layer 4: Application Framework

The Application Framework provides high-level building blocks (APIs) that developers use to build Android applications. These are exposed as Java/Kotlin APIs.

### Key Framework Services

| Manager/Service          | Purpose                                       |
| ------------------------ | --------------------------------------------- |
| **Activity Manager**     | Manages Activity lifecycle and back stack     |
| **Window Manager**       | Manages windows and their display on screen   |
| **Content Providers**    | Manages shared data access between apps       |
| **View System**          | UI components (buttons, lists, text fields)   |
| **Package Manager**      | Manages installed apps and their components   |
| **Telephony Manager**    | Manages phone call and cellular functionality |
| **Resource Manager**     | Manages non-code resources (strings, layouts) |
| **Location Manager**     | Manages GPS and location services             |
| **Notification Manager** | Manages status bar notifications              |

### How Framework Services Work

When an app calls `getSystemService(Context.LOCATION_SERVICE)`, the framework returns a LocationManager object that communicates with the location service running in the system process. The service uses HAL to access GPS hardware through the kernel driver.

## Layer 5: System Apps and Applications

The top layer consists of both system apps and user-installed applications.

### System Apps

- Pre-installed apps (Phone, Contacts, Messages, Camera, Browser)
- Can be used by other apps through the framework
- Example: An app can use the Camera system app to capture photos via an Intent

### User Applications

- Installed from Google Play Store or sideloaded
- Built using the Application Framework APIs
- Run in their own sandbox with isolated processes
- Each app gets a unique Linux user ID for security

## Data Flow Example

When a user takes a photo:

```
1. User taps "Capture" in Camera App (Application Layer)
2. App calls CameraManager.openCamera() (Application Framework)
3. Framework calls Camera HAL interface (HAL Layer)
4. HAL module calls camera kernel driver (Linux Kernel)
5. Driver communicates with camera hardware (Hardware)
6. Image data flows back up through layers
7. Image displayed using Surface/View System
```

## Summary

- Android architecture has five main layers: Linux Kernel, HAL, ART + Native Libraries, Application Framework, and Applications
- The Linux Kernel provides hardware abstraction, security, and process management
- HAL provides standard interfaces between framework and hardware drivers
- ART compiles app bytecode to native code for better performance
- The Application Framework provides Java/Kotlin APIs for app development
- System apps and user apps sit at the top of the stack
