# Viewing with a Computer - Summary

## Key Definitions and Concepts

- **Viewing Pipeline**: The sequential transformation process: Modeling → Viewing → Projection → Viewport → Device Coordinates
- **Window**: Rectangular region in world coordinates defining the visible scene portion
- **Viewport**: Rectangular region on the display device where content is rendered
- **Clipping**: Removing portions of objects outside the viewing region
- **Projection**: Converting 3D coordinates to 2D representation

## Important Formulas and Equations

**Window to Viewport Transformation**:

```
x_screen = (x_world - xw_min) × (xv_max - xv_min) / (xw_max - xw_min) + xv_min
y_screen = (y_world - yw_min) × (yv_max - yv_min) / (yw_max - yw_min) + yv_min
```

**Perspective Projection**:

```
x' = x × (d / z'), y' = y × (d / z')
```

**Cohen-Sutherland Outcode Bits**: Top(1000), Bottom(0100), Right(0010), Left(0001)

## Key Points

- The viewing pipeline converts object coordinates through multiple stages to finally produce screen pixels
- Window-to-viewport transformation maintains proportional relationships while scaling content
- Cohen-Sutherland algorithm uses 4-bit outcodes for efficient line clipping decisions
- Perspective projection creates realistic depth perception through vanishing points
- Parallel projection maintains parallel lines and is used in technical drawings
- The camera model uses VRP, VPN, VUP, and PRP to define the viewing coordinate system
- Clipping operations optimize rendering by eliminating invisible geometry

## Common Mistakes to Avoid

- Confusing the order of transformations in the viewing pipeline
- Forgetting to check trivial acceptance/rejection before computing intersections in clipping
- Not maintaining aspect ratio when performing window-to-viewport transformation
- Mixing up parallel and perspective projection characteristics

## Revision Tips

1. Practice window-to-viewport problems with different coordinate systems
2. Draw the Cohen-Sutherland outcode bit positions and memorize the logic
3. Review the mathematical derivation of perspective projection using similar triangles
4. Understand how clipping integrates with the overall viewing pipeline for efficient rendering
