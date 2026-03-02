# Cohen-Sutherland Line Clipping Algorithm - Summary

## Key Definitions and Concepts

- **Line Clipping**: The process of determining which portions of a line segment lie within a visible rectangular region (clipping window) before rendering.

- **Outcode (Region Code)**: A 4-bit code assigned to each endpoint indicating its position relative to the clipping window boundaries.

- **Clipping Window**: A rectangular region defined by xmin, xmax, ymin, and ymax boundaries.

## Important Formulas and Theorems

- **Outcode Bit Assignment**:
  - Bit 1 (1000): Top (y > ymax)
  - Bit 2 (0100): Bottom (y < ymin)
  - Bit 3 (0010): Right (x > xmax)
  - Bit 4 (0001): Left (x < xmin)

- **Intersection Formula**: Using parametric form P = P1 + t(P2-P1), solve for boundary conditions to find intersection points.

- **Rejection Test**: If (outcode1 AND outcode2) ≠ 0, the line is completely outside.

- **Acceptance Test**: If both outcodes = 0000, the line is completely inside.

## Key Points

- The algorithm divides the plane into 9 regions using the clipping window boundaries.

- Outcode 0000 indicates the point is inside the clipping window.

- The algorithm uses a divide-and-conquer approach, repeatedly clipping against boundaries until acceptance or rejection.

- Lines completely inside (both endpoints 0000) are accepted in one step.

- Lines completely outside (AND test non-zero) are rejected in one step.

- Partial lines require iterative clipping calculations.

- The algorithm is highly efficient as it quickly eliminates obvious cases.

## Common Mistakes to Avoid

1. Forgetting to check the logical AND test for rejection before attempting clipping calculations.

2. Incorrect bit assignments when computing outcodes (confusing top/bottom or left/right).

3. Not updating the outcode after computing a new intersection point.

4. Using wrong intersection formulas, especially for vertical or horizontal lines.

## Revision Tips

1. Practice computing outcodes for various point positions relative to window boundaries.

2. Memorize the bit assignment: Top=8, Bottom=4, Right=2, Left=1.

3. Solve at least 3-4 complete numerical examples to understand the iterative clipping process.

4. Remember that the algorithm terminates in a maximum of 4 iterations (one per edge).
