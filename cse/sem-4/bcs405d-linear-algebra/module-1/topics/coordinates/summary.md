# Coordinates in Linear Algebra - Summary

## Key Definitions and Concepts

- **Ordered Basis**: A basis with vectors arranged in a specific sequence; each vector gets a unique position.
- **Coordinate Vector**: For v = c₁v₁ + c₂v₂ + ... + cₙvₙ relative to basis B = {v₁, v₂, ..., vₙ}, the coordinate vector is [v]ᵦ = [c₁, c₂, ..., cₙ]ᵀ.
- **Transition Matrix**: Matrix P where columns are coordinates of new basis vectors relative to old basis; transforms coordinates from old basis to new basis.
- **Change of Basis**: The process of converting vector coordinates between different bases.

## Important Formulas and Theorems

- **Coordinate transformation**: [v]ᵦ' = P[v]ᵦ (where P is transition matrix from B to B')
- **Inverse transformation**: [v]ᵦ = P⁻¹[v]ᵦ'
- **Polar to Cartesian**: x = r cos θ, y = r sin θ
- **Cartesian to Polar**: r = √(x² + y²), θ = arctan(y/x)
- **Transition matrix inverse**: If P transforms from B to B', then P⁻¹ transforms from B' to B

## Key Points

- Coordinates are unique for each vector given a specific basis
- In ℝⁿ with standard basis, coordinates equal the vector components
- Transition matrix columns are the coordinates of new basis vectors in old basis
- The determinant of a transition matrix is never zero (it's invertible)
- Linear transformation matrix changes with change of basis: [T]ᵦ' = P⁻¹AP
- Polar coordinates use (r, θ) where r ≥ 0 and 0 ≤ θ < 2π

## Common Mistakes to Avoid

1. Confusing the direction of transformation - always check whether P converts from B to B' or vice versa
2. Forgetting that coordinate vectors are column vectors (column matrices)
3. Not verifying answers by reconstructing the original vector
4. Incorrectly setting up the transition matrix - columns vs rows matters
5. Using degrees instead of radians in trigonometric calculations

## Revision Tips

1. Practice finding coordinates by solving systems of linear equations
2. Memorize the pattern: transition matrix columns = new basis vectors in old coordinates
3. Always invert the matrix when converting in the opposite direction
4. Work through at least 3-4 problems on change of basis to build confidence
5. Remember that verification catches most calculation errors
