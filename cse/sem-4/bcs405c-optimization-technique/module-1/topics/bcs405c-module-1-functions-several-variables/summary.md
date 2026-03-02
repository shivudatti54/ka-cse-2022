# Functions of Several Variables - Summary

## Key Definitions and Concepts

- **Partial Derivative**: Rate of change of f(x,y) with respect to one variable, holding others constant: ∂f/∂x = lim[h→0] (f(x+h,y) - f(x,y))/h

- **Gradient Vector**: ∇f = (∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ) — points in direction of steepest ascent

- **Directional Derivative**: D_u f = ∇f · u, where u is a unit vector in the desired direction

- **Jacobian Matrix**: Matrix of all first-order partial derivatives for vector-valued functions

- **Hessian Matrix**: Matrix of all second-order partial derivatives; symmetric when continuous

- **Critical Point**: Point where ∇f = 0 or ∇f doesn't exist

- **Saddle Point**: Point that is a minimum in one direction and maximum in another

## Important Formulas and Theorems

- **Clairaut's Theorem**: fₓᵧ = fᵧₓ when partial derivatives are continuous

- **Hessian Test (2 variables)**:
- Δ = fₓₓfᵧᵧ - (fₓᵧ)²
- Δ > 0 and fₓₓ > 0: Local minimum
- Δ > 0 and fₓₓ < 0: Local maximum
- Δ < 0: Saddle point
- Δ = 0: Inconclusive

- **Taylor's Expansion (quadratic approximation)**:
  f(a+h,b+k) ≈ f(a,b) + hf_x + kf_y + ½(h²f_xx + 2hkf_xy + k²f_yy)

- **Lagrange Multipliers**: ∇f = λ∇g for constraint g(x,y,z) = 0

## Key Points

- The gradient is always perpendicular to level curves/surfaces of f

- The magnitude of the gradient equals the maximum rate of change

- For continuous functions on closed bounded domains, global extrema exist at critical points or boundaries

- The Hessian determines local curvature — positive definite means local minimum, negative definite means local maximum

- Directional derivative in gradient direction equals gradient magnitude; in opposite direction equals negative gradient magnitude

- The Jacobian determinant represents the scaling factor for coordinate transformations

## Common Mistakes to Avoid

- Forgetting to normalize direction vectors when computing directional derivatives — always use unit vectors

- Confusing local and global extrema — local tests don't guarantee global behavior

- Incorrectly computing mixed partials — apply Clairaut's theorem to simplify when possible

- Neglecting boundary analysis when finding global extrema on closed domains

## Revision Tips

- Practice finding critical points by solving systems of ∂f/∂xᵢ = 0 equations

- Memorize the Hessian classification test for two variables — it's frequently tested

- Visualize gradient as pointing uphill and perpendicular to level curves

- Work through at least 5-6 problems classifying critical points to build confidence

- Remember: ∇f = 0 is necessary but not sufficient for local extrema (saddle points also satisfy this)
