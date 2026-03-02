# Optimization Technique

### Unconstrained Optimization

- **Method of Steepest Ascent/Descent**:
  - Steepest ascent: increment in the direction of the gradient to maximize/minimize
  - Steepest descent: decrement in the direction of the negative gradient to minimize

- **Nelder-Mead (NR) Method**:
  - Simplex-based optimization method
  - Uses the distance of points from the center to determine convergence

- **Gradient Descent (GD)**:
  - Iteratively update the parameters in the direction of the negative gradient
  - Convergence condition: gradient norm ≤ ε or iteration limit

### Learning Rate and Convergence

- **Learning Rate**:
  - Step size for each gradient update (α)
  - Affects convergence speed and stability

- **Convergence Theorems**:
  - Weierstrass Theorem: a continuous function achieves a local minimum on a compact set
  - Asymptotic Convergence: gradient descent converges to the solution as the number of iterations increases

### Mini Batch Gradient Descent and Stochastic Gradient Descent

- **Mini Batch Gradient Descent**:
  - Uses a mini-batch of data at each iteration
  - Reduces variance in gradient estimates

- **Stochastic Gradient Descent**:
  - Uses a single data point at each iteration
  - More computationally efficient but less accurate than mini-batch GD

## Formulas

- Gradient: ∇f(x) = ∂f/∂x
- Steepest Descent update: x_new = x_old - α∇f(x_old)
- Gradient Descent update: x_new = x_old - α∇f(x_old)
