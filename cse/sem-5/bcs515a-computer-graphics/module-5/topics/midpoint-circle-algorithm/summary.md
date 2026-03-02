# Midpoint Circle Algorithm - Summary

## Key Definitions and Concepts

- **Midpoint Circle Algorithm**: An efficient rasterization algorithm that draws circles using only integer arithmetic by evaluating a decision parameter at the midpoint between two candidate pixels.

- **Decision Parameter (p)**: A value that determines whether the midpoint between two candidate pixels lies inside or outside the circle boundary.

- **Circle Equation**: F(x, y) = x² + y² - r², where r is the radius. F(x, y) = 0 indicates the point is on the circle.

- **8-way Symmetry**: Property of circles where points in one octant can be reflected to obtain points in all eight octants.

## Important Formulas and Theorems

- **Initial Decision Parameter**: p₀ = 1 - r (for r ≥ 0)

- **If p < 0 (Midpoint inside circle)**:
  - Next pixel: (x + 1, y)
  - p(new) = p(old) + 2x + 3

- **If p ≥ 0 (Midpoint outside circle)**:
  - Next pixel: (x + 1, y - 1)
  - p(new) = p(old) + 2x - 2y + 5

- **Termination Condition**: Continue while x ≥ y

## Key Points

- The algorithm starts at (r, 0) and proceeds clockwise within the first octant.

- Only integer operations are used, making it highly efficient for hardware implementation.

- For each point (x, y) generated, eight symmetric points are plotted using sign changes and coordinate swapping.

- The algorithm is approximately 3x faster than trigonometric approaches.

- Initial value p₀ = 1 - r is derived from evaluating the decision parameter at starting point (r + 1, 0).

- The x coordinate always increments by 1 at each step; only the y coordinate may stay the same or decrement by 1.

## Common Mistakes to Avoid

- Using floating-point values for coordinates instead of integers; the algorithm is designed for integer arithmetic.

- Forgetting to plot symmetric points in all eight octants, resulting in incomplete circles.

- Not updating the x value in the decision parameter calculation after selecting a new pixel.

- Using the wrong update formula based on the sign of the decision parameter.

- Confusing the termination condition; stopping when x < y rather than x ≥ y.

## Revision Tips

- Practice calculating at least 5-6 iterations manually to understand the pattern of decision parameter updates.

- Remember the symmetry property: for point (x, y), also plot (±x, ±y) and (±y, ±x).

- Memorize both update formulas and the initial condition p₀ = 1 - r.

- Solve previous year exam questions to familiarise with the problem-solving approach.
