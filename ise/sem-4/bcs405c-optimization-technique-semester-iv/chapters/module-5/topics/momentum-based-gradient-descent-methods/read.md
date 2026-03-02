# Gradient Descent Methods

## Introduction to Gradient Descent

Gradient Descent is a first-order iterative optimization algorithm used to find a **local minimum** of a differentiable function. The core idea is to take repeated steps in the **opposite direction of the gradient** (or approximate gradient) of the function at the current point, because this is the direction of steepest descent.

In the context of Non-Linear Programming for unconstrained optimization, Gradient Descent is a fundamental method for minimizing an objective function `f(x)` where `x` is a vector of parameters. It is widely used in machine learning, data science, and various engineering fields due to its simplicity and effectiveness, especially with high-dimensional problems.

## Mathematical Foundation

### The Gradient Vector

The gradient of a scalar-valued multivariate function `f(x)`, denoted by `∇f(x)`, is a vector of its partial derivatives. For a function `f(x₁, x₂, ..., xₙ)`, the gradient is:

`∇f(x) = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ`

This vector points in the direction of the **steepest ascent** of the function at point `x`. Consequently, the negative gradient, `-∇f(x)`, points in the direction of the **steepest descent**.

### The Basic Update Rule

The fundamental step of the Gradient Descent algorithm is the parameter update. Starting from an initial guess `x⁽⁰⁾`, the parameters are updated iteratively using the following rule:

`x⁽ᵏ⁺¹⁾ = x⁽ᵏ⁾ - η⁽ᵏ⁾ ∇f(x⁽ᵏ⁾)`

Where:

- `x⁽ᵏ⁾` is the parameter vector at iteration `k`.
- `η⁽ᵏ⁾` (eta) is the **learning rate** or **step size** at iteration `k`.
- `∇f(x⁽ᵏ⁾)` is the gradient of the objective function evaluated at `x⁽ᵏ⁾`.

### Conceptual Example in 1D

Consider a simple convex function in one variable, `f(x) = (x-3)² + 1`. Its gradient (derivative) is `f'(x) = 2(x-3)`.

Let's minimize this function starting from `x⁽⁰⁾ = 0` with a fixed learning rate `η = 0.1`.

1.  **Iteration 1 (k=0):**
    - `x⁽⁰⁾ = 0`
    - `f'(0) = 2(0-3) = -6`
    - Update: `x⁽¹⁾ = 0 - (0.1 * -6) = 0.6`

2.  **Iteration 2 (k=1):**
    - `x⁽¹⁾ = 0.6`
    - `f'(0.6) = 2(0.6-3) = -4.8`
    - Update: `x⁽²⁾ = 0.6 - (0.1 * -4.8) = 1.08`

This process continues, with each step moving `x` closer to the minimum at `x=3`. The following ASCII art visualizes the first few steps:

```
Initial point (x0)
  |
  V
f(x) |         .*
     |        .   *
     |       .       *
     |      .           *
     |     . . . . . . . . * . . .> x
     |          |  |  |
     |        x0 x1 x2
     +-----------------------------
     0        1.0       2.0       3.0
```

## The Learning Rate (Step Size)

The learning rate `η` is the most critical **hyperparameter** in the Gradient Descent algorithm. It determines the size of the steps we take towards the minimum.

- **Too Small (`η`):** The algorithm will require many iterations to converge, making it very slow.
  ```
  Path with small η: x0 --- x1 --- x2 --- x3 --- x4 ... (slow convergence)
  ```
- **Too Large (`η`):** The algorithm can overshoot the minimum, causing it to diverge or oscillate around the minimum without converging.
  ```
  Path with large η: x0 --------> x1 (overshoot) <------- x2 (oscillation)
  ```
- **Optimal (`η`):** The algorithm converges efficiently to the minimum with a reasonable number of steps.

### Adaptive Learning Rates

To address the challenge of choosing a fixed `η`, several strategies use an adaptive learning rate that changes during training:

- **Time-Based Decay:** `η⁽ᵏ⁾ = η / (1 + decay * k)`
- **Step Decay:** Reduce `η` by a factor every few epochs.
- **Exponential Decay:** `η⁽ᵏ⁾ = η * exp^(-decay * k)`

## Variants of Gradient Descent

There are three main variants of Gradient Descent, differentiated by the amount of data used to compute the gradient.

### 1. Batch Gradient Descent (Vanilla)

This is the original version. It uses the **entire training dataset** to compute the gradient of the objective function for each iteration.

- **Advantage:** Since it uses the full dataset, it provides a stable convergence path and a clear error gradient.
- **Disadvantage:** It can be very slow and computationally expensive for large datasets, as it requires calculating the gradient for the entire dataset for a single update.

**Update Rule:** `x⁽ᵏ⁺¹⁾ = x⁽ᵏ⁾ - η ∇f(x⁽ᵏ⁾)` where `∇f(x)` is computed over all data points.

### 2. Stochastic Gradient Descent (SGD)

SGD performs a parameter update for **each individual training example** `x⁽ⁱ⁾`.

- **Advantage:** Much faster than Batch GD, especially on large datasets. The frequent updates create a noisy, random process that can help escape shallow local minima.
- **Disadvantage:** The noise in the updates can cause the convergence path to be highly erratic. It may never settle exactly at the minimum but oscillate around it.

**Update Rule:** `x⁽ᵏ⁺¹⁾ = x⁽ᵏ⁾ - η ∇fᵢ(x⁽ᵏ⁾)` where `∇fᵢ(x)` is the gradient for a single, randomly chosen data point `i`.

```
SGD Path ASCII:
f(x) |   *     .     .     .
     |     .     .     *     .
     |  .     *     .     .
     |    .     .     *     .
     | .     .     .     *
     +-------------------------> x
```

### 3. Mini-Batch Gradient Descent

This is a hybrid approach that splits the training dataset into small batches (e.g., 32, 64, 128 examples). It performs an update for **each mini-batch**.

- **Advantage:** Reduces the variance of the parameter updates compared to SGD, leading to more stable convergence. It leverages optimized matrix operations for faster computation on hardware like GPUs.
- **Disadvantage:** Introduces a new hyperparameter: the batch size.

**Update Rule:** `x⁽ᵏ⁺¹⁾ = x⁽ᵏ⁾ - η ∇f_B(x⁽ᵏ⁾)` where `∇f_B(x)` is the gradient computed over a mini-batch `B`.

### Comparison of Variants

| Feature                     | Batch GD       | Stochastic GD | Mini-Batch GD    |
| :-------------------------- | :------------- | :------------ | :--------------- |
| **Accuracy of Gradient**    | High           | Low           | Medium           |
| **Convergence Speed**       | Slow           | Fast          | Very Fast        |
| **Computational Cost**      | High per epoch | Low per epoch | Medium per epoch |
| **Memory Usage**            | High           | Low           | Medium           |
| **Noise in Updates**        | None           | High          | Medium           |
| **Suitable for Large Data** | No             | Yes           | Yes              |

## Convergence and Stopping Criteria

Gradient Descent iterates until it reaches a stopping criterion. Common criteria include:

1.  **Maximum Iterations:** Stop after a predefined number of iterations `k_max`.
2.  **Tolerance in Function Value:** Stop when the change in the objective function value is sufficiently small: `|f(x⁽ᵏ⁺¹⁾) - f(x⁽ᵏ⁾)| < ε`.
3.  **Tolerance in Parameter Change:** Stop when the norm of the parameter update is sufficiently small: `||x⁽ᵏ⁺¹⁾ - x⁽ᵏ⁾|| < ε`.
4.  **Gradient Magnitude:** Stop when the norm of the gradient is close to zero (a necessary condition for a minimum): `||∇f(x⁽ᵏ⁾)|| < ε`.

## Challenges and Mitigations

### 1. Local Minima and Saddle Points

- **Problem:** In non-convex functions, GD can get stuck in a local minimum or a saddle point (where the gradient is zero but it is not a minimum).
- **Mitigation:** The inherent noise in Stochastic GD helps it to jump out of shallow local minima and saddle points. Momentum-based methods (discussed next) also help with this.

### 2. Ill-Conditioning and Ravines

- **Problem:** If the curvature of the loss surface is much steeper in one dimension than in another (a "ravine"), standard GD will oscillate across the slopes while making slow progress down the valley.
- **Mitigation:** Momentum and adaptive learning rate methods (like AdaGrad, RMSProp, Adam) are designed to handle this.

## Enhancements: Momentum

Momentum helps accelerate Gradient Descent in the relevant direction and dampens oscillations. It does this by adding a fraction `γ` (gamma) of the previous update vector to the current update.

**Update with Momentum:**

```
v⁽ᵏ⁺¹⁾ = γ v⁽ᵏ⁾ + η ∇f(x⁽ᵏ⁾)
x⁽ᵏ⁺¹⁾ = x⁽ᵏ⁾ - v⁽ᵏ⁺¹⁾
```

Where `v` is the velocity vector, initially zero. The momentum term `γ` (typically 0.9) smooths the update path.

```
Path without Momentum: x0 -> x1 -> x2 -> x3 (oscillatory)
Path with Momentum:    x0 --------> x2 --------> x4 (smoother, faster)
```

## Exam Tips

1.  **Understand the Core Update Rule:** Be able to write and explain the update rule `x = x - η ∇f(x)`. It is the foundation of all variants.
2.  **Learning Rate is Key:** Always discuss the implications of the learning rate choice—too small, too large, and just right. This shows deep understanding.
3.  **Compare and Contrast Variants:** Be prepared to create a table or write a paragraph comparing Batch, Stochastic, and Mini-Batch GD. Mention computational efficiency, noise, and convergence behavior.
4.  **Know the Stopping Criteria:** List the common ways to decide when to stop the algorithm. The gradient magnitude criterion is particularly important theoretically.
5.  **Momentum Concept:** Understand how momentum works conceptually. You don't always need to derive the equations, but you should be able to explain why it leads to faster and smoother convergence.
6.  **Link to Broader Context:** Remember that Gradient Descent is a tool for **Unconstrained Optimization** within Non-Linear Programming. Be ready to contrast it with methods for constrained optimization (like KKT) or second-order methods (like Newton's Method).
