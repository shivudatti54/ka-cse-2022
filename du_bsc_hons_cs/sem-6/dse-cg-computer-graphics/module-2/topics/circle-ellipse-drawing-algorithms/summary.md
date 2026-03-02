# Circle and Ellipse Drawing Algorithms - Summary

## Key Definitions and Concepts

- **Raster Display**: A display grid where shapes are represented by discrete pixels
- **Symmetry**: Circles have 8-way symmetry (all octants mirror each other), ellipses have 4-way symmetry (all quadrants mirror)
- **Decision Parameter**: A value used to determine which pixel (E or SE for circles) better approximates the true curve
- **Midpoint Test**: Geometric test checking whether the midpoint between two candidate pixels lies inside or outside the true circle/ellipse
- **Region 1 (Ellipse)**: Region where slope magnitude > 1 (steeper curve)
- **Region 2 (Ellipse)**: Region where slope magnitude ≤ 1 (flatter curve)

## Important Formulas and Theorems

- **Circle Equation**: x² + y² = r²
- **Ellipse Equation**: x²/rx² + y²/ry² = 1
- **Midpoint Circle P-init**: P = 1 - r
- **Midpoint Circle Update (P < 0)**: P = P + 2x + 1
- **Midpoint Circle Update (P ≥ 0)**: P = P + 2x + 1 - 2y
- **Bresenham Circle d-init**: d = 2(1-r)
- **Bresenham Circle Update (d < 0)**: d = d + 2x + 3
- **Bresenham Circle Update (d ≥ 0)**: d = d + 2x - 2y + 5
- **Ellipse Transition**: 2·ry²·x ≥ 2·rx²·y

## Key Points

- All algorithms use incremental computation with simple integer additions/subtractions, avoiding expensive operations like multiplication and square root.

- The Midpoint Circle Algorithm is essentially Bresenham's circle algorithm using the midpoint convention.

- For circles, plot points only in the first octant (x from r to 0, y from 0 to x), then mirror to all 8 octants.

- For ellipses, plot points only in the first quadrant, then mirror to all 4 quadrants.

- Termination for circles: stop when x ≥ y (after crossing the 45° line).

- The ellipse algorithm requires two separate decision parameters: P1 for Region 1 and P2 for Region 2.

- Bresenham's algorithm minimizes the distance between the actual curve and pixel centers.

- All algorithms run in O(r) time complexity where r is the radius.

## Common Mistakes to Avoid

- **Forgetting symmetry**: Students often plot every point individually instead of using 8-way/4-way symmetry, losing efficiency.

- **Wrong decision parameter sign**: The sign of P or d determines which pixel is chosen—be careful with inequality directions.

- **Incorrect Region 2 transition**: The condition for transitioning from Region 1 to Region 2 in ellipse algorithm is commonly confused.

- **Not updating both x and y**: When choosing the SE pixel (diagonal), remember to update both coordinates.

- **Ignoring the condition r ≥ 1**: The initial decision parameter P = 1 - r assumes radius is at least 1.

## Revision Tips

1. **Practice with small radius values**: Work through Examples 1-3 manually to understand the step-by-step execution.

2. **Create a comparison table**: List Midpoint vs Bresenham approaches side-by-side for both circle and ellipse.

3. **Remember the symmetry trick**: Always think about how many points you actually need to compute vs. how many you plot.

4. **Understand "why" not just "how":** Know why the midpoint test works—it's checking whether the geometric midpoint lies inside or outside the true shape.

5. **Time yourself**: Practice implementing these algorithms in pseudocode within 10-15 minutes for exam conditions.