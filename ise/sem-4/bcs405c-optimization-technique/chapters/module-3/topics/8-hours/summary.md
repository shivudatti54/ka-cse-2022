# Convex Optimization-1 Topic: (8 hours)

### Overview

- Convex optimization is a field of mathematics that deals with optimizing functions subject to constraints.
- The topic covers the basics of convex optimization, including definitions, theorems, and important formulas.

### Key Definitions

- **Convex Function**: A function f(x) is said to be convex if for any two points x1 and x2 in its domain and any λ in [0,1], the following inequality holds: f(λx1 + (1-λ)x2) ≤ λf(x1) + (1-λ)f(x2)
- **Convex Set**: A set S is said to be convex if for any two points x1 and x2 in S and any λ in [0,1], the point λx1 + (1-λ)x2 is also in S.
- **Convex Optimization Problem**: A problem of the form: minimize/copy maximize subject to a set of constraints, where the objective function and the constraints are convex.

### Important Formulas

- **Karamardian Theorem**: If the gradient of a convex function is Lipschitz continuous, then the function is strictly convex.
- **Karush-Kuhn-Tucker (KKT) Theorem**: If a point x is a local minimum of a convex function subject to a set of constraints, then there exists a Lagrange multiplier λ such that the KKT conditions are satisfied.
- **Cauchy-Schwarz Inequality**: For any vectors u and v in Euclidean space, the following inequality holds: (u,v)^2 ≤ (u,u)(v,v)

### Important Theorems

- **Weber's Theorem**: If a function f(x) is convex on the interval [a,b] and continuous on [a,b], then the minimum value of f(x) occurs at one of the endpoints of the interval.
- **Farkas' Lemma**: If a point x satisfies the constraints of a convex optimization problem, then either the objective function is minimized at x or there exists a non-zero vector y such that y^T x = 0.

### Useful Concepts

- **Convex Hull**: The smallest convex set that contains a given set of points.
- **Saddler Convexity**: A function is said to be saddler convex if it is convex on one side of the origin and concave on the other side.

### Additional Tips

- Recall the properties of convex sets and functions, including the definition of convexity and the KKT theorem.
- Practice solving optimization problems using the KKT theorem and other techniques.
- Review the concepts of convex optimization, including the Cauchy-Schwarz inequality and Farkas' lemma.
