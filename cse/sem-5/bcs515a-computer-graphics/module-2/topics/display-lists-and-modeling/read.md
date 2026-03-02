# Display Lists and Modeling in Computer Graphics

## Introduction

Display lists and modeling are fundamental concepts in computer graphics, particularly in the context of OpenGL programming. A **display list** is a group of OpenGL commands that have been stored (compiled) for later execution. When a display list is invoked, the commands within it are executed in the order in which they were originally stored. This mechanism provides significant performance improvements, especially when the same set of commands needs to be executed repeatedly.

**Modeling** in computer graphics refers to the process of creating mathematical representations of three-dimensional objects. It involves defining the geometry, topology, and appearance of objects in a scene. Hierarchical modeling, also known as scene graph modeling, allows complex objects to be built from simpler components using transformations. This approach mirrors real-world object composition — for example, a car model can be built from wheels, a body, doors, and windows, each defined independently and assembled using transformations.

Together, display lists and modeling form the backbone of efficient and structured graphics programming. Display lists optimize rendering performance by pre-compiling frequently used command sequences, while hierarchical modeling provides an organized framework for constructing complex scenes. These concepts are crucial for Computer Science students studying Computer Graphics (OpenGL-based courses) as they bridge the gap between basic rendering and real-world application development.

## Key Concepts

### Display Lists

#### What is a Display List?

A display list is a named collection of pre-compiled OpenGL commands stored on the server (GPU side). Once created, a display list can be called multiple times without re-sending or re-processing the commands. This is analogous to a compiled function — you define it once and call it whenever needed.

#### Creating a Display List

Display lists are created using the `glNewList()` and `glEndList()` functions:

```c
GLuint listID = glGenLists(1); // Generate a unique list ID

glNewList(listID, GL_COMPILE);
 // OpenGL commands go here
 glBegin(GL_TRIANGLES);
 glVertex3f(0.0, 0.0, 0.0);
 glVertex3f(1.0, 0.0, 0.0);
 glVertex3f(0.5, 1.0, 0.0);
 glEnd();
glEndList();
```

The second argument to `glNewList()` can be:

- **GL_COMPILE**: Commands are stored but not executed immediately.
- **GL_COMPILE_AND_EXECUTE**: Commands are both stored and executed immediately upon creation.

#### Executing a Display List

To execute (call) a display list:

```c
glCallList(listID);
```

To execute multiple display lists:

```c
glCallLists(n, type, lists);
```

#### Deleting a Display List

When a display list is no longer needed:

```c
glDeleteLists(listID, range);
```

#### Advantages of Display Lists

1. **Performance Optimization**: Commands are pre-compiled and stored on the server, reducing communication overhead between CPU and GPU.
2. **Code Reusability**: Define once, use many times.
3. **Network Efficiency**: In client-server architectures, display lists reduce network traffic as the commands reside on the server after creation.
4. **State Encapsulation**: Display lists can encapsulate state changes (color, material, transformations).

#### Limitations of Display Lists

- Once created, display lists **cannot be modified**. They must be deleted and recreated.
- Not all OpenGL commands can be stored in display lists (e.g., `glGenLists`, `glIsList`, `glDeleteLists` cannot be placed inside).
- They consume GPU memory.

### Modeling

#### Geometric Modeling

Geometric modeling involves defining the shape and structure of 3D objects. Common representations include:

- **Wireframe Models**: Objects represented by edges only.
- **Surface Models**: Objects defined by their surfaces (polygonal meshes, parametric surfaces).
- **Solid Models**: Complete volumetric representations (CSG, B-rep).

#### Hierarchical Modeling

Hierarchical modeling is a technique where complex objects are constructed from simpler sub-objects organized in a tree structure (scene graph). Each node in the hierarchy represents a component with its own local coordinate system and transformation.

**Key Principles:**

- Each object is defined in its own **local coordinate system**.
- **Parent-child relationships** define how parts are connected.
- Transformations propagate from parent to child nodes.
- The **model-view matrix stack** (`glPushMatrix()` and `glPopMatrix()`) is used to manage transformations hierarchically.

#### Using Matrix Stack for Hierarchical Modeling

OpenGL provides a matrix stack to handle nested transformations:

```c
glPushMatrix(); // Save current transformation state
 glTranslatef(x, y, z);
 glRotatef(angle, ax, ay, az);
 drawComponent(); // Draw in local coordinates

 glPushMatrix(); // Save state for sub-component
 glTranslatef(dx, dy, dz);
 drawSubComponent();
 glPopMatrix(); // Restore to parent state

glPopMatrix(); // Restore to original state
```

#### Instance Transformations

An **instance transformation** positions, orients, and scales a prototype object (master copy) to create an instance in the scene. Using display lists as prototypes and applying different transformations creates multiple instances efficiently.

```c
// Define prototype
GLuint cubeList = glGenLists(1);
glNewList(cubeList, GL_COMPILE);
 drawUnitCube();
glEndList();

// Create instances
glPushMatrix();
 glTranslatef(2.0, 0.0, 0.0);
 glScalef(1.0, 2.0, 1.0);
 glCallList(cubeList); // Tall cube at (2,0,0)
glPopMatrix();

glPushMatrix();
 glTranslatef(-2.0, 0.0, 0.0);
 glScalef(2.0, 1.0, 1.0);
 glCallList(cubeList); // Wide cube at (-2,0,0)
glPopMatrix();
```

#### Scene Graphs and DAGs

A **scene graph** is a directed acyclic graph (DAG) that represents the logical and spatial relationships of a scene. Each node can be:

- **Group node**: Contains transformations and children.
- **Leaf node**: Contains geometry (display lists).

This structure allows:

- Shared geometry (a wheel display list reused for all four wheels of a car).
- Efficient traversal for rendering.
- Easy manipulation of object hierarchies.

### Combining Display Lists and Modeling

Display lists and hierarchical modeling work synergistically:

1. **Prototyping**: Create display lists for basic shapes (cube, sphere, cylinder).
2. **Instancing**: Use instance transformations to place prototypes in the scene.
3. **Hierarchical Assembly**: Use the matrix stack to build complex objects from simpler display list components.
4. **Animation**: Modify transformation parameters each frame while reusing the same display lists.

## Examples

### Example 1: Creating and Using a Simple Display List

**Problem**: Create a display list for a colored triangle and render it at three different positions.

**Solution**:

```c
GLuint triangleList;

void init() {
 triangleList = glGenLists(1);
 glNewList(triangleList, GL_COMPILE);
 glBegin(GL_TRIANGLES);
 glColor3f(1.0, 0.0, 0.0);
 glVertex2f(0.0, 0.0);
 glColor3f(0.0, 1.0, 0.0);
 glVertex2f(1.0, 0.0);
 glColor3f(0.0, 0.0, 1.0);
 glVertex2f(0.5, 0.866);
 glEnd();
 glEndList();
}

void display() {
 glClear(GL_COLOR_BUFFER_BIT);

 // Instance 1: Original position
 glPushMatrix();
 glTranslatef(-2.0, 0.0, 0.0);
 glCallList(triangleList);
 glPopMatrix();

 // Instance 2: Scaled and translated
 glPushMatrix();
 glTranslatef(0.0, 0.0, 0.0);
 glScalef(1.5, 1.5, 1.0);
 glCallList(triangleList);
 glPopMatrix();

 // Instance 3: Rotated and translated
 glPushMatrix();
 glTranslatef(2.5, 0.0, 0.0);
 glRotatef(45.0, 0.0, 0.0, 1.0);
 glCallList(triangleList);
 glPopMatrix();

 glFlush();
}
```

**Explanation**: The triangle is defined once in the display list. Three instances are created using different transformations (translation, scaling, rotation). The `glPushMatrix()` and `glPopMatrix()` calls ensure each transformation is independent.

### Example 2: Hierarchical Model of a Simple Robot Arm

**Problem**: Model a 2D robot arm with a base, upper arm, and forearm using hierarchical modeling.

**Solution**:

```c
void drawRectangle(float width, float height) {
 glBegin(GL_POLYGON);
 glVertex2f(0.0, -height/2);
 glVertex2f(width, -height/2);
 glVertex2f(width, height/2);
 glVertex2f(0.0, height/2);
 glEnd();
}

float baseAngle = 0.0, elbowAngle = 0.0;

void display() {
 glClear(GL_COLOR_BUFFER_BIT);
 glLoadIdentity();

 // BASE (root of hierarchy)
 glPushMatrix();
 glTranslatef(0.0, 0.0, 0.0); // Base position
 glRotatef(baseAngle, 0.0, 0.0, 1.0); // Base rotation

 // Draw upper arm
 glColor3f(1.0, 0.0, 0.0);
 drawRectangle(100.0, 20.0); // Upper arm: 100x20

 // ELBOW (child of base)
 glTranslatef(100.0, 0.0, 0.0); // Move to end of upper arm
 glRotatef(elbowAngle, 0.0, 0.0, 1.0); // Elbow rotation

 // Draw forearm
 glColor3f(0.0, 0.0, 1.0);
 drawRectangle(80.0, 15.0); // Forearm: 80x15

 glPopMatrix();

 glFlush();
}
```

**Explanation**:

- The upper arm rotates about the base by `baseAngle`.
- The forearm is a child of the upper arm — it translates to the elbow joint, then rotates by `elbowAngle`.
- When `baseAngle` changes, both the upper arm and forearm move together (parent-child relationship).
- When `elbowAngle` changes, only the forearm moves relative to the upper arm.

### Example 3: Display List with Hierarchical Car Model

**Problem**: Create a simple 2D car using display lists for wheels and body.

**Solution**:

```c
GLuint wheelList, bodyList;

void createDisplayLists() {
 // Wheel prototype
 wheelList = glGenLists(2);
 glNewList(wheelList, GL_COMPILE);
 glColor3f(0.0, 0.0, 0.0);
 drawCircle(0.0, 0.0, 15.0); // Unit wheel
 glEndList();

 // Body prototype
 glNewList(wheelList + 1, GL_COMPILE);
 glColor3f(0.0, 0.0, 1.0);
 glRectf(-60.0, 0.0, 60.0, 30.0); // Car body
 glEndList();

 bodyList = wheelList + 1;
}

void display() {
 glClear(GL_COLOR_BUFFER_BIT);
 glLoadIdentity();

 glPushMatrix();
 glTranslatef(200.0, 100.0, 0.0); // Car position

 // Draw body
 glCallList(bodyList);

 // Left wheel (child of car)
 glPushMatrix();
 glTranslatef(-40.0, -5.0, 0.0);
 glCallList(wheelList);
 glPopMatrix();

 // Right wheel (child of car)
 glPushMatrix();
 glTranslatef(40.0, -5.0, 0.0);
 glCallList(wheelList);
 glPopMatrix();

 glPopMatrix();

 glFlush();
}
```

**Explanation**: The wheel display list is defined once but instantiated twice (left and right wheel). The body is another display list. All components are assembled hierarchically under a single car transformation, so moving the car moves all its parts.

## Exam Tips

1. **Definition Questions**: Be ready to define display lists clearly — emphasize that they are pre-compiled, stored on the server, and immutable once created. frequently asks 2-mark definitions.

2. **Function Syntax**: Memorize the key functions: `glGenLists()`, `glNewList()`, `glEndList()`, `glCallList()`, `glCallLists()`, `glDeleteLists()`, and their parameters. Pay attention to `GL_COMPILE` vs `GL_COMPILE_AND_EXECUTE`.

3. **Advantages/Disadvantages**: Questions asking to list advantages of display lists are common (4-5 marks). Always mention performance, reusability, and network efficiency.

4. **Matrix Stack Operations**: Understanding `glPushMatrix()` and `glPopMatrix()` is critical. Draw the stack state at each step if asked to trace through hierarchical code.

5. **Hierarchical Modeling Diagrams**: Practice drawing tree/DAG structures for scene graphs. Label nodes with transformations and leaf nodes with geometry. The robot arm example is a favorite.

6. **Code Writing**: Be prepared to write short OpenGL programs (10-mark questions) demonstrating display list creation and hierarchical modeling. The robot arm and simple vehicle models are commonly asked.

7. **Differentiate Concepts**: Know the difference between immediate mode rendering and display list rendering. Also understand how display lists differ from vertex buffer objects (VBOs) conceptually.
