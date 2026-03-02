# Non-Convex Optimization: Convergence to Critical Points

### Definitions

- **Non-convex optimization**: An optimization problem where the objective function is non-convex, meaning its graph is not a convex set.
- **Critical points**: Points in the domain where the gradient is zero or undefined, indicating potential optimality.

### Key Concepts

- **KKT conditions**: Necessary conditions for a point to be a local minimum or maximum, including:
  - Stationarity
  - Primal feasibility
  - Dual feasibility
  - Complementary slackness
- **Karush-Kuhn-Tucker (KKT) theorem**: A sufficient condition for a point to be a local minimum or maximum, stating that if the KKT conditions are satisfied, then the point is a local minimum.
- **First-order methods**: Iterative methods that use gradients to improve the solution, such as gradient descent and its variants.
- **Second-order methods**: Iterative methods that use Hessian matrices to improve the solution, such as Newton's method.

### Important Formulas

- **Gradient descent**: `x_new = x_old - α \* ∇f(x_old)`
- **Newton's method**: `x_new = x_old - α \* H^(-1) \* ∇f(x_old)`
- **KKT conditions**: F1(x) ≤ 0, F2(x) ≥ 0, F3(x) = 0, g(x) ≤ 0, g(x) = 0

### Theorems

- **Weierstrass's theorem**: Any continuous function on a compact set has a local minimum.
- **Monge-Ampère theorem**: The Hessian determinant of a convex function is non-negative.

### Revision Tips

- Understand the KKT conditions and the Karush-Kuhn-Tucker theorem.
- Familiarize yourself with gradient descent and Newton's method.
- Recognize the importance of convexity in optimization problems.
- Be aware of the limitations of first-order and second-order methods for non-convex optimization.
