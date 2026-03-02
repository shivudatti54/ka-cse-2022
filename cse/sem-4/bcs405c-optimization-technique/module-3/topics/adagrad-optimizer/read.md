# Adagrad Optimizer

## Table of Contents

- [Adagrad Optimizer](#adagrad-optimizer)
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Algorithm](#algorithm)
- [Advantages](#advantages)
- [Disadvantages](#disadvantages)
- [Variants](#variants)
- [Important Points](#important-points)

## Introduction

Adagrad (Adaptive Gradient Algorithm) is an adaptive learning rate optimization algorithm that adjusts the learning rate based on the frequency of parameter updates.

## Key Features

- Per-parameter learning rates
- Automatically adapts learning rate based on gradient history
- Good for sparse data

## Algorithm

For each parameter θ:

- Accumulate squared gradient: G += ∇J(θ)²
- Update: θ = θ - α/√G + ε × ∇J(θ)

Where ε prevents division by zero.

## Advantages

1. No manual tuning of learning rate
2. Works well with sparse gradients
3. Each parameter gets its own learning rate

## Disadvantages

1. Learning rate monotonically decreases
2. Can stop learning too early in deep networks

## Variants

- Adadelta
- Adam (Adaptive Moment Estimation)
- RMSprop

## Important Points

1. Adagrad divides by sqrt of accumulated gradients
2. Good for text classification tasks
3. Learning rate decreases over time
4. Often replaced by Adam in practice
