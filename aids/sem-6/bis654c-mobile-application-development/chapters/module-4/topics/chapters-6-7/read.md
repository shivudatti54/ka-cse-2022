# **Mobile Application Development**

## **Module: Activity - Intent - Intent Filter - Activity Life Cycle - Broadcast Life Cycle**

## **Introduction to Activities**

- An **Activity** is a fundamental concept in Android app development. It represents a single screen or UI component in an app.
- An activity is a self-contained piece of code that performs a specific task, such as displaying a list of items or handling user input.
- Activities are used to manage the user interface and user experience of an app.

## **Intent**

- An **Intent** is a message sent from an app to another component, such as another app or a service.
- Intents are used to communicate between different parts of an app or between apps.
- Intents can be used to start a new activity, send a broadcast, or bind to a service.
- There are two types of intents:
  - **Explicit intent**: An explicit intent is a specific intent that is used to start a specific activity or component.
  - **Implicit intent**: An implicit intent is a generic intent that is used to start a component, such as a service or broadcast receiver.

## **Intent Filters**

- An **Intent Filter** is a component that specifies the types of intents that can be received by an app.
- Intent filters are used to define the capabilities of an app and the types of intents that it can handle.
- Intent filters are defined in the AndroidManifest.xml file using the `<intent-filter>` element.

## **Activity Life Cycle**

- The **Activity Life Cycle** refers to the different stages that an activity goes through when it is created, started, paused, stopped, and destroyed.
- The activity life cycle is as follows:
  - **onCreate()**: This method is called when the activity is created.
  - **onStart()**: This method is called when the activity is started.
  - **onResume()**: This method is called when the activity is resumed.
  - **onPause()**: This method is called when the activity is paused.
  - **onStop()**: This method is called when the activity is stopped.
  - **onDestroy()**: This method is called when the activity is destroyed.

### Activity Life Cycle Methods

| Method        | Description                           |
| ------------- | ------------------------------------- |
| `onCreate()`  | Called when the activity is created   |
| `onStart()`   | Called when the activity is started   |
| `onResume()`  | Called when the activity is resumed   |
| `onPause()`   | Called when the activity is paused    |
| `onStop()`    | Called when the activity is stopped   |
| `onDestroy()` | Called when the activity is destroyed |

## **Broadcast Life Cycle**

- The **Broadcast Life Cycle** refers to the different stages that a broadcast receiver goes through when it receives a broadcast.
- The broadcast life cycle is as follows:
  - **onReceive()**: This method is called when the broadcast receiver receives the broadcast.
  - \*\*onStartTracking()`: This method is called when the broadcast receiver starts tracking the broadcast.
  - \*\*onStopped()`: This method is called when the broadcast receiver stops tracking the broadcast.

### Broadcast Life Cycle Methods

| Method               | Description                                                      |
| -------------------- | ---------------------------------------------------------------- |
| `onReceive()`        | Called when the broadcast receiver receives the broadcast        |
| `onStartTracking()`: | Called when the broadcast receiver starts tracking the broadcast |
| `onStopped()``:      | Called when the broadcast receiver stops tracking the broadcast  |

## **Example: Using Intent and Intent Filter**

```java
// Define an intent filter in the AndroidManifest.xml file
<intent-filter>
    <action android:name="com.example.MyApp.ACTION_START_ACTIVITY" />
    <category android:name="android.intent.category.DEFAULT" />
</intent-filter>

// Create an intent to start the activity
Intent intent = new Intent(this, MyClass.class);
intent.setAction("com.example.MyApp.ACTION_START_ACTIVITY");

// Start the activity using the intent
startActivity(intent);
```

## **Example: Using Broadcast Life Cycle**

```java
// Define a broadcast receiver in the AndroidManifest.xml file
<receiver android:name=".MyBroadcastReceiver">
    <intent-filter>
        <action android:name="com.example.MyApp.ACTION_START_BROADCAST" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</receiver>

// Create a broadcast to start the broadcast receiver
Intent intent = new Intent(this, MyBroadcastReceiver.class);
intent.setAction("com.example.MyApp.ACTION_START_BROADCAST");

// Send the broadcast to the broadcast receiver
sendBroadcast(intent);

// Define the broadcast receiver class
public class MyBroadcastReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        // Handle the broadcast
        Log.d("MyBroadcastReceiver", "Received broadcast");
    }
}
```
