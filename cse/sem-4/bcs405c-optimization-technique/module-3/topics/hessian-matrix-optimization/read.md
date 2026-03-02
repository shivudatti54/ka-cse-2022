# Application of Hessian Matrix in Optimization

## Table of Contents

- [Application of Hessian Matrix in Optimization](#application-of-hessian-matrix-in-optimization)
- [Introduction](#introduction)
- [Hessian Definition](#hessian-definition)
- [Role in Optimization](#role-in-optimization)
  - [Second Derivative Test](#second-derivative-test)
  - [Step Size Determination](#step-size-determination)
  - [Curvature Information](#curvature-information)
- [Practical Considerations](#practical-considerations)
  - [Computing Hessian](#computing-hessian)
  - [Hessian-Free Optimization](#hessian-free-optimization)
- [Important Points](#important-points)

## Introduction

The Hessian matrix contains second-order partial derivatives and provides crucial information about local curvature.

## Hessian Definition

For function f: ℝⁿ → ℝ:
H[i,j] = ∂²f/∂xᵢ∂xⱼ

## Role in Optimization

### Second Derivative Test

- H > 0 (positive definite): local minimum
- H < 0 (negative definite): local maximum
- H indefinite: saddle point
- H ≥ 0 (positive semi-definite): convex

### Step Size Determination

Newton's method uses Hessian:
x(k+1) = x(k) - H⁻¹∇f

### Curvature Information

- Large curvature: smaller steps needed
- Small curvature: larger steps possible
- Negative curvature: step in wrong direction

## Practical Considerations

### Computing Hessian

- O(n²) elements for n variables
- Expensive for high dimensions
- Often approximated

### Hessian-Free Optimization

- Use gradient information only
- Approximate Hessian-vector products
- Used in deep learning

## Important Points

1. Hessian tells us about local curvature
2. Newton's method uses Hessian for faster convergence
3. Positive definite Hessian indicates minimum
4. Computational cost is O(n²)
