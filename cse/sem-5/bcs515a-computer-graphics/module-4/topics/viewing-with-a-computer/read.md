# Viewing with a Computer

## Introduction

Viewing with a computer is a fundamental concept in computer graphics that deals with how objects and scenes are rendered on a display device. When we create graphics on a computer, we need a systematic way to transform the description of a scene into what the user sees on the screen. This process involves several mathematical transformations and pipeline stages that convert 3D world coordinates into 2D screen coordinates.

The viewing transformation is essential because it allows us to position the camera or observer at any location and point in any direction. Without proper viewing mechanisms, we would only be able to see objects from a fixed, predetermined perspective. In modern computer graphics applications ranging from video games to medical imaging, the ability to control the viewpoint is crucial for creating immersive and informative visualizations.

This topic covers the mathematical foundations of viewing, including the viewing pipeline, window-to-viewport transformations, clipping operations, and various projection methods. Understanding these concepts is essential for any computer graphics programmer or designer, as they form the backbone of how computers render visual content.

## Key Concepts

### The Viewing Pipeline

The viewing pipeline is a sequence of transformations that converts object coordinates to device coordinates (screen pixels). The pipeline consists of several stages:

1. **Modeling Transformation**: Objects are positioned in the world coordinate system using translation, rotation, and scaling.
2. **Viewing Transformation**: The scene is positioned relative to a camera or viewing reference frame.
3. **Projection Transformation**: 3D coordinates are projected onto a 2D projection plane.
4. **Viewport Transformation**: The projected coordinates are mapped to the physical display device.

The viewing transformation establishes a coordinate system called the viewing coordinate system or camera coordinate system. This system has its origin at the camera position, with the viewing direction along the negative z-axis.

### Camera Specifications

A camera in computer graphics is defined by several parameters:

- **View Reference Point (VRP)**: The origin of the viewing coordinate system, typically representing the camera position.
- **View Plane Normal (VPN)**: A vector indicating the direction of the viewing plane.
- **View Up Vector (VUP)**: A vector defining the upward direction on the viewing plane.
- **Projection Reference Point (PRP)**: The point from which projections are taken (for perspective projections).

These parameters define a viewing coordinate system using a transformation matrix that converts world coordinates to viewing coordinates.

### Window to Viewport Transformation

The window-to-viewport transformation is a 2D mapping that determines what portion of the world is displayed and how it fits on the screen. This transformation involves:

- **Window**: A rectangular region in world coordinates that defines the visible portion of the scene.
- **Viewport**: A rectangular region on the display device (screen) where the window contents are mapped.

The transformation equations are:

```
x_screen = (x_world - xw_min) * (xv_max - xv_min) / (xw_max - xw_min) + xv_min
y_screen = (y_world - yw_min) * (yv_max - yv_min) / (yw_max - yw_min) + yv_min
```

This allows graphics to be displayed at different sizes and positions on the screen while maintaining the relative proportions of the original scene.

### Clipping Operations

Clipping is the process of removing portions of objects that lie outside the viewing region. The clipping region is typically defined by the window boundaries. Several algorithms exist for clipping:

**Cohen-Sutherland Line Clipping**: Uses a 4-bit outcode to quickly determine whether lines are completely inside, completely outside, or require further processing.

**Liang-Barsky Line Clipping**: An efficient parametric line clipping algorithm that treats lines as parametric equations and calculates intersection parameters.

**Sutherland-Hodgman Polygon Clipping**: Clips polygons against each edge of the clipping window sequentially.

### Projection Transformations

Projections transform 3D coordinates into 2D coordinates. There are two main categories:

**Parallel Projection**: Lines remain parallel after projection. Includes:

- Orthographic projection: Projection lines are perpendicular to the projection plane
- Oblique projection: Projection lines are at an angle to the projection plane

**Perspective Projection**: Lines converge at a vanishing point, creating depth perception. Objects appear smaller as they get further from the viewer.

The perspective projection transformation matrix uses a homogeneous coordinate w-component to achieve the perspective divide:

```
x_projected = x / z
y_projected = y / z
```

This creates the characteristic foreshortening effect where distant objects appear smaller.

## Examples

### Example 1: Window to Viewport Transformation

**Problem**: A point P(15, 25) in world coordinates needs to be displayed. The window in world coordinates has corners at (0, 0) and (100, 100). The viewport on the screen has corners at (100, 100) and (400, 300). Find the screen coordinates.

**Solution**:

Given:

- World window: xw_min = 0, xw_max = 100, yw_min = 0, yw_max = 100
- Viewport: xv_min = 100, xv_max = 400, yv_min = 100, yv_max = 300
- Point: x_world = 15, y_world = 25

Calculate x_screen:

```
x_screen = (15 - 0) * (400 - 100) / (100 - 0) + 100
x_screen = 15 * 300 / 100 + 100
x_screen = 45 + 100 = 145
```

Calculate y_screen:

```
y_screen = (25 - 0) * (300 - 100) / (100 - 0) + 100
y_screen = 25 * 200 / 100 + 100
y_screen = 50 + 100 = 150
```

**Answer**: The screen coordinates are (145, 150)

### Example 2: Cohen-Sutherland Line Clipping

**Problem**: Using Cohen-Sutherland algorithm, determine if the line from A(10, 10) to B(90, 90) should be clipped, given a rectangular window from (20, 20) to (80, 80).

**Solution**:

**Step 1: Calculate outcodes**

For point A(10, 10):

- Left of window (x < 20): Yes → Bit 1 = 1
- Right of window (x > 80): No → Bit 2 = 0
- Below window (y < 20): Yes → Bit 3 = 1
- Above window (y > 80): No → Bit 4 = 0
- Outcode A: 1010 (binary)

For point B(90, 90):

- Left of window (x < 20): No → Bit 1 = 0
- Right of window (x > 80): Yes → Bit 2 = 1
- Below window (y < 20): No → Bit 3 = 0
- Above window (y > 80): Yes → Bit 4 = 1
- Outcode B: 0101 (binary)

**Step 2: Check for trivial acceptance or rejection**

- Both outcodes are 0000? No (both are non-zero)
- Bitwise AND of outcodes ≠ 0000? 1010 AND 0101 = 0000

Since the bitwise AND is 0000, the line is neither completely rejected nor completely accepted.

**Step 3: Clip the line**

Since we cannot trivially accept or reject, we need to clip. Using the first point's outcode (1010), we find the line intersects the left edge (x = 20).

Parameter t for intersection: t = (20 - 10) / (90 - 10) = 10/80 = 0.125
y at intersection: y = 10 + 0.125 × (90 - 10) = 10 + 10 = 20

New endpoint: (20, 20)

Now check again - both points are inside the window.

**Answer**: The line needs to be clipped and the portion from (10, 10) to (20, 20) is removed.

### Example 3: Perspective Projection

**Problem**: A point P(4, 6, 12) in 3D space is viewed from a projection reference point at (0, 0, 5). The projection plane is z = 0. Find the projected 2D coordinates.

**Solution**:

For perspective projection, we use similar triangles:

The distance from the projection reference point to the projection plane is: d = 5 - 0 = 5
The z-distance from the projection reference point to the point is: z' = 12 - 5 = 7

Using the perspective projection formula:

```
x' = x × (d / z') = 4 × (5/7) = 20/7 ≈ 2.857
y' = y × (d / z') = 6 × (5/7) = 30/7 ≈ 4.286
```

**Answer**: The projected 2D coordinates are approximately (2.86, 4.29)

## Exam Tips

1. **Remember the viewing pipeline order**: Modeling → Viewing → Projection → Viewport. This sequence is crucial for understanding how transformations are applied.

2. **Know the difference between parallel and perspective projections**: Parallel maintains parallel lines and has no depth perception, while perspective creates convergence at vanishing points and provides depth cues.

3. **Practice window-to-viewport calculations**: This is a common exam problem. Remember the scaling factors and offset additions.

4. **Cohen-Sutherland outcodes**: Know the bit assignments (top, bottom, right, left) and remember to check trivial acceptance/rejection before computing intersections.

5. **Homogeneous coordinates**: Understand how the w-component in homogeneous coordinates enables perspective division and projection transformations.

6. **Clipping is essential**: Many exam questions involve clipping line segments against a rectangular window. Master both Cohen-Sutherland and Liang-Barsky algorithms.

7. **Camera parameters**: Remember the key viewing parameters: VRP (View Reference Point), VPN (View Plane Normal), VUP (View Up Vector), and PRP (Projection Reference Point).

8. **Aspect ratio consideration**: When mapping window to viewport, maintain aspect ratio to prevent distortion. Calculate appropriate window dimensions based on viewport aspect ratio.
