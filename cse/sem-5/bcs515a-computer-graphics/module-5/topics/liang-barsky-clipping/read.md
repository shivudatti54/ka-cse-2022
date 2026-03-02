# Liang-Barsky Line Clipping Algorithm

## Introduction

Line clipping is a fundamental operation in computer graphics that involves removing portions of line segments that lie outside a rectangular clipping window. The Liang-Barsky algorithm is an efficient parametric line clipping algorithm that offers significant computational advantages over the traditional Cohen-Sutherland algorithm. Developed by You-Dong Liang and Brian Barsky in 1984, this algorithm uses parametric equations of lines and performs clipping by checking each line segment against four inequality conditions representing the clipping boundaries.

The importance of the Liang-Barsky algorithm in computer graphics cannot be overstated. It is widely used in rendering pipelines, graphical user interfaces, CAD systems, and visualization applications where efficient clipping operations are essential for maintaining real-time performance. Unlike the Cohen-Sutherland algorithm that may require multiple subdivisions of line segments, Liang-Barsky computes the exact intersection points using parametric analysis, making it particularly efficient for lines that either lie completely inside or completely outside the clipping window.

## Key Concepts

### Parametric Line Representation

The Liang-Barsky algorithm represents a line segment from point P1(x1, y1) to P2(x2, y2) using parametric equations:

```
x = x1 + t(x2 - x1), where 0 ≤ t ≤ 1
y = y1 + t(y2 - y1), where 0 ≤ t ≤ 1
```

Here, parameter t represents the normalized position along the line segment, where t=0 corresponds to point P1 and t=1 corresponds to point P2.

### Clipping Window Boundaries

The clipping window is defined by four boundaries:

- Left boundary: x = xwmin (xmin)
- Right boundary: x = xwmax (xmax)
- Bottom boundary: y = ywmin (ymin)
- Top boundary: y = ywmax (ymax)

### The Four Inequality Conditions

For a point (x, y) to be inside the clipping window, all four conditions must be satisfied:

1. x ≥ xwmin (Left boundary)
2. x ≤ xwmax (Right boundary)
3. y ≥ ywmin (Bottom boundary)
4. y ≤ ywmax (Top boundary)

Substituting the parametric equations:

1. x1 + t(x2 - x1) ≥ xwmin
2. x1 + t(x2 - x1) ≤ xwmax
3. y1 + t(y2 - y1) ≥ ywmin
4. y1 + t(y2 - y1) ≤ ywmax

### Delta Values (P and Q Values)

For computational purposes, we define:

- Δx = x2 - x1
- Δy = y2 - y1

For each boundary, we calculate:

- p1 = -Δx (left boundary)
- p2 = Δx (right boundary)
- p3 = -Δy (bottom boundary)
- p4 = Δy (top boundary)

And corresponding q values:

- q1 = x1 - xwmin (left boundary)
- q2 = xwmax - x1 (right boundary)
- q3 = y1 - ywmin (bottom boundary)
- q4 = ywmax - y1 (top boundary)

### The Clipping Logic

The algorithm proceeds as follows:

1. **Initialize**: Set t0 = 0 and t1 = 1

2. **Check each boundary**: For each of the four boundaries:

- If p = 0 and q < 0: Line is completely outside (reject)
- If p < 0: Line enters the clipping window at t = q/p, update t0
- If p > 0: Line exits the clipping window at t = q/p, update t1
- If p = 0 and q ≥ 0: Line is parallel to this boundary

3. **Check validity**: If t0 > t1, the line is completely outside; otherwise, calculate the clipped endpoints using t0 and t1

## Examples

### Example 1: Simple Line Completely Inside

**Problem**: Clip the line from P1(2, 2) to P2(5, 5) against clipping window [0, 0] to [10, 10].

**Solution**:

Step 1: Calculate deltas

- Δx = 5 - 2 = 3
- Δy = 5 - 2 = 3

Step 2: Calculate p and q values

- p1 = -3, q1 = 2 - 0 = 2
- p2 = 3, q2 = 10 - 2 = 8
- p3 = -3, q3 = 2 - 0 = 2
- p4 = 3, q4 = 10 - 2 = 8

Step 3: Process each boundary

Boundary 1 (Left, p1 = -3):

- p1 < 0, so t0 = max(0, 2/(-3)) = max(0, -0.67) = 0

Boundary 2 (Right, p2 = 3):

- p2 > 0, so t1 = min(1, 8/3) = min(1, 2.67) = 1

Boundary 3 (Bottom, p3 = -3):

- p3 < 0, so t0 = max(0, 2/(-3)) = max(0, -0.67) = 0

Boundary 4 (Top, p4 = 3):

- p4 > 0, so t1 = min(1, 8/3) = min(1, 2.67) = 1

Step 4: Check validity

- t0 = 0, t1 = 1, so t0 ≤ t1

Step 5: Calculate clipped endpoints

- xnew1 = 2 + 0(3) = 2, ynew1 = 2 + 0(3) = 2
- xnew2 = 2 + 1(3) = 5, ynew2 = 2 + 1(3) = 5

**Result**: The line remains unchanged at (2, 2) to (5, 5) - completely inside the window.

### Example 2: Line Requiring Clipping

**Problem**: Clip the line from P1(5, 15) to P2(15, 5) against clipping window with corners (0, 0) and (10, 10).

**Solution**:

Step 1: Calculate deltas

- Δx = 15 - 5 = 10
- Δy = 5 - 15 = -10

Step 2: Calculate p and q values

- p1 = -10, q1 = 5 - 0 = 5
- p2 = 10, q2 = 10 - 5 = 5
- p3 = 10, q3 = 15 - 0 = 15
- p4 = -10, q4 = 10 - 15 = -5

Step 3: Process each boundary

Boundary 1 (Left, p1 = -10):

- p1 < 0, so t0 = max(0, 5/(-10)) = max(0, -0.5) = 0

Boundary 2 (Right, p2 = 10):

- p2 > 0, so t1 = min(1, 5/10) = min(1, 0.5) = 0.5

Boundary 3 (Bottom, p3 = 10):

- p3 > 0, so t1 = min(0.5, 15/10) = min(0.5, 1.5) = 0.5

Boundary 4 (Top, p4 = -10):

- p4 < 0, so t0 = max(0, -5/(-10)) = max(0, 0.5) = 0.5

Step 4: Check validity

- t0 = 0.5, t1 = 0.5, so t0 ≤ t1 (line clips to a single point)

Step 5: Calculate clipped endpoints

- xnew1 = 5 + 0.5(10) = 10, ynew1 = 15 + 0.5(-10) = 10
- xnew2 = 5 + 0.5(10) = 10, ynew2 = 15 + 0.5(-10) = 10

**Result**: The line clips to a single point at (10, 10) - it just touches the corner of the window.

### Example 3: Line Completely Outside

**Problem**: Clip the line from P1(-5, -5) to P2(-2, -2) against clipping window [0, 0] to [10, 10].

**Solution**:

Step 1: Calculate deltas

- Δx = -2 - (-5) = 3
- Δy = -2 - (-5) = 3

Step 2: Calculate p and q values

- p1 = -3, q1 = -5 - 0 = -5
- p2 = 3, q2 = 10 - (-5) = 15
- p3 = -3, q3 = -5 - 0 = -5
- p4 = 3, q4 = 10 - (-5) = 15

Step 3: Process each boundary

Boundary 1 (Left, p1 = -3):

- p1 < 0, so t0 = max(0, -5/(-3)) = max(0, 1.67) = 1.67

Boundary 2 (Right, p2 = 3):

- p2 > 0, so t1 = min(1, 15/3) = min(1, 5) = 1

**Result**: Since p1 = 0 case check isn't triggered, we continue. At this point t0 = 1.67 > t1 = 1.

Step 4: Since t0 > t1, the line is completely outside the clipping window.

**Result**: The line from (-5, -5) to (-2, -2) is completely rejected.

## Exam Tips

1. **Remember the parametric form**: The parametric equations x = x1 + t(x2-x1) and y = y1 + t(y2-y1) form the foundation of this algorithm.

2. **Master p and q calculations**: p1 = -Δx (left), p2 = Δx (right), p3 = -Δy (bottom), p4 = Δy (top). For q values, remember q1 = x1 - xmin, q2 = xmax - x1, q3 = y1 - ymin, q4 = ymax - y1.

3. **Understand p=0 special case**: When p=0 and q<0, the line is parallel to and outside the boundary (reject). When p=0 and q≥0, the line is parallel and inside (continue).

4. **The rejection condition**: If t0 > t1 after processing all boundaries, the line is completely outside the clipping window.

5. **Comparison with Cohen-Sutherland**: Remember that Liang-Barsky is more efficient for line clipping because it calculates exact intersection points rather than repeatedly subdividing lines.

6. **Drawing the algorithm flow**: Be prepared to draw or describe the step-by-step flow of the algorithm in exams.

7. **Calculate final coordinates correctly**: After obtaining t0 and t1, use x = x1 + t×Δx and y = y1 + t×Δy to find clipped endpoints.
