# Activity Component

## Overview

Activity is a fundamental Android component representing a single screen with user interface. Understanding activity lifecycle and navigation is crucial for building functional Android applications.

## Key Points

- **Activity Lifecycle**: onCreate(), onStart(), onResume(), onPause(), onStop(), onDestroy()
- **Intent Navigation**: Explicit intents for specific activities, implicit intents for actions
- **Activity Stack**: Back stack manages activity navigation history
- **Bundle**: Saves and restores activity state during configuration changes
- **Launch Modes**: standard, singleTop, singleTask, singleInstance
- **Activity Declaration**: Must be declared in AndroidManifest.xml

## Important Concepts

- onCreate() initializes activity and inflates layout
- onSaveInstanceState() preserves data during rotation
- Intent extras pass data between activities
- startActivity() launches new activities
- finish() terminates current activity

## Notes

- Master activity lifecycle callback order
- Practice passing data via Intent extras
- Understand configuration changes and state preservation
- Learn launch modes for different navigation patterns
