# Convex Optimization-1: (8 hours)

## **Key Concepts**

- **Convex Optimization**: A subfield of optimization that deals with convex functions and convex sets.
- **Convex Function**: A function f(x) that satisfies the following property:
  - For any two points x1 and x2 in the domain of f, and any λ in [0, 1]:
    f(λx1 + (1-λ)x2) ≤ λf(x1) + (1-λ)f(x2)
- **Convex Set**: A set S that satisfies the following property:
  - For any two points x1 and x2 in S, and any λ in [0, 1]:
    λx1 + (1-λ)x2 ∈ S
- **Strong Convexity**: A function f(x) is strongly convex if it satisfies the following property:
  - For any two points x1 and x2 in the domain of f, and any λ in [0, 1]:
    f(λx1 + (1-λ)x2) ≤ (1-λ)f(x1) + λf(x2) - (λ^2/2)(f(x1) - f(x2))^2

## **Important Formulas and Definitions**

- **Karush-Kuhn-Tucker (KKT) Conditions**: A set of conditions used to determine the optimality of a solution in a convex optimization problem.
  - ∇f(x) + ∇g(x)^T y = 0
  - g(x) ≤ 0
  - y^T g(x) = 0
  - y ≥ 0
- **Lagrange Multiplier Method**: A method used to find the optimal values of variables in a constrained optimization problem.
  - f(x) + λ^T g(x) = c
  - ∇f(x) + λ^T ∇g(x) = 0

## **Important Theorems**

- **Weierstrass Theorem**: A theorem that states that a continuous function on a compact set attains its minimum value.
- **Karamata's Theorem**: A theorem that states that a convex function is differentiable if and only if it is strictly convex.

## **Revision Tips**

- Understand the definitions of convex functions and convex sets.
- Learn the KKT conditions and the Lagrange multiplier method.
- Review the Weierstrass Theorem and Karamata's Theorem.
