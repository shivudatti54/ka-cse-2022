# Android Ecosystem, Versions, Activities, Features, and Architecture Stack

## 1. Introduction

Android, developed by Open Handset Alliance (led by Google), is the world's most widely adopted mobile operating system. Built upon the Linux kernel, Android provides a robust, scalable platform for mobile application development. This study material examines the fundamental components of the Android ecosystem, including its version history, core components such as Activities, platform features, and the layered architecture stack that enables developers to create feature-rich mobile applications.

## 2. Android Ecosystem

The Android ecosystem constitutes a comprehensive framework encompassing hardware manufacturers, software developers, end-users, and cloud-based services. This interconnected environment includes:

- **Hardware Layer**: smartphones, tablets, wearable devices, smart TVs, and in-vehicle infotainment systems from various manufacturers
- **Software Stack**: Android Open Source Project (AOSP) OS, framework APIs, and native libraries
- **Service Framework**: Google Play Services, Google Play Store, Cloud Messaging, and location services
- **Developer Ecosystem**: Android Studio IDE, SDK tools, documentation, and community support

The ecosystem operates on an open-source model, enabling manufacturers to customize the OS while maintaining compatibility through the Android Compatibility Program.

## 3. Android Versions and API Levels

Android versioning follows a dual identification system: version numbers (e.g., Android 14) and code names (historically desserts). More critically, API levels provide a numerical identifier for the framework API revision.

### API Level Significance

API levels are integers incrementally assigned to each Android platform release, enabling developers to specify minimum and target compatibility:

- **minSdkVersion**: Defines the minimum Android version the application supports
- **targetSdkVersion**: Indicates the API level for which the application was designed
- **compileSdkVersion**: Specifies the SDK platform used during compilation

### Version History and Support

Android releases major versions annually, with security patches distributed monthly. Each version introduces platform features, API additions, and behavioral changes. The Android platform follows a deprecation lifecycle, where older APIs are deprecated but remain functional for backward compatibility.

## 4. Android Activity Component

An Activity represents a single user interface screen and serves as the fundamental building block of Android application UI. The Activity class extends ContextThemeWrapper and implements the component lifecycle defined by the Android Activity Manager.

### Activity Lifecycle

The Activity lifecycle comprises callback methods that manage the component's state transitions:

1. **onCreate()**: Called when Activity is first instantiated; initializes UI and critical data
2. **onStart()**: Activity becomes visible to user
3. **onResume()**: Activity gains user focus and becomes interactive
4. **onPause()**: User leaving Activity; indicates focus loss
5. **onStop()**: Activity no longer visible; resources may be released
6. **onDestroy()**: Activity termination; final cleanup operations

### Intents and Activation

Activities are activated through Intent objects, which can be explicit (specifying target component) or implicit (declaring action and data type). The Intent resolution process matches against registered IntentFilters in the Android Package Manager to determine appropriate target components.

### Window Modes and Configuration

Activities support various window modes including standard, singleInstance, singleTask, and singleTop, affecting task and back stack behavior. Configuration changes (orientation, keyboard availability) trigger Activity recreation by default, though this behavior can be customized through configChanges attributes.

## 5. Features of Android Platform

Android provides extensive platform features enabling sophisticated application development:

- **Multi-touch Input System**: Supports gesture detection including pinch-to-zoom, pan, swipe, and rotation through the MotionEvent class
- **Sensor Framework**: Access to accelerometer, gyroscope, magnetometer, barometer, proximity, light, and heart rate sensors via SensorManager API
- **Location Services**: GPS, Network-based positioning through LocationManager with fused location provider
- **Background Processing**: Services, WorkManager, and JobScheduler enable background task execution
- **Rich Media Support**: MediaCodec, MediaExtractor, and AudioTrack APIs for audio/video processing
- **Connectivity**: Wi-Fi Direct, Bluetooth (classic and BLE), NFC, and USB connectivity APIs

## 6. Android Architecture Stack

Android employs a layered architecture enabling abstraction and modularity in application development.

### Layer 1: Linux Kernel

The foundation layer providing core system services: memory management, process scheduling, power management, device drivers, and security enforcement through SELinux policies.

### Layer 2: Native Libraries

C/C++ libraries including:

- **Bionic**: Custom libc implementation
- **WebKit**: HTML rendering engine
- **OpenGL ES**: Graphics rendering
- **SQLite**: Embedded database
- **Media Framework**: Audio/video codecs

### Layer 3: Android Runtime (ART)

ART compiles DEX bytecode to native machine code via ahead-of-time (AOT) compilation, replacing the legacy Dalvik interpreter. Features include garbage collection optimizations, debugging support, and improved performance.

### Layer 4: Application Framework

Java API framework providing:

- **Activity Manager**: Manages application lifecycle and task orchestration
- **Window Manager**: Controls window display and positioning
- **Content Provider**: Manages inter-application data sharing
- **View System**: UI component hierarchy and rendering
- **Package Manager**: Application installation and metadata management
- **Telephony Manager**: Cellular communication services
- **Location Manager**: Geographic positioning services

### Layer 5: Applications

User applications and system applications (Dialer, Settings, Browser) constructed using Application Framework APIs.

## 7. Linux Kernel Relationship

Android's utilization of the Linux kernel (versions 3.x through 5.x adapted for mobile) provides several critical capabilities:

- **Process Isolation**: Linux cgroups and namespaces provide application sandboxing
- **Memory Management**: Low Memory Killer and Ashmem manage constrained mobile memory
- **File System**: YAFFS2, ext4, and F2FS provide flash storage optimization
- **Security Model**: SELinux mandatory access control, UID-based process separation, and SELinux contexts
- **Power Management**: Wakelocks, cpufreq governors, and suspend/resume mechanisms

The kernel abstraction enables Android to remain agnostic to specific hardware while leveraging proven, battle-tested kernel subsystems.