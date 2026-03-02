# 2D Geometric Transformations

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

**2D Geometric Transformations** form a fundamental pillar of computer graphics, enabling the manipulation of graphical objects in two-dimensional space. These mathematical operations allow us to translate (move), rotate, scale (resize), and shear (skew) graphical elements, which is essential for everything from simple image editing to complex animation systems and game development.

In the context of the **DSE-CG (Discipline Specific Elective - Computer Graphics)** course under the **NEP 2024 UGCF curriculum** at Delhi University, this topic carries significant weight as it forms the backbone of rendering pipelines and graphical user interfaces. Understanding these transformations is not merely academic—it powers the digital world around us, from the animations in your favorite mobile games to the CAD software used by architects and engineers.

### Real-World Relevance

- **Animation Studios**: Pixar and Disney use geometric transformations to animate characters
- **Video Games**: Every character movement involves translation, rotation, and scaling
- **Medical Imaging**: CT scans and MRIs use transformations to align and compare images
- **Computer-Aided Design (CAD)**: Architects use transformations to manipulate building models
- **Robotics**: Path planning and robot movement rely on geometric transformations

---

## 2. Fundamental Concepts

### 2.1 What Are Geometric Transformations?

A **geometric transformation** is a function that maps points from one coordinate system to another. In 2D computer graphics, we typically work with points defined by their (x, y) coordinates and apply mathematical operations to transform these points.

### 2.2 Types of Transformations

The five fundamental 2D geometric transformations are:

1. **Translation** — Moving a point/object from one position to another
2. **Rotation** — Rotating a point/object around a pivot point
3. **Scaling** — Enlarging or shrinking an object
4. **Shearing** — Slanting/skewing an object along an axis
5. **Composite Transformations** — Combining multiple transformations into one

### 2.3 Coordinate Systems

In computer graphics, we primarily work with:

- **Screen Coordinates**: Origin at top-left corner, y increases downward
- **Cartesian Coordinates**: Origin at center, y increases upward (mathematical convention)

For transformation mathematics, we use the **Cartesian coordinate system** and then convert to screen coordinates for display.

---

## 3. Translation

### 3.1 Definition

**Translation** moves every point of a figure or object by the same distance in a given direction. It is a rigid motion that preserves the shape and size of the object.

### 3.2 Mathematical Formulation

Given a point P(x, y) and translation distances (tx, ty), the translated point P'(x', y') is:

```
x' = x + tx
y' = y + ty
```

In matrix form using **homogeneous coordinates**:

```
| x' |   | 1  0  tx |   | x |
| y' | = | 0  1  ty | × | y |
| 1  |   | 0  0  1  |   | 1 |
```

### 3.3 Translation Matrix

The general translation matrix in homogeneous form is:

```
T(tx, ty) = | 1   0   tx |
            | 0   1   ty |
            | 0   0   1  |
```

### 3.4 Properties of Translation

- **Preserves distances** between points
- **Preserves angles** within the object
- **Preserves parallelism** of lines
- The translation vector (tx, ty) determines the direction and magnitude of movement

### 3.5 Example: Translating a Triangle

Consider a triangle with vertices A(2, 3), B(6, 3), and C(4, 7). Translate by tx = 3, ty = 2:

- A' = (2+3, 3+2) = (5, 5)
- B' = (6+3, 3+2) = (9, 5)
- C' = (4+3, 7+2) = (7, 9)

---

## 4. Rotation

### 4.1 Definition

**Rotation** turns a point or object around a fixed point called the **center of rotation** (or pivot point) by a specified angle. By convention, positive angles rotate counter-clockwise (CCW), while negative angles rotate clockwise (CW).

### 4.2 Mathematical Formulation

Given a point P(x, y), center of rotation (xc, yc), and angle θ (in radians), the rotated point P'(x', y') is:

```
x' = xc + (x - xc)cos(θ) - (y - yc)sin(θ)
y' = yc + (x - xc)sin(θ) + (y - yc)cos(θ)
```

### 4.3 Rotation Matrix (Origin Rotation)

When rotating around the origin (0, 0):

```
| x' |   | cos(θ)  -sin(θ)  0 |   | x |
| y' | = | sin(θ)   cos(θ)  0 | × | y |
| 1  |   |   0        0     1 |   | 1 |
```

### 4.4 Rotation Matrix for Arbitrary Point

To rotate around point (xc, yc), we use:

```
R(θ, xc, yc) = | cos(θ)  -sin(θ)  xc(1-cos(θ)) + yc·sin(θ) |
               | sin(θ)   cos(θ)  yc(1-cos(θ)) - xc·sin(θ) |
               |    0        0               1              |
```

### 4.5 Properties of Rotation

- **Preserves distances** from the center of rotation
- **Preserves shape and size** of the object
- **Preserves angles** within the object
- The center of rotation remains fixed

### 4.6 Common Rotation Angles

| Angle (θ) | cos(θ) | sin(θ) |
|-----------|--------|--------|
| 0°        | 1      | 0      |
| 90°       | 0      | 1      |
| 180°      | -1     | 0      |
| 270°      | 0      | -1     |

---

## 5. Scaling

### 5.1 Definition

**Scaling** enlarges or shrinks an object by applying scale factors along the x and y axes. It can make objects larger (dilatation) or smaller (contraction).

### 5.2 Mathematical Formulation

Given scale factors sx (x-direction) and sy (y-direction), the scaled point P'(x', y') is:

```
x' = x × sx
y' = y × sy
```

### 5.3 Scaling Matrix

```
| x' |   | sx  0  0 |   | x |
| y' | = | 0  sy  0 | × | y |
| 1  |   | 0   0  1 |   | 1 |
```

### 5.4 Types of Scaling

1. **Uniform Scaling** (sx = sy): Maintains aspect ratio
   - sx = sy > 1: Uniform enlargement
   - 0 < sx = sy < 1: Uniform reduction

2. **Non-Uniform Scaling** (sx ≠ sy): Distorts aspect ratio
   - sx > 1, sy < 1: Stretches horizontally, compresses vertically

3. **Reflection** (Negative scaling): Creates a mirror image
   - sx = -1: Reflection across y-axis
   - sy = -1: Reflection across x-axis

### 5.5 Scaling About Origin vs. About Point

**Scaling about origin** is straightforward as shown above. To scale about a fixed point (xf, yf):

```
x' = xf + (x - xf) × sx
y' = yf + (y - yf) × sy
```

### 5.6 Properties of Scaling

- **Does not preserve distances** unless uniform
- **Preserves parallelism** of lines
- **Preserves angles** only in uniform scaling
- The origin is the default center of scaling

---

## 6. Shearing (Skewing)

### 6.1 Definition

**Shearing** (or skewing) displaces each point in a fixed direction, by an amount proportional to its signed distance from the line that is parallel to that direction and goes through the origin. It creates a "slanted" effect.

### 6.2 X-Shear

Displaces points along the x-axis based on their y-coordinate:

```
x' = x + shx × y
y' = y
```

Matrix form:

```
| x' |   | 1  shx  0 |   | x |
| y' | = | 0   1   0 | × | y |
| 1  |   | 0   0   1 |   | 1 |
```

### 6.3 Y-Shear

Displaces points along the y-axis based on their x-coordinate:

```
x' = x
y' = y + shy × x
```

Matrix form:

```
| x' |   | 1   0  0 |   | x |
| y' | = | shy  1  0 | × | y |
| 1  |   | 0   0  1 |   | 1 |
```

### 6.4 Combined Shear

To apply both x-shear and y-shear:

```
| x' |   | 1   shx  0 |   | x |
| y' | = | shy  1   0 | × | y |
| 1  |   | 0   0   1 |   | 1 |
```

### 6.5 Properties of Shearing

- **Preserves area** (determinant = 1)
- **Does not preserve distances** generally
- **Preserves parallelism** of lines
- Does not preserve angles (except in special cases)

---

## 7. Homogeneous Coordinates

### 7.1 Why Homogeneous Coordinates?

Homogeneous coordinates allow us to represent all affine transformations (translation, rotation, scaling, shearing) as matrix multiplications. This unified representation is crucial for the graphics pipeline.

### 7.2 Definition

A 2D point (x, y) is represented in homogeneous coordinates as (x, y, w), where:

```
x_homogeneous = x / w
y_homogeneous = y / w
```

Typically, we use w = 1, giving (x, y, 1).

### 7.3 General Transformation Matrix

```
| a  b  tx |
| c  d  ty |
| 0  0  1  |
```

Where:
- **a, b, c, d**: Handle rotation, scaling, and shearing
- **tx, ty**: Handle translation
- **Bottom row**: Always (0, 0, 1) for 2D affine transformations

### 7.4 Matrix Multiplication Order

**Important**: Matrix multiplication is **not commutative**. The order of transformations matters significantly:

```
P' = T × R × S × P  ≠  P' = S × R × T × P
```

In computer graphics, transformations are typically applied **right to left** in the code (the last transformation specified is applied first mathematically).

---

## 8. Composite Transformations

### 8.1 Definition

A **composite transformation** combines two or more basic transformations into a single transformation matrix. This improves computational efficiency by reducing the number of matrix multiplications during rendering.

### 8.2 Common Composite Operations

#### Rotation About an Arbitrary Point

To rotate by angle θ about point (xr, yr):

1. **Translate** the point to origin: T(-xr, -yr)
2. **Rotate** about origin: R(θ)
3. **Translate** back: T(xr, yr)

Matrix: **T(xr, yr) × R(θ) × T(-xr, -yr)**

#### Scaling About an Arbitrary Point

To scale by (sx, sy) about point (xf, yf):

1. Translate point to origin: T(-xf, -yf)
2. Scale about origin: S(sx, sy)
3. Translate back: T(xf, yf)

Matrix: **T(xf, yf) × S(sx, sy) × T(-xf, -yf)**

### 8.3 Composite Transformation Example

**Problem**: Rotate a point (3, 4) by 90° about point (1, 1)

**Solution**:
1. Translate to origin: T(-1, -1) → (2, 3)
2. Rotate 90° about origin: R(90°) → (-3, 2)
3. Translate back: T(1, 1) → (-2, 3)

Using matrices:
```
R(90°, 1, 1) = T(1,1) × R(90°) × T(-1,-1)
```

---

## 9. Practical Examples with Code

### Example 1: Translation, Rotation, and Scaling in C

```c
#include <stdio.h>

// Structure for a 2D point
typedef struct {
    float x, y;
} Point;

// Translation matrix application
Point translate(Point p, float tx, float ty) {
    Point result;
    result.x = p.x + tx;
    result.y = p.y + ty;
    return result;
}

// Rotation about origin (angle in radians)
Point rotate(Point p, float angle) {
    Point result;
    result.x = p.x * cos(angle) - p.y * sin(angle);
    result.y = p.x * sin(angle) + p.y * cos(angle);
    return result;
}

// Scaling about origin
Point scale(Point p, float sx, float sy) {
    Point result;
    result.x = p.x * sx;
    result.y = p.y * sy;
    return result;
}

int main() {
    Point p = {4, 3};
    float tx = 2, ty = 1;
    float angle = 3.14159 / 4;  // 45 degrees
    float sx = 2, sy = 0.5;
    
    // Apply transformations
    Point t = translate(p, tx, ty);
    printf("After translation: (%.2f, %.2f)\n", t.x, t.y);
    
    Point r = rotate(p, angle);
    printf("After rotation: (%.2f, %.2f)\n", r.x, r.y);
    
    Point s = scale(p, sx, sy);
    printf("After scaling: (%.2f, %.2f)\n", s.x, s.y);
    
    return 0;
}
```

### Example 2: Composite Transformation in Python

```python
import numpy as np
import matplotlib.pyplot as plt

def create_transformation_matrix(tx=0, ty=0, sx=1, sy=1, angle=0, cx=0, cy=0):
    """Create composite transformation matrix"""
    # Translation matrix
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    
    # Rotation matrix (about origin)
    R = np.array([[np.cos(angle), -np.sin(angle), 0],
                  [np.sin(angle),  np.cos(angle), 0],
                  [0,              0,             1]])
    
    # Scaling matrix
    S = np.array([[sx, 0,  0],
                  [0,  sy, 0],
                  [0,  0,  1]])
    
    # Center translation for rotation about arbitrary point
    Tc = np.array([[1, 0, cx],
                   [0, 1, cy],
                   [0, 0, 1]])
    
    Tc_inv = np.array([[1, 0, -cx],
                        [0, 1, -cy],
                        [0, 0, 1]])
    
    # Composite: Translate to center, scale, rotate, translate back
    M = Tc @ S @ R @ Tc_inv @ T
    return M

def apply_transform(point, matrix):
    """Apply transformation matrix to a point"""
    homogeneous = np.array([point[0], point[1], 1])
    transformed = matrix @ homogeneous
    return (transformed[0], transformed[1])

# Example: Rectangle vertices
rectangle = [(0, 0), (4, 0), (4, 3), (0, 3)]

# Create composite transformation
M = create_transformation_matrix(tx=2, ty=1, sx=1.5, sy=1.5, 
                                  angle=np.pi/6, cx=2, cy=1.5)

# Apply to all points
transformed_rect = [apply_transform(p, M) for p in rectangle]

print("Original:", rectangle)
print("Transformed:", transformed_rect)
```

---

## 10. Key Takeaways

1. **Translation** moves objects by adding translation vectors (tx, ty) to coordinates; represented by a matrix with 1s on diagonal and translation values in the third column.

2. **Rotation** turns objects around a center point; counter-clockwise is positive by convention; requires trigonometric functions (sin, cos).

3. **Scaling** enlarges or shrinks objects using scale factors (sx, sy); uniform scaling (sx = sy) preserves aspect ratio; negative scaling creates reflections.

4. **Shearing** skews objects by displacing points proportionally to their distance from an axis; preserves area but distorts angles.

5. **Homogeneous coordinates** (adding a third coordinate = 1) allow all affine transformations to be represented as matrix multiplications.

6. **Composite transformations** combine multiple operations into a single matrix for efficiency; order matters—transformations are applied right to left mathematically.

7. The general transformation matrix is:
   ```
   | a  b  tx |
   | c  d  ty |
   | 0  0  1  |
   ```
   where the 2×2 submatrix handles rotation/scaling/shearing, and (tx, ty) handles translation.

8. These transformations are the foundation of the graphics rendering pipeline and are essential for animation, game development, CAD systems, and image processing.

---

## 11. Multiple Choice Questions (MCQs)

### Easy Level

1. **Which transformation preserves the shape and size of an object but changes its position?**
   - A) Rotation
   - B) Scaling
   - C) Translation
   - D) Shearing
   
   **Answer: C**

2. **In a translation matrix, the translation values (tx, ty) are stored in:**
   - A) First row
   - B) Second row
   - C) Third column
   - D) Diagonal positions
   
   **Answer: C**

3. **A 90° rotation in counter-clockwise direction transforms point (1, 0) to:**
   - A) (0, 1)
   - B) (1, 0)
   - C) (-1, 0)
   - D) (0, -1)
   
   **Answer: A**

### Medium Level

4. **What type of transformation changes the aspect ratio of an object?**
   - A) Uniform scaling
   - B) Non-uniform scaling
   - C) Translation
   - D) Rotation about origin
   
   **Answer: B**

5. **The homogeneous coordinates of a 2D point (x, y) are typically represented as:**
   - A) (x, y)
   - B) (x, y, 0)
   - C) (x, y, 1)
   - D) (x, y, x+y)
   
   **Answer: C**

6. **Which of the following transformations preserve parallelism of lines?**
   - A) Translation only
   - B) Translation and rotation only
   - C) Translation, rotation, scaling, and shearing
   - D) None of the above
   
   **Answer: C**

7. **To rotate an object about an arbitrary point P, the correct sequence is:**
   - A) Rotate, Translate
   - B) Translate to origin, Rotate, Translate back
   - C) Scale, Rotate
   - D) Shear, Rotate
   
   **Answer: B**

### Hard Level

8. **A shear transformation with shx = 2 transforms point (3, 4) to:**
   - A) (3, 4)
   - B) (11, 4)
   - C) (5, 4)
   - D) (3, 10)
   
   **Answer: B** (x' = x + shx × y = 3 + 2×4 = 11)

9. **Matrix multiplication for transformations is:**
   - A) Commutative
   - B) Associative
   - C) Distributive over addition
   - D) All of the above
   
   **Answer: B** (associative but not commutative)

10. **The determinant of a pure shearing matrix is:**
    - A) 0
    - B) 1
    - C) -1
    - D) Cannot be determined
    
    **Answer: B** (shear preserves area, determinant = 1)

---

## 12. Flashcards

### Flashcard 1
**Q: What is the translation matrix T(tx, ty) in homogeneous coordinates?**

**A:**
```
| 1  0  tx |
| 0  1  ty |
| 0  0  1  |
```

---

### Flashcard 2
**Q: How do you rotate a point (x, y) by angle θ around the origin?**

**A:**
```
x' = x·cos(θ) - y·sin(θ)
y' = x·sin(θ) + y·cos(θ)
```

---

### Flashcard 3
**Q: What is the scaling matrix S(sx, sy)?**

**A:**
```
| sx  0  0 |
| 0  sy  0 |
| 0   0  1 |
```

---

### Flashcard 4
**Q: What is the x-shear transformation formula?**

**A:**
```
x' = x + shx·y
y' = y
```

Matrix form:
```
| 1  shx  0 |
| 0   1   0 |
| 0   0   1 |
```

---

### Flashcard 5
**Q: What is the sequence to rotate an object about an arbitrary point (cx, cy)?**

**A:**
1. Translate by (-cx, -cy) to move center to origin
2. Apply rotation R(θ) about origin
3. Translate by (cx, cy) to move back

Matrix: T(cx, cy) × R(θ) × T(-cx, -cy)

---

### Flashcard 6
**Q: What property makes homogeneous coordinates useful in computer graphics?**

**A:** They allow ALL affine transformations (translation, rotation, scaling, shearing) to be represented as matrix multiplications, enabling efficient composition of multiple transformations into a single matrix.

---

### Flashcard 7
**Q: What is uniform scaling vs. non-uniform scaling?**

**A:**
- **Uniform scaling**: sx = sy; preserves aspect ratio
- **Non-uniform scaling**: sx ≠ sy; distorts aspect ratio

---

### Flashcard 8
**Q: Why is transformation order important in composite transformations?**

**A:** Matrix multiplication is NOT commutative (A×B ≠ B×A). Different orders produce different results. For example, rotate-then-translate gives a different result than translate-then-rotate.

---

## 13. Assessment Items

### Short Answer Questions

1. **Define homogeneous coordinates and explain their importance in 2D geometric transformations.**

2. **Derive the transformation matrix for rotating a point by 90° counter-clockwise about the origin.**

3. **Explain why we use composite transformations instead of applying individual transformations sequentially.**

4. **Differentiate between uniform and non-uniform scaling with examples.**

5. **How does shearing differ from other transformations in terms of its effect on angles?**

### Long Answer Questions

6. **Explain the process of rotating an object about an arbitrary point (not the origin). Derive the composite transformation matrix and provide a numerical example.**

7. **Write a detailed note on the five fundamental 2D geometric transformations (translation, rotation, scaling, shearing, composite) including their matrices and properties.**

8. **Explain the concept of homogeneous coordinates. Show how all affine transformations can be represented as matrix operations in homogeneous coordinates.**

---

## 14. References and Syllabus Alignment

This study material aligns with the **DSE-CG (Computer Graphics)** module under the **NEP 2024 UGCF curriculum** for BSc (Hons) Computer Science at Delhi University. The content covers:

- Unit III: 2D Geometric Transformations
- Homogeneous coordinates and matrix representation
- Basic transformations: Translation, Rotation, Scaling, Shearing
- Composite transformations
- Practical implementation aspects

**Suggested References:**
- "Computer Graphics: Principles and Practice" by Foley, van Dam, Feiner, Hughes
- "Computer Graphics" by Donald Hearn and M. Pauline Baker
- Delhi University BSc (Hons) Computer Science NEP 2024 Syllabus

---

*End of Study Material*