# **Mobile Application Development: Introduction – Intent – Intent Filter – Activity Life Cycle – Broadcast Life Cycle**

## **Chapter 6: Intent**

### Introduction

In Android, an intent is a message that is sent from one application to another. It is used to request a specific action to be performed, such as launching a new activity or retrieving data from a web service. Intents are the primary means of communication between different components of an Android application.

### Types of Intents

- **Explicit Intents**: These are used to launch a specific activity. The intent is sent to the bundle of the activity we want to open.
- **Implicit Intents**: These are used to request the system to find an activity that can handle the intent. The system looks for an activity that matches the intent filter.

### Creating Intents

Intents can be created using the `Intent` class. The following code snippet demonstrates how to create an explicit intent.

```java
// Create an explicit intent
Intent intent = new Intent(this, MyActivity.class);
```

### Setting Intent Data

Intents can also be used to pass data to an activity. The following code snippet demonstrates how to set data in an explicit intent.

```java
// Create an explicit intent
Intent intent = new Intent(this, MyActivity.class);
intent.putExtra("key", "value");
```

### Intent Filters

---

An intent filter is used to define the components that can handle an intent. It is used in implicit intents to specify which activities can handle the intent.

### Declaring Intent Filters in AndroidManifest.xml

```xml
<activity android:name=".MyActivity">
    <intent-filter>
        <action android:name="com.example.MyActivityAction" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

## **Chapter 7: Intent Filters and Activity Life Cycle**

### Intent Filters

Intent filters are used to specify which components can handle an intent. They are used in implicit intents to define the activities that can handle the intent.

### Activity Life Cycle

---

The activity life cycle is the sequence of events that an activity goes through when it is created and destroyed. Each activity in an Android application goes through the following states:

1.  **Paused**: The activity is paused and the user is interacting with other applications.
2.  **Stopped**: The activity is stopped and any background threads are canceled.
3.  **Resumed**: The activity is resumed and the user can interact with the application again.
4.  **Destroyed**: The activity is completely destroyed and any resources are released.

### Activity Life Cycle Methods

The following methods are called by the Android system during the activity life cycle:

- `onCreate()`: Called when the activity is created.
- `onStart()`: Called when the activity becomes visible.
- `onResume()`: Called when the activity is resumed.
- `onPause()`: Called when the activity is paused.
- `onStop()`: Called when the activity is stopped.
- `onDestroy()`: Called when the activity is completely destroyed.

### Example Code

The following code snippet demonstrates the activity life cycle.

```java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d("MainActivity", "onCreate");
    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.d("MainActivity", "onStart");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.d("MainActivity", "onResume");
    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.d("MainActivity", "onPause");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.d("MainActivity", "onStop");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d("MainActivity", "onDestroy");
    }
}
```

### Key Concepts

---

- **Intent Filters**: Used to specify which components can handle an intent.
- **Activity Life Cycle**: The sequence of events that an activity goes through when it is created and destroyed.
- **Explicit Intents**: Used to launch a specific activity.
- **Implicit Intents**: Used to request the system to find an activity that can handle the intent.
- **Broadcast Intents**: Used to send a message to all applications that are registered to receive the broadcast.
