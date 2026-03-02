# Circle Generating Algorithms

## Introduction

Circle-generating algorithms form a fundamental component of computer graphics, enabling the efficient and accurate rendering of circular shapes on raster display systems. Circles are ubiquitous in graphical applications, from simple UI elements like buttons and icons to complex engineering drawings, game graphics, and scientific visualizations. Unlike line drawing where we can use simple interpolation, drawing circles presents unique challenges due to the mathematical nature of the circle equation and the discrete nature of pixel grids.

The primary challenge in circle generation arises from the need to plot pixels at integer coordinates that best approximate the ideal mathematical circle. Since pixel positions are discrete (integer values), we cannot plot every point that satisfies the circle equation. Instead, we must select specific pixel positions that create the closest approximation to a true circle. This problem becomes particularly interesting because circles have eight-way symmetry - if we can compute pixels for one octant, we can mirror them to generate the complete circle.

For the university's Computer Graphics curriculum, understanding circle-generating algorithms is essential because these algorithms demonstrate fundamental optimization techniques used throughout computer graphics. The algorithms discussed here - particularly the Midpoint Circle Algorithm and Bresenham's Circle Algorithm - are direct applications of incremental calculation techniques that minimize computational complexity. These same principles extend to ellipse generation, curve rendering, and many other areas of computer graphics.

## Key Concepts

### Properties of a Circle

A circle is defined as the set of all points in a plane that are at a fixed distance (radius r) from a fixed point (center at coordinates (xc, yc)). The standard equation of a circle with center (xc, yc) and radius r is:

(x - xc)² + (y - yc)² = r²

This equation represents the ideal mathematical circle. When rendering on a raster display, we must select integer pixel coordinates (x, y) that best approximate this curve.

**Eight-Way Symmetry**: A crucial property that makes circle drawing efficient is that circles exhibit eight-way symmetry. This means if we know a point (x, y) on the circle, we can determine seven other points without additional computation:

- (x, y), (-x, y), (x, -y), (-x, -y)
- (y, x), (-y, x), (y, -x), (-y, -x)

This symmetry allows us to compute pixel positions for only one-eighth of the circle (typically the octant from 0 to 45 degrees) and mirror them to generate the complete circle, reducing computational work by approximately 87.5%.

### Midpoint Circle Algorithm

The Midpoint Circle Algorithm, developed by Jack Bresenham (also known as Bresenham's Circle Algorithm), is the most widely taught and implemented algorithm for circle generation. It uses the concept of the midpoint between two candidate pixels to determine which pixel is closer to the actual circle boundary.

**The Decision Parameter:**

For the second octant (where x increases from 0 to r and y decreases from r to 0), we start at position (0, r) and proceed by choosing between two positions:

- East pixel: (x + 1, y)
- Southeast pixel: (x + 1, y - 1)

The circle equation evaluated at the midpoint (x + 1, y - 0.5) gives us the decision parameter P:

P = f(x + 1, y - 0.5) = (x + 1)² + (y - 0.5)² - r²

If P < 0, the midpoint is inside the circle, so we choose the East pixel (x + 1, y).
If P ≥ 0, the midpoint is outside (or on) the circle, so we choose the Southeast pixel (x + 1, y - 1).

**Algorithm Steps:**

1. Initialize: x = 0, y = r, P = 1 - r (initial decision parameter)
2. Plot the initial point at (x, y) and its symmetric points
3. Repeat while x < y:

- If P < 0: x = x + 1, P = P + 2x + 3 (next decision parameter)
- Else: x = x + 1, y = y - 1, P = P + 2x - 2y + 5
- Plot all eight symmetric points

**Why P = 1 - r?**

The initial decision parameter is derived by evaluating the circle equation at the first midpoint (1, r - 0.5):
P₀ = (1)² + (r - 0.5)² - r²
P₀ = 1 + r² - r + 0.25 - r²
P₀ = 1.25 - r
P₀ = 1 - r (rounded)

### Bresenham's Circle Algorithm

Bresenham's Circle Algorithm is essentially the same as the Midpoint Circle Algorithm, with slight variations in the decision parameter calculation. It uses an error term approach to determine which pixel to plot next.

**Algorithm Steps:**

1. Initialize: x = 0, y = r, d = 3 - 2r (decision parameter)
2. Plot circle points at (x, y) and all symmetric positions
3. Repeat while x ≤ y:

- Increment x by 1
- If d < 0: d = d + 4x + 6 (choose East pixel)
- Else: y = y - 1, d = d + 4(x - y) + 10 (choose Southeast pixel)
- Plot all eight symmetric points

The decision parameter d is essentially comparing the squared distances from the ideal circle to the two candidate pixels, avoiding the expensive square root calculations.

### Comparison of Circle Drawing Algorithms

| Algorithm          | Complexity        | Accuracy | Implementation  |
| ------------------ | ----------------- | -------- | --------------- |
| Direct Equation    | O(n) with sqrt    | High     | Simple but slow |
| Midpoint/Bresenham | O(n) without sqrt | Good     | Efficient       |
| Trigonometric      | O(n) with sin/cos | Good     | Simple but slow |

The Midpoint and Bresenham algorithms are preferred because they avoid expensive floating-point trigonometric and square root operations, making them highly efficient for real-time graphics applications.

## Examples

### Example 1: Drawing a Circle with Radius 10 using Midpoint Algorithm

**Step-by-step solution:**

Starting point: (0, 10)
Initial decision parameter: P₀ = 1 - r = 1 - 10 = -9

**Iteration 1:** x = 0, y = 10, P = -9

- Since P < 0, choose East pixel
- x = 1, P = -9 + 2(0) + 3 = -6
- Points: (1, 10), (-1, 10), (1, -10), (-1, -10), (10, 1), (-10, 1), (10, -1), (-10, -1)

**Iteration 2:** x = 1, y = 10, P = -6

- Since P < 0, choose East pixel
- x = 2, P = -6 + 2(1) + 3 = -1
- Points: (2, 10), (10, 2), and their symmetries

**Iteration 3:** x = 2, y = 10, P = -1

- Since P < 0, choose East pixel
- x = 3, P = -1 + 2(2) + 3 = 6
- Points: (3, 10), (10, 3), and their symmetries

**Iteration 4:** x = 3, y = 10, P = 6

- Since P ≥ 0, choose Southeast pixel
- x = 4, y = 9, P = 6 + 2(3) - 2(9) + 5 = 6 + 6 - 18 + 5 = -1
- Points: (4, 9), (9, 4), and their symmetries

**Continue until x ≥ y...**

### Example 2: Circle with Radius 6

Initial: x = 0, y = 6, P₀ = 1 - 6 = -5

| Iteration | x   | y   | P   | Decision     | Next P             |
| --------- | --- | --- | --- | ------------ | ------------------ |
| 1         | 0   | 6   | -5  | East         | -5 + 3 = -2        |
| 2         | 1   | 6   | -2  | East         | -2 + 5 = 3         |
| 3         | 2   | 6   | 3   | Southeast    | 3 + 4 - 10 + 5 = 2 |
| 4         | 3   | 5   | 2   | Southeast    | 2 + 6 - 8 + 5 = 5  |
| 5         | 4   | 4   | 5   | Stop (x ≥ y) | -                  |

### Example 3: Converting Midpoint to Pseudocode

```
procedure drawCircle(radius)
 x = 0
 y = radius
 P = 1 - radius

 while x < y
 plotPoints(x, y)

 if P < 0
 x = x + 1
 P = P + 2*x + 3
 else
 x = x + 1
 y = y - 1
 P = P + 2*x - 2*y + 5
 end if
 end while

 if x == y
 plotPoints(x, y)
 end if
end procedure
```

## Exam Tips

1. **Remember the initial decision parameter**: For Midpoint Circle Algorithm, P₀ = 1 - r. This is a frequently asked question in university exams.

2. **Understand the decision logic**: If P < 0, the midpoint is inside the circle → choose East pixel. If P ≥ 0, the midpoint is outside → choose Southeast pixel.

3. **Update formulas are crucial**:

- After East pixel: P_new = P + 2x + 3
- After Southeast pixel: P_new = P + 2x - 2y + 5

Note that x is incremented before calculating the new P.

4. **Eight-way symmetry is key**: Remember that plotting one point gives you 8 points automatically. This reduces computation by factor of 8.

5. **Know when to stop**: The algorithm continues until x ≥ y (reaching the 45-degree line in the first octant).

6. **Initial point is always (0, r)**: The circle drawing starts at the "top" of the circle at position (0, r).

7. **Difference between algorithms**: Bresenham's uses d = 3 - 2r as initial parameter, while Midpoint uses 1 - r. Both produce similar results but differ slightly in calculation.

8. **Plot the final point**: When x == y, plot that point explicitly to avoid missing it in the loop condition.

9. **Avoid expensive operations**: These algorithms are efficient because they avoid trigonometric functions and square roots by using incremental calculations.

10. **Understand the geometric interpretation**: The decision parameter essentially compares the distance from the ideal circle to the two candidate pixel centers.
