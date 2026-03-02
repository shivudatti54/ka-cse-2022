# Hessian Matrix - Summary

## Key Definitions and Concepts

- **Hessian Matrix**: An n × n matrix containing all second-order partial derivatives of a scalar function f: ℝⁿ → ℝ. The (i,j)-th element is ∂²f/(∂xᵢ∂xⱼ).

- **Critical Point**: A point where ∇f = 0 (gradient is zero). At critical points, first-order necessary condition for optimality is satisfied.

- **Positive Definite Matrix**: A symmetric matrix H where xᵀHx > 0 for all non-zero vectors x. All eigenvalues are positive.

- **Negative Definite Matrix**: A symmetric matrix H where xᵀHx < 0 for all non-zero vectors x. All eigenvalues are negative.

- **Indefinite Matrix**: A matrix with both positive and negative eigenvalues, leading to a saddle point.

## Important Formulas and Theorems

- **Hessian Definition**: H(f) = [∂²f/∂xᵢ∂xⱼ] for i,j = 1 to n

- **Second-Order Taylor Series**: f(x) ≈ f(a) + ∇f(a)ᵀ(x-a) + ½(x-a)ᵀH(a)(x-a)

- **Sylvester's Criterion (Positive Definite)**: All leading principal minors > 0

- **Sylvester's Criterion (Negative Definite)**: Leading principal minors alternate: -, +, -, +,... starting with negative

- **Clairaut's Theorem**: If second-order partial derivatives are continuous, Hessian is symmetric: ∂²f/∂xᵢ∂xⱼ = ∂²f/∂xⱼ∂xᵢ

## Key Points

- The Hessian Matrix represents the curvature of a multivariable function.

- At a critical point, positive definite Hessian ⇒ local minimum; negative definite ⇒ local maximum; indefinite ⇒ saddle point.

- For functions with continuous second derivatives, the Hessian is always symmetric.

- Sylvester's criterion provides a computationally efficient way to test definiteness without computing eigenvalues.

- The Hessian is essential in optimization algorithms (Newton's method, quasi-Newton methods) and machine learning (neural network training).

- A positive definite Hessian indicates convexity (local minimum = global minimum).

## Common Mistakes to Avoid

- **Forgetting to check critical points**: The Hessian classification is meaningless unless ∇f = 0 at the point.

- **Ignoring symmetry**: Using Sylvester's criterion requires a symmetric matrix; always verify symmetry first ( Clairaut's theorem ensures it for continuously differentiable functions).

- **Sign errors in partial derivatives**: Carefully compute all second-order derivatives; common errors include wrong application of chain rule.

- **Confusing definiteness conditions**: Positive semidefinite is NOT the same as positive definite; check strict inequalities.

## Revision Tips

1. Practice computing Hessians for various functions until you can do it quickly and accurately.

2. Memorize Sylvester's criterion conditions for both positive and negative definiteness.

3. Work through at least 5-6 classification problems to reinforce the procedure.

4. Remember: critical point → compute Hessian → check definiteness → classify.

5. Understand the geometric interpretation: positive definite = bowl-shaped (minimum), negative definite = inverted bowl (maximum), indefinite = saddle-shaped.
