# Mini-Batch and Stochastic Gradient Descent

## Table of Contents

- [Mini-Batch and Stochastic Gradient Descent](#mini-batch-and-stochastic-gradient-descent)
- [Batch Gradient Descent](#batch-gradient-descent)
- [Stochastic Gradient Descent (SGD)](#stochastic-gradient-descent-sgd)
- [Mini-Batch Gradient Descent](#mini-batch-gradient-descent)
- [Batch Size Impact](#batch-size-impact)
- [Variants](#variants)
  - [Momentum](#momentum)
  - [Nesterov Accelerated Gradient](#nesterov-accelerated-gradient)
- [Learning Rate Schedules](#learning-rate-schedules)
- [Important Points](#important-points)

## Batch Gradient Descent

Uses entire dataset for each update:
θ = θ - α∇J(θ; all samples)

Pros: Stable convergence
Cons: Slow for large datasets

## Stochastic Gradient Descent (SGD)

Uses single sample for each update:
θ = θ - α∇J(θ; single sample)

Pros: Fast, can escape local minima
Cons: Noisy updates, many iterations

## Mini-Batch Gradient Descent

Uses small batch (e.g., 32, 64, 128 samples):
θ = θ - α∇J(θ; batch)

Combines benefits of both:

- Faster than batch
- Less noisy than SGD
- Efficient with vectorization

## Batch Size Impact

- Large batch: stable, GPU efficient
- Small batch: more noise, regularization effect
- Typical: 32-512

## Variants

### Momentum

v = βv + α∇J(θ)
θ = θ - v

### Nesterov Accelerated Gradient

Computes gradient at lookahead position

## Learning Rate Schedules

1. Step decay
2. Exponential decay
3. Cosine annealing
4. Warm restarts

## Important Points

1. Mini-batch balances speed and stability
2. Learning rate is critical
3. Momentum helps escape local minima
4. Batch size affects generalization
