# Affine Transformations

## Introduction

Affine transformations are fundamental operations in computer graphics, image processing, and geometric modeling that preserve parallel lines and ratios of distances along lines. These transformations form the mathematical backbone of how computers manipulate and render graphical objects, making them essential knowledge for any computer science engineer studying computer graphics under the 2022 scheme.

In the context of computer graphics, affine transformations enable us to perform essential operations such as moving objects (translation), rotating them around a point, changing their size (scaling), and distorting their shapes (shearing). What makes these transformations particularly powerful is their ability to combine multiple simple transformations into a single composite transformation through matrix multiplication. This property significantly simplifies the implementation of complex graphical operations in software systems.

The significance of affine transformations extends beyond just visual effects. They are crucial in coordinate system conversions, camera transformations in 3D graphics, robotic kinematics, computer vision, and even in data augmentation for machine learning. Understanding the mathematical foundations of affine transformations prepares students to tackle advanced topics in computer graphics and related fields.

## Key Concepts

### Definition and Properties of Affine Transformations

An affine transformation is a geometric transformation that preserves collinearity (points on a line remain on a line) and ratios of distances along lines. Mathematically, a transformation T is affine if it can be expressed in the form:

**T(p) = Ap + b**

Where:

- **p** is a point represented as a column vector
- **A** is a linear transformation matrix
- **b** is a translation vector

The key properties of affine transformations include:

1. **Parallelism preservation**: Parallel lines remain parallel after transformation
2. **Ratio preservation**: The ratio of distances between points on a straight line is preserved
3. **Composition**: The composition of two affine transformations is also an affine transformation
4. **Inverse**: If an affine transformation is invertible, its inverse is also affine

### Homogeneous Coordinates

To represent translation as matrix multiplication (which is essential for combining transformations), we use homogeneous coordinates. In 2D, a point (x, y) is represented as (x, y, 1) in homogeneous coordinates. In 3D, a point (x, y, z) becomes (x, y, z, 1).

This representation allows all affine transformations to be expressed as 3×3 matrices in 2D and 4×4 matrices in 3D, enabling uniform treatment of all transformation types through matrix operations.

### Types of Affine Transformations

**1. Translation**

Translation moves every point of an object by the same amount in a given direction. In 2D, if we want to translate by (tx, ty), the transformation matrix is:

```
| 1 0 tx |
| 0 1 ty |
| 0 0 1 |
```

The transformed point (x', y') is calculated as:

- x' = x + tx
- y' = y + ty

**2. Rotation**

Rotation turns an object around a fixed point (usually the origin) by a specified angle θ. The 2D rotation matrix for rotating by angle θ (counterclockwise) is:

```
| cos(θ) -sin(θ) 0 |
| sin(θ) cos(θ) 0 |
| 0 0 1 |
```

The transformed coordinates are:

- x' = x cos(θ) - y sin(θ)
- y' = x sin(θ) + y cos(θ)

**3. Scaling**

Scaling changes the size of an object by multiplying coordinates by scaling factors. Non-uniform scaling uses different factors for x and y directions:

```
| sx 0 0 |
| 0 sy 0 |
| 0 0 1 |
```

Where sx and sy are scaling factors. If sx = sy, it's uniform scaling. If either factor is less than 1, it's shrinking; if greater than 1, it's enlargement.

**4. Shearing (Skewing)**

Shearing displaces each point in a direction parallel to one axis, proportional to its distance from another axis. The 2D shear transformation in x-direction is:

```
| 1 shx 0 |
| 0 1 0 |
| 0 0 1 |
```

The x-shearing formula: x' = x + shx × y, y' = y

Similarly, y-shearing: x' = x, y' = y + shy × x

### Composite Transformations

One of the most powerful aspects of affine transformations is that multiple transformations can be combined into a single matrix through multiplication. If we want to rotate an object and then translate it, we multiply the translation matrix by the rotation matrix.

**Important Note**: Matrix multiplication is generally not commutative, meaning the order of transformations matters significantly. If you translate then rotate, you get a different result than rotating then translating.

For transformations about an arbitrary point (not the origin), we use a three-step process:

1. Translate the arbitrary point to the origin
2. Perform the transformation (rotate, scale, etc.)
3. Translate back to the original position

### Reflection

Reflection is a transformation that produces a mirror image of an object. Common reflections include:

- Reflection about x-axis: (x, y) → (x, -y)
- Reflection about y-axis: (x, y) → (-x, y)
- Reflection about origin: (x, y) → (-x, -y)
- Reflection about line y = x: (x, y) → (y, x)

## Examples

### Example 1: Rotating a Triangle About Origin

**Problem**: A triangle has vertices at A(1, 1), B(3, 1), and C(2, 3). Rotate the triangle by 90° counterclockwise about the origin and find the new coordinates.

**Solution**:

For 90° counterclockwise rotation, θ = 90° = π/2 radians

Rotation matrix:

```
| cos(90°) -sin(90°) 0 | | 0 -1 0 |
| sin(90°) cos(90°) 0 | = | 1 0 0 |
| 0 0 1 | | 0 0 1 |
```

Transform each vertex:

**Point A(1, 1):**

- x' = 0(1) + (-1)(1) = -1
- y' = 1(1) + 0(1) = 1
- A' = (-1, 1)

**Point B(3, 1):**

- x' = 0(3) + (-1)(1) = -1
- y' = 1(3) + 0(1) = 3
- B' = (-1, 3)

**Point C(2, 3):**

- x' = 0(2) + (-1)(3) = -3
- y' = 1(2) + 0(3) = 2
- C' = (-3, 2)

**Answer**: The rotated triangle vertices are A'(-1, 1), B'(-1, 3), C'(-3, 2)

### Example 2: Composite Transformation - Scale Then Translate

**Problem**: A square with vertices (0, 0), (2, 0), (2, 2), (0, 2) is scaled by a factor of 2 about the origin, then translated by (3, 4). Find the final coordinates.

**Solution**:

**Step 1: Scaling by factor of 2**

Scale matrix (sx = 2, sy = 2):

```
| 2 0 0 |
| 0 2 0 |
| 0 0 1 |
```

Apply to each vertex:

- (0, 0) → (0, 0)
- (2, 0) → (4, 0)
- (2, 2) → (4, 4)
- (0, 2) → (0, 4)

**Step 2: Translation by (3, 4)**

Translation matrix:

```
| 1 0 3 |
| 0 1 4 |
| 0 0 1 |
```

Apply to scaled vertices:

- (0, 0) + (3, 4) = (3, 4)
- (4, 0) + (3, 4) = (7, 4)
- (4, 4) + (3, 4) = (7, 8)
- (0, 4) + (3, 4) = (3, 8)

**Composite Matrix Method**:
M = T × S =

```
| 1 0 3 | | 2 0 0 | | 2 0 3 |
| 0 1 4 | × | 0 2 0 | = | 0 2 4 |
| 0 0 1 | | 0 0 1 | | 0 0 1 |
```

**Answer**: Final coordinates are (3, 4), (7, 4), (7, 8), (3, 8)

### Example 3: Rotation About Arbitrary Point

**Problem**: Rotate point P(5, 5) by 45° about point Q(2, 2). Find the rotated point.

**Solution**:

**Step 1**: Translate Q to origin: P' = P - Q = (5-2, 5-2) = (3, 3)

**Step 2**: Rotate P' by 45° about origin
cos(45°) = sin(45°) = √2/2 ≈ 0.7071

Rotation matrix:

```
| 0.7071 -0.7071 0 |
| 0.7071 0.7071 0 |
| 0 0 1 |
```

Apply to (3, 3):

- x'' = 0.7071(3) - 0.7071(3) = 0
- y'' = 0.7071(3) + 0.7071(3) = 4.2426

P'' = (0, 4.2426)

**Step 3**: Translate back: P''' = P'' + Q = (0+2, 4.2426+2) = (2, 6.2426)

**Answer**: The rotated point is approximately (2, 6.24)

## Exam Tips

1. **Remember the homogeneous coordinate representation**: Always add '1' as the third coordinate in 2D transformations to enable matrix multiplication for translation.

2. **Matrix multiplication order matters**: In computer graphics, transformations are typically applied right-to-left in the matrix representation, but the composite matrix is written with the first transformation on the left.

3. **Standard transformation matrices**: Memorize the basic matrices for translation, rotation, scaling, and shearing - these are frequently asked in exams.

4. **Inverse transformations**: Know how to find inverse transformation matrices - translation is reversed by negative values, rotation by negative angle, scaling by reciprocal values.

5. **Order of composite transformations**: For rotation/scaling about arbitrary points, always translate to origin → transform → translate back.

6. **Clockwise vs Counterclockwise**: Remember that positive angles in the standard rotation matrix represent counterclockwise rotation; use negative angle for clockwise.

7. **Practice coordinate calculations**: Be thorough with the formula x' = x cos(θ) - y sin(θ), y' = x sin(θ) + y cos(θ) for rotation calculations.

8. **Homogeneous coordinates in 3D**: For exams, remember that 3D affine transformations use 4×4 matrices with homogeneous coordinate w = 1.
