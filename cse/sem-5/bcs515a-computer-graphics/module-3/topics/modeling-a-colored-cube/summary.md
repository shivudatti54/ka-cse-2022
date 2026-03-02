# Modeling a Colored Cube - Summary

## Key Definitions and Concepts

- **Vertex**: A point in 3D space defined by (x, y, z) coordinates; a cube has 8 vertices
- **Face**: A flat surface of the cube defined by 4 vertices; a cube has 6 faces
- **Winding Order**: The direction (clockwise or counter-clockwise) vertices are specified, determining which side is "front"
- **Depth Buffer**: A buffer storing the depth of each pixel for visibility determination
- **MVP Matrix**: Model-View-Projection matrix combining all transformations
- **Face Culling**: Optimization technique that discards back-facing polygons

## Important Formulas and Theorems

- **Vertex positions for unit cube**: (±0.5, ±0.5, ±0.5) at origin
- **Transformation pipeline**: Clip = Projection × View × Model × Local
- **Perspective projection**: fov_aspect = tan(fov/2), depth = (far+near)/(far-near) - (2×far×near)/(depth×(far-near))
- **Counter-clockwise winding**: Right-hand rule curl determines face normal direction
- **Normalized color range**: RGB values from 0.0 (minimum) to 1.0 (maximum)

## Key Points

1. A cube requires 36 vertices when triangulated (6 faces × 2 triangles × 3 vertices each)
2. Vertex order must be consistent (CCW when viewed from outside) for proper face culling
3. Different colors must be explicitly assigned to each of the six faces
4. Model matrix handles object transformations, View matrix handles camera, Projection handles perspective
5. Depth testing must be enabled with glEnable(GL_DEPTH_TEST) for correct 3D rendering
6. Face culling improves performance by not rendering hidden back faces
7. The right-hand rule determines face normals from vertex winding order
8. Transformation matrices must be multiplied in correct order: P × V × M × vertex

## Common Mistakes to Avoid

1. **Forgetting to enable depth testing**: Results in incorrect face visibility and flickering
2. **Incorrect transformation order**: Multiplying matrices in wrong sequence produces distorted output
3. **Wrong vertex winding**: Clockwise instead of counter-clockwise causes face culling to remove front faces
4. **Using integer color values**: Modern OpenGL requires normalized floats (0.0-1.0), not 0-255
5. **Not unbinding buffers**: Can cause interference with subsequent render calls

## Revision Tips

1. Practice drawing cube vertices on paper with coordinate axes labeled
2. Memorize the standard transformation matrix multiplication order
3. Remember that GL_CCW is the default front face convention in OpenGL
4. Review how perspective division affects vertices with different Z values
5. Understand that depth buffer clearing is required each frame before rendering
