# Interaction in Computer Graphics

## Introduction

Interaction in computer graphics refers to the mechanisms and techniques that enable users to communicate with graphical applications, manipulate visual objects, and control the rendering process in real-time. As computer graphics evolved from static pre-rendered images to dynamic, real-time visualizations, the need for robust interaction paradigms became paramount. Modern graphical applications—from CAD systems to video games—rely heavily on sophisticated interaction models that translate user inputs into visual feedback.

The foundation of interactive computer graphics lies in the event-driven programming model, where the program flow is determined by user actions (events) rather than a predetermined sequence of operations. This paradigm shift from procedural to event-driven programming revolutionized how graphical applications are developed, enabling the creation of responsive, user-friendly interfaces. Understanding interaction mechanisms is essential for any computer graphics practitioner, as it bridges the gap between static rendering and dynamic, immersive visual experiences.

This topic explores the fundamental concepts of interaction in computer graphics, including event handling, callback mechanisms, input device integration, and interaction techniques that enable users to effectively communicate with graphical systems.

## Key Concepts

### Event-Driven Model

The event-driven model forms the backbone of interactive computer graphics. In this model, the application enters an event loop (also called a message loop or main loop) that continuously checks for and processes user inputs. When an event occurs—such as a mouse click, keyboard press, or window resize—the system generates an event message that is dispatched to the appropriate handler.

The typical structure of an event-driven graphics application includes:

1. **Initialization**: Setting up the graphics context, creating windows, and registering callback functions
2. **Event Loop**: Continuously retrieving events from an event queue
3. **Event Dispatch**: Routing events to registered callback functions based on event type
4. **Rendering**: Updating the display based on changes caused by events

This model ensures that the application remains responsive to user input while efficiently managing system resources.

### Callback Mechanisms

Callbacks are functions that are registered with the graphics system and automatically invoked when specific events occur. This mechanism allows developers to specify custom behavior without modifying the core graphics library. The callback registration pattern typically follows this structure:

```
register_callback(event_type, handler_function)
```

When the specified event occurs, the graphics system calls the registered handler function, passing relevant event data (such as mouse coordinates, key codes, or window dimensions). This separation of event detection from event handling promotes modular code design and enables multiple independent components to respond to the same events.

### Input Devices and Event Types

Interactive graphics systems must support various input devices, each generating specific event types:

**Mouse Events:**

- Mouse move: Cursor position changes
- Mouse button press: Button depressed at specific coordinates
- Mouse button release: Button released at specific coordinates
- Mouse wheel: Scroll or zoom operations

**Keyboard Events:**

- Key press: Key depressed
- Key release: Key released
- Modifier keys: Shift, Ctrl, Alt states

**Window Events:**

- Expose: Window needs redrawing
- Resize: Window dimensions changed
- Focus: Window gained or lost input focus
- Close: Window close request

### Coordinate Systems in Interaction

Understanding coordinate systems is crucial for implementing proper interaction. Graphics applications typically use multiple coordinate systems:

1. **Screen Coordinates**: Origin at top-left corner of the display, measured in pixels
2. **Window Coordinates**: Origin at top-left corner of the application window
3. **World Coordinates**: The application's logical coordinate system, independent of screen resolution
4. **Normalized Device Coordinates (NDC)**: Device-independent coordinates in range [0,1] or [-1,1]

Transformations between these coordinate systems are essential for accurate mouse picking and object manipulation.

### Interaction Techniques

Several established techniques enable effective user interaction:

**Picking**: The process of identifying which graphical object is under the mouse cursor. Common methods include:

- Color picking: Rendering objects with unique colors to an off-screen buffer
- Geometric testing: Ray casting or bounding box intersection tests
- Ray tracing: Tracing rays from camera through cursor position

**Dragging**: Maintaining object selection while moving the mouse, enabling intuitive repositioning of graphical elements

**Rubber-banding**: Visual feedback technique showing a temporary shape (typically a rectangle or line) during drag operations

**Snapping**: Constraining movement to predefined grids or geometric relationships for precise input

## Examples

### Example 1: Simple Mouse Click Handler

Consider a basic implementation using a callback-based graphics library:

```c
// Structure to store point data
typedef struct {
 int x, y;
} Point;

// Global state
Point points[100];
int point_count = 0;

// Mouse button callback
void mouse_button_callback(int button, int state, int x, int y) {
 if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
 // Store clicked point
 if (point_count < 100) {
 points[point_count].x = x;
 points[point_count].y = y;
 point_count++;
 // Request display update
 glutPostRedisplay();
 }
 }
}

// Display callback
void display_callback(void) {
 glClear(GL_COLOR_BUFFER_BIT);

 // Draw all stored points
 glBegin(GL_POINTS);
 for (int i = 0; i < point_count; i++) {
 glVertex2i(points[i].x, points[i].y);
 }
 glEnd();

 glutSwapBuffers();
}

// Main function
int main(int argc, char** argv) {
 glutInit(&argc, argv);
 glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
 glutCreateWindow("Point Placement");

 glOrtho(0, 500, 0, 500, -1, 1);

 glutMouseFunc(mouse_button_callback);
 glutDisplayFunc(display_callback);

 glutMainLoop();
 return 0;
}
```

This example demonstrates the callback registration pattern where mouse and display callbacks are registered with GLUT, which invokes them automatically when events occur.

### Example 2: Implementing Object Dragging

```python
# Pseudocode for drag operation
class DraggableObject:
 def __init__(self, x, y, width, height):
 self.x = x
 self.y = y
 self.width = width
 self.height = height
 self.dragging = False
 self.drag_offset_x = 0
 self.drag_offset_y = 0

 def contains_point(self, px, py):
 return (self.x <= px <= self.x + self.width and
 self.y <= py <= self.y + self.height)

 def on_mouse_down(self, mouse_x, mouse_y):
 if self.contains_point(mouse_x, mouse_y):
 self.dragging = True
 self.drag_offset_x = mouse_x - self.x
 self.drag_offset_y = mouse_y - self.y
 return True
 return False

 def on_mouse_move(self, mouse_x, mouse_y):
 if self.dragging:
 self.x = mouse_x - self.drag_offset_x
 self.y = mouse_y - self.drag_offset_y
 return True
 return False

 def on_mouse_up(self):
 self.dragging = False
```

This example shows the three-state drag model: idle, dragging, and dropped. The offset calculation ensures smooth dragging without the object "jumping" to the cursor position.

### Example 3: Coordinate Transformation for Picking

```c
// Convert screen coordinates to world coordinates
void screen_to_world(int screen_x, int screen_y,
 int window_width, int window_height,
 float projection_matrix[16],
 float view_matrix[16],
 float *world_x, float *world_y) {

 // Normalize screen coordinates to NDC [-1, 1]
 float ndc_x = (2.0f * screen_x) / window_width - 1.0f;
 float ndc_y = 1.0f - (2.0f * screen_y) / window_height;

 // Apply inverse projection (simplified for orthographic)
 // In full implementation, this would involve matrix inversion

 *world_x = ndc_x; // Simplified for orthographic projection
 *world_y = ndc_y;
}

// Picking algorithm using geometric testing
bool pick_object(Object *objects, int num_objects,
 float pick_x, float pick_y) {
 for (int i = 0; i < num_objects; i++) {
 // Check if pick point is within object's bounding box
 if (objects[i].min_x <= pick_x && pick_x <= objects[i].max_x &&
 objects[i].min_y <= pick_y && pick_y <= objects[i].max_y) {
 return true; // Hit detected
 }
 }
 return false;
}
```

This example demonstrates coordinate transformation and geometric picking, essential techniques for determining which object the user has selected.

## Exam Tips

1. **Understand the Event Loop**: Be able to trace through a typical event loop and explain how events are processed, dispatched, and handled in a graphics application.

2. **Coordinate System Transformations**: Know how to convert between screen, window, world, and normalized device coordinates—this is frequently tested in exams.

3. **Callback Registration Pattern**: Understand how callbacks are registered and why this separation of concerns is important for modular graphics programming.

4. **Picking Techniques**: Be familiar with at least two picking methods (color picking, geometric testing) and know the advantages and disadvantages of each.

5. **State Management in Interaction**: Recognize that interaction often involves maintaining state (is a button pressed? is an object being dragged?) and understand how this state affects event handling.

6. **Event vs. Callback Models**: Understand the distinction between polling (continuously checking input state) and event-driven (responding to input events) approaches.

7. **Common Interaction Patterns**: Memorize standard interaction patterns like rubber-banding, snapping, and the three-state drag model, as these frequently appear in exam questions.
