# Line Segment Clipping

## Introduction

Line segment clipping is a fundamental operation in computer graphics that determines which portions of a line segment are visible within a specified rectangular region called a "clip window" or "viewport." This process is essential for rendering only the visible portions of objects, preventing unnecessary computation and memory usage when displaying graphics on output devices. Every graphics application that renders objects larger than or extending beyond the visible screen area relies on efficient line clipping algorithms to ensure proper display.

The clipping operation becomes particularly crucial when dealing with 3D graphics pipelines, where objects are transformed and projected onto 2D screens. Without proper clipping, portions of graphics outside the visible area would still be processed, leading to significant performance degradation and potential errors in rendering. The evolution of line clipping algorithms has focused on reducing computational complexity while maintaining accuracy, making them a cornerstone topic in computer graphics education and practical applications.

In the context of 's Computer Science curriculum, line segment clipping algorithms form an essential part of understanding the graphics rendering pipeline. Students must master both the theoretical foundations and practical implementations of these algorithms, as they frequently appear in university examinations and form the basis for more advanced graphics concepts.

## Key Concepts

### Window and Viewport

The **clip window** (or simply "window") is a rectangular region defined by minimum and maximum x and y coordinates (Xmin, Xmax, Ymin, Ymax) that represents the visible portion of the world coordinate system. Any graphics primitive outside this window must be clipped, while those inside are preserved. The **viewport** is the corresponding rectangular region on the output device (screen) where the clipped content is displayed. Understanding the relationship between window and viewport is crucial for implementing proper zoom, pan, and view transformation operations in graphics applications.

### End Point Codes (Cohen-Sutherland Algorithm)

The Cohen-Sutherland algorithm uses a 4-bit region code to classify each endpoint of a line segment relative to the clip window. Each bit represents a position relative to the window boundaries:

- **Bit 1 (1000)**: Above the window (y > Ymax)
- **Bit 2 (0100)**: Below the window (y < Ymin)
- **Bit 3 (0010)**: To the right of the window (x > Xmax)
- **Bit 4 (0001)**: To the left of the window (x < Xmin)

A point inside the window has code 0000. The algorithm uses these codes to quickly determine trivial acceptance (both endpoints have code 0000) or trivial rejection (both endpoints share a set bit, indicating the line lies completely outside one side).

### Cohen-Sutherland Line Clipping Algorithm

The algorithm follows these steps:

1. Compute the region codes for both endpoints P1 and P2
2. If both codes are 0000 (trivial accept), the entire line is inside the window
3. If the bitwise AND of the codes is non-zero (trivial reject), the line is completely outside
4. Otherwise, calculate intersection points with one or more window boundaries
5. Replace the outside endpoint with the intersection point
6. Repeat until the line is either accepted or rejected

The intersection points are calculated using parametric equations. For example, when clipping against the left boundary (x = Xmin), the intersection point is found using:

- t = (Xmin - x1) / (x2 - x1)
- y = y1 + t × (y2 - y1)

### Liang-Barsky Line Clipping Algorithm

The Liang-Barsky algorithm is a more efficient parametric approach that uses the parametric equation of a line segment: P(t) = P1 + t(P2 - P1), where 0 ≤ t ≤ 1. The algorithm calculates entering and leaving values for the parameter t based on four inequalities representing the window boundaries:

- x1 + t × dx ≥ Xmin → t ≤ (Xmin - x1) / dx (for dx > 0)
- x1 + t × dx ≤ Xmax → t ≥ (Xmax - x1) / dx (for dx < 0)
- y1 + t × dy ≥ Ymin → t ≤ (Ymin - y1) / dy (for dy > 0)
- y1 + t × dy ≤ Ymax → t ≥ (Ymax - y1) / dy (for dy < 0)

The algorithm maintains two parameters t1 (entering) and t2 (leaving), initializing them to 0 and 1 respectively. For each boundary, update these values. If t1 > t2 after processing all boundaries, the line is completely outside. Otherwise, the clipped segment runs from P(t1) to P(t2).

### Midpoint Subdivision Algorithm

This divide-and-conquer approach repeatedly bisects line segments that partially intersect the window. For each segment:

1. Compute the midpoint of the line segment
2. Determine the region code of the midpoint
3. If the midpoint is inside, use the half containing the inside endpoint
4. If outside, use the half containing the outside endpoint
5. Repeat until the segment is small enough (within one pixel) or trivially accepted/rejected

This algorithm is particularly suitable for parallel processing and hardware implementation.

## Examples

### Example 1: Cohen-Sutherland Algorithm

**Problem**: Clip the line segment from P1(100, 50) to P2(200, 150) against the window defined by Xmin=120, Xmax=180, Ymin=80, Ymax=140.

**Solution**:

_Step 1: Compute Region Codes_

For P1(100, 50):

- Left of window (100 < 120): Bit 4 = 1
- Below window (50 < 80): Bit 2 = 1
- Code: 0101 (binary) = 5 (decimal)

For P2(200, 150):

- Right of window (200 > 180): Bit 3 = 1
- Above window (150 > 140): Bit 1 = 1
- Code: 1010 (binary) = 10 (decimal)

_Step 2: Check Trivial Acceptance/Rejection_

- Both codes are not 0000 (not trivial accept)
- 0101 AND 1010 = 0000 (not trivial reject)
- Must find intersections

_Step 3: Find Intersections_

Using P1 (code 0101), clip against left boundary (x = 120):
t = (120 - 100) / (200 - 100) = 20/100 = 0.2
y = 50 + 0.2 × (150 - 50) = 50 + 20 = 70
New P1 becomes (120, 70), code: 0100 (below window)

Now P1(120, 70) is below window, clip against bottom (y = 80):
t = (80 - 70) / (150 - 70) = 10/80 = 0.125
x = 120 + 0.125 × (200 - 120) = 120 + 10 = 130
New P1 becomes (130, 80), code: 0000

_Step 4: Final Check_
Now P1(130, 80) has code 0000 and P2(200, 150) has code 1010.
The algorithm continues and finds intersection with right boundary:
t = (180 - 120) / (200 - 120) = 60/80 = 0.75
y = 70 + 0.75 × (150 - 70) = 70 + 60 = 130
New P2 becomes (180, 130)

**Result**: The clipped line segment is from (130, 80) to (180, 130).

### Example 2: Liang-Barsky Algorithm

**Problem**: Clip line P1(50, 20) to P2(150, 100) with window Xmin=80, Xmax=120, Ymin=40, Ymax=80.

**Solution**:

_Step 1: Identify parameters_
x1=50, y1=20, x2=150, y2=100
dx = x2 - x1 = 100, dy = y2 - y1 = 80
Xmin=80, Xmax=120, Ymin=40, Ymax=80
Initialize: t1 = 0, t2 = 1

_Step 2: Process left boundary (x ≥ 80)_
Since dx > 0: p1 = -dx = -100, q1 = x1 - Xmin = 50 - 80 = -30
r = q1/p1 = -30/(-100) = 0.3
Since p1 ≠ 0 and r > t1: t1 = max(0, 0.3) = 0.3

_Step 3: Process right boundary (x ≤ 120)_
Since dx > 0: p2 = dx = 100, q2 = Xmax - x1 = 120 - 50 = 70
r = q2/p2 = 70/100 = 0.7
Since p2 ≠ 0 and r < t2: t2 = min(1, 0.7) = 0.7

_Step 4: Process bottom boundary (y ≥ 40)_
Since dy > 0: p3 = -dy = -80, q3 = y1 - Ymin = 20 - 40 = -20
r = q3/p3 = -20/(-80) = 0.25
Since p1 ≠ 0 and r > t1: t1 = max(0.3, 0.25) = 0.3

_Step 5: Process top boundary (y ≤ 80)_
Since dy > 0: p4 = dy = 80, q4 = Ymax - y1 = 80 - 20 = 60
r = q4/p4 = 60/80 = 0.75
Since p4 ≠ 0 and r < t2: t2 = min(0.7, 0.75) = 0.7

_Step 6: Check result_
Since t1(0.3) < t2(0.7), the line is partially inside.

_Step 7: Calculate clipped endpoints_
x(t1) = 50 + 0.3 × 100 = 80
y(t1) = 20 + 0.3 × 80 = 44
x(t2) = 50 + 0.7 × 100 = 120
y(t2) = 20 + 0.7 × 80 = 76

**Result**: Clipped line from (80, 44) to (120, 76).

### Example 3: Trivial Rejection Case

**Problem**: Determine if line from P1(50, 50) to P2(70, 90) is completely inside, outside, or requires clipping for window Xmin=100, Xmax=200, Ymin=100, Ymax=200.

**Solution**:

_For P1(50, 50):_

- Left of window (50 < 100): Bit 4 = 1
- Below window (50 < 100): Bit 2 = 1
- Code: 0101

_For P2(70, 90):_

- Left of window (70 < 100): Bit 4 = 1
- Below window (90 < 100): Bit 2 = 1
- Code: 0101

_Trivial Rejection Check:_
0101 AND 0101 = 0101 (non-zero)

**Result**: The line is completely outside the window and should be rejected.

## Exam Tips

1. **Remember the region code bit positions**: Always memorize that bits are assigned as Top(1), Bottom(2), Right(4), Left(8) or their binary equivalents (1000, 0100, 0010, 0001).

2. **Know when to accept or reject**: If both endpoint codes are 0000, accept immediately. If bitwise AND of codes is non-zero, reject immediately.

3. **Cohen-Sutherland is most frequently asked**: This algorithm appears most commonly in exams. Ensure you can work through it completely.

4. **Liang-Barsky is more efficient**: Remember that Liang-Barsky uses parametric approach and is faster than Cohen-Sutherland for single line clipping.

5. **Intersection formulas are important**: For Cohen-Sutherland, remember t = (boundary - coord1) / (coord2 - coord1).

6. **Understand the relationship**: The window-to-viewport transformation uses proportional mapping, which often appears in exam questions.

7. **Practice numerical problems**: Most questions require manual calculation, so practice working through examples completely.
