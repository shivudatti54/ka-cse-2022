# Activation Functions: ReLU & Softmax
**BSc (Hons) Computer Science – Delhi University, NEP 2024 UGCF**

---

## Introduction
Activation functions are mathematical equations that determine the output of a neural network node given an input. They introduce non-linearity into the network, enabling deep learning models to learn complex patterns. As per the Delhi University NEP 2024 UGCF syllabus, understanding these functions is essential for neural network design.

---

## Key Concepts

### ReLU (Rectified Linear Unit)
- **Definition**: f(x) = max(0, x) — outputs x for positive values, 0 for negative inputs
- **Purpose**: Introduces sparsity by deactivating negative neurons
- **Advantages**:
  - Computationally efficient (simple thresholding)
  - Reduces vanishing gradient problem
  - Accelerates convergence in deep networks
- **Limitations**:
  - "Dying ReLU" problem — neurons stuck in negative region
  - Not suitable for outputs requiring probabilities
- **Variants**: Leaky ReLU, Parametric ReLU, ELU

### Softmax Function
- **Definition**: Converts logits into probabilities for multi-class classification
- **Formula**: σ(zᵢ) = e^(zᵢ) / Σⱼ e^(zⱼ)
- **Purpose**: Ensures output values sum to 1 (probability distribution)
- **Key Features**:
  - Used in output layer for multi-class problems
  - Amplifies differences between logit values
  - Essential for cross-entropy loss computation
- **Limitation**: Computationally expensive for large number of classes

---

## Comparison & Use Cases

| Aspect | ReLU | Softmax |
|--------|------|---------|
| **Layer** | Hidden layers | Output layer |
| **Output** | Unbounded values | Probabilities (0-1) |
| **Use Case** | Feature learning | Multi-class classification |

---

## Exam Quick Points
- Activation functions enable non-linearity — without them, neural networks reduce to linear models
- ReLU is the most popular hidden layer activation due to simplicity and efficiency
- Softmax is mandatory for multi-class classification problems (e.g., image recognition, NLP)
- ReLU solves vanishing gradient better than sigmoid/tanh
- Choice depends on problem type: ReLU for hidden layers, Softmax for output classification

---

## Conclusion
ReLU and Softmax are fundamental activation functions in deep learning. ReLU powers hidden layers for efficient feature extraction, while Softmax enables proper probability-based classification. Mastery of these functions is crucial for implementing neural networks as per the Delhi University curriculum.