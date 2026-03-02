# Multilayer Feedforward Networks — Quick Revision Summary

## Introduction

Multilayer Feedforward Networks (MLFNs), commonly known as Multilayer Perceptrons (MLPs), form the foundation of classical deep learning. These networks consist of multiple layers of interconnected neurons that process information in a unidirectional manner—from input to output—without feedback loops. Under the Delhi University NEP 2024 UGCF syllabus (Paper: Deep Learning), MLFNs serve as the prerequisite understanding before advancing to complex architectures like CNNs and RNNs.

---

## Key Concepts

### 1. Network Architecture
- **Input Layer**: Receives raw data features (e.g., pixel values, sensor readings)
- **Hidden Layer(s)**: One or more intermediate layers that perform feature extraction and transformation
- **Output Layer**: Produces final predictions (class labels, regression values)
- **Fully Connected (Dense) Layers**: Each neuron connects to every neuron in adjacent layers

### 2. Neurons and Weights
- Each connection has an associated **weight** (w)
- Each neuron has a **bias** (b) added to the weighted sum
- **Activation Function**: Introduces non-linearity; common functions include:
  - Sigmoid: σ(z) = 1/(1+e^(-z))
  - Tanh: tanh(z)
  - ReLU: max(0, z) — most widely used in modern networks

### 3. Feedforward Propagation
- Input signals flow forward through the network
- Each neuron computes: **output = activation(Σwᵢxᵢ + b)**
- Final output is compared with target using a **loss function** (e.g., MSE, Cross-Entropy)

### 4. Learning Process: Backpropagation
- **Gradient Descent** optimization minimizes the loss function
- **Chain Rule** computes gradients layer-by-layer from output to input
- **Epochs**: Complete passes through the training dataset
- **Learning Rate (η)**: Step size for weight updates
- Weights update: **w_new = w_old - η × ∂L/∂w**

### 5. Universal Approximation Theorem
- A single hidden layer with finite neurons can approximate any continuous function (given sufficient width)
- Practical networks use multiple hidden layers for better representation learning

### 6. Training Considerations
- **Overfitting**: Mitigate using dropout, regularization, early stopping
- **Vanishing Gradient**: Problem in deep networks; addressed by ReLU and normalization
- **Hyperparameters**: Number of layers, neurons per layer, learning rate, batch size

### 7. Applications
- Pattern recognition and classification
- Function approximation
- Time series prediction (basic)
- Natural language processing (foundational)

---

## Conclusion

Multilayer Feedforward Networks represent the cornerstone of neural network fundamentals. Despite being surpassed by specialized architectures (CNNs, RNNs) for specific tasks, their learning principles—particularly backpropagation and gradient-based optimization—remain universal. Mastery of MLFNs is essential for understanding advanced deep learning models covered in the Delhi University B.Sc. (Hons) Computer Science curriculum under NEP 2024.