# Artificial Neurons

## Overview

Artificial neurons (perceptrons) are mathematical models inspired by biological neurons. They form the building blocks of artificial neural networks, computing weighted sums of inputs and applying activation functions to produce outputs. Understanding single neurons is essential before studying deep neural networks.

## Key Points

- **Model**: Output y = f(Σ(wi\*xi) + b); where w = weights, x = inputs, b = bias, f = activation function
- **Components**: Input signals (x1, x2, ..., xn), Weights (w1, w2, ..., wn), Bias (b), Weighted sum (z = Σwixi + b), Activation function f(z)
- **Activation Functions**: Sigmoid σ(z)=1/(1+e^-z), Tanh tanh(z), ReLU max(0,z), Step (binary 0/1)
- **Geometric Interpretation**: Decision boundary is hyperplane w^Tx + b = 0; weights determine orientation, bias determines position
- **Learning**: Adjust weights and bias to minimize error; gradient descent on loss function
- **Linear Separability**: Single neuron can only learn linearly separable functions; XOR problem requires multiple neurons

## Important Concepts

- Bias allows shifting decision boundary away from origin; without bias, boundary passes through origin
- Activation function introduces non-linearity; without it, network reduces to linear transformation
- Weights determine feature importance; larger magnitude = more influence on output
- Single neuron limitation: can only separate linearly separable classes (AND, OR yes; XOR no)

## Notes

- Memorize neuron model: y = f(Σwixi + b)
- Know activation functions: Sigmoid (smooth, [0,1]), ReLU (fast, [0,∞)), Tanh ([-1,1])
- Explain geometric interpretation: w^Tx + b = 0 is decision boundary hyperplane
- Understand limitation: single neuron cannot solve XOR (requires hidden layer)
