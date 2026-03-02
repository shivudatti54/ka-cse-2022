# Circle Generating Algorithms - Summary

## Key Definitions and Concepts

- **Circle Equation**: (x - xc)² + (y - yc)² = r², where (xc, yc) is the center and r is the radius
- **Eight-Way Symmetry**: Property allowing one computed point to generate seven additional symmetric points
- **Decision Parameter (P)**: Value used to determine which pixel (East or Southeast) is closer to the actual circle boundary
- **Midpoint Circle Algorithm**: Incremental algorithm using midpoint evaluation to plot optimal pixel positions

## Important Formulas and Theorems

- **Initial Decision Parameter**: P₀ = 1 - r (for Midpoint Algorithm)
- **If P < 0** (midpoint inside): x = x + 1, P_new = P + 2x + 3
- **If P ≥ 0** (midpoint outside): x = x + 1, y = y - 1, P_new = P + 2x - 2y + 5
- **Stopping Condition**: Continue while x < y

## Key Points

- Circles have eight-way symmetry: if (x, y) is on the circle, so are (±x, ±y) and (±y, ±x)
- The algorithm only needs to compute one octant (1/8th) of the circle and mirror the results
- Starting point is always (0, r) at the top of the circle
- The algorithm avoids expensive trigonometric and square root operations
- Each iteration plots 8 symmetric points simultaneously
- When x reaches y, plot the final point explicitly to complete the circle

## Common Mistakes to Avoid

- Forgetting to increment x before calculating the new decision parameter in the update formulas
- Using the wrong initial decision parameter value (commonly confused with Bresenham's line algorithm)
- Not plotting the final point when x equals y
- Confusing the pixel selection criteria (P < 0 means choose East, not Southeast)
- Attempting to calculate using actual distances instead of the decision parameter approach

## Revision Tips

- Practice tracing through the algorithm with small radii (r = 3, 5, 6) to understand the step-by-step execution
- Memorize the initial parameter (1 - r) and both update formulas as they are frequently asked in exams
- Remember that x always increments by 1, while y either stays same or decrements by 1
- Focus on understanding why the algorithm works rather than just memorizing the steps
- Review the relationship between the decision parameter and the geometric midpoint
