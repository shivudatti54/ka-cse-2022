# Translation and Scaling in 2D Computer Graphics

## Introduction

Translation and scaling are fundamental geometric transformations in computer graphics that form the backbone of all visual manipulations performed on digital images and objects. These transformations are essential for creating animations, designing user interfaces, rendering 3D scenes, and performing virtually any graphical operation that involves moving or resizing objects on a screen. Understanding these transformations is crucial for any computer science engineer, as they are extensively used in applications ranging from video games and computer-aided design (CAD) software to medical imaging and virtual reality systems.

In the context of 's Computer Graphics curriculum, translation and scaling represent the most basic yet indispensable operations in the transformation pipeline. Translation refers to the process of moving an object from one position to another without altering its shape, orientation, or size. Scaling, on the other hand, involves resizing an object either uniformly or non-uniformly along the coordinate axes. Together with rotation (which will be covered in subsequent modules), these transformations enable programmers to manipulate graphical objects with complete freedom. The mathematical foundations of these transformations are based on homogeneous coordinates and matrix operations, which provide an elegant and computationally efficient way to combine multiple transformations into a single operation.

## Key Concepts

### Homogeneous Coordinates

Before discussing translation and scaling, it is essential to understand homogeneous coordinates, which provide a unified framework for representing all affine transformations. In 2D Cartesian coordinates, a point is represented as (x, y). In homogeneous coordinates, the same point is represented as (x, y, w), where the relationship between Cartesian and homogeneous coordinates is given by x = x'/w and y = y'/w. For practical purposes in computer graphics, we typically set w = 1, representing the point as a 3-element column vector [x, y, 1]^T.

The advantage of using homogeneous coordinates becomes apparent when we represent transformations as matrices. Without homogeneous coordinates, translation would require addition, while scaling would require multiplication. By using homogeneous coordinates, both transformations can be expressed as matrix multiplication, allowing us to combine multiple transformations into a single composite transformation matrix through matrix multiplication.

### Translation

Translation is a transformation that moves every point of an object by the same distance in a given direction. If a point P has coordinates (x, y) and we want to translate it by distances tx and ty along the x and y axes respectively, the translated point P' will have coordinates (x + tx, y + ty).

In matrix form using homogeneous coordinates, translation is represented as:

```
| 1 0 tx | | x | | x + tx |
| 0 1 ty | × | y | = | y + ty |
| 0 0 1 | | 1 | | 1 |
```

The 3×3 matrix shown above is called the translation matrix T(tx, ty). Key properties of translation include:

- It preserves parallelism: parallel lines remain parallel after translation
- It preserves angles: all angles remain unchanged
- It is a rigid body transformation: the shape and size of the object remain unchanged
- Translation is commutative: the order of applying multiple translations does not matter (T1 × T2 = T2 × T1)

### Scaling

Scaling is a transformation that changes the size of an object by multiplying the coordinates by scale factors. There are two types of scaling: uniform scaling (where the scale factor is the same in all directions) and non-uniform scaling (where different scale factors are applied to different axes).

For a point P(x, y) scaled by factors sx and sy along the x and y axes respectively, the scaled point P' has coordinates (x × sx, y × sy).

In matrix form using homogeneous coordinates, scaling is represented as:

```
| sx 0 0 | | x | | x × sx |
| 0 sy 0 | × | y | = | y × sy |
| 0 0 1 | | 1 | | 1 |
```

The matrix S(sx, sy) is the scaling matrix. Important properties include:

- When sx = sy = 1, no scaling occurs (identity transformation)
- When sx > 1 or sy > 1, the object enlarges (dilation)
- When 0 < sx < 1 or 0 < sy < 1, the object shrinks (contraction)
- When sx or sy is negative, the object undergoes reflection along that axis
- Scaling is not commutative: S1 × S2 ≠ S2 × S1 in general

### Fixed Point Scaling

A crucial concept in scaling is scaling about a fixed point (also called pivot point). By default, scaling occurs about the origin (0, 0), which means the object moves away from or toward the origin. To scale an object about a specific point (xf, yf), we must:

1. Translate the object so that the fixed point moves to the origin
2. Apply the scaling transformation
3. Translate the object back so that the fixed point returns to its original position

The composite transformation matrix for scaling about a fixed point is: T(xf, yf) × S(sx, sy) × T(-xf, -yf)

This sequence ensures that the point (xf, yf) remains stationary while the rest of the object scales relative to it.

### Composite Transformations

One of the most powerful aspects of using matrix representations is the ability to combine multiple transformations into a single composite matrix. For example, if we want to translate an object and then scale it, we multiply the translation matrix by the scaling matrix: M = S × T. The order of multiplication is critical because matrix multiplication is not commutative. The composite transformation is applied from right to left: first T, then S.

## Examples

### Example 1: Translating a Triangle

Consider a triangle with vertices at A(2, 3), B(5, 3), and C(2, 7). Translate this triangle by tx = 4 units in the x-direction and ty = -2 units in the y-direction.

**Solution:**

Using the translation formula: P'(x') = P(x + tx, y + ty)

- Vertex A: (2 + 4, 3 + (-2)) = (6, 1)
- Vertex B: (5 + 4, 3 + (-2)) = (9, 1)
- Vertex C: (2 + 4, 7 + (-2)) = (6, 5)

The translated triangle has vertices at A'(6, 1), B'(9, 1), and C'(6, 5).

**Matrix Method:**

Using the translation matrix T(4, -2):

```
| 1 0 4 | | 2 | | 6 |
| 0 1 -2 | × | 3 | = | 1 |
| 0 0 1 | | 1 | | 1 |
```

This confirms A' = (6, 1). Similarly, we can verify B' and C'.

### Example 2: Scaling a Rectangle

A rectangle has vertices at P1(1, 1), P2(4, 1), P3(4, 3), and P4(1, 3). Apply uniform scaling with scale factor 2.5.

**Solution:**

Using scaling formula: P'(x') = P(x × sx, y × sy), with sx = sy = 2.5

- P1: (1 × 2.5, 1 × 2.5) = (2.5, 2.5)
- P2: (4 × 2.5, 1 × 2.5) = (10, 2.5)
- P3: (4 × 2.5, 3 × 2.5) = (10, 7.5)
- P4: (1 × 2.5, 3 × 2.5) = (2.5, 7.5)

The scaled rectangle has dimensions 7.5 × 5 (original was 3 × 2), representing a 2.5 times increase in both width and height.

### Example 3: Scaling About a Fixed Point

A line segment has endpoints at A(2, 4) and B(6, 8). Scale this line by a factor of 0.5 about the fixed point F(4, 6).

**Solution:**

We apply the three-step process: T(-4, -6) → S(0.5, 0.5) → T(4, 6)

**For Point A(2, 4):**
Step 1 (Translate to origin): (2 - 4, 4 - 6) = (-2, -2)
Step 2 (Scale): (-2 × 0.5, -2 × 0.5) = (-1, -1)
Step 3 (Translate back): (-1 + 4, -1 + 6) = (3, 5)

**For Point B(6, 8):**
Step 1: (6 - 4, 8 - 6) = (2, 2)
Step 2: (2 × 0.5, 2 × 0.5) = (1, 1)
Step 3: (1 + 4, 1 + 6) = (5, 7)

The scaled line segment has endpoints at A'(3, 5) and B'(5, 7). Notice that point F(4, 6) remains unchanged: (4-4=0, 6-6=0) → (0×0.5=0, 0×0.5=0) → (0+4, 0+6) = (4, 6).

## Exam Tips

1. **Remember the order of matrix multiplication**: When combining transformations M = T × S, the transformation on the right (S) is applied first. This is a common source of errors in exam problems.

2. **Homogeneous coordinates always use w = 1**: For 2D transformations, always use the third coordinate as 1 when representing points in homogeneous form.

3. **Fixed point scaling is a three-step process**: Always translate to origin, scale, then translate back when scaling about a point other than the origin.

4. **Negative scale factors cause reflection**: If sx or sy is negative, the object reflects across the corresponding axis. This is a frequently tested concept.

5. **Translation preserves shape and size**: Only the position changes; the object remains congruent to its original form.

6. **Matrix multiplication order matters**: Unlike translation, scaling is not commutative. The order S1 × S2 is generally different from S2 × S1.

7. **Draw the coordinate system**: For geometry-based questions, always sketch the original and transformed positions to verify your answer.

8. **Know the identity matrices**: T(tx, ty) with tx = ty = 0 gives the identity matrix; S(sx, sy) with sx = sy = 1 gives the identity matrix.

9. **Composite transformation matrix derivation**: For complex problems, derive the composite matrix step by step rather than memorizing formulas.

10. **Check your answers**: Verify that points transformed and then inverse-transformed return to original positions.
