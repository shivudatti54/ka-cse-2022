# Activation Functions: ReLU and Softmax

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

Activation functions are the fundamental building blocks of neural networks, serving as the nonlinear transformations that enable deep learning models to learn complex patterns. Without activation functions, a neural network—regardless of its depth—would simply behave as a linear model, severely limiting its capacity to approximate nonlinear relationships present in real-world data.

In the context of the Delhi University BSc (Hons) Computer Science curriculum under NEP 2024 UGCF, understanding activation functions is essential for courses on Artificial Intelligence, Machine Learning, and Deep Learning. This study material covers two critical activation functions: **ReLU (Rectified Linear Unit)** and **Softmax**, which form the backbone of modern neural network architectures.

**Real-World Applications:**
- **ReLU**: Powers virtually all modern CNNs (Convolutional Neural Networks), RNNs (Recurrent Neural Networks), and Transformers. Used in image classification (ResNet, VGG), object detection, and speech recognition systems.
- **Softmax**: Essential for multi-class classification problems—medical diagnosis systems, handwritten digit recognition (MNIST), natural language processing tasks like sentiment analysis, and recommendation systems.

---

## 2. Understanding Activation Functions

An activation function determines whether a neuron should be activated based on its weighted sum input. It introduces **nonlinearity** into the network, enabling it to:

- Model complex, non-linear relationships
- Enable gradient-based optimization via backpropagation
- Allow the network to learn hierarchical representations

**Mathematical Form:** For a neuron with input vector **z** = [z₁, z₂, ..., zₙ], weights **w** = [w₁, w₂, ..., wₙ], and bias b:

```
output = f(z) = f(Σ(wᵢ × xᵢ) + b)
```

where f is the activation function.

---

## 3. ReLU (Rectified Linear Unit)

### 3.1 Definition and Formula

ReLU is the most widely used activation function in deep learning today. It is defined as:

$$f(z) = \max(0, z)$$

**Or equivalently:**
```
f(z) = z if z > 0
f(z) = 0 otherwise
```

### 3.2 Why ReLU? Key Advantages

| Advantage | Explanation |
|-----------|-------------|
| **Computational Efficiency** | Simple max(0, z) operation is much faster than sigmoid/tanh (no exponentials) |
| **Sparse Activation** | Outputs true zero for negative inputs, creating efficient representations |
| **Mitigates Vanishing Gradient** | Gradient is 1 for positive inputs, avoiding gradient decay in deep networks |
| **Biological Plausibility** | Similar to neuronal "off" states in biological neurons |
| **Empirical Success** | Consistently outperforms other activations in deep networks |

### 3.3 The Derivative of ReLU

The derivative (gradient) of ReLU is crucial for backpropagation:

$$f'(z) = \begin{cases} 1 & \text{if } z > 0 \\ 0 & \text{if } z < 0 \\ \text{undefined} & \text{if } z = 0 \end{cases}$$

**In practice (for implementation):**
```python
# Derivative is typically set to 0 or 1 at z=0
# PyTorch/TensorFlow handle this automatically
gradient = (z > 0).astype(float)  # Returns 1 for z>0, 0 otherwise
```

### 3.4 The "Dying ReLU" Problem

One limitation of ReLU is the "dying ReLU" phenomenon—when a neuron gets stuck in the negative region and always outputs zero, its gradient becomes zero, and it stops learning. This occurs when:

- Learning rate is too high
- Weights are initialized poorly
- Large negative biases shift the activation

### 3.5 ReLU Variants

To address the dying ReLU problem, several variants have been proposed:

#### a) Leaky ReLU
Allows a small, non-zero gradient for negative values:

$$f(z) = \max(\alpha z, z) \text{ where } \alpha \approx 0.01$$

```python
def leaky_relu(z, alpha=0.01):
    return np.maximum(alpha * z, z)
```

#### b) Parametric ReLU (PReLU)
The α parameter is learnable during training:

$$f(z) = \max(\alpha z, z)$$

#### c) Exponential Linear Unit (ELU)
Uses exponential functions for smooth negative values:

$$f(z) = \begin{cases} z & \text{if } z > 0 \\ \alpha(e^z - 1) & \text{if } z \leq 0 \end{cases}$$

### 3.6 Practical Implementation of ReLU

**NumPy Implementation:**
```python
import numpy as np

def relu(z):
    """ReLU activation function"""
    return np.maximum(0, z)

def relu_derivative(z):
    """Derivative of ReLU for backpropagation"""
    return (z > 0).astype(float)

# Example usage
z = np.array([-2, -1, 0, 1, 2])
output = relu(z)
gradient = relu_derivative(z)

print(f"Input:    {z}")
print(f"Output:   {output}")   # [0, 0, 0, 1, 2]
print(f"Gradient: {gradient}") # [0, 0, 1, 1, 1]
```

**PyTorch Implementation:**
```python
import torch
import torch.nn as nn

# Using nn.ReLU() module
relu_layer = nn.ReLU()

# Forward pass
z = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0], requires_grad=True)
output = relu_layer(z)

print(f"Input:  {z}")
print(f"Output: {output}")  # tensor([0., 0., 0., 1., 2.], grad_fn=<ReluBackward0>)
```

**Using ReLU in a Simple Neural Network:**
```python
import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc = nn.Linear(64 * 8 * 8, 10)
    
    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
```

---

## 4. Softmax Function

### 4.1 Definition and Formula

The Softmax function (also known as **Normalized Exponential Function**) is specifically designed for multi-class classification problems. It converts a vector of raw scores (logits) into a probability distribution where:

- All output values are in the range (0, 1)
- All outputs sum to 1

**Formula:**
$$f(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

Where:
- **z** = input vector of logits [z₁, z₂, ..., zₖ]
- **K** = number of classes
- **e** = Euler's number (≈ 2.71828)
- **f(zᵢ)** = probability of class i

### 4.2 Mathematical Properties

1. **Probability Distribution**: Σᵢ f(zᵢ) = 1
2. **Monotonicity**: If zᵢ > zⱼ, then f(zᵢ) > f(zⱼ)
3. **Differentiability**: Smooth function, enabling gradient-based optimization

### 4.3 Derivative of Softmax

The derivative of softmax with respect to its input is essential for backpropagation. For the i-th output:

$$\frac{\partial f(z_i)}{\partial z_j} = f(z_i)(\delta_{ij} - f(z_j))$$

Where δᵢⱼ is the Kronecker delta (1 if i=j, 0 otherwise).

**In matrix form**, this creates the Jacobian matrix. The derivative is particularly simple when computing the loss gradient using **Cross-Entropy Loss**—the gradient simplifies to **(predicted_probability - one_hot_label)**.

### 4.4 Numerical Stability Problem

A critical issue with softmax is **numerical overflow/underflow** when computing exponentials of large numbers.

**Problem:**
```python
# This causes overflow!
z = [1000, 1001, 1002]
exp_sum = sum(np.exp(z))  # Overflow: exp(1000) is infinity
```

**Solution: Subtract Maximum (Log-Sum-Exp Trick):**

The numerically stable formula:
$$f(z_i) = \frac{e^{z_i - \max(z)}}{\sum_{j=1}^{K} e^{z_j - \max(z)}}$$

This works because:
$$\frac{e^{z_i - M}}{\sum e^{z_j - M}} = \frac{e^{z_i}}{e^M \sum e^{z_j}} = \frac{e^{z_i}}{\sum e^{z_j}}$$

### 4.5 Temperature Parameter

The **temperature** parameter controls how "sharp" or "soft" the probability distribution is:

$$f(z_i, T) = \frac{e^{z_i/T}}{\sum_{j=1}^{K} e^{z_j/T}}$$

| Temperature | Effect |
|-------------|--------|
| **T < 1** | Sharper distribution (higher confidence) |
| **T = 1** | Standard softmax |
| **T > 1** | Softer distribution (more uncertainty) |

**Applications of Temperature:**
- **Knowledge Distillation**: Lower temperature in teacher model to transfer sharper knowledge
- **Calibration**: Adjust confidence estimates
- **Generation**: Higher temperature in LLMs increases creativity/diversity

```python
def softmax_with_temperature(logits, temperature=1.0):
    """Numerically stable softmax with temperature"""
    # Subtract max for numerical stability
    shifted = logits - np.max(logits)
    exp_shifted = np.exp(shifted / temperature)
    return exp_shifted / np.sum(exp_shifted)

# Example
logits = np.array([2.0, 1.0, 0.1])

print("Standard (T=1):", softmax_with_temperature(logits, 1.0))
print("Sharp (T=0.5):", softmax_with_temperature(logits, 0.5))
print("Soft (T=2.0):", softmax_with_temperature(logits, 2.0))
```

### 4.6 Practical Implementation of Softmax

**NumPy Implementation (Numerically Stable):**
```python
import numpy as np

def softmax(logits):
    """
    Numerically stable softmax implementation
    
    Args:
        logits: numpy array of shape (n_classes,) or (batch_size, n_classes)
    Returns:
        Probability distribution summing to 1
    """
    # For numerical stability, subtract the maximum
    shifted_logits = logits - np.max(logits, axis=-1, keepdims=True)
    exp_logits = np.exp(shifted_logits)
    return exp_logits / np.sum(exp_logits, axis=-1, keepdims=True)

# Test with single sample
logits_single = np.array([2.0, 1.0, 0.1])
print("Single sample:", softmax(logits_single))
print("Sum:", np.sum(softmax(logits_single)))  # Should be 1.0

# Test with batch
logits_batch = np.array([[2.0, 1.0, 0.1],
                         [1.0, 3.0, 0.5]])
print("\nBatch:", softmax(logits_batch))
print("Sum per row:", np.sum(softmax(logits_batch), axis=1))
```

**PyTorch Implementation:**
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

# Method 1: Using functional API
logits = torch.tensor([[2.0, 1.0, 0.1],
                       [1.0, 3.0, 0.5]])
probabilities = F.softmax(logits, dim=1)
print(probabilities)

# Method 2: Using nn.Module
softmax_layer = nn.Softmax(dim=1)
output = softmax_layer(logits)
print(output)

# Method 3: With temperature (manual implementation)
def softmax_with_temp(logits, temperature=1.0):
    return F.softmax(logits / temperature, dim=1)
```

**Complete Classification Example:**
```python
import torch
import torch.nn as nn

class ImageClassifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super(ImageClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)  # Raw logits before softmax
        # During training: use F.cross_entropy which applies softmax internally
        # During inference: apply softmax for probabilities
        return x

# Create model
model = ImageClassifier(input_size=784, num_classes=10)

# Forward pass - get raw logits
dummy_input = torch.randn(32, 784)  # Batch of 32 images
logits = model(dummy_input)

# Method 1: Using cross-entropy loss (applies softmax internally)
criterion = nn.CrossEntropyLoss()
# For CE loss, provide class indices (not one-hot)
labels = torch.randint(0, 10, (32,))
loss = criterion(logits, labels)

# Method 2: Manual softmax for inference
probabilities = F.softmax(logits, dim=1)
predicted_classes = torch.argmax(probabilities, dim=1)
print("Predicted classes:", predicted_classes)
```

---

## 5. Comparison: ReLU vs Softmax

| Aspect | ReLU | Softmax |
|--------|------|---------|
| **Purpose** | Neuron-level activation | Output layer for multi-class classification |
| **Output Range** | [0, ∞) | (0, 1), sums to 1 |
| **Nonlinearity** | Piecewise linear | Exponential, produces probability distribution |
| **Used In** | Hidden layers | Output layer (typically) |
| **Parameters** | None (can have variants with α) | None |
| **Typical Use** | Feature learning in hidden layers | Final prediction probabilities |

---

## 6. Key Takeaways

1. **ReLU** is the workhorse activation for hidden layers—simple, efficient, and effective in deep networks
2. **Softmax** converts raw scores to probabilities for multi-class classification, always summing to 1
3. **Numerical stability** is critical for Softmax—always subtract the maximum logit before exponentiating
4. **Temperature** controls the "sharpness" of Softmax distributions, useful in distillation and generation
5. **ReLU variants** (Leaky ReLU, ELU) address the dying ReLU problem
6. The **derivative** of these functions enables backpropagation and gradient-based learning
7. In practice, **Cross-Entropy Loss + Softmax** is the standard combination for classification

---

## 7. Assessment Questions

### 7.1 Multiple Choice Questions (MCQs)

**Q1.** What is the mathematical definition of ReLU?
- A) f(z) = 1 / (1 + e^(-z))
- B) f(z) = max(0, z)
- C) f(z) = tanh(z)
- D) f(z) = e^z / Σe^z

**Q2.** The derivative of ReLU for z > 0 is:
- A) 0
- B) 1
- C) z
- D) undefined

**Q3.** Which problem does ReLU sometimes suffer from?
- A) Exploding gradient
- B) Vanishing gradient
- C) Dying ReLU
- D) Overfitting

**Q4.** The Softmax function outputs:
- A) Any real number
- B) Values between 0 and 1
- C) Values between -1 and 1
- D) Binary values (0 or 1)

**Q5.** In Softmax, what ensures numerical stability?
- A) Adding a constant to all logits
- B) Subtracting the maximum logit before exponentiating
- C) Using log base 2
- D) Dividing by the number of classes

**Q6.** If temperature T > 1 in Softmax, the distribution becomes:
- A) More peaked/sharper
- B) More uniform/softer
- C) Binary
- D) Unchanged

**Q7.** Which activation is typically used in the output layer for 10-class classification?
- A) ReLU
- B) Sigmoid
- C) Softmax
- D) Tanh

**Q8.** Leaky ReLU allows a small gradient for negative inputs to prevent:
- A) Exploding gradients
- B) Overfitting
- C) Dying ReLU
- D) Vanishing gradients

**Q9.** The sum of all outputs from Softmax equals:
- A) 0
- B) 1
- C) Number of classes
- D) Infinity

**Q10.** In a neural network for digit recognition (0-9), if logits are [2.1, 1.5, 0.3, 4.2, 0.8, 1.1, 0.5, 2.0, 3.1, 1.8], the predicted class is:
- A) 1
- B) 3
- C) 8
- D) 4

**Q11.** Which ReLU variant makes the α parameter learnable?
- A) Leaky ReLU
- B) PReLU (Parametric ReLU)
- C) ELU
- D) SeLU

**Q12.** Cross-Entropy Loss with Softmax derivative simplifies to:
- A) (prediction - target) × softmax_derivative
- B) prediction - one_hot_target
- C) target - prediction
- D) sigmoid_derivative

### 7.2 Short Answer Questions

1. Explain why ReLU is computationally efficient compared to sigmoid.
2. Define the mathematical formula for Softmax with temperature parameter.
3. What is the "dying ReLU" problem and how can it be mitigated?
4. Why is numerical stability important in Softmax implementation?
5. Differentiate between the use of ReLU in hidden layers vs Softmax in output layers.
6. Calculate Softmax outputs for logits [1, 2, 3] showing all steps.
7. Explain the concept of sparse activation in ReLU.
8. What is the gradient of Softmax at z=0?

### 7.3 Long Answer / Application-Based Questions

**Q1.** You are building a neural network for classifying images into 100 categories.
- (a) Explain where ReLU would be used in your network architecture.
- (b) Explain where Softmax would be used.
- (c) If your model predictions are all nearly equal (low confidence), what would you check? How might adjusting temperature help?
- (d) Write the complete forward pass code using PyTorch, showing both activations.

**Q2.** Consider a scenario where you are training a very deep neural network (50+ layers) for medical image classification.
- (a) Why would you choose ReLU over sigmoid/tanh for hidden layers?
- (b) If you notice many neurons have become "dead" (outputting 0), what could be the causes?
- (c) Propose two solutions to address the dying neurons problem.
- (d) Implement a custom Leaky ReLU activation in NumPy and verify its gradient calculation.

**Q3.** A student implemented Softmax as follows:
```python
def softmax_bad(logits):
    return np.exp(logits) / np.sum(np.exp(logits))
```
- (a) Identify the problem with this implementation.
- (b) Explain the mathematical reasoning behind the fix.
- (c) Write the corrected implementation.
- (d) If logits = [1000, 1001, 1002], show what happens with the bad implementation vs the corrected one.

**Q4.** In production deployment of a classification model, you need calibrated probability estimates for medical diagnosis.
- (a) Explain the difference between model accuracy and probability calibration.
- (b) How does temperature scaling help in calibration?
- (c) Would you use higher or lower temperature for high-stakes medical decisions? Justify your answer.
- (d) Write code to apply temperature scaling to model predictions.

---

## References and Further Reading

1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
2. LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature*, 521(7553), 436-444.
3. Maas, A. L., Hannun, A. Y., & Ng, A. Y. (2013). Rectifier nonlinearities improve neural network acoustic models. *ICML*.
4. Hinton, G., Vinyals, O., & Dean, J. (2015). Distilling the knowledge in a neural network. *NIPS Deep Learning and Representation Learning Workshop*.
5. Delhi University NEP 2024 UGCF Syllabus - Artificial Intelligence and Machine Learning.

---

*End of Study Material*