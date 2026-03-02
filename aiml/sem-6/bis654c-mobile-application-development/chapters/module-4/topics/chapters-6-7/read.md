# **Mobile Application Development: Chapters 6 & 7**

## **Introduction**

In this module, we will be exploring the fundamental concepts of Android application development, including the intent system, intent filters, and activity and broadcast life cycles.

## **Intent System**

An **intent** is a message that Android sends to an application component (such as an `Activity`, `Service`, or `BroadcastReceiver`) to perform a specific action. Intents are used to communicate between different components of an app, as well as between different apps.

## **Types of Intents**

There are several types of intents:

- **Explicit Intents**: These intents are used to directly invoke a specific component of an app. They require the exact package name and class name of the component.
- **Implicit Intents**: These intents are used to request a component to perform a specific action, but the component is not specified. The system will match the intent with the first component that can handle it.
- **Query Intents**: These intents are used to request a specific piece of data from the system.

## **Intent Filters**

An **intent filter** is a declaration in the manifest file of an app that specifies which intent actions the app can handle. When an intent is sent to the system, the system will match it with the first intent filter that matches.

## **Activity Life Cycle**

An **activity** is a component of an Android app that is responsible for displaying user interface (UI) elements and handling user input. The activity life cycle consists of several states:

### Activity States

- **New**: The activity is created but has not been started yet.
- **Created**: The activity has been started and is now running.
- **Resume**: The activity is running and is visible to the user.
- **Pause**: The activity is running but the user has paused it (e.g., to switch to another app).
- **Stopped**: The activity has been stopped and will not be resumed.
- **Destroyed**: The activity has been destroyed and will be recreated if needed.

### Activity Methods

- `onCreate()`: Called when the activity is created.
- `onStart()`: Called when the activity is started.
- `onResume()`: Called when the activity is resumed.
- `onPause()`: Called when the activity is paused.
- `onStop()`: Called when the activity is stopped.
- `onDestroy()`: Called when the activity is destroyed.

## **Broadcast Life Cycle**

A **broadcast** is a message sent to all components of an app that are registered to receive it. The broadcast life cycle consists of several states:

### Broadcast States

- **Broadcast Intent**: The broadcast intent is sent to the system.
- **Broadcast Receiver**: The broadcast receiver is created and will receive the broadcast intent.
- **Broadcasting**: The broadcast is being sent to all registered broadcast receivers.
- **Finished**: The broadcast has been received by all registered broadcast receivers.

### Broadcast Receiver Methods

- `onReceive()`: Called when the broadcast intent is received.

## **Example Code**

```java
// Intent Filter
<IntentFilter>
    <action android:name="com.example.MY_ACTION" />
</IntentFilter>

// Activity Life Cycle
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onStart() {
        super.onStart();
        // Activity has started
    }

    @Override
    protected void onResume() {
        super.onResume();
        // Activity has resumed
    }
}

// Broadcast Life Cycle
public class BroadcastReceiver extends AndroidBroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        // Broadcast intent received
    }
}
```
