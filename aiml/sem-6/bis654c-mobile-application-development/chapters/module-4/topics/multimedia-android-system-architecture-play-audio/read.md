# **Multimedia: Android System Architecture – Play Audio and Video – Text to Speech**

### Introduction

---

In Android, multimedia refers to the integration of various media types such as audio, video, and text. This topic focuses on playing audio and video files, as well as using text-to-speech functionality.

### Android System Architecture

---

### Audio Playback

#### Audio Files

Android supports various audio file formats such as MP3, AAC, and WAV. These files can be played using the `MediaPlayer` class.

#### Playing Audio

To play an audio file, you need to:

- Create a `MediaPlayer` object
- Specify the audio file path
- Set the audio file type (e.g., `MediaFormat.MIMES` enum)
- Start playing the audio

```java
// Create a MediaPlayer object
MediaPlayer mediaPlayer = new MediaPlayer();

// Specify the audio file path
mediaPlayer.setDataSource("/path/to/audio/file.mp3");

// Set the audio file type
mediaPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);

// Start playing the audio
mediaPlayer.start();
```

### Video Playback

Android supports various video file formats such as MP4, AVI, and FLV. Video playback can be achieved using the `MediaPlayer` class or the `VideoView` widget.

#### Playing Video

To play a video file, you need to:

- Create a `MediaPlayer` object or inflate a `VideoView` widget
- Specify the video file path
- Set the video file type (e.g., `MediaFormat.MIMES` enum)
- Start playing the video

```java
// Create a MediaPlayer object
MediaPlayer mediaPlayer = new MediaPlayer();

// Specify the video file path
mediaPlayer.setDataSource("/path/to/video/file.mp4");

// Set the video file type
mediaPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);

// Start playing the video
mediaPlayer.start();
```

### Text to Speech

Android provides the `textToSpeech` method in the `SpeechRecognizer` class to convert text into speech.

#### Text to Speech

To use text-to-speech functionality:

- Create a `SpeechRecognizer` object
- Specify the text to be converted to speech
- Set the language and voice parameters
- Start the speech synthesis

```java
// Create a SpeechRecognizer object
SpeechRecognizer speechRecognizer = SpeechRecognizer.createSpeechRecognizer(this);

// Specify the text to be converted to speech
String text = "Hello, World!";
String lang = "en-US";

// Set the language and voice parameters
 speechRecognizer.setLanguage(lang);

// Start the speech synthesis
 speechRecognizer.speak(text, TextToSpeech.QUEUE_FLUSH, null);
```

### Key Concepts

---

- `MediaPlayer` class for playing audio and video files
- `VideoView` widget for playing video files
- `SpeechRecognizer` class for text-to-speech functionality
- `MediaFormat.MIMES` enum for specifying audio and video file types
- `AudioManager.STREAM_MUSIC` for setting audio stream type

### Best Practices

---

- Use the `MediaPlayer` class for playing audio and video files
- Use the `VideoView` widget for playing video files
- Use the `SpeechRecognizer` class for text-to-speech functionality
- Set the language and voice parameters for the text-to-speech functionality
