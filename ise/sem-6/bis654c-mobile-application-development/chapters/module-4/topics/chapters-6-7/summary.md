# **Mobile Application Development Revision Notes - Chapters 6 & 7**

### Intent

- **Definition:** An intent is a message sent from one application to another, requesting a specific action.
- **Types:**
  - Implicit intent: requests a general action (e.g., "open the browser").
  - Explicit intent: requests a specific action (e.g., "open the browser with Google").
- **Intent Filter:**
  - A component that specifies the actions an intent can trigger.
  - Declared in the AndroidManifest.xml file.
- **Intent Action:**
  - The specific action requested by the intent.
  - Defined as an action in the intent filter.

### Activity Life Cycle

- **Definition:** The sequence of events an activity undergoes during its lifetime.
- **Life Cycle Methods:**
  - `onCreate()`: called when the activity is created.
  - `onStart()`: called when the activity becomes visible.
  - `onResume()`: called when the activity is resumed.
  - `onPause()`: called when the activity is paused.
  - `onStop()`: called when the activity is stopped.
  - `onDestroy()`: called when the activity is destroyed.

### Broadcast Life Cycle

- **Definition:** The sequence of events a broadcast receives during its lifetime.
- **Broadcast Methods:**
  - `onReceive()`: called when the broadcast is received.
  - `onPause()`: called when the broadcast is paused.
  - `onResume()`: called when the broadcast is resumed.
  - `onDestroy()`: called when the broadcast is destroyed.

### Important Formulas and Definitions

- **Intent Filter:** ` android.content.IntentFilter = <action> + <category> + <data> + <category> android.content.IntentFilter = <action> + <category> + <data> + < extras>`

Note: These notes are based on general Android development concepts and may not cover all the topics in chapters 6 & 7.
