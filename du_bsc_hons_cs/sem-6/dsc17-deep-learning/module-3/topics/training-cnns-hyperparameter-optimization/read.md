# Training CNNs and Hyperparameter Optimization

## Introduction

Convolutional Neural Networks (CNNs) have revolutionized computer vision and image classification tasks, powering applications from facial recognition systems to autonomous vehicles. However, building an effective CNN requires more than just architectural design—it demands careful attention to the training process and strategic optimization of hyperparameters. This topic covers the essential techniques for training CNNs effectively and systematically tuning hyperparameters to achieve optimal model performance.

For University of Delhi Computer Science students preparing for semester examinations, understanding these concepts is crucial as they form the foundation of modern deep learning applications. The training process involves iterative optimization, where the network learns to minimize prediction errors through backpropagation, while hyperparameter optimization ensures that the model achieves its full potential without overfitting or underfitting.

## Key Concepts

### 1. Training CNNs: The Backpropagation Process

Training a CNN involves forward propagation, loss computation, and backpropagation. In forward propagation, input images pass through convolutional layers, pooling layers, and fully connected layers to produce predictions. The network's output is compared with ground truth labels using a loss function, typically **cross-entropy loss** for classification tasks:

**L = -Σ(y_true × log(y_pred))**

During backpropagation, gradients of the loss with respect to each parameter are computed using the chain rule. These gradients flow backward through the network, updating weights via gradient descent. The update rule for a weight w at iteration t is:

**w(t+1) = w(t) - η × ∂L/∂w**

where η represents the learning rate.

### 2. Optimization Algorithms

**Stochastic Gradient Descent (SGD)** updates parameters using mini-batches of training data, introducing noise that can help escape local minima. **Momentum** accelerates convergence by accumulating past gradients:

**v(t+1) = β × v(t) + η × ∂L/∂w**
**w(t+1) = w(t) - v(t+1)**

where β (typically 0.9) is the momentum coefficient.

**Adam (Adaptive Moment Estimation)** combines momentum with adaptive learning rates for each parameter. It maintains running averages of gradients (first moment) and squared gradients (second moment):

**m(t+1) = β₁ × m(t) + (1-β₁) × g**
**v(t+1) = β₂ × v(t) + (1-β₂) × g²**
**w(t+1) = w(t) - η × m(t+1) / (√v(t+1) + ε)**

where g is the gradient, ε (10⁻⁸) prevents division by zero, and β₁ = 0.9, β₂ = 0.999 are typical defaults.

### 3. Regularization Techniques

**Dropout** randomly deactivates neurons during training with probability p (typically 0.5 for hidden layers), preventing co-adaptation of neurons:

**During training:** y = f(Wx) × mask(where mask ~ Bernoulli(p))
**During inference:** y = f(Wx) × p (or use inverted dropout)

**L2 Regularization (Weight Decay)** adds a penalty term to the loss:
**L_total = L_original + λ × Σw²**

where λ (typically 0.0001 to 0.001) controls regularization strength.

### 4. Batch Normalization

Batch Normalization normalizes activations within each mini-batch, reducing internal covariate shift:

**μ_B = (1/B) × Σx_i**
**σ²_B = (1/B) × Σ(x_i - μ_B)²**
**x̂_i = (x_i - μ_B) / √(σ²_B + ε)**
**y_i = γ × x̂_i + β**

where γ (scale) and β (shift) are learnable parameters. This allows higher learning rates and acts as a regularizer.

### 5. Data Augmentation

Data augmentation artificially expands the training dataset by applying transformations:

- **Geometric transformations:** rotation, flipping, scaling, cropping
- **Color augmentation:** brightness, contrast, saturation adjustments
- **Advanced techniques:** mixup, cutout, random erasing

### 6. Hyperparameter Optimization

**Learning Rate** is the most critical hyperparameter. Too high causes divergence, too low leads to slow convergence. **Learning Rate Scheduling** adapts it during training:

- **Step decay:** reduce by factor every N epochs
- **Exponential decay:** lr = lr₀ × e^(-kt)
- **Cosine annealing:** lr = lr_min + 0.5 × (lr_max - lr_min) × (1 + cos(π × t/T))

**Batch Size** affects training stability and generalization. Larger batches (256-1024) provide accurate gradient estimates but may generalize worse. Smaller batches (16-64) introduce noise that aids generalization.

**Network Architecture Hyperparameters:**
- Number of convolutional layers (typically 3-19)
- Number of filters (typically 32, 64, 128, 256, 512)
- Filter size (1×1, 3×3, 5×5, 7×7)
- Pooling strategy (max pooling, average pooling, strided convolutions)
- Dropout rate (0.1-0.5)

**Search Strategies:**
- **Grid Search:** exhaustive search over predefined values
- **Random Search:** random sampling, often more efficient
- **Bayesian Optimization:** builds probabilistic model for efficient search

## Examples

### Example 1: Computing a Convolution Layer Forward Pass

Given an input image of size 5×5 with values, a 3×3 filter with stride 1 and no padding:

Input:
```
[[1, 2, 3, 4, 5],
 [2, 3, 4, 5, 6],
 [3, 4, 5, 6, 7],
 [4, 5, 6, 7, 8],
 [5, 6, 7, 8, 9]]
```

Filter (3×3, all ones):
```
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
```

**Solution:** With valid padding (no padding) and stride 1, output size = (5-3+1) × (5-3+1) = 3×3

First output element (position [0,0]): 1×1 + 1×2 + 1×3 + 1×2 + 1×3 + 1×4 + 1×3 + 1×4 + 1×5 = 27

Complete output:
```
[[27, 33, 39],
 [39, 45, 51],
 [51, 57, 63]]
```

### Example 2: Backpropagation Through Max Pooling

Given gradient from next layer: dL/dy = [[1, 2], [3, 4]] for a 2×2 max pooling with stride 2 on 4×4 input:

**Solution:** For max pooling, gradients pass only through the position with maximum value.

If input was:
```
[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]]
```

Max pooling selects: 6 (top-left quadrant max), 8 (top-right), 14 (bottom-left), 16 (bottom-right)

Gradient assignment:
```
[[0, 0, 0, 0],
 [0, 1, 0, 2],
 [0, 0, 0, 0],
 [0, 3, 0, 4]]
```

### Example 3: Computing Batch Normalization

Given mini-batch with values: [2, 4, 6, 8], γ = 2, β = 1, ε = 0.01

**Solution:**

μ_B = (2+4+6+8)/4 = 5
σ²_B = [(2-5)² + (4-5)² + (6-5)² + (8-5)²]/4 = 5
σ_B = √5 ≈ 2.236

Normalized values:
x̂ = [(2-5)/2.236, (4-5)/2.236, (6-5)/2.236, (8-5)/2.236]
x̂ ≈ [-1.342, -0.447, 0.447, 1.342]

Output: y = γ × x̂ + β = 2 × x̂ + 1
y ≈ [-1.684, 0.106, 1.894, 3.684]

## Exam Tips

1. **Remember the backpropagation chain rule** for CNNs: gradients flow through convolutions, pooling, and fully connected layers differently—focus on understanding how each layer type propagates gradients.

2. **Differentiate between regularization techniques**: Dropout during training vs. inference, L2 penalty on weights, Batch Norm as implicit regularizer—know when and how each applies.

3. **Adam optimizer defaults**: Remember β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸ as standard hyperparameters for Adam in most frameworks.

4. **Output size formula**: For convolution with padding p, filter size f, stride s on input size n:
   Output = floor((n + 2p - f)/s) + 1

5. **Trade-offs matter**: Larger batch sizes train faster but may generalize worse; higher dropout reduces overfitting but can cause underfitting; deeper networks capture more features but require more data.

6. **Batch Normalization placement**: Typically placed after convolution and before activation function (Conv → BN → ReLU is common).

7. **Learning rate impact**: Sketch learning curves showing underfitting (high loss), optimal training (steady decrease), and divergence (loss increases) with different learning rates.