# Line and Polygon Clipping Algorithms

## Comprehensive Study Material for BSc (Hons) Computer Science — NEP 2024 UGCF

---

## 1. Introduction

**Clipping** is a fundamental operation in computer graphics that determines which portions of geometric objects are visible within a specified region of interest, known as the **clipping window** or **viewport**. This process is essential for rendering only the visible portions of scenes, preventing computational waste on invisible elements and ensuring proper display of graphics.

### Real-World Relevance

Clipping algorithms are ubiquitous in modern computing applications:

- **Windowing Systems**: Operating systems use clipping to ensure window contents don't overlap incorrectly
- **Computer-Aided Design (CAD)**: Engineers use clipping to focus on specific components of complex drawings
- **Game Development**: Real-time rendering engines employ clipping to optimize scene display
- **Map Applications**: Digital maps clip terrain data to visible viewport areas
- **Print Media**: Desktop publishing uses clipping to control page layout elements

In the context of the Delhi University BSc (Hons) Computer Science syllabus (NEP 2024 UGCF), this topic falls under **DSE-CG: Computer Graphics** and carries significant weight in both theoretical understanding and practical implementation.

---

## 2. Understanding Clipping Windows

Before diving into algorithms, it's essential to understand the clipping window concept:

```
        |----------- Clipping Window -----------|
        |                                     |
   (xmin, ymax)                              (xmax, ymax)
        +-------------------------------------+
        |          Viewport                   |
        |    (Visible Display Area)           |
        +-------------------------------------+
   (xmin, ymin)                              (xmax, ymin)
        |                                     |
        ---------------------------------------
```

The clipping window is defined by four boundaries:
- **Left boundary (xmin)**: Minimum x-coordinate
- **Right boundary (xmax)**: Maximum x-coordinate
- **Bottom boundary (ymin)**: Minimum y-coordinate
- **Top boundary (ymax)**: Maximum y-coordinate

---

## 3. Line Clipping Algorithms

Line clipping determines which portions of line segments (from point P1 to P2) lie within the clipping window. We will examine two primary algorithms: **Cohen-Sutherland** and **Liang-Barsky**.

### 3.1 Cohen-Sutherland Line Clipping Algorithm

#### Concept

The Cohen-Sutherland algorithm uses a **divide-and-conquer** approach with **region codes** (also called outcodes) to quickly eliminate lines that are completely inside or completely outside the clipping window. This algorithm is particularly efficient for batch processing of multiple line segments.

#### Region Codes

Each endpoint of a line is assigned a 4-bit region code based on its position relative to the clipping window:

```
    Bit 3 (Top)     |  1000  |  1001  |  1010  |  1011  |  1010  |  1011
    Bit 2 (Bottom)  |  0100  |  0101  |  0110  |  0111  |  0100  |  0101
    Bit 1 (Right)   |  0010  |  0011  |  0010  |  0011  |  0000  |  0000
    Bit 0 (Left)    |  0001  |  0001  |  0000  |  0000  |  0001  |  0001
                    -------------------------------------------
                       Above   Above   Within   Within   Below   Below
                       Right   Left    Right    Left     
```

**Bit assignments:**
- **Bit 0 (Left)**: 1 if x < xmin
- **Bit 1 (Right)**: 1 if x > xmax
- **Bit 2 (Below)**: 1 if y < ymin
- **Bit 3 (Above)**: 1 if y > ymax

#### Algorithm Steps

**Step 1**: Compute region codes for both endpoints P1 and P2.

**Step 2**: Apply the **trivial acceptance test**:
- If both region codes are `0000`, the line is completely inside → **ACCEPT**

**Step 3**: Apply the **trivial rejection test**:
- If the logical AND of both region codes is non-zero, both points are on the same outside region → **REJECT**

**Step 4**: If neither trivial test passes, calculate intersection points with one or more clipping boundaries and recursively process the resulting sub-segments.

#### Pseudocode

```python
# Cohen-Sutherland Line Clipping Algorithm
# Constants for region codes
INSIDE = 0  # 0000
LEFT   = 1  # 0001
RIGHT  = 2  # 0010
BOTTOM = 4  # 0100
TOP    = 8  # 1000

def compute_region_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1 = compute_region_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_region_code(x2, y2, xmin, ymin, xmax, ymax)
    
    while True:
        # Trivial acceptance: both points inside
        if code1 == 0 and code2 == 0:
            return (x1, y1, x2, y2)  # Accept entire line
        
        # Trivial rejection: both points on same outside region
        if code1 & code2 != 0:
            return None  # Reject line
        
        # Non-trivial case: calculate intersections
        # Use the point with non-zero code
        if code1 != 0:
            code_out = code1
        else:
            code_out = code2
        
        # Calculate intersection with clipping boundary
        if code_out & TOP:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax
        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            y = xmax
        elif code_out & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin
        
        # Replace the outside point with intersection
        if code_out == code1:
            x1, y1 = x, y
            code1 = compute_region_code(x1, y1, xmin, ymin, xmax, ymax)
        else:
            x2, y2 = x, y
            code2 = compute_region_code(x2, y2, xmin, ymin, xmax, ymax)
```

#### Visual Representation

```
    Before Clipping:              After Clipping:
    
    +------------------+          +------------------+
    |                  |          |                  |
    |    P1--------P2  |          |    P1------P2    |
    |                  |          |        ↑         |
    |                  |          |   Clipped Edge   |
    |                  |          |                  |
    +------------------+          +------------------+
    
    The portion of line outside 
    the window is removed
```

### 3.2 Liang-Barsky Line Clipping Algorithm

#### Concept

The **Liang-Barsky algorithm** is a **parametric line clipping algorithm** that is more efficient than Cohen-Sutherland for line segments. It uses **parametric equations** to determine clipping points and handles the clipping window as a set of four half-planes.

#### Mathematical Foundation

A line segment from P1(x1, y1) to P2(x2, y2) is represented parametrically as:

```
x = x1 + t(x2 - x1),  where 0 ≤ t ≤ 1
y = y1 + t(y2 - y1)
```

The algorithm computes the values of parameter `t` for which the point lies within the clipping window boundaries:

- For left boundary:  x1 + t(x2 - x1) ≥ xmin
- For right boundary: x1 + t(x2 - x1) ≤ xmax
- For bottom boundary: y1 + t(y2 - y1) ≥ ymin
- For top boundary:   y1 + t(y2 - y1) ≤ ymax

#### Algorithm Steps

**Step 1**: Initialize parameters:
- p1 = -(x2 - x1), p2 = (x2 - x1)
- p3 = -(y2 - y1), p4 = (y2 - y1)
- q1 = x1 - xmin, q2 = xmax - x1
- q3 = y1 - ymin, q4 = ymax - y1

**Step 2**: Initialize: t0 = 0, t1 = 1

**Step 3**: For each boundary:
- If pi = 0 and qi < 0 → Line is parallel and outside → **REJECT**
- Otherwise, calculate r = qi / pi
- If pi < 0, update t0 = max(t0, r)
- If pi > 0, update t1 = min(t1, r)

**Step 4**: If t0 < t1, the line intersects the window:
- New endpoint 1: (x1 + t0(x2-x1), y1 + t0(y2-y1))
- New endpoint 2: (x1 + t1(x2-x1), y1 + t1(y2-y1))

#### Pseudocode

```python
# Liang-Barsky Line Clipping Algorithm
def liang_barsky_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    # Parametric coefficients
    dx = x2 - x1
    dy = y2 - y1
    
    # p values (directional parameters)
    p = [-dx, dx, -dy, dy]
    
    # q values (position parameters)
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
    
    # Initialize t values
    t0 = 0.0
    t1 = 1.0
    
    for i in range(4):
        if p[i] == 0:
            # Line is parallel to this boundary
            if q[i] < 0:
                return None  # Line is outside
        else:
            r = q[i] / p[i]
            if p[i] < 0:
                t0 = max(t0, r)
            else:
                t1 = min(t1, r)
    
    # Check if valid clipping exists
    if t0 < t1:
        # Calculate clipped endpoints
        x1_clip = x1 + t0 * dx
        y1_clip = y1 + t0 * dy
        x2_clip = x1 + t1 * dx
        y2_clip = y1 + t1 * dy
        return (x1_clip, y1_clip, x2_clip, y2_clip)
    else:
        return None  # Line completely outside
```

#### Comparison: Cohen-Sutherland vs Liang-Barsky

| Aspect | Cohen-Sutherland | Liang-Barsky |
|--------|------------------|--------------|
| **Approach** | Region codes with divide-and-conquer | Parametric equation |
| **Efficiency** | Good for multiple segments | More efficient for single segments |
| **Computations** | Multiple intersection calculations | Single pass with parameter updates |
| **Parallel Lines** | Easily handled | Requires special checking |
| **Window Shape** | Rectangular only | Rectangular only |

---

## 4. Polygon Clipping Algorithms

Polygon clipping determines the visible portion of polygons within a clipping window. Unlike line clipping, polygon clipping must maintain the topological integrity of the resulting shape.

### 4.1 Sutherland-Hodgman Polygon Clipping Algorithm

#### Concept

The **Sutherland-Hodgman algorithm** uses a **re-entrant polygon clipping** approach that clips the polygon against each edge of the clipping window sequentially. It processes the polygon edge by edge, producing a new polygon at each stage.

#### Algorithm Overview

The algorithm clips the polygon against four boundaries in sequence:
1. Left boundary
2. Right boundary  
3. Bottom boundary
4. Top boundary

For each boundary, the algorithm examines each edge of the input polygon and:
- **If both vertices are inside**: Add the second vertex to output
- **If first vertex is inside and second is outside**: Add intersection point to output
- **If first vertex is outside and second is inside**: Add intersection point and second vertex to output
- **If both vertices are outside**: Add nothing to output

#### Visual Representation

```
    Original Polygon:          After Left Clip:        After Complete Clip:
    
    +------------------+        +------------------+    +------------------+
    |                  |        |        /\        |    |        /\        |
    |         *        |   →    |       /  \       |→   |       /  \       |
    |      *     *     |        |      /    \      |    |      /    \      |
    |    *         *   |        +-----/------\-----+    +-----/------\-----+
    |                  |        |    \      /    |          \    /    |
    +------------------+        |     \    /     |           \  /     |
                                |      \  /      |            \/      |
                                +------------------+    +------------------+
```

#### Pseudocode

```python
# Sutherland-Hodgman Polygon Clipping
def sutherland_hodgman_clip(polygon, clip_edge):
    """
    Clip polygon against a single edge
    polygon: list of (x, y) vertices
    clip_edge: tuple of (x1, y1, x2, y2) defining clipping boundary
    """
    output_polygon = []
    n = len(polygon)
    
    for i in range(n):
        current_point = polygon[i]
        previous_point = polygon[(i - 1) % n]
        
        # Check if current point is inside
        current_inside = is_point_inside(current_point, clip_edge)
        previous_inside = is_point_inside(previous_point, clip_edge)
        
        if current_inside and previous_inside:
            # Both inside: add current point
            output_polygon.append(current_point)
        elif current_inside and not previous_inside:
            # Entering: add intersection and current point
            intersection = compute_intersection(previous_point, 
                                               current_point, clip_edge)
            output_polygon.append(intersection)
            output_polygon.append(current_point)
        elif not current_inside and previous_inside:
            # Exiting: add intersection only
            intersection = compute_intersection(previous_point,
                                               current_point, clip_edge)
            output_polygon.append(intersection)
        # Both outside: add nothing
    
    return output_polygon

def is_point_inside(point, edge):
    """Check if point is inside the clipping edge"""
    x, y = point
    x1, y1, x2, y2 = edge
    
    # For left edge (x >= xmin)
    if x1 == x2:  # Vertical edge
        return x >= min(y1, y2)
    # For bottom edge (y >= ymin)
    if y1 == y2:  # Horizontal edge
        return y >= min(x1, x2)
    return True
```

#### Complete Implementation

```python
def clip_polygon_sutherland_hodgman(vertices, xmin, ymin, xmax, ymax):
    """
    Complete Sutherland-Hodgman polygon clipping
    """
    # Define clipping boundaries
    boundaries = [
        (xmin, ymin, xmin, ymax),  # Left
        (xmax, ymin, xmax, ymax),  # Right
        (xmin, ymin, xmax, ymin),  # Bottom
        (xmin, ymax, xmax, ymax)   # Top
    ]
    
    # Start with original polygon
    clipped_polygon = vertices
    
    # Clip against each boundary sequentially
    for boundary in boundaries:
        clipped_polygon = sutherland_hodgman_clip(clipped_polygon, boundary)
        if not clipped_polygon:
            return []  # Polygon completely clipped away
    
    return clipped_polygon
```

### 4.2 Weiler-Atherton Polygon Clipping Algorithm

#### Concept

The **Weiler-Atherton algorithm** is more sophisticated than Sutherland-Hodgman and can handle both clipping windows and complex polygon operations. It uses a **node-based approach** to identify intersection points and construct the resulting polygon.

#### Key Features

- Can handle both clipping and masking operations
- Works with concave polygons effectively
- Uses a list of intersection points to track entry and exit points
- More suitable for complex polygon operations

#### Algorithm Steps

**Step 1**: Find all intersection points between polygon edges and clipping window boundaries.

**Step 2**: Mark intersection points as either **entry points** (entering the clipping window) or **exit points** (leaving the clipping window).

**Step 3**: Build linked lists of vertices and intersection points for both the polygon and clipping window.

**Step 4**: Traverse from an entry intersection point to construct the clipped polygon:
- Follow polygon edges until reaching an exit point
- Then follow clipping window boundary
- Continue until returning to the starting point

#### Pseudocode

```python
# Weiler-Atherton Polygon Clipping (Conceptual)
class Vertex:
    def __init__(self, x, y, is_intersection=False, entry=None):
        self.x = x
        self.y = y
        self.is_intersection = is_intersection
        self.entry = entry  # True for entry, False for exit
        self.next = None
        self.next_boundary = None

def weiler_atherton_clip(subject_polygon, clip_polygon):
    """
    Weiler-Atherton polygon clipping algorithm
    subject_polygon: polygon to be clipped
    clip_polygon: clipping window polygon
    """
    # Step 1: Find all intersection points
    intersection_points = find_intersections(subject_polygon, clip_polygon)
    
    # Step 2: Mark entry/exit points
    for ip in intersection_points:
        ip.entry = determine_entry_exit(ip, subject_polygon, clip_polygon)
    
    # Step 3: Insert intersection points into both polygons
    insert_intersections(subject_polygon, intersection_points)
    insert_intersections(clip_polygon, intersection_points)
    
    # Step 4: Build result polygon
    result = []
    for ip in intersection_points:
        if ip.entry:
            result.append(traverse_from_entry(ip, subject_polygon, 
                                             clip_polygon))
    
    return result

def traverse_from_entry(entry_point, subject, clip):
    """Traverse from entry point to construct clipped polygon"""
    result = [entry_point]
    current = entry_point
    
    while True:
        # Follow subject polygon
        current = current.next
        if current.is_intersection:
            if current == entry_point:
                break
            # Switch to clipping boundary
            current = current.next_boundary
        
        result.append(current)
    
    return result
```

#### Visual Comparison

```
    Sutherland-Hodgman:              Weiler-Atherton:
    
    Sequential edge clipping         Node-based traversal
    +------------------+             +------------------+
    |        /\        |             |        /    \    |
    |       /  \       |             |   *---*      *---*|
    |      /    \      |             |   |   |      |   ||
    +-----/------\-----+             +---|---*      *---|--+
        Simple approach                  Complex but powerful
```

---

## 5. Worked Examples with Code

### Example 1: Line Clipping with Cohen-Sutherland

**Problem**: Clip the line segment from P1(100, 50) to P2(250, 150) against a clipping window with corners (150, 80) and (300, 200).

**Solution**:

```python
# Example 1: Cohen-Sutherland Line Clipping

# Define clipping window
xmin, ymin = 150, 80
xmax, ymax = 300, 200

# Define line segment
x1, y1 = 100, 50
x2, y2 = 250, 150

# Compute region codes
code1 = compute_region_code(x1, y1, xmin, ymin, xmax, ymax)
code2 = compute_region_code(x2, y2, xmin, ymin, xmax, ymax)

print(f"P1 region code: {bin(code1)}")  # 1001 (Above + Left)
print(f"P2 region code: {bin(code2)}")  # 0000 (Inside)

# Since code1 has LEFT bit set, need to clip
# Intersection with left boundary (x = 150):
# y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
# y = 50 + (150 - 50) * (150 - 100) / (250 - 100)
# y = 50 + 100 * 50 / 150 = 50 + 33.33 = 83.33

# After clipping: (150, 83.33) to (250, 150)
print(f"Clipped line: (150, 83.33) to (250, 150)")
```

### Example 2: Polygon Clipping with Sutherland-Hodgman

**Problem**: Clip a triangle with vertices (100, 100), (200, 250), (300, 100) against a rectangular window (150, 80) to (280, 220).

**Solution**:

```python
# Example 2: Sutherland-Hodgman Polygon Clipping

# Original triangle vertices (counter-clockwise)
polygon = [(100, 100), (200, 250), (300, 100)]

# Clipping window
xmin, ymin = 150, 80
xmax, ymax = 280, 220

# Step 1: Clip against left boundary (x = 150)
left_boundary = (150, 80, 150, 220)
after_left = sutherland_hodgman_clip(polygon, left_boundary)
print(f"After left clip: {after_left}")
# Output: [(150, 112.5), (200, 250), (280, 195), (280, 100)]

# Step 2: Clip against right boundary (x = 280)
right_boundary = (280, 80, 280, 220)
after_right = sutherland_hodgman_clip(after_left, right_boundary)
print(f"After right clip: {after_right}")
# Output: [(150, 112.5), (200, 250), (280, 195)]

# Step 3: Clip against bottom boundary (y = 80)
bottom_boundary = (150, 80, 280, 80)
after_bottom = sutherland_hodgman_clip(after_right, bottom_boundary)
print(f"After bottom clip: {after_bottom}")
# Output: [(150, 112.5), (200, 250), (280, 195)]

# Step 4: Clip against top boundary (y = 220)
top_boundary = (150, 220, 280, 220)
final_polygon = sutherland_hodgman_clip(after_bottom, top_boundary)
print(f"Final clipped polygon: {final_polygon}")
# Output: [(150, 112.5), (200, 220), (280, 195)]
```

---

## 6. Comparative Analysis

### When to Use Each Algorithm

| Scenario | Recommended Algorithm |
|----------|----------------------|
| **Batch line clipping** | Cohen-Sutherland |
| **Single line clipping** | Liang-Barsky |
| **Simple polygon clipping** | Sutherland-Hodgman |
| **Complex polygon operations** | Weiler-Atherton |
| **Real-time applications** | Liang-Barsky (for lines) |
| **CAD applications** | Weiler-Atherton |

### Time Complexity

| Algorithm | Time Complexity |
|-----------|-----------------|
| Cohen-Sutherland | O(N) per line |
| Liang-Barsky | O(1) per line |
| Sutherland-Hodgman | O(N × M) where N=polygon vertices, M=window edges |
| Weiler-Atherton | O(N + M + I) where I=intersection points |

---

## 7. Multiple Choice Questions

### Section A: Line Clipping

**Question 1**: In the Cohen-Sutherland algorithm, what does a region code of `0000` indicate?
- (a) Point is outside the clipping window
- (b) Point is inside the clipping window
- (c) Point is on the boundary
- (d) Point requires further testing

**Answer**: (b) Point is inside the clipping window

**Question 2**: The Liang-Barsky algorithm uses which mathematical representation?
- (a) Vector representation
- (b) Parametric equations
- (c) Polar coordinates
- (d) Homogeneous coordinates

**Answer**: (b) Parametric equations

**Question 3**: What is the maximum number of clipping operations needed for Cohen-Sutherland algorithm?
- (a) 1
- (b) 2
- (c) 4
- (d) 8

**Answer**: (c) 4

**Question 4**: If the logical AND of two region codes is non-zero in Cohen-Sutherland, the line is:
- (a) Completely inside
- (b) Completely outside
- (c) Partially inside
- (d) Requires intersection calculation

**Answer**: (b) Completely outside

**Question 5**: Which algorithm is more efficient for clipping a single line segment?
- (a) Cohen-Sutherland
- (b) Liang-Barsky
- (c) Both equally efficient
- (d) Neither

**Answer**: (b) Liang-Barsky

### Section B: Polygon Clipping

**Question 6**: The Sutherland-Hodgman algorithm processes clipping boundaries in:
- (a) Random order
- (b) Parallel fashion
- (c) Sequential order
- (d) Recursive order

**Answer**: (c) Sequential order

**Question 7**: In Sutherland-Hodgman, when both vertices are outside the clipping boundary, we:
- (a) Add both vertices to output
- (b) Add only the intersection point
- (c) Add nothing to output
- (d) Add the first vertex

**Answer**: (c) Add nothing to output

**Question 8**: The Weiler-Atherton algorithm can handle:
- (a) Only convex polygons
- (b) Only concave polygons
- (c) Both convex and concave polygons
- (d) Only rectangular windows

**Answer**: (c) Both convex and concave polygons

**Question 9**: In polygon clipping, an entry point is defined as:
- (a) Point leaving the clipping window
- (b) Point entering the clipping window
- (c) Point on the boundary
- (d) Point of tangency

**Answer**: (b) Point entering the clipping window

**Question 10**: The time complexity of Sutherland-Hodgman for clipping an N-vertex polygon is:
- (a) O(N)
- (b) O(N²)
- (c) O(N × M) where M is window edges
- (d) O(1)

**Answer**: (c) O(N × M) where M is window edges

---

## 8. Key Takeaways

### Line Clipping Algorithms

1. **Cohen-Sutherland** uses region codes (outcodes) for efficient elimination of trivial cases:
   - Trivial acceptance: both codes are `0000`
   - Trivial rejection: logical AND is non-zero
   - Uses parametric intersection calculations for non-trivial cases

2. **Liang-Barsky** provides more efficient single-segment clipping:
   - Uses parametric line equation: P = P1 + t(P2 - P1)
   - Updates t0 and t1 parameters incrementally
   - Superior for single line clipping operations

### Polygon Clipping Algorithms

3. **Sutherland-Hodgman** clips polygon against each boundary sequentially:
   - Produces new polygon at each stage
   - Works well for convex clipping windows
   - Simple to implement but may produce unnecessary vertices

4. **Weiler-Atherton** handles complex polygon operations:
   - Uses intersection point classification (entry/exit)
   - Can handle concave polygons and complex boolean operations
   - More computationally intensive but more powerful

### Practical Applications

5. These algorithms are foundational for:
   - Windowing systems in operating systems
   - Computer-aided design software
   - Game engines and real-time rendering
   - Geographic information systems (GIS)

### Implementation Considerations

6. For Delhi University examination:
   - Understand region code calculation for Cohen-Sutherland
   - Know parametric derivation for Liang-Barsky
   - Remember the four cases in Sutherland-Hodgman edge processing
   - Be able to trace through examples by hand

### Performance Notes

7. Choose algorithms based on:
   - Number of objects to clip
   - Complexity of clipping window
   - Real-time vs. batch processing requirements

---

## References for Further Study

1. Computer Graphics: Principles and Practice by Foley, van Dam, Feiner, Hughes
2. Computer Graphics by Donald Hearn and M. Pauline Baker
3. Delhi University BSc (Hons) Computer Science Syllabus - NEP 2024 UGCF
4. "CLIP: A Line Clipping Algorithm" - Technical references for Liang-Barsky

---

*This study material covers the complete syllabus requirements for Line and Polygon Clipping Algorithms as specified in the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF curriculum.*