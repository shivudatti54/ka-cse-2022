# Midpoint Circle Algorithm

## Introduction

The Midpoint Circle Algorithm is a fundamental rasterization technique used in computer graphics to draw circles on a pixel-based display. Developed as an improvement over trigonometric methods, this algorithm efficiently generates the points that form the circumference of a circle using only integer arithmetic. The algorithm was pioneered by Jack Bresenham and is sometimes referred to as the Bresenham's Circle Algorithm.

In computer graphics, circle drawing is essential for various applications including GUI design, game development, CAD software, and scientific visualization. Unlike lines where we can directly interpolate between endpoints, circles require careful consideration because the relationship between x and y coordinates is non-linear. The Midpoint Circle Algorithm solves this problem by using a decision parameter that determines which pixel (between two candidates) is closer to the actual circle at each step, ensuring smooth and accurate circle rendering with minimal computational overhead.

The algorithm exploits the 8-way symmetry of a circle, meaning we only need to calculate points for one octant (45-degree segment) and then reflect these points to obtain the complete circle. This symmetry property makes it significantly faster than trigonometric approaches that require expensive sine and cosine calculations for every point.

## Key Concepts

### Circle Equation

A circle with center (0, 0) and radius r is defined by the equation:

**x² + y² = r²**

For any point (x, y), we can determine whether it lies inside, on, or outside the circle by evaluating:

- **F(x, y) = x² + y² - r²**
- If F(x, y) = 0, the point lies exactly on the circle
- If F(x, y) < 0, the point lies inside the circle
- If F(x, y) > 0, the point lies outside the circle

### Decision Parameter

The Midpoint Circle Algorithm starts from the point (r, 0) and proceeds in the clockwise direction within the first octant. At each step, we have two candidate pixels:

- **P1 = (x + 1, y)** - East pixel
- **P2 = (x + 1, y - 1)** - Southeast pixel

The decision parameter (p) is calculated at the midpoint between these two candidates:

**p = F(x + 1, y - 0.5) = (x + 1)² + (y - 0.5)² - r²**

Simplifying:
**p = x² + 2x + 1 + y² - y + 0.25 - r²**
**p = (x² + y² - r²) + 2x + 1 - y + 0.25**

### Algorithm Steps

1. **Initialize**: Set starting point at (r, 0) and calculate initial decision parameter:

- p₀ = 1 - r (for r ≥ 0)

2. **Iteration**: For each step while x ≥ y:

- If p < 0: The midpoint is inside the circle, so choose the East pixel (x + 1, y)
- Next point: (x + 1, y)
- Update: p = p + 2x + 3
- If p ≥ 0: The midpoint is outside the circle, so choose the Southeast pixel (x + 1, y - 1)
- Next point: (x + 1, y - 1)
- Update: p = p + 2x - 2y + 5

3. **Symmetry**: Plot the calculated points in all 8 octants by changing signs and swapping coordinates

4. **Translation**: Add the circle center coordinates (h, k) to all points

### Example with Decision Parameter Calculation

For a circle with radius r = 10:

- **Initial point**: (10, 0)
- **Initial decision parameter**: p₀ = 1 - r = 1 - 10 = -9

**Step 1**: p₀ = -9 < 0

- Choose pixel at (x + 1, y) = (11, 0)
- Next p = p + 2x + 3 = -9 + 2(10) + 3 = -9 + 20 + 3 = 14
- Points in all octants: (±10, 0), (0, ±10), (±10, 0)

**Step 2**: p = 14 ≥ 0

- Choose pixel at (x + 1, y - 1) = (11, -1)
- Next p = p + 2x - 2y + 5 = 14 + 20 - 2(0) + 5 = 39

**Step 3**: p = 39 ≥ 0

- Choose pixel at (12, -1)
- Next p = 39 + 22 - 2(-1) + 5 = 68

And so on until x ≥ y.

## Examples

### Example 1: Drawing Circle with Radius 5

**Problem**: Use the Midpoint Circle Algorithm to find all pixels for drawing a circle with radius 5 centered at origin.

**Solution**:

**Step 1: Initialize**

- Starting point: (x, y) = (5, 0)
- Initial decision parameter: p₀ = 1 - r = 1 - 5 = -4

**Step 2: Iteration 1**

- p₀ = -4 < 0
- Plot point (6, 0)
- Next p = -4 + 2(5) + 3 = -4 + 10 + 3 = 9

**Step 3: Iteration 2**

- p = 9 ≥ 0
- Plot point (6, -1)
- Next p = 9 + 2(6) - 2(0) + 5 = 9 + 12 + 5 = 26

**Step 4: Iteration 3**

- p = 26 ≥ 0
- Plot point (7, -1)
- Next p = 26 + 2(7) - 2(-1) + 5 = 26 + 14 + 2 + 5 = 47

**Step 5: Iteration 4**

- p = 47 ≥ 0
- Plot point (7, -2)
- Next p = 47 + 2(7) - 2(0) + 5 = 47 + 14 + 4 + 5 = 70

**Step 6: Iteration 5**

- p = 70 ≥ 0
- Plot point (8, -2)
- Next p = 70 + 2(8) - 2(-1) + 5 = 70 + 16 + 2 + 5 = 93

Since x = 8 > y = 2, we stop for the first octant.

**Plotted points in first octant**: (5,0), (6,0), (6,-1), (7,-1), (7,-2), (8,-2)

Using 8-way symmetry, the complete circle pixels are generated.

### Example 2: Radius 8 Circle

**Problem**: Calculate the first three decision parameter values for a circle with radius 8.

**Solution**:

**Initialize**:

- Start point: (8, 0)
- p₀ = 1 - r = 1 - 8 = -7

**First iteration**: p₀ = -7 < 0

- Select pixel (9, 0)
- p₁ = p₀ + 2x + 3 = -7 + 2(8) + 3 = -7 + 16 + 3 = 12

**Second iteration**: p₁ = 12 ≥ 0

- Select pixel (9, -1)
- p₂ = p₁ + 2x - 2y + 5 = 12 + 2(9) - 2(0) + 5 = 12 + 18 + 5 = 35

**Third iteration**: p₂ = 35 ≥ 0

- Select pixel (10, -1)
- p₃ = p₂ + 2x - 2y + 5 = 35 + 2(10) - 2(-1) + 5 = 35 + 20 + 2 + 5 = 62

## Exam Tips

1. **Remember the initial decision parameter formula**: p₀ = 1 - r (for r ≥ 0), which is the most commonly asked formula in exams.

2. **Understand when to use which update formula**: If p < 0, use p + 2x + 3 (East pixel); if p ≥ 0, use p + 2x - 2y + 5 (Southeast pixel).

3. **Know the termination condition**: Continue plotting while x ≥ y, which ensures we cover exactly one octant.

4. **8-way symmetry is crucial**: Remember that for each calculated point (x, y), you must plot points in all eight octants by changing signs and swapping coordinates.

5. **Watch for the radius value**: For very small radii (r = 0, 1), the algorithm may need special handling or may not produce meaningful results.

6. **Common mistake to avoid**: Always increment x by 1 at each step - the algorithm always moves to x + 1, never just changing y.

7. **Translation to arbitrary center**: After generating points for a circle centered at origin, add the center coordinates (h, k) to all points to shift the circle.

8. **Comparison with other algorithms**: Be prepared to explain why Midpoint Circle Algorithm is better than trigonometric methods (uses only integer arithmetic, no floating-point operations, more efficient).
