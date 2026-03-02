# **Mobile Application Development: Chapters 6 & 7**

## **Table of Contents**

1. [Introduction to Intent and Intent Filters](#introduction-to-intent-and-intent-filters)
2. [Intent Filters](#intent-filters)
3. [Activity Life Cycle](#activity-life-cycle)
4. [Broadcast Life Cycle](#broadcast-life-cycle)
5. [Case Study: Implementing Intent and Intent Filters](#case-study-implementing-intent-and-intent-filters)
6. [Modern Developments and Future Directions](#modern-developments-and-future-directions)
7. [Conclusion](#conclusion)
8. [Further Reading](#further-reading)

## **Introduction to Intent and Intent Filters**

In the context of Android application development, an **intent** is a message that requests an action from an application component. Intents are used to start a new activity, send data, or perform a specific task. Intent filters are used to filter the intents that an activity or broadcast receiver can handle. In this chapter, we will explore the concept of intents and intent filters in depth.

### Historical Context

The concept of intents was introduced in Android 1.5 (Cupcake) as a way to decouple the components of an application and allow them to communicate with each other. Intents have been an essential part of the Android API ever since.

### Modern Developments

In recent years, the Android API has introduced new concepts such as **intent filters** and **action intent filters**. Intent filters allow applications to filter the intents that they can handle, which helps to improve security and reduce the number of unintended intent handlers.

## **Intent Filters**

An **intent filter** is a mechanism that allows an application component to declare which intents it can handle. Intent filters are used to filter the intents that an activity or broadcast receiver can handle.

### Types of Intent Filters

There are two types of intent filters:

- **Action intent filters**: These filters specify the actions that an application component can perform. For example, a camera application might declare an action intent filter to handle the `android.intent.action.CAMERA_OPEN` intent.
- **Data intent filters**: These filters specify the data types that an application component can handle. For example, a messaging application might declare a data intent filter to handle `text/plain` data.

### Declaring Intent Filters

Intent filters can be declared using the following syntax:

```xml
<intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <data android:scheme="http" android:host="www.example.com" />
</intent-filter>
```

In this example, the `intent-filter` element specifies that the application component can handle the `android.intent.action.VIEW` action, the `android.intent.category.DEFAULT` category, and `http` scheme data.

## **Activity Life Cycle**

An **activity life cycle** refers to the sequence of events that an activity goes through when it is created, started, and stopped. The activity life cycle consists of several phases:

- **onCreate**: Called when the activity is created.
- **onStart**: Called when the activity starts.
- **onResume**: Called when the activity becomes visible.
- **onPause**: Called when the activity is paused.
- **onStop**: Called when the activity is stopped.
- **onDestroy**: Called when the activity is destroyed.

### Activity Life Cycle Methods

The following methods are used to manage the activity life cycle:

```java
public void onCreate(Bundle savedInstanceState) {
    // Called when the activity is created
}

public void onStart() {
    // Called when the activity starts
}

public void onResume() {
    // Called when the activity becomes visible
}

public void onPause() {
    // Called when the activity is paused
}

public void onStop() {
    // Called when the activity is stopped
}

public void onDestroy() {
    // Called when the activity is destroyed
}
```

## **Broadcast Life Cycle**

A **broadcast life cycle** refers to the sequence of events that a broadcast receiver goes through when it receives a broadcast. The broadcast life cycle consists of several phases:

- **onReceive**: Called when the broadcast receiver receives the broadcast.
- **onStart**: Called when the broadcast receiver starts.
- **onStop**: Called when the broadcast receiver stops.

### Broadcast Life Cycle Methods

The following methods are used to manage the broadcast life cycle:

```java
public void onReceive(Context context, Intent intent) {
    // Called when the broadcast receiver receives the broadcast
}

public void onStart() {
    // Called when the broadcast receiver starts
}

public void onStop() {
    // Called when the broadcast receiver stops
}
```

## **Case Study: Implementing Intent and Intent Filters**

In this case study, we will create a simple Android application that uses intent filters to handle camera intent and display the captured image.

### CameraActivity.java

```java
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

public class CameraActivity extends AppCompatActivity {

    private Button captureButton;
    private ImageView imageView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera);

        captureButton = findViewById(R.id.capture_button);
        imageView = findViewById(R.id.image_view);

        captureButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent("android.intent.action.CAMERA_OPEN");
                intent.addCategory("android.intent.category.DEFAULT");
                intent.putExtra("android.intent.extras.CAMERA_FACING", 0);
                intent.putExtra("android.intent.extras.LENS_FACING", 0);
                startActivity(intent);
            }
        });
    }
}
```

### activity_camera.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <Button
        android:id="@+id/capture_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Capture" />

    <ImageView
        android:id="@+id/image_view"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

</LinearLayout>
```

In this case study, we declare an intent filter in the `CameraActivity` class to handle the `android.intent.action.CAMERA_OPEN` action. We also specify the `android.intent.category.DEFAULT` category and add camera extras to the intent.

## **Modern Developments and Future Directions**

The concept of intents and intent filters has been an essential part of the Android API since its introduction in Android 1.5. In recent years, the Android API has introduced new concepts such as **action intent filters** and **data intent filters**, which allow applications to filter the intents that they can handle.

The future of intents and intent filters will likely involve the development of more advanced filtering mechanisms, such as machine learning-based intent filtering, and the integration of intents with other Android APIs, such as the `ContentResolver` and the `PackageManager`.

## **Conclusion**

In this chapter, we have explored the concept of intents and intent filters in Android application development. We have discussed the historical context of intents, the types of intent filters, and the activity and broadcast life cycles. We have also presented a case study on implementing intent and intent filters in a simple Android application.

## **Further Reading**

- [Android Developers: Intents](https://developer.android.com/training/basics/intents)
- [Android Developers: Intent Filters](https://developer.android.com/guide/topics/intents/intents-filters)
- [Android Developers: Activity Life Cycle](https://developer.android.com/guide/components/activity)
- [Android Developers: Broadcast Life Cycle](https://developer.android.com/guide/components/broadcasts)
- [Android Developers: Action Intent Filters](https://developer.android.com/reference/android/content/Intent#ACTION_*)
- [Android Developers: Data Intent Filters](https://developer.android.com/reference/android/content/Intent#DATA_*)
- [Android Developers: Camera API](https://developer.android.com/reference/android/hardware/Camera)
