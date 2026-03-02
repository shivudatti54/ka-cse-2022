# Multimedia in Android

## Overview

Android provides comprehensive multimedia support for audio, video, and image handling. Understanding MediaPlayer, ExoPlayer, and camera APIs enables rich multimedia experiences in applications.

## Key Points

- **MediaPlayer**: Plays audio/video from resources, files, or streams
- **ExoPlayer**: Advanced media player with adaptive streaming support
- **Camera API**: Camera and Camera2 for capturing photos and videos
- **MediaRecorder**: Records audio and video with various formats
- **Bitmap**: Image loading and manipulation
- **Image Loading Libraries**: Glide, Picasso for efficient image loading
- **Permissions**: CAMERA, RECORD_AUDIO, READ_EXTERNAL_STORAGE required

## Important Concepts

- MediaPlayer lifecycle: prepare(), start(), pause(), stop(), release()
- SurfaceView for video playback display
- Camera2 API provides manual camera controls
- Bitmap optimization to prevent OutOfMemoryError
- ExoPlayer handles DASH, HLS, SmoothStreaming

## Notes

- Always release MediaPlayer resources in onDestroy()
- Use Glide/Picasso to avoid bitmap memory issues
- Request runtime permissions for camera and audio recording
- Prefer ExoPlayer for advanced video streaming needs
