# **Mobile Application Development: Chapters 6 & 7**

## **Table of Contents**

1. [Introduction to Intent and Intent Filter](#introduction-to-intent-and-intent-filter)
2. [Intent Filtration](#intent-filtration)
3. [Activity Life Cycle](#activity-life-cycle)
   - [Starting an Activity](#starting-an-activity)
   - [Resuming an Activity](#resuming-an-activity)
   - [Pausing an Activity](#pausing-an-activity)
   - [Stopping an Activity](#stopping-an-activity)
   - [Finishing an Activity](#finishing-an-activity)
4. [Broadcast Life Cycle](#broadcast-life-cycle)
5. [Case Studies and Applications](#case-studies-and-applications)
6. [Historical Context and Modern Developments](#historical-context-and-modern-developments)
7. [Conclusion](#conclusion)

## **Introduction to Intent and Intent Filter**

In Android, an **intent** is a message sent from an application component to another component or to the system. Intents are used to start activities, broadcast messages, or bind services. An **intent filter** is a mechanism that allows the system to match an intent with a component that can handle it.

An intent filter is defined in the `AndroidManifest.xml` file using the `<intent-filter>` element. The intent filter specifies the components that can receive the intent.

## **Intent Filtration**

Intent filtration is a mechanism that allows the system to match an intent with a component that can handle it. When an intent is sent, the system checks the intent filter of the component that receives the intent to see if it can handle the intent.

There are three types of intent filters:

- **Action filter**: specifies the action that the component can handle.
- **Category filter**: specifies the categories that the component can handle.
- **Data filter**: specifies the data type that the component can handle.

For example:

```xml
<intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <data android:scheme="http" android:host="www.example.com" />
</intent-filter>
```

This intent filter specifies that the component can handle the `VIEW` action, `DEFAULT` category, and `http://www.example.com` data.

## **Activity Life Cycle**

An **activity** is a component that interacts with the user. Android provides a lifecycle for activities, which consists of several states:

- **Created**: the activity is created and the `onCreate()` method is called.
- **Started**: the activity is started and the `onStart()` method is called.
- **Resumed**: the activity is resumed and the `onResume()` method is called.
- **Stopped**: the activity is stopped and the `onStop()` method is called.
- **Paused**: the activity is paused and the `onPause()` method is called.
- **Stopped**: the activity is stopped and the `onStop()` method is called.
- **Destroyed**: the activity is destroyed and the `onDestroy()` method is called.

Here are some key methods in the activity life cycle:

### Starting an Activity

To start an activity, you use the `startActivity()` method. For example:

```java
Intent intent = new Intent(this, anotherActivity.class);
startActivity(intent);
```

### Resuming an Activity

To resume an activity, you use the `startActivity()` method with the `REPLACE_IN_LIST` flag. For example:

```java
Intent intent = new Intent(this, anotherActivity.class);
startActivity(intent, Activity.REPLACE_IN_LIST);
```

### Pausing an Activity

To pause an activity, you use the `pause()` method. For example:

```java
activity.pause();
```

### Stopping an Activity

To stop an activity, you use the `stop()` method. For example:

```java
activity.stop();
```

### Finishing an Activity

To finish an activity, you use the `finish()` method. For example:

```java
activity.finish();
```

## **Broadcast Life Cycle**

A **broadcast** is a message sent from an application component to multiple components. Android provides a lifecycle for broadcasts, which consists of several states:

- **Created**: the broadcast is created and the `onCreate()` method is called.
- **Delivered**: the broadcast is delivered to all recipients.
- **Cancelled**: the broadcast is cancelled.

Here are some key methods in the broadcast life cycle:

### Sending a Broadcast

To send a broadcast, you use the `sendBroadcast()` method. For example:

```java
Intent intent = new Intent(this, anotherActivity.class);
sendBroadcast(intent);
```

### Receiving a Broadcast

To receive a broadcast, you use the `registerReceiver()` method. For example:

```java
IntentFilter intentFilter = new IntentFilter();
registerReceiver(receiver, intentFilter);
```

## **Case Studies and Applications**

Here are some case studies and applications of intent, intent filter, activity life cycle, and broadcast life cycle:

- **Google Maps**: Google Maps uses intents to send information about the user's location to the device's GPS service.
- **Social Media Apps**: Social media apps use intents to send information about the user's activity to the server.
- **SMS Apps**: SMS apps use intents to send information about the user's SMS activity to the device's SMS service.

## **Historical Context and Modern Developments**

Here are some historical context and modern developments related to intent, intent filter, activity life cycle, and broadcast life cycle:

- **Android 1.0**: Android 1.0 introduced the concept of intents and intent filters.
- **Android 2.0**: Android 2.0 introduced the concept of activities and activity life cycles.
- **Android 3.0**: Android 3.0 introduced the concept of broadcasts and broadcast life cycles.
- **Google Play Services**: Google Play Services uses intents and intent filters to send information about the user's activity to the server.

## **Conclusion**

In conclusion, intents, intent filters, activities, and broadcasts are fundamental concepts in Android development. Understanding these concepts is essential for building robust and efficient Android applications.

## **Further Reading**

Here are some further reading suggestions:

- **Android Developer Documentation**: Android Developer Documentation provides comprehensive information on intents, intent filters, activities, and broadcasts.
- **Android API Reference**: Android API Reference provides detailed information on the Android API.
- **Android Developers Blog**: Android Developers Blog provides news and updates on Android development.
- **Android Programming Books**: Android Programming Books provides comprehensive information on Android development.

I hope this helps! Let me know if you have any questions or need further clarification.
