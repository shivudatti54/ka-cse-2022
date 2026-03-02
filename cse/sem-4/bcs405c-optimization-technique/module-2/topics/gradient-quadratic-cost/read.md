# Gradient of Quadratic Cost

## Table of Contents

- [Gradient of Quadratic Cost](#gradient-of-quadratic-cost)
- [Introduction](#introduction)
- [Quadratic Cost Definition](#quadratic-cost-definition)
- [Gradient Computation](#gradient-computation)
- [Why Quadratic Cost?](#why-quadratic-cost)
- [Relationship with Activation](#relationship-with-activation)
- [Important Points](#important-points)

## Introduction

Quadratic cost (also called mean squared error) is a common loss function in neural networks, especially for regression tasks.

## Quadratic Cost Definition

For a single training example:
L(y, ŷ) = (y - ŷ)² / 2

For m examples:
L = (1/2m) Σ(y(i) - ŷ(i))²

## Gradient Computation

For a single output neuron:
∂L/∂ŷ = ŷ - y

For weights connecting to output:
∂L/∂w = (ŷ - y) × input

## Why Quadratic Cost?

- Smooth, continuous gradient
- Always non-negative
- Penalizes large errors more than small ones
- Simple derivative for optimization

## Relationship with Activation

- With linear output: straightforward gradient
- With sigmoid: gradient shaped by derivative
- With softmax: gradient depends on predicted class

## Important Points

1. Quadratic cost prefers outputs far from target
2. Gradient magnitude proportional to error
3. Often used with linear/sigmoid activations
4. Can be combined with regularization
