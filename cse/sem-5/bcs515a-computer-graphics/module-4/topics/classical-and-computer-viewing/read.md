# Classical and Computer Viewing in Computer Graphics

## Introduction

Viewing transformations constitute a fundamental aspect of computer graphics that bridges the gap between three-dimensional object descriptions and their two-dimensional representation on output devices such as monitors and printers. The process of converting 3D world coordinates to 2D screen coordinates involves several mathematical transformations that simulate how cameras capture visual information. Understanding viewing transformations is essential for any computer graphics programmer or designer, as it forms the backbone of realistic image synthesis, virtual reality environments, CAD applications, and game development.

Classical viewing techniques, also known as classical projection theory, originated from engineering and architectural drawing practices developed over centuries. These techniques provide systematic methods for representing 3D objects on 2D planes while preserving certain geometric properties. Computer viewing, on the other hand, refers to the algorithmic implementation of these viewing concepts using matrix transformations and coordinate systems. The combination of classical projection theory with modern computational methods enables the creation of sophisticated visual representations that form the foundation of modern computer graphics systems.

The importance of viewing transformations extends beyond mere visualization. They determine how spatial relationships, depth perception, and perspective are conveyed to the viewer. Different viewing techniques serve different purposes: parallel projections are preferred for technical drawings where measurements must be accurate, while perspective projections create realistic images that mimic human visual perception. Mastery of these concepts is crucial for CSE students as they form the basis for advanced topics in computer graphics, animation, and virtual reality.

## Key Concepts

### Viewing Coordinate System

The viewing coordinate system, also called the camera coordinate system or eye coordinate system, is a fundamental concept in computer viewing. This coordinate system defines the position and orientation of the "camera" or viewer in 3D space. The viewing coordinate system consists of three mutually perpendicular vectors: the view plane normal (VPN), the view up vector (VUP), and the right vector (RIGHT). The origin of this system is called the view reference point (VRP), which represents the camera position in world coordinates.

The transformation from world coordinates to viewing coordinates involves a series of geometric transformations. First, the view reference point is translated to the origin. Then, the coordinate system is rotated so that the VPN aligns with the positive Z-axis, the RIGHT vector aligns with the positive X-axis, and the VUP vector aligns with the positive Y-axis. This transformation is typically implemented using a 4×4 viewing transformation matrix that combines both translation and rotation operations.

### Window and Viewport

The window is a rectangular region defined in the viewing coordinate system that specifies which portion of the 3D scene is to be displayed. The window acts as a "clipping" mechanism, determining which objects or parts of objects are visible in the final image. Objects or parts of objects outside the window boundaries are clipped and not rendered. The window is defined by four boundary values: left, right, bottom, and top, which correspond to the x and y coordinates in the viewing coordinate system.

The viewport is the rectangular region on the output device (screen) where the final image is displayed. Like the window, the viewport is defined by four boundary values but these correspond to device coordinates rather than viewing coordinates. The relationship between the window and viewport determines how the 3D scene is mapped to the 2D screen. When the window and viewport have the same aspect ratio, the image is displayed without distortion. Different aspect ratios require appropriate scaling to prevent stretching or compression of the displayed image.

### Parallel Projection

Parallel projection is a viewing technique where projection lines (projectors) are parallel to each other and perpendicular to the projection plane. This projection method preserves parallel lines in the original object, meaning that parallel lines in the 3D scene remain parallel in the 2D projection. Parallel projections are extensively used in technical and engineering drawings because they allow accurate measurement of dimensions.

In orthographic projection, a specific type of parallel projection, the projection plane is perpendicular to the projection direction. Common orthographic projections include front view, top view, and side view. The projection equations for orthographic projection are straightforward: the x and y coordinates remain unchanged while the z coordinate is discarded or set to zero. Isometric projection is another important parallel projection where the projection plane is positioned such that all three coordinate axes appear equally foreshortened, creating a visually balanced representation of 3D objects.

### Perspective Projection

Perspective projection simulates the way human vision and cameras perceive the world. In this projection technique, objects farther from the viewer appear smaller than objects closer to the viewer. The projection lines converge at a point called the projection reference point (PRP) or center of projection, located at a finite distance from the projection plane. This creates the phenomenon of foreshortening, where parallel lines appear to converge in the distance.

The perspective projection transformation is more complex than parallel projection. The projection equations involve division by the depth (z-coordinate), which creates the characteristic perspective effects. The perspective transformation matrix introduces a perspective division that depends on the z-coordinate. Key parameters in perspective projection include the view distance (distance from the viewer to the projection plane) and the field of view (angle that determines how much of the scene is visible). Perspective projections are essential for creating realistic images, architectural visualizations, and immersive virtual environments.

### Clipping in Viewing

Clipping is a critical operation in the viewing pipeline that removes portions of objects that lie outside the viewing volume. The viewing volume, defined by the window (for 2D viewing) or a viewing frustum (for 3D perspective viewing), establishes the boundaries of visible space. Cohen-Sutherland clipping algorithm is a widely used method for line clipping against rectangular windows, while Sutherland-Hodgman algorithm handles polygon clipping.

In 3D viewing, clipping becomes more complex with perspective projections. The viewing frustum is a pyramid-shaped volume (or truncated pyramid for asymmetric cases) that extends from the center of projection to infinity. Objects outside this frustum are not visible and are discarded. Near clipping plane and far clipping plane parameters define the minimum and maximum distances from the viewer that are rendered, preventing division by zero errors in perspective calculations and limiting the rendering range.

## Examples

### Example 1: Parallel Projection Calculation

Given a 3D point P(4, 6, 8) and a parallel projection plane defined by z = 0 with projection direction along the negative z-axis, calculate the projected point P'.

**Solution:**

For orthographic parallel projection onto the xy-plane:

- The x-coordinate remains unchanged: x' = x = 4
- The y-coordinate remains unchanged: y' = y = 6
- The z-coordinate is discarded: z' = 0

Therefore, the projected point is P'(4, 6, 0).

### Example 2: Viewport Mapping

A rectangular window in viewing coordinates has boundaries: left = -2, right = 2, bottom = -1.5, top = 1.5. The viewport on the screen has boundaries: left = 0, right = 640, bottom = 0, height = 480. A point in the window is located at (1, 0.75). Calculate its viewport coordinates.

**Solution:**

First, calculate normalized device coordinates (NDC):

- NDC x = (1 - (-2)) / (2 - (-2)) = 3/4 = 0.75
- NDC y = (0.75 - (-1.5)) / (1.5 - (-1.5)) = 2.25/3 = 0.75

Now map to viewport coordinates:

- Viewport x = 0 + 0.75 × (640 - 0) = 0.75 × 640 = 480
- Viewport y = 0 + 0.75 × (480 - 0) = 0.75 × 480 = 360

The point maps to viewport coordinates (480, 360).

### Example 3: Perspective Projection Matrix

For a perspective projection with projection reference point at origin (0, 0, 0) and projection plane at z = d (where d < 0, in front of the viewer), derive the projected coordinates of a point P(x, y, z).

**Solution:**

Using similar triangles in the xz-plane:

- x' / d = x / z
- Therefore, x' = x × d / z

Similarly for y-coordinate:

- y' = y × d / z

The projected point is P'(xd/z, yd/z, d).

In homogeneous coordinates, this perspective transformation is represented by the matrix:

```
| 1 0 0 0 |
| 0 1 0 0 |
| 0 0 1 0 |
| 0 0 1/d 0 |
```

## Exam Tips

1. **Remember the viewing pipeline sequence**: The standard order is modeling transformation → viewing transformation → projection transformation → viewport transformation → device transformation. This sequence is frequently asked in exams.

2. **Distinguish between parallel and perspective projections**: Parallel projection maintains parallel lines and is used for technical drawings, while perspective projection creates realistic images with foreshortening. Know when to use each type.

3. **Understand the role of view reference point (VRP)**: The VRP is the origin of the viewing coordinate system and represents the camera position. It is a crucial parameter in the viewing transformation matrix.

4. **Window-to-viewport transformation formula**: Be prepared to write and apply the formula: x_viewport = (x_window - window_left) × (viewport_width / window_width) + viewport_left. A similar formula applies for y-coordinates.

5. **Know the difference between window and viewport**: The window is defined in viewing coordinates (world space after viewing transformation), while the viewport is defined in screen or device coordinates.

6. **Perspective projection creates a viewing frustum**: Remember that the viewing frustum in perspective projection is a truncated pyramid, with near and far clipping planes defining what is rendered.

7. **Homogeneous coordinates are essential**: Viewing and projection transformations are implemented using 4×4 homogeneous transformation matrices. Understand how the w-component affects the final coordinates through perspective division.

8. **Cohen-Sutherland algorithm for clipping**: This is an important algorithm that uses outcodes to efficiently determine whether line segments need clipping against a rectangular window.

9. **Parallel projection preserves parallelism**: This is a key property that distinguishes it from perspective projection and makes it suitable for engineering drawings where true dimensions must be maintained.

10. **Aspect ratio matching**: To prevent image distortion, the aspect ratio of the window should match the aspect ratio of the viewport. This is a common consideration in graphics programming questions.
