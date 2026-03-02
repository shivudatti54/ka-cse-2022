# Transformation in Homogeneous Coordinates - Summary

## Key Definitions and Concepts

- **Homogeneous Coordinates**: A coordinate system that adds an extra dimension (w) to represent points, allowing all affine transformations to be expressed as matrix multiplications. For 2D: (x, y) → (x, y, 1); for 3D: (x, y, z) → (x, y, z, 1).

- **Affine Transformation**: A transformation that preserves parallel lines and ratios of distances along lines. Includes translation, scaling, rotation, and shearing.

- **Composite Transformation**: Combining multiple transformations into a single matrix by multiplying individual transformation matrices.

## Important Formulas and Theorems

**2D Translation Matrix:**

```
| 1   0   tx |
| 0   1   ty |
| 0   0   1  |
```

**2D Scaling Matrix:**

```
| sx  0   0 |
| 0   sy  0 |
| 0   0   1  |
```

**2D Rotation Matrix (angle θ):**

```
| cosθ  -sinθ  0 |
| sinθ   cosθ  0 |
|  0       0   1 |
```

**2D Shearing Matrix (x-direction):**

```
| 1   shx  0 |
| 0    1   0 |
| 0    0   1 |
```

## Key Points

- Homogeneous coordinates unify all affine transformations under matrix multiplication
- Transformation matrices for 2D are 3×3, for 3D are 4×4
- Matrix multiplication for transformations is not commutative—order matters
- Transformations apply right-to-left (matrix closest to point is applied first)
- To rotate/scale about arbitrary point P: T(P) × Transformation × T(-P)
- 3D rotation matrices differ for x, y, and z axes
- The identity matrix (1s on diagonal, 0s elsewhere) represents "no transformation"

## Common Mistakes to Avoid

1. Forgetting to add the extra coordinate '1' when representing points in homogeneous form
2. Applying transformations in wrong order—remember right-to-left application
3. Using degrees instead of radians in rotation matrices (use radians for calculation)
4. Confusing clockwise and counterclockwise rotation signs
5. Not normalizing the homogeneous coordinate after transformation (when w ≠ 1)

## Revision Tips

1. Practice writing each transformation matrix from memory until automatic
2. Work through at least 3-4 composite transformation problems before the exam
3. Remember: translation matrix has 1s on diagonal, rotation has cosθ and sinθ on diagonal and off-diagonal
4. For rotation about a point, always use the three-step approach: translate to origin, transform, translate back
5. In exams, show all matrix multiplication steps clearly for full marks
