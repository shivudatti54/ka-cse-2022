# Event-Driven Programming and Input Handling - Summary

## Key Definitions and Concepts

- **Event**: An object representing an action or occurrence (click, keypress, mouse movement) that the program must respond to
- **Event Source**: The component on which the event initially occurred (button, text field, frame)
- **Event Listener**: An interface that defines methods to handle specific event types
- **Delegation Event Model**: Java's event handling architecture where sources delegate events to registered listeners

## Important Formulas and Theorems

- Event handling follows: Source generates EventObject → Delegates to Listener → Listener executes handler method
- Listener registration: `add<Type>Listener()` methods establish source-listener relationships
- Event class hierarchy: `AWTEvent` → `ActionEvent`, `MouseEvent`, `KeyEvent`, `WindowEvent`

## Key Points

- All GUI components can be event sources; events are objects containing event-specific data
- ActionListener uses `actionPerformed(ActionEvent e)` method for button clicks and menu selections
- Mouse events: pressed, released, clicked, entered, exited, dragged, moved
- Key events: keyPressed, keyReleased, keyTyped - keyTyped provides character input
- Adapter classes provide empty implementations of listener interfaces for convenience
- The Event Dispatch Thread (EDT) handles all GUI events sequentially

## Common Mistakes to Avoid

- Forgetting to register listeners with `addXXXListener()` - the event will never be handled
- Implementing all methods of a listener interface when only some are needed (use adapters instead)
- Performing time-consuming operations on the EDT, which freezes the GUI
- Confusing mouse event methods - each has distinct behavior during user interaction

## Revision Tips

- Practice writing complete event-driven programs with multiple event types
- Remember that `getSource()` returns the component that generated the event
- Review adapter classes as they simplify listener implementation significantly
- Understand the difference between keyTyped (character) and keyPressed (virtual key code)
- Draw the event flow diagram: User Action → Event Object Creation → Listener Notification → Handler Execution
