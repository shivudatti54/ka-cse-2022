# Android Project Directory Structure - Summary

## Key Definitions and Concepts

- **AndroidManifest.xml**: Configuration file declaring app components, permissions, and metadata
- **Gradle**: Build automation system managing dependencies and build configurations
- **res/ directory**: Contains all non-code resources (layouts, strings, images)
- **APK**: Android Package file containing compiled code and resources
- **Build Variants**: Different versions of app (debug/release) with shared codebase

## Important Formulas and Theorems

```gradle
// Project-level build.gradle
classpath 'com.android.tools.build:gradle:x.x.x'

// App-level build.gradle
implementation 'androidx.core:core-ktx:1.7.0'
minSdk 21
targetSdk 33

// settings.gradle
include ':app', ':mylibrary'
```

## Key Points

1. **Core Directories**:
   - `app/manifests`: Contains AndroidManifest.xml
   - `app/java`: Java/Kotlin source code + test files
   - `app/res`: Resources organized in subdirectories (layout, values, drawable)

2. **Resource Types**:
   - `res/layout/`: XML UI definitions
   - `res/values/`: Strings, colors, styles
   - `res/drawable/`: Images and vector assets
   - `res/mipmap/`: Launcher icons

3. **Build System**:
   - Two `build.gradle` files: Project-level (global config) and App-level (module-specific)
   - `settings.gradle` defines included modules

4. **Testing Structure**:
   - `androidTest/` for instrumentation tests
   - `test/` for unit tests

5. **Gradle Wrapper**:
   - `gradle/wrapper/` ensures consistent build environment
   - Contains `gradle-wrapper.properties` specifying Gradle version

6. **Generated Files**:
   - `build/` contains auto-generated files (APKs, intermediates)
   - `R.java` auto-generated resource IDs (don't modify)

7. **Multi-module Projects**:
   - Each module has its own `build.gradle`
   - Common dependencies in project-level file

## Common Mistakes to Avoid

1. Modifying project-level `build.gradle` for app-specific dependencies
2. Placing Java/Kotlin files outside `java/` directory package structure
3. Using uppercase letters or spaces in resource names
4. Confusing `drawable/` (general images) with `mipmap/` (app icons)

## Revision Tips

1. **Visual Mapping**: Create a mind map of directory structure with key files
2. **Gradle Comparison**: Make table comparing project-level vs app-level build.gradle
3. **Resource Hierarchy**: Practice resource override hierarchy (e.g., how different density drawables work)
4. **Manifest Walkthrough**: Memorize essential manifest elements:
   ```xml
   <application>, <activity>, <intent-filter>, <uses-permission>
   ```
