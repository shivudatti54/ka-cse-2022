# Components and Containers

## Overview

Swing architecture divides GUI elements into components (buttons, labels, text fields) and containers (frames, panels) that hold other components. Understanding the containment hierarchy and proper use of containers is essential for building organized, maintainable Swing applications.

## Key Points

- **Component**: Basic GUI element (JButton, JLabel, JTextField, JCheckBox)
- **Container**: Special component that can hold other components (JFrame, JPanel)
- **Top-Level Containers**: JFrame, JDialog, JApplet cannot be contained in other containers
- **Intermediate Containers**: JPanel, JScrollPane can contain and be contained
- **Content Pane**: Default container in JFrame where components are added
- **Containment Hierarchy**: Tree structure with frame at root
- **add() Method**: Adds component to container
- **Layout Manager**: Controls component positioning within container

## Important Concepts

- JFrame is top-level container
- JPanel is most common intermediate container
- Components added to content pane, not directly to JFrame
- Container manages layout of contained components
- Nested panels enable complex layouts

## Notes

- Remember distinction: components are GUI elements, containers hold components
- For exams, know top-level containers (JFrame, JDialog) vs intermediate (JPanel)
- Practice nesting panels for complex layouts
