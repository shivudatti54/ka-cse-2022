# Affine Transformations - Summary

## Key Definitions and Concepts

- **Affine Transformation**: A geometric transformation T(p) = Ap + b that preserves parallel lines and ratios of distances along lines.

- **Homogeneous Coordinates**: Extended coordinates (x, y, 1) in 2D and (x, y, z, 1) in 3D that enable all transformations to be represented as matrix multiplications.

- **Composite Transformation**: Combining multiple affine transformations into a single matrix through multiplication.

## Important Formulas and Theorems

**Translation**:

- Matrix: `|1 0 tx| |0 1 ty| |0 0 1|`
- Formula: x' = x + tx, y' = y + ty

**Rotation (θ counterclockwise)**:

- Matrix: `|cos(θ) -sin(θ) 0| |sin(θ) cos(θ) 0| |0 0 1|`
- Formula: x' = x cos(θ) - y sin(θ), y' = x sin(θ) + y cos(θ)

**Scaling (sx, sy)**:

- Matrix: `|sx 0 0| |0 sy 0| |0 0 1|`
- Formula: x' = sx × x, y' = sy × y

**Shearing**:

- x-shear: x' = x + shx × y
- y-shear: y' = y + shy × x

## Key Points

- Affine transformations preserve parallelism and ratios along straight lines
- All affine transformations can be represented as 3×3 matrices in 2D homogeneous coordinates
- Translation cannot be represented as a 2×2 matrix - requires homogeneous coordinates
- Matrix multiplication for composite transformations is not commutative (order matters)
- Rotation/scaling about arbitrary points requires: Translate to origin → Transform → Translate back
- Positive rotation angles are counterclockwise in standard coordinate systems
- The inverse of a transformation reverses its effect (negative parameters)

## Common Mistakes to Avoid

1. **Forgetting homogeneous coordinates**: Always add '1' as the third coordinate for 2D transformations; failing to do so gives incorrect results.

2. **Incorrect matrix multiplication order**: Transformations apply right-to-left - if you want to rotate then translate, multiply T × R.

3. **Confusing clockwise and counterclockwise**: Standard rotation matrix uses positive angles for counterclockwise rotation.

4. **Ignoring the origin**: When rotating or scaling about a point other than origin, always translate the point to origin first.

## Revision Tips

1. Practice deriving transformation matrices for each basic transformation type until you can write them from memory.

2. Work through at least 3-4 composite transformation problems to understand the importance of transformation order.

3. Remember that the last row of homogeneous transformation matrices is always (0, 0, 1) in 2D.

4. For exam questions, always verify if the transformation is about origin or arbitrary point - this changes the approach completely.
