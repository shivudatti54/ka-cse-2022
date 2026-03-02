# Two Key Swing Features - Summary

## Key Definitions and Concepts

- **Swing**: Lightweight GUI widget toolkit for Java using AWT infrastructure
- **Delegation Event Model**: Event handling mechanism using _event sources_ and _event listeners_
- **MVC Architecture**: Separation of data (Model), presentation (View), and control logic (Controller)
- **Pluggable Look & Feel**: Ability to change UI appearance without code changes
- **Event Source**: Component generating events (e.g., `JButton`)
- **Event Listener**: Object receiving and processing events (e.g., `ActionListener`)
- **Swing Thread Safety**: GUI updates must use `EventQueue.invokeLater()`

## Important Formulas and Theorems

```java
// Event Handling Pattern
component.addActionListener(new ActionListener() {
    public void actionPerformed(ActionEvent e) {
        // Handle event
    }
});

// MVC Relationships
Model ↔ Controller ↔ View
View observes Model changes

// Thread-Safe GUI Update
EventQueue.invokeLater(() -> {
    component.setVisible(true);
});
```

## Key Points

1. **Event-Driven Architecture**:
   - Uses _event sources_ and _listeners_ instead of procedural flow
   - 3-part handling: Event Source → Event Object → Event Listener
   - Common listeners: `ActionListener`, `MouseListener`, `KeyListener`

2. **MVC Implementation**:
   - **Model**: Data structure (e.g., `DefaultListModel`)
   - **View**: Visual representation (e.g., `JList`)
   - **Controller**: Event handlers modifying Model/View
   - Enables independent component updates

3. **Pluggable Look & Feel**:
   - Change UI theme via `UIManager.setLookAndFeel()`
   - Built-in options: Metal (default), Nimbus, System, Motif
   - Maintains consistent functionality across themes

4. **Lightweight Components**:
   - Swing components (J-prefix) don't rely on native peers
   - Custom painting via `paintComponent()` method
   - Better performance than AWT heavyweights

5. **Thread Safety**:
   - Swing components are _not thread-safe_
   - Use `EventQueue.invokeLater()` for GUI updates from non-EDT threads

6. **Composite Design**:
   - Containers (e.g., `JPanel`) manage child components
   - Layout managers handle positioning (`FlowLayout`, `BorderLayout`)

7. **Observer Pattern**:
   - Views automatically update when Model changes
   - Implemented via `PropertyChangeListener`

## Common Mistakes to Avoid

1. **Mixing MVC Layers**:
   - Incorrect: Putting business logic in View components
   - Correct: Keep View for display only, Controller handles logic

2. **Thread Violations**:
   - Error: Updating GUI from background threads directly
   - Fix: Always use `EventQueue.invokeLater()`

3. **Overlooking Look & Feel**:
   - Mistake: Hardcoding component appearances
   - Better: Use `UIManager` defaults for theme consistency

4. **Memory Leaks**:
   - Error: Not removing listeners when components are disposed
   - Fix: Implement proper component lifecycle management

## Revision Tips

1. **Practice Event Flow**:
   - Diagram sequence: User action → Event generation → Listener invocation → Handler execution

2. **MVC Code Tracing**:
   - Study `JTable` with `TableModel` to see MVC in action
   - Note how data changes automatically refresh the view

3. **Theme Experimentation**:
   - Modify the Look & Feel in sample code:

   ```java
   UIManager.setLookAndFeel("javax.swing.plaf.nimbus.NimbusLookAndFeel");
   ```

4. **Thread Safety Drill**:
   - Create a button that updates a counter from a separate thread
   - Implement both incorrect and correct (EDT) versions

5. **Component Hierarchy**:
   - Memorize common container-component relationships:
     `JFrame` → `JPanel` → `JButton/JLabel/JTextField`
