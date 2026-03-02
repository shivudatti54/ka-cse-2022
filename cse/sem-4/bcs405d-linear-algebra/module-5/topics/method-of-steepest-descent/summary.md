# Method of Steepest Descent - Summary

## Key Definitions and Concepts

- **Steepest Descent Method**: An iterative optimization technique that finds the minimum of a function by moving in the direction of the negative gradient (steepest descent direction).

- **Quadratic Function**: f(x) = (1/2)x^T A x - b^T x, where A is symmetric positive definite (SPD).

- **Residual**: r_k = b - Ax_k, representing the error in satisfying the linear system at iteration k.

- **A-norm**: ||x||\_A = sqrt(x^T A x), a weighted norm used in convergence analysis.

- **Condition Number**: κ(A) = λ_max/λ_min, determining the convergence rate of the method.

## Important Formulas and Theorems

- **Gradient**: ∇f(x) = Ax - b

- **Search Direction**: d_k = -∇f(x_k) = r_k = b - Ax_k

- **Optimal Step Size**: α_k = (r_k^T r_k) / (r_k^T A r_k)

- **Iteration Formula**: x\_{k+1} = x_k + α_k r_k

- **Residual Update**: r\_{k+1} = r_k - α_k A r_k

- **Convergence Factor**: (κ(A) - 1)/(κ(A) + 1)

- **Convergence Bound**: ||x_k - x^_||\_A ≤ ((κ-1)/(κ+1))^k ||x_0 - x^_||\_A

## Key Points

- The method solves Ax = b by minimizing the associated quadratic function f(x).

- At each iteration, the search direction is the negative gradient (residual vector).

- The step size is optimally chosen to minimize f along the search direction.

- Convergence is linear and depends heavily on the condition number of A.

- For well-conditioned matrices (κ ≈ 1), convergence is very fast.

- For ill-conditioned matrices (κ >> 1), convergence can be extremely slow.

- The method requires A to be symmetric and positive definite for guaranteed convergence.

- Search directions at successive iterations are orthogonal (r_i^T r_j = 0 for i ≠ j).

## Common Mistakes to Avoid

1. Using arbitrary step sizes instead of the optimal formula α_k = (r_k^T r_k)/(r_k^T A r_k).

2. Forgetting that the method only guarantees convergence for SPD matrices.

3. Not checking the condition number before applying the method—ill-conditioned systems lead to very slow convergence.

4. Using the wrong formula for the quadratic function—missing the (1/2) factor changes the gradient.

5. Confusing the residual r_k with the error e_k = x_k - x^\*—they are different quantities.

## Revision Tips

1. Practice deriving the optimal step size formula by differentiating f(x_k + αd_k) with respect to α.

2. Solve at least 2-3 complete examples by hand to understand the iteration process.

3. Remember the geometric interpretation: each step goes perpendicular to the contour lines of f.

4. Know the relationship between condition number and convergence—if κ = 1, convergence is immediate; if κ = 1000, convergence is very slow.

5. Understand why the method "zig-zags" toward the solution—successive search directions are orthogonal.
