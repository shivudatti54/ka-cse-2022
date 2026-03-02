# The Swing Buttons - JButton

## Introduction

JButton is a fundamental Swing component that creates clickable buttons in Java GUI applications. As part of the javax.swing package, it represents an improved version of AWT's Button class with enhanced features and customization options.

In modern software development, JButton serves as the primary interaction mechanism between users and applications. Its importance lies in enabling event-driven programming through action listeners, making applications responsive to user inputs. Unlike AWT components, JButton supports icons, HTML formatting, and pluggable look-and-feel - key features that align with Swing's philosophy of lightweight, customizable components.

Mastering JButton is essential for building professional interfaces. From simple OK/Cancel dialogs to complex toolbars with image buttons, this component forms the basis of interactive elements in desktop applications. Understanding its event handling mechanism also provides foundation for working with other Swing components.

## Key Concepts

### 1. JButton Hierarchy

```
Component
 → Container
 → JComponent
 → AbstractButton
 → JButton
```

### 2. Constructors

```java
JButton() // Empty button
JButton(String text) // Text button
JButton(Icon icon) // Icon button
JButton(String text, Icon icon) // Combined
```

### 3. Essential Methods

```java
setText(String text)
getText()
setIcon(Icon icon)
setEnabled(boolean)
setMnemonic(int key) // Keyboard shortcut
setToolTipText(String)
addActionListener(ActionListener)
```

### 4. Event Handling

Uses ActionListener interface:

```java
button.addActionListener(new ActionListener() {
 public void actionPerformed(ActionEvent e) {
 // Handle click
 }
});
```

### 5. MVC Connection

JButton follows Model-View-Controller architecture:

- Model: ButtonModel interface tracks state
- View: UI delegate handles rendering
- Controller: ActionListener handles events

## Examples

### Example 1: Basic Button with Action

```java
import javax.swing.*;
import java.awt.event.*;

public class BasicButtonDemo {
 public static void main(String[] args) {
 JFrame frame = new JFrame("Button Demo");
 JButton btn = new JButton("Click Me!");

 btn.addActionListener(new ActionListener() {
 int clickCount = 0;
 public void actionPerformed(ActionEvent e) {
 JOptionPane.showMessageDialog(frame,
 "Clicked " + (++clickCount) + " times");
 }
 });

 frame.add(btn);
 frame.setSize(300, 200);
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 frame.setVisible(true);
 }
}
```

### Example 2: Button with Icon and Tooltip

```java
JButton downloadBtn = new JButton("Download",
 new ImageIcon("download.png"));
downloadBtn.setToolTipText("Click to download file");
downloadBtn.setMnemonic(KeyEvent.VK_D); // Alt+D shortcut

// Add to panel
JPanel panel = new JPanel();
panel.add(downloadBtn);
```

### Example 3: Multiple Buttons with Shared Listener

```java
JButton redBtn = new JButton("Red");
JButton blueBtn = new JButton("Blue");

ActionListener colorChanger = e -> {
 String cmd = e.getActionCommand();
 panel.setBackground(cmd.equals("Red") ? Color.RED : Color.BLUE);
};

redBtn.addActionListener(colorChanger);
blueBtn.addActionListener(colorChanger);
```

## Visual Elements

### Button States Diagram

A JButton has three visual states:

1. Normal (unpressed)
2. Rollover (mouse over)
3. Pressed (mouse down)

Use `setRolloverIcon()` and `setPressedIcon()` to customize these states.

### Component Hierarchy

A typical JButton container structure:

```
JFrame (Top-level container)
 → JPanel (Intermediate container)
 → JButton (Leaf component)
```

## Real-World Applications

1. Form submission buttons in data entry systems
2. Toolbar buttons with icons in IDEs
3. Game control panels
4. Dialog box actions (OK/Cancel/Apply)
5. Multi-step wizard navigation

## Exam Tips

1. **Constructor Chaining**: Remember JButton can be created with text, icon, or both
2. **Event Handling**: Always implement ActionListener for click events
3. **MVC Question**: Be prepared to explain JButton's Model-View-Controller architecture
4. **Method Naming**: Use correct method names - setText(), not setLabel()
5. **State Methods**: Know enable/disable methods: setEnabled(true/false)
6. **Keyboard Shortcuts**: Use setMnemonic() for Alt+key combinations
7. **Difference from AWT**: Swing's JButton supports icons vs AWT's text-only Button

**Common Questions:**

- Write code to create a button with icon and tooltip
- Explain event handling mechanism for JButton
- Differentiate between AWT Button and Swing JButton
- Demonstrate use of ActionListener with multiple buttons
- List methods available in AbstractButton class
