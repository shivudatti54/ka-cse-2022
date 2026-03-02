# Gradient of Mean Squared Error

## Table of Contents

- [Gradient of Mean Squared Error](#gradient-of-mean-squared-error)
- [Introduction](#introduction)
- [MSE Formula](#mse-formula)
- [Gradient with Respect to Weights](#gradient-with-respect-to-weights)
- [Properties](#properties)
- [Relationship with Quadratic Cost](#relationship-with-quadratic-cost)
- [Important Points](#important-points)

## Introduction

Mean Squared Error (MSE) is the average squared difference between predicted and actual values.

## MSE Formula

MSE = (1/n) Σ(yi - ŷi)²

Where n = number of samples

## Gradient with Respect to Weights

For a single output:
∂MSE/∂w = (2/n) × Σ(ŷi - yi) × ∂ŷi/∂w

For linear activation:
∂MSE/∂w = (2/n) × Σ(ŷi - yi) × xi

## Properties

- Always non-negative
- Units squared (not intuitive)
- Sensitive to outliers
- Penalizes large errors heavily

## Relationship with Quadratic Cost

MSE = Quadratic Cost / n
Gradients differ by factor of 1/n

## Important Points

1. MSE gradient is proportional to prediction error
2. Factor of 2/n in gradient formula
3. Outliers heavily influence MSE
4. Commonly used in regression tasks
