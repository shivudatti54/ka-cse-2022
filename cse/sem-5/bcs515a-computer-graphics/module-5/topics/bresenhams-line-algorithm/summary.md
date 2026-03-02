# Bresenham's Line Algorithm - Summary

## Key Definitions and Concepts

- **Raster Display**: A display device consisting of discrete pixels arranged in a grid, requiring algorithms to approximate continuous mathematical lines.

- **Decision Parameter (Pk)**: A value used to determine which pixel (y or y+1) is closer to the true line at each x-position. It represents twice the signed distance from the line to the decision point.

- **First Octant**: The region where 0 ≤ slope ≤ 1 and Δx > Δy, which is the primary case handled by Bresenham's algorithm.

- **Incremental Algorithm**: An algorithm that computes each step from the previous step using simple additions, avoiding redundant calculations.

## Important Formulas and Theorems

- **Initial Decision Parameter**: P₀ = 2Δy - Δx

- **Slope Calculation**: m = Δy/Δx where Δx = x₁ - x₀ and Δy = y₁ - y₀

- **Update Formula (Pk < 0)**: Pk₊₁ = Pk + 2Δy — choose pixel at (xₖ₊₁, yₖ)

- **Update Formula (Pk ≥ 0)**: Pk₊₁ = Pk + 2Δy - 2Δx — choose pixel at (xₖ₊₁, yₖ₊₁)

- **Pixel Selection Rule**: If Pk < 0, plot lower pixel; if Pk ≥ 0, plot upper pixel.

## Key Points

- Bresenham's algorithm uses only integer arithmetic, making it significantly faster than floating-point-based algorithms like DDA.

- The algorithm minimizes the error between the actual mathematical line and the selected pixels, producing visually smooth lines.

- The basic algorithm works for lines with slope between 0 and 1 in the first octant; modifications are needed for other octants.

- The decision parameter Pk is always an integer because 2Δy and 2Δx are integers when Δx and Δy are integers.

- For steep lines (|Δy| > |Δx|), the algorithm iterates along the y-axis instead of the x-axis.

- Bresenham's algorithm is the industry standard for hardware implementations of line drawing due to its efficiency.

- The algorithm can be extended to draw circles (Bresenham's circle algorithm) and other curves.

## Common Mistakes to Avoid

1. **Confusing the decision threshold**: Remember that Pk < 0 chooses y (lower pixel), while Pk ≥ 0 chooses y+1 (upper pixel).

2. **Forgetting to plot the endpoint**: Both the starting and ending pixels must be plotted; the algorithm stops at x = x₁.

3. **Using wrong update formulas**: Ensure you use the correct update formula based on the sign of Pk at each step.

4. **Ignoring octant handling**: The basic algorithm only works for the first octant; don't apply it blindly to all lines.

5. **Calculation errors in decision parameter**: Always double-check initial P₀ and subsequent Pk calculations.

## Revision Tips

1. Practice tracing through the algorithm with at least 3-4 different examples, including lines with different slopes.

2. Memorize the initial formula P₀ = 2Δy - Δx and the two update formulas as they are frequently tested.

3. Draw pixel grids to visualize the line drawing process and verify your traced results.

4. Compare Bresenham's algorithm with DDA to understand why integer arithmetic is preferable in graphics.

5. Review how to handle negative slopes and steep lines by considering coordinate transformations.
