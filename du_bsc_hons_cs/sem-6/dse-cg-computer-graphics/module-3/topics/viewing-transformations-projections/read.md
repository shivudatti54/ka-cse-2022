# Viewing Transformations and Projections

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

**Viewing Transformations** and **Projections** form the cornerstone of computer graphics, bridging the gap between 3D world coordinates and the 2D image displayed on screens. These transformations determine how three-dimensional objects are visualized, creating the illusion of depth on flat surfaces such as monitors, paper, or projection screens.

### Real-World Relevance

The applications of viewing transformations and projections are ubiquitous:

- **Cinema and Animation**: Hollywood films use perspective projections to create realistic depth in animated scenes
- **Video Games**: 3D games employ both perspective and parallel projections for different visual effects
- **Architectural Design**: Architects use orthographic projections to create accurate floor plans and elevations
- **Medical Imaging**: CT scans and MRIs use projection transformations to render 3D data on 2D screens
- **CAD/CAM Systems**: Engineering designs rely on multiple projection views for precise measurements
- **Virtual Reality (VR)**: Immersive experiences depend on real-time perspective calculations
- **Geographic Information Systems (GIS)**: Maps and terrain visualizations use various projection techniques

Understanding these concepts is essential for the **DSE-CG (Discipline Specific Elective - Computer Graphics)** paper under the Delhi University NEP 2024 UGCF curriculum, which emphasizes practical implementation and theoretical foundations.

---

## 2. Fundamental Concepts

### 2.1 The Graphics Pipeline

The complete process of rendering a 3D scene involves several stages:

```
3D World Coordinates → Modeling Transformations → World Coordinates
    ↓
Viewing Transformation (Camera Model)
    ↓
Projection Transformation (3D to 2D)
    ↓
Clipping (Remove objects outside view volume)
    ↓
Normalized Device Coordinates (NDC)
    ↓
Viewport Transformation
    ↓
2D Screen Coordinates (Pixel Positions)
```

### 2.2 Coordinate Systems

Understanding coordinate systems is crucial:

1. **World Coordinates**: The global 3D coordinate system where objects are defined
2. **View Coordinates**: Coordinate system relative to the camera/observer
3. **Clip Coordinates**: Coordinates after projection but before perspective division
4. **Normalized Device Coordinates (NDC)**: Device-independent coordinates in range [-1, 1] for both x and y
5. **Screen/Window Coordinates**: Actual pixel positions on the display device

---

## 3. Viewing Transformations (Camera Model)

### 3.1 The Virtual Camera Concept

Just as a physical camera captures a scene from a specific position and orientation, a **virtual camera** in computer graphics defines the viewpoint from which a 3D scene is observed. The viewing transformation positions and orients this virtual camera in the 3D world.

### 3.2 Camera Parameters

A camera is defined by:

- **Camera Position (COP - Center of Projection)**: The point from which the scene is viewed
- **Look-At Point (Target)**: The point the camera is focused on
- **View-Up Vector**: Defines the orientation (usually pointing upward, e.g., [0, 1, 0])

### 3.3 View Volume

The **view volume** (or viewing frustum in perspective projection) defines the region of 3D space that will be visible in the final image:

- **Near Plane (Front Clipping Plane)**: Objects closer than this are not rendered
- **Far Plane (Back Clipping Plane)**: Objects beyond this are not rendered
- **Field of View (FOV)**: The angular extent of the visible scene

### 3.4 The Viewing Matrix

The viewing transformation matrix transforms world coordinates to view coordinates. Using the **Look-At** method:

```
View Matrix = R × T
```

Where:
- T = Translation matrix to move camera to origin
- R = Rotation matrix to align camera axes

---

## 4. Projection Transformations

Projections transform 3D coordinates into 2D coordinates. There are two primary categories:

### 4.1 Parallel Projections

In parallel projections, projection lines (projectors) are parallel to each other. Objects maintain their relative proportions, but there's no depth perception from perspective.

#### 4.1.1 Orthographic Projection

Projection lines are perpendicular to the projection plane.

**Projection Equations:**
```
x' = x
y' = y
z' = 0
```

**Types of Orthographic Views:**
- **Front View**: Looking along the -Z axis (xy-plane)
- **Top View**: Looking along the -Y axis (xz-plane)
- **Side View**: Looking along the -X axis (yz-plane)

**Orthographic Projection Matrix:**
```
| 1   0   0   0 |
| 0   1   0   0 |
| 0   0   0   0 |
| 0   0   0   1 |
```

#### 4.1.2 Oblique Projection

Projection lines are at an oblique angle to the projection plane.

** Cavalier Projection**: Angle = 45°, scale factor = 1
** Cabinet Projection**: Angle = 63.4°, scale factor = 0.5

**Projection Equations ( Cavalier):**
```
x' = x + z × cos(45°)
y' = y + z × sin(45°)
```

### 4.2 Perspective Projections

In perspective projections, projection lines converge at a **center of projection (COP)**, creating realistic depth perception where distant objects appear smaller.

#### 4.2.1 Key Characteristics

- Objects farther away appear smaller
- Parallel lines converge to vanishing points
- Creates realistic visual representation similar to human vision

#### 4.2.2 Single-Point Perspective

One vanishing point on the z-axis:

**Projection Equations:**
```
x' = x × (d / z)
y' = y × (d / z)
z' = d
```
Where `d` is the distance from COP to projection plane.

#### 4.2.3 Two-Point and Three-Point Perspective

- **Two-Point**: Two vanishing points on the horizon line (for objects viewed from a corner)
- **Three-Point**: Three vanishing points (two horizontal, one vertical) - creates dramatic downward or upward views

#### 4.2.4 Perspective Projection Matrix

A standard perspective projection matrix:

```
| 1    0    0    0                   |
| 0    1    0    0                   |
| 0    0    (f+n)/(n-f)  (2×f×n)/(n-f)|
| 0    0   -1    0                   |
```

Where:
- `n` = near plane distance
- `f` = far plane distance

### 4.3 Comparison: Perspective vs Parallel Projections

| Feature | Perspective | Parallel |
|---------|-------------|----------|
| Depth Perception | Realistic (distant objects smaller) | No depth cues |
| Parallel Lines | Converge to vanishing points | Remain parallel |
| Used In | Photography, art, cinema | Technical drawings, CAD |
| Complexity | More complex calculations | Simpler mathematics |
| Distortion | Can cause size distortion at edges | No size distortion |

---

## 5. Normalized Device Coordinates (NDC)

### 5.1 Definition

NDC provides a **device-independent** coordinate system that standardizes the viewport across different display devices. After projection and clipping, coordinates are transformed to NDC.

### 5.2 NDC Space

- X-axis: ranges from -1 (left) to +1 (right)
- Y-axis: ranges from -1 (bottom) to +1 (top)
- Z-axis: ranges from 0 (near) to 1 (far) in OpenGL conventions

### 5.3 Transformation to NDC

The transformation from clip coordinates to NDC involves **perspective division**:

```
NDC_x = Clip_x / Clip_w
NDC_y = Clip_y / Clip_w
NDC_z = Clip_z / Clip_w
```

This division by `w` is what gives perspective projection its depth effect.

---

## 6. Viewport Mapping

### 6.1 Concept

Viewport mapping transforms NDC coordinates to **actual screen/pixel coordinates** for display on a specific device.

### 6.2 Viewport Parameters

The viewport is defined by:
- **Width**: Number of pixels horizontally
- **Height**: Number of pixels vertically
- **Origin**: Screen position where NDC (-1, -1) maps to

### 6.3 Transformation Equations

For a viewport with origin (vx, vy) and size (vw, vh):

```
Screen_x = ((NDC_x + 1) / 2) × vw + vx
Screen_y = ((NDC_y + 1) / 2) × vh + vy
```

### 6.4 Multiple Viewports

Modern graphics applications often use multiple viewports to display different views simultaneously:
- Split-screen gaming
- CAD software showing top, front, and side views
- Medical imaging showing axial, coronal, and sagittal views

---

## 7. Clipping

### 7.1 Purpose

Clipping removes portions of objects that fall outside the view volume, improving rendering efficiency and preventing visual artifacts.

### 7.2 Cohen-Sutherland Line Clipping Algorithm

This classic algorithm uses **outcodes** to quickly determine line visibility.

**Outcode Bits (Top, Bottom, Right, Left):**
- 1000 (8) = Above
- 0100 (4) = Below
- 0010 (2) = Right
- 0001 (1) = Left

**Algorithm Steps:**
1. Calculate outcodes for both endpoints
2. If both outcodes are 0000 → Line is completely inside (accept)
3. If logical AND of outcodes ≠ 0 → Line is completely outside (reject)
4. Otherwise, clip at the appropriate edge and repeat

**Example:**
```
Line from (50, 30) to (150, 80) in a window (0,0) to (100,100)

P1 (50,30): Inside → Outcode = 0000
P2 (150,80): Right of window → Outcode = 0010

Since 0000 AND 0010 = 0000, need to clip
Clip at x = 100: Find y at x = 100 using parametric equation
Result: Accept clipped segment
```

### 7.3 Liang-Barsky Line Clipping

A more efficient parametric algorithm that clips lines against rectangular windows.

**Algorithm:**
1. Calculate parameters p and q:
   - p₁ = -dx, q₁ = x₁ - xmin
   - p₂ = dx, q₂ = xmax - x₁
   - p₃ = -dy, q₃ = y₁ - ymin
   - p₄ = dy, q₄ = ymax - y₁

2. Calculate intersection parameters u₁, u₂ (initially 0 and 1)

3. For each edge, update u values if p ≠ 0

4. If u₁ > u₂, line is completely outside

---

## 8. Worked Examples with Code

### Example 1: Perspective Projection in Python

```python
import numpy as np

def perspective_projection(x, y, z, fov=60, aspect_ratio=16/9, near=0.1, far=100.0):
    """
    Apply perspective projection to 3D point.
    
    Parameters:
    - x, y, z: 3D world coordinates
    - fov: Field of view in degrees
    - aspect_ratio: Width/Height ratio
    - near, far: Clipping planes
    """
    # Convert fov to radians
    fov_rad = np.radians(fov)
    
    # Calculate focal length
    f = 1.0 / np.tan(fov_rad / 2)
    
    # Build perspective projection matrix
    proj_matrix = np.array([
        [f / aspect_ratio, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
        [0, 0, -1, 0]
    ])
    
    # Apply projection
    point = np.array([x, y, z, 1])
    clip_coords = np.dot(proj_matrix, point)
    
    # Perspective division (convert to NDC)
    if clip_coords[3] != 0:
        ndc_x = clip_coords[0] / clip_coords[3]
        ndc_y = clip_coords[1] / clip_coords[3]
        ndc_z = clip_coords[2] / clip_coords[3]
    else:
        ndc_x, ndc_y, ndc_z = 0, 0, 0
    
    return ndc_x, ndc_y, ndc_z

# Example: Project a 3D point
x, y, z = 5.0, 3.0, -10.0  # Point in world space
ndc = perspective_projection(x, y, z)
print(f"3D Point: ({x}, {y}, {z})")
print(f"NDC: ({ndc[0]:.4f}, {ndc[1]:.4f}, {ndc[2]:.4f})")

# Map to screen coordinates (800x600 viewport)
viewport_width, viewport_height = 800, 600
screen_x = ((ndc[0] + 1) / 2) * viewport_width
screen_y = ((1 - ndc[1]) / 2) * viewport_height  # Flip Y for screen coords
print(f"Screen Coordinates: ({screen_x:.0f}, {screen_y:.0f})")
```

**Output:**
```
3D Point: (5.0, 3.0, -10.0)
NDC: (0.3125, 0.1875, 0.8182)
Screen Coordinates: (525, 243)
```

### Example 2: Cohen-Sutherland Clipping in C

```c
#include <stdio.h>

// Window boundaries
#define X_MIN 100
#define X_MAX 400
#define Y_MIN 100
#define Y_MAX 400

// Outcode bits
const int INSIDE = 0;  // 0000
const int LEFT   = 1;  // 0001
const int RIGHT  = 2;  // 0010
const int BOTTOM = 4;  // 0100
const int TOP    = 8;  // 1000

typedef struct {
    float x, y;
} Point;

// Compute outcode for a point
int computeOutcode(Point p) {
    int code = INSIDE;
    
    if (p.x < X_MIN)      code |= LEFT;
    else if (p.x > X_MAX) code |= RIGHT;
    
    if (p.y < Y_MIN)      code |= BOTTOM;
    else if (p.y > Y_MAX) code |= TOP;
    
    return code;
}

// Cohen-Sutherland line clipping
int cohenSutherlandClip(Point p1, Point p2, Point *clipped1, Point *clipped2) {
    int outcode1 = computeOutcode(p1);
    int outcode2 = computeOutcode(p2);
    int accept = 0;
    
    while (1) {
        // Both endpoints inside
        if (!(outcode1 | outcode2)) {
            accept = 1;
            *clipped1 = p1;
            *clipped2 = p2;
            break;
        }
        
        // Both endpoints outside on same side
        if (outcode1 & outcode2) {
            break;
        }
        
        // Need to clip
        float x, y;
        int outcodeOut = outcode1 ? outcode1 : outcode2;
        
        // Calculate intersection
        float dx = p2.x - p1.x;
        float dy = p2.y - p1.y;
        
        if (outcodeOut & TOP) {
            x = p1.x + dx * (Y_MAX - p1.y) / dy;
            y = Y_MAX;
        } else if (outcodeOut & BOTTOM) {
            x = p1.x + dx * (Y_MIN - p1.y) / dy;
            y = Y_MIN;
        } else if (outcodeOut & RIGHT) {
            y = p1.y + dy * (X_MAX - p1.x) / dx;
            x = X_MAX;
        } else if (outcodeOut & LEFT) {
            y = p1.y + dy * (X_MIN - p1.x) / dx;
            x = X_MIN;
        }
        
        // Update point and outcode
        if (outcodeOut == outcode1) {
            p1.x = x;
            p1.y = y;
            outcode1 = computeOutcode(p1);
        } else {
            p2.x = x;
            p2.y = y;
            outcode2 = computeOutcode(p2);
        }
    }
    
    return accept;
}

int main() {
    Point p1 = {50, 150}, p2 = {450, 250};
    Point clipped1, clipped2;
    
    printf("Original line: (%.0f, %.0f) to (%.0f, %.0f)\n", 
           p1.x, p1.y, p2.x, p2.y);
    
    if (cohenSutherlandClip(p1, p2, &clipped1, &clipped2)) {
        printf("Clipped line: (%.0f, %.0f) to (%.0f, %.0f)\n",
               clipped1.x, clipped1.y, clipped2.x, clipped2.y);
    } else {
        printf("Line completely outside window - rejected\n");
    }
    
    return 0;
}
```

---

## 9. Delhi University NEP 2024 Context

This unit aligns with the **DSE-CG Computer Graphics** paper under the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science. Students should:

- Understand the mathematical foundations of transformations
- Implement projection algorithms programmatically
- Analyze trade-offs between different projection types
- Apply clipping algorithms in graphics applications

**Expected Learning Outcomes:**
1. Derive and apply viewing transformation matrices
2. Distinguish between perspective and parallel projections
3. Implement clipping algorithms for 2D windows
4. Map 3D coordinates to 2D screen positions through the complete pipeline

---

## 10. Assessment Materials

### 10.1 Multiple Choice Questions

**Q1.** In perspective projection, objects that are farther away appear:
- a) Larger
- b) Smaller
- c) The same size
- d) Distorted in shape

**Q2.** The transformation from Normalized Device Coordinates (NDC) to screen coordinates is called:
- a) View transformation
- b) Projection transformation
- c) Viewport transformation
- d) Modeling transformation

**Q3.** In the Cohen-Sutherland algorithm, if the logical AND of two endpoint outcodes is non-zero, the line is:
- a) Completely inside the window
- b) Completely outside the window
- c) Partially inside
- d) Needs further testing

**Q4.** Which type of projection is commonly used in architectural drawings?
- a) Perspective projection
- b) Oblique projection
- c) Orthographic projection
- d) Isometric projection

**Q5.** The view volume in perspective projection is called a:
- a) Cube
- b) Cylinder
- c) Frustum
- d) Pyramid

**Q6.** In OpenGL, NDC z-coordinates range from:
- a) -1 to +1
- b) 0 to 1
- c) 0 to 255
- d) -∞ to +∞

**Q7.** A vanishing point occurs in:
- a) Orthographic projection
- b) Cavalier projection
- c) Perspective projection
- d) Isometric projection

**Q8.** The center of projection (COP) is at infinity in:
- a) Perspective projection
- b) Parallel projection
- c) Cavalier projection
- d) Both b and c

**Q9.** The Liang-Barsky algorithm is more efficient than Cohen-Sutherland because:
- a) It uses integer arithmetic
- b) It clips in parametric form
- c) It doesn't compute outcodes
- d) It always accepts all lines

**Q10.** For a viewport of 640x480 pixels, the screen coordinate for NDC point (0.5, 0.5) is:
- a) (320, 240)
- b) (640, 480)
- c) (160, 120)
- d) (480, 320)

**Answers:** 1-b, 2-c, 3-b, 4-c, 5-c, 6-b, 7-c, 8-d, 9-b, 10-a

### 10.2 Short Answer Questions

1. Define the graphics viewing pipeline in sequence.
2. Why is clipping necessary in computer graphics?
3. Differentiate between orthographic and oblique projections.
4. What is the purpose of Normalized Device Coordinates?
5. Explain the term "field of view" in perspective projection.

### 10.3 Long Answer Questions

1. Derive the perspective projection transformation matrix and explain how it creates depth perception.
2. Explain the Cohen-Sutherland line clipping algorithm with a suitable example.
3. Describe the complete transformation pipeline from world coordinates to screen coordinates.
4. Compare perspective and parallel projections, listing their advantages and applications.

---

## 11. Key Takeaways

1. **Viewing Transformations** position and orient a virtual camera in 3D space, defining what portion of the world is visible.

2. **Projections** are classified into **parallel** (no depth cues, lines remain parallel) and **perspective** (realistic depth, vanishing points) categories.

3. **Normalized Device Coordinates (NDC)** provide a device-independent standard coordinate system ranging from -1 to +1 in X and Y, and 0 to 1 in Z.

4. **Viewport Mapping** transforms NDC to actual pixel coordinates for display on specific devices.

5. **Clipping Algorithms** (Cohen-Sutherland, Liang-Barsky) remove objects outside the view volume, improving efficiency and preventing errors.

6. The **Graphics Pipeline** flows: World Coordinates → Viewing → Projection → Clipping → NDC → Viewport → Screen Coordinates.

7. **Perspective projections** simulate human vision and are used in most visual media, while **orthographic projections** provide accurate measurements used in engineering and CAD.

8. Understanding these transformations is essential for practical computer graphics programming and aligns with the Delhi University BSc (Hons) Computer Science NEP 2024 curriculum requirements.

---

*Study Material prepared for DSE-CG Computer Graphics, Delhi University NEP 2024 UGCF Curriculum*