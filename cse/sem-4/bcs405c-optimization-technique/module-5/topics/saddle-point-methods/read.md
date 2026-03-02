# Saddle Point Methods

## Table of Contents

- [Saddle Point Methods](#saddle-point-methods)
- [Introduction](#introduction)
- [Identifying Saddle Points](#identifying-saddle-points)
- [Challenges](#challenges)
- [Escape Methods](#escape-methods)
- [Visualizing](#visualizing)

## Introduction

Saddle points are critical points where gradient is zero but function is neither minimum nor maximum. They pose challenges in non-convex optimization.

## Identifying Saddle Points

- Hessian has mixed eigenvalues
- Some positive, some negative
- Local minimum in some directions, maximum in others

## Challenges

1. Gradient descent can get stuck
2. Common in high-dimensional spaces
3. Difficulty escaping affects training

## Escape Methods

1. Add gradient noise
2. Stochastic gradient descent
3. Batch normalization
4. Proper weight initialization
5. Learning rate scheduling

## Visualizing

Think of a saddle: curves up in one direction, down in another.

1. Saddle points## Important Points
   more common than local minima in high dimensions
2. Escape requires breaking symmetry
3. Modern optimizers help avoid getting stuck
4. Initialization affects likelihood of encountering
