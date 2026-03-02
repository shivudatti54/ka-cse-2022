## Quick Reference Card: Four Major Tasks in the Graphics Pipeline

### Pipeline Stages in Order
**Modeling → Geometric Processing → Rasterization → Fragment Processing**

### Key Definitions (2-3 Lines Each)

| Stage | Definition |
|-------|------------|
| **Modeling** | Creates geometric representations (vertices, edges, faces) using polygon meshes, NURBS, or subdivision surfaces |
| **Geometric Processing** | Applies transformations (model/view), clipping, and projection to convert 3D vertices to 2D screen coordinates |
| **Rasterization** | Converts primitives (lines, triangles) into fragments through scan conversion; generates per-fragment interpolated attributes |
| **Fragment Processing** | Processes fragments with texturing, blending, depth testing, and outputs final pixels to the framebuffer |

### Comparison Table

| Aspect | Modeling | Geometric Processing | Rasterization | Fragment Processing |
|--------|----------|----------------------|---------------|---------------------|
| **Input** | Raw geometry data | Vertices/Primitives | Primitives | Fragments |
| **Output** | Scene/Mesh | Screen primitives | Fragments | Pixels |
| **Key Ops** | Vertex definition | Transform, Clip, Project | Scan-convert | Texture, Blend, Test |
| **Programmable** | No (data prep) | Yes (Vertex Shader) | Mostly Fixed | Yes (Fragment Shader) |

### Must-Remember Points
- **Pipeline order is critical**: Data flows sequentially; each stage depends on previous output
- **Model Matrix**: Object-to-world transform; **View Matrix**: World-to-camera; **Projection Matrix**: Camera-to-clip space
- **Clipping** removes primitives outside the viewing frustum before rasterization
- **Fragments** are not pixels yet—they have potential to be discarded by tests
- **Depth Buffer (Z-Buffer)** stores closest fragment depth for visibility determination
- **Antialiasing** (MSAA, FXAA) reduces jagged edges; MSAA samples multiple times per pixel
- **Blending** combines fragment color with framebuffer using alpha (transparency)
- **OpenGL Shader Pipeline**: Vertex Shader → Rasterizer → Fragment Shader → Framebuffer