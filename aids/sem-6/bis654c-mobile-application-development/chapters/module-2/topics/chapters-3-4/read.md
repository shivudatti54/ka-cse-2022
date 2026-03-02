# **MOBILE APPLICATION DEVELOPMENT**

## **Module: Create the First Android Application: Directory Structure. Android User Interface**

## **Chapter 3: Directory Structure**

### Overview

In this chapter, we will explore the concept of directory structure in Android application development. A directory structure is a hierarchical organization of files and folders in an Android project. This structure helps in maintaining a clean and organized codebase, making it easier for developers to navigate and manage their code.

### Directory Hierarchy

The following is the standard directory hierarchy for an Android application:

- `app`: This is the top-level directory for the application.
  - `src`: This directory contains the source code for the application.
    - `main`: This directory contains the source code for the main application.
      - `java`: This directory contains the Java source code for the application.
      - `res`: This directory contains the resources for the application.
        - `layout`: This directory contains the layout files for the application.
        - `values`: This directory contains the values files for the application.
- `android`: This directory contains the Android-specific code for the application.
- `build.gradle`: This file contains the build configuration for the application.

### Directory Structure

The following is an example of a well-structured Android project directory:

```
myapp/
|---- app/
|    |---- src/
|    |    |---- main/
|    |    |    |---- java/
|    |    |    |    |---- com.example.myapp/
|    |    |    |    |    |---- MainActivity.java
|    |    |    |    |---- res/
|    |    |    |    |    |---- layout/
|    |    |    |    |    |    |---- activity_main.xml
|    |    |    |    |---- values/
|    |    |    |    |    |---- strings.xml
|    |---- android/
|    |    |---- build.gradle
|---- build.gradle
|---- settings.gradle
|---- gradle.properties
```

### Best Practices

- Keep the `app` directory at the top level.
- Use the `src` directory to contain the source code for the application.
- Use the `main` directory to contain the source code for the main application.
- Use the `java` directory to contain the Java source code for the application.
- Use the `res` directory to contain the resources for the application.
- Use the `layout` directory to contain the layout files for the application.
- Use the `values` directory to contain the values files for the application.

## **Chapter 4: Android User Interface**

### Overview

In this chapter, we will explore the concept of Android user interface (UI) and how to design and implement it in an Android application. The Android UI is the graphical representation of the application, and it is used to interact with the user.

### UI Components

The following are some of the basic UI components in Android:

- `TextView`: This component is used to display text to the user.
- `Button`: This component is used to provide a way for the user to interact with the application.
- `EditText`: This component is used to allow the user to enter text.
- `ImageView`: This component is used to display an image.
- `ListView`: This component is used to display a list of items.
- `GridLayout`: This component is used to display a grid of items.

### Designing the UI

The following are some best practices for designing the UI:

- Use a consistent layout throughout the application.
- Use a clear and simple layout for the main screen.
- Use a navigation bar or a tab bar to provide a way for the user to navigate between screens.
- Use icons and graphics to make the UI visually appealing.
- Use a consistent color scheme throughout the application.

### Implementing the UI

The following are some steps to implement the UI:

- Create a new layout file for each screen.
- Use XML to define the layout of the screen.
- Use Java to handle the logic for the screen.
- Use the `setContentView()` method to set the layout for the screen.

### Example

Here is an example of a simple Android application with a UI:

```xml
<!-- activity_main.xml -->
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="24sp" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Click me!" />

    <EditText
        android:id="@+id/editText"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

</LinearLayout>
```

```java
// MainActivity.java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
```

This is a basic example of a UI in Android. In a real-world application, you would use more complex layouts and design principles to create a visually appealing and user-friendly interface.
