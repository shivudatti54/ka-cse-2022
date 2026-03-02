# Descending the Gradient of Cost

## Table of Contents

- [Descending the Gradient of Cost](#descending-the-gradient-of-cost)
- [Introduction](#introduction)
- [The Gradient Descent Algorithm](#the-gradient-descent-algorithm)
- [Learning Rate Impact](#learning-rate-impact)
- [Types of Gradient Descent](#types-of-gradient-descent)
  - [Batch Gradient Descent](#batch-gradient-descent)
  - [Stochastic Gradient Descent (SGD)](#stochastic-gradient-descent-sgd)
  - [Mini-batch Gradient Descent](#mini-batch-gradient-descent)
- [Cost Function Landscape](#cost-function-landscape)
- [Important Points](#important-points)

## Introduction

Gradient descent is the fundamental optimization algorithm that minimizes the cost function by moving in the direction of steepest descent.

## The Gradient Descent Algorithm

Repeat until convergence:

1. Compute gradient: g = ∂J/∂w
2. Update weights: w = w - α × g

Where α = learning rate

## Learning Rate Impact

- Too small: slow convergence
- Too large: may overshoot minimum
- Just right: efficient convergence

## Types of Gradient Descent

### Batch Gradient Descent

- Computes gradient using entire dataset
- Stable but slow for large datasets

### Stochastic Gradient Descent (SGD)

- Computes gradient for single sample
- Fast but noisy updates

### Mini-batch Gradient Descent

- Uses small batches of samples
- Balances speed and stability

## Cost Function Landscape

- Global minimum: lowest point overall
- Local minimum: lowest in nearby region
- Saddle point: flat in one direction, curved in another

## Important Points

1. Learning rate is crucial hyperparameter
2. Gradient points uphill, so we subtract
3. Convergence may get stuck in local minima
4. Learning rate can be adaptive
