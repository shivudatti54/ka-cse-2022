# Module 2: Creating Your First Android Application

## Introduction

Welcome to the practical core of Android development. This module guides you through the process of creating, building, and running a simple "Hello World" application. This foundational exercise is crucial as it introduces you to the Android project structure, the core components of an app, and the development workflow using Android Studio, the official Integrated Development Environment (IDE).

## Core Concepts and Step-by-Step Guide

### 1. Setting Up the Development Environment

Before you begin, ensure you have **Android Studio** installed. It bundles the Android SDK (Software Development Kit), emulator, and all necessary tools. Create a new project by selecting "New Project" and choosing the "Empty Activity" template.

*   **Project Name:** `MyFirstApp` (or a name of your choice)
*   **Package Name:** Typically in the format `com.yourcompany.yourapp` (e.g., `com..myfirstapp`). This is a unique identifier on the Google Play Store.
*   **Save Location:** Choose a suitable directory on your machine.
*   **Language:** Select **Kotlin**. (While Java is also an option, Kotlin is now the modern and preferred language for Android development).
*   **Minimum SDK:** Select a version (e.g., API 24: Android 7.0 Nougat). This defines the oldest version of Android your app will support.

### 2. Understanding the Generated Project Structure

After creation, Android Studio generates a standard project structure. Key directories include:

*   `app/`: The most important folder, containing your application's code and resources.
    *   `manifests/AndroidManifest.xml`: A crucial file that describes essential information about your app to the Android system (e.g., its components, permissions).
    *   `java/`: Contains all your Kotlin (or Java) source code files.
    *   `res/` (Resources): Contains non-code resources like layouts, strings, and images.
        *   `layout/`: Holds XML files that define the UI. `activity_main.xml` is created by default.
        *   `values/`: Contains files like `strings.xml` for defining text strings, `colors.xml` for colors, and `themes.xml` for app themes.

### 3. The Main Components: Activity and Layout

An **Activity** is a single, focused thing a user can do. It's responsible for creating a window and managing the user interface (UI). Your app's `MainActivity.kt` is a subclass of the `AppCompatActivity` class.

The UI for an Activity is defined in a **Layout** file (XML). The default `activity_main.xml` uses a `ConstraintLayout` and contains a `TextView` widget.

**Example: `activity_main.xml` (Simplified)**