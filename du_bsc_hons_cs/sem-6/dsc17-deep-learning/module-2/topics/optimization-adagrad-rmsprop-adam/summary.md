# Optimization Algorithms: Adagrad, RMSprop, and Adam

## Introduction

In deep learning, optimization algorithms are used to minimize the loss function by updating model parameters (weights and biases). Traditional gradient descent uses a fixed learning rate for all parameters, which can be inefficient. Adaptive optimization algorithms adjust learning rates dynamically based on past gradients, improving convergence speed and performance. These algorithms are a crucial part of the Delhi University B.Sc. (Hons) Computer Science syllabus under Deep Learning (NEP 2024 UGCF).

---

## Adagrad (Adaptive Gradient Algorithm)

- **Key Idea**: Adapts the learning rate for each parameter based on the sum of squared gradients history.
- **Working**: Accumulates past squared gradients in a cache variable (G). Parameters with larger gradients get smaller updates, while those with smaller gradients get larger updates.
- **Advantages**:
  - Effective for sparse data
  - No manual tuning of learning rate required
- **Disadvantages**:
  - Learning rate monotonically decreases, which can cause premature convergence
  - Memory-intensive due to storing all past gradients
- **Update Formula**: θ(t+1) = θ(t) - (η / √(G + ε)) × g(t)

---

## RMSprop (Root Mean Square Propagation)

- **Key Idea**: Addresses Adagrad's diminishing learning rate problem by using a decaying average of squared gradients.
- **Working**: Maintains a moving average of squared gradients (E[g²]). The learning rate is divided by the square root of this average.
- **Advantages**:
  - Suitable for non-stationary objectives
  - Better convergence than Adagrad in practice
  - Effective for online and recurrent neural networks
- **Disadvantages**:
  - Requires tuning of decay parameter
  - Still has room for improvement with momentum
- **Hyperparameters**: Learning rate (η), decay rate (ρ typically 0.9)

---

## Adam (Adaptive Moment Estimation)

- **Key Idea**: Combines benefits of RMSprop (adaptive learning rates) and momentum. It maintains both first-moment (momentum) and second-moment (variance) estimates.
- **Working**:
  - First moment (m): moving average of gradients (like velocity)
  - Second moment (v): moving average of squared gradients (like adaptive learning rate)
  - Both are bias-corrected for accurate estimation in early training
- **Advantages**:
  - Most widely used optimizer in deep learning
  - Works well with default hyperparameters
  - Effective for noisy gradients and non-convex optimization
- **Disadvantages**:
  - Can converge to sharper minima
  - More computationally expensive than RMSprop
- **Hyperparameters**: Learning rate (η default 0.001), β1 (momentum, default 0.9), β2 (variance decay, default 0.999)

---

## Quick Comparison

| Algorithm | Learning Rate Adaptation | Momentum | Best Use Case |
|-----------|--------------------------|----------|---------------|
| Adagrad | Per-parameter (decreasing) | No | Sparse data |
| RMSprop | Per-parameter (decaying avg) | No | RNNs, online learning |
| Adam | Per-parameter with bias correction | Yes | General deep learning |

---

## Conclusion

Adagrad, RMSprop, and Adam are adaptive learning rate optimizers that significantly improve training efficiency in deep neural networks. **Adam** has become the default choice due to its robust performance, but understanding Adagrad and RMSprop is essential for comprehending the evolution of optimization techniques. These algorithms are fundamental for the Delhi University exam and practical deep learning implementations.

*Reference: Delhi University B.Sc. (Hons) CS NEP 2024 UGCF – Deep Learning Syllabus*