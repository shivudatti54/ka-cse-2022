# Liang-Barsky Line Clipping Algorithm - Summary

## Key Definitions and Concepts

- **Line Clipping**: The process of removing portions of line segments that lie outside a rectangular clipping window.

- **Parametric Line Representation**: A line from P1(x1,y1) to P2(x2,y2) is represented as x = x1 + t(x2-x1), y = y1 + t(y2-y1), where 0 ≤ t ≤ 1.

- **t0 and t1**: Parameters representing the start and end of the clipped portion of the line within the window.

- **p-values**: Directional parameters for each boundary (p1=-Δx, p2=Δx, p3=-Δy, p4=Δy).

- **q-values**: Position parameters for each boundary (q1=x1-xmin, q2=xmax-x1, q3=y1-ymin, q4=ymax-y1).

## Important Formulas and Theorems

- Parametric equation: x = x1 + t(x2 - x1), y = y1 + t(y2 - y1)
- p1 = -(x2 - x1), p2 = (x2 - x1), p3 = -(y2 - y1), p4 = (y2 - y1)
- q1 = x1 - xwmin, q2 = xwmax - x1, q3 = y1 - ywmin, q4 = ywmax - y1
- For p < 0: t0 = max(t0, q/p); For p > 0: t1 = min(t1, q/p)
- Rejection condition: If t0 > t1, the line is completely outside

## Key Points

- The Liang-Barsky algorithm is a parametric line clipping algorithm that offers O(1) complexity per line.

- It directly computes intersection points rather than repeatedly subdividing lines like Cohen-Sutherland.

- When p=0 and q<0, the line is parallel to and outside the boundary—reject the line.

- When p=0 and q≥0, the line is parallel to and inside the boundary—continue checking other boundaries.

- If t0 ≤ t1 after processing all boundaries, the line has valid clipping; otherwise, reject it.

- The algorithm works efficiently for rectangular clipping windows only.

- Both endpoints of the clipped line are calculated using: P = P1 + t(P2 - P1)

## Common Mistakes to Avoid

1. Confusing the signs of p and q values—remember p1 and p3 are negative (entering conditions).

2. Forgetting to check the p=0 special case before calculating t values—this leads to division by zero errors.

3. Swapping t0 and t1 or incorrectly applying max/min functions.

4. Not converting parametric values back to actual x,y coordinates for the final clipped line.

5. Confusing Liang-Barsky with Cyrus-Beck (which works for convex polygons).

## Revision Tips

1. Practice with 3-4 numerical examples covering all three cases: completely inside, partially inside, and completely outside.

2. Memorize the p and q value formulas for each boundary—these are tested frequently.

3. Create a flowchart of the algorithm and rehearse the step-by-step procedure.

4. Compare with Cohen-Sutherland to understand when each algorithm is preferred.

5. Solve previous year exam questions on line clipping algorithms.
