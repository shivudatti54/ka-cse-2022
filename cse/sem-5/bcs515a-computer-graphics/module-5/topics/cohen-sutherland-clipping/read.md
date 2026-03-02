# Cohen-Sutherland Line Clipping Algorithm

## Introduction

Line clipping is a fundamental operation in computer graphics that determines which portions of a line segment lie within a visible region (clipping window) and should be displayed. The Cohen-Sutherland algorithm, developed by Danny Cohen and Ivan Sutherland in 1967, is one of the most efficient and widely used algorithms for line clipping against a rectangular window. This algorithm revolutionized computer graphics by providing a fast, systematic approach to determining which lines intersect a clipping region, significantly reducing the computational complexity compared to naive approaches.

The algorithm is particularly important in rendering pipelines where only visible portions of graphics objects need to be displayed. When creating complex scenes, graphics systems must clip all primitives against the viewport boundaries before rasterization. The Cohen-Sutherland algorithm's efficiency stems from its use of outcodes (region codes) that quickly identify lines that are either completely inside the window, completely outside, or require further intersection calculations. This makes it an essential topic in the Computer Graphics curriculum for CSE students, as it appears frequently in examinations and forms the foundation for understanding more advanced clipping algorithms.

## Key Concepts

### Outcode (Region Code)

The Cohen-Sutherland algorithm divides the 2D plane into nine regions using the clipping window boundaries. Each region is assigned a 4-bit outcode that indicates the position of a point relative to the clipping window. The bits represent:

- **Bit 1 (1000)**: Above the window (Top) - y > ymax
- **Bit 2 (0100)**: Below the window (Bottom) - y < ymin
- **Bit 3 (0010)**: Right of the window (Right) - x > xmax
- **Bit 4 (0001)**: Left of the window (Left) - x < xmin

The clipping window is defined by four boundaries: xmin, xmax, ymin, and ymax. A point inside the window has an outcode of 0000.

### Clipping Window Regions

The algorithm classifies the clipping window into nine regions:

1. **Center (0000)**: Inside the clipping window
2. **Top (1000)**: Above ymax
3. **Bottom (0100)**: Below ymin
4. **Right (0010)**: Right of xmax
5. **Left (0001)**: Left of xmin
6. **Top-Right (1010)**: Above and right
7. **Top-Left (1001)**: Above and left
8. **Bottom-Right (0110)**: Below and right
9. **Bottom-Left (0101)**: Below and left

### Algorithm Steps

**Step 1: Compute Outcodes**
Calculate the outcode for both endpoints P1(x1, y1) and P2(x2, y2) of the line segment.

**Step 2: Check for Acceptance**
If both endpoints have outcode 0000 (both inside), the entire line is accepted and drawn.

**Step 3: Check for Rejection**
If the logical AND of the two outcodes is non-zero, the line is completely outside and rejected. This is because both endpoints share at least one region that is outside, meaning the line cannot intersect the window.

**Step 4: Clipping**
If the line is neither accepted nor rejected, divide the line at the intersection point with one of the window boundaries. Replace the outside endpoint with the intersection point and recompute its outcode. Repeat steps 2-4 until acceptance or rejection.

### Intersection Calculations

When clipping is required, the algorithm finds intersections with window edges:

- **Left Edge (x = xmin)**: Using parametric form x = x1 + t(x2 - x1), solve for t when x = xmin
- **Right Edge (x = xmax)**: Similar calculation for xmax
- **Bottom Edge (y = ymin)**: y = y1 + t(y2 - y1), solve for ymin
- **Top Edge (y = ymax)**: Similar calculation for ymax

The intersection point is calculated using the slope of the line:

- For vertical lines: use y-coordinates
- For horizontal lines: use x-coordinates
- For general lines: use parametric equations

## Examples

### Example 1: Completely Inside Line

**Given:**

- Clipping Window: xmin=100, xmax=500, ymin=100, ymax=400
- Line P1(200, 200) to P2(400, 300)

**Solution:**

**Step 1: Compute Outcodes**

For P1(200, 200):

- x = 200 (between 100 and 500) → Bit 4 = 0
- y = 200 (between 100 and 400) → Bit 2 = 0, Bit 1 = 0
- Outcode = 0000

For P2(400, 300):

- x = 400 (between 100 and 500) → Bit 4 = 0
- y = 300 (between 100 and 400) → Bit 2 = 0, Bit 1 = 0
- Outcode = 0000

**Step 2: Check Acceptance**
Both outcodes are 0000, so the line is completely inside.

**Result**: Draw the line from (200, 200) to (400, 300)

### Example 2: Completely Outside Line

**Given:**

- Clipping Window: xmin=100, xmax=500, ymin=100, ymax=400
- Line P1(50, 200) to P2(80, 300)

**Solution:**

**Step 1: Compute Outcodes**

For P1(50, 200):

- x = 50 < 100 → Bit 4 (Left) = 1
- y = 200 (between 100 and 400) → Bits 1,2 = 0
- Outcode = 0001

For P2(80, 300):

- x = 80 < 100 → Bit 4 = 1
- y = 300 (between 100 and 400) → Bits 1,2 = 0
- Outcode = 0001

**Step 2: Check Rejection**
AND = 0001 AND 0001 = 0001 (non-zero)

**Result**: The line is completely outside the window, reject it.

### Example 3: Line Requiring Clipping

**Given:**

- Clipping Window: xmin=100, xmax=500, ymin=100, ymax=400
- Line P1(50, 50) to P2(600, 450)

**Solution:**

**Step 1: Compute Outcodes**

For P1(50, 50):

- x = 50 < 100 → Left = 1
- y = 50 < 100 → Bottom = 1
- Outcode = 0101 (Bottom-Left)

For P2(600, 450):

- x = 600 > 500 → Right = 1
- y = 450 > 400 → Top = 1
- Outcode = 1010 (Top-Right)

**Step 2: Check Acceptance**
Both not 0000, so not accepted.

**Step 3: Check Rejection**
AND = 0101 AND 1010 = 0000, so not rejected. Must clip.

**Step 4: Clipping (First Iteration)**

P1 is outside (0101), so clip at P1. Check P1's outcode:

- Bottom bit (0100) is set: Intersect with y = 100
- Slope m = (450-50)/(600-50) = 400/550 = 0.727
- At y = 100: 100 = 50 + t(400) → t = 50/400 = 0.125
- x = 50 + 0.125(550) = 118.75
- New point: P1'(118.75, 100)

- Left bit (0001) is set: Intersect with x = 100
- At x = 100: 100 = 50 + t(550) → t = 50/550 = 0.0909
- y = 50 + 0.0909(400) = 86.36
- Use this intersection (whichever clips properly)

New line: P1'(100, 86.36) to P2(600, 450)

Recompute outcodes:

- P1': Inside → 0000
- P2: 1010

Neither both 0000, AND = 0000, continue clipping.

**Step 5: Clipping (Second Iteration)**

P2 is outside (1010), clip at P2:

- Top bit (1000): y = 400
- At y = 400: 400 = 50 + t(400) → t = 350/400 = 0.875
- x = 50 + 0.875(550) = 531.25
- New point: P2'(531.25, 400)

- Right bit (0010): x = 500
- At x = 500: 500 = 50 + t(550) → t = 450/550 = 0.818
- y = 50 + 0.818(400) = 377.27
- Use intersection with proper boundary

New line: P1'(100, 86.36) to P2'(500, 377.27)

**Step 6: Final Check**
Both endpoints now inside (0000).

**Result**: Draw clipped line from (100, 86.36) to (500, 377.27)

## Exam Tips

1. **Remember the bit assignments**: Top=1000, Bottom=0100, Right=0010, Left=0001 - this is crucial for computing outcodes correctly in exams.

2. **Logical AND test**: If (outcode1 AND outcode2) ≠ 0, reject the line immediately - this is a quick elimination test.

3. **Both endpoints inside**: If both outcodes are 0000, accept without any calculations - this saves time.

4. **Order of clipping**: When clipping against multiple edges, you can clip against any boundary first; the algorithm converges to the correct result.

5. **Slope calculation**: Remember slope = (y2-y1)/(x2-x1), and use parametric form for intersection: P = P1 + t(P2-P1), where 0 ≤ t ≤ 1.

6. **Window boundary values**: Always clearly define xmin, xmax, ymin, ymax from the problem before starting.

7. **Know when to stop**: The algorithm terminates when either both points are inside (accept) or the line is rejected (AND ≠ 0).

8. **Practice both types**: Be prepared to solve problems where lines are completely inside, completely outside, or partially intersecting.
