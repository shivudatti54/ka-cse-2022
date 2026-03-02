# Rotation in Computer Graphics

## Introduction

Rotation is one of the fundamental geometric transformations in computer graphics that rotates a point or object around a fixed point (origin) or a specified pivot point by a certain angle. This transformation is essential in computer graphics for creating animations, rotating objects, and performing complex geometric operations. In the context of 's Computer Graphics curriculum (subject: Computer Graphics, Module 3), rotation transformation is crucial for understanding how objects can be manipulated in 2D space.

The rotation transformation is particularly important in applications like computer-aided design (CAD), gaming, animation, and simulation. Understanding the mathematical foundations of rotation is essential for graphics programmers and developers. The transformation preserves the shape and size of the object while changing its orientation in the 2D plane. Rotation can be performed in two directions: clockwise (negative angle) or counter-clockwise (positive angle), and the angle of rotation is measured in degrees or radians.

## Key Concepts

### Basic Rotation about Origin

When rotating a point P(x, y) counter-clockwise by an angle θ about the origin, the new coordinates P'(x', y') are obtained using the following transformation equations:

**x' = x cos θ - y sin θ**
**y' = x sin θ + y cos θ**

This can also be represented in matrix form as a 3×3 homogeneous transformation matrix:

```
| cosθ -sinθ 0 |
| sinθ cosθ 0 |
| 0 0 1 |
```

### Clockwise Rotation

For clockwise rotation (negative angle), the transformation equations become:

**x' = x cos θ + y sin θ**
**y' = -x sin θ + y cos θ**

This is equivalent to rotating counter-clockwise by -θ.

### Rotation about an Arbitrary Point (Pivot Point)

When rotating about a point P(h, k) other than the origin, the transformation involves three steps:

1. Translate the pivot point to origin (subtract h from x and k from y)
2. Rotate about the origin using the standard rotation equations
3. Translate back (add h to x and k from y)

The combined transformation matrix for rotation about pivot point (h, k) by angle θ:

```
| cosθ -sinθ h(1-cosθ) + k sinθ |
| sinθ cosθ k(1-cosθ) - h sinθ |
| 0 0 1 |
```

### Homogeneous Coordinates

In computer graphics, homogeneous coordinates are used to represent 2D points in a 3-dimensional space. A 2D point (x, y) is represented as (x, y, 1) in homogeneous coordinates. This allows all affine transformations (translation, rotation, scaling, shearing) to be represented as matrix multiplications, enabling efficient composition of multiple transformations.

### Properties of Rotation

1. **Orientation preservation**: Rotation preserves the handedness of the coordinate system (counter-clockwise is positive)
2. **Distance preservation**: The distance from the origin remains unchanged
3. **Angle preservation**: Angles between lines are preserved
4. **Commutativity**: Rotation is commutative only when rotating about the same point
5. **Inverse**: The inverse of a rotation by angle θ is rotation by angle -θ (or 360° - θ)

## Examples

### Example 1: Rotation of a Point about Origin

**Problem**: Rotate point P(3, 4) by 90° counter-clockwise about the origin.

**Solution**:

Given: x = 3, y = 4, θ = 90°

Since cos 90° = 0 and sin 90° = 1:

x' = x cos θ - y sin θ = 3(0) - 4(1) = -4
y' = x sin θ + y cos θ = 3(1) + 4(0) = 3

Therefore, the rotated point is P'(-4, 3)

**Verification**: This matches the geometric intuition - a 90° counter-clockwise rotation moves the point from (3, 4) to (-4, 3).

### Example 2: Rotation of a Triangle

**Problem**: Rotate triangle with vertices A(1, 1), B(4, 1), C(1, 3) by 45° clockwise about origin.

**Solution**:

For clockwise rotation, we use θ = -45° (or equivalently, 315°)
cos 45° = sin 45° = √2/2 ≈ 0.7071

Using clockwise rotation formulas:
x' = x cos θ + y sin θ
y' = -x sin θ + y cos θ

**Vertex A(1, 1):**
x' = 1(0.7071) + 1(0.7071) = 1.4142
y' = -1(0.7071) + 1(0.7071) = 0

**Vertex B(4, 1):**
x' = 4(0.7071) + 1(0.7071) = 3.5355
y' = -4(0.7071) + 1(0.7071) = -2.1213

**Vertex C(1, 3):**
x' = 1(0.7071) + 3(0.7071) = 2.8284
y' = -1(0.7071) + 3(0.7071) = 1.4142

Rotated triangle vertices: A'(1.41, 0), B'(3.54, -2.12), C'(2.83, 1.41)

### Example 3: Rotation about Arbitrary Point

**Problem**: Rotate point P(5, 5) by 60° counter-clockwise about pivot point (2, 2).

**Solution**:

Given: x = 5, y = 5, h = 2, k = 2, θ = 60°
cos 60° = 0.5, sin 60° = 0.866

Using the formula for rotation about pivot point:
x' = x cosθ - y sinθ + h(1-cosθ) + k sinθ
y' = x sinθ + y cosθ + k(1-cosθ) - h sinθ

x' = 5(0.5) - 5(0.866) + 2(1-0.5) + 2(0.866)
x' = 2.5 - 4.33 + 1 + 1.732 = 0.902

y' = 5(0.866) + 5(0.5) + 2(1-0.5) - 2(0.866)
y' = 4.33 + 2.5 + 1 - 1.732 = 6.098

Rotated point: P'(0.902, 6.098)

## Exam Tips

1. **Remember the standard rotation matrix**: For counter-clockwise rotation by θ, the matrix is [[cosθ, -sinθ], [sinθ, cosθ]] - this is frequently asked in exams.

2. **Homogeneous coordinate representation**: Always express transformations in 3×3 matrix form for homogeneous coordinates as this is the standard approach in computer graphics.

3. **Angle conventions**: Counter-clockwise is positive, clockwise is negative. Remember this distinction clearly.

4. **Rotation about arbitrary point**: For rotation about a point other than origin, always use the three-step approach: translate to origin, rotate, translate back.

5. **Special angles**: Memorize sin and cos values for common angles (0°, 30°, 45°, 60°, 90°, 180°, 270°, 360°) as they frequently appear in exam problems.

6. **Matrix multiplication order**: When composing multiple transformations, remember that the transformation closest to the point is applied first. In matrix form, pre-multiplication is used.

7. **Inverse rotation**: The inverse of rotation by angle θ is rotation by -θ. This property is useful for solving reverse transformation problems.

8. **Practice coordinate computation**: Most exam questions require computing new coordinates after rotation. Practice both the equation method and matrix method.
