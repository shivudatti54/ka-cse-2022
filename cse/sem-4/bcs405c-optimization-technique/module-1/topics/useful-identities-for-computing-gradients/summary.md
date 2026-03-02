# Useful Identities for Computing Gradients - Summary

## Key Definitions and Concepts

- **Gradient (∇f)**: The vector of first-order partial derivatives of a scalar function f(x) with respect to x = [x₁, x₂, ..., xₙ]ᵀ, pointing in the direction of steepest ascent.

- **Jacobian Matrix**: Matrix of first-order partial derivatives for vector-valued functions F: ℝⁿ → ℝᵐ.

- **Hessian Matrix (∇²f)**: Matrix of second-order partial derivatives, symmetric for continuously differentiable functions.

- **Directional Derivative (Dₐf)**: Rate of change of f in direction a, given by ∇f · a.

## Important Formulas and Theorems

- **Gradient definition**: ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ
- **Product rule**: ∇(fg) = f∇g + g∇f
- **Chain rule**: ∇ₓf(g(x)) = f'(u) · ∇ₓu
- **Quadratic form**: ∇(xᵀAx) = (A + Aᵀ)x = 2Ax (when A is symmetric)
- **Norm gradient**: ∇(‖x‖²) = 2x, ∇(‖x‖) = x/‖x‖
- **Linear term**: ∇(cᵀx) = c
- **Directional derivative**: Dₐf = ∇f · a

## Key Points

- Gradients point in the direction of maximum increase; the negative gradient indicates the direction of steepest descent.

- For quadratic functions f(x) = xᵀQx + cᵀx + d with symmetric Q, the gradient is ∇f = 2Qx + c.

- The Hessian matrix is essential for determining whether critical points are minima, maxima, or saddle points.

- Setting ∇f = 0 finds critical points that are candidates for optimal solutions.

- In gradient descent, xₖ₊₁ = xₖ - α∇f(xₖ) moves toward minima when α is appropriately chosen.

- The Jacobian generalizes the gradient to vector-valued functions.

- Chain rule is crucial for computing gradients of composite functions like exp(-‖x‖²).

## Common Mistakes to Avoid

- Forgetting that ∇(xᵀAx) requires (A + Aᵀ)x when A is not symmetric.

- Confusing the gradient (vector) with the directional derivative (scalar).

- Not checking dimension compatibility when computing gradients of vector functions.

- Omitting the learning rate or using incorrect sign in gradient descent updates.

## Revision Tips

- Memorize the standard gradient formulas for quadratic forms, norms, and exponential functions.

- Practice computing partial derivatives as they form the foundation of gradient computation.

- Remember that negative gradient gives the descent direction in optimization algorithms.

- Review the relationship between gradient, Hessian, and the nature of critical points.
