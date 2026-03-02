# Stochastic Gradient Descent - Summary

## Key Definitions and Concepts

- **Stochastic Gradient Descent (SGD)**: An optimization method that approximates the true gradient using a single training sample at each iteration, enabling efficient large-scale optimization.

- **Unbiased Estimator**: The stochastic gradient g(w; xᵢ, yᵢ) satisfies E[g(w; x, y)] = ∇L(w), ensuring that on average we move in the correct direction toward the optimum.

- **Mini-Batch Gradient Descent**: A variant using small batches (typically 32-256 samples) to balance gradient estimate quality with computational efficiency.

- **Learning Rate Scheduling**: Strategies for adjusting the learning rate over time, including constant, decaying, and adaptive methods.

- **Momentum**: A technique that accumulates gradient history to accelerate convergence and dampen oscillations.

## Important Formulas and Theorems

- **SGD Update Rule**: wₜ₊₁ = wₜ - ηₜ · g(wₜ; xᵢₜ, yᵢₜ)

- **Robbins-Monro Conditions**: Σₜ ηₜ = ∞ and Σₜ ηₜ² < ∞ ensure convergence.

- **Convergence Rates**: Batch GD: O(1/T) for strongly convex; SGD: O(1/√T) in expectation.

- **Momentum Update**: vₜ₊₁ = γvₜ + ηₜg(wₜ), wₜ₊₁ = wₜ - vₜ₊₁

## Key Points

- SGD computes gradients using single samples rather than the entire dataset, reducing per-iteration cost from O(nd) to O(d).

- The noise in gradient estimates can help escape shallow local minima, potentially improving generalization.

- Learning rate selection critically impacts convergence—a too-large rate causes divergence, too-small rate causes slow convergence.

- Mini-batch SGD is the most commonly used variant in practice, balancing stability and efficiency.

- Momentum with γ = 0.9 is the standard choice, providing significant speedup over vanilla SGD.

- For convex problems, SGD converges to the global optimum under appropriate conditions.

- SGD enables online learning, where the model continuously updates as new data arrives.

## Common Mistakes to Avoid

- Using a constant learning rate that is too large, causing oscillations or divergence instead of convergence.

- Failing to properly shuffle data between epochs, leading to biased gradient estimates and poor convergence.

- Confusing the expected stochastic gradient with the actual gradient at each iteration—the expectation is what matters theoretically.

- Applying SGD to non-convex problems without understanding that convergence guarantees differ significantly.

## Revision Tips

- Practice deriving SGD updates for different loss functions—linear regression squared loss and logistic regression cross-entropy loss are essential.

- Work through numerical examples by hand to build intuition about how SGD progresses toward the optimum.

- Memorize the convergence rate comparisons between batch GD and SGD, as this frequently appears in exams.

- Review the relationship between batch size, gradient variance, and convergence stability to understand mini-batch sizing trade-offs.