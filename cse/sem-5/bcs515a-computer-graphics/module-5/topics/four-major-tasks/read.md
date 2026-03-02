# Four Major Tasks in the Graphics Pipeline

## Module 5: Implementation - Computer Graphics (BCS515A)

The graphics pipeline represents the fundamental sequence of operations that transform 3D scene descriptions into final 2D images displayed on screen. Understanding these four major tasks—Modeling, Geometric Processing, Rasterization, and Fragment Processing—is essential for any computer graphics developer.

---

## 1. Modeling: Creating Geometric Representations

**Modeling** is the first stage where objects are defined using geometric data structures. The pipeline begins with mathematical descriptions of shapes.

### Polygon-Based Representations

The most common approach uses **polygon meshes** (typically triangles or quads):

- **Vertices**: Points in 3D space (x, y, z)
- **Edges**: Connections between vertices
- **Faces**: Flat surfaces bounded by edges
- **Example in OpenGL**: `glBegin(GL_TRIANGLES)` followed by vertex specifications

### Advanced Surface Representations

| Type                     | Description                    | Use Case                                      |
| ------------------------ | ------------------------------ | --------------------------------------------- |
| **NURBS**                | Non-Uniform Rational B-Splines | Smooth curved surfaces (car bodies, aircraft) |
| **Subdivision Surfaces** | Recursively refined polygons   | Character animation, organic shapes           |
| **Implicit Surfaces**    | Level sets, metaballs          | Soft objects, fluid simulation                |
| **Point Clouds**         | Unstructured sample points     | 3D scanning, LIDAR data                       |

### Data Structure Example (Triangle Mesh)

```c
struct Vertex { float x, y, z; }; // Position
struct Mesh {
 std::vector<Vertex> vertices;
 std::vector<unsigned int> indices; // Triangle topology
};
```

---

## 2. Geometric Processing: Transformations and Projection

This stage operates on vertices and primitives, applying mathematical operations to position objects in 3D space.

### Key Operations

1. **Model Transformations**

- Translation, rotation, scaling
- Model matrix: `M = T * R * S`

2. **View Transformation**

- Camera positioning using view matrix
- Transforms world space to camera space

3. **Projection**

- **Perspective**: Objects shrink with distance (realistic)
- **Orthographic**: Parallel lines preserved (technical drawing)
- Projection matrix defines the viewing frustum

4. **Clipping**

- Removes primitives outside the viewing volume
- **Cohen-Sutherland algorithm** for line clipping
- **Sutherland-Hodgman** for polygon clipping

5. **Screen Mapping**

- Converts normalized device coordinates to screen pixels

### Transformation Pipeline

```
Model Space → Model Matrix → World Space → View Matrix →
View Space → Projection Matrix → Clip Space →
Viewport Transform → Screen Space
```

### OpenGL Transformation Example

```c
glm::mat4 model = glm::translate(glm::mat4(1.0f), glm::vec3(1.0f, 2.0f, 3.0f));
glm::mat4 view = glm::lookAt(cameraPos, cameraTarget, upVector);
glm::mat4 projection = glm::perspective(fov, aspectRatio, near, far);
glm::mat4 mvp = projection * view * model;
```

---

## 3. Rasterization: Converting Primitives to Fragments

Rasterization transforms geometric primitives (points, lines, triangles) into **fragments**—potential pixels that may appear on screen.

### Scan Conversion

**Line Drawing Algorithms**:

- **DDA (Digital Differential Analyzer)**: Incremental calculation
- **Bresenham's Algorithm**: Efficient integer arithmetic, no floating point
- **Midpoint Algorithm**: Extension for circles and curves

**Triangle Rasterization**:

- Barycentric coordinate calculation
- Edge function evaluation
- Determines which pixels are inside the triangle

### Fragment Generation

Each fragment represents a single pixel sample with attributes:

- Position (screen coordinates)
- Color (interpolated from vertices)
- Depth value (for z-buffering)
- Texture coordinates
- Normals for lighting

### Antialiasing Techniques

| Technique                | Description                              | Quality                               |
| ------------------------ | ---------------------------------------- | ------------------------------------- |
| **Supersampling (SSAA)** | Render at higher resolution, downsample  | High quality, expensive               |
| **Multisampling (MSAA)** | Multiple samples per pixel, shared color | Balanced                              |
| **FXAA**                 | Post-processing filter                   | Fast, lower quality                   |
| **TAA**                  | Temporal antialiasing                    | Good motion, requires multiple frames |

### Rasterization Rules (OpenGL)

- **Point primitives**: Rasterized if point size > 0
- **Line primitives**: Using Bresenham or similar
- **Triangle primitives**: "Even-odd rule" or "Non-zero rule" for fill

---

## 4. Fragment Processing: Texturing and Output

The final stage processes each fragment into a final pixel color, handling textures, lighting, and blending.

### Texturing Pipeline

1. **Texture Access**: Sample texture at UV coordinates
2. **Filtering**: Bilinear, Trilinear, Anisotropic
3. **Mipmapping**: Pre-computed texture levels for distance
4. **Wrapping**: Repeat, clamp, mirror modes

### Texture Operations

```glsl
// Fragment shader example
vec4 texColor = texture2D(myTexture, vTexCoord);
vec4 finalColor = texColor * lighting;
```

### Blending

Combines fragment color with existing framebuffer color:

- **Alpha blending**: `Final = SrcColor × SrcAlpha + DstColor × (1-SrcAlpha)`
- **Additive blending**: For glow effects
- **Multiplicative blending**: For shadows

### Depth Testing

- **Z-buffer algorithm**: Stores closest fragment depth
- **Less/Equal/Greater**: Configurable comparison functions
- **Early-Z optimization**: Skip hidden surface fragments

### Framebuffer Operations

- Color buffer write (RGBA)
- Depth buffer update
- Stencil buffer (masking, shadows)
- Scissor test (limited rendering region)

### Output Merging

Final fragment operations before writing to framebuffer:

1. Scissor test
2. Stencil test
3. Depth test
4. Blending
5. Logical operations (AND, OR, XOR)

---

## Pipeline Summary Diagram

```
[Application] → [Vertices/Primitives] → [Geometric Processing]
 ↓ ↓
 Modeling Transform → Clip → Project
 ↓ ↓
 [Triangles] [Screen Primitives]
 ↓
 Rasterization → [Fragments]
 ↓
 Fragment Processing → [Pixels]
 ↓
 [FrameBuffer]
 ↓
 [Display]
```

---

## Comparison Table: Pipeline Stages

| Stage             | Input      | Output     | Key Operations            | API Functions            |
| ----------------- | ---------- | ---------- | ------------------------- | ------------------------ |
| **Modeling**      | Raw data   | Mesh/Scene | Vertex creation, topology | glVertex, buffer objects |
| **Geometric**     | Vertices   | Primitives | Transform, clip, project  | glMatrixMode, glFrustum  |
| **Rasterization** | Primitives | Fragments  | Scan-convert, interpolate | Built-in pipeline        |
| **Fragment**      | Fragments  | Pixels     | Texture, blend, test      | glEnable, shaders        |

---

## Key Takeaways

1. **Pipeline is sequential** but modern GPUs execute stages in parallel (pipelining)
2. **Programmable stages**: Vertex and Fragment Shaders (GLSL/HLSL)
3. **Fixed-function stages**: Assembly language equivalents in legacy OpenGL
4. **Performance considerations**: Minimize state changes, use VBOs, batch draws
5. **Debugging tools**: RenderDoc, NVIDIA Nsight, gDEBugger

---

## References

- OpenGL Specification (Khronos Group)
- "Computer Graphics: Principles and Practice" - Foley, van Dam
- "Real-Time Rendering" - Akenine-Möller, Haines, Hoffman
