# Convex Sets and Functions

## Table of Contents

- [Convex Sets and Functions](#convex-sets-and-functions)
- [Convex Sets](#convex-sets)
- [Convex Functions](#convex-functions)
- [Properties of Convex Functions](#properties-of-convex-functions)
- [Examples](#examples)
- [Non-Convex Functions](#non-convex-functions)
- [Importance in Optimization](#importance-in-optimization)
- [Important Points](#important-points)

## Convex Sets

A set S is convex if for any two points in S, the line segment between them is also in S.

Mathematically:
If x, y ∈ S, then λx + (1-λ)y ∈ S for 0 ≤ λ ≤ 1

## Convex Functions

A function f is convex if:
f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y)

## Properties of Convex Functions

1. Any local minimum is also global minimum
2. Second derivative ≥ 0 (for twice differentiable)
3. Epigraph is a convex set

## Examples

- Linear functions: f(x) = ax + b
- Quadratic (positive definite): f(x) = x²
- Exponential: f(x) = eˣ
- Norms: f(x) = ||x||

## Non-Convex Functions

- Sine, cosine
- Neural network loss landscapes
- Polynomial of degree > 2

## Importance in Optimization

1. Convex problems are "easy"
2. Gradient descent converges to global minimum
3. Many machine learning problems relaxed to convex

## Important Points

1. Convex = no local minima trap
2. Second derivative test for convexity
3. Sum of convex functions is convex
