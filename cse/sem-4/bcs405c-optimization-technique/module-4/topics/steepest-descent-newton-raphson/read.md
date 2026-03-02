# Method of Steepest Descent and Newton-Raphson

## Table of Contents

- [Method of Steepest Descent and Newton-Raphson](#method-of-steepest-descent-and-newton-raphson)
- [Steepest Descent (Gradient Descent)](#steepest-descent-gradient-descent)
  - [Properties](#properties)
- [Newton-Raphson Method](#newton-raphson-method)
  - [Properties](#properties)
- [Comparison](#comparison)
- [When to Use Each](#when-to-use-each)
- [Practical Considerations](#practical-considerations)
- [Important Points](#important-points)

## Steepest Descent (Gradient Descent)

The direction of steepest descent is opposite to the gradient.

Algorithm:
x(k+1) = x(k) - α∇f(x(k))

### Properties

- Simple to implement
- First-order method (uses gradient)
- Slow convergence near optimum
- Oscillates in narrow valleys

## Newton-Raphson Method

Uses second-order derivative (Hessian):

x(k+1) = x(k) - H⁻¹∇f(x(k))

### Properties

- Second-order method
- Fast quadratic convergence near optimum
- Requires Hessian computation/inversion
- May diverge if starting far from optimum

## Comparison

| Aspect      | Steepest Descent | Newton-Raphson |
| ----------- | ---------------- | -------------- |
| Order       | First            | Second         |
| Convergence | Linear           | Quadratic      |
| Hessian     | Not needed       | Required       |
| Stability   | More stable      | Can diverge    |

## When to Use Each

- Steepest Descent: Far from optimum, simple problems
- Newton-Raphson: Near optimum, when Hessian available

## Practical Considerations

1. Learning rate for steepest descent
2. Hessian may be singular/invertible
3. Often combined: steepest descent far, Newton near

## Important Points

1. Steepest descent: x = x - α∇f
2. Newton: x = x - H⁻¹∇f
3. Newton converges faster near solution
4. Steepest descent is more robust
