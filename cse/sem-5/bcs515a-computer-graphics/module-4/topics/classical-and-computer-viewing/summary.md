# Classical and Computer Viewing - Summary

## Key Definitions and Concepts

- **Viewing Coordinate System**: A coordinate system defined by the view reference point (VRP), view plane normal (VPN), view up vector (VUP), and right vector (RIGHT), representing the camera position and orientation.

- **Window**: A rectangular region in viewing coordinates that defines the portion of the scene to be displayed.

- **Viewport**: The rectangular region on the output device where the final image is rendered.

- **Parallel Projection**: A projection technique where projection lines are parallel, preserving parallelism in the original objects.

- **Perspective Projection**: A projection technique that simulates human vision, where objects farther away appear smaller.

- **Viewing Frustum**: The volume of space that is visible in perspective projection, defined by near and far clipping planes.

- **Clipping**: The process of removing portions of objects outside the viewing volume.

## Important Formulas and Theorems

- **Window-to-Viewport Transformation**:
  - x_vp = (x_w - w_left) × (vp_width / w_width) + vp_left
  - y_vp = (y_w - w_bottom) × (vp_height / w_height) + vp_bottom

- **Parallel Projection** (onto xy-plane): P'(x, y, 0)

- **Perspective Projection**: P'(xd/z, yd/z, d) where d is the projection plane distance

- **Viewing Transformation Matrix**: 4×4 matrix combining translation of VRP to origin and rotation to align VPN with Z-axis

## Key Points

1. The viewing transformation converts world coordinates to viewing (camera) coordinates.

2. Parallel projections maintain parallel lines and are used in technical drawings; perspective projections create realistic images with foreshortening.

3. The viewing pipeline follows the sequence: modeling → viewing → projection → viewport → device transformation.

4. Window defines what portion of the scene is visible; viewport defines where on screen it appears.

5. Clipping removes objects outside the viewing volume before rendering.

6. Cohen-Sutherland algorithm uses outcodes for efficient line clipping against rectangular windows.

7. Perspective projection involves division by depth (z-coordinate), creating realistic depth perception.

8. Matching aspect ratios between window and viewport prevents image distortion.

9. Near and far clipping planes in perspective viewing control the depth range of visible objects.

10. Homogeneous coordinates enable representation of all viewing and projection transformations as 4×4 matrices.

## Common Mistakes to Avoid

- Confusing window and viewport: Remember window is in viewing coordinates, viewport is in screen/device coordinates.

- Forgetting perspective division when implementing perspective projection in homogeneous coordinates.

- Not maintaining aspect ratio between window and viewport, leading to distorted images.

- Incorrectly ordering transformations in the viewing pipeline, which can produce wrong results.

- Confusing VRP (view reference point) with PRP (projection reference point) - they serve different purposes.

## Revision Tips

1. Practice drawing the complete viewing pipeline diagram to understand how transformations flow.

2. Solve numerical problems on window-to-viewport mapping to gain confidence in the formulas.

3. Compare parallel and perspective projections side-by-side, noting their differences and applications.

4. Review the 4×4 transformation matrices for viewing and projection transformations.

5. Remember that clipping is applied before rasterization to avoid processing invisible geometry.
