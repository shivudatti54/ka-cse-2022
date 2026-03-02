# Chapter 10 Revision Notes

### Introduction (10.1-10.2)

- **Artificial Neural Networks (ANNs)**: A computational model inspired by the structure and function of the biological nervous system
- **Biological Neurons**: Basic computing units of the brain, receiving, processing, and transmitting information

### Artificial Neurons (10.2-10.3)

- **Artificial Neurons**: Mathematical models of biological neurons, which process and transmit information
- **Perceptron**: A type of feedforward neural network, which is the simplest form of artificial neural network
- **Activation Function**: A mathematical function that introduces non-linearity into the model, enabling it to learn and represent complex relationships

### Perceptron and Learning (10.4-10.5)

- **Perceptron Learning Rule**: A method for training perceptrons to minimize the error between predictions and actual outputs
- **Weighted Sum**: The weighted sum of inputs to an artificial neuron, used to calculate the output
- **Threshold Function**: A simple activation function that outputs 1 if the weighted sum exceeds a certain threshold, and 0 otherwise
- **Linearity and Non-Linearity**: Perceptrons are linear models, but activation functions introduce non-linearity, enabling them to learn complex relationships
- **Convergence**: Perceptrons may not converge to the optimal solution, especially in multi-layer networks

## Key Formulas and Definitions

- **Activation Function**: `f(z) = sigmoid(z) = 1 / (1 + e^(-z))`
- **Perceptron Learning Rule**: `w = w + α * (y - f(x)) * x`, where `α` is the learning rate
- **Weighted Sum**: `z = Σ(wi * xi)`, where `wi` is the weight, and `xi` is the input

## Important Theorems

- **Universal Approximation Theorem**: Any continuous function can be approximated by a multilayer perceptron
- **Convergence Theorem**: Perceptrons converge to the optimal solution if the learning rate is sufficiently small

Note: This summary covers the key points for Chapter 10 (10.1-10.5) of Machine Learning. It is designed to be a concise revision guide, focusing on the most important concepts and formulas.
