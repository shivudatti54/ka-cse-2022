# Programmable Pipelines - Summary

## Key Definitions and Concepts

- **Programmable Pipeline**: A graphics rendering architecture where specific stages can be customized using user-written programs called shaders, replacing the hardwired operations of fixed-function pipelines.

- **Shader**: A program that executes on the GPU at a specific pipeline stage. Common types include vertex shaders, fragment shaders (pixel shaders), geometry shaders, and tessellation shaders.

- **Vertex Shader**: The first programmable pipeline stage that processes each vertex individually, performing coordinate transformations and passing interpolated data to subsequent stages.

- **Fragment Shader**: The stage that determines the final color of each pixel, handling per-pixel lighting, texture sampling, and other fragment-level operations.

- **Uniform Variables**: Global shader variables that remain constant across all invocations during a draw call, used for matrices, light properties, and texture samplers.

## Important Formulas and Theorems

- **Coordinate Transformation Pipeline**: `gl_Position = Projection × View × Model × VertexPosition`

- **Lambert's Cosine Law (Diffuse)**: `diffuse = max(dot(normal, lightDir), 0.0)`

- **Blinn-Phong Specular**: `specular = pow(max(dot(viewDir, reflectDir), 0.0), shininess)`

- **Normal Transformation**: `normalWorld = transpose(inverse(modelMatrix)) × normalLocal`

## Key Points

- Programmable pipelines replaced fixed-function pipelines, offering flexibility and improved visual quality.

- The graphics pipeline flows: Input Assembler → Vertex Shader → (Optional: Tessellation) → Geometry Shader → Rasterizer → Fragment Shader → Output Merger.

- Vertex shaders transform vertices and pass data; fragment shaders compute final pixel colors.

- GLSL (OpenGL) and HLSL (DirectX) are the primary shader languages used in graphics programming.

- Uniform variables transfer application data (matrices, lights, textures) to shaders.

- Geometry shaders can create or destroy primitives, enabling effects like particle systems and shadow volumes.

- Fragment shaders support per-pixel lighting (Phong shading) which produces smoother highlights than vertex-based Gouraud shading.

## Common Mistakes to Avoid

1. Forgetting to normalize vectors after interpolation - interpolated vectors lose their unit length.

2. Using the model matrix directly for normal transformation without the inverse-transpose, causing incorrect lighting with non-uniform scaling.

3. Confusing when operations should occur: expensive per-vertex vs. per-fragment calculations, and which provides better quality.

4. Not declaring uniform variables correctly or failing to update them in the application code before drawing.

## Revision Tips

1. Practice writing simple shaders from memory - vertex transformation followed by basic lighting in the fragment shader.

2. Trace through a complete example by hand: understand how vertex positions and normals flow through each pipeline stage.

3. Remember that fragment shaders receive interpolated values from vertex shader outputs, not the original vertex values.

4. Review the difference between vertex and fragment shader responsibilities: geometry processing vs. pixel coloring.

5. Study the matrix transformation sequence (Model → View → Projection) until it becomes automatic.
