# **Multimedia: Android System Architecture – Play Audio and Video – Text to Speech**

## **Key Points**

- **Audio Playback**
  - `MediaPlayer` class is used to play audio files
  - `Uri` object is passed to `MediaPlayer` to specify the audio file
  - `setAudioStreamType()` method is used to specify the audio stream type
  - `start()` method is used to start playing the audio
- **Video Playback**
  - `SurfaceView` or `VideoView` class is used to play video files
  - `Uri` object is passed to the video view to specify the video file
  - `setVideoPath()` method is used to specify the video file
  - `start()` method is used to start playing the video
- **Text to Speech**
  - `TextToSpeech` class is used to convert text to speech
  - `Uri` object is passed to `TextToSpeech` to specify the text
  - `setLanguage()` method is used to specify the language
  - `setSpeechRate()` method is used to specify the speech rate

## **Important Formulas and Definitions**

- **Audio Stream Type**
  - `MediaPlayer.AUDIO_STREAM_MUSIC`
  - `MediaPlayer.AUDIO_STREAM_AUDIO_ONLY`
- **Video Stream Type**
  - `MediaPlayer.VIDEO_STREAM_VIDEO`
  - `MediaPlayer.VIDEO_STREAM_AUDIO`

## **Theorems**

- **Android System Architecture**
  - The Android system architecture is designed to provide a robust and efficient way to handle multimedia operations.

## **Revision Tips**

- Practice playing audio and video files using `MediaPlayer` and `SurfaceView` or `VideoView` classes.
- Practice converting text to speech using `TextToSpeech` class.
- Review the different audio and video stream types and their usage.
