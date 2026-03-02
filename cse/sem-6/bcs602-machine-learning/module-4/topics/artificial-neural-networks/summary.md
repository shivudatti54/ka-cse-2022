# Artificial Neural Networks

## Overview

Artificial Neural Networks (ANNs) are computing systems inspired by biological brains, consisting of interconnected artificial neurons organized in layers. They learn complex non-linear mappings through backpropagation, making them powerful for pattern recognition, classification, and regression tasks.

## Key Points

- **Architecture**: Input layer (features), Hidden layers (learned representations), Output layer (predictions); connections have weights
- **Feedforward**: Information flows input → hidden → output; each neuron computes weighted sum + activation
- **Backpropagation**: Algorithm for computing gradients; propagates error backward from output to adjust all weights
- **Activation Functions**: Sigmoid, Tanh (hidden layers historically), ReLU (modern standard for hidden), Softmax (output for multiclass)
- **Universal Approximation**: Neural network with one hidden layer can approximate any continuous function (given enough neurons)
- **Training**: Minimize loss function (MSE for regression, cross-entropy for classification) using gradient descent variants (SGD, Adam)

## Important Concepts

- Deep network: multiple hidden layers learn hierarchical representations (low-level features → high-level concepts)
- Vanishing gradient: sigmoid/tanh cause gradients to diminish in deep networks; ReLU helps mitigate
- Regularization: Dropout (randomly disable neurons), L2 penalty, Early stopping prevent overfitting
- Batch normalization: normalize layer inputs; accelerates training and improves stability

## Notes

- Understand architecture: input layer, hidden layers (feature learning), output layer (prediction)
- Backpropagation computes gradients via chain rule; enables training deep networks
- ReLU activation (max(0,x)) is modern standard for hidden layers (solves vanishing gradient)
- Universal approximation theorem: one hidden layer sufficient but deep networks learn better representations
