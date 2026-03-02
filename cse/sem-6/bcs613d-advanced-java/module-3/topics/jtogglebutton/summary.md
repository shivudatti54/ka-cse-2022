# JToggleButton

## Overview

JToggleButton is a two-state button that remains pressed after being clicked, unlike regular JButton which returns to unpressed state. It serves as the base class for JCheckBox and JRadioButton, providing selected/unselected states with corresponding visual feedback.

## Key Points

- **Two States**: Selected (pressed) or deselected (unpressed)
- **Toggle Behavior**: Clicking alternates between states
- **isSelected()**: Returns true if button is selected
- **setSelected(boolean)**: Programmatically set button state
- **ItemListener**: Receives events when selection state changes
- **Base Class**: Parent of JCheckBox and JRadioButton
- **Visual Feedback**: Appears pressed when selected
- **ActionEvent**: Still generates action events like JButton

## Important Concepts

- State persists after click unlike regular button
- Use for on/off, yes/no binary choices
- ItemEvent provides old and new state information
- Can be grouped using ButtonGroup for radio behavior
- Selected state independent of enabled state

## Notes

- Remember JToggleButton maintains state, JButton doesn't
- For exams, know JCheckBox and JRadioButton extend JToggleButton
- Practice using ItemListener to detect state changes
