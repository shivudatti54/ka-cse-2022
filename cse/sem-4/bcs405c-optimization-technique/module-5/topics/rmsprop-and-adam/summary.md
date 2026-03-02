# RMSprop and Adam Optimizers - Summary

## Key Definitions and Concepts

- **RMSprop (Root Mean Square Propagation):** An adaptive learning rate optimization algorithm that divides the learning rate by the root mean square of recent gradients, effectively normalizing parameter updates based on gradient magnitudes.

- **Adam (Adaptive Moment Estimation):** An optimizer that combines momentum (first moment) with adaptive learning rates (second moment) by maintaining moving averages of both gradients and squared gradients.

- **Bias Correction:** A technique in Adam that corrects the initial bias of first and second moment estimates toward zero using the factor (1 - βᵗ).

- **Exponential Moving Average:** A method used in both RMSprop and Adam to give more weight to recent gradients while gradually forgetting older gradient information.

## Important Formulas and Theorems

**RMSprop Update:**

- E[g²] = β × E[g²] + (1 - β) × (∇J)²
- θ = θ - η × ∇J / √(E[g²] + ε)

**Adam Update:**

- m = β₁ × m + (1 - β₁) × ∇J (first moment)
- v = β₂ × v + (1 - β₂) × (∇J)² (second moment)
- m̂ = m / (1 - β₁ᵗ), v̂ = v / (1 - β₂ᵗ) (bias correction)
- θ = θ - η × m̂ / (√v̂ + ε)

## Key Points

- RMSprop uses only the second moment (squared gradients) for adaptation, while Adam uses both first moment (momentum) and second moment.

- Default hyperparameters: RMSprop uses β = 0.9; Adam uses β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸, η = 0.001.

- Adam includes bias correction to address the zero-initialization bias of moment estimates.

- The ε term (10⁻⁸) prevents division by zero when gradients are very small.

- Adam combines benefits of both AdaGrad (handles sparse gradients) and RMSprop (handles non-stationary gradients).

- Adam typically requires less hyperparameter tuning than SGD or RMSprop.

- RMSprop is computationally lighter than Adam due to maintaining fewer moving averages.

## Common Mistakes to Avoid

- Forgetting to apply bias correction in Adam, especially in early iterations when t is small.

- Using the same learning rate for Adam as for SGD—Adam's default learning rate of 0.001 is typically appropriate.

- Confusing the squared gradient operation (element-wise square) with the square root in the denominator.

- Not understanding that β decay rates are typically close to 1 (0.9-0.999), meaning older gradients have less influence.

## Revision Tips

1. Practice deriving parameter updates by hand for both RMSprop and Adam with simple numerical examples.

2. Create a comparison table of SGD, AdaGrad, RMSprop, and Adam covering their learning rate adaptation, momentum usage, and computational complexity.

3. Remember that Adam's name comes from "Adaptive Moment Estimation"—the first moment (mean) provides momentum, and the second moment (variance) provides adaptive learning rates.

4. Focus on understanding why bias correction is necessary—it compensates for the initial zero initialization of moment vectors.

5. Review the role of ε (epsilon) as a small constant preventing numerical instability in division operations.
