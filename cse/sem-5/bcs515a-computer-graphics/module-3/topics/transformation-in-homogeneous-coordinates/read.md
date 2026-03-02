# Transformation in Homogeneous Coordinates

## Introduction

Transformation in homogeneous coordinates is a fundamental concept in computer graphics that provides a unified and efficient way to represent and compute geometric transformations. In computer graphics, we frequently need to perform operations such as translation, rotation, scaling, and shearing on graphical objects. While these transformations can be represented using separate mathematical forms, homogeneous coordinates allow us to express all affine transformations as matrix multiplications, significantly simplifying the computational pipeline.

The concept of homogeneous coordinates extends a 2D point (x, y) to a 3D representation (x, y, 1) by adding a third coordinate. Similarly, 3D points (x, y, z) become 4D points (x, y, z, 1). This seemingly simple addition of an extra coordinate enables us to combine multiple transformations into a single composite transformation matrix. This unified approach is crucial for rendering pipelines in graphics systems, CAD applications, animation systems, and robotic transformations.

The importance of homogeneous coordinates in 's Computer Graphics curriculum cannot be overstated. It forms the backbone of understanding how graphical objects are manipulated in virtual space, and questions from this topic frequently appear in university examinations. Mastery of this topic enables students to understand the mathematical foundations behind graphics libraries like OpenGL and DirectX, where transformation matrices are extensively used.

## Key Concepts

### 1. Homogeneous Coordinates: The Foundation

In Euclidean coordinates, a 2D point is represented as P(x, y). The same point in homogeneous coordinates is represented as P̄(x̄, ȳ, w), where x = x̄/w and y = ȳ/w. For practical graphics applications, we typically set w = 1, giving us P̄(x, y, 1). This representation allows us to perform translation using matrix multiplication, which was not possible with standard coordinate representation.

The transformation from Cartesian to homogeneous coordinates involves adding a third coordinate. For a 2D point (x, y), the homogeneous representation is (x_h, y_h, w) where x = x_h/w and y = y_h/w. When w ≠ 0, we can always normalize to get (x, y, 1). This mathematical trick transforms translation from addition to matrix multiplication, unifying all affine transformations.

### 2. Basic 2D Transformation Matrices

**Translation**: Moving a point from (x, y) to (x + tx, y + ty) is represented by the translation matrix:

```
| 1 0 tx |
| 0 1 ty |
| 0 0 1 |
```

The translation matrix is a 3×3 matrix that, when multiplied with the homogeneous coordinate vector [x, y, 1]ᵀ, produces [x + tx, y + ty, 1]ᵀ.

**Scaling**: Changing the size of an object is achieved through scaling. Uniform scaling (same factor in both directions) uses:

```
| sx 0 0 |
| 0 sy 0 |
| 0 0 1 |
```

For scaling about the origin, the transformation is [sx·x, sy·y, 1]. For scaling about an arbitrary point, we need to translate to origin, scale, then translate back.

**Rotation**: Rotating a point by angle θ about the origin follows the matrix:

```
| cosθ -sinθ 0 |
| sinθ cosθ 0 |
| 0 0 1 |
```

This matrix rotates points counterclockwise by θ degrees. For clockwise rotation, use -θ in the matrix.

**Shearing**: Shearing distorts the shape of an object. The shear matrix in x-direction with parameter shx is:

```
| 1 shx 0 |
| 0 1 0 |
| 0 0 1 |
```

This transforms (x, y) to (x + shx·y, y). Similarly, y-direction shear uses:

```
| 1 0 0 |
| shy 1 0 |
| 0 0 1 |
```

### 3. 3D Transformation Matrices

Extending homogeneous coordinates to 3D gives us 4×4 transformation matrices. The 3D translation matrix is:

```
| 1 0 0 tx |
| 0 1 0 ty |
| 0 0 1 tz |
| 0 0 0 1 |
```

3D scaling uses a similar 4×4 matrix with sx, sy, sz scaling factors along the diagonal. 3D rotation becomes more complex with rotations possible about x, y, and z axes. Rotation about the z-axis uses the 2D rotation matrix extended to 4×4:

```
| cosθ -sinθ 0 0 |
| sinθ cosθ 0 0 |
| 0 0 1 0 |
| 0 0 0 1 |
```

Rotation about the x-axis (by angle θ) is:

```
| 1 0 0 0 |
| 0 cosθ -sinθ 0 |
| 0 sinθ cosθ 0 |
| 0 0 0 1 |
```

Rotation about the y-axis is:

```
| cosθ 0 sinθ 0 |
| 0 1 0 0 |
| -sinθ 0 cosθ 0 |
| 0 0 0 1 |
```

### 4. Composite Transformations

The true power of homogeneous coordinates lies in composite transformations. Since all transformations are represented as matrices, we can multiply them together to create a single transformation matrix. If we want to rotate an object about a specific point (not the origin), we can compose: translate to origin, rotate, then translate back.

For example, rotating a point about pivot (px, py) by angle θ:

1. Translate by (-px, -py) to move pivot to origin
2. Apply rotation matrix
3. Translate back by (px, py)

The composite matrix is: T(px, py) × R(θ) × T(-px, -py)

Matrix multiplication is generally not commutative, meaning the order of transformations matters. In computer graphics, transformations are typically applied right-to-left relative to the written order—the rightmost matrix is applied first.

### 5. Transformation Pipeline

In graphics systems, objects undergo a series of transformations: Model transformation (positioning in world space), View transformation (camera positioning), Projection transformation (3D to 2D), and Viewport transformation (screen mapping). Each stage uses homogeneous coordinate transformation matrices, making this concept essential for understanding the entire graphics pipeline.

## Examples

### Example 1: Translating a Triangle

**Problem**: A triangle has vertices A(2, 3), B(5, 3), C(3, 6). Translate it by tx = 3 and ty = -2 using homogeneous coordinates.

**Solution**:

Step 1: Represent vertices in homogeneous coordinates:

- A: [2, 3, 1]ᵀ
- B: [5, 3, 1]ᵀ
- C: [3, 6, 1]ᵀ

Step 2: Write the translation matrix:

```
T = | 1 0 3 |
 | 0 1 -2 |
 | 0 0 1 |
```

Step 3: Multiply each vertex:

For A: T × A = |1 0 3| × |2| = |1(2) + 0(3) + 3(1)| = |5|
|0 1 -2| |3| |0(2) + 1(3) + (-2)(1)| |1|
|0 0 1| |1| |0(2) + 0(3) + 1(1)| |1|

New A' = (5, 1)

For B: T × B = |1 0 3| × |5| = |8|
|0 1 -2| |3| |1|
|0 0 1| |1| |1|

New B' = (8, 1)

For C: T × C = |1 0 3| × |3| = |6|
|0 1 -2| |6| |4|
|0 0 1| |1| |1|

New C' = (6, 4)

**Answer**: Translated triangle vertices are A'(5, 1), B'(8, 1), C'(6, 4)

### Example 2: Rotation About a Point

**Problem**: Rotate point P(4, 3) by 90° counterclockwise about pivot point (1, 1).

**Solution**:

Step 1: Translate pivot to origin: T₁ = |1 0 -1|
|0 1 -1|
|0 0 1|

Step 2: Rotate 90° (θ = 90°): R = |0 -1 0|
|1 0 0|
|0 0 1|

Step 3: Translate back: T₂ = |1 0 1|
|0 1 1|
|0 0 1|

Step 4: Composite matrix M = T₂ × R × T₁

First, compute R × T₁:
R × T₁ = |0 -1 0| × |1 0 -1| = |0 -1 1|
|1 0 0| |0 1 -1| |1 0 -1|
|0 0 1| |0 0 1| |0 0 1|

Now compute T₂ × (R × T₁):
M = |1 0 1| × |0 -1 1| = |0 -1 2|
|0 1 1| |1 0 -1| |1 0 0|
|0 0 1| |0 0 1| |0 0 1|

Step 5: Apply to point P: P = [4, 3, 1]ᵀ
M × P = |0 -1 2| × |4| = |0(4) + (-1)(3) + 2(1)| = |-1|
|1 0 0| |3| |1(4) + 0(3) + 0(1)| |4|
|0 0 1| |1| |0(4) + 0(3) + 1(1)| |1|

**Answer**: Rotated point is P'(-1, 4)

### Example 3: Composite Transformation

**Problem**: A square with vertices (1,1), (2,1), (2,2), (1,2) is scaled by 2, then rotated by 45° about origin. Find the final coordinates.

**Solution**:

Step 1: Scaling matrix (sx = sy = 2):
S = |2 0 0|
|0 2 0|
|0 0 1|

Step 2: Rotation matrix (θ = 45°):
R = |cos45° -sin45° 0| = |0.707 -0.707 0|
|sin45° cos45° 0| |0.707 0.707 0|
| 0 0 1| | 0 0 1|

Step 3: Composite matrix M = R × S (rotation applied after scaling):
M = |0.707 -0.707 0| × |2 0 0|
|0.707 0.707 0| |0 2 0|
| 0 0 1| |0 0 1|

M = |0.707×2 -0.707×2 0| = |1.414 -1.414 0|
|0.707×2 0.707×2 0| |1.414 1.414 0|
| 0 0 1| | 0 0 1|

Step 4: Apply to each vertex:

For (1,1): M × [1,1,1]ᵀ = [1.414-1.414+0, 1.414+1.414+0, 1] = [0, 2.828, 1]
→ (0, 2.828)

For (2,1): M × [2,1,1]ᵀ = [2.828-0.707, 2.828+0.707, 1] = [2.121, 3.535, 1]
→ (2.121, 3.535)

For (2,2): M × [2,2,1]ᵀ = [2.828-1.414, 2.828+1.414, 1] = [1.414, 4.242, 1]
→ (1.414, 4.242)

For (1,2): M × [1,2,1]ᵀ = [0.707-1.414, 0.707+1.414, 1] = [-0.707, 2.121, 1]
→ (-0.707, 2.121)

**Answer**: Final vertices are (0, 2.828), (2.121, 3.535), (1.414, 4.242), (-0.707, 2.121)

## Exam Tips

1. **Remember the homogeneous coordinate format**: Always add '1' as the third coordinate for 2D points and fourth coordinate for 3D points.

2. **Matrix multiplication order matters**: Transformations are applied right-to-left. If the sequence is "translate then rotate," the matrix is R × T.

3. **Translation matrix identity**: The 3×3 translation matrix always has 1s on the diagonal and translation values in the last column.

4. **Rotation about arbitrary point**: Always translate the pivot to origin, rotate, then translate back—the three-matrix approach is essential.

5. **Know all standard matrices**: Memorize translation, scaling, rotation (both axes), and shear matrices as they frequently appear in exam questions.

6. **Check your matrix dimensions**: 2D transformations use 3×3 matrices, 3D transformations use 4×4 matrices.

7. **Verify results**: After computing, check if the transformation makes sense—rotating 90° should exchange coordinates, scaling by 2 should double coordinates.

8. **Composite matrix computation**: For efficiency, remember that you can compute the final matrix first, then multiply by all points—don't multiply each point by each transformation separately.
