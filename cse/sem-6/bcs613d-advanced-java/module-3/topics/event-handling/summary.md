# Event Handling in Swing

## Overview

Event handling in Swing uses the delegation event model where event sources generate events and event listeners receive and process them. This model separates UI components from business logic, enabling flexible and maintainable code through ActionListener, MouseListener, KeyListener, and other listener interfaces.

## Key Points

- **Delegation Event Model**: Events delegated from source to registered listeners
- **Event Sources**: Components like buttons, text fields that generate events
- **Event Listeners**: Interfaces like ActionListener, MouseListener for handling events
- **ActionListener**: Single method actionPerformed() for action events
- **MouseListener**: Methods for mouseClicked, mousePressed, mouseReleased, mouseEntered, mouseExited
- **KeyListener**: Methods for keyPressed, keyReleased, keyTyped
- **addActionListener()**: Register listener with component
- **Event Object**: Contains information about the event (source, type, data)

## Important Concepts

- Multiple listeners can register with single component
- Listener interfaces may have multiple methods (adapter classes help)
- Anonymous inner classes commonly used for event handlers
- Lambda expressions (Java 8+) simplify listener code
- Event dispatch thread handles all Swing events

## Notes

- Remember ActionListener has single method, MouseListener has five methods
- For exams, practice writing ActionListener implementations
- Know difference between ActionListener (button clicks) and MouseListener (mouse operations)
