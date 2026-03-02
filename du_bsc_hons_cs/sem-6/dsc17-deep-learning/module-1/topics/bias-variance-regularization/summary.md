# Bias-Variance Tradeoff and Regularization - Summary

## Key Definitions and Concepts

- **Bias:** Systematic error from overly simplistic model assumptions; causes underfitting
- **Variance:** Model sensitivity to training data fluctuations; causes overfitting
- **Underfitting:** High training error and high test error; model too simple
- **Overfitting:** Low training error but high test error; model too complex
- **Regularization:** Techniques to constrain model complexity and improve generalization

## Important Formulas and Theorems

- **Bias-Variance Decomposition:** Expected Error = Bias² + Variance + Irreducible Error
- **L1 Regularization (Lasso):** Loss + λ∑|wᵢ| — promotes sparsity
- **L2 Regularization (Ridge):** Loss + (λ/2)∑wᵢ² — shrinks weights toward zero
- **Dropout:** Randomly sets p fraction of neuron outputs to zero during training

## Key Points

- The bias-variance tradeoff is fundamental to understanding model generalization
- As model complexity increases, bias decreases but variance increases
- The optimal model complexity balances bias and variance at minimum total error
- L1 regularization can drive weights to exactly zero (feature selection)
- L2 regularization is more common in deep learning (weight decay)
- Dropout works by preventing co-adaptation of neurons
- Early stopping prevents overfitting by monitoring validation error
- Data augmentation increases effective training data size
- Batch normalization provides implicit regularization through mini-batch noise
- Regularization hyperparameter (λ) must be tuned appropriately

## Common Mistakes to Avoid

- Confusing bias with variance — they represent different types of errors
- Setting dropout rate too high during training can severely underfit the model
- Forgetting that dropout is disabled during inference/evaluation
- Using too strong regularization (large λ) which causes underfitting
- Not separating training, validation, and test sets for proper model selection

## Revision Tips

1. Memorize the bias-variance decomposition formula and understand each term's meaning
2. Practice identifying underfitting vs overfitting from training/test error curves
3. Remember the key difference: L1 promotes sparsity, L2 promotes shrinkage
4. Know that dropout applies during training only; inference uses all neurons
5. Review PyTorch/TensorFlow implementations of regularization techniques