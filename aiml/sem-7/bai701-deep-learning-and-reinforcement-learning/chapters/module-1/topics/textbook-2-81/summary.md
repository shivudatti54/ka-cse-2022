### Textbook 2: 8.1 - Deep Learning and Reinforcement Learning

#### Introduction

- Deep Learning: a subset of Machine Learning that uses neural networks with multiple layers to analyze data.
- Reinforcement Learning: a type of Machine Learning where an agent learns to take actions to maximize a reward.

#### Key Concepts

- **Neural Networks**: composed of layers of interconnected nodes (neurons) that process inputs and produce outputs.
  - Input layer: receives input data
  - Hidden layers: process inputs and produce abstract representations
  - Output layer: produces the final output
- **Activation Functions**:
  - Sigmoid: maps inputs to output values between 0 and 1
  - ReLU (Rectified Linear Unit): maps inputs to output values greater than or equal to 0
  - Tanh (Hyperbolic Tangent): maps inputs to output values between -1 and 1
- **Backpropagation**: an algorithm used to train neural networks by minimizing the error between predicted and actual outputs.
- **Loss Functions**:
  - Mean Squared Error (MSE): measures the difference between predicted and actual outputs
  - Cross-Entropy Loss: measures the difference between predicted and actual outputs in classification tasks

#### Important Formulas and Theorems

- **Activation Function Derivatives**:
  - d/da(σ(z)) = σ(z)(1-σ(z))
- **Backpropagation Update Rules**:
  - Weight update: w_new = w_old - α \* dw
  - Bias update: b_new = b_old - α \* db
- **Stochastic Gradient Descent (SGD)**: an optimization algorithm used to minimize the loss function.

#### Key Theorems

- **Universal Approximation Theorem**: states that a neural network with one hidden layer can approximate any continuous function.
- **Hamilton-Jacobi-Bellman (HJB) Equation**: a partial differential equation used to solve optimal control problems in Markov decision processes.
