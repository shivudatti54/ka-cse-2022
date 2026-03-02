# Local and Global Optima

## Table of Contents

- [Local and Global Optima](#local-and-global-optima)
- [Introduction](#introduction)
- [Definitions](#definitions)
  - [Global Minimum](#global-minimum)
  - [Local Minimum](#local-minimum)
- [Characteristics](#characteristics)
  - [Global Optimum](#global-optimum)
  - [Local Optimum](#local-optimum)
- [Implications for Optimization](#implications-for-optimization)
  - [Convex Functions](#convex-functions)
  - [Non-Convex Functions](#non-convex-functions)
- [Escape from Local Minima](#escape-from-local-minima)
- [Important Points](#important-points)

## Introduction

In optimization, we seek the best solution. However, there may be multiple optima - local and global.

## Definitions

### Global Minimum

The point with the lowest function value over the entire domain:
f(x\*) ≤ f(x) for all x in domain

### Local Minimum

The point with the lowest value in its neighborhood:
f(x*) ≤ f(x) for all x near x*

## Characteristics

### Global Optimum

- Best possible solution
- Unique (or few) in convex problems
- Desired solution in optimization

### Local Optimum

- Best in local neighborhood
- May not be global
- Can trap gradient descent

## Implications for Optimization

### Convex Functions

- Only one minimum (global)
- Gradient descent finds global optimum
- Easier to optimize

### Non-Convex Functions

- Multiple local minima
- Need better initialization
- May require sophisticated methods

## Escape from Local Minima

1. Random restarts
2. Momentum-based methods
3. Simulated annealing
4. Evolutionary algorithms

## Important Points

1. Local minima are problematic in deep learning
2. Saddle points more common in high dimensions
3. Initialization affects which minimum found
4. Global optimum guaranteed only for convex problems
