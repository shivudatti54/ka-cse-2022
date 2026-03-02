# Translation and Scaling in 2D Computer Graphics - Summary

## Key Definitions and Concepts

- **Homogeneous Coordinates**: A coordinate system where a 2D point (x, y) is represented as (x, y, 1) in 3D space, enabling all transformations to be expressed as matrix multiplications.

- **Translation**: A rigid body transformation that moves every point of an object by the same amount (tx, ty) without changing its shape, size, or orientation.

- **Scaling**: A transformation that changes the size of an object by multiplying coordinates by scale factors (sx, sy); uniform scaling uses equal factors, non-uniform uses different factors.

- **Fixed Point Scaling**: Scaling about a point other than the origin by first translating the fixed point to origin, scaling, then translating back.

## Important Formulas and Theorems

**Translation Matrix:**

```
T(tx, ty) = | 1  0  tx |
            | 0  1  ty |
            | 0  0  1  |
```

**Scaling Matrix:**

```
S(sx, sy) = | sx 0  0 |
            | 0  sy 0 |
            | 0  0  1 |
```

**Scaling about Fixed Point (xf, yf):**
M = T(xf, yf) × S(sx, sy) × T(-xf, -yf)

**Translation of Point:**
x' = x + tx, y' = y + ty

**Scaling of Point:**
x' = x × sx, y' = y × sy

## Key Points

- Translation preserves parallelism, angles, and shape; only position changes
- Scaling by factors > 1 enlarges objects; factors between 0 and 1 shrink objects
- Negative scale factors cause reflection across axes
- Matrix multiplication applies transformations right-to-left: M = T × S means S first, then T
- Translation is commutative; scaling is generally not commutative
- Fixed point scaling keeps one point stationary while scaling everything relative to it
- Identity transformation: T(0, 0) = S(1, 1) = 3×3 identity matrix
- Composite transformations reduce multiple operations to a single matrix multiplication

## Common Mistakes to Avoid

1. **Wrong transformation order**: Applying transformations in incorrect sequence; remember right-to-left application
2. **Forgetting homogeneous coordinate**: Using [x, y] instead of [x, y, 1] for matrix operations
3. **Ignoring fixed point**: Scaling about origin when a fixed point is specified
4. **Negative scale confusion**: Not recognizing that negative sx or sy causes reflection
5. **Matrix multiplication errors**: Treating matrix multiplication as element-wise multiplication

## Revision Tips

1. Practice deriving transformation matrices for different scenarios until the process becomes automatic
2. Always verify composite matrices by applying them step-by-step to test points
3. Draw coordinate diagrams to visualize transformations before solving algebraically
4. Memorize the standard forms of translation and scaling matrices
5. Solve at least 5-10 problems on composite transformations to master the right-to-left application rule
