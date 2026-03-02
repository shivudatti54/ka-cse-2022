# A Simple Swing Application in Java

## Introduction

Swing is part of the Java Foundation Classes (JFC) and provides a comprehensive set of GUI components for building desktop applications. Unlike its predecessor AWT (Abstract Window Toolkit), Swing offers platform-independent components with a pluggable look-and-feel architecture.

## Complete Example

```java
import javax.swing.*; // Core Swing components
import java.awt.*; // Layout managers and graphics
import java.awt.event.*; // Event handling interfaces

public class SimpleSwingApp extends JFrame implements ActionListener {

 // GUI Components
 private JButton clickButton;
 private JLabel statusLabel;
 private int clickCount = 0;

 // Constructor to initialize the GUI
 public SimpleSwingApp() {
 // Set frame properties
 setTitle("Simple Swing Application");
 setSize(400, 200);
 setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

 // Get content pane and set layout
 Container contentPane = getContentPane();
 contentPane.setLayout(new FlowLayout());

 // Create and configure components
 clickButton = new JButton("Click Me");
 statusLabel = new JLabel("Button clicked: 0 times");

 // Register event listener
 clickButton.addActionListener(this);

 // Add components to content pane
 contentPane.add(clickButton);
 contentPane.add(statusLabel);
 }

 // Handle button click events
 @Override
 public void actionPerformed(ActionEvent e) {
 if (e.getSource() == clickButton) {
 clickCount++;
 statusLabel.setText("Button clicked: " + clickCount + " times");
 }
 }

 // Main method - entry point
 public static void main(String[] args) {
 // Create instance on Event Dispatch Thread (EDT)
 SwingUtilities.invokeLater(() -> {
 SimpleSwingApp app = new SimpleSwingApp();
 app.setVisible(true);
 });
 }
}
```

## Step-by-Step Explanation

### 1. Import Statements

```java
import javax.swing.*; // All Swing components (JFrame, JButton, JLabel)
import java.awt.*; // Layout managers (FlowLayout) and Container class
import java.awt.event.*; // Event handling (ActionListener, ActionEvent)
```

### 2. Class Declaration

The class extends `JFrame` (top-level window) and implements `ActionListener` (interface for handling button clicks).

### 3. Component Initialization

Components are declared as instance variables to allow access across methods:

- `JButton`: Clickable button component
- `JLabel`: Text display component

### 4. Constructor Setup

The constructor performs essential initialization:

| Method                          | Purpose                                  |
| ------------------------------- | ---------------------------------------- |
| `setTitle(String)`              | Sets window title displayed in title bar |
| `setSize(width, height)`        | Sets frame dimensions in pixels          |
| `setDefaultCloseOperation(int)` | Defines close button behavior            |
| `getContentPane()`              | Returns container for adding components  |
| `setLayout(LayoutManager)`      | Specifies component arrangement          |

### 5. Event Handling

The `ActionListener` interface requires implementing the `actionPerformed(ActionEvent e)` method. This method executes when the button is clicked.

### 6. Event Dispatch Thread (EDT)

The `main` method uses `SwingUtilities.invokeLater()` to create and display the GUI on the EDT. This is crucial for thread safety in Swing applications.

## Key Swing Concepts

### JFrame Structure

A JFrame consists of multiple layers:

- **Root Pane**: Contains all other panels
- **Content Pane**: Where user components are added (default)
- **Glass Pane**: Overlay for event handling
- **Layered Pane**: Contains menu bar and content pane

### Layout Managers

The `FlowLayout` arranges components left-to-right, wrapping to next line when needed. Other layout managers include:

- `BorderLayout`: Five regions (North, South, East, West, Center)
- `GridLayout`: Rows and columns grid
- `GridBagLayout`: Flexible grid with constraints

### Default Close Operations

```java
JFrame.EXIT_ON_CLOSE // Terminates application (most common)
JFrame.HIDE_ON_CLOSE // Hides frame (default)
JFrame.DISPOSE_ON_CLOSE // Disposes frame resources
JFrame.DO_NOTHING_ON_CLOSE // Ignores close request
```

## Important Notes

1. **Thread Safety**: All Swing components must be created and modified on the EDT using `SwingUtilities.invokeLater()` or `invokeAndWait()`.

2. **Component Addition**: Components are added to the content pane, not directly to the JFrame (prior to Java 5). Modern Java allows direct `add()` calls that automatically delegate to the content pane.

3. **Pluggable Look-and-Feel**: Swing components use the platform's native look-and-feel by default, but this can be changed using `UIManager.setLookAndFeel()`.

4. **Lightweight Components**: Most Swing components are lightweight (drawn by Java), unlike AWT's heavyweight components that use native peer widgets.
