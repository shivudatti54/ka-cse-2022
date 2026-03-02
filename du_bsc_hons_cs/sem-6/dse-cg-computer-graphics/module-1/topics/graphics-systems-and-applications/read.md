# Graphics Systems And Applications

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

Computer Graphics is the branch of computer science that deals with the creation, manipulation, and representation of visual data using computers. It forms the backbone of modern visual computing and has revolutionized how we interact with technology. From the movies we watch to the video games we play, from medical imaging to architectural design, computer graphics permeates virtually every aspect of our digital lives.

**Real-World Applications:**
- **Entertainment Industry**: Hollywood movies like Avatar and Avengers use advanced computer-generated imagery (CGI) to create stunning visual effects
- **Gaming**: Modern video games rely heavily on 3D graphics rendering, texture mapping, and real-time animations
- **Medical Imaging**: CT scans, MRI, and ultrasound imaging use graphics techniques for visualization
- **Virtual Reality (VR) and Augmented Reality (AR)**: Immersive experiences powered by real-time graphics rendering
- **Computer-Aided Design (CAD)**: Architects, engineers, and designers use graphics systems for modeling
- **Simulation and Training**: Flight simulators, driving simulators, and military training applications
- **User Interfaces**: All modern operating systems and applications use graphical user interfaces (GUIs)

This study material covers the complete syllabus for **DSE-CG: Computer Graphics** under the Delhi University NEP 2024 UGCF curriculum for BSc (Hons) Computer Science.

---

## 2. Display Systems

Display systems are the primary output devices in computer graphics, responsible for presenting visual information to users.

### 2.1 Cathode Ray Tube (CRT) Display

CRT is the oldest display technology, though largely obsolete today. It works by:
1. Electron guns fire electron beams at a phosphor-coated screen
2. Electrons strike phosphors, causing them to emit light
3. Magnetic coils deflect electron beams to scan the entire screen
4. Refresh rate (typically 60-120 Hz) determines how often the image is redrawn

**Types of CRT Scanning:**
- **Raster Scan**: Most common; electron beam moves horizontally left-to-right, then down (like reading a book)
- **Random Scan (Vector Scan)**: Electron beam moves directly to points that need to be drawn (like writing)

### 2.2 Flat Panel Displays

**Liquid Crystal Display (LCD)**:
- Uses liquid crystal molecules between two polarizing filters
- Electric current changes orientation of crystals, controlling light passage
- Backlight provides illumination (unlike CRT which emits light)
- Advantages: Thin, lightweight, low power consumption, no flicker

**Light Emitting Diode (LED) Display**:
- Uses semiconductor diodes that emit light when current flows
- Used in large outdoor displays and modern televisions
- Better contrast ratio and energy efficiency than LCD

**Organic LED (OLED)**:
- Organic compounds that emit light when electrified
- Each pixel is self-emitting (no backlight needed)
- Superior color accuracy, wider viewing angles, flexible displays possible

### 2.3 Resolution and Color Depth

- **Resolution**: Number of pixels (horizontal × vertical), e.g., 1920×1080 (Full HD)
- **Color Depth**: Number of bits used to represent each pixel's color
  - 1-bit: 2 colors (black and white)
  - 8-bit: 256 colors (indexed color)
  - 24-bit: 16.7 million colors (true color, 8 bits per channel for RGB)
  - 32-bit: Adds 8-bit alpha channel for transparency

### 2.4 Video Controller

The video controller manages the interface between the computer and display device:
- **Frame Buffer**: Memory that stores the complete image to be displayed
- **Video RAM**: Dedicated memory for rapid read/write operations
- **Refresh Rate**: Frequency of screen updates (measured in Hz)
- **Double Buffering**: Technique using two frame buffers to prevent flicker

---

## 3. Input Devices

Input devices allow users to interact with graphics applications and provide data for graphical representation.

### 3.1 Pointing Devices

| Device | Description | Applications |
|--------|-------------|--------------|
| **Mouse** | Hand-held pointing device with 2D motion detection | General GUI navigation, drawing |
| **Trackball** | Ball-based pointing device (inverted mouse) | CAD, precision work |
| **Joystick** | Lever-based device for directional control | Games, flight simulators |
| **Light Pen** | Photosensitive pen that detects screen content | Early GUI, point selection |
| **Touch Screen** | Touch-sensitive display overlay | Mobile devices, kiosks |
| **Graphics Tablet** | Flat surface with stylus for precise input | Digital art, CAD drawings |

### 3.2 Keyboard

- Standard alphanumeric input
- Function keys for commands
- Arrow keys for navigation
- Modifier keys (Shift, Ctrl, Alt) for special operations

### 3.3 Digitizer

Converts physical drawings into digital format:
- **Tablet**: Flat surface with electromagnetic grid
- **Stylus**: Position-sensing pen
- Typical accuracy: 0.01 to 0.005 inches
- Applications: Architectural drawings, maps, engineering schematics

### 3.4 3D Input Devices

- **Spaceball**: 6-DOF (degrees of freedom) input for 3D navigation
- **Data Glove**: Tracks hand and finger movements for VR
- **Motion Capture Suits**: Track full-body movement

---

## 4. Graphics Pipeline

The graphics pipeline is the sequence of steps a computer takes to render a 3D scene into a 2D image displayed on screen. Understanding this pipeline is crucial for comprehending how graphics systems work.

### 4.1 Stages of the Graphics Pipeline

```
[3D Model] → [Vertex Processing] → [Primitive Assembly] → [Rasterization] 
→ [Fragment Processing] → [Output Merger] → [2D Display]
```

**1. Application Stage**:
- 3D models defined as vertices and primitives (points, lines, triangles)
- Geometry data prepared
- Transformation matrices defined

**2. Vertex Processing**:
- Model transformation: Position vertices in world coordinates
- View transformation: Position camera and transform to view/camera coordinates
- Projection transformation: Perspective or orthographic projection
- Lighting calculations (vertex lighting)

**3. Primitive Assembly**:
- Vertices grouped into primitives (triangles, lines)
- Clipping performed against the view frustum
- Culling (back-face culling) removes invisible primitives

**4. Rasterization**:
- Converts primitives into fragments (potential pixels)
- Interpolates vertex attributes across the primitive

**5. Fragment Processing**:
- Texture mapping
- Per-fragment lighting calculations (pixel shading)
- Fog and transparency effects

**6. Output Merger**:
- Depth testing (Z-buffer)
- Blending with existing frame buffer
- Final color output

### 4.2 Coordinate Systems

- **Object Space**: Local coordinates of individual objects
- **World Space**: Global coordinates where all objects are placed
- **View/Camera Space**: Coordinates relative to camera
- **Clip Space**: After projection transformation
- **Normalized Device Coordinates (NDC)**: -1 to +1 in x, y, z
- **Window/Screen Space**: Final pixel coordinates

---

## 5. Transformations

Transformations are mathematical operations that change the position, size, orientation, or shape of geometric objects.

### 5.1 2D Transformations

**Translation**:
```
[x']   [1  0  Tx] [x]
[y'] = [0  1  Ty] [y]
[1 ]   [0  0  1 ] [1]
```

Moves a point (x, y) by Tx units horizontally and Ty units vertically.

**Rotation** (counter-clockwise by angle θ):
```
[x']   [cosθ  -sinθ  0] [x]
[y'] = [sinθ   cosθ  0] [y]
[1 ]   [0       0    1] [1]
```

**Scaling** (sx in x-direction, sy in y-direction):
```
[x']   [sx  0   0] [x]
[y'] = [0   sy  0] [y]
[1 ]   [0   0   1] [1]
```

**Shearing**:
```
[x']   [1  shx  0] [x]
[y'] = [shy 1   0] [y]
[1 ]   [0   0   1] [1]
```

### 5.2 Homogeneous Coordinates

Using 3×3 matrices for 2D transformations and 4×4 matrices for 3D allows combining multiple transformations into a single matrix through matrix multiplication.

### 5.3 3D Transformations

3D transformations extend 2D concepts with an additional z-coordinate:

**3D Translation**:
```
[x']   [1  0  0  Tx] [x]
[y'] = [0  1  0  Ty] [y]
[z']   [0  0  1  Tz] [z]
[1 ]   [0  0  0  1 ] [1]
```

**3D Rotation** (around x-axis):
```
[x']   [1    0       0    0] [x]
[y'] = [0  cosθ  -sinθ  0] [y]
[z']   [0  sinθ   cosθ  0] [z]
[1 ]   [0    0       0    1] [1]
```

### 5.4 Composite Transformations

Multiple transformations can be combined into one matrix. For example, to rotate an object around a point other than origin:
1. Translate to origin
2. Rotate
3. Translate back

---

## 6. Rasterization and Scan Conversion

Rasterization is the process of converting geometric primitives (points, lines, polygons) into pixels on the raster display.

### 6.1 Line Drawing Algorithms

**Digital Differential Analyzer (DDA) Algorithm**:
```c
void drawLineDDA(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;
    int steps = max(abs(dx), abs(dy));
    float xinc = dx / (float)steps;
    float yinc = dy / (float)steps;
    float x = x1, y = y1;
    
    for (int i = 0; i <= steps; i++) {
        putpixel(round(x), round(y), WHITE);
        x += xinc;
        y += yinc;
    }
}
```

**Bresenham's Line Algorithm**:
More efficient than DDA, uses only integer arithmetic:
```c
void drawLineBresenham(int x1, int y1, int x2, int y2) {
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);
    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;
    int err = dx - dy;
    
    while (true) {
        putpixel(x1, y1, WHITE);
        if (x1 == x2 && y1 == y2) break;
        int e2 = 2 * err;
        if (e2 > -dy) { err -= dy; x1 += sx; }
        if (e2 < dx) { err += dx; y1 += sy; }
    }
}
```

### 6.2 Circle Drawing

**Midpoint Circle Algorithm**:
```c
void drawCircle(int xc, int yc, int r) {
    int x = r, y = 0;
    int err = 0;
    
    while (x >= y) {
        putpixel(xc + x, yc + y, WHITE);
        putpixel(xc + y, yc + x, WHITE);
        putpixel(xc - y, yc + x, WHITE);
        putpixel(xc - x, yc + y, WHITE);
        putpixel(xc - x, yc - y, WHITE);
        putpixel(xc - y, yc - x, WHITE);
        putpixel(xc + y, yc - x, WHITE);
        putpixel(xc + x, yc - y, WHITE);
        
        y++;
        err += 1 + 2*y;
        if (2*(err - x) + 1 > 0) {
            x--;
            err += 1 - 2*x;
        }
    }
}
```

### 6.3 Polygon Filling

**Scanline Fill Algorithm**:
1. Find intersection of scanline with each polygon edge
2. Sort intersections by x-coordinate
3. Fill pixels between pairs of intersections

---

## 7. Color Models

Color models define how colors can be represented as numerical values.

### 7.1 RGB Color Model

Additive model used by monitors, TVs, and screens:
- **R**ed, **G**reen, **B**lue primary colors
- Each channel: 0-255 (8-bit)
- Black = (0, 0, 0), White = (255, 255, 255)
- Used in: Computer monitors, projectors, smartphones

### 7.2 CMY Color Model

Subtractive model used in printing:
- **C**yan, **M**agenta, **Y**ellow
- White = (0, 0, 0), Black = (1, 1, 1) or added as K (CMYK)
- Conversion: C = 1 - R, M = 1 - G, Y = 1 - B

### 7.3 HSL and HSV Color Models

More intuitive for humans:
- **H**ue: Color type (0-360° on color wheel)
- **S**aturation: Color purity (0-100%)
- **L**ightness / **V**alue: Brightness (0-100%)

HSV is particularly useful for:
- Color picking in graphics software
- Implementing highlights and shadows
- Creating gradients

### 7.4 Color Interpolation

For smooth color transitions (gouraud shading):
```
color = color1 + t * (color2 - color1)
```
where t ranges from 0 to 1.

---

## 8. OpenGL Basics

OpenGL (Open Graphics Library) is a cross-language, cross-platform API for rendering 2D and 3D graphics.

### 8.1 OpenGL Pipeline

1. Vertex data → Vertex Shader → Primitive Assembly
2. Primitive Processing (clipping, culling) → Rasterization
3. Fragment Shader → Per-Fragment Operations → Framebuffer

### 8.2 Basic OpenGL Program Structure (using GLUT)

```c
#include <GL/gl.h>
#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0, 0.0, 0.0);  // Red color
    
    // Draw a triangle
    glBegin(GL_TRIANGLES);
        glVertex2f(0.0, 0.5);
        glVertex2f(-0.5, -0.5);
        glVertex2f(0.5, -0.5);
    glEnd();
    
    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Basic OpenGL");
    glClearColor(0.0, 0.0, 0.0, 0.0);  // Black background
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0);  // Set coordinate system
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
```

### 8.3 Modern OpenGL (Shaders)

Modern OpenGL uses programmable shaders:

**Vertex Shader**:
```glsl
#version 330 core
layout(location = 0) in vec3 position;
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main() {
    gl_Position = projection * view * model * vec4(position, 1.0);
}
```

**Fragment Shader**:
```glsl
#version 330 core
out vec4 fragColor;
uniform vec3 color;

void main() {
    fragColor = vec4(color, 1.0);
}
```

### 8.4 Common OpenGL Functions

| Function | Purpose |
|----------|---------|
| `glClear()` | Clear buffers |
| `glColor*()` | Set current color |
| `glBegin()/glEnd()` | Define geometric primitives |
| `glVertex*()` | Specify vertex coordinates |
| `glRotatef()` | Apply rotation |
| `glTranslatef()` | Apply translation |
| `glScalef()` | Apply scaling |
| `glMatrixMode()` | Select matrix stack |

---

## 9. Clipping Algorithms

Clipping removes portions of primitives that lie outside the viewing region.

### 9.1 Cohen-Sutherland Line Clipping

Divides space into 9 regions using 4-bit codes:
- Each bit represents: Top, Bottom, Right, Left
- Algorithm:
  1. Compute outcode for both endpoints
  2. If both endpoints have code 0000 → line is inside
  3. If bitwise AND of codes ≠ 0 → line is completely outside
  4. Otherwise, clip at edge and repeat

### 9.2 Liang-Barsky Line Clipping

Parametric line clipping algorithm:
- More efficient than Cohen-Sutherland
- Uses parametric equation: P(t) = P1 + t(P2 - P1), where 0 ≤ t ≤ 1
- Computes entering and exiting parameters

### 9.3 Sutherland-Hodgman Polygon Clipping

Clips polygon against one edge at a time:
1. Start with input polygon vertices
2. For each edge of clipping window:
   - If both vertices inside → add second vertex
   - If first inside, second outside → add intersection point
   - If first outside, second inside → add intersection and second vertex
   - If both outside → add nothing
3. Output becomes input for next edge

---

## 10. Hidden Surface Removal

Determines which surfaces are visible and which are obscured by other surfaces.

### 10.1 Z-Buffer Algorithm (Depth Buffer)

Most common algorithm:
1. Initialize depth buffer to farthest distance (1.0 for normalized)
2. For each pixel:
   - Calculate depth of surface at that pixel
   - If depth < stored depth: update color buffer and depth buffer
3. Advantages: Simple, handles arbitrary geometry
4. Disadvantages: Requires additional memory, per-pixel processing

### 10.2 Painter's Algorithm

Simpler but less robust:
1. Sort all polygons by depth (back to front)
2. Draw polygons in order (painting over previous)
3. Limitations: Cannot handle intersecting polygons

### 10.3 Back-Face Culling

Eliminates back faces of objects:
- Calculate surface normal
- If normal points away from camera → don't draw
- Test: dot(normal, viewDirection) > 0

### 10.4 Binary Space Partitioning (BSP)

Preprocesses scene for efficient visibility determination:
- Recursively divides space with planes
- Draws back-to-front for any viewpoint

---

## 11. Animation

Animation creates the illusion of motion through rapid display of sequential images.

### 11.1 Principles of Animation

1. **Squash and Stretch**: Deform objects to show weight
2. **Timing**: Speed of action affects perception
3. **Anticipation**: Prepare viewer for action
4. **Follow-through**: Parts continue after main action ends
5. **Arcs**: Natural motion follows curved paths

### 11.2 Keyframe Animation

- Define positions at key moments
- System interpolates between keyframes
- Types of interpolation:
  - **Linear**: Constant speed
  - **Ease-in/Ease-out**: Smooth start and end
  - **Bezier**: Complex curved paths

### 11.3 Computer Animation Techniques

**Tweening/Interpolation**:
```python
# Linear interpolation between two keyframes
def interpolate(p1, p2, t):
    return p1 + t * (p2 - p1)

# Bezier curve interpolation
def bezier(p0, p1, p2, p3, t):
    t2 = t * t
    t3 = t2 * t
    return (1-t)**3 * p0 + 3*(1-t)**2*t * p1 + 3*(1-t)*t2 * p2 + t3 * p3
```

### 11.4 Frame Rate and Timing

- **FPS (Frames Per Second)**: Measure of animation smoothness
- Film: 24 FPS
- Television: 30 FPS (NTSC), 25 FPS (PAL)
- Games: 60+ FPS for smooth gameplay
- **Delta Time**: Time between frames for frame-rate independent animation

### 11.5 Animation in OpenGL

```c
void animate(int value) {
    angle += 0.5;  // Increment rotation angle
    glutPostRedisplay();  // Request redraw
    glutTimerFunc(16, animate, 0);  // ~60 FPS
}
```

---

## 12. Key Takeaways

1. **Display Systems**: Understanding CRT, LCD, LED, and OLED technologies is fundamental; resolution and color depth determine display quality.

2. **Graphics Pipeline**: The complete pipeline from 3D model to 2D display involves vertex processing, rasterization, and fragment processing—each stage is crucial.

3. **Transformations**: Matrix operations (translation, rotation, scaling) form the mathematical foundation for manipulating objects in 2D and 3D space.

4. **Rasterization**: Algorithms like DDA, Bresenham's, and scanline filling convert geometric primitives into displayable pixels.

5. **Color Models**: RGB (additive), CMY (subtractive), and HSL/HSV each serve different purposes; choice depends on the application context.

6. **OpenGL**: Industry-standard API that implements the graphics pipeline; modern OpenGL uses programmable shaders for flexibility.

7. **Clipping**: Essential for rendering only visible portions of objects; Cohen-Sutherland and Liang-Barsky are fundamental line clipping algorithms.

8. **Hidden Surface Removal**: Z-buffer is the most widely used algorithm; ensures correct visibility in complex 3D scenes.

9. **Animation**: Frame-rate independent animation using interpolation techniques creates smooth motion.

---

## 13. Assessment Questions

### 13.1 Multiple Choice Questions (MCQs)

**Level 1: Basic**

1. Which display technology uses liquid crystals between two polarizing filters?
   - a) CRT
   - b) LED
   - c) LCD
   - d) Plasma
   - **Answer: c**

2. In RGB color model, what is the color (255, 0, 0)?
   - a) Green
   - b) Blue
   - c) Red
   - d) White
   - **Answer: c**

**Level 2: Intermediate**

3. Bresenham's line algorithm is preferred over DDA because:
   - a) It uses floating-point arithmetic
   - b) It uses only integer arithmetic
   - c) It cannot draw diagonal lines
   - d) It requires more memory
   - **Answer: b**

4. In the Cohen-Sutherland line clipping algorithm, if the bitwise AND of endpoint codes is non-zero, the line is:
   - a) Completely inside
   - b) Completely outside
   - c) Partially inside
   - d) Cannot be determined
   - **Answer: b**

5. Which transformation changes the size of an object?
   - a) Translation
   - b) Rotation
   - c) Scaling
   - d) Shearing
   - **Answer: c**

**Level 3: Advanced/Application-Based**

6. A point (5, 5) is rotated 90° counterclockwise around origin. What is the new position?
   - a) (-5, 5)
   - b) (5, -5)
   - c) (-5, -5)
   - d) (0, 0)
   - **Answer: a**

7. In a Z-buffer algorithm with normalized depth (0=near, 1=far), a fragment at depth 0.3 compared to a stored depth 0.5 will:
   - a) Be discarded
   - b) Update both color and depth buffer
   - c) Only update color buffer
   - d) Cause an error
   - **Answer: b**

8. If you want to display a scene with a red sphere behind a blue cube, which algorithm ensures correct visibility?
   - a) Back-face culling only
   - b) Painter's algorithm only
   - c) Z-buffer algorithm
   - d) Wireframe rendering
   - **Answer: c**

9. For a 3D transformation pipeline, the correct order of transformations to rotate an object around its own center is:
   - a) Translate to origin → Rotate → Translate back
   - b) Rotate → Translate to origin → Translate back
   - c) Translate back → Translate to origin → Rotate
   - d) Rotate directly without translation
   - **Answer: a**

10. Which color model is most suitable for a color picker in a painting application?
    - a) CMY
    - b) RGB
    - c) HSV
    - d) Indexed color
    - **Answer: c**

### 13.2 Short Answer Questions

1. **Explain the concept of homogeneous coordinates in computer graphics.** (5 marks)
   - *Answer: Homogeneous coordinates represent n-dimensional points using n+1 coordinates. For 2D, a point (x, y) becomes (x, y, 1). This allows all geometric transformations (translation, rotation, scaling) to be represented as matrix multiplications, enabling concatenation of multiple transformations into a single matrix.*

2. **Compare raster scan and random scan displays.** (5 marks)
   - *Answer: Raster scan displays images by scanning rows horizontally, like a television, covering entire screen with refresh rate. Random scan (vector display) directs electron beam only to points that need drawing, producing wireframe images with higher resolution for specific lines but cannot display complex filled areas.*

3. **What is the purpose of the viewing transformation in the graphics pipeline?** (3 marks)
   - *Answer: Viewing transformation converts world coordinates to camera/eye coordinates, positioning the scene relative to the camera. It establishes the viewer's position and orientation, defining what portion of the scene is visible through the camera.*

4. **Differentiate between back-face culling and hidden surface removal.** (5 marks)
   - *Answer: Back-face culling eliminates polygons facing away from the camera, reducing the number of primitives to process. Hidden surface removal determines which surfaces are actually visible when objects overlap, ensuring correct visibility in complex 3D scenes. Culling is a pre-processing optimization, while hidden surface removal handles actual visibility determination.*

### 13.3 Long Answer Questions

1. **Describe the complete graphics pipeline, explaining each stage with its functions.** (10 marks)
   - *Answer should cover: Application stage (geometry definition), Vertex processing (transformations, lighting), Primitive assembly (grouping vertices, clipping), Rasterization (converting to fragments), Fragment processing (texturing, shading), and Output merger (depth testing, blending).*

2. **Explain the Z-buffer algorithm for hidden surface removal. Discuss its advantages and limitations.** (10 marks)
   - *Answer should include: Initialization of depth buffer, per-pixel depth comparison, update mechanism, advantages (handles arbitrary geometry, simple to implement), limitations (memory overhead, no transparency handling without additional logic).*

3. **Write and explain the Bresenham's line drawing algorithm. Why is it more efficient than the DDA algorithm?** (10 marks)
   - *Answer should include: Algorithm steps, decision variable approach, integer-only arithmetic, comparison with floating-point operations in DDA, why integer operations are faster.*

---

## 14. Flashcards

### Concept Flashcards

| Term | Definition |
|------|------------|
| **Frame Buffer** | Memory that stores the complete image to be displayed on screen |
| **Refresh Rate** | Number of times per second the display updates the image (measured in Hz) |
| **Color Depth** | Number of bits used to represent each pixel's color |
| **Homogeneous Coordinates** | Coordinates with one additional dimension (w), allowing transformations as matrix multiplications |
| **Clipping** | Process of removing portions of primitives outside the viewing region |
| **Z-Buffer** | Algorithm using depth information to determine visible surfaces |
| **Rasterization** | Converting geometric primitives into pixels on a raster display |
| **Back-face Culling** | Optimization that discards polygons facing away from the camera |
| **Gouraud Shading** | Color interpolation across polygon vertices for smooth shading |
| **Phong Shading** | Per-pixel lighting calculation for more accurate shading |
| **Model Matrix** | Transformation matrix that positions objects in world space |
| **View Matrix** | Transformation matrix that positions world space relative to camera |
| **Projection Matrix** | Transformation matrix that converts 3D to 2D (perspective or orthographic) |
| **Scanline** | Horizontal line of pixels processed during polygon filling |
| **Vertex Shader** | Program that processes each vertex in the graphics pipeline |
| **Fragment Shader** | Program that processes each fragment (potential pixel) |
| **Double Buffering** | Using two frame buffers to prevent visual flickering |
| **Anti-aliasing** | Technique to smooth jagged edges in raster graphics |
| **Texture Mapping** | Applying 2D images (textures) to 3D surfaces |
| **Alpha Blending** | Combining colors with transparency information |

---

## 15. References and Further Reading

1. Donald Hearn and M. Pauline Baker, "Computer Graphics with OpenGL"
2. Foley, van Dam, Feiner, Hughes, "Computer Graphics: Principles and Practice"
3. OpenGL Documentation: https://www.opengl.org/
4. Delhi University BSc (Hons) Computer Science NEP 2024 Syllabus

---

*This study material covers the complete DSE-CG Computer Graphics syllabus for Delhi University's BSc (Hons) Computer Science program under NEP 2024 UGCF guidelines.*