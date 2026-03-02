# Stochastic Gradient Descent

## Introduction

In the realm of convex optimization and machine learning, gradient descent methods form the backbone of numerical optimization techniques. While batch gradient descent computes the gradient using the entire dataset before taking a single step, this approach becomes computationally prohibitive when dealing with massive datasets containing millions of samples. Stochastic Gradient Descent (SGD) addresses this fundamental challenge by approximating the true gradient using a single training example or a small batch of examples at each iteration.

Stochastic Gradient Descent represents a pivotal advancement in optimization theory, transforming how we approach large-scale machine learning problems. The method was popularized in the machine learning community through its effectiveness in training neural networks and support vector machines. Today, SGD and its variants power some of the most influential applications in computer science, including image classification, natural language processing, and recommendation systems.

The core intuition behind SGD lies in the observation that the expected value of the stochastic gradient approximates the true gradient under mild conditions. This theoretical foundation allows us to make progress toward the optimum even when we cannot compute the exact gradient. The noise introduced by this approximation, while seemingly a limitation, actually helps the optimizer escape shallow local minima, potentially leading to better generalization in machine learning contexts.

## Key Concepts

### The Optimization Problem

Consider the standard empirical risk minimization problem in machine learning. We have a training dataset of n samples: {(x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ)}. The objective is to find parameters w that minimize the average loss:

L(w) = (1/n) Σᵢ₌₁ⁿ ℓ(f(xᵢ, w), yᵢ)

where ℓ is the loss function and f is our prediction model. The gradient of this objective is:

∇L(w) = (1/n) Σᵢ₌₁ⁿ ∇ℓ(f(xᵢ, w), yᵢ)

For linear regression with squared loss, this becomes:

∇L(w) = (1/n) Xᵀ(Xw - y)

When n is extremely large (millions of samples), computing this gradient at each iteration becomes computationally expensive, requiring O(nd) operations where d is the number of features.

### The Stochastic Approximation

Instead of computing the gradient over all n samples, SGD selects a single sample (or a small mini-batch) at each iteration and computes the gradient using only that sample:

g(w; xᵢ, yᵢ) = ∇ℓ(f(xᵢ, w), yᵢ)

The update rule becomes:

wₜ₊₁ = wₜ - ηₜ · g(wₜ; xᵢₜ, yᵢₜ)

where ηₜ is the learning rate at iteration t, and (xᵢₜ, yᵢₜ) is the randomly selected sample for that iteration.

The key theoretical result is that E[g(w; x, y)] = ∇L(w), meaning the stochastic gradient is an unbiased estimator of the true gradient. This unbiasedness ensures that, on average, we move in the correct direction toward the optimum.

### Learning Rate Scheduling

The choice of learning rate significantly impacts SGD's convergence. Several scheduling strategies exist:

**Constant Learning Rate**: Using a fixed η throughout training. Simple but may not achieve optimal convergence.

**Decaying Learning Rate**: Reducing the learning rate over time using schedules such as:

- ηₜ = η₀ / (1 + λt) where λ is the decay rate
- ηₜ = η₀ · (0.95)^t
- Step decay: halving the learning rate every k epochs

**Adaptive Learning Rates**: Methods like AdaGrad, RMSProp, and Adam automatically adjust learning rates based on historical gradient information.

### Convergence Analysis

Under appropriate conditions, SGD converges to the global minimum for convex problems. The Robbins-Monro conditions ensure convergence:

1. Σₜ ηₜ = ∞ (learning rates sum to infinity, ensuring we can reach any point)
2. Σₜ ηₜ² < ∞ (learning rates are square-summable, ensuring variance goes to zero)

For strongly convex functions with Lipschitz gradients, SGD achieves O(1/√T) convergence in expectation, where T is the number of iterations. This can be improved to O(1/T) with appropriate step sizes for smooth functions.

### Mini-Batch Gradient Descent

A popular compromise between pure SGD and batch gradient descent uses small batches of 32 to 256 samples:

wₜ₊₁ = wₜ - ηₜ · (1/B) Σᵢ₌₁ᴮ ∇ℓ(f(xᵢₜ, w), yᵢₜ)

Mini-batches provide more stable gradient estimates than single-sample SGD while maintaining computational efficiency. The batch size B is a hyperparameter that balances gradient estimate quality against computational cost.

### Momentum

Momentum accelerates SGD by accumulating a velocity vector in directions of persistent gradient descent:

vₜ₊₁ = γvₜ + ηₜ · g(wₜ)

wₜ₊₁ = wₜ - vₜ₊₁

where γ ∈ [0, 1) is the momentum coefficient (typically 0.9). This technique helps dampen oscillations and speeds up convergence, especially in regions with high curvature.

## Examples

### Example 1: Linear Regression with SGD

Consider simple linear regression with data points (x, y) where we want to find w such that y ≈ wx. Using squared loss ℓ(ŷ, y) = (ŷ - y)², the gradient for a single sample (xᵢ, yᵢ) is:

g(w; xᵢ, yᵢ) = 2(wxᵢ - yᵢ)xᵢ

Given training data: {(1, 2), (2, 3), (3, 5)} and initial weight w₀ = 0, using learning rate η = 0.1:

Iteration 1: Sample (1, 2)
g = 2(0×1 - 2)×1 = -4
w₁ = 0 - 0.1(-4) = 0.4

Iteration 2: Sample (3, 5)
g = 2(0.4×3 - 5)×3 = 2(1.2 - 5)×3 = 2(-3.8)×3 = -22.8
w₂ = 0.4 - 0.1(-22.8) = 2.68

Iteration 3: Sample (2, 3)
g = 2(2.68×2 - 3)×2 = 2(5.36 - 3)×2 = 2(2.36)×2 = 9.44
w₃ = 2.68 - 0.1(9.44) = 1.736

Continuing this process converges toward the optimal slope that minimizes mean squared error across all points.

### Example 2: Logistic Regression Binary Classification

For binary classification with labels y ∈ {0, 1}, logistic regression uses the sigmoid function σ(z) = 1/(1 + e⁻ᶻ) and cross-entropy loss:

ℓ(ŷ, y) = -[y log(ŷ) + (1-y) log(1-ŷ)]

For parameters w and single sample (xᵢ, yᵢ), the gradient is:

g(w; xᵢ, yᵢ) = (σ(wᵀxᵢ) - yᵢ)xᵢ

With data points for two classes and initial weights w = [0, 0], learning rate η = 0.1, we compute gradients for each sampled point and update accordingly, gradually learning the decision boundary that separates the classes.

### Example 3: Comparing Batch GD vs SGD Convergence

Consider minimizing f(w) = w² starting from w₀ = 5. The true gradient is 2w.

**Batch Gradient Descent** (η = 0.1):
w₁ = 5 - 0.1(10) = 4
w₂ = 4 - 0.1(8) = 3.2
w₃ = 3.2 - 0.1(6.4) = 2.56

Converges smoothly to 0 in approximately 40 iterations.

**SGD with random sampling** (η = 0.1):
Using approximate stochastic gradients: g ≈ 2w + noise(σ=3)
w₁ = 5 - 0.1(10 + 2) = 3.8
w₂ = 3.8 - 0.1(7.6 - 1) = 3.34
w₃ = 3.34 - 0.1(6.68 + 3) = 2.67

SGD takes a noisier path but requires far less computation per iteration. For large n, the total computational cost to reach a given accuracy is often lower with SGD.

## Exam Tips

1. **Understand the Unbiased Estimator Property**: The key theoretical property of SGD is that E[∇ℓ(f(x,w), y)] = ∇L(w). This ensures convergence in expectation and is frequently tested in exams.

2. **Distinguish Between SGD, Mini-Batch, and Batch GD**: Know the trade-offs: batch GD provides accurate gradients but is slow for large datasets; SGD is fast but noisy; mini-batch balances both. Questions often ask for comparisons.

3. **Learning Rate Scheduling**: Be familiar with different learning rate decay strategies and the Robbins-Monro conditions for convergence. Understand why a constant learning rate may not converge.

4. **Convergence Rate Formulas**: Remember that batch GD achieves O(1/T) for strongly convex functions, while SGD achieves O(1/√T). This difference is crucial for theoretical questions.

5. **Momentum and Variants**: Understand how momentum accelerates convergence by accumulating velocity. Know the update equations for classical momentum and Nesterov accelerated gradient.

6. **Practical Advantages**: SGD's ability to escape local minima, handle large datasets efficiently, and enable online learning are important practical considerations often tested.

7. **Mathematical Formulation**: Be able to write the SGD update rule wₜ₊₁ = wₜ - ηₜ∇ℓ(wₜ; xᵢₜ, yᵢₜ) and explain each component's role.

8. **Relationship to Other Topics**: Connect SGD to the broader optimization landscape—understand how it relates to steepest descent (which becomes SGD in the stochastic setting) and when each method is appropriate.