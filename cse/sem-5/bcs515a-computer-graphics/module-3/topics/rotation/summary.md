# Rotation in Computer Graphics - Summary

## Key Definitions and Concepts

- **Rotation**: A transformation that rotates a point or object around a fixed point (origin or pivot) by a specified angle
- **Counter-clockwise rotation**: Positive angle rotation (standard direction)
- **Clockwise rotation**: Negative angle rotation
- **Pivot point**: The fixed point about which rotation occurs
- **Homogeneous coordinates**: 2D points represented as (x, y, 1) for matrix operations

## Important Formulas and Theorems

**Rotation about origin (counter-clockwise):**

- x' = x cosθ - y sinθ
- y' = x sinθ + y cosθ

**Rotation about origin (clockwise):**

- x' = x cosθ + y sinθ
- y' = -x sinθ + y cosθ

**Homogeneous rotation matrix (3×3):**

```
| cosθ  -sinθ  0 |
| sinθ   cosθ  0 |
|   0      0   1 |
```

**Rotation about arbitrary point (h, k):**

- Use three-step process: Translate to origin → Rotate → Translate back

## Key Points

- Rotation preserves shape and size of objects (rigid body transformation)
- Rotation preserves distances from the center of rotation
- Angle of rotation is measured in degrees or radians (radians for programming)
- Special angles: 90°, 180°, 270°, 360° have simple trigonometric values
- 360° rotation returns to original position
- Rotation matrix is orthogonal: R(θ)⁻¹ = R(-θ) = R(θ)ᵀ

## Common Mistakes to Avoid

1. **Wrong sign for clockwise rotation**: Using counter-clockwise formulas for clockwise rotation
2. **Forgetting to convert degrees to radians** when programming
3. **Incorrect matrix multiplication order** when composing transformations
4. **Ignoring pivot point** when rotation is about arbitrary point - always translate first

## Revision Tips

1. Practice 5-6 problems involving rotation of points and polygons about origin and arbitrary points
2. Memorize the standard rotation matrix structure
3. Remember the three-step process for arbitrary point rotation
4. Review special angle trigonometric values
5. Solve previous year exam questions on rotation transformations
6. Understand how rotation combines with translation and scaling through matrix multiplication
