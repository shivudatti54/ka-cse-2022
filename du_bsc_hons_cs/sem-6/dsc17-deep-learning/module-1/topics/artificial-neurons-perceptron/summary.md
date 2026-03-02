# Artificial Neurons & Perceptron
## Deep Learning — BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)

### Introduction

The **perceptron**, introduced by Frank Rosenblatt in 1958, is the fundamental building block of neural networks and forms the cornerstone of deep learning. It represents the simplest model of an artificial neuron, inspired by biological neurons in the human brain. Understanding perceptrons is essential for grasping how modern deep learning architectures process and learn from data.

### Key Concepts

**1. Biological Inspiration**
- Human brain neurons receive signals through dendrites, process them in the cell body, and transmit output via axons
- Artificial neurons mimic this structure using mathematical operations

**2. Structure of a Perceptron**
- **Input Layer (x₁, x₂, ..., xₙ)**: Receives features from the dataset
- **Weights (w₁, w₂, ..., wₙ)**: Determine the importance of each input
- **Bias (b)**: Shifts the activation function, helps in better fitting
- **Summation Function**: Computes weighted sum: z = Σ(wᵢ × xᵢ) + b
- **Activation Function**: Introduces non-linearity to handle complex patterns

**3. Working Mechanism**
```
Inputs → Weighted Sum → Activation Function → Output
```
- Each input is multiplied by its corresponding weight
- All weighted inputs are summed along with bias
- Activation function transforms the sum into output (0 or 1 for binary classification)

**4. Common Activation Functions**
- **Step Function**: Output 0 or 1 based on threshold
- **Sigmoid**: S-shaped curve, outputs between 0 and 1
- **ReLU (Rectified Linear Unit)**: f(x) = max(0, x) — most popular in deep learning
- **Tanh**: Outputs between -1 and 1

**5. Learning Process**
- **Forward Pass**: Compute output using current weights
- **Error Calculation**: Compare predicted output with actual label
- **Weight Update**: Adjust weights using learning rate and error
- **Epochs**: Repeat training process multiple times until convergence

**6. Mathematical Representation**
```
Output: ŷ = f(w·x + b)
Weight Update: w_new = w_old + η × (y - ŷ) × x
```
where η = learning rate

**7. Limitations of Single Perceptron**
- Can only solve **linearly separable** problems (e.g., AND, OR gates)
- **Cannot solve XOR problem** — requires multi-layer networks
- This limitation led to the development of **Multi-Layer Perceptrons (MLPs)**

### Conclusion

The perceptron, though simple, laid the foundation for modern neural networks. It demonstrates how weighted inputs combined with non-linear activation functions enable machines to learn from data. While a single perceptron has limitations with complex patterns, stacking multiple perceptrons in layers creates powerful deep learning models capable of solving real-world problems like image recognition, natural language processing, and autonomous systems.

---
*For exam preparation: Remember the perceptron formula, understand the role of weights/bias, and know why multi-layers are needed for non-linear problems.*