# Gradients in a Deep Network

## Table of Contents

- [Gradients in a Deep Network](#gradients-in-a-deep-network)
- [Introduction](#introduction)
- [Gradient Computation](#gradient-computation)
- [Challenges in Deep Networks](#challenges-in-deep-networks)
  - [Vanishing Gradients](#vanishing-gradients)
  - [Exploding Gradients](#exploding-gradients)
- [Gradient Flow in Layers](#gradient-flow-in-layers)
- [Solutions](#solutions)
- [Important Points](#important-points)

## Introduction

In deep neural networks, gradients represent how much each parameter contributes to the loss. Understanding gradient flow is crucial for training effective models.

## Gradient Computation

For a network with L layers:

- Gradient at layer l depends on gradients at layer l+1
- Chain rule links all layers
- ∂L/∂w[l] = ∂L/∂a[l] × ∂a[l]/∂z[l] × ∂z[l]/∂w[l]

## Challenges in Deep Networks

### Vanishing Gradients

- Gradients become extremely small as they propagate backwards
- Earlier layers learn very slowly
- Caused by activation functions with derivatives < 1

### Exploding Gradients

- Gradients grow exponentially through layers
- Makes training unstable
- Common in RNNs and very deep networks

## Gradient Flow in Layers

- Input layer gradients depend on all subsequent layers
- Each layer's gradient: local gradient × upstream gradient
- Chain of multiplications determines gradient magnitude

## Solutions

1. Proper weight initialization
2. Batch normalization
3. Residual connections
4. Appropriate activation functions (ReLU)

## Important Points

1. Deeper networks face more gradient issues
2. Gradient clipping prevents exploding gradients
3. ReLU helps with vanishing gradients
4. Gradient tells us direction and magnitude of parameter update
