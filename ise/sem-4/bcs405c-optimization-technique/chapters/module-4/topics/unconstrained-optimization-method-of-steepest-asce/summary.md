# Unconstrained Optimization

### Method of Steepest Ascent/Descent

- **Method of Steepest Ascent:**
  - Updates the current estimate by moving in the direction of the negative gradient.
  - **Formula:** `x_new = x_old - α * (-grad(f(x_old)))`
  - **Example:** `x_new = x_old - α * (-f'(x_old))`
- **Method of Descent:**
  - Similar to the method of steepest ascent but with a smaller step size.
  - **Formula:** `x_new = x_old - α * (-grad(f(x_old)))` (smaller step size)

### Newton-Raphson (NR) Method

- **Formula:** `x_new = x_old - H^-1 * (-grad(f(x_old)))`
- **Hessian Matrix (H):** The second partial derivatives of the function.
- **Importance:** Faster convergence than gradient descent, but requires the Hessian matrix.

### Gradient Descent

- **Formula:** `x_new = x_old - α * (-grad(f(x_old)))`
- **Importance:** Simple and widely used, but slow convergence.
- **Mini-batch Gradient Descent:**
  - Use a subset of the data to compute the gradient.
  - **Formula:** `x_new = x_old - α * (1/n) * Σ(-grad(f(xi)))`

### Stochastic Gradient Descent (SGD)

- **Formula:** `x_new = x_old - α * (-grad(f(xi)))`
- **Importance:** Fast and efficient, but may not converge to the global minimum.
- **Importance:** More suitable for large datasets.

## Key Concepts

- **Convergence:** The process of reaching a minimum or maximum value.
- **Optimization:** The process of finding the best solution.
- **Gradient:** A measure of the rate of change of a function.

## Important Formulas and Theorems

- **Gradient Descent Formula:** `x_new = x_old - α * (-grad(f(x_old)))`
- **Hessian Matrix Formula:** `H = [∂^2 f/∂x_i ∂x_j]`
- **Convergence Theorem:** If the gradient is zero, the algorithm has converged.

## Revision Tips

- Review the formulas and concepts.
- Practice implementing the algorithms.
- Understand the importance of each method.
- Review the convergence theorems and formulas.
