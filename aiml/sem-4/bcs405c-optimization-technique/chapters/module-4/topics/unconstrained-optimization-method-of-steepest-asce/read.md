# Unconstrained Optimization Techniques

## Table of Contents

- [Introduction](#introduction)
- [Method of Steepest Ascent/Descent](#method-of-steepest-ascent/descent)
- [Newton-Raphson (NR) Method](#newton-raphson-nr-method)
- [Gradient Descent](#gradient-descent)
- [Mini-Batch Gradient Descent](#mini-batch-gradient-descent)
- [Stochastic Gradient Descent](#stochastic-gradient-descent)

## Introduction

Unconstrained optimization is a method used to find the minimum or maximum of a function without any constraints. This technique is widely used in various fields such as machine learning, optimization, and engineering. In this study material, we will discuss five popular unconstrained optimization techniques: Method of Steepest Ascent/Descent, Newton-Raphson (NR) Method, Gradient Descent, Mini-Batch Gradient Descent, and Stochastic Gradient Descent.

## Method of Steepest Ascent/Descent

- **Definition:** The Method of Steepest Ascent/Descent is a simple optimization technique that uses the gradient of the objective function to move in the direction of the negative gradient.
- **How it works:**
  - Initialize a starting point for the optimization.
  - Calculate the gradient of the objective function at the current point.
  - Move in the direction of the negative gradient by a small step size.
  - Repeat the process until convergence.
- **Example:** Consider the objective function f(x) = x^2. The gradient of f(x) is f'(x) = 2x. Initialize x = 1 and take a step size of 0.1. The new point is x = 1 - 0.1 \* 2 = 0.8. Repeat the process until convergence.

## Newton-Raphson (NR) Method

- **Definition:** The Newton-Raphson (NR) Method is a powerful optimization technique that uses the Hessian matrix of the objective function to find the minimum or maximum.
- **How it works:**
  - Initialize a starting point for the optimization.
  - Calculate the gradient and Hessian matrix of the objective function at the current point.
  - Solve the system of equations using the inverse of the Hessian matrix.
  - Move to the new point and repeat the process until convergence.
- **Example:** Consider the objective function f(x) = x^3 - 2x^2 + x - 1. Calculate the gradient and Hessian matrix at x = 1. The gradient is f'(x) = 3x^2 - 4x + 1 and the Hessian matrix is H = [[6x - 4, -4], [-4, 2]]. Solve the system of equations to find the new point.

## Gradient Descent

- **Definition:** Gradient Descent is a popular optimization technique that uses the gradient of the objective function to find the minimum.
- **How it works:**
  - Initialize a starting point for the optimization.
  - Calculate the gradient of the objective function at the current point.
  - Move in the direction of the negative gradient by a small step size.
  - Repeat the process until convergence.
- **Example:** Consider the objective function f(x) = x^2. The gradient of f(x) is f'(x) = 2x. Initialize x = 1 and take a step size of 0.1. The new point is x = 1 - 0.1 \* 2 = 0.8. Repeat the process until convergence.

## Mini-Batch Gradient Descent

- **Definition:** Mini-Batch Gradient Descent is an extension of Gradient Descent that uses a mini-batch of data to calculate the gradient.
- **How it works:**
  - Initialize a starting point for the optimization.
  - Split the data into mini-batches.
  - Calculate the gradient of the objective function using a mini-batch.
  - Move in the direction of the negative gradient by a small step size.
  - Repeat the process until convergence.
- **Example:** Consider the objective function f(x) = x^2. Split the data into mini-batches of size 10. Calculate the gradient of f(x) using each mini-batch. Initialize x = 1 and take a step size of 0.1. The new point is x = 1 - 0.1 \* 2 = 0.8. Repeat the process until convergence.

## Stochastic Gradient Descent

- **Definition:** Stochastic Gradient Descent is an extension of Gradient Descent that uses a single sample from the data to calculate the gradient.
- **How it works:**
  - Initialize a starting point for the optimization.
  - Choose a random sample from the data.
  - Calculate the gradient of the objective function using the sample.
  - Move in the direction of the negative gradient by a small step size.
  - Repeat the process until convergence.
- **Example:** Consider the objective function f(x) = x^2. Choose a random sample from the data. Calculate the gradient of f(x) using the sample. Initialize x = 1 and take a step size of 0.1. The new point is x = 1 - 0.1 \* 2 = 0.8. Repeat the process until convergence.

## Key Concepts

- **Gradient:** The derivative of the objective function.
- **Hessian Matrix:** The matrix of second derivatives of the objective function.
- **Newton-Raphson Method:** A powerful optimization technique that uses the Hessian matrix to find the minimum or maximum.
- **Mini-Batch Gradient Descent:** An extension of Gradient Descent that uses a mini-batch of data to calculate the gradient.
- **Stochastic Gradient Descent:** An extension of Gradient Descent that uses a single sample from the data to calculate the gradient.

## Conclusion

In this study material, we discussed five popular unconstrained optimization techniques: Method of Steepest Ascent/Descent, Newton-Raphson (NR) Method, Gradient Descent, Mini-Batch Gradient Descent, and Stochastic Gradient Descent. These techniques are widely used in various fields such as machine learning, optimization, and engineering. Understanding these techniques is essential for developing efficient optimization algorithms.
