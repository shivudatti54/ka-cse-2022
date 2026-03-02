# Clipping Algorithms in Computer Graphics - Summary

## Key Definitions and Concepts

- **Clipping**: The process of eliminating portions of geometric primitives outside the viewing region
- **Viewport**: The rectangular area on the display device where graphics are rendered
- **Window**: The region in world coordinates corresponding to the viewport
- **Cohen-Sutherland Algorithm**: Line clipping using 4-bit region codes for trivial acceptance/rejection
- **Liang-Barsky Algorithm**: Parametric line clipping using parameter u calculations
- **Sutherland-Hodgman Algorithm**: Polygon clipping by processing one boundary at a time

## Important Formulas and Theorems

- **Region Code Bits**: Top=1000 (8), Bottom=0100 (4), Right=0010 (2), Left=0001 (1)
- **Cohen-Sutherland Acceptance**: Both codes = 0000 (inside)
- **Cohen-Sutherland Rejection**: Code1 AND Code2 ≠ 0 (completely outside)
- **Liang-Barsky Parametric Equations**: x = x1 + u(x2-x1), y = y1 + u(y2-y1)
- **Liang-Barsky Visibility Condition**: u1 < u2 and u2 ≥ 0 and u1 ≤ 1
- **Point Clipping**: xmin ≤ x ≤ xmax AND ymin ≤ y ≤ ymax

## Key Points

- Clipping improves rendering efficiency by eliminating invisible portions before rasterization
- Cohen-Sutherland uses region codes for quick trivial acceptance/rejection, then computes intersections
- Liang-Barsky is more efficient than Cohen-Sutherland as it directly computes parameters without subdivision
- Sutherland-Hodgman clips polygon against one edge at a time, passing output to next stage
- For 3D graphics, clipping occurs against the view frustum (six clipping planes)
- Clipping is performed in normalized device coordinates (NDC) before viewport transformation
- Text clipping can be all-or-nothing, per-character, or pixel-level

## Common Mistakes to Avoid

- Confusing window and viewport - window is in world coordinates, viewport is in device coordinates
- Forgetting to check both trivial acceptance AND rejection before computing intersections
- In Liang-Barsky, not handling negative p values correctly (these represent opposite direction)
- In Sutherland-Hodgman, not adding intersection points when one vertex is inside and one outside

## Revision Tips

- Practice drawing region codes for various endpoint positions relative to a window
- Work through at least 2-3 solved examples of each algorithm before the exam
- Remember the key difference: Cohen-Sutherland computes geometric intersections while Liang-Barsky solves parametric equations
- Focus on understanding when to accept, reject, or subdivide lines in Cohen-Sutherland
- Review the Sutherland-Hodgman logic: inside→keep, outside→discard, mixed→add intersection
