# Multimedia Android System Architecture - Play Audio - Summary

## Key Definitions

- **MediaPlayer**: Core Android class for controlling audio/video playback, implementing a state machine pattern
- **AudioFocus**: Android's mechanism to manage concurrent audio playback between applications
- **MediaSession**: Framework component enabling media control from external sources (lock screen, Bluetooth, notification)
- **MediaBrowserService**: Service that provides media content browsing capabilities for background playback
- **HAL (Hardware Abstraction Layer)**: Interface connecting software layers to hardware-specific implementations

## Important Formulas

- AudioFocus Request: `AudioManager.requestAudioFocus(AudioFocusRequest)`
- MediaPlayer State Transitions: Idle → Initialized → Prepared → Started → Paused/Stopped → PlaybackCompleted
- Volume during ducking: typically 20-30% of maximum (0.2f - 0.3f)

## Key Points

1. Android multimedia architecture consists of Application, Framework, Native, and HAL layers working in coordination.

2. MediaPlayer must follow strict state machine rules - invalid method calls throw IllegalStateException.

3. Always request audio focus before playback and handle AUDIOFOCUS_LOSS, AUDIOFOCUS_LOSS_TRANSIENT, and AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK events.

4. Background audio requires MediaBrowserService with MediaSession for proper system integration.

5. Call release() on MediaPlayer in onDestroy() to prevent resource leaks - this is critical for application performance.

6. Use prepareAsync() for large files or network streams to avoid blocking the UI thread.

7. MediaSession enables lock screen controls, Bluetooth headset controls, and Android Auto integration.

8. The AudioAttributes.Builder configures audio focus behavior based on usage (USAGE_MEDIA) and content type (CONTENT_TYPE_MUSIC).

## Common Mistakes

1. Forgetting to call release() on MediaPlayer, causing memory leaks and resource exhaustion.

2. Not handling audio focus, leading to unpredictable audio interruption behavior.

3. Calling blocking prepare() on large files in the main thread, causing ANR (Application Not Responding) errors.

4. Attempting to call MediaPlayer methods in invalid states (e.g., calling pause() when in Idle state).

5. Implementing background playback in an Activity instead of a Service, causing playback to stop when app is backgrounded.

6. Not setting AudioAttributes correctly, resulting in improper audio focus behavior.

7. Ignoring error callbacks, which leads to unhandled playback failures and poor user experience.