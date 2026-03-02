# Neural Networks & Backpropagation - Summary

## Key Definitions and Concepts
- **Perceptron**: Basic unit with weights and activation
- **Epoch**: One full pass through training data
- **Backpropagation**: Efficient gradient computation using reverse-mode autodiff
- **Vanishing Gradient**: Problem where lower-layer gradients become negligible

## Important Formulas and Theorems
- **Gradient Descent**: Wₜ₊₁ = Wₜ - α∇L(Wₜ)
- **Chain Rule**: ∂L/∂Wⁱ = ∂L/∂aᴸ · ∂aᴸ/∂zᴸ · ∂zᴸ/∂aᴸ⁻¹ ... ∂aⁱ/∂Wⁱ
- **Cross-Entropy Loss**: L = -Σ yᵢ log(ŷᵢ)
- **ReLU Derivative**: 1 if input >0 else 0

## Key Points
- Neural networks approximate complex functions through composition of layers
- Backpropagation computes gradients in O(N) time (vs O(N²) for numerical methods)
- Mini-batch GD balances noise reduction and computational efficiency
- Weight initialization (He/Xavier) prevents activation saturation
- Batch normalization accelerates convergence
- Dropout randomly deactivates neurons to prevent co-adaptation
- Adam optimizer combines momentum and adaptive learning rates

## Common Mistakes to Avoid
- Forgetting to apply activation function derivatives in backprop
- Using ReLU in final layer for classification tasks
- Initializing all weights to zero (causes symmetric gradients)
- Ignoring gradient clipping in RNNs

## Revision Tips
1. Practice manual gradient calculations for 3-layer networks
2. Implement a neural network from scratch using NumPy
3. Use TensorFlow Playground (tensorflow.org/playground) to visualize learning
4. Focus on hyperparameter tuning strategies for Indian datasets