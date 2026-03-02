# Interaction in Computer Graphics - Summary

## Key Definitions

- **Event-Driven Model**: A programming paradigm where application flow is determined by user actions (events) rather than predetermined sequences
- **Event Loop**: The continuous cycle that checks for and processes user input events in an interactive application
- **Callback**: A function registered with the graphics system that is automatically invoked when specific events occur
- **Picking**: The process of identifying which graphical object is under a specific screen coordinate
- **Rubber-banding**: A visual feedback technique displaying temporary shapes during drag operations
- **Coordinate Transformation**: Converting coordinates between different coordinate systems (screen, window, world, NDC)

## Important Formulas

- **Screen to NDC Conversion**: `ndc_x = (2 × screen_x / window_width) - 1`, `ndc_y = 1 - (2 × screen_y / window_height)`
- **World to Screen Conversion**: Applies inverse of viewport and projection transformations
- **Drag Offset Calculation**: `offset_x = mouse_x - object_x`, `offset_y = mouse_y - object_y`

## Key Points

1. Interactive computer graphics relies on the event-driven model where applications respond to user inputs through registered callbacks

2. The event loop continuously polls for events, dispatches them to handlers, and triggers display updates as needed

3. Different input devices (mouse, keyboard, tablet) generate distinct event types that graphics systems must handle appropriately

4. Coordinate systems in graphics range from pixel-based screen coordinates to abstract world coordinates, requiring proper transformation

5. Picking can be implemented through color-based rendering to off-screen buffers or through geometric intersection tests

6. The three-state drag model (idle → dragging → dropped) is fundamental to implementing object manipulation

7. Proper interaction design considers responsiveness, visual feedback, and intuitive mapping between input and output

8. Interaction techniques like snapping, constraint solving, and gesture recognition enhance user productivity

## Common Mistakes

1. **Confusing coordinate systems**: Failing to account for origin differences (top-left vs. bottom-left) between screen and world coordinates

2. **Ignoring coordinate transformation**: Attempting to use screen coordinates directly for world-space operations without proper conversion

3. **State management errors**: Forgetting to reset drag state on mouse release, causing unexpected behavior in subsequent interactions

4. **Inadequate input validation**: Not checking bounds or validating input before using coordinates in picking or transformation operations

5. **Callback timing assumptions**: Assuming callbacks execute in a particular order or that display updates occur immediately after event handling