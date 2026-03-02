# Geometric Linear Transformations of R² - Summary

## Key Definitions and Concepts

- **Linear Transformation**: A mapping T: R² → R² satisfying T(u + v) = T(u) + T(v) and T(cu) = cT(u) for all vectors u, v and scalars c.

- **Standard Matrix**: For a linear transformation T, if T(e₁) = (a, c) and T(e₂) = (b, d), then the matrix is A = [[a, b], [c, d]].

- **Invertibility**: A linear transformation is invertible if and only if its matrix has non-zero determinant.

## Important Formulas and Matrices

| Transformation       | Matrix                            |
| -------------------- | --------------------------------- |
| Rotation by θ        | [[cos θ, -sin θ], [sin θ, cos θ]] |
| Scaling (a, b)       | [[a, 0], [0, b]]                  |
| Horizontal Shear (k) | [[1, k], [0, 1]]                  |
| Vertical Shear (k)   | [[1, 0], [k, 1]]                  |
| Reflection (x-axis)  | [[1, 0], [0, -1]]                 |
| Projection (x-axis)  | [[1, 0], [0, 0]]                  |

- **Inverse of 2×2 matrix**: A⁻¹ = (1/det) × [[d, -b], [-c, a]]

## Key Points

- All linear transformations map the origin to itself: T(0) = 0
- Rotation matrices are orthogonal with determinant 1
- Shear transformations preserve area (det = 1)
- Composition corresponds to matrix multiplication (rightmost applies first)
- The determinant indicates area scaling factor
- Projections and reflections are idempotent: P² = P, R² = I
- For any linear transformation, applying to basis vectors gives the matrix columns

## Common Mistakes to Avoid

1. **Wrong composition order**: Students often multiply matrices in the wrong order. Remember: to apply T₂ then T₁, use matrix A₁A₂ (left applies first when reading right-to-left).

2. **Forgetting to verify linearity**: Not all functions are linear. Always check T(0) = 0 as a necessary first test.

3. **Confusing determinant meaning**: A negative determinant indicates orientation reversal, not negative area.

4. **Incorrect inverse formula**: The adjugate formula has swapped positions of a and d, with sign changes on b and c.

## Revision Tips

1. Practice deriving transformation matrices from geometric descriptions by applying to e₁ and e₂.

2. Work through composition problems step-by-step, explicitly stating which transformation applies at each stage.

3. Create a quick reference card of standard transformation matrices for last-minute revision.

4. Solve at least 3-4 previous year university questions on this topic to understand the exam pattern and common question types.
