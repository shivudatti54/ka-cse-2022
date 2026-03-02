# Transformation in Homogeneous Coordinates

## 1. Introduction: The Problem with Cartesian Coordinates

In computer graphics, we constantly manipulate objects in 2D and 3D space using transformations like translation (moving), rotation (turning), and scaling (resizing). While rotation and scaling can be neatly represented using matrix multiplication in standard Cartesian coordinates (x, y, z), translation presents a fundamental problem.

Consider a simple 2D translation:

- To move a point `P(x, y)` by `(tx, ty)`, the new point is `P'(x + tx, y + ty)`.
- This is an **additive** operation, not a multiplicative one like rotation or scaling.
- It is impossible to represent this translation as a matrix multiplication of a 2x2 matrix with the 2D vector `[x, y]^T`.

This inconsistency means we cannot easily combine (concatenate) multiple transformations (e.g., rotate, then scale, then translate) into a single, efficient operation. Homogeneous coordinates solve this elegantly.

## 2. What are Homogeneous Coordinates?

Homogeneous coordinates are a system of coordinates used in projective geometry that allows affine transformations (like translation) to be represented as linear transformations via matrix multiplication. The key idea is to **add an extra dimension**.

- For a 2D point `(x, y)`, its homogeneous representation is `(x, y, w)`, where `w` is a scalar (often called the homogeneous coordinate or weight).
- For a 3D point `(x, y, z)`, its homogeneous representation is `(x, y, z, w)`.

The Cartesian coordinates are recovered by dividing by `w`:
`(Cartesian_x, Cartesian_y) = (x/w, y/w)`
`(Cartesian_x, Cartesian_y, Cartesian_z) = (x/w, y/w, z/w)`

Typically, we use `w = 1` for points, as it simplifies the transformation matrices. A homogeneous point `(x, y, 1)` corresponds to the Cartesian point `(x, y)`.

```
Homogeneous Point (x, y, w)  -->  Cartesian Point (x/w, y/w)
        ^                             ^
        | (Set w=1)                   | (Divide by w)
        |                             |
Standard Cartesian (x, y)  <--  Homogeneous with w=1 (x, y, 1)
```

## 3. Transformation Matrices in Homogeneous Form

The power of homogeneous coordinates lies in representing all fundamental transformations as matrix multiplications.

### 3.1. 2D Translation

To translate a point `(x, y)` by `(tx, ty)`:

```
[ 1  0  tx ]   [x]   [x + tx]
[ 0  1  ty ] * [y] = [y + ty]
[ 0  0  1  ]   [1]   [   1  ]
```

The transformation matrix is:

```
T(tx, ty) = [ 1  0  tx ]
            [ 0  1  ty ]
            [ 0  0  1  ]
```

### 3.2. 2D Rotation

To rotate a point `(x, y)` by an angle `θ` counterclockwise around the origin:

```
[ cosθ  -sinθ  0 ]   [x]   [xcosθ - ysinθ]
[ sinθ   cosθ  0 ] * [y] = [xsinθ + ycosθ]
[  0      0    1 ]   [1]   [      1      ]
```

The transformation matrix is:

```
R(θ) = [ cosθ  -sinθ  0 ]
       [ sinθ   cosθ  0 ]
       [  0      0    1 ]
```

### 3.3. 2D Scaling

To scale a point `(x, y)` by factors `(sx, sy)` relative to the origin:

```
[ sx  0  0 ]   [x]   [sx * x]
[ 0  sy  0 ] * [y] = [sy * y]
[ 0  0  1 ]   [1]   [  1   ]
```

The transformation matrix is:

```
S(sx, sy) = [ sx  0  0 ]
            [ 0  sy  0 ]
            [ 0  0  1 ]
```

## 4. Concatenation of Transformations (Composition)

The primary advantage of homogeneous coordinates is that a sequence of transformations can be pre-multiplied (concatenated) into a single **composite transformation matrix**. This is incredibly efficient for computer graphics pipelines.

**Order matters!** Matrix multiplication is not commutative. `A * B ≠ B * A`.

**Example: Rotate a point around an arbitrary point P(h, k), not the origin.**
The sequence is:

1.  **Translate** by `(-h, -k)` to move point P to the origin.
2.  **Rotate** by the desired angle `θ`.
3.  **Translate** back by `(h, k)` to move the pivot back to its original position.

The composite matrix `M` is calculated as:
`M = T(h, k) * R(θ) * T(-h, -k)`

This single matrix `M` can then be applied to every vertex of the object, which is far more efficient than applying three separate transformations per vertex.

```
+----------------+      +-------------+      +----------------+      +-------------+
| Original Object|----->| Translate   |----->| Rotate around  |----->| Translate   |-----> Final
| centered at P  |      | P to Origin |      | Origin (θ)     |      | Back to P  |      Transformed
+----------------+      +-------------+      +-------------+      +----------------+      Object
                          T(-h, -k)            R(θ)                 T(h, k)
```

## 5. 3D Transformations in Homogeneous Coordinates

The concept extends naturally to 3D. Points are now represented as `(x, y, z, w)`, and transformation matrices are 4x4.

### 5.1. 3D Translation

```
T(tx, ty, tz) = [ 1  0  0  tx ]
                 [ 0  1  0  ty ]
                 [ 0  0  1  tz ]
                 [ 0  0  0  1  ]
```

### 5.2. 3D Scaling

```
S(sx, sy, sz) = [ sx  0  0  0 ]
                 [ 0  sy  0  0 ]
                 [ 0  0  sz  0 ]
                 [ 0  0  0  1  ]
```

### 5.3. 3D Rotation

Rotation is more complex in 3D as we must define an axis of rotation.

**Rotation around the z-axis ( analogous to 2D rotation):**

```
Rz(θ) = [ cosθ  -sinθ  0  0 ]
        [ sinθ   cosθ  0  0 ]
        [  0      0    1  0 ]
        [  0      0    0  1 ]
```

**Rotation around the x-axis:**

```
Rx(θ) = [ 1    0     0    0 ]
        [ 0  cosθ  -sinθ  0 ]
        [ 0  sinθ   cosθ  0 ]
        [ 0    0     0    1 ]
```

**Rotation around the y-axis:**

```
Ry(θ) = [  cosθ   0   sinθ  0 ]
        [   0     1    0    0 ]
        [ -sinθ   0   cosθ  0 ]
        [   0     0    0    1 ]
```

## 6. Implementation in OpenGL

OpenGL and WebGL are built around the use of 4x4 transformation matrices in homogeneous coordinates. The graphics pipeline is designed to apply these matrices to every vertex of a model.

- The **Model-View matrix** combines all modeling transformations (translation, rotation, scaling of an object) and viewing transformations (positioning the camera).
- The **Projection matrix** applies perspective or orthographic projection to map the 3D scene onto a 2D viewport.

These matrices are stored and manipulated in the pipeline, allowing for extremely fast rendering of complex scenes.

**Table: Comparison of Transformation Representations**
| Transformation | Cartesian Form | Homogeneous Matrix Form (2D) | Homogeneous Matrix Form (3D) |
| :--- | :--- | :--- | :--- |
| **Translation** | `(x+tx, y+ty)` | `T(tx,ty) = [[1,0,tx],[0,1,ty],[0,0,1]]` | `T(tx,ty,tz) = [[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]` |
| **Rotation** | `(xcosθ-ysinθ, xsinθ+ycosθ)` | `R(θ) = [[cosθ,-sinθ,0],[sinθ,cosθ,0],[0,0,1]]` | `Rz(θ) = [[cosθ,-sinθ,0,0],[sinθ,cosθ,0,0],[0,0,1,0],[0,0,0,1]]` |
| **Scaling** | `(sx*x, sy*y)` | `S(sx,sy) = [[sx,0,0],[0,sy,0],[0,0,1]]` | `S(sx,sy,sz) = [[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]` |
| **Concatenation** | Sequential operations | Single matrix multiplication `M = T * R * S` | Single matrix multiplication `M = T * R * S` |

## 7. Exam Tips

1.  **Remember the `w` component:** Always remember that a point in homogeneous coordinates is `(x, y, w)`. For transformations, using `w=1` is standard. The final Cartesian coordinate is always `(x/w, y/w)`.
2.  **Order of Operations:** Matrix multiplication is applied from right to left. The transformation closest to the point vector is applied first. For a sequence "A then B", the matrix is `B * A`.
3.  **Write the Matrices Clearly:** In exams, always write out the full 3x3 or 4x4 matrix. This helps avoid simple arithmetic errors and shows the examiner you understand the structure.
4.  **Practice Composite Transforms:** Be very comfortable deriving the composite matrix for a sequence like "scale, then rotate, then translate" or "rotate around a fixed point".
5.  **Understand the "Why":** Be prepared to explain why homogeneous coordinates are necessary (to represent translation as matrix multiplication for efficient concatenation).
