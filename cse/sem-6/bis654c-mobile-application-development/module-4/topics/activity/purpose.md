### Learning Purpose: Android Activity Lifecycle

**1. Why is this topic important?**
The Activity is the fundamental building block of Android application UI. Understanding its lifecycle -- the sequence of callback methods (onCreate, onStart, onResume, onPause, onStop, onDestroy) -- is critical for managing resources, preserving user state, and preventing crashes caused by improper lifecycle handling.

**2. Real-world applications:**
Every Android application uses Activities. Proper lifecycle management ensures that apps save user progress when interrupted by phone calls, preserve form data during screen rotations, release camera or GPS resources when backgrounded, and resume smoothly when the user returns. These are essential behaviors users expect from any well-built app.

**3. Connection to other topics:**
The Activity lifecycle is foundational to Services (which have their own lifecycle), multimedia playback (which must respect lifecycle state changes to pause/resume audio and video), and navigation between screens using Intents. Mastery of the Activity lifecycle is a prerequisite for understanding every other Android component.
