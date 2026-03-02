# The Swing Buttons - JButton - Summary

## Key Definitions and Concepts

- **JButton**: Swing's push-button component that triggers actions when clicked
- **ActionListener**: Interface with `actionPerformed()` method for handling button clicks
- **AbstractButton**: Base class for JButton providing common functionality (text, icons, events)
- **MVC Architecture**: Swing's Model-View-Controller design pattern separating data, presentation, and control
- **Pluggable Look & Feel**: Swing's ability to change component appearance without altering functionality
- **Mnemonics**: Keyboard shortcuts (e.g., Alt+C) for button activation

## Important Formulas and Theorems

```java
// Button Creation
JButton btn = new JButton();                   // Empty button
JButton btn = new JButton("Text");             // Text button
JButton btn = new JButton(icon);               // Icon button
JButton btn = new JButton("Text", icon);       // Combined

// Key Methods
btn.addActionListener(listener);               // Event handling
btn.setMnemonic(KeyEvent.VK_C);                // Set keyboard shortcut
btn.setToolTipText("Description");             // Hover text
btn.setEnabled(false);                         // Disable button
btn.setIcon(icon);                             // Change button icon
```

## Key Points

1. JButton inherits from AbstractButton (which extends JComponent)
2. Supports text, icons, or both with multiple layout configurations
3. Event handling requires implementing ActionListener interface
4. Buttons must be added to containers (JPanel/JFrame) using `add()`
5. Swing uses **Event Dispatch Thread (EDT)** for thread-safe GUI updates
6. MVC architecture separates:
   - Model (button state)
   - View (visual representation)
   - Controller (event handling)
7. Buttons can have rollover effects and disabled states
8. Unlike AWT Button, JButton supports HTML formatting and icons
9. Common parent containers: JFrame (window), JPanel (layout container)
10. Button customization through borders, colors, and fonts

## Common Mistakes to Avoid

1. Forgetting to add button to container (invisible buttons)
2. Performing long operations in ActionListener (blocks EDT)
3. Using multiple buttons with same ActionListener without `e.getSource()` check
4. Incorrect image paths for icons (use relative paths or resource loading)

```java
// Bad Practice (Blocking EDT)
button.addActionListener(e -> {
    try { Thread.sleep(5000); }  // Freezes UI
    catch (InterruptedException ex) {}
});

// Good Practice (Use SwingWorker)
button.addActionListener(e -> new SwingWorker<Void, Void>() {
    protected Void doInBackground() {
        // Long operation here
        return null;
    }
}.execute());
```

## Revision Tips

1. Practice writing complete button lifecycle code:
   - Create container
   - Instantiate button
   - Add to container
   - Attach ActionListener
2. Memorize common methods using mnemonics:
   - **S**etText(), **S**etIcon(), **A**ddActionListener()
3. Compare JButton vs AWT Button in table format:
   | Feature | JButton | AWT Button |
   |----------------|------------------|------------|
   | Icons | Supported | No |
   | HTML Text | Yes | No |
   | Look & Feel | Pluggable | System |
4. Review MVC implementation pattern using JButton's:
   - Model: ButtonModel interface
   - View: UI delegate
   - Controller: ActionListener
