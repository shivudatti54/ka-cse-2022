# Circle and Ellipse Drawing Algorithms

## Introduction

Computer graphics fundamentally relies on the ability to render basic geometric shapes efficiently and accurately. Among these shapes, circles and ellipses are essential primitives used in UI design, game development, CAD applications, and scientific visualization. Drawing perfect circles and ellipses on a raster display (pixel grid) requires specialized algorithms because the continuous mathematical definition must be mapped to discrete pixel positions.

In this topic, we explore the fundamental algorithms for generating circles and ellipses: the **Midpoint Circle Algorithm** (an extension of Bresenham's line algorithm), **Bresenham's Circle Algorithm**, and the **Midpoint Ellipse Algorithm**. These algorithms minimize computational complexity by making incremental decisions based on a midpoint test, ensuring pixel-perfect approximations of these curved shapes.

Understanding these algorithms is crucial for the DU Computer Science curriculum, as they form the foundation for more advanced rendering techniques in computer graphics.

## Key Concepts

### 1. Fundamental Principles

The challenge in drawing circles and ellipses on a pixel grid lies in maintaining a smooth, continuous appearance while minimizing calculations. Both circles and ellipses exhibit symmetry that can be exploited:

- **Eight-way symmetry** for circles: Points in all eight octants can be computed from just one-eighth of the circle.
- **Four-way symmetry** for ellipses: Points in all four quadrants can be computed from just one quadrant.

### 2. Circle Equation

A circle with center (0,0) and radius r is defined by:
$$x^2 + y^2 = r^2$$

For drawing, we solve for y:
$$y = \sqrt{r^2 - x^2}$$

However, computing square roots at each step is computationally expensive. The midpoint algorithms avoid this by using a decision parameter.

### 3. Midpoint Circle Algorithm

The Midpoint Circle Algorithm (also known as the **Midpoint Circle Algorithm** or a variation of Bresenham's approach) plots points in the first octant and uses symmetry to fill the rest.

**Algorithm Steps:**

1. Start with coordinates (x, y) = (r, 0)
2. Initialize the decision parameter: $P = 1 - r$ (for r ≥ 1)
3. For each x position (starting from r and decrementing):
   - Plot the point (x, y) and its symmetric counterparts in all 8 octants
   - If P < 0: The midpoint is inside the circle. Choose the eastern point (x-1, y).
     Update: $P = P + 2(x_{new}) + 1$
   - If P ≥ 0: The midpoint is outside/on circle. Choose the southern point (x-1, y-1).
     Update: $P = P + 2(x_{new}) + 1 - 2(y_{new})$

4. Repeat until x < y

### 4. Bresenham's Circle Algorithm

Bresenham's Circle Algorithm uses integer arithmetic and a decision parameter based on the difference between two candidate pixel positions.

**Decision Parameter:** $d = (x+1)^2 + y^2 - r^2$ (comparing midpoint to radius squared)

**Algorithm:**

1. Initialize: x = 0, y = r, d = 2(1-r)
2. While y > x:
   - Plot (x, y) and 7 symmetric points
   - If d < 0: Next point is (x+1, y)
     Update: d = d + 2x + 3
   - Else: Next point is (x+1, y-1)
     Update: d = d + 2x - 2y + 5
   - Increment x

### 5. Ellipse Equation

An ellipse with center (0,0), semi-major axis rx (along x) and semi-minor axis ry (along y) is defined by:
$$\frac{x^2}{rx^2} + \frac{y^2}{ry^2} = 1$$

### 6. Midpoint Ellipse Algorithm

This algorithm divides the ellipse drawing into two regions based on the slope:

- **Region 1:** Where the slope magnitude > 1 (steeper in y-direction)
- **Region 2:** Where the slope magnitude ≤ 1 (flatter in y-direction)

The transition point occurs where: $dy/dx = -1$

**Algorithm Steps:**

1. Initialize: x = 0, y = ry
2. Calculate initial decision parameters:
   - $P1 = ry^2 - rx^2 \cdot ry + \frac{1}{4}rx^2$ (for Region 1)
3. **Region 1** (while $2 \cdot ry^2 \cdot x < 2 \cdot rx^2 \cdot y$):
   - Plot points in quadrant 1 and mirror to others
   - Update based on P1 value
4. **Region 2** (after transition):
   - Calculate initial P2: $P2 = ry^2(x+\frac{1}{2})^2 + rx^2(y-1)^2 - rx^2 \cdot ry^2$
   - Continue plotting until y = 0

## Examples

### Example 1: Midpoint Circle Algorithm for r = 10

**Step-by-step calculation:**

Initial: x = 10, y = 0, P = 1 - 10 = -9

| Step | x | y | P | Decision | Next Point |
|------|---|----|---|----------|------------|
| 1 | 10 | 0 | -9 | P < 0, choose E | (9, 0) |
| 2 | 9 | 0 | P = -9 + 2(9) + 1 = 10 | P ≥ 0, choose SE | (8, 1) |
| 3 | 8 | 1 | P = 10 + 2(8) + 1 - 2(1) = 25 | P ≥ 0, choose SE | (7, 2) |
| 4 | 7 | 2 | P = 25 + 2(7) + 1 - 2(2) = 33 | P ≥ 0, choose SE | (6, 3) |
| 5 | 6 | 3 | P = 33 + 2(6) + 1 - 2(3) = 34 | P ≥ 0, choose SE | (5, 4) |
| 6 | 5 | 4 | P = 34 + 2(5) + 1 - 2(4) = 27 | P ≥ 0, choose SE | (4, 5) |

Stop when x ≥ y (5 ≥ 4, continue)

The algorithm generates pixel positions approximating a circle of radius 10.

### Example 2: Midpoint Ellipse Algorithm for rx = 8, ry = 6

**Step 1: Region 1 (slope > 1)**

Initial: x = 0, y = 6
P1 = 6² - 8² × 6 + (1/4) × 8² = 36 - 384 + 16 = -332

While 2×6²×x < 2×8²×y (i.e., 72x < 128y):

| Step | x | y | P1 | Decision |
|------|---|---|-----|----------|
| 1 | 0 | 6 | -332 | P1 < 0, E: (1,6) |
| 2 | 1 | 6 | -332 + 72×1 + 1 = -259 | P1 < 0, E: (2,6) |
| 3 | 2 | 6 | -259 + 144 + 1 = -114 | P1 < 0, E: (3,6) |
| 4 | 3 | 6 | -114 + 216 + 1 = 103 | P1 ≥ 0, SE: (4,5) |

Transition: Since 2×72×4 = 576 ≥ 2×64×5 = 640 is false, continue in Region 1.

**Step 2: Region 2**

Continue with y decreasing until y = 0, using P2 decision parameter.

### Example 3: Bresenham's Circle for r = 5

**Step-by-step:**

Initial: x = 0, y = 5, d = 2(1-5) = -8

| Step | x | y | d | Plot | Next |
|------|---|---|---|------|------|
| 1 | 0 | 5 | -8 | (0,5) | E: (1,5), d = -8 + 3 = -5 |
| 2 | 1 | 5 | -5 | (1,5) | E: (2,5), d = -5 + 5 = 0 |
| 3 | 2 | 5 | 0 | (2,5) | SE: (3,4), d = 0 + 10 - 10 + 5 = 5 |
| 4 | 3 | 4 | 5 | (3,4) | SE: (4,3), d = 5 + 14 - 8 + 5 = 16 |

Stop when x ≥ y (4 ≥ 3 - stop after this step, but continue checking)

Final points in first octant: (0,5), (1,5), (2,5), (3,4), (4,3)

## Exam Tips

1. **Understand the symmetry properties**: Remember circles have 8-way symmetry and ellipses have 4-way symmetry—this is crucial for algorithm efficiency and exam questions.

2. **Decision parameter initialization**: For Midpoint Circle Algorithm, remember P = 1 - r. For Bresenham's, remember d = 2(1-r).

3. **Region transitions in ellipse algorithm**: Know that the transition from Region 1 to Region 2 occurs when $2 \cdot ry^2 \cdot x \geq 2 \cdot rx^2 \cdot y$.

4. **Integer arithmetic advantage**: Bresenham's algorithms use only integer addition, subtraction, and bit shifting (multiplication by 2), making them extremely fast.

5. **Difference between algorithms**: Midpoint algorithms use a geometric midpoint test, while Bresenham's minimizes the distance between circle/ellipse and pixel centers.

6. **Drawing order**: Always plot points in the first quadrant and mirror to other quadrants/octants—this reduces computation by factor of 8 for circles.

7. **Termination condition**: For circles, terminate when x ≥ y. For ellipses, terminate when y becomes 0 in Region 2.

8. **Handle special case r = 0**: Remember to handle degenerate cases where radius equals 0.

9. **Anti-aliasing (advanced)**: While not in core syllabus, know that basic algorithms produce aliased (jagged) edges; advanced techniques like Wu's algorithm provide anti-aliased circles.

10. **Time complexity**: All these algorithms run in O(r) time, where r is the radius, making them highly efficient compared to naive approaches.