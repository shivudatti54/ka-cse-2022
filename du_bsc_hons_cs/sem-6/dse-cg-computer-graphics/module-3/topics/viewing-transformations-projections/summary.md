# Viewing Transformations & Projections

## Introduction

Viewing transformations and projections are fundamental concepts in computer graphics that transform 3D world coordinates into 2D screen coordinates for display. These techniques form the viewing pipeline, essential for rendering scenes from any perspective on output devices.

---

## Key Concepts

### 1. Viewing Transformation Pipeline
- **World Coordinates** → **Viewing Coordinates** → **Projection Coordinates** → **Device Coordinates**
- Establishes the camera position and orientation in 3D space
- Defines the view volume (region of space visible to the camera)

### 2. Viewing Parameters
- **View Reference Point (VRP)**: Origin of viewing coordinate system
- **View Plane Normal (VPN)**: Perpendicular to viewing plane
- **View Up Vector (VUP)**: Defines "up" direction
- **Window**: 2D rectangular region in view plane
- **Viewport**: Rectangular region on output device for display

### 3. Parallel Projections
- Lines remain parallel; no depth perception
- **Orthographic Projection**: Projection lines perpendicular to projection plane
- **Oblique Projection**: Projection lines at oblique angles
  - Cavalier (45°, full depth)
  - Cabinet (63.4°, half depth)
- Preserves relative proportions; used in engineering drawings

### 4. Perspective Projections
- Lines converge to vanishing points; creates depth perception
- **One-Point Perspective**: One vanishing point (objects face viewer)
- **Two-Point Perspective**: Two vanishing points (corner view)
- **Three-Point Perspective**: Three vanishing points (bird's eye/worm's eye view)
- Mimics human visual system; realistic rendering

### 5. Projection Equations
- **Perspective Projection Matrix**:
  - x' = x/z, y' = y/z (division by depth)
  - f = focal length/distance from viewer
- **Parallel Projection**: x' = x, y' = y (no depth division)

### 6. Clipping Operations
- Remove objects outside view volume
- **Cohen-Sutherland Line Clipping Algorithm**
- **Sutherland-Hodgman Polygon Clipping**

---

## Exam Tips

- Remember the viewing pipeline sequence
- Distinguish between parallel and perspective projections
- Know that perspective projections involve division by z-coordinate
- Vanishing points differentiate perspective types

---

## Conclusion

Mastering viewing transformations and projections enables realistic 3D scene rendering on 2D displays. These concepts are crucial for understanding camera models, rendering pipelines, and visual fidelity in computer graphics applications.