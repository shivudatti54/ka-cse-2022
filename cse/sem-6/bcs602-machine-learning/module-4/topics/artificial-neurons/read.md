# Artificial Neurons

## Introduction

An artificial neuron is the fundamental computational unit of neural networks, inspired by biological neurons. Understanding its structure and function is essential for comprehending how neural networks learn and make predictions.

## Biological Inspiration

### Biological Neuron Components

| Biological Part  | Function                                            |
| ---------------- | --------------------------------------------------- |
| Dendrites        | Receive input signals from other neurons            |
| Soma (Cell body) | Processes and integrates incoming signals           |
| Axon hillock     | Decides whether to fire (threshold check)           |
| Axon             | Transmits output signal                             |
| Synapses         | Connections to other neurons with varying strengths |

### The Analogy

| Biological        | Artificial                          |
| ----------------- | ----------------------------------- |
| Dendrites         | Input connections (x₁, x₂, ..., xₙ) |
| Synaptic strength | Weights (w₁, w₂, ..., wₙ)           |
| Soma integration  | Weighted summation (Σwᵢxᵢ + b)      |
| Firing threshold  | Activation function f(z)            |
| Axon output       | Output signal y                     |

## Structure of an Artificial Neuron

### Components

1. **Inputs (x₁, x₂, ..., xₙ)**: Feature values fed to the neuron
2. **Weights (w₁, w₂, ..., wₙ)**: Learnable parameters controlling input importance
3. **Bias (b)**: Additional learnable parameter for shifting the activation
4. **Summation function**: Computes z = Σwᵢxᵢ + b (net input)
5. **Activation function**: f(z) transforms the net input to produce the output
6. **Output (y)**: y = f(z) = f(Σwᵢxᵢ + b)

### Mathematical Model

**y = f(w₁x₁ + w₂x₂ + ... + wₙxₙ + b) = f(w^T x + b)**

In vector notation: y = f(w · x + b)

## Role of Weights

Weights determine how much each input influences the neuron's output:

- **Large positive weight**: Input has strong positive influence
- **Large negative weight**: Input has strong negative influence
- **Weight near zero**: Input has minimal influence
- **Learning**: Adjusting weights to minimize prediction errors

## Role of Bias

The bias term provides additional flexibility:

- Allows the neuron to activate even when all inputs are zero
- Shifts the activation function left or right
- Analogous to the intercept in linear regression (y = mx + **b**)
- Without bias, the activation always passes through the origin

## Activation Functions

### Step Function (Heaviside)

f(z) = 1 if z ≥ 0, else 0

- Binary output: 0 or 1
- Used in the original perceptron
- **Limitation**: Not differentiable at z = 0, no gradient information

### Sigmoid (Logistic)

f(z) = 1 / (1 + e^(-z))

- Smooth, differentiable, range (0, 1)
- Interpretable as probability
- **Limitation**: Vanishing gradient for very large or small z
- **Limitation**: Outputs are not zero-centered

### Hyperbolic Tangent (Tanh)

f(z) = (e^z - e^(-z)) / (e^z + e^(-z))

- Range: (-1, 1)
- Zero-centered (better than sigmoid for hidden layers)
- **Limitation**: Still suffers from vanishing gradients at extremes

### ReLU (Rectified Linear Unit)

f(z) = max(0, z)

- Range: [0, ∞)
- Computationally efficient (simple comparison)
- Mitigates vanishing gradient for positive values
- Enables sparse activation (many neurons output 0)
- **Limitation**: "Dying ReLU" - neurons stuck at 0 if they enter negative region

### Leaky ReLU

f(z) = z if z > 0, else αz (α is small, e.g., 0.01)

- Addresses the dying ReLU problem
- Allows small gradient for negative values

### Softmax

f(zᵢ) = e^(zᵢ) / Σe^(zⱼ)

- Converts a vector of values to probabilities summing to 1
- Used in the output layer for multi-class classification

## Comparison of Activation Functions

| Function   | Range   | Zero-centered | Vanishing Gradient | Computation |
| ---------- | ------- | ------------- | ------------------ | ----------- |
| Step       | {0, 1}  | No            | N/A (non-diff.)    | Very fast   |
| Sigmoid    | (0, 1)  | No            | Yes (extremes)     | Moderate    |
| Tanh       | (-1, 1) | Yes           | Yes (extremes)     | Moderate    |
| ReLU       | [0, ∞)  | No            | No (positive z)    | Very fast   |
| Leaky ReLU | (-∞, ∞) | No            | No                 | Very fast   |

## Types of Artificial Neurons

### McCulloch-Pitts Neuron (1943)

- First mathematical model of a neuron
- Binary inputs and outputs
- Fixed weights (not learnable)
- Used step activation function

### Perceptron (Rosenblatt, 1958)

- First neuron with learnable weights
- Step activation function
- Can solve linearly separable problems
- Learning rule: wᵢ = wᵢ + α(y - ŷ)xᵢ

### Adaline (Widrow & Hoff, 1960)

- Uses linear activation for training, step for prediction
- Introduced the LMS (Least Mean Squares) learning rule
- Minimizes continuous error function

### Modern Neurons

- Use differentiable activation functions (sigmoid, ReLU)
- Trained with backpropagation algorithm
- Form building blocks of deep neural networks

## Exam Tips

- Know the mathematical model of an artificial neuron
- Be able to draw the analogy between biological and artificial neurons
- Compare all activation functions with their properties and limitations
- Understand the role of weights and bias
- Know the evolution: McCulloch-Pitts → Perceptron → Adaline → Modern neurons
