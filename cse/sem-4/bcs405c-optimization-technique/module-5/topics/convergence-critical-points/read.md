# Convergence to Critical Points

## Table of Contents

- [Convergence to Critical Points](#convergence-to-critical-points)
- [Critical Points](#critical-points)
- [Convergence Analysis](#convergence-analysis)
  - [For Convex Functions](#for-convex-functions)
  - [For Non-Convex Functions](#for-non-convex-functions)
- [Conditions for Convergence](#conditions-for-convergence)
  - [Learning Rate Conditions](#learning-rate-conditions)
  - [Sufficient Conditions](#sufficient-conditions)
- [Types of Convergence](#types-of-convergence)
- [Escape from Saddle Points](#escape-from-saddle-points)
- [Important Points](#important-points)

## Critical Points

A point x is critical if:
∇f(x) = 0

Types of critical points:

- Local minima
- Local maxima
- Saddle points

## Convergence Analysis

### For Convex Functions

- Any critical point is global minimum
- Gradient descent converges to optimum

### For Non-Convex Functions

- May converge to local minimum
- May get stuck at saddle point
- Can escape with noise/momentum

## Conditions for Convergence

### Learning Rate Conditions

For step size α:

- α < 2/L (L = Lipschitz constant of gradient)
- Ensures descent at each step

### Sufficient Conditions

1. Function bounded below
2. Learning rate in valid range
3. Gradient Lipschitz continuous

## Types of Convergence

1. Convergence to critical point
2. Convergence to local minimum
3. Convergence rate (linear, superlinear, quadratic)

## Escape from Saddle Points

1. Add noise to gradients
2. Use momentum
3. Random initialization
4. Batch normalization

## Important Points

1. Critical point: gradient equals zero
2. Not all critical points are minima
3. Learning rate affects convergence
4. Saddle points common in high dimensions
