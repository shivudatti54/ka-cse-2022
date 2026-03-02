# DDA Algorithm - Summary

## Key Definitions and Concepts

- **DDA (Digital Differential Analyzer) Algorithm**: An incremental line drawing algorithm that uses differential equations to compute pixel positions along a line segment between two endpoints.
- **Raster Graphics**: Display systems where images are represented as a grid of pixels; requires algorithms to discretize continuous mathematical lines.
- **Slope (m)**: The steepness of a line calculated as m = (y₂ - y₁) / (x₂ - x₁)
- **Incremental Calculation**: Computing successive values by adding a constant increment rather than performing full calculations at each step.

## Important Formulas and Theorems

- **Number of steps**: steps = max(|Δx|, |Δy|) where Δx = x₂ - x₁ and Δy = y₂ - y₁
- **x-increment**: xinc = Δx / steps
- **y-increment**: yinc = Δy / steps
- **Pixel plotting**: At each step, plot at (round(x), round(y))
- **Decision rule**: If |m| ≤ 1, step along x-axis; if |m| > 1, step along y-axis

## Key Points

1. The DDA algorithm replaces expensive multiplication with simple addition by maintaining running values of x and y.
2. Always step along the axis with the greater change to avoid gaps in the line representation.
3. The algorithm handles all line orientations including horizontal, vertical, and diagonal lines.
4. Floating-point arithmetic is used for incremental calculations, with rounding applied when plotting pixels.
5. The algorithm derives from analog differential analyzers that solved equations through incremental steps.
6. DDA is conceptually simpler than Bresenham's algorithm but less efficient due to floating-point operations.
7. For lines with |m| = 1 (diagonal), both axes change equally and either approach works.
8. The algorithm produces smooth lines but may accumulate rounding errors over long distances.

## Common Mistakes to Avoid

1. **Using |Δx| as steps instead of max(|Δx|, |Δy|)**: This causes gaps in steep lines.
2. **Forgetting to round coordinates**: Plotting without rounding results in inaccurate line placement.
3. **Not swapping axes for steep lines**: Attempting to step along x for steep lines creates discontinuous pixels.
4. **Ignoring negative slopes**: The algorithm must handle negative slopes correctly by preserving sign in increments.

## Revision Tips

1. Practice solving DDA problems with different line orientations: gentle positive slope, steep positive slope, gentle negative slope, horizontal, and vertical lines.
2. Remember the decision rule: compare |Δx| with |Δy| to determine stepping direction.
3. When reviewing, always calculate Δx, Δy, steps, xinc, and yinc before generating pixel coordinates.
4. Understand the conceptual difference between DDA (incremental floating-point) and Bresenham (integer-only) to answer comparison questions effectively.
