# Menus in Computer Graphics - Summary

## Key Definitions

- **Menu:** A graphical user interface element that provides a list of options or commands from which users can make selections
- **Popup Menu:** A context-sensitive menu that appears at the cursor position when triggered, typically by right-clicking
- **Submenu:** A secondary menu that appears when selecting certain items in a parent menu, creating hierarchical organization
- **Callback Function:** A function executed in response to menu item selection, receiving an identifier for the chosen item

## Important Formulas

No specific mathematical formulas apply to this topic. The implementation relies on API function calls:

```
Menu Creation: glutCreateMenu(callback)
Menu Items: glutAddMenuEntry(name, value)
Submenus: glutAddSubMenu(name, submenuID)
Attachment: glutAttachMenu(button)
```

## Key Points

1. Menus provide structured user interface elements for accessing application commands in graphics programs

2. GLUT simplifies menu creation through a set of dedicated functions for creation, population, and attachment

3. Menu callbacks receive integer values enabling identification of selected options through switch statements

4. Submenus must be created before being added to parent menus using glutCreateMenu()

5. Menus can be attached to mouse buttons (typically right button) for popup activation

6. glutPostRedisplay() must be called after menu callbacks modify rendering parameters

7. Only one menu can be attached to a specific mouse button at a time

8. The menu system follows the event-driven programming paradigm common in graphics applications

## Common Mistakes

1. **Creating submenus after main menu:** Forgetting that submenus must exist (be created) before they can be added to parent menus, resulting in undefined behavior

2. **Missing glutPostRedisplay:** Modifying graphics state in menu callbacks without triggering display refresh, causing visual updates to not appear

3. **Incorrect callback parameter handling:** Not properly using the integer value passed to callbacks to determine which menu item was selected

4. **Attempting multiple menu attachments:** Trying to attach different menus to the same mouse button without first detaching the existing menu