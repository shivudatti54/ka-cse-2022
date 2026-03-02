# Line Drawing Algorithms - Summary

## Key Definitions and Concepts

- **Raster Display**: A display system consisting of a finite grid of pixels that are illuminated to create images.
- **Line Drawing**: The process of determining which pixels to illuminate to represent a straight line between two endpoints on a discrete grid.
- **DDA (Digital Differential Analyzer) Algorithm**: A line drawing algorithm that uses floating-point arithmetic to increment along the line by equal steps.
- **Bresenham's Line Algorithm**: An efficient line drawing algorithm that uses only integer arithmetic to determine pixel positions.
- **Decision Parameter**: A variable used in Bresenham's algorithm to determine whether the next pixel should be at the same level or at the next level.

## Important Formulas and Theorems

- **DDA Step Calculation**:
  - Steps = max(|Δx|, |Δy|)
  - x_increment = Δx / steps
  - y_increment = Δy / steps

- **Bresenham's Algorithm Formulas (Shallow lines)**:
  - Initial parameter: P₀ = 2Δy - Δx
  - If Pᵢ ≥ 0: Pᵢ₊₁ = Pᵢ + 2Δy - 2Δx (choose upper pixel)
  - If Pᵢ < 0: Pᵢ₊₁ = Pᵢ + 2Δy (choose lower pixel)

- **Bresenham's Algorithm Formulas (Steep lines)**:
  - Initial parameter: P₀ = 2Δx - Δy
  - If Pᵢ ≥ 0: Pᵢ₊₁ = Pᵢ + 2Δx - 2Δy (choose upper pixel)
  - If Pᵢ < 0: Pᵢ₊₁ = Pᵢ + 2Δx (choose lower pixel)

## Key Points

- Line drawing algorithms convert continuous mathematical lines into discrete pixel representations.
- The DDA algorithm uses floating-point arithmetic and rounding operations, making it computationally expensive.
- Bresenham's algorithm is the industry standard due to its use of only integer arithmetic.
- For lines where |Δx| > |Δy|, we increment x by 1 and decide y; for steeper lines, we increment y by 1 and decide x.
- Bresenham's algorithm produces lines visually identical to ideal lines while minimizing computational overhead.
- The decision parameter in Bresenham's algorithm compares the midpoint between candidate pixels with the ideal line position.
- All line drawing algorithms have O(n) complexity where n is the length of the line in pixels.

## Common Mistakes to Avoid

1. Forgetting to swap axes for steep lines (when |Δy| > |Δx|) and using the wrong set of formulas.
2. Confusing the update formulas for the decision parameter—always verify whether you're using the correct case (P ≥ 0 or P < 0).
3. Using floating-point arithmetic in Bresenham's algorithm when the entire point is to use integer operations.
4. Not properly handling lines with negative slopes or lines in different quadrants.

## Revision Tips

1. Practice at least three complete numerical examples of Bresenham's algorithm covering different cases.
2. Memorize the initial decision parameter formulas: P₀ = 2Δy - Δx for shallow, P₀ = 2Δx - Δy for steep.
3. Remember the key advantage of Bresenham: integer arithmetic only, no rounding errors.
4. Understand the geometric interpretation: choosing pixels based on which side of the midpoint the ideal line passes through.
5. Review past exam questions on this topic to understand the pattern and level of difficulty expected.
