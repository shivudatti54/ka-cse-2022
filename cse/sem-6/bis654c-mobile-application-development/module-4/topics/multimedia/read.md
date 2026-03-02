# Audio and Video Playback in Android

## Introduction to Multimedia Playback

Multimedia playback is a fundamental feature in modern mobile applications, enabling users to consume audio and video content. Android provides robust frameworks and APIs to handle multimedia efficiently. This module focuses on implementing audio and video playback in Android applications using the `MediaPlayer` and `VideoView` classes, along with managing media resources and understanding the associated lifecycle events.

## Key Components for Multimedia Playback

### 1. MediaPlayer Class

The `MediaPlayer` class is the primary API for playing audio and video. It supports various media sources, including local files, raw resources, and network streams.

**Key Methods of MediaPlayer:**

- `setDataSource()`: Sets the data source (file path, URI, or file descriptor).
- `prepare()`: Prepares the player for playback synchronously.
- `prepareAsync()`: Prepares the player asynchronously (non-blocking).
- `start()`: Starts or resumes playback.
- `pause()`: Pauses playback.
- `stop()`: Stops playback; requires re-preparation to play again.
- `release()`: Releases resources associated with the MediaPlayer.
- `seekTo()`: Seeks to a specified position in the media.

**State Diagram of MediaPlayer:**

```
Idle → setDataSource() → Initialized → prepare()/prepareAsync() → Prepared → start() → Started
 ↑ ↓
 ←←←←←←←←←←←←←←←←←←←←← pause() ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
 ↓ ↓
Stopped ←←←←←←←←←←←←←←←← stop() ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
```

### 2. VideoView Class

The `VideoView` class is a wrapper around `MediaPlayer` specifically designed for video playback. It provides a UI component that displays video and handles user interactions like play, pause, and seek.

**Key Methods of VideoView:**

- `setVideoPath()`: Sets the video file path.
- `setVideoURI()`: Sets the video URI (local or network).
- `start()`, `pause()`, `stopPlayback()`: Control playback.
- `seekTo()`: Seeks to a specified position.

**Usage Example:**

```xml
<VideoView
 android:id="@+id/videoView"
 android:layout_width="match_parent"
 android:layout_height="match_parent" />
```

```java
VideoView videoView = findViewById(R.id.videoView);
videoView.setVideoPath("path/to/video.mp4");
videoView.start();
```

## Implementing Audio Playback

### Using MediaPlayer for Audio

To play audio, you can use the `MediaPlayer` class. Here's a step-by-step implementation:

1. **Initialize MediaPlayer:**

```java
MediaPlayer mediaPlayer = new MediaPlayer();
```

2. **Set Data Source:**

```java
try {
mediaPlayer.setDataSource("path/to/audio.mp3");
} catch (IOException e) {
e.printStackTrace();
}
```

3. **Prepare and Play:**

```java
mediaPlayer.prepareAsync(); // Asynchronous preparation
mediaPlayer.setOnPreparedListener(new MediaPlayer.OnPreparedListener() {
@Override
public void onPrepared(MediaPlayer mp) {
mediaPlayer.start();
}
});
```

4. **Handle Playback Controls:**

```java
// Pause playback
mediaPlayer.pause();

// Resume playback
mediaPlayer.start();

// Stop and release
mediaPlayer.stop();
mediaPlayer.release();
```

### Playing Audio from Raw Resources

You can also play audio from the `res/raw` directory:

```java
MediaPlayer mediaPlayer = MediaPlayer.create(this, R.raw.audio_file);
mediaPlayer.start();
```

## Implementing Video Playback

### Using VideoView for Video

The `VideoView` simplifies video playback by integrating with `MediaPlayer` and providing a built-in UI.

1. **Add VideoView to Layout:**

```xml
<VideoView
android:id="@+id/videoView"
android:layout_width="match_parent"
android:layout_height="match_parent" />
```

2. **Set Video Source and Play:**

```java
VideoView videoView = findViewById(R.id.videoView);
videoView.setVideoPath("path/to/video.mp4");
videoView.start();
```

3. **Add MediaController for Playback Controls:**

```java
MediaController mediaController = new MediaController(this);
mediaController.setAnchorView(videoView);
videoView.setMediaController(mediaController);
```

### Using MediaPlayer for Advanced Video Playback

For more control over video playback, use `MediaPlayer` with `SurfaceView`:

```java
SurfaceView surfaceView = findViewById(R.id.surfaceView);
SurfaceHolder surfaceHolder = surfaceView.getHolder();
surfaceHolder.addCallback(new SurfaceHolder.Callback() {
 @Override
 public void surfaceCreated(SurfaceHolder holder) {
 mediaPlayer.setDisplay(holder);
 mediaPlayer.start();
 }

 @Override
 public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {}

 @Override
 public void surfaceDestroyed(SurfaceHolder holder) {}
});
```

## Managing Media Resources

### Handling Audio Focus

When playing audio, it's important to request audio focus to avoid conflicts with other apps:

```java
AudioManager audioManager = (AudioManager) getSystemService(Context.AUDIO_SERVICE);
int result = audioManager.requestAudioFocus(afChangeListener, AudioManager.STREAM_MUSIC, AudioManager.AUDIOFOCUS_GAIN);

if (result == AudioManager.AUDIOFOCUS_REQUEST_GRANTED) {
 // Start playback
}
```

### Managing Lifecycle

Properly manage the MediaPlayer lifecycle to avoid resource leaks:

```java
@Override
protected void onPause() {
 super.onPause();
 if (mediaPlayer != null && mediaPlayer.isPlaying()) {
 mediaPlayer.pause();
 }
}

@Override
protected void onDestroy() {
 super.onDestroy();
 if (mediaPlayer != null) {
 mediaPlayer.stop();
 mediaPlayer.release();
 mediaPlayer = null;
 }
}
```

## Supported Media Formats

Android supports various media formats. The following table summarizes the common supported formats:

| Format Type            | Audio Formats         | Video Formats          |
| ---------------------- | --------------------- | ---------------------- |
| **Commonly Supported** | MP3, AAC, WAV, OGG    | MP4, 3GP, WebM         |
| **Codecs**             | AAC, MP3, AMR, Vorbis | H.264, H.265, VP8, VP9 |

**Note:** Support may vary across devices and Android versions.

## Error Handling and Events

Implement listeners to handle events and errors:

```java
mediaPlayer.setOnErrorListener(new MediaPlayer.OnErrorListener() {
 @Override
 public boolean onError(MediaPlayer mp, int what, int extra) {
 // Handle error
 return false;
 }
});

mediaPlayer.setOnCompletionListener(new MediaPlayer.OnCompletionListener() {
 @Override
 public void onCompletion(MediaPlayer mp) {
 // Playback completed
 }
});
```

## Performance Considerations

- Use `prepareAsync()` instead of `prepare()` to avoid blocking the UI thread.
- Always call `release()` when done with MediaPlayer to free resources.
- Consider using ExoPlayer for advanced features and better performance with streaming.

## Exam Tips

1. **Remember the MediaPlayer States:** Understand the state transitions (Idle, Initialized, Prepared, Started, Paused, Stopped, PlaybackCompleted, Error).
2. **Lifecycle Management:** Always release MediaPlayer in `onDestroy()` to prevent resource leaks.
3. **Audio Focus:** Request audio focus before playback and handle focus change events appropriately.
4. **Error Handling:** Implement OnErrorListener to handle playback errors gracefully.
5. **VideoView vs MediaPlayer:** Know when to use VideoView (simple playback) vs MediaPlayer with SurfaceView (advanced control).
6. **Threading:** Use asynchronous preparation (`prepareAsync()`) to avoid ANR (Application Not Responding) errors.
7. **Format Support:** Be aware that supported media formats may vary across devices.
