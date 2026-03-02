# OPTIMIZATION TECHNIQUE

Module: Convex Optimization-2
Topic: Unconstrained Optimization

## Table of Contents

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [Method of Steepest Ascent/Descent](#method-of-steepest-ascent/descent)
4. [Newton-Raphson (NR) Method](#newton-raphson-nr-method)
5. [Gradient Descent](#gradient-descent)
6. [Mini Batch Gradient Descent](#mini-batch-gradient-descent)
7. [Stochastic Gradient Descent](#stochastic-gradient-descent)
8. [Applications and Case Studies](#applications-and-case-studies)
9. [Comparison of Methods](#comparison-of-methods)
10. [Further Reading](#further-reading)

### Introduction

Unconstrained optimization is a fundamental problem in mathematics and computer science, where the goal is to find the maximum or minimum of a scalar function without any constraints on the variables. This problem has numerous applications in various fields, including machine learning, optimization, and signal processing.

Optimization techniques are used to find the optimal values of variables that maximize or minimize a given function. In this module, we will explore five popular unconstrained optimization methods: Method of Steepest Ascent/Descent, Newton-Raphson (NR) Method, Gradient Descent, Mini Batch Gradient Descent, and Stochastic Gradient Descent.

### Historical Context

The concept of unconstrained optimization dates back to the 18th century, when mathematicians like Leonhard Euler and Joseph-Louis Lagrange developed methods for finding the maximum and minimum of functions. However, the development of optimization techniques as we know them today is a relatively recent phenomenon.

In the 1950s and 1960s, optimization techniques were primarily used in the field of linear programming. The introduction of the first programming languages like Fortran and COBOL in the 1950s and 1960s revolutionized the field of optimization by enabling the efficient solution of large-scale optimization problems.

In the 1970s and 1980s, the development of optimization algorithms for non-linear functions began. This led to the introduction of methods like the Newton-Raphson method, which is still widely used today.

### Method of Steepest Ascent/Descent

The method of steepest ascent/descent is a simple optimization algorithm that finds the maximum or minimum of a scalar function by iteratively moving in the direction of the steepest ascent or descent.

The algorithm works as follows:

- Initialize a starting point `x` for the optimization process.
- Compute the gradient of the objective function `f(x)` at the current point `x`.
- Move in the direction of the negative gradient to find the steepest descent or in the direction of the positive gradient to find the steepest ascent.
- Repeat the process until convergence.

The method of steepest ascent/descent has several limitations. It requires the computation of the gradient of the objective function, which can be time-consuming and expensive. Additionally, the algorithm may get stuck in local minima.

### Newton-Raphson (NR) Method

The Newton-Raphson method is an optimization algorithm that uses the Hessian matrix to find the maximum or minimum of a scalar function. The Hessian matrix is a square matrix of second-order partial derivatives of the objective function.

The algorithm works as follows:

- Initialize a starting point `x` for the optimization process.
- Compute the gradient of the objective function `f(x)` at the current point `x`.
- Compute the Hessian matrix `H(x)` of the objective function.
- Use the Hessian matrix to find the optimal step size `α` that minimizes the objective function.
- Update the current point `x` using the following equation:

x = x - αH(x)^-1 \* f'(x)

Repeat the process until convergence.

The Newton-Raphson method is a powerful optimization algorithm that can find the global maximum or minimum of a scalar function. However, it requires the computation of the Hessian matrix, which can be time-consuming and expensive.

### Gradient Descent

Gradient descent is an optimization algorithm that finds the maximum or minimum of a scalar function by iteratively moving in the direction of the negative gradient.

The algorithm works as follows:

- Initialize a starting point `x` for the optimization process.
- Compute the gradient of the objective function `f(x)` at the current point `x`.
- Move in the direction of the negative gradient to find the descent.
- Update the current point `x` using the following equation:

x = x - αf'(x)

where `α` is the learning rate.

Repeat the process until convergence.

Gradient descent is a simple and efficient optimization algorithm that is widely used in machine learning and other fields. However, it may get stuck in local minima if the learning rate is too high.

### Mini Batch Gradient Descent

Mini batch gradient descent is an optimization algorithm that finds the maximum or minimum of a scalar function by iteratively moving in the direction of the negative gradient using a mini batch of data.

The algorithm works as follows:

- Initialize a starting point `x` for the optimization process.
- Compute the gradient of the objective function `f(x)` at the current point `x` using a mini batch of `m` data points.
- Move in the direction of the negative gradient to find the descent.
- Update the current point `x` using the following equation:

x = x - α\* (1/m) \* ∑(f(x_i) - f(x))^2

where `α` is the learning rate and `x_i` are the data points in the mini batch.

Mini batch gradient descent is a more efficient version of gradient descent that reduces the computational cost of computing the gradient.

### Stochastic Gradient Descent

Stochastic gradient descent is an optimization algorithm that finds the maximum or minimum of a scalar function by iteratively moving in the direction of the negative gradient using a single data point.

The algorithm works as follows:

- Initialize a starting point `x` for the optimization process.
- Compute the gradient of the objective function `f(x)` at the current point `x` using a single data point `x_i`.
- Move in the direction of the negative gradient to find the descent.
- Update the current point `x` using the following equation:

x = x - αf'(x_i)

where `α` is the learning rate.

Stochastic gradient descent is a simple and efficient optimization algorithm that is widely used in machine learning and other fields.

### Applications and Case Studies

Unconstrained optimization has numerous applications in various fields, including:

- Machine learning: Optimization techniques are used to find the optimal weights and biases of a neural network.
- Signal processing: Optimization techniques are used to find the optimal filter coefficients for signal processing.
- Economics: Optimization techniques are used to find the optimal production levels and resource allocation.

Case studies:

- Image recognition: Gradient descent is used to optimize the weights and biases of a neural network for image recognition.
- Speech recognition: Stochastic gradient descent is used to optimize the weights and biases of a neural network for speech recognition.

### Comparison of Methods

| Method                      | Complexity | Speed  | Accuracy      |
| --------------------------- | ---------- | ------ | ------------- |
| Steepest Ascent/Descent     | O(n)       | Slow   | Local minima  |
| Newton-Raphson              | O(n^2)     | Fast   | Global minima |
| Gradient Descent            | O(n)       | Slow   | Local minima  |
| Mini Batch Gradient Descent | O(n)       | Faster | Global minima |
| Stochastic Gradient Descent | O(n)       | Fast   | Local minima  |

### Further Reading

- "Optimization: Theory and Methods" by N. S. Bakhshali
- "Introduction to Optimization" by V. Chandra Chekuri
- "Optimization Techniques in Machine Learning" by H. Chen

Note: The depth of the content can be increased or decreased as per the requirement. The above content is just a starting point and can be further expanded upon.
