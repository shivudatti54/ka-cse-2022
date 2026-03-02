# Android User Interface (UI)

## Introduction
The User Interface (UI) is the bridge between your Android application and its users. A well-designed UI is crucial for a positive user experience. In Android, the UI is built using a hierarchy of `View` and `ViewGroup` objects. This module delves into the core components and principles that form the foundation of Android's UI system.

## Core Concepts

### 1. Views and ViewGroups
*   **View:** A `View` is the basic building block for UI components. It occupies a rectangular area on the screen and is responsible for drawing and event handling. Common examples are `TextView`, `Button`, `EditText`, and `ImageView`.
*   **ViewGroup:** A `ViewGroup` is a subclass of `View` that serves as an invisible container for other `View` and `ViewGroup` objects. It defines the layout properties for its children. Examples include `LinearLayout`, `ConstraintLayout`, and `RelativeLayout`.

Think of it as a tree structure: `ViewGroups` are the branches that hold the leaves (`Views`) and other branches.

### 2. Layouts
Layouts are `ViewGroups` that define the visual structure for your UI. Choosing the right layout is key to creating a responsive and efficient interface.

*   **LinearLayout:** Arranges its children in a single row (horizontal) or column (vertical). Uses `android:orientation` attribute.