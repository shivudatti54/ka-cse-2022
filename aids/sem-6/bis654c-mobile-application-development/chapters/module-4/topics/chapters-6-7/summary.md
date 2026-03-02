# **Mobile Application Development Revision Notes**

## **Chapters 6 & 7: Intent, Intent Filter, Activity Life Cycle, and Broadcast Life Cycle**

### Intent

- **Definition:** A message sent from an application to another application or a system component.
- **Types:**
  - Explicit intent: Specific intent with a well-defined action and data.
  - Implicit intent: Vague intent that requires the system to match the intent with a specific action.
- **Intent Filter:**
  - A component that declares an intent filter to receive an intent.
  - The intent filter specifies the action, category, and data types that the component can handle.

### Intent Filter

- **Definition:** A component that declares an intent filter to receive an intent.
- **Components that can have an intent filter:**
  - Activities
  - Broadcast Receivers
  - Services
- **Intent Filter Declaration:**
  - Added in AndroidManifest.xml file
  - `<intent-filter>` tag
  - Specifies the action, category, and data types that the component can handle

### Activity Life Cycle

- **Definition:** The sequence of events an activity goes through while running.
- **Activity Life Cycle Methods:**
  - `onCreate()`: Called when the activity is created.
  - `onStart()`: Called when the activity is started.
  - `onResume()`: Called when the activity is resumed.
  - `onPause()`: Called when the activity is paused.
  - `onStop()`: Called when the activity is stopped.
  - `onDestroy()`: Called when the activity is destroyed.
  - `onDestroyOptionsMenu()`: Called when the options menu is destroyed.
  - `onDestroyOptionsMenu()`: Called when the options menu is destroyed.
  - `onSaveInstanceState()`: Called to save the activity's state.

### Broadcast Life Cycle

- **Definition:** The sequence of events a broadcast receiver goes through while receiving a broadcast.
- **Broadcast Life Cycle Methods:**
  - `onReceive()`: Called when the broadcast is received.
  - `onReceiveIntent()`: Called when the intent is received.
  - `onIntentFilterMismatch()`: Called when the intent filter does not match.
  - `onActivityResult()` : Called when activity result is broadcast.

### Important Formulas and Theorems

- **Intent Filter Formula:** `intent-filter = <action>, <category>, <data-type>`
- **Broadcast Life Cycle Theorem:** "A broadcast receiver can handle a broadcast only if its intent filter matches the broadcast's intent"

Note: This is a concise summary of the key points. For a more detailed understanding, refer to the Android documentation and code examples.
