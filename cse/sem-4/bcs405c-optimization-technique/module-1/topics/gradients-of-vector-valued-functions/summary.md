# Gradients of Vector-Valued Functions - Summary

## Key Definitions and Concepts

- **Vector-valued function**: A function f: ℝⁿ → ℝᵐ that maps n-dimensional input to m-dimensional output, written as f(x) = [f₁(x), f₂(x), ..., fₘ(x)]ᵀ where each fᵢ is a scalar component function.

- **Jacobian matrix**: The m×n matrix J(f) containing all first-order partial derivatives: Jᵢⱼ = ∂fᵢ/∂xⱼ. Represents the best linear approximation of f at a point.

- **Gradient**: For scalar function f: ℝⁿ → ℝ, the gradient ∇f is an n-dimensional column vector of partial derivatives: ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ. Note: ∇f = Jᵀ.

- **Hessian matrix**: The n×n matrix of second-order partial derivatives for scalar functions: Hᵢⱼ = ∂²f/∂xᵢ∂xⱼ. Symmetric if partial derivatives are continuous.

- **Directional derivative**: Dᵤf(x) = lim(h→0) [f(x + hu) - f(x)]/h = ∇f(x) · u, where u is a unit vector.

## Important Formulas and Theorems

1. **Jacobian definition**: J(f)(x) = ∂f/∂x ∈ ℝᵐˣⁿ

2. **Chain rule**: If h(x) = g(f(x)), then J(h)(x) = J(g)(f(x)) · J(f)(x)

3. **Gradient descent update**: xₖ₊₁ = xₖ - α∇f(xₖ), where α is learning rate

4. **Newton's method**: xₖ₊₁ = xₖ - [H(xₖ)]⁻¹∇f(xₖ)

5. **Directional derivative**: Dᵤf = ∇f · u

## Key Points

- The Jacobian generalizes the derivative to vector-valued functions; for scalar functions, it reduces to the gradient (transposed)

- The gradient points in the direction of steepest ascent; for descent, move in the negative gradient direction

- Chain rule for vector-valued functions involves matrix multiplication of Jacobians, not element-wise products

- The Hessian captures curvature information and determines convergence rates of optimization algorithms

- For unconstrained optimization, ∇f(x\*) = 0 is a necessary condition for local optima (first-order condition)

- Positive definiteness of Hessian at a critical point ensures a local minimum (second-order sufficient condition)

- Jacobian-vector products can be computed efficiently without forming the full Jacobian matrix

## Common Mistakes to Avoid

1. **Confusing Jacobian orientation**: Students often write the Jacobian with variables in rows and outputs in columns; it should be outputs (rows) × inputs (columns)

2. **Forgetting the transpose**: For scalar functions, gradient = Jacobian transpose; don't forget this relationship

3. **Incorrect chain rule application**: The order matters—J(g) is evaluated at f(x), then multiplied by J(f)

4. **Dimension mismatches**: Always verify matrix dimensions are compatible for multiplication (inner dimensions must match)

## Revision Tips

1. Practice computing Jacobians for various function types: polynomial, trigonometric, exponential combinations

2. Derive the gradient for simple functions like f(x) = xᵀAx + bᵀx + c to understand matrix calculus

3. Implement gradient descent on simple 2D quadratic functions to build intuition

4. Review the chain rule through composition examples before the exam

5. Remember that symmetry of the Hessian is guaranteed when second partial derivatives are continuous
