# Feedforward Networks Optimization

## Introduction
Feedforward neural networks form the foundation of modern deep learning systems. These networks process information in a single direction from input to output layers through hidden units, enabling complex function approximation. Optimization of these networks refers to the process of adjusting weights and biases to minimize loss functions, a critical challenge in machine learning due to high-dimensional parameter spaces and non-convex optimization landscapes.

Effective optimization enables networks to learn hierarchical representations from data, making them essential for tasks like image classification (ResNet), speech recognition (WaveNet), and natural language processing (Transformer architectures). Current research focuses on overcoming local minima, addressing vanishing/exploding gradients, and improving convergence rates through advanced optimization algorithms.

The importance of optimization extends beyond basic network training. Recent developments in neural architecture search (NAS) and meta-learning require sophisticated optimization strategies. For DU MSc CS students, understanding these mechanisms is crucial for both implementing standard models and conducting original research in deep learning.

## Key Concepts
1. **Gradient Descent Variants**:
   - Stochastic Gradient Descent (SGD): Updates weights using mini-batch gradients
   - Momentum: Accumulates velocity vectors to escape local minima
   - Adam: Combines adaptive learning rates with momentum (β₁=0.9, β₂=0.999)
   - Adagrad: Adapts learning rates per-parameter

2. **Activation Function Considerations**:
   - ReLU vs. Leaky ReLU: Trade-offs in dead neuron problem
   - Swish (x·sigmoid(βx)): Smooth non-monotonic activation from Google Brain
   - Gradient Preservation: How activation choices affect backpropagation

3. **Regularization Techniques**:
   - L1/L2 Regularization: Weight penalty terms
   - Dropout (Srivastava et al.): Random neuron deactivation
   - Early Stopping: Monitoring validation loss curves

4. **Weight Initialization**:
   - Xavier/Glorot: Variance scaling for sigmoid activations
   - He Initialization: Optimized for ReLU networks

5. **Batch Normalization**:
   - Reduces internal covariate shift by normalizing layer inputs
   - Enables higher learning rates and acts as regularizer

## Examples

**Example 1: Implementing Momentum SGD**
```python
# Hyperparameters
learning_rate = 0.01
momentum = 0.9
velocity = 0

# Update rule
for param, grad in network.gradients():
    velocity = momentum * velocity - learning_rate * grad
    param += velocity
```
*Analysis*: Momentum helps accelerate gradients in relevant directions while dampening oscillations, particularly useful in ravines of loss landscapes.

**Example 2: ReLU vs. Sigmoid in MNIST Classification**
A 3-layer network with ReLU achieves 98% test accuracy in 10 epochs vs. 95% with sigmoid. ReLU's sparse activation prevents gradient saturation in deep layers.

**Example 3: Dropout Regularization**
```python
keras.Sequential([
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])
```
Dropout probability of 0.5 forces network to learn redundant representations, reducing overfitting on CIFAR-10 by 12% compared to baseline.

## Exam Tips
1. Derive weight update rules for Adam optimizer from first principles
2. Compare convergence properties of SGD vs. Adam on non-convex landscapes
3. Analyze gradient flow through tanh vs. swish activations using chain rule
4. Explain how batch normalization enables higher learning rates mathematically
5. Discuss recent research on optimization: Lookahead (2019), Lion (2023)
6. Solve weight initialization problems using He/Xavier formulae
7. Interpret learning curves to diagnose underfitting/overfitting

Length: 2500 words, MSc CS (research-oriented) postgraduate level