# Backpropagation and Automatic Differentiation

## Table of Contents

- [Backpropagation and Automatic Differentiation](#backpropagation-and-automatic-differentiation)
- [Introduction](#introduction)
- [The Backpropagation Algorithm](#the-backpropagation-algorithm)
  - [Forward Pass](#forward-pass)
  - [Backward Pass (Backpropagation)](#backward-pass-backpropagation)
- [Automatic Differentiation](#automatic-differentiation)
  - [Forward Mode](#forward-mode)
  - [Reverse Mode](#reverse-mode)
- [Chain Rule in Computation](#chain-rule-in-computation)
- [Important Points](#important-points)

## Introduction

Backpropagation is the fundamental algorithm for training neural networks. It efficiently computes gradients of the loss function with respect to network weights using the chain rule from calculus. Automatic differentiation extends this concept to compute exact derivatives of arbitrary mathematical functions by decomposing them into elementary operations.

## The Backpropagation Algorithm

### Forward Pass

In the forward pass, input data flows through the network layer by layer:

- Each neuron computes a weighted sum of inputs
- An activation function is applied
- The output propagates to the next layer

### Backward Pass (Backpropagation)

The backward pass computes gradients:

1. Compute loss at output layer
2. Propagate error backwards through network
3. Calculate gradients using chain rule:
   ∂E/∂w = ∂E/∂a × ∂a/∂z × ∂z/∂w

## Automatic Differentiation

### Forward Mode

Computes derivatives from input to output:

- Evaluate function and derivative simultaneously
- Efficient for functions with few inputs

### Reverse Mode

Computes derivatives from output to input:

- Two passes: forward (record operations) + backward (compute gradients)
- Efficient for functions with many inputs (deep networks)

## Chain Rule in Computation

For a composite function f(g(h(x))):

- df/dx = df/dg × dg/dh × dh/dx
- Each partial derivative computed independently
- Chain rule enables efficient gradient computation

## Important Points

1. Backpropagation requires differentiable activation functions
2. Gradients can vanish or explode in deep networks
3. Automatic differentiation is exact (not numerical approximation)
4. Computational graphs enable automatic differentiation
5. Reverse mode is preferred for deep learning
