# Create the First Android Application - Summary

## Key Definitions and Concepts

- **Android Studio**: Official IDE for Android development with emulator, code editor, and debugger
- **AVD (Android Virtual Device)**: Software emulator for testing apps without physical hardware
- **APK (Android Package Kit)**: Compiled application file format for Android OS
- **MainActivity**: Entry point class for app execution (extends `AppCompatActivity`)
- **setContentView()**: Method linking Java/Kotlin code with XML layout
- **AndroidManifest.xml**: Configuration file declaring app components and permissions

## Important Formulas and Theorems

```xml
<!-- Basic View properties -->
android:layout_width="match_parent|wrap_content"
android:layout_height="match_parent|wrap_content"
```

```kotlin
// MainActivity.kt core structure
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)
}
```

## Key Points

1. **Project Creation Steps**: File → New Project → Empty Activity → Configure (Name, Package, Language, API Level)
2. **Critical Files**:
   - `app/src/main/res/layout/activity_main.xml` (UI Design)
   - `app/src/main/java/MainActivity.kt` (Business Logic)
   - `app/manifests/AndroidManifest.xml` (App Configuration)
3. **Build Process**: Code → Build Gradle → Generate APK → Run on AVD/Device
4. **XML Layout Fundamentals**: Views (UI elements) and ViewGroups (Layout containers)
5. **Lifecycle Methods**: `onCreate()` is first method called when activity starts
6. **Resource Identification**: `R.layout.activity_main` references XML layout files
7. **Emulator Configuration**: Minimum RAM 2GB, prefer API 28+ for modern development

## Common Mistakes to Avoid

1. **XML Typos**: Misspelling attributes like `android:text` vs `androod:text`
2. **Missing setContentView()**: Forgetting to link activity with layout file
3. **AVD Configuration Errors**: Selecting incompatible API levels for project settings
4. **Ignoring Logcat**: Not checking system logs for runtime errors

## Revision Tips

1. **Practice Workflow**: Create 3-4 test projects focusing on different API levels
2. **Diagram Relationships**: Draw connection between Java/Kotlin code, XML layouts, and manifest
3. **Lifecycle Cheat Sheet**: Memorize order of activity methods: onCreate() → onStart() → onResume()
4. **Use Official Docs**: Bookmark [developer.android.com](https://developer.android.com) for quick API reference
