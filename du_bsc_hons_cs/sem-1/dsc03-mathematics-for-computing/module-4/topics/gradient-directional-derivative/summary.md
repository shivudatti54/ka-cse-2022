# Gradient and Directional Derivative - Summary

## Key Definitions and Concepts

- **Partial Derivative**: The derivative of f(x,y) with respect to one variable while holding the other constant. Notation: ∂f/∂x or fₓ.

- **Gradient (∇f)**: A vector pointing in the direction of maximum increase: ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z).

- **Directional Derivative (Dᵤf)**: The rate of change of f in the direction of unit vector u. Formula: Dᵤf = ∇f · u.

- **Unit Vector (u)**: A vector with magnitude 1, obtained by dividing direction vector by its magnitude.

## Important Formulas and Theorems

- **Gradient Definition**: ∇f = (∂f/∂x)i + (∂f/∂y)j + (∂f/∂z)k

- **Directional Derivative**: Dᵤf = (∂f/∂x)u₁ + (∂f/∂y)u₂ + (∂f/∂z)u₃

- **Relationship**: Dᵤf = ||∇f|| cos θ, where θ is angle between ∇f and u

- **Maximum Directional Derivative**: ||∇f|| (in direction of ∇f)

- **Minimum Directional Derivative**: -||∇f|| (opposite to ∇f)

- **Gradient Descent**: w_new = w_old - η∇L (for minimization)

## Key Points

- The gradient is always perpendicular to level curves/surfaces of the function.

- The gradient points in the direction of steepest increase; its magnitude equals the maximum rate of increase.

- A zero gradient (∇f = 0) indicates a critical point (potential local extremum).

- Directional derivative is maximum when direction aligns with gradient, zero when perpendicular.

- In machine learning, gradient descent uses negative gradient direction to find function minima.

- Always convert direction vectors to unit vectors before computing directional derivatives.

- The gradient provides information about both the direction and rate of change.

## Common Mistakes to Avoid

1. Forgetting to convert direction vector to unit vector when computing directional derivatives.

2. Confusing gradient (a vector) with directional derivative (a scalar).

3. Using addition instead of subtraction in gradient descent (moving toward maximum instead of minimum).

4. Computing partial derivatives incorrectly, especially with product or chain rule.

5. Assuming gradient zero always means maximum/minimum (it could be a saddle point).

## Revision Tips

1. Practice computing gradients for various polynomial, trigonometric, and exponential functions.

2. Memorize the relationship Dᵤf = ||∇f|| cos θ—it connects gradient magnitude to directional derivative.

3. Solve at least 5-6 problems on directional derivatives with different direction vectors.

4. Review the geometric interpretation: gradient is perpendicular to level curves.

5. Connect concepts to ML: understand why we use negative gradient in optimization.