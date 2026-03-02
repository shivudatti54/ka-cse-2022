# Multimedia: Android System Architecture – Play Audio and Video – Text to Speech

===========================================================

## Introduction

---

In Android development, multimedia refers to the ability of an application to play audio and video files, as well as convert text into speech. This topic will cover the android system architecture for playing multimedia content, including a brief overview of audio and video playback, as well as text-to-speech functionality.

## Android System Architecture for Multimedia Playback

---

Android provides a framework for playing multimedia content, including audio and video files. The following components are involved in multimedia playback:

### Audio Playback

Audio playback in Android is handled by the `MediaPlayer` class. This class provides methods for playing, pausing, and stopping audio files.

- `MediaPlayer(context, Uri)` - Creates a new `MediaPlayer` instance.
- `setAudioStreamType(int)` - Sets the audio stream type.
- `setDataSource(Uri)` - Sets the data source for the media player.
- `start()` - Starts playing the media.
- `pause()` - Pauses the media playback.
- `stop()` - Stops the media playback.

### Video Playback

Video playback in Android is handled by the `MediaPlayer` class as well. However, the `MediaPlayer` class only supports playing audio streams. For playing video streams, you need to use the `SurfaceView` class and the `SurfaceHolder` interface.

- `SurfaceView` - A `SurfaceView` is a view that displays a surface that can be used to render video frames.
- `SurfaceHolder` - A `SurfaceHolder` is an interface that provides methods for creating, updating, and destroying a surface.

## Text-to-Speech (TTS) Functionality

---

Text-to-speech functionality in Android is provided by the `TextToSpeech` class. This class allows you to convert text into speech using a synthesizer.

- `TextToSpeech(context, Handler)` - Creates a new `TextToSpeech` instance.
- `speak()` - Speaks the given text.
- `stop()` - Stops speaking.

### TTS Modes

There are two TTS modes in Android: `TTS_mode` and `TTS_mode_enhanced`. The choice of mode depends on the device hardware.

- `TTS_mode` - This mode is used for devices that support hardware TTS.
- `TTS_mode_enhanced` - This mode is used for devices that do not support hardware TTS.

### TTS Settings

You can customize the TTS settings using the `TextToSpeech` class. You can control the speed, pitch, and voice of the speech.

- `setSpeechRate(float)` - Sets the speech rate.
- `setPitch(float)` - Sets the pitch.
- `setVoice(Voice)` - Sets the voice.

## Key Concepts

---

- **MediaPlayer**: A class used for playing audio and video files.
- **SurfaceView**: A view used for rendering video frames.
- **SurfaceHolder**: An interface used for creating, updating, and destroying a surface.
- **TextToSpeech**: A class used for converting text into speech.
- **TTS_mode**: A mode used for devices that support hardware TTS.
- **TTS_mode_enhanced**: A mode used for devices that do not support hardware TTS.
- **SpeechRate**: The speed of the speech.
- **Pitch**: The pitch of the speech.
- **Voice**: The voice of the speech.

### Intent Filter

---

When handling multimedia intent, you need to register an intent filter for the `android.intent.action.VIEW` intent action and the `android.intent.action.MEDIA_PLAYBACK` intent action.

- `IntentFilter` - A class used for specifying the intent filter.
- `action` - The action of the intent.
- `category` - The category of the intent.

### Example Code

---

```java
// Audio Playback
MediaPlayer mediaPlayer = new MediaPlayer(this, Uri.parse("android.resource://com.example.app/raw/audio_file"));
mediaPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);
mediaPlayer.setDataSource(this, Uri.parse("android.resource://com.example.app/raw/audio_file"));
mediaPlayer.start();

// Video Playback
SurfaceView surfaceView = new SurfaceView(this);
SurfaceHolder surfaceHolder = surfaceView.getHolder();
surfaceHolder.setFormat(SurfaceFormat.SWF);
surfaceView.setKeepScreenOn(true);
surfaceView.setZOrderOnTop(true);

// Text-to-Speech
TextToSpeech tts = new TextToSpeech(this, new TextToSpeech.OnInitListener() {
    @Override
    public void onInit(int status) {
        if (status != TTS_ERROR) {
            tts.speak("Hello World", TextToSpeech.QUEUE_FLUSH, null);
        }
    }
});
```

### Best Practices

---

- Always check the device hardware support for TTS before using it.
- Use the `setSpeed` and `setPitch` methods to customize the speech.
- Use the `setVoice` method to change the voice of the speech.
- Always check for errors when handling media playback.
