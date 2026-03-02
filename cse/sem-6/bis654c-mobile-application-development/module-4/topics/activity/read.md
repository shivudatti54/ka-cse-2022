# Activity Lifecycle in Android

## Introduction to Activity Lifecycle

In Android development, an **Activity** represents a single screen with a user interface. Understanding the Activity lifecycle is crucial for building robust applications that respond appropriately to user interactions and system events. The lifecycle consists of a series of states that an Activity transitions through from creation to destruction.

## Why Activity Lifecycle Matters

The Android system manages Activities through a stack-like structure. When a new Activity starts, it moves to the top of the stack and becomes the running Activity. The previous Activity remains below it and is stopped or paused. The system can destroy Activities when memory is low, making it essential to properly manage state transitions.

## Activity Lifecycle States and Callback Methods

An Activity transitions through various states, and the system calls specific callback methods at each transition. You should override these methods to perform appropriate actions.

### Core Lifecycle States

1. **Created**: Activity is being initialized
2. **Started**: Activity is visible but not interactive
3. **Resumed**: Activity is visible and interactive (foreground)
4. **Paused**: Activity is partially visible but not interactive
5. **Stopped**: Activity is not visible
6. **Destroyed**: Activity is being removed from memory

### Lifecycle Callback Methods

```java
public class MainActivity extends AppCompatActivity {

 @Override
 protected void onCreate(Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 setContentView(R.layout.activity_main);
 // Initialize UI components and data
 }

 @Override
 protected void onStart() {
 super.onStart();
 // Activity becoming visible
 }

 @Override
 protected void onResume() {
 super.onResume();
 // Activity now interactive
 }

 @Override
 protected void onPause() {
 super.onPause();
 // Activity partially obscured
 }

 @Override
 protected void onStop() {
 super.onStop();
 // Activity no longer visible
 }

 @Override
 protected void onRestart() {
 super.onRestart();
 // Activity restarting after being stopped
 }

 @Override
 protected void onDestroy() {
 super.onDestroy();
 // Activity being destroyed
 }
}
```

## Lifecycle Flow Diagram

```
 onCreate() → onStart() → onResume()
 ↑ | ↑ |
 | ↓ | ↓
 onRestart() ← onStop() ← onPause()
 ↑ ↓
 └────── onDestroy() ←
```

ASCII representation of the lifecycle flow:

```
 +------------+
 | Created | ← onCreate()
 +------------+
 ↓
 +------------+
 | Started | ← onStart()
 +------------+
 ↓
 +------------+ User returns +------------+
 | Resumed | ← onResume() | Paused | ← onPause()
 +------------+ → onPause() +------------+
 | ↓
 +------------+ +------------+
 | Stopped | ← onStop() | Destroyed | ← onDestroy()
 +------------+ +------------+
 ↑ ↑
 └────── onRestart() ──────────────┘
```

## Detailed Explanation of Each Callback

### onCreate()

- Called when the Activity is first created
- Perform one-time initialization (UI setup, data binding)
- Always followed by onStart()
- Receives savedInstanceState Bundle for state restoration

### onStart()

- Called when the Activity becomes visible to the user
- Prepare resources needed while visible
- Followed by onResume() if Activity comes to foreground
- Followed by onStop() if Activity becomes hidden

### onResume()

- Called when the Activity starts interacting with the user
- Resume animations, updates, or resources that were paused
- Activity is at the top of the activity stack
- Followed by onPause() when another Activity comes forward

### onPause()

- Called when the Activity is partially obscured
- Pause ongoing operations that shouldn't continue while paused
- Commit unsaved changes (draft emails, etc.)
- Should perform lightweight operations (this method is not for heavy work)

### onStop()

- Called when the Activity is no longer visible to the user
- Release or adjust resources that aren't needed while not visible
- Perform relatively heavy cleanup operations
- The system may kill the process after this without calling onDestroy()

### onRestart()

- Called when the Activity is restarting after being stopped
- Special case between onStop() and onStart()
- Perform any special re-initialization needed after being stopped

### onDestroy()

- Called before the Activity is destroyed
- Final cleanup of resources to avoid memory leaks
- Is the final call the Activity receives
- May not be called if the system needs to urgently reclaim memory

## Saving and Restoring Activity State

### onSaveInstanceState()

```java
@Override
protected void onSaveInstanceState(Bundle outState) {
 super.onSaveInstanceState(outState);
 outState.putString("KEY_USER_INPUT", userInputText);
 outState.putInt("KEY_SCORE", currentScore);
}
```

### Restoring State

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 setContentView(R.layout.activity_main);

 if (savedInstanceState != null) {
 String savedInput = savedInstanceState.getString("KEY_USER_INPUT");
 int savedScore = savedInstanceState.getInt("KEY_SCORE");
 // Restore your state here
 }
}
```

## Lifecycle-Aware Components

With Android Architecture Components, you can create lifecycle-aware components:

```java
public class MyLocationListener implements LifecycleObserver {

 @OnLifecycleEvent(Lifecycle.Event.ON_RESUME)
 public void startLocationUpdates() {
 // Start location updates
 }

 @OnLifecycleEvent(Lifecycle.Event.ON_PAUSE)
 public void stopLocationUpdates() {
 // Stop location updates
 }
}

// In your Activity
MyLocationListener listener = new MyLocationListener();
getLifecycle().addObserver(listener);
```

## Common Lifecycle Scenarios

### Scenario 1: Starting a New Activity

```
Current Activity: onPause() → onStop()
New Activity: onCreate() → onStart() → onResume()
```

### Scenario 2: Returning to Previous Activity

```
Current Activity: onPause() → onStop() → onDestroy()
Previous Activity: onRestart() → onStart() → onResume()
```

### Scenario 3: Configuration Changes (Screen Rotation)

```
Current Activity: onPause() → onSaveInstanceState() → onStop() → onDestroy()
New Activity: onCreate() → onStart() → onRestoreInstanceState() → onResume()
```

## Comparison Table: Lifecycle Methods

| Method      | When Called           | Typical Use Cases                                          |
| ----------- | --------------------- | ---------------------------------------------------------- |
| onCreate()  | First creation        | Initialize UI, bind data, set content view                 |
| onStart()   | Becoming visible      | Start animations, register broadcast receivers             |
| onResume()  | Becoming interactive  | Start sensors, animations, camera preview                  |
| onPause()   | Partially obscured    | Pause animations, commit data, release exclusive resources |
| onStop()    | No longer visible     | Stop heavy operations, unregister listeners                |
| onRestart() | Restarting after stop | Reinitialize resources released in onStop()                |
| onDestroy() | Final cleanup         | Release all resources, close database connections          |

## Best Practices

1. **Keep onCreate() lightweight** - Don't perform long operations here
2. **Use onPause() for critical saves** - This method is always called
3. **Release resources in onStop()** - Don't wait until onDestroy()
4. **Use ViewModel for configuration changes** - Preserve UI data across rotations
5. **Test lifecycle transitions** - Ensure your app behaves correctly in all scenarios

## Common Mistakes to Avoid

- Performing network operations in UI lifecycle methods
- Not saving state in onSaveInstanceState()
- Forgetting to call super methods in overridden lifecycle methods
- Holding references to Context that can cause memory leaks

## Exam Tips

1. Remember the order of lifecycle calls: onCreate() → onStart() → onResume() → onPause() → onStop() → onDestroy()
2. onSaveInstanceState() is called before onStop() but not before onPause()
3. onRestart() is only called when returning from a stopped state, not from paused
4. Configuration changes destroy and recreate the Activity, triggering the full lifecycle
5. The system can kill your process after onStop() without calling onDestroy()
