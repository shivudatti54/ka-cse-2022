# Perceptron and Learning Theory

## Overview

The Perceptron is the simplest artificial neural network, consisting of a single neuron with binary output. Introduced by Rosenblatt (1958), it learns linearly separable patterns through an iterative weight update rule. Understanding perceptron theory provides foundation for modern neural networks.

## Key Points

- **Algorithm**: Initialize weights randomly; for each misclassified point: w = w + η*y*x (η = learning rate, y = true label ±1, x = input)
- **Convergence Theorem**: If data is linearly separable, perceptron converges to solution in finite steps; no convergence if not separable
- **Decision Boundary**: w^Tx + b = 0; updates move boundary toward misclassified points
- **Limitations**: Cannot learn non-linearly separable functions (XOR problem); sensitive to learning rate; no probabilistic outputs
- **Learning Rate η**: Controls update step size; too large = oscillation, too small = slow convergence
- **Multi-class**: One-vs-rest or one-vs-one strategies extend binary perceptron to multiple classes

## Important Concepts

- Perceptron criterion (loss): Σ max(0, -yi(w^Txi + b)); sum of distances of misclassified points to boundary
- Weight update intuition: add η*y*x moves boundary toward correctly classifying point x with label y
- Convergence requires linear separability; otherwise oscillates forever
- Voted perceptron: ensemble of perceptrons from training history; improves generalization

## Notes

- Memorize update rule: w = w + η*y*x for misclassified point
- Convergence theorem: linearly separable → finite steps; otherwise no convergence
- XOR limitation: classic example of non-linearly separable problem
- Understand geometric interpretation: update moves boundary toward misclassified points
