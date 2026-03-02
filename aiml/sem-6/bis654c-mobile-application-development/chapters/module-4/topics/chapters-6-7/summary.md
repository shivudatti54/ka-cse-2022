# **Mobile Application Development Revision Notes - Chapters 6 & 7**

### Intent and Intent Filter

- **Intent**: A message sent from an application to another application or a service.
- **Intent Filter**: A component that specifies the actions that an application can handle.
- **Intents with Data**:
  - Have a `data` URI or a ` parcel` URI
  - Can be used to start an activity or a service
- **Default Intent Filter**:
  - Used to handle a default action for a particular intent
  - Must be declared in the AndroidManifest.xml file
- **Explicit Intent Filter**:
  - Used to handle a specific action for a particular intent
  - Must be declared in the AndroidManifest.xml file

### Activity Life Cycle

- **Activity Life Cycle Phases**:
  1.  **New**: The activity is created.
  2.  **Created**: The activity is fully created.
  3.  **Resumed**: The activity is visible to the user.
  4.  **Paused**: The activity is not visible to the user.
  5.  **Stopped**: The activity is paused and will not be resumed.
  6.  **Destroyed**: The activity is destroyed.

- **Activity Life Cycle Methods**:
  - `onCreate()`: Called when the activity is created.
  - `onStart()`: Called when the activity is started.
  - `onPause()`: Called when the activity is paused.
  - `onStop()`: Called when the activity is stopped.
  - `onResume()`: Called when the activity is resumed.
  - `onDestroy()`: Called when the activity is destroyed.

### Broadcast Life Cycle

- **Broadcast Life Cycle Phases**:
  1.  **Broadcast Creation**: The broadcast is created.
  2.  **Broadcast Sending**: The broadcast is sent.
  3.  **Broadcast Receiving**: The broadcast is received.
  4.  **Broadcast Completion**: The broadcast is completed.

- **Broadcast Life Cycle Methods**:
  - `onReceive()`: Called when the broadcast is received.

### Important Formulas, Definitions, and Theorems

- **AndroidManifest.xml**: The declaration file for the application's components.
- **Manifest File**: The file that declares the application's components.
- **Component Name**: A unique name for an application's component.
- **Intent Filter Pattern**: ` IntentFilter("action" or "category")`
- **Broadcast Receiver**: A component that receives broadcasts.
