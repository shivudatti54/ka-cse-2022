# Create the First Android Application

## Introduction

Creating your first Android application marks the beginning of hands-on mobile development. This process introduces you to Android Studio (the official IDE), project structure, and fundamental app components. A simple "Hello World" app demonstrates the relationship between Java/Kotlin code, XML layouts, and the Android operating system.

Mastering this process is critical because:

1. It establishes the **development workflow** (code → build → run → debug)
2. Introduces core Android architecture components
3. Provides a foundation for understanding advanced concepts like activities, intents, and lifecycle management

In industry, this basic app structure forms the skeleton for all professional Android apps, from utility tools to complex enterprise solutions.

## Key Concepts

### 1. Android Project Structure

```
app/
├── manifests/AndroidManifest.xml
├── java/ (package name)/MainActivity
├── res/
│ ├── layout/activity_main.xml
│ ├── values/strings.xml
│ └── drawable/ (images)
└── Gradle Scripts
```

- **AndroidManifest.xml**: Declares app components and permissions
- **MainActivity**: Entry point class extending `AppCompatActivity`
- **activity_main.xml**: Defines UI layout using XML
- **Gradle**: Build automation system managing dependencies

### 2. Core Components of a Screen

1. **Activity**: Java/Kotlin class managing UI and user interaction
2. **Layout**: XML file defining visual structure (Views and ViewGroups)
3. **Resources**: External elements like strings, images, and dimensions

### 3. Activity Lifecycle Basics

```java
public class MainActivity extends AppCompatActivity {
 @Override
 protected void onCreate(Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 setContentView(R.layout.activity_main); // Links XML to Activity
 }
}
```

### 4. View Hierarchy

- **ViewGroup** (Layouts): Container for other views (LinearLayout, RelativeLayout)
- **View**: UI elements (TextView, Button)
- **Attributes**: Define properties like `android:layout_width`, `android:text`

## Examples

### Example 1: Basic Hello World App

**Step 1:** Create New Project in Android Studio

- Select "Empty Activity" template
- Set minimum SDK (API 21: Lollipop recommended)

**Step 2:** Edit activity_main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
 xmlns:android="http://schemas.android.com/apk/res/android"
 android:layout_width="match_parent"
 android:layout_height="match_parent"
 android:gravity="center"
 android:orientation="vertical">

 <TextView
 android:id="@+id/textView"
 android:layout_width="wrap_content"
 android:layout_height="wrap_content"
 android:text="Hello Students!"
 android:textSize="24sp"/>
</LinearLayout>
```

**Step 3:** Run the Application

- Create AVD (Android Virtual Device) via AVD Manager
- Select device (Pixel 5 recommended) and API level
- Click Run (Shift+F10)

### Example 2: Interactive App with Button

**Step 1:** Add Button to XML

```xml
<Button
 android:id="@+id/btnClick"
 android:layout_width="wrap_content"
 android:layout_height="wrap_content"
 android:text="Show Message"
 android:layout_marginTop="16dp"/>
```

**Step 2:** Implement Click Handler in MainActivity

```java
public class MainActivity extends AppCompatActivity {
 private TextView textView;

 @Override
 protected void onCreate(Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 setContentView(R.layout.activity_main);

 textView = findViewById(R.id.textView);
 Button button = findViewById(R.id.btnClick);

 button.setOnClickListener(view -> {
 textView.setText("Welcome to Android Development!");
 });
 }
}
```

## Exam Tips

1. **Manifest File Importance**: Always mention `AndroidManifest.xml` when asked about app configuration - it declares activities, permissions, and app metadata.

2. **Layout Differences**:

- LinearLayout: Arranges views sequentially
- RelativeLayout: Positions views relative to parent/sibling views

3. **Activity Lifecycle**: Remember `onCreate()` is mandatory - it initializes UI and binds data.

4. **View Binding**: Use `findViewById()` to connect XML elements with Java code. Modern alternative: View Binding.

5. **Resource References**: Always use `@string/` for text values (never hardcode strings in XML).

6. **Common Errors**:

- Forgetting to call `setContentView()`
- Mismatched IDs in XML and Java code
- Not declaring Activity in Manifest

7. **Emulator Setup**: Know AVD configuration steps - device profile, system image, and hardware acceleration requirements.
