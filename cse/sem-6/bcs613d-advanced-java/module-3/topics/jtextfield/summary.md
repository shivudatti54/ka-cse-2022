# JTextField

## Overview

JTextField is a single-line text input component allowing users to enter and edit text. It generates ActionEvent when Enter key is pressed and supports text selection, copying, pasting, and programmatic text manipulation through various methods.

## Key Points

- **Constructor**: JTextField(), JTextField(int columns), JTextField(String text, int columns)
- **getText()**: Retrieve current text content
- **setText(String)**: Set text content programmatically
- **addActionListener()**: Handle Enter key press events
- **setEditable(boolean)**: Make field read-only or editable
- **setColumns(int)**: Set preferred width in columns
- **Document Model**: Underlying model for text content
- **Selection Methods**: select(), selectAll(), getSelectedText()

## Important Concepts

- Single-line text input only
- Enter key generates ActionEvent
- Default 0 columns if not specified
- Editable vs enabled: editable affects text entry, enabled affects all interaction
- Use JTextArea for multi-line text input

## Notes

- Remember JTextField is single-line, JTextArea is multi-line
- For exams, know how to retrieve text using getText() method
- Practice adding ActionListener to handle Enter key