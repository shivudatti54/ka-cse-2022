# Differentiation and Partial Differentials - Summary

## Key Definitions and Concepts

- **Derivative**: The instantaneous rate of change of a function f(x) with respect to x, defined as f'(x) = lim[h→0] [f(x+h) - f(x)]/h

- **Partial Derivative**: The derivative of a function of multiple variables with respect to one variable while treating other variables as constants (denoted as ∂f/∂x)

- **Critical Point**: A point where f'(x) = 0 or f'(x) does not exist; candidates for local maxima or minima

- **Total Derivative**: For z = f(x, y) where x and y are functions of t: dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt)

- **Jacobian Matrix**: Matrix of all first-order partial derivatives of a vector-valued function

## Important Formulas and Theorems

- **Power Rule**: d/dx(xⁿ) = nxⁿ⁻¹
- **Product Rule**: d/dx[f(x)g(x)] = f'g + fg'
- **Quotient Rule**: d/dx[f/g] = (f'g - fg')/g²
- **Chain Rule**: d/dx[f(g(x))] = f'(g(x)) × g'(x)
- **Young's Theorem**: ∂²f/∂x∂y = ∂²f/∂y∂x (when continuous)
- **Second Derivative Test**: f''(c) > 0 → minimum; f''(c) < 0 → maximum
- **Taylor Series**: f(x+h) = f(x) + hf' + (h²/2!)f'' + ...

## Key Points

- Differentiation measures instantaneous rate of change; partial differentiation measures change in one direction while holding other variables constant

- The second derivative test classifies critical points: positive indicates minimum, negative indicates maximum

- Mixed partial derivatives are equal under continuity conditions (Young's theorem)

- Total differentiation accounts for indirect dependencies through chain rule

- Taylor series provides polynomial approximation of functions, essential for numerical optimization

- Critical points are found by setting first derivative(s) to zero

- The Jacobian determinant helps determine if implicit functions can be solved and in coordinate transformations

## Common Mistakes to Avoid

- Confusing partial derivatives (∂) with total derivatives (d)—partial holds other variables constant

- Forgetting to apply the chain rule when differentiating composite functions

- Using the wrong sign in the second derivative test—remember: concave up (minimum), concave down (maximum)

- Not checking conditions for Young's theorem before claiming equality of mixed partials

## Revision Tips

- Practice differentiating various function types (polynomial, trigonometric, exponential, logarithmic) until comfortable with all rules

- Solve at least 3-4 problems each on critical point finding, partial differentiation, and total differentiation

- Create a formula sheet with all differentiation rules and review it daily

- Understand the geometric meaning: derivative = slope of tangent, partial derivative = slope in one coordinate direction

- Work through previous year university exam questions on this topic to understand the pattern and difficulty level
