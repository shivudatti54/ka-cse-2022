# Linearization and Multivariate Taylor Series - Summary

## Key Definitions and Concepts

- **Linearization:** The first-order Taylor approximation of a multivariable function: L(x) = f(a) + ∇f(a)ᵀ(x-a)
- **Gradient Vector (∇f):** Column vector of first-order partial derivatives pointing in direction of steepest ascent
- **Hessian Matrix:** Square matrix of second-order partial derivatives representing local curvature
- **Taylor Series Expansion:** Infinite sum representation of functions using derivatives at a single point

## Important Formulas and Theorems

**First-Order (Linear):** f(x) ≈ f(a) + ∇f(a)ᵀ(x-a)

**Second-Order:** f(x) ≈ f(a) + ∇f(a)ᵀ(x-a) + ½(x-a)ᵀH(f)(a)(x-a)

**Gradient:** ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ

**Hessian (2×2):** H = [∂²f/∂x², ∂²f/∂x∂y; ∂²f/∂y∂x, ∂²f/∂y²]

**Error Bound:** First-order error is O(||x-a||²)

## Key Points

- Linearization simplifies complex nonlinear functions to linear ones for local approximation
- Gradient indicates direction of maximum function increase; negative gradient points to steepest descent
- Hessian matrix is always symmetric when second-order partial derivatives are continuous
- Positive definite Hessian → local minimum; Negative definite → local maximum; Indefinite → saddle point
- Taylor series forms mathematical foundation for Newton's method and other gradient-based optimization algorithms
- Higher-order terms become negligible close to expansion point, making local analysis accurate
- The expansion point 'a' is typically chosen as a critical point or current iterate in optimization

## Common Mistakes to Avoid

1. **Forgetting to evaluate derivatives at the expansion point** - Always compute ∇f(a) and H(a) at the correct point
2. **Incorrect matrix multiplication** - Remember (x-a)ᵀH(x-a) expands to quadratic form correctly
3. **Sign errors in gradient** - Double-check partial derivative calculations, especially with product/quotient rules
4. **Confusing local and global behavior** - Taylor series only guarantees accurate local approximation

## Revision Tips

1. Practice computing gradients and Hessians for various functions until automatic
2. Memorize the first and second-order Taylor formulas - they appear in every exam
3. Work through at least 3-4 examples of linearization before the exam
4. Understand the geometric interpretation: linearization = tangent plane; second-order = paraboloid approximation
5. Remember classification rules: eigenvalues of Hessian determine the nature of critical points
