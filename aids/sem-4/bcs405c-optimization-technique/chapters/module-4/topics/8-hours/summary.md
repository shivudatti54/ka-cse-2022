# Revision Notes: Optimization Techniques (8 hours)

=============================================

### Introduction

---

- Optimization techniques are used to minimize or maximize a function subject to constraints.

### Key Concepts

---

- **Optimization Problem**: A problem of the form minimize/c maximize f(x) subject to g(x) ≤ 0, h(x) = 0, ..., etc.
- **Convex Optimization**: A field of optimization where the objective function and the constraints are convex functions.
- **Convex Set**: A set for which the line segment connecting any two points in the set lies entirely within the set.

### Important Formulas and Definitions

---

- **KKT Conditions**: Necessary conditions for a point to be a local minimum or maximum of a convex optimization problem:
  ```math
  \begin{align*}
  \nabla f(x) + \sum_{i=1}^m \lambda_i \nabla g_i(x) &= 0 \\
  g_i(x) &= 0, \quad \forall i = 1, \ldots, m \\
  \lambda_i &\geq 0, \quad \forall i = 1, \ldots, m
  \end{align*}
  ```

```
* **Karush-Kuhn-Tucker (KKT) Theorem**: A theorem that guarantees the existence of a solution to a convex optimization problem using the KKT conditions.

### Important Theorems
----------------------

* **Weierstrass Theorem**: A theorem that states every continuous function on a closed and bounded interval attains its minimum and maximum values.
* **Fermat's Theorem**: A theorem that states that a function attains its minimum value at a point where its gradient is zero.

### Important Algorithms
------------------------

* **Gradient Descent**: An iterative algorithm used to minimize a convex function.
* **Newton's Method**: An iterative algorithm used to minimize a convex function, especially when the Hessian matrix is available.

### References
--------------

* [Insert references]
```
