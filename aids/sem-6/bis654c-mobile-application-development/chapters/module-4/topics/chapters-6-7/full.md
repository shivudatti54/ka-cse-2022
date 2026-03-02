# **Introduction to Intent and Intent Filter**

In the world of Android app development, intents are a fundamental concept that enables communication between different components of an application and between applications themselves. In this chapter, we will delve into the world of intents and intent filters, exploring their history, working, and application in mobile application development.

### Historical Context

The concept of intents dates back to the early days of Android, when it was first introduced in Android 1.5 (Cupcake). The introduction of intents allowed Android applications to communicate with each other, enabling features such as sharing files, launching other applications, and performing actions on behalf of the user.

### Working of Intents

An intent is a message that an Android application sends to another application or component, requesting a specific action to be performed. Intents can be thought of as a request for a service, where the requesting application specifies the service it needs, and the receiving application decides whether to provide it.

An intent is composed of three main components:

1.  **Action**: The action that the intent is requesting the receiving application to perform. Actions are represented as strings and can be anything from "android.intent.action.VIEW" to "android.intent.action.SEND".
2.  **Data**: The data that the intent is requesting the receiving application to handle. Data can be in the form of a URL, a file path, or even a custom data type.
3.  **Type**: The MIME type of the data being requested. MIME types are used to determine the type of data being requested, such as "text/plain" for text data or "image/jpeg" for image data.

### Intent Filters

Intent filters are used to specify which components of an Android application can handle a particular intent. Intent filters are added to the AndroidManifest.xml file and are used to define the components that can receive an intent.

An intent filter has three main components:

1.  **Action**: The action that the intent filter is requesting to handle.
2.  **Data**: The data that the intent filter is requesting to handle.
3.  **Category**: A category that specifies the type of intent filter. Categories are used to group intent filters together and can be used to specify additional requirements for an intent filter.

### Activity Life Cycle and Intents

Activities in Android are the primary entry points for an application. When an activity is created, it goes through a life cycle of states, including onCreate, onStart, onResume, onPause, onStop, and onDestroy.

Intents can be used to communicate between activities within the same application. For example, when a user selects a file from the file manager, an intent is sent to the activity that is currently handling the file selection. The selected file is then passed to the activity as an intent extra.

### Broadcast Life Cycle and Intents

Broadcasts in Android are used to send an intent to all components of an application that are registered to receive it. Broadcasts are typically used to notify components of an application of an event, such as a new message being received.

When a broadcast is sent, the Android system checks all the registered components to see if they can handle the broadcast. If a component can handle the broadcast, it is executed and returns a result to the Android system.

### Example: Using Intents to Launch an Activity

Here is an example of how an intent can be used to launch an activity:

```java
// Create an intent to launch an activity
Intent intent = new Intent(this, MyActivity.class);

// Start the activity
startActivity(intent);
```

In this example, an intent is created to launch the MyActivity class. The intent is then started using the startActivity method.

### Example: Using Intents to Send Data to an Activity

Here is an example of how an intent can be used to send data to an activity:

```java
// Create an intent to send data to an activity
Intent intent = new Intent(this, MyActivity.class);
intent.putExtra("name", "John Doe");

// Start the activity
startActivity(intent);
```

In this example, an intent is created to send a string extra named "name" to the MyActivity class. The intent is then started using the startActivity method.

### Example: Using Intent Filters to Handle Intents

Here is an example of how an intent filter can be used to handle an intent:

```xml
// Define an intent filter in the AndroidManifest.xml file
<intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="http" />
    <data android:scheme="https" />
</intent-filter>
```

In this example, an intent filter is defined to handle intents with the action android.intent.action.VIEW and category android.intent.category.DEFAULT. The intent filter also specifies the schemes http and https.

### Conclusion

Intents are a powerful tool in Android app development, allowing applications to communicate with each other and with the Android system. Intent filters are used to specify which components can handle an intent, and activities and broadcasts are used to send and receive intents.

In the next chapter, we will explore the concept of broadcasting in Android, including how to send and receive broadcasts, and how to handle broadcasts in an application.

---

### Further Reading

- "Android Intent" by Android Developers
- "Intents in Android" by Android Authority
- "Android Broadcasts" by Droid Guide
- "Android App Development: The Big Nerd Ranch Guide" by Big Nerd Ranch
- "Android Programming: The Complete Reference" by Packt Publishing
