# **Revision Notes: Optimization Technique (8 hours)**

### Overview

---

- Convex optimization techniques are used to solve optimization problems where the objective function and constraints are convex.
- The goal is to find the optimal solution that minimizes or maximizes the objective function.

### Key Points

---

- **Convex Sets**:
  - A set is convex if for any two points in the set, the line segment connecting them is also in the set.
  - Examples: closed intervals, balls, convex polyhedra.
- **Convex Functions**:
  - A function is convex if its graph lies above or on all tangent lines to the graph.
  - Examples: quadratic functions, concave functions.
- **Convex Optimization**:
  - Minimize or maximize a convex function subject to convex constraints.
  - The optimal solution can be found using various techniques such as:
    - Gradient Descent
    - Lagrange Multipliers
    - Karush-Kuhn-Tucker (KKT) Conditions
- **Important Formulas and Definitions**

---

- **Convex Function**: $f(x) \geq f(y) + \nabla f(x) (x-y)$ for all $x, y$ in the domain.
- **Gradien Descent**: $\nabla f(x) = 0$ for local minima.
- **Lagrange Multiplier**: $\nabla f(x) + \lambda \nabla g(x) = 0$ where $g(x) = 0$ is the constraint function.
- **KKT Conditions**: $(\nabla f(x) + \lambda \nabla g(x)) \cdot x = 0$, $g(x) = 0$, $\lambda \geq 0$.

### Important Theorems

---

- **Weierstrass Theorem**: Every continuous function on a compact set attains its minimum and maximum.
- **Karush-Kuhn-Tucker Theorem**: Necessary and sufficient conditions for a point to be a local minimum of a convex function subject to convex constraints.

### Additional Tips

---

- Always check the type of optimization problem (minimize or maximize) and the nature of the objective function and constraints.
- Use the appropriate optimization technique (Gradient Descent, Lagrange Multipliers, KKT Conditions) to solve the problem.
- Always check the KKT conditions to ensure that the solution is optimal.
