# Raster Scan Line Algorithms - Summary

## Key Definitions and Concepts

- **Raster Display**: A display system where the screen is composed of a grid of pixels arranged in rows and columns; each pixel is identified by its (x, y) coordinates.

- **Pixel**: The smallest unit of a raster image; a discrete picture element that can be illuminated with a specific color.

- **Resolution**: The total number of pixels on a display, typically expressed as width × height (e.g., 1920×1080).

- **Line Drawing Algorithm**: An algorithm that determines which pixels should be illuminated to create the visual impression of a straight line between two endpoints.

- **Decision Parameter**: A value used in Bresenham's and Midpoint algorithms to determine which pixel to plot next based on the proximity to the ideal line or curve.

## Important Formulas and Theorems

**DDA Algorithm:**
- Steps = max(|Δx|, |Δy|)
- x-increment = Δx / steps
- y-increment = Δy / steps

**Bresenham's Line Algorithm:**
- Initial P₀ = 2Δy - Δx
- If Pₖ < 0: Pₖ₊₁ = Pₖ + 2Δy (horizontal step)
- If Pₖ ≥ 0: Pₖ₊₁ = Pₖ + 2Δy - 2Δx (diagonal step)

**Midpoint Circle Algorithm:**
- Initial P₀ = 1 - R
- If Pₖ < 0: Pₖ₊₁ = Pₖ + 2x + 3 (horizontal step)
- If Pₖ ≥ 0: Pₖ₊₁ = Pₖ + 2x - 2y + 5 (diagonal step)

## Key Points

1. Raster graphics represent images as a grid of pixels; every geometric shape must be discretized for display.

2. DDA uses floating-point arithmetic and is conceptually simple but computationally expensive.

3. Bresenham's algorithm eliminates floating-point operations by using only integer arithmetic, making it faster and suitable for hardware implementation.

4. The Midpoint Circle Algorithm exploits eight-way symmetry to generate complete circles from only one-eighth of the calculations.

5. Scan-line polygon fill works by intersecting horizontal scan lines with polygon edges and filling between pairs of intersections.

6. Bresenham's algorithm minimizes the error between the ideal mathematical line and the selected pixels.

7. Edge cases in polygon filling include vertices shared by edges on the same side (count as one intersection) versus opposite sides (count as two).

8. Modern graphics systems still use variations of these fundamental algorithms, making them essential knowledge for understanding graphics pipelines.

## Common Mistakes to Not Avoid

1. **Forgetting to round in DDA**: The DDA algorithm produces floating-point coordinates that must be rounded to the nearest integer for pixel plotting.

2. **Incorrect decision parameter update**: Using the wrong formula for updating the decision parameter P is a common error that produces incorrect results.

3. **Not handling negative slopes**: Basic implementations often assume positive slopes; negative slopes require special handling by swapping start and end points or inverting the direction.

4. **Double-counting intersections**: In polygon fill, horizontal edges must be handled carefully to avoid counting the same intersection twice.

5. **Wrong initial values**: Using the wrong initial decision parameter (P₀) will cause the entire algorithm to produce incorrect pixel positions.

## Revision Tips

1. Practice implementing both DDA and Bresenham's algorithms by hand for various line endpoints to reinforce understanding of the decision parameter logic.

2. Remember the key difference: DDA uses division (floating-point), while Bresenham uses only addition, subtraction, and multiplication by 2 (bit shifting).

3. For circle algorithms, always start from (0, R) and remember that only one-eighth of the circle needs to be computed explicitly.

4. In exams, clearly show your decision parameter calculations and the reasoning behind each step—the process matters as much as the final answer.

5. Create a comparison table of all algorithms covering their time complexity, space complexity, arithmetic type used, and specific use cases.