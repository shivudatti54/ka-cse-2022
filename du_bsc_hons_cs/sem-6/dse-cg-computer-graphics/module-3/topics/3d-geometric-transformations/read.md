# 3D Geometric Transformations

## Comprehensive Study Material for BSc (Hons) Computer Science

### Delhi University - NEP 2024 UGCF (DSE-CG: Computer Graphics)

---

## 1. Introduction

**3D Geometric Transformations** form the foundation of computer graphics, enabling the manipulation of objects in three-dimensional space. These transformations are essential for rendering scenes, animating objects, and simulating real-world environments. In the context of the Delhi University syllabus for DSE-CG (Computer Graphics), understanding 3D transformations is crucial for students to master the core concepts required for graphics programming and visual computing.

In this study material, we will cover all major 3D transformation types, their mathematical representations using homogeneous coordinates, composite transformations, and practical implementation through code examples.

---

## 2. Real-World Relevance

3D geometric transformations are extensively used in various real-world applications:

- **Video Game Development**: Character movement, camera controls, and environment rendering
- **Computer-Aided Design (CAD)**: Modeling and manipulating 3D objects in engineering
- **Medical Imaging**: CT scans and MRI visualizations
- **Virtual Reality (VR) and Augmented Reality (AR)**: Immersive experience creation
- **Animation and Film Production**: CGI and special effects
- **Robotics**: Path planning and object manipulation
- **Architectural Visualization**: Building walkthroughs and rendering

---

## 3. Fundamentals of 3D Transformations

### 3.1 Homogeneous Coordinates

In 3D graphics, points in space are represented using **homogeneous coordinates** (x, y, z, w), where the actual 3D point is obtained by dividing the first three coordinates by w (when w ≠ 0). This allows all geometric transformations to be represented as **4×4 matrices**, enabling matrix multiplication for composite transformations.

A 3D point P(x, y, z) is represented as P̂ = [x, y, z, 1]ᵀ in homogeneous coordinates.

### 3.2 General Transformation Matrix

The general 4×4 transformation matrix has the following structure:

```
| a  b  c  tx |
| d  e  f  ty |
| g  h  i  tz |
| 0  0  0  1  |
```

Where:
- The 3×3 upper-left submatrix (a to i) handles rotation, scaling, and shearing
- The fourth column (tx, ty, tz) handles translation
- The last row is [0 0 0 1] for affine transformations

---

## 4. Basic 3D Transformations

### 4.1 Translation

Translation moves a point from one position to another by adding displacement values along each axis. It is a **rigid body transformation** that preserves distances and angles.

**Translation Matrix T(tx, ty, tz)**:

```
| 1  0  0  tx |
| 0  1  0  ty |
| 0  0  1  tz |
| 0  0  0  1  |
```

**Mathematical Representation**:
```
x' = x + tx
y' = y + ty
z' = z + tz
```

**Properties**:
- Commutative with other translations
- Preserves shape and size
- Inverse: T⁻¹(tx, ty, tz) = T(-tx, -ty, -tz)

### 4.2 Rotation

Rotation turns objects around a specified axis by a given angle (θ). The direction of positive rotation follows the **right-hand rule**.

#### 4.2.1 Rotation about X-axis

```
| 1    0       0    0 |
| 0  cos(θ) -sin(θ)  0 |
| 0  sin(θ)  cos(θ)  0 |
| 0    0       0    1 |
```

#### 4.2.2 Rotation about Y-axis

```
| cos(θ)  0  sin(θ)  0 |
|   0     1    0     0 |
| -sin(θ) 0  cos(θ)  0 |
|   0     0    0     1 |
```

#### 4.2.3 Rotation about Z-axis

```
| cos(θ) -sin(θ)  0  0 |
| sin(θ)  cos(θ)  0  0 |
|   0       0     1  0 |
|   0       0     0  1 |
```

#### 4.2.4 Rotation about Arbitrary Axis

For rotation about an arbitrary axis passing through the origin with direction vector (a, b, c):

1. **Normalize the axis vector**: (a', b', c')
2. Use the general rotation matrix formula

**Properties**:
- Preserves distances (orthogonal transformation)
- Determinant = +1
- Inverse: R⁻¹(θ) = R(-θ) = R(θ)ᵀ

### 4.3 Scaling

Scaling changes the size of an object by multiplying coordinates by scale factors along each axis.

**Scaling Matrix S(sx, sy, sz)**:

```
| sx  0   0  0 |
| 0  sy   0  0 |
| 0   0  sz  0 |
| 0   0   0  1 |
```

**Types of Scaling**:
- **Uniform Scaling**: sx = sy = sz (maintains proportions)
- **Non-uniform Scaling**: Different values along each axis
- **Reflection (mirroring)**: One or more scale factors are negative

**Mathematical Representation**:
```
x' = x × sx
y' = y × sy
z' = z × sz
```

**Properties**:
- Inverse: S⁻¹(sx, sy, sz) = S(1/sx, 1/sy, 1/sz)
- When sx = sy = sz = -1, it becomes **reflection through origin**

### 4.4 Shearing

Shearing distorts the shape of an object by shifting one coordinate proportionally to another.

**Shearing Matrix (along x-axis based on y and z)**:

```
| 1  shxy  shxz  0 |
| 0   1    0    0 |
| 0   0    1    0 |
| 0   0    0    1 |
```

Where `shxy` is the shear in x-direction proportional to y, and `shxz` is shear in x-direction proportional to z.

**Types**:
- **XY Shear**: x' = x + shxy × y
- **XZ Shear**: x' = x + shxz × z
- **YZ Shear**: y' = y + shyz × z + shzx × z

### 4.5 Reflection

**Reflection is indeed a valid 3D transformation** that creates a mirror image of an object across a plane or axis. This was incorrectly stated in the previous version.

**Reflection across XY-plane (z = 0)**:
```
| 1  0   0  0 |
| 0  1   0  0 |
| 0  0  -1  0 |
| 0  0   0  1 |
```

**Reflection across YZ-plane (x = 0)**:
```
| -1  0  0  0 |
|  0  1  0  0 |
|  0  0  1  0 |
|  0  0  0  1 |
```

**Reflection across XZ-plane (y = 0)**:
```
| 1   0  0  0 |
| 0  -1  0  0 |
| 0   0  1  0 |
| 0   0  0  1 |
```

**Reflection through Origin**:
```
| -1  0  0  0 |
|  0 -1  0  0 |
|  0  0 -1  0 |
|  0  0  0  1 |
```

---

## 5. Composite Transformations

A **composite transformation** combines multiple basic transformations into a single matrix. This is crucial for efficient graphics operations as it reduces multiple matrix multiplications to one.

### 5.1 Process for Composite Transformations

1. Start with the identity matrix
2. Multiply by each transformation matrix in the desired order
3. Apply the composite matrix to the points

**Important**: Matrix multiplication is **not commutative** — the order of transformations matters significantly!

### 5.2 Common Composite Transformations

#### 5.2.1 Rotation about an Arbitrary Point (not origin)

To rotate an object about a point P(a, b, c):

1. **Translate** the object so that P moves to origin: T(-a, -b, -c)
2. **Rotate** about the origin: R(θ)
3. **Translate** back: T(a, b, c)

**Composite Matrix**: T(a, b, c) × R(θ) × T(-a, -b, -c)

#### 5.2.2 Scaling about an Arbitrary Point

To scale an object about a point P(a, b, c):

1. Translate to origin: T(-a, -b, -c)
2. Scale: S(sx, sy, sz)
3. Translate back: T(a, b, c)

**Composite Matrix**: T(a, b, c) × S(sx, sy, sz) × T(-a, -b, -c)

#### 5.2.3 Change of Coordinate Systems

To transform coordinates from one system to another:
- Translate origin to new position
- Apply rotations to align axes

---

## 6. Examples with Code

### Example 1: Implementing 3D Rotation in Python

```python
import numpy as np
import math

def create_rotation_matrix_x(theta):
    """Create rotation matrix about X-axis"""
    c = math.cos(theta)
    s = math.sin(theta)
    return np.array([
        [1,  0,  0, 0],
        [0,  c, -s, 0],
        [0,  s,  c, 0],
        [0,  0,  0, 1]
    ])

def create_rotation_matrix_y(theta):
    """Create rotation matrix about Y-axis"""
    c = math.cos(theta)
    s = math.sin(theta)
    return np.array([
        [ c,  0,  s, 0],
        [ 0,  1,  0, 0],
        [-s,  0,  c, 0],
        [ 0,  0,  0, 1]
    ])

def create_rotation_matrix_z(theta):
    """Create rotation matrix about Z-axis"""
    c = math.cos(theta)
    s = math.sin(theta)
    return np.array([
        [c, -s,  0, 0],
        [s,  c,  0, 0],
        [0,  0,  1, 0],
        [0,  0,  0, 1]
    ])

def transform_point(point, matrix):
    """Apply transformation matrix to a 3D point"""
    point_h = np.array([point[0], point[1], point[2], 1])
    result = np.dot(matrix, point_h)
    return result[:3]  # Return x, y, z

# Example: Rotate point (1, 0, 0) by 90 degrees about Y-axis
point = np.array([1.0, 0.0, 0.0])
theta = math.radians(90)  # Convert to radians

ry = create_rotation_matrix_y(theta)
new_point = transform_point(point, ry)
print(f"Original: {point}")
print(f"After 90° Y-rotation: {new_point}")
# Expected output: [0, 0, -1]
```

### Example 2: Composite Transformation for 3D Object Rotation

```python
import numpy as np
import math

def translation_matrix(tx, ty, tz):
    """Create translation matrix"""
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def rotation_matrix_z(theta):
    """Create rotation matrix about Z-axis"""
    c = math.cos(theta)
    s = math.sin(theta)
    return np.array([
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])

def scale_matrix(sx, sy, sz):
    """Create scaling matrix"""
    return np.array([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1]
    ])

def rotate_about_point(point, axis_point, theta):
    """
    Rotate a point about an arbitrary point in 3D
    Step 1: Translate so axis_point is at origin
    Step 2: Rotate about Z-axis
    Step 3: Translate back
    """
    # Move point to origin-relative position
    T1 = translation_matrix(-axis_point[0], -axis_point[1], -axis_point[2])
    # Rotate
    R = rotation_matrix_z(theta)
    # Move back
    T2 = translation_matrix(axis_point[0], axis_point[1], axis_point[2])
    
    # Composite transformation: T2 × R × T1
    composite = np.dot(T2, np.dot(R, T1))
    
    # Apply to point
    point_h = np.array([point[0], point[1], point[2], 1])
    result = np.dot(composite, point_h)
    return result[:3]

# Example: Rotate point (2, 2, 0) by 90° about point (1, 1, 0)
point = np.array([2.0, 2.0, 0.0])
axis_point = np.array([1.0, 1.0, 0.0])
theta = math.radians(90)

new_point = rotate_about_point(point, axis_point, theta)
print(f"Original: {point}")
print(f"After rotation about ({axis_point}): {new_point}")
# Expected: [1, 2, 0] (rotates 90° clockwise around (1,1))
```

### Example 3: Scaling and Translation Composite

```python
import numpy as np

def create_composite_transform(scale, translate):
    """
    Create composite transformation: Translate then Scale
    Order matters: We apply translation first, then scale
    Matrix: S × T
    """
    # Scale matrix
    S = np.diag([scale[0], scale[1], scale[2], 1])
    # Translation matrix
    T = np.eye(4)
    T[0:3, 3] = translate
    
    # Composite: S × T (transform translation first, then scale)
    return np.dot(S, T)

# Example: Scale by 2x and translate by (1, 2, 3)
scale = (2.0, 2.0, 2.0)
translate = (1.0, 2.0, 3.0)

composite = create_composite_transform(scale, translate)
print("Composite Transformation Matrix:")
print(composite)

# Apply to a point (1, 1, 1)
point = np.array([1.0, 1.0, 1.0, 1.0])
result = np.dot(composite, point)
print(f"Original point: {point[:3]}")
print(f"After transform: {result[:3]}")
# Calculation: First translate: (1+1, 1+2, 1+3) = (2,3,4)
# Then scale: (2*2, 3*2, 4*2) = (4, 6, 8)
```

---

## 7. Key Takeaways

1. **Homogeneous Coordinates**: All 3D transformations use 4×4 matrices with homogeneous coordinates (x, y, z, 1) for unified representation.

2. **Translation**: Adds displacement values; matrix has identity in 3×3 submatrix and translation values in fourth column.

3. **Rotation**: 
   - Uses trigonometric functions (sin, cos)
   - Follows right-hand rule for positive rotation
   - Main axes rotations have specific matrix forms
   - Determinant = 1 (preserves volume)

4. **Scaling**: Multiplies coordinates by scale factors; uniform scaling maintains proportions; negative scaling creates reflection.

5. **Reflection**: **IS a valid 3D transformation** — creates mirror images across planes; represented by negative scale factors along specific axes.

6. **Shearing**: Distorts shape by making one coordinate dependent on others; useful for oblique projections.

7. **Composite Transformations**: 
   - Multiple transformations can be combined into single matrix
   - **Order is critical** — matrix multiplication is non-commutative
   - Use T × R × T⁻¹ format for rotation about arbitrary point

8. **Inverse Transformations**: Each basic transformation has an inverse that reverses its effect.

---

## 8. Assessment Materials

### 8.1 Multiple Choice Questions (MCQs)

**Q1. In 3D homogeneous coordinates, a point (x, y, z) is represented as:**
- a) [x, y, z]
- b) [x, y, z, 0]
- c) **[x, y, z, 1]** ✓
- d) [x, y, z, w]

**Q2. The determinant of a pure rotation matrix in 3D is:**
- a) 0
- b) -1
- c) **+1** ✓
- d) Any value

**Q3. Reflection IS a valid 3D transformation:**
- a) **True** ✓
- b) False
- c) Only in 2D
- d) Only about origin

**Q4. Which transformation matrix represents translation along z-axis by 5 units?**
- a) 
```
|1 0 0 0|
|0 1 0 0|
|0 0 1 5|
|0 0 0 1|
```
- b) 
```
|1 0 0 5|
|0 1 0 5|
|0 0 1 5|
|0 0 0 1|
```
- c) 
```
|1 0 0 0|
|0 1 0 0|
|0 0 1 5|
|0 0 0 1|
```
✓ (Answer a - note translation is in the fourth column for z)

**Q5. For rotating a point about an arbitrary point P, the correct order is:**
- a) Rotate, Translate, Translate
- b) **Translate to origin, Rotate, Translate back** ✓
- c) Translate, Rotate, Translate
- d) Scale, Rotate, Translate

**Q6. The scaling matrix S(sx, sy, sz) has non-zero values at positions:**
- a) (0,0), (1,1), (2,2), (3,3)
- b) (0,0), (1,1), (2,2)
- c) **(0,0), (1,1), (2,2)** — all diagonal positions ✓
- d) All positions in first three columns

**Q7. Matrix multiplication for transformations is:**
- a) Commutative
- b) **Non-commutative** ✓
- c) Associative only
- d) Distributive only

**Q8. Uniform scaling with factor k where k > 1 results in:**
- a) Shrinking the object
- b) **Enlarging the object** ✓
- c) No change
- d) Distorting the object

### 8.2 Short Answer Questions

**Q1. What are homogeneous coordinates? Why are they used in 3D graphics?**

*Answer: Homogeneous coordinates represent 3D points using 4 coordinates (x, y, z, w). They allow all geometric transformations (translation, rotation, scaling) to be represented as 4×4 matrices, enabling matrix multiplication for composite transformations. The actual 3D point is obtained by dividing x, y, z by w.*

**Q2. Differentiate between uniform and non-uniform scaling with examples.**

*Answer: Uniform scaling applies the same scale factor along all axes, maintaining the object's proportions (e.g., S(2, 2, 2) doubles the size equally). Non-uniform scaling uses different factors along each axis (e.g., S(2, 1, 0.5) doubles width, keeps height, halves depth), which can distort the object.*

**Q3. State and explain the right-hand rule for 3D rotation.**

*Answer: The right-hand rule determines the positive direction of rotation. Point the thumb of your right hand along the axis of rotation (positive direction); the curl of your fingers indicates the positive rotation angle. For example, rotation about the positive Z-axis appears counterclockwise when viewed from the positive Z direction.*

**Q4. Why is the order of matrix multiplication important in composite transformations?**

*Answer: Matrix multiplication is non-commutative, meaning A×B ≠ B×A. The order of transformations matters because each successive transformation is applied in the coordinate system established by previous transformations. For example, "rotate then translate" produces a different result than "translate then rotate."*

**Q5. How is reflection represented as a transformation matrix? Give an example.**

*Answer: Reflection is represented by negative scale factors. For reflection across the XY-plane (z=0), the matrix is:*

```
| 1  0  0  0 |
| 0  1  0  0 |
| 0  0 -1  0 |
| 0  0  0  1 |
```

*This negates the z-coordinate, creating a mirror image across the XY-plane.*

### 8.3 Long Answer Questions

**Q1. Derive the rotation matrices for rotation about X, Y, and Z axes. Explain how these can be used to rotate an object about an arbitrary axis.**

*Answer: [Derive matrices as shown in Section 4.2. For arbitrary axis rotation, explain the process using normalized direction vectors and the general rotation formula, or using the three-step approach of aligning the axis to a coordinate axis, rotating, and restoring.]*

**Q2. Explain the process of performing rotation about an arbitrary point in 3D space. Derive the composite transformation matrix.**

*Answer: [As explained in Section 5.2.1: 1) Translate object so point moves to origin, 2) Rotate about origin, 3) Translate back. Matrix: T(a,b,c) × R(θ) × T(-a,-b,-c)]*

**Q3. Discuss composite transformations in detail with examples. How would you implement a transformation that scales an object by 2x and then rotates it by 45° about its center?**

*Answer: [Comprehensive explanation of composite transformations with the code example demonstrated in Section 6, explaining the mathematical basis and implementation.]*

**Q4. Compare and contrast all 3D geometric transformations: translation, rotation, scaling, shearing, and reflection. Include their matrix representations and properties.**

*Answer: [Detailed comparison covering: matrix structure for each transformation, effect on object geometry, inverse operations, and practical applications as covered in Section 4.]*

---

## 9. References and Further Reading

- Delhi University BSc (Hons) Computer Science NEP 2024 UGCF Syllabus
- "Computer Graphics: Principles and Practice" by Foley, van Dam, Feiner, Hughes
- "Computer Graphics with OpenGL" by Hearn and Baker
- Class notes and lecture materials from DSE-CG (Computer Graphics)

---

*This study material covers all essential topics for the Delhi University BSc (Hons) Computer Science examination under NEP 2024 UGCF curriculum.*