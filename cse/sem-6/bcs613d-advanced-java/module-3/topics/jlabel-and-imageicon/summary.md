# JLabel and ImageIcon

## Overview

JLabel displays non-editable text or images in Swing applications, serving as a simple component for showing information to users. ImageIcon loads and displays images in various formats (GIF, JPEG, PNG), and can be combined with JLabel to show both text and images simultaneously.

## Key Points

- **JLabel Constructors**: JLabel(String text), JLabel(Icon icon), JLabel(String, Icon, alignment)
- **setText()**: Change label text dynamically
- **setIcon()**: Set or change label icon
- **Alignment**: SwingConstants.LEFT, CENTER, RIGHT for text/icon positioning
- **ImageIcon**: Loads images from file path or URL
- **Image Formats**: Supports GIF, JPEG, PNG formats
- **Non-Editable**: Labels display information, users cannot edit content
- **Combined Display**: Can show text and icon together

## Important Concepts

- JLabel is passive component (no user interaction)
- ImageIcon simplifies image loading
- Alignment constants control positioning
- Use setHorizontalAlignment() and setVerticalAlignment()
- Labels useful for form field descriptions

## Notes

- Remember JLabel is for display only, not input
- For exams, know JLabel constructors and alignment constants
- Practice creating ImageIcon and adding to JLabel