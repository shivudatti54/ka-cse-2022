# Clipping Algorithms in Computer Graphics

## Introduction

Clipping is a fundamental operation in computer graphics that determines which portions of geometric primitives (points, lines, polygons) are visible within a specified region called the viewport or window. When we render a 3D scene onto a 2D screen or define a rectangular viewing region, not all objects or their parts are visible. Clipping eliminates the portions that fall outside the viewing area before the rasterization process, significantly improving rendering efficiency and preventing artifacts.

The importance of clipping in graphics systems cannot be overstated. Without clipping, rendering engines would waste computational resources processing pixels that will never be displayed. Additionally, clipping prevents undefined behavior that could occur when attempting to draw primitives outside the screen boundaries. In 's 2022 scheme, this topic covers both 2D and 3D clipping algorithms, with emphasis on line clipping and polygon clipping techniques that form the backbone of modern graphics pipelines.

## Key Concepts

### Viewport and Window

The clipping process operates within a defined region called the viewport - a rectangular area on the output device (screen) where the image is displayed. The corresponding region in world coordinates is called the window. The transformation from window to viewport coordinates involves scaling and translation, and clipping is performed in normalized device coordinates (NDC) before this transformation.

### Cohen-Sutherland Line Clipping Algorithm

The Cohen-Sutherland algorithm is the most widely taught line clipping method. It assigns 4-bit region codes to each endpoint of a line segment:

- Bit 1 (1000): Above the window (top)
- Bit 2 (0100): Below the window (bottom)
- Bit 3 (0010): Right of the window (right)
- Bit 4 (0001): Left of the window (left)

The algorithm follows these steps:

1. Compute region codes for both endpoints
2. If both codes are 0000, the line is completely inside (accept)
3. If the bitwise AND of codes is non-zero, the line is completely outside (reject)
4. Otherwise, compute intersection points with window boundaries and subdivide the line

### Liang-Barsky Line Clipping Algorithm

This is a parametric line clipping algorithm that is more efficient than Cohen-Sutherland, especially for rectangular windows. It represents the line as parametric equations:

- x = x1 + u(x2 - x1)
- y = y1 + u(y2 - y1)

where u ranges from 0 to 1. The algorithm calculates entry and exit parameters (u1 and u2) for the line against each boundary, updating them progressively. The line is visible if u1 < u2 and u2 ≥ 0 and u1 ≤ 1.

### Sutherland-Hodgman Polygon Clipping

This algorithm clips a polygon against one boundary edge at a time. For each edge of the clipping window, the algorithm examines each vertex of the polygon:

- If the vertex is inside the boundary, keep it
- If the vertex was outside but the previous vertex was inside, add the intersection point
- If the vertex was inside but the previous vertex was outside, add the intersection point
- If both are outside, add nothing

The output of each stage becomes the input for the next boundary, progressively clipping the polygon.

### Point Clipping

The simplest form of clipping checks if a point (x, y) lies within the window boundaries:

- xmin ≤ x ≤ xmax AND ymin ≤ y ≤ ymax
  If both conditions are satisfied, the point is displayed; otherwise, it is discarded.

### Text Clipping

Text clipping can be implemented in three ways:

- All-or-nothing clipping: Reject entire character strings outside the window
- Individual character clipping: Clip each character at window boundaries
- Stroke/waveform clipping: Clip at the pixel level for maximum precision

## Examples

### Example 1: Cohen-Sutherland Algorithm

**Problem:** Clip the line from P1(100, 50) to P2(200, 150) against window (xmin=120, ymin=80, xmax=180, ymax=120).

**Solution:**

- Window: left=120, right=180, bottom=80, top=120

**Step 1: Compute region codes**

- P1(100, 50): Left of window (bit 4=1) and below window (bit 2=1)
  Code: 0101 (binary) = 5 (decimal)
- P2(200, 150): Right of window (bit 3=1) and above window (bit 1=1)
  Code: 1010 (binary) = 10 (decimal)

**Step 2: Check trivial acceptance/rejection**

- Both codes = 0000? No
- AND of codes = 0101 AND 1010 = 0000? Yes! (No trivial rejection)

**Step 3: Calculate intersections**
Since neither trivial acceptance nor rejection applies, we need to compute intersections.

For P1 (code 0101 = below and left):

- Intersection with left edge (x=120): y = 50 + (120-100)/(200-100) × (150-50) = 50 + 0.2 × 100 = 70
- Since y=70 is below bottom (80), reject intersection
- Intersection with bottom edge (y=80): x = 100 + (80-50)/(150-50) × (200-100) = 100 + 0.3 × 100 = 130

New point: P1'(130, 80) — code 0000 (inside)
Now P1' to P2: 0000 to 1010 (inside to top-right)

Intersection with top edge (y=120): x = 100 + (120-50)/(150-50) × (200-100) = 100 + 0.7 × 100 = 170
Intersection with right edge (x=180): y = 50 + (180-100)/(200-100) × (150-50) = 50 + 0.8 × 100 = 130

Both intersections (170,120) and (180,130) are outside. Use (170,120).

**Result:** Clipped line from (130,80) to (170,120)

### Example 2: Liang-Barsky Algorithm

**Problem:** Clip line from (10, 30) to (50, 50) against window (20, 20, 40, 40).

**Solution:**

- x1=10, y1=30, x2=50, y2=50
- dx = 40, dy = 20
- p1 = -dx = -40, p2 = dx = 40, p3 = -dy = -20, p4 = dy = 20
- q1 = x1 - xmin = 10 - 20 = -10
- q2 = xmax - x1 = 40 - 10 = 30
- q3 = y1 - ymin = 30 - 20 = 10
- q4 = ymax - y1 = 40 - 30 = 10

**Calculate u1 and u2:**

- r1 = q1/p1 = -10/(-40) = 0.25
- r2 = q2/p2 = 30/40 = 0.75
- r3 = q3/p3 = 10/(-20) = -0.5
- r4 = q4/p4 = 10/20 = 0.5

For p1 (-40) < 0: u1 = max(0, r1) = max(0, 0.25) = 0.25
For p2 (40) > 0: u2 = min(1, r2) = min(1, 0.75) = 0.75
For p3 (-20) < 0: u1 = max(0.25, -0.5) = 0.25
For p4 (20) > 0: u2 = min(0.75, 0.5) = 0.5

Since u1 (0.25) < u2 (0.5), the line is visible.

**Calculate clipped endpoints:**

- x = 10 + 0.25 × 40 = 20
- y = 30 + 0.25 × 20 = 35
- x = 10 + 0.5 × 40 = 30
- y = 30 + 0.5 × 20 = 40

**Result:** Clipped line from (20, 35) to (30, 40)

### Example 3: Sutherland-Hodgman Polygon Clipping

**Problem:** Clip triangle with vertices (10,10), (30,5), (25,25) against window (15,15) to (35,35).

**Solution:**
**Step 1: Clip against left edge (x=15)**

- V1(10,10): Outside → V2(30,5): Inside → Add intersection
- Intersection: x=15, y = 10 + (15-10)/(30-10) × (5-10) = 10 + 0.25 × (-5) = 8.75
- V2(30,5): Inside → V3(25,25): Inside → Keep V2, V3
- V3(25,25): Inside → V1(10,10): Outside → Add intersection
- Intersection: x=15, y = 10 + (15-10)/(25-10) × (25-10) = 10 + 0.33 × 15 = 15

Output: (15, 8.75), (30, 5), (25, 25), (15, 15)

**Step 2: Clip against right edge (x=35)**
All points x ≤ 35, so keep all: (15, 8.75), (30, 5), (25, 25), (15, 15)

**Step 3: Clip against bottom edge (y=15)**

- Process similarly, keeping points above y=15

Final clipped polygon vertices approximately: (15, 15), (25, 25), (21.25, 15)

## Exam Tips

1. **Remember region code bits**: Top=1000, Bottom=0100, Right=0010, Left=0001 - this mnemonic "TRBL" (Top Right Bottom Left) helps in exams.

2. **Cohen-Sutherland conditions**: Both endpoints inside (0000,0000) = accept; both on same side = reject (AND ≠ 0).

3. **Liang-Barsky is parametric**: Unlike Cohen-Sutherland which computes geometric intersections, Liang-Barsky works with parameter u in range [0,1].

4. **Sutherland-Hodgman is iterative**: It clips against one boundary at a time, passing output to next stage - remember all four edges must be processed.

5. **Algorithm complexity**: Cohen-Sutherland is O(1) for simple cases but may iterate; Liang-Barsky is consistently efficient for lines; Sutherland-Hodgman is O(n) where n is vertices.

6. **3D clipping**: In 3D, clipping occurs against the view frustum (six planes), and homogeneous coordinates are often used.

7. **Cohen-Sutherland vs Liang-Barsky**: Cohen-Sutherland is easier to understand and implement; Liang-Barsky is more efficient for line clipping.

8. **Clipping before rasterization**: Clipping happens in the graphics pipeline BEFORE the conversion to pixels, saving computational work.

9. **Point clipping condition**: Simply check xmin ≤ x ≤ xmax AND ymin ≤ y ≤ ymax.

10. **Normalized Device Coordinates (NDC)**: Clipping is often performed in NDC space where coordinates are normalized to [-1,1] or [0,1].
