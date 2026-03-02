# The Swing Packages

## Overview

Swing functionality is organized into several packages with javax.swing as the main package containing core components, and additional packages for specialized features like borders, events, tables, trees, and text components. Understanding package organization helps locate and use appropriate classes for GUI development.

## Key Points

- **javax.swing**: Main package with core components (JButton, JLabel, JTextField, JFrame)
- **javax.swing.border**: Border classes for component decoration
- **javax.swing.event**: Swing-specific event classes and listeners
- **javax.swing.table**: Classes for JTable component (TableModel, TableColumn)
- **javax.swing.tree**: Classes for JTree component (TreeModel, TreeNode)
- **javax.swing.text**: Text editing components and document model
- **javax.swing.plaf**: Pluggable look-and-feel classes
- **javax.swing.undo**: Undo/redo functionality support

## Important Concepts

- Most commonly used classes in javax.swing package
- Package naming convention: javax vs java (extension vs core)
- Specialized packages for complex components
- Look-and-feel implementation in plaf subpackages
- Event classes specific to Swing in swing.event

## Notes

- Remember javax.swing is main package for core components
- For exams, know which package contains JButton, JLabel, JFrame
- Understand separation of concerns through package structure
