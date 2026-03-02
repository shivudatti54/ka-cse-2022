# Linearization and Multivariate Taylor Series

## Table of Contents

- [Linearization and Multivariate Taylor Series](#linearization-and-multivariate-taylor-series)
- [Introduction](#introduction)
- [Linearization](#linearization)
- [Multivariate Taylor Series](#multivariate-taylor-series)
- [Applications](#applications)
- [Important Points](#important-points)

## Introduction

Linearization approximates a nonlinear function with a linear function near a point. Multivariate Taylor series extends this to functions of multiple variables.

## Linearization

For f(x) near x=a:
f(x) ≈ f(a) + f'(a)(x-a)

For multivariate f(x,y):
f(x,y) ≈ f(a,b) + fx(a,b)(x-a) + fy(a,b)(y-b)

## Multivariate Taylor Series

f(x+h) = f(x) + ∇f(x)·h + 1/2 hᵀH(x)h + ...

Where:

- ∇f is the gradient
- H is the Hessian matrix

## Applications

1. Optimization: approximating cost functions
2. Machine learning: gradient computation
3. Physics: small perturbation analysis

## Important Points

1. First-order approximation uses gradient only
2. Second-order uses Hessian
3. Higher order terms improve accuracy
4. Taylor series used in optimization algorithms
