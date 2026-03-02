# Deep Neural Networks - Summary

## Key Definitions and Concepts

- **Deep Neural Network (DNN):** A neural network with multiple hidden layers (typically 3+) that learns hierarchical representations from data through nonlinear transformations.

- **Perceptron:** The fundamental computational unit that computes a weighted sum of inputs plus bias, passed through an activation function.

- **Backpropagation:** The learning algorithm that computes gradients of the loss function with respect to network parameters using the chain rule, enabling efficient gradient descent training.

- **Activation Function:** A nonlinear function (sigmoid, tanh, ReLU) applied to the weighted sum that introduces nonlinearity, enabling the network to learn complex patterns.

- **Convolutional Neural Network (CNN):** A specialized architecture using convolutional layers with learnable filters for processing grid-structured data like images.

- **Recurrent Neural Network (RNN):** Architecture designed for sequential data that maintains hidden state to capture temporal dependencies.

- **Dropout:** A regularization technique that randomly deactivates neurons during training to prevent co-adaptation.

- **Batch Normalization:** A technique that normalizes layer inputs to stabilize training and accelerate convergence.

## Important Formulas and Theorems

- **Perceptron Output:** y = f(Σᵢ wᵢxᵢ + b) = f(w · x + b)

- **Sigmoid:** σ(z) = 1/(1 + e⁻ᶻ), derivative: σ'(z) = σ(z)(1 - σ(z))

- **ReLU:** f(z) = max(0, z), derivative: f'(z) = 1 if z > 0, else 0

- **Gradient Descent Update:** θₜ₊₁ = θₜ - η∇L(θₜ)

- **Momentum Update:** vₜ = γvₜ₋₁ + η∇L(θₜ); θₜ₊₁ = θₜ - vₜ

- **Adam Optimizer:** Combines adaptive learning rates with momentum for robust optimization

- **Chain Rule in Backprop:** ∂L/∂w = ∂L/∂a · ∂a/∂z · ∂z/∂w

## Key Points

- Deep neural networks automatically learn hierarchical feature representations from raw data, eliminating manual feature engineering.

- Network depth (adding more layers) enables learning of increasingly abstract features, but poses challenges like vanishing gradients—addressed by skip connections in ResNet.

- Activation functions introduce necessary nonlinearity; ReLU is the default choice due to computational efficiency and gradient preservation.

- Backpropagation enables efficient gradient computation through the network, making training tractable for networks with millions of parameters.

- Regularization is essential to prevent overfitting; dropout and batch normalization are standard techniques in modern architectures.

- CNNs excel at image tasks through local connectivity and parameter sharing; RNNs handle sequential data through recurrent connections.

- Transfer learning—using pre-trained models as starting points—has become standard practice due to data efficiency benefits.

## Common Mistakes to Avoid

- Using sigmoid activation in hidden layers causes vanishing gradients, severely limiting network depth and learning capability.

- Forgetting to set models to training mode when using dropout or batch normalization during inference leads to incorrect predictions.

- Not normalizing input data can cause slow convergence or training failure due to varying feature scales.

- Assuming deeper is always better: very deep networks suffer from degradation problems and increased computational cost without proper architectural design.

- Ignoring overfitting indicators like training loss continuing to decrease while validation loss increases—regularization must be applied appropriately.

## Revision Tips

1. Practice deriving backpropagation equations for simple networks manually to solidify understanding of gradient flow.

2. Implement a simple neural network from scratch (using NumPy only) to understand the complete training pipeline.

3. Study the AlexNet, ResNet, and Transformer architectures in detail—they frequently appear in exams as examples.

4. Review recent deep learning research papers (2019-2024) to understand current trends like large language models and multimodal learning.

5. Solve numerical problems involving gradient computations, parameter counting, and computational complexity analysis.