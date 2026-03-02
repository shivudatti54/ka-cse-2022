# Parallel Line Algorithms - Summary

## Key Definitions and Concepts

- **Raster Display**: A display device where images are composed of an array of pixels arranged in rows and columns.
- **Pixel**: The smallest unit of a digital image that can be displayed and addressed on a raster display.
- **Line Drawing Algorithm**: A procedure to determine which pixels should be illuminated to represent a straight line between two points on a grid.
- **Slope**: The ratio of vertical change to horizontal change between two points (dy/dx), determining the steepness and direction of a line.

## Important Formulas and Theorems

**DDA Algorithm:**

- Number of steps = max(|dx|, |dy|)
- Step sizes: xStep = dx/steps, yStep = dy/steps
- Pixel position = (round(x), round(y))

**Bresenham's Algorithm (0 ≤ slope ≤ 1):**

- Initial decision parameter: P₀ = 2\*dy - dx
- Update: If P < 0, P += 2*dy; else P += 2*dy - 2\*dx

**Midpoint Algorithm:**

- Implicit line equation: Ax + By + C = 0
- Initial decision: d = A + 0.5B (or integer equivalent)
- Update depends on sign of d

## Key Points

1. Line drawing algorithms are essential for rendering straight lines on digital displays where only discrete pixels exist.

2. DDA uses floating-point arithmetic and is conceptually simpler but computationally heavier than integer-based methods.

3. Bresenham's algorithm uses only integer arithmetic, making it extremely efficient and the most widely used algorithm in practice.

4. The Midpoint algorithm achieves similar performance to Bresenham using the implicit equation form of a line.

5. All algorithms require special handling for steep lines (|dy| > |dx|), horizontal lines, vertical lines, and negative slopes.

6. The error in line drawing is measured as the distance between selected pixels and the ideal mathematical line.

7. Bresenham's algorithm minimizes this error by choosing pixels that keep the cumulative error minimal at each step.

8. Hardware implementations of line drawing almost universally use variations of Bresenham's algorithm.

## Common Mistakes to Avoid

1. **Forgetting to handle steep lines**: When |dy| > |dx|, algorithms must step through y coordinates instead of x.

2. **Incorrect initial parameter calculation**: A small error in the initial decision parameter leads to completely incorrect results.

3. **Using floating-point in Bresenham**: Remember that Bresenham's algorithm specifically uses integer arithmetic for efficiency.

4. **Not plotting the starting point**: Always ensure the first endpoint is plotted before entering the main loop.

5. **Confusing update rules**: The conditional update rules for decision parameters are commonly mixed up during exams.

## Revision Tips

1. Practice at least 3-4 problems for each algorithm to become comfortable with the step-by-step procedure.

2. Create a comparison chart of all three algorithms to quickly recall their differences during exams.

3. Memorize the initial decision parameter formulas—they are most frequently asked in questions.

4. Understand why Bresenham works by thinking about the midpoint between candidate pixels rather than memorizing mechanically.

5. Solve previous year questions on this topic to understand the exam pattern and common question types.
