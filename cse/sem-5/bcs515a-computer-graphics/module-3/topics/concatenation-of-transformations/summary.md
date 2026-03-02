# Concatenation of Transformations - Summary

## Key Definitions and Concepts

- **Concatenation (Composition)**: Combining multiple transformation matrices into a single matrix using matrix multiplication
- **Homogeneous Coordinates**: Representing n-dimensional points as (n+1)-dimensional vectors with last coordinate = 1
- **Composite Transformation Matrix**: A single matrix M that produces the same result as applying multiple transformations sequentially

## Important Formulas and Theorems

- **2D Translation**: T(tx, ty) = [[1, 0, tx], [0, 1, ty], [0, 0, 1]]
- **2D Rotation**: R(θ) = [[cosθ, -sinθ, 0], [sinθ, cosθ, 0], [0, 0, 1]]
- **2D Scaling**: S(sx, sy) = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
- **Fixed Point Rotation/Scaling**: M = T(px, py) × Transformation × T(-px, -py)
- **Order Rule**: In composite M = A × B, B is applied first, then A

## Key Points

- Matrix multiplication enables efficient composition of transformations
- Transformation order critically affects final results (non-commutative property)
- 4×4 matrices represent all 3D transformations in homogeneous coordinates
- Three-step process rotates/scales about arbitrary points: translate to origin → transform → translate back
- Composite transformations reduce per-vertex computation in rendering pipelines
- Inverse of composite M = A × B is M⁻¹ = B⁻¹ × A⁻¹ (reversed order)
- Common applications: camera matrices, hierarchical modeling, scene graphs, animation systems

## Common Mistakes to Avoid

- Applying transformations in wrong order—remember rightmost matrix in product applies first
- Forgetting homogeneous coordinate (w=1) when performing calculations
- Using 3×3 matrices for 3D transformations (should use 4×4)
- Ignoring the sign change in translation when computing inverse transformations

## Revision Tips

- Practice deriving composite matrices from transformation sequences
- Always verify matrix multiplication dimensions before computing
- Draw transformation sequences for fixed-point problems: translate pivot to origin first
- Memorize the standard transformation matrices for quick recall during exams
- Solve at least 3-4 composite transformation problems to reinforce the concept
