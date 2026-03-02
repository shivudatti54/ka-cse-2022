# **Multimedia: Android System Architecture – Play Audio and Video – Text to Speech**

### Key Points

- **Android System Architecture**
  - Android is a multi-touch, multi-core, and multi-tasking operating system.
  - Android system architecture consists of:
    - Kernel
    - System services
    - Libraries and frameworks
    - Applications
- **Playing Audio and Video**
  - Android provides several ways to play audio and video:
    - `MediaPlayer` class
    - `SurfaceView` and `SurfaceHolder` for custom playback
    - ` texturesView` for displaying video
  - Audio formats supported:
    - MP3
    - AAC
    - WAV
    - AMR
- **Text to Speech**
  - Android provides `TextToSpeech` API for text-to-speech functionality:
    - Supports multiple languages
    - Can be controlled by user (e.g., pause, resume, speak again)
  - Text-to-speech engines:
    - eSpeak
    - Flite
    - Google Text-to-Speech

### Important Formulas and Definitions

- **OSI Model**: 7-layered model for describing network communication
  - Application layer
  - Presentation layer
  - Session layer
  - Transport layer
  - Network layer
  - Data link layer
  - Physical layer
- **TCP/IP Model**: 4-layered model for describing network communication
  - Application layer
  - Transport layer
  - Internet layer
  - Network Access layer

### Theorems

- **NDP (New Data Packet) Theorem**: States that a receiver can never know that a packet was delayed in transmission.
- **SNP (Sliding Window Packet) Theorem**: States that a receiver can never know that a packet was lost in transmission.

### Revision Tips

- Understand the Android system architecture and its components.
- Familiarize yourself with the `MediaPlayer` class and its usage.
- Understand the `TextToSpeech` API and its functionality.
- Practice implementing audio and video playback in your Android applications.
