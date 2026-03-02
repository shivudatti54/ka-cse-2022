# Modeling a Colored Cube

## Introduction

Three-dimensional modeling forms the foundation of modern computer graphics, enabling the creation of virtual objects, environments, and animations that we see in games, simulations, and visualizations. Among the simplest yet most instructive 3D objects to model is the colored cube—a fundamental geometric primitive that demonstrates core concepts in 3D graphics programming including vertex specification, face construction, color assignment, transformation matrices, and rendering pipelines.

Understanding how to model a colored cube is essential for any computer graphics developer because it encapsulates the entire workflow from abstract mathematical representation to visible output on a screen. The cube serves as a building block for more complex models, and mastering its creation provides the conceptual framework needed to handle sophisticated 3D objects. In the context of 's Computer Graphics curriculum, this topic bridges theoretical knowledge of coordinate systems, transformations, and rendering algorithms with practical implementation skills using graphics libraries like OpenGL.

This module explores the complete process of creating a colored cube, starting from defining its geometry in 3D space, through applying colors to individual faces, to transforming and rendering it using standard graphics pipelines. We will examine both the mathematical foundations and practical implementation considerations that enable proper cube visualization.

## Key Concepts

### 3D Coordinate Systems and Vertices

A cube in 3D space is defined by its eight vertices (corners). In a right-handed Cartesian coordinate system with X, Y, and Z axes, a unit cube centered at the origin has vertices at coordinates representing the extremes along each axis. Each vertex is represented as a tuple (x, y, z) where each coordinate can be either -1 or +1 (for a unit cube with side length 2). For a cube with side length 1 centered at origin, vertices range from -0.5 to +0.5 along each axis.

The eight vertices of a unit cube are:

- Bottom face: (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5)
- Top face: (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)

Understanding vertex ordering is crucial for proper face rendering and back-face culling optimization.

### Face Definition and Polygon Winding

A cube consists of six rectangular faces, each comprising four vertices. The order in which vertices are specified determines the face normal direction through the right-hand rule—curling the fingers of your right hand in the vertex order points your thumb in the direction of the face normal. This winding order (clockwise or counter-clockwise) is essential for determining which side of the face is the "front" and enabling back-face culling.

Each face is defined by connecting four vertices in sequence:

- Front face: 4 vertices in counter-clockwise order when viewed from outside
- Back face: 4 vertices in counter-clockwise order when viewed from outside
- Similarly for top, bottom, left, and right faces

### Color Assignment to Faces

Coloring a cube involves assigning RGB (Red, Green, Blue) or RGBA (with Alpha transparency) values to each face. Modern OpenGL uses normalized floating-point values between 0.0 and 1.0 for each color component. A common approach is to assign different colors to each of the six faces to make the cube's orientation clearly visible when rendered.

For example:

- Front face: Red (1.0, 0.0, 0.0)
- Back face: Green (0.0, 1.0, 0.0)
- Top face: Blue (0.0, 0.0, 1.0)
- Bottom face: Yellow (1.0, 1.0, 0.0)
- Right face: Magenta (1.0, 0.0, 1.0)
- Left face: Cyan (0.0, 1.0, 1.0)

### Transformation Matrices

To view the cube from different angles and positions, we apply transformation matrices:

**Model Matrix**: Transforms vertices from object space to world space. Includes translation, rotation, and scaling operations. A 4×4 homogeneous transformation matrix combines these operations.

**View Matrix**: Transforms world coordinates to camera (view) coordinates, positioning the scene relative to the viewer.

**Projection Matrix**: Projects 3D coordinates onto 2D screen coordinates, implementing perspective or orthographic projection.

The combined transformation is: Clip Space = Projection × View × Model × Local Vertex

### The Rendering Pipeline

The complete pipeline for rendering a colored cube involves:

1. **Vertex Specification**: Defining vertex positions, colors, and other attributes in vertex buffers
2. **Vertex Shader**: Processing vertices, applying transformations
3. **Primitive Assembly**: Grouping vertices into triangles (each quad becomes two triangles)
4. **Rasterization**: Converting primitives into fragments (potential pixels)
5. **Fragment Shader**: Computing final color for each fragment
6. **Per-Fragment Operations**: Depth testing, blending, and final pixel output

### Depth Buffering

When rendering 3D objects, the depth buffer (Z-buffer) ensures correct visibility by storing the depth of each rendered pixel. Without depth buffering, faces closer to the camera might be overwritten by distant faces. Enabling depth testing (glEnable(GL_DEPTH_TEST)) is essential for proper cube rendering.

## Examples

### Example 1: Defining Cube Vertices and Colors in Modern OpenGL

**Problem**: Define the vertex data structure and specify vertices for a colored cube with different colors on each face.

**Solution**:

```cpp
// Vertex structure with position and color
struct Vertex {
 glm::vec3 Position;
 glm::vec3 Color;
};

// Define 36 vertices (6 faces × 2 triangles × 3 vertices)
// Each face has 4 vertices, triangulated as 2 triangles
std::vector<Vertex> cubeVertices = {
 // Front face (Red) - triangle 1
 {{-0.5f, -0.5f, 0.5f}, {1.0f, 0.0f, 0.0f}}, // bottom-left
 {{ 0.5f, -0.5f, 0.5f}, {1.0f, 0.0f, 0.0f}}, // bottom-right
 {{ 0.5f, 0.5f, 0.5f}, {1.0f, 0.0f, 0.0f}}, // top-right
 // Front face - triangle 2
 {{ 0.5f, 0.5f, 0.5f}, {1.0f, 0.0f, 0.0f}}, // top-right
 {{-0.5f, 0.5f, 0.5f}, {1.0f, 0.0f, 0.0f}}, // top-left
 {{-0.5f, -0.5f, 0.5f}, {1.0f, 0.0f, 0.0f}}, // bottom-left

 // Back face (Green)
 {{-0.5f, -0.5f, -0.5f}, {0.0f, 1.0f, 0.0f}},
 {{-0.5f, 0.5f, -0.5f}, {0.0f, 1.0f, 0.0f}},
 {{ 0.5f, 0.5f, -0.5f}, {0.0f, 1.0f, 0.0f}},
 {{ 0.5f, 0.5f, -0.5f}, {0.0f, 1.0f, 0.0f}},
 {{ 0.5f, -0.5f, -0.5f}, {0.0f, 1.0f, 0.0f}},
 {{-0.5f, -0.5f, -0.5f}, {0.0f, 1.0f, 0.0f}},

 // Continue for remaining 4 faces...
};
```

**Explanation**: Each rectangular face requires 6 vertices (2 triangles × 3 vertices) to properly assign individual face colors. The vertices are ordered counter-clockwise when viewed from outside the cube to ensure proper face normals.

### Example 2: Setting Up Transformation Matrices

**Problem**: Create model, view, and projection matrices to display a colored cube at position (2, 1, -3) with 45° rotation around Y-axis, viewed from a camera at (0, 2, 5) looking at origin.

**Solution**:

```cpp
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

// Model Matrix: Translate and rotate
glm::mat4 model = glm::mat4(1.0f);
model = glm::translate(model, glm::vec3(2.0f, 1.0f, -3.0f)); // Position
model = glm::rotate(model, glm::radians(45.0f), glm::vec3(0.0f, 1.0f, 0.0f)); // Y rotation

// View Matrix: Camera setup
glm::vec3 cameraPos = glm::vec3(0.0f, 2.0f, 5.0f);
glm::vec3 cameraTarget = glm::vec3(0.0f, 0.0f, 0.0f);
glm::vec3 up = glm::vec3(0.0f, 1.0f, 0.0f);

glm::mat4 view = glm::lookAt(cameraPos, cameraTarget, up);

// Projection Matrix: Perspective projection
glm::mat4 projection = glm::mat4(1.0f);
float fov = glm::radians(45.0f);
float aspectRatio = 800.0f / 600.0f; // window width/height
float nearPlane = 0.1f;
float farPlane = 100.0f;

projection = glm::perspective(fov, aspectRatio, nearPlane, farPlane);

// Combined matrix sent to vertex shader
glm::mat4 mvp = projection * view * model;

// Pass to shader
unsigned int transformLoc = glGetUniformLocation(shaderProgram, "uTransform");
glUniformMatrix4fv(transformLoc, 1, GL_FALSE, glm::value_ptr(mvp));
```

**Explanation**: The model matrix positions and orients the cube in world space. The view matrix transforms world coordinates to camera-relative coordinates. The projection matrix applies perspective, making distant objects appear smaller. The MVP (Model-View-Projection) matrix combines all three transformations.

### Example 3: Complete Cube Rendering with Depth Testing

**Problem**: Write the complete rendering code to draw a colored cube with proper depth testing and face culling.

**Solution**:

```cpp
void renderCube(unsigned int VAO, unsigned int shaderProgram) {
 // Clear buffers
 glClearColor(0.1f, 0.1f, 0.1f, 1.0f); // dark gray background
 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

 // Enable depth testing
 glEnable(GL_DEPTH_TEST);
 glDepthFunc(GL_LESS); // Pass test if fragment depth < stored depth

 // Enable back-face culling (render only front faces)
 glEnable(GL_CULL_FACE);
 glCullFace(GL_BACK);
 glFrontFace(GL_CCW); // Counter-clockwise winding is front

 // Use shader program
 glUseProgram(shaderProgram);

 // Set transformation matrix (from Example 2)
 glm::mat4 model = glm::mat4(1.0f);
 glm::mat4 mvp = projection * view * model;

 unsigned int mvpLoc = glGetUniformLocation(shaderProgram, "uMVP");
 glUniformMatrix4fv(mvpLoc, 1, GL_FALSE, glm::value_ptr(mvp));

 // Bind cube VAO and draw
 glBindVertexArray(VAO);
 glDrawArrays(GL_TRIANGLES, 0, 36); // 6 faces × 2 triangles × 3 vertices

 // Unbind
 glBindVertexArray(0);
}
```

**Explanation**: This rendering function clears the color and depth buffers, enables depth testing for correct 3D visibility, enables face culling to improve performance by not rendering back faces, binds the vertex array object containing our cube data, and draws 36 vertices (6 faces × 6 vertices per face after triangulation).

## Exam Tips

1. **Remember vertex count**: A cube requires 36 vertices when using triangle primitives (6 faces × 2 triangles × 3 vertices), or 24 vertices when using triangle strip with restart.

2. **Understand coordinate systems**: exams frequently ask about right-handed coordinate systems and how vertices are ordered for proper face normals.

3. **Transformation matrix order**: Remember the correct order is Projection × View × Model × Vertex. Reversing this order produces incorrect results.

4. **Depth buffer importance**: Always enable GL_DEPTH_TEST when rendering 3D objects. Without it, faces render in the wrong order and visual artifacts appear.

5. **Face culling concept**: Know that glCullFace(GL_BACK) combined with proper vertex winding order improves performance by not rendering hidden faces.

6. **Color representation**: Modern OpenGL uses normalized floats [0.0, 1.0] for colors, not the 0-255 integer range used in older graphics APIs.

7. **Winding order convention**: Counter-clockwise vertex order defines the front face in standard OpenGL convention, following the right-hand rule for normal calculation.

8. **Homogeneous coordinates**: The 4×4 transformation matrix uses homogeneous coordinates, where the w-component handles perspective division automatically.
