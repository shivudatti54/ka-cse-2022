# RMSprop and Adam Optimizers

## Table of Contents

- [RMSprop and Adam Optimizers](#rmsprop-and-adam-optimizers)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Gradient Descent Review](#gradient-descent-review)
  - [RMSprop (Root Mean Square Propagation)](#rmsprop-root-mean-square-propagation)
  - [Momentum in Optimization](#momentum-in-optimization)
  - [Adam (Adaptive Moment Estimation)](#adam-adaptive-moment-estimation)
  - [Comparison of Optimizers](#comparison-of-optimizers)
- [Examples](#examples)
  - [Example 1: RMSprop Update Computation](#example-1-rmsprop-update-computation)
  - [Example 2: Adam Optimizer Computation](#example-2-adam-optimizer-computation)
  - [Example 3: Choosing Between RMSprop and Adam](#example-3-choosing-between-rmsprop-and-adam)
- [Exam Tips](#exam-tips)

## Introduction

In the field of machine learning and deep learning, the choice of optimization algorithm plays a crucial role in determining how quickly and effectively a neural network learns. While basic gradient descent methods like Stochastic Gradient Descent (SGD) provide a foundation, they often suffer from issues such as slow convergence, oscillation in steep directions, and sensitivity to learning rate selection. This has led to the development of adaptive optimization algorithms that adjust learning rates dynamically based on the history of gradients.

RMSprop (Root Mean Square Propagation) and Adam (Adaptive Moment Estimation) are two of the most widely used adaptive optimization algorithms in modern neural network training. Both algorithms address the limitations of vanilla gradient descent by maintaining per-parameter learning rates that adapt based on the gradients observed during training. RMSprop, introduced by Geoffrey Hinton in his popular lecture notes, divides the learning rate by a running average of the magnitudes of recent gradients. Adam, on the other hand, combines the benefits of momentum (from AdaGrad and RMSprop) with adaptive learning rates, making it one of the most robust and popular optimizers in deep learning today.

Understanding these optimization algorithms is essential for CSE students as they form the backbone of modern neural network implementations. Whether training convolutional neural networks for image classification, recurrent neural networks for sequence modeling, or transformers for natural language processing, the choice between RMSprop and Adam can significantly impact training time, model performance, and generalization ability.

## Key Concepts

### Gradient Descent Review

Before diving into RMSprop and Adam, it is essential to understand the basic gradient descent update rule. In vanilla gradient descent, parameters are updated as:

**θ = θ - η × ∇J(θ)**

where θ represents the parameters, η is the learning rate, and ∇J(θ) is the gradient of the loss function with respect to parameters. This approach uses a single global learning rate for all parameters, which can be problematic when dealing with features that have different scales or when gradients vary significantly across different dimensions.

### RMSprop (Root Mean Square Propagation)

RMSprop addresses the problem of oscillating updates in directions with steep gradients by dividing the learning rate by a running average of the magnitudes of recent gradients. The key idea is to normalize the gradient by its root mean square, which effectively scales down large gradients and allows for larger updates in directions with smaller gradients.

The RMSprop algorithm maintains a running average of the squared gradients for each parameter. Let us denote the squared gradient cache as E[g²]. The update equations are:

**E[g²] = β × E[g²] + (1 - β) × (∇J)²**

**θ = θ - η/√(E[g²] + ε) × ∇J**

Here, β is the decay rate (typically set to 0.9), ε is a small constant (usually 10⁻⁸) to prevent division by zero, and the squared gradient (∇J)² is applied element-wise. The denominator √(E[g²] + ε) acts as an adaptive learning rate that shrinks for frequently occurring features (large gradients) and grows for rare features (small gradients).

### Momentum in Optimization

Momentum is a technique that accelerates gradient descent by accumulating a velocity vector in directions of persistent gradient descent. It helps dampen oscillations and speeds up convergence, especially in regions where the loss landscape has long, narrow valleys. The momentum update is:

**v = γ × v + η × ∇J**

**θ = θ - v**

where γ is the momentum coefficient (typically 0.9) and v is the velocity vector. Momentum can be viewed as a ball rolling down a hill—it gains speed in directions where gradients point consistently in the same direction.

### Adam (Adaptive Moment Estimation)

Adam combines the benefits of both RMSprop and momentum. It maintains two moving averages: the first moment (mean of gradients, acting like momentum) and the second moment (uncentered variance of gradients, similar to RMSprop). These are called "moments" because the first moment is the mean (related to momentum) and the second moment is related to the variance (uncentered second moment).

The Adam algorithm maintains:

**m = β₁ × m + (1 - β₁) × ∇J** (first moment estimate)
**v = β₂ × v + (1 - β₂) × (∇J)²** (second moment estimate)

Since m and v are initialized as zero vectors, they are biased toward zero, especially during the initial training steps when the decay rates are close to 1. To correct this bias, Adam applies bias correction:

**m̂ = m / (1 - β₁ᵗ)**
**v̂ = v / (1 - β₂ᵗ)**

where t is the iteration number. The parameter update becomes:

**θ = θ - η × m̂ / (√v̂ + ε)**

The default hyperparameter values recommended in the original Adam paper are β₁ = 0.9, β₂ = 0.999, and ε = 10⁻⁸. These values have proven effective across a wide range of problems.

### Comparison of Optimizers

**SGD** uses a fixed learning rate and can get stuck in local minima or converge slowly. **AdaGrad** adapts learning rates based on historical gradients but can prematurely reduce learning rates to near-zero for deep networks. **RMSprop** addresses AdaGrad's vanishing learning rate problem by using exponential moving averages of squared gradients. **Adam** combines momentum with adaptive learning rates, making it robust to the choice of hyperparameters and effective across various problems.

## Examples

### Example 1: RMSprop Update Computation

Consider a simple neural network with one parameter θ = 2.0, learning rate η = 0.01, decay rate β = 0.9, and gradient ∇J = 0.5 at iteration t = 1. Assume E[g²] is initialized to 0.

**Step 1: Update the squared gradient cache**

E[g²] = β × E[g²] + (1 - β) × (∇J)²
E[g²] = 0.9 × 0 + 0.1 × (0.5)² = 0.1 × 0.25 = 0.025

**Step 2: Compute the adaptive learning rate denominator**

√(E[g²] + ε) = √(0.025 + 10⁻⁸) ≈ √0.025 ≈ 0.1581

**Step 3: Update parameters**

θ_new = θ - (η/√(E[g²] + ε)) × ∇J
θ_new = 2.0 - (0.01/0.1581) × 0.5 = 2.0 - 0.0632 × 0.5 = 2.0 - 0.0316 = 1.9684

Notice how the effective learning rate (0.01/0.1581 ≈ 0.0632) is higher than the base rate because the gradient is relatively small. This adaptive scaling helps the optimizer navigate the loss landscape more effectively.

### Example 2: Adam Optimizer Computation

Now consider training with Adam optimizer at iteration t = 2 with parameters: θ = 1.5, learning rate η = 0.001, β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸. Let the current gradient be ∇J = 0.3. Assume m = 0.15 and v = 0.0225 from the previous iteration.

**Step 1: Update first moment estimate**

m_new = β₁ × m + (1 - β₁) × ∇J
m_new = 0.9 × 0.15 + 0.1 × 0.3 = 0.135 + 0.03 = 0.165

**Step 2: Update second moment estimate**

v_new = β₂ × v + (1 - β₂) × (∇J)²
v_new = 0.999 × 0.0225 + 0.001 × (0.3)² = 0.0224775 + 0.001 × 0.09 = 0.0224775 + 0.00009 = 0.0225675

**Step 3: Apply bias correction**

m̂ = m_new / (1 - β₁ᵗ) = 0.165 / (1 - 0.9²) = 0.165 / (1 - 0.81) = 0.165 / 0.19 ≈ 0.8684
v̂ = v_new / (1 - β₂ᵗ) = 0.0225675 / (1 - 0.999²) = 0.0225675 / (1 - 0.998001) = 0.0225675 / 0.001999 ≈ 11.29

**Step 4: Update parameters**

θ_new = θ - η × m̂ / (√v̂ + ε)
θ_new = 1.5 - 0.001 × 0.8684 / (√11.29 + 10⁻⁸)
θ_new = 1.5 - 0.0008684 / 3.3607 ≈ 1.5 - 0.0002584 = 1.4997

The bias correction becomes particularly important in early iterations when t is small, preventing the moments from being biased toward zero.

### Example 3: Choosing Between RMSprop and Adam

Suppose you are training a convolutional neural network for image classification on the CIFAR-10 dataset. Consider two scenarios:

**Scenario A:** Limited computational resources, need for interpretable training dynamics
**Solution:** Use RMSprop. RMSprop is computationally lighter than Adam because it only maintains one moving average (v) instead of two (m and v). It also provides more interpretable behavior since the effective learning rate can be directly observed through the cache values.

**Scenario B:** Fast convergence is critical, unsure about optimal learning rate
**Solution:** Use Adam with default hyperparameters. Adam's adaptive learning rates and momentum combination typically achieves good results without extensive hyperparameter tuning. The default learning rate of 0.001 works well for most problems.

## Exam Tips

1. **Understand the mathematical formulations:** Be able to write and explain the update equations for both RMSprop and Adam, including all hyperparameter notations (β, β₁, β₂, ε, η).

2. **Know the default hyperparameter values:** For RMSprop, β = 0.9. For Adam, β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸, and default learning rate η = 0.001.

3. **Explain bias correction in Adam:** Understand why bias correction is needed (m and v initialized to zero cause bias toward zero) and how the correction factor (1 - βᵗ) addresses this.

4. **Compare optimizer characteristics:** Be prepared to differentiate between SGD, AdaGrad, RMSprop, and Adam based on their learning rate adaptation strategies and momentum usage.

5. **Understand when to use which optimizer:** Adam is generally the default choice for most deep learning problems due to its robustness. RMSprop is preferred when memory is constrained or when interpretability is important.

6. **Know the role of epsilon (ε):** The small constant (usually 10⁻⁸) prevents division by zero in both RMSprop and Adam when the moving average of squared gradients is very small.

7. **Understand convergence behavior:** Adam typically converges faster than RMSprop, which converges faster than vanilla SGD. However, SGD with momentum can sometimes generalize better on certain problems.

8. **Be aware of learning rate schedules:** While adaptive optimizers reduce the need for manual learning rate tuning, using learning rate decay (like step decay or cosine annealing) can still improve final model performance.
