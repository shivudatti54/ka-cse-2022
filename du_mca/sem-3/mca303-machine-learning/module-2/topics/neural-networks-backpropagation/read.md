# Neural Networks & Backpropagation

## Introduction
Neural networks are computational models inspired by biological neural systems, capable of learning complex patterns through layered transformations of data. At the core of modern machine learning, they power breakthroughs in image recognition (CNNs), sequence modeling (RNNs), and transformer-based architectures. Backpropagation is the foundational algorithm for training neural networks by efficiently computing gradients through the chain rule of calculus.

The importance of this topic lies in its universal applicability across AI domains. From recommendation systems to autonomous vehicles, neural networks require precise understanding of forward/backward passes, activation functions, and optimization mechanics. For DU MCA students, mastering these concepts is critical for implementing deep learning solutions and contributing to India's growing AI industry.

## Key Concepts
1. **Network Architecture**: 
   - Input/Hidden/Output layers with learnable weights (θ)
   - Fully connected vs specialized layers (convolutional, recurrent)
   - Activation functions: Sigmoid, ReLU, Softmax

2. **Forward Propagation**:
   - Computation: zⁱ = Wⁱaⁱ⁻¹ + bⁱ  
   - Activation: aⁱ = σ(zⁱ)
   - Loss functions: MSE, Cross-Entropy

3. **Backpropagation Algorithm**:
   - Chain rule: ∂L/∂Wⁱ = (∂L/∂aⁱ) ⊙ σ'(zⁱ) · aⁱ⁻¹ᵀ
   - Gradient computation from output to input layers
   - Batch vs stochastic gradient descent

4. **Optimization**:
   - Learning rate (α) and momentum
   - Regularization: L2, Dropout
   - Vanishing/exploding gradients

## Examples

**Example 1: XOR Problem with 2-Layer Network**
```
Input: X = [[0,0],[0,1],[1,0],[1,1]]
Target: y = [0,1,1,0]

Forward Pass:
h1 = ReLU(W1·x + b1)
y_pred = Sigmoid(W2·h1 + b2)

Backward Pass:
Compute ∂L/∂W2 = (y_pred - y) * h1
∂L/∂W1 = (∂L/∂h1) * x where ∂L/∂h1 = (y_pred - y) * W2 ⊙ ReLU'(h1)
Update weights: W := W - α·∂L/∂W
```

**Example 2: MNIST Digit Classification**
```python
# TensorFlow implementation sketch
model = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),
    Dropout(0.2),
    Dense(10, activation='softmax')
])
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)
```

## Exam Tips
1. Always write dimensions of weight matrices (e.g., W¹ ∈ ℝ^{hidden×input})
2. Memorize derivatives of common activation functions:
   - ReLU: 1 if z>0 else 0
   - Sigmoid: σ(z)(1-σ(z))
3. For numerical stability, use logits with Cross-Entropy loss
4. Explain vanishing gradients in deep networks and solutions like residual connections
5. Practice computing gradients for 3-layer networks manually
6. Compare batch, mini-batch, and stochastic GD
7. Mention India-specific applications: Aadhaar biometrics, crop yield prediction