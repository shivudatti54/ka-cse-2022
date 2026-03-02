# Training CNNs and Hyperparameter Optimization - Summary

## Key Definitions and Concepts

- **Backpropagation**: Process of computing gradients of loss with respect to network parameters using chain rule, enabling weight updates via gradient descent
- **Cross-Entropy Loss**: Standard loss function for classification: L = -Σ(y_true × log(y_pred))
- **Adam Optimizer**: Adaptive moment estimation combining momentum with per-parameter learning rates (β₁=0.9, β₂=0.999)
- **Dropout**: Regularization technique randomly deactivating neurons during training with probability p
- **Batch Normalization**: Normalizes layer inputs using mini-batch statistics, with learnable γ (scale) and β (shift) parameters
- **Learning Rate**: Step size for weight updates during gradient descent—most critical hyperparameter

## Important Formulas and Theorems

- **Convolution Output Size**: floor((n + 2p - f)/s) + 1
- **SGD with Momentum**: v(t+1) = βv(t) + η∇L; w(t+1) = w(t) - v(t+1)
- **Adam Update**: w(t+1) = w(t) - η × m̂(t) / (√v̂(t) + ε)
- **L2 Regularization**: L_total = L_original + λΣw²
- **Batch Norm**: y = γ × (x - μ)/√(σ² + ε) + β

## Key Points

- CNN training involves iterative optimization minimizing loss through forward pass (prediction) and backward pass (gradient computation)
- Adam is typically the best default optimizer for CNN training tasks
- Batch Normalization stabilizes training, allows higher learning rates, and provides mild regularization
- Dropout should only be applied during training, not inference (or scale by dropout probability)
- Data augmentation is essential for limited datasets—geometric and color transforms expand training data
- Learning rate scheduling (step decay, cosine annealing) improves convergence
- Deeper networks require more regularization to prevent overfitting

## Common Mistakes to Avoid

- Forgetting to set model to training mode when using Dropout/BatchNorm during inference
- Using learning rates too high causing loss divergence or too low causing slow convergence
- Applying Batch Normalization after activation instead of before (standard practice)
- Not using cross-validation or validation data when tuning hyperparameters
- Assuming more layers always improves performance—deeper networks need more data

## Revision Tips

1. Practice deriving convolution output sizes for different padding, stride, and filter combinations
2. Memorize the Adam optimizer update equations with default hyperparameters
3. Review the order of layers in modern architectures: Conv → BatchNorm → ReLU → Pooling
4. Understand when to use each regularization technique based on dataset size and model complexity
5. Be prepared to sketch and explain learning curves showing effects of different hyperparameters