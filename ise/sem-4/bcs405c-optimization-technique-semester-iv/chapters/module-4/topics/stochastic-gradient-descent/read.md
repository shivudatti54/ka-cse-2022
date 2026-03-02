# Gradient Descent

## What is Gradient Descent?

Gradient descent is an optimization algorithm that iteratively updates parameters by moving in the direction opposite to the gradient of the loss function. It's the foundation of neural network training.

## Key Concepts

### The Basic Update Rule

```
θ = θ - α * ∇L(θ)
```

Where:

- θ: Parameters (weights and biases)
- α: Learning rate (step size)
- ∇L(θ): Gradient of loss w.r.t. parameters

### Intuition

- Gradient points in direction of steepest increase
- Moving opposite to gradient decreases loss
- Learning rate controls step size

## Types of Gradient Descent

### Batch Gradient Descent

Uses ALL training examples to compute gradients:

```
θ = θ - α * (1/n) * Σ ∇L(x_i, y_i; θ)
```

| Aspect      | Value                          |
| ----------- | ------------------------------ |
| Stability   | High - smooth updates          |
| Speed       | Slow - full dataset per update |
| Memory      | High - load all data           |
| Convergence | Guaranteed for convex          |

### Stochastic Gradient Descent (SGD)

Uses ONE example per update:

```
for each (x_i, y_i):
    θ = θ - α * ∇L(x_i, y_i; θ)
```

| Aspect      | Value                     |
| ----------- | ------------------------- |
| Stability   | Low - noisy updates       |
| Speed       | Fast per update           |
| Memory      | Low - one example         |
| Convergence | Oscillates around minimum |

### Mini-Batch Gradient Descent

Uses a subset (batch) of examples:

```
for each batch B:
    θ = θ - α * (1/|B|) * Σ ∇L(x_i, y_i; θ)
```

| Aspect      | Value                          |
| ----------- | ------------------------------ |
| Stability   | Medium - balanced              |
| Speed       | Efficient GPU utilization      |
| Memory      | Moderate - batch_size examples |
| Convergence | Good with momentum             |

**This is the standard approach in deep learning!**

## Learning Rate

### Effect of Learning Rate

| Learning Rate | Effect                          |
| ------------- | ------------------------------- |
| Too small     | Slow convergence, may get stuck |
| Just right    | Smooth convergence to minimum   |
| Too large     | Overshooting, divergence        |

### Learning Rate Schedules

1. **Step Decay**: Reduce by factor every N epochs
2. **Exponential Decay**: α = α_0 \* e^(-kt)
3. **Cosine Annealing**: Smooth oscillation between bounds
4. **Warmup**: Start small, increase, then decay

## Common Terms

### Epoch

One pass through the entire training dataset.

### Iteration

One parameter update (one batch processed).

### Batch Size

Number of samples per gradient computation.

```
iterations_per_epoch = dataset_size / batch_size
```

## Momentum

### Basic Momentum

Accelerates convergence by accumulating past gradients:

```
v = β*v - α*∇L(θ)
θ = θ + v
```

- β: Momentum coefficient (typically 0.9)
- v: Velocity (accumulated gradient)
- Dampens oscillations, accelerates in consistent direction

### Nesterov Momentum

"Look ahead" before computing gradient:

```
θ_ahead = θ + β*v
v = β*v - α*∇L(θ_ahead)
θ = θ + v
```

- Often faster convergence than standard momentum

## Challenges in Optimization

### Local Minima

- Less problematic in high dimensions
- Many saddle points instead

### Saddle Points

- Gradient is zero but not a minimum
- Common in high-dimensional spaces
- SGD noise helps escape

### Plateaus

- Flat regions with near-zero gradients
- Slow training progress
- Momentum helps traverse

## Summary

- Gradient descent updates parameters opposite to gradient
- Mini-batch is standard: balances stability and efficiency
- Learning rate is critical: too small = slow, too large = unstable
- Momentum accelerates convergence and dampens oscillations
- Modern optimizers (Adam, etc.) build on these foundations
