# Service Component

## Overview

Services run background operations without user interface, perfect for long-running tasks like music playback, network operations, or data synchronization. Understanding service types and lifecycle is essential.

## Key Points

- **Started Service**: Runs indefinitely until stopped, initiated via startService()
- **Bound Service**: Provides client-server interface, initiated via bindService()
- **Foreground Service**: Shows notification, higher priority, less likely killed
- **IntentService**: Handles asynchronous requests on worker thread, self-stopping
- **Service Lifecycle**: onCreate(), onStartCommand(), onBind(), onDestroy()
- **WorkManager**: Modern alternative for deferrable background work

## Important Concepts

- Services run on main thread by default (manual threading needed)
- Foreground services require FOREGROUND_SERVICE permission
- Bound services die when no clients connected
- IntentService deprecated in API 30, use JobIntentService or WorkManager

## Notes

- Use foreground services for user-aware operations
- Prefer WorkManager for background tasks over raw services
- Understand service vs thread distinction
- Master onStartCommand() return values: START_STICKY, START_NOT_STICKY
