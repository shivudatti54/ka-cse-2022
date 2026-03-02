# Multimedia: Android System Architecture – Play Audio and Video – Text to Speech

===========================================================

## Introduction

In this topic, we will explore the Android system architecture and how to play audio and video, as well as use text-to-speech functionality.

## Android System Architecture

### Definition

The Android system architecture refers to the underlying structure and components that make up the Android operating system.

- **Components:** The Android system architecture is composed of various components, including applications, services, broadcasts, content providers, and more.
- **Components Interaction:** These components interact with each other through intent, broadcast, and content provider mechanisms.

### Intent

An intent is a message that an application sends to the system to request a specific action or service.

- **Intent Filter:** An intent filter is a mechanism that allows an application to specify what actions it can handle.
- **Intent Action:** An intent action is the specific action that an application is requesting, such as "play audio" or "open URL".
- **Intent Data:** An intent data is the additional information associated with an intent, such as a URL or a file path.

### Activity Life Cycle

An activity is a single-screen application that interacts with the user.

- **Activity Creation:** When an activity is created, it goes through a life cycle of states, including `CREATE`, `START`, `RESUMED`, `PAUSED`, `STOPPED`, and `DESTROY`.
- **Activity Methods:** Activities have various methods that can be called at different points during the life cycle, such as `onCreate`, `onStart`, and `onPause`.

### Broadcast Life Cycle

A broadcast is a way for an application to send a message to other applications.

- **Broadcast Creation:** A broadcast is created when an application uses the `Intent` class to send a message to the system.
- **Broadcast Receiver:** A broadcast receiver is an application that registers to receive broadcasts and handles the messages.

## Playing Audio

### Definition

Playing audio refers to the process of producing sound or music.

- **Audio Players:** Android provides various audio player components, including `MediaPlayer`, `AudioManager`, and `SoundPool`.
- **Audio Formats:** Android supports various audio formats, including MP3, AAC, and WAV.

### Playing Audio with MediaPlayer

The `MediaPlayer` class is a common audio player component in Android.

- **MediaPlayer Methods:** The `MediaPlayer` class has various methods that can be used to play audio, such as `setDataSource`, `setAudioStreamType`, and `start`.
- **MediaPlayer States:** The `MediaPlayer` class has various states, including `STATE_IDLE`, `STATE_PREPARED`, `STATE_PLAYING`, and `STATE_PAUSED`.

### Playing Audio with AudioPlayer

The `AudioPlayer` class is another audio player component in Android.

- **AudioPlayer Methods:** The `AudioPlayer` class has various methods that can be used to play audio, such as `play`, `pause`, and `stop`.
- **AudioPlayer States:** The `AudioPlayer` class has various states, including `PLAYING`, `PAUSED`, and `STOPPED`.

## Playing Video

### Definition

Playing video refers to the process of displaying moving images.

- **Video Players:** Android provides various video player components, including `MediaPlayer`, `VideoView`, and `SurfaceView`.
- **Video Formats:** Android supports various video formats, including MP4, AVI, and FLV.

### Playing Video with MediaPlayer

The `MediaPlayer` class can be used to play video.

- **MediaPlayer Methods:** The `MediaPlayer` class has various methods that can be used to play video, such as `setDataSource`, `setAudioStreamType`, and `start`.
- **MediaPlayer States:** The `MediaPlayer` class has various states, including `STATE_IDLE`, `STATE_PREPARED`, `STATE_PLAYING`, and `STATE_PAUSED`.

### Playing Video with VideoView

The `VideoView` class is a common video player component in Android.

- **VideoView Methods:** The `VideoView` class has various methods that can be used to play video, such as `setVideoUri`, `start`, and `stop`.
- **VideoView States:** The `VideoView` class has various states, including `PLAYING`, `PAUSED`, and `STOPPED`.

## Text-to-Speech

### Definition

Text-to-speech refers to the process of converting written text into spoken words.

- **Text-to-Speech Engines:** Android provides various text-to-speech engines, including Google Text-to-Speech and EBS TTS.
- **Text-to-Speech Methods:** Text-to-speech engines have various methods that can be used to convert text into speech, such as `speak` and `stop`.

### Using Text-to-Speech

To use text-to-speech in Android, you can use the `TextToSpeech` class.

- **TextToSpeech Methods:** The `TextToSpeech` class has various methods that can be used to convert text into speech, such as `init` and `speak`.
- **TextToSpeech States:** The `TextToSpeech` class has various states, including `Idle` and `Speaking`.

### Example Code

Here is an example of how to use text-to-speech in Android:

```java
import android.os.Bundle;
import android.speech.tts.TextToSpeech;

public class MainActivity extends AppCompatActivity {
    private TextToSpeech textToSpeech;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textToSpeech = TextToSpeech(this, new TextToSpeech.OnInitListener() {
            @Override
            public void onInit(int status) {
                if (status != TextToSpeech.ERROR) {
                    textToSpeech.speak("Hello, World!", TextToSpeech.QUEUE_FLUSH, null);
                }
            }
        });
    }
}
```

### Key Concepts

- Intent: A message that an application sends to the system to request a specific action or service.
- Activity Life Cycle: The life cycle of an activity, including creation, start, resumed, paused, stopped, and destroyed.
- Broadcast Life Cycle: The life cycle of a broadcast, including creation, broadcast, and finished.
- MediaPlayer: A common audio player component in Android.
- VideoView: A common video player component in Android.
- TextToSpeech: A class that provides text-to-speech functionality in Android.
