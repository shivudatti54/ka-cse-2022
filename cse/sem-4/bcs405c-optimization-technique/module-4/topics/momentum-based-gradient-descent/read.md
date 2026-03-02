# Momentum-Based Gradient Descent

## Table of Contents

- [Momentum-Based Gradient Descent](#momentum-based-gradient-descent)
- [Introduction](#introduction)
- [Algorithm](#algorithm)
- [Benefits](#benefits)
- [How It Works](#how-it-works)
- [Variants](#variants)
- [Important Points](#important-points)

## Introduction

Momentum accelerates gradient descent by adding a velocity term that accumulates past gradients.

## Algorithm

v = βv + α∇f(x)
x = x - v

Where:

- v = velocity
- β = momentum coefficient (typically 0.9)
- α = learning rate

## Benefits

1. Faster convergence
2. Reduces oscillation
3. Escapes local minima better

## How It Works

- Like a ball rolling downhill
- Accumulates velocity in consistent directions
- Slows down in oscillating directions

## Variants

1. Classical Momentum
2. Nesterov Accelerated Gradient (NAG)

## Important Points

1. β typically 0.9
2. Reduces oscillations in narrow valleys
3. Helps escape shallow local minima
4. NAG is more responsive
