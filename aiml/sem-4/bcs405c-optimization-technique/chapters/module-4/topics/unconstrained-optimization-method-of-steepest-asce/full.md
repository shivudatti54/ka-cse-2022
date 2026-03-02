# OPTIMIZATION TECHNIQUE

Module: Convex Optimization-2
Topic: Unconstrained optimization -Method of steepest ascent/descent, NR method, Gradient descent, Mini batch gradient descent, Stochastic gradient descent
=====================================

## Table of Contents

- [Introduction](#introduction)
- [Historical Context](#historical-context)
- [Method of Steepest Ascent/Descent](#method-of-steepest-ascent/descent)
- [Newton-Raphson (NR) Method](#newton-raphson-nr-method)
- [Gradient Descent](#gradient-descent)
- [Mini Batch Gradient Descent](#mini-batch-gradient-descent)
- [Stochastic Gradient Descent](#stochastic-gradient-descent)
- [Applications and Case Studies](#applications-and-case-studies)
- [Further Reading](#further-reading)

## Introduction

Unconstrained optimization is a fundamental problem in mathematics and computer science. Given a function f(x) and a vector x, the goal is to find the value of x that minimizes or maximizes f(x). This topic covers five popular methods for unconstrained optimization: Method of Steepest Ascent/Descent, Newton-Raphson (NR) Method, Gradient Descent, Mini Batch Gradient Descent, and Stochastic Gradient Descent.

## Historical Context

The Method of Steepest Ascent/Descent dates back to the 18th century, when it was used by Leonhard Euler to find the maximum of a function. The Newton-Raphson method was developed in the 17th century by Isaac Newton and German mathematician Gottfried Wilhelm Leibniz. Gradient Descent was first introduced in the 1950s by Roger W. Dorsey and others. Mini Batch Gradient Descent and Stochastic Gradient Descent were developed in the 2000s.

## Method of Steepest Ascent/Descent

The Method of Steepest Ascent/Descent is a simple, iterative method for finding the maximum of a function. The algorithm starts at an initial point x0 and moves in the direction of the gradient of the function at each step, with the size of the step determined by a step size parameter α.

**Algorithm:**

1. Initialize x0 to be a random point in the domain of the function.
2. Set α to be a small positive number.
3. Compute the gradient of the function at x0.
4. Move x to be x0 + α \* gradient(x0).
5. Repeat steps 3-4 until convergence or a maximum is reached.

**Example:**

Consider the function f(x) = x^2. The gradient of f(x) is f'(x) = 2x. If we choose x0 = 0 and α = 0.1, the algorithm will move to x1 = 0.1, x2 = 0.2, and so on.

## Newton-Raphson (NR) Method

The Newton-Raphson method is an iterative method for finding the roots of a function. The algorithm uses the Hessian matrix to estimate the curvature of the function at each step.

**Algorithm:**

1. Initialize x0 to be a random point in the domain of the function.
2. Compute the gradient of the function at x0.
3. Compute the Hessian matrix of the function at x0.
4. Compute the update rule x1 = x0 - H^-1 \* gradient(x0), where H is the Hessian matrix.
5. Repeat steps 2-4 until convergence or a root is reached.

**Example:**

Consider the function f(x) = x^2 + 10x + 2. The gradient of f(x) is f'(x) = 2x + 10. The Hessian matrix of f(x) is H(x) = [[2, 10], [10, 2]]. If we choose x0 = 0 and α = 0.1, the algorithm will move to x1 = -5, x2 = -5.1, and so on.

## Gradient Descent

Gradient Descent is an iterative method for finding the minimum of a function. The algorithm starts at an initial point x0 and moves in the direction of the negative gradient of the function at each step.

**Algorithm:**

1. Initialize x0 to be a random point in the domain of the function.
2. Set α to be a small positive number.
3. Compute the gradient of the function at x0.
4. Move x to be x0 - α \* gradient(x0).
5. Repeat steps 3-4 until convergence or a minimum is reached.

**Example:**

Consider the function f(x) = x^2 + 10x + 2. The gradient of f(x) is f'(x) = 2x + 10. If we choose x0 = 0 and α = 0.1, the algorithm will move to x1 = -5, x2 = -5.1, and so on.

## Mini Batch Gradient Descent

Mini Batch Gradient Descent is an iterative method for finding the minimum of a function, where a small batch of points is used to compute the gradient at each step.

**Algorithm:**

1. Initialize x0 to be a random point in the domain of the function.
2. Set α to be a small positive number.
3. Choose a small batch of points B = {xb1, xb2, ..., xbn}.
4. Compute the gradient of the function at each point in B.
5. Move x to be x0 - α \* sum(gradient(xb1), ..., gradient(xbn)) / n, where n is the size of B.
6. Repeat steps 3-5 until convergence or a minimum is reached.

**Example:**

Consider the function f(x) = x^2 + 10x + 2. The gradient of f(x) is f'(x) = 2x + 10. If we choose x0 = 0 and α = 0.1, B = {0, 1, 2, 3, 4, 5}, and n = 6, the algorithm will move to x1 = -5.11, x2 = -5.21, and so on.

## Stochastic Gradient Descent

Stochastic Gradient Descent is an iterative method for finding the minimum of a function, where a single point is used to compute the gradient at each step.

**Algorithm:**

1. Initialize x0 to be a random point in the domain of the function.
2. Set α to be a small positive number.
3. Choose a random point xb in the domain of the function.
4. Compute the gradient of the function at xb.
5. Move x to be x0 - α \* gradient(xb).
6. Repeat steps 3-5 until convergence or a minimum is reached.

**Example:**

Consider the function f(x) = x^2 + 10x + 2. The gradient of f(x) is f'(x) = 2x + 10. If we choose x0 = 0 and α = 0.1, the algorithm will move to x1 = -5.1, x2 = -5.21, and so on.

## Applications and Case Studies

Unconstrained optimization has numerous applications in various fields, including:

- **Machine Learning**: Unconstrained optimization is used to train machine learning models, such as neural networks and support vector machines.
- **Optimization Problems**: Unconstrained optimization is used to solve optimization problems in various fields, including economics, engineering, and finance.
- **Signal Processing**: Unconstrained optimization is used to filter signals and remove noise.
- **Computer Vision**: Unconstrained optimization is used to detect faces, recognize objects, and track motion.

Case Study: **Minimizing the Mean Squared Error**

Consider a linear regression model, where the goal is to minimize the mean squared error (MSE) between the predicted and actual values. The MSE is a function of the model's parameters, and unconstrained optimization can be used to find the optimal parameters that minimize the MSE. In this case, the Method of Steepest Ascent/Descent, Newton-Raphson (NR) Method, and Gradient Descent can be used to find the optimal parameters.

## Further Reading

- **"Optimization Techniques"** by Edwin M. L. Beale
- **"Numerical Optimization"** by Jorge Nocedal and Stephen J. Wright
- **"Machine Learning"** by Andrew Ng and Michael I. Jordan
- **"Signal Processing"** by Ronald A. Fisher
- **"Computer Vision"** by Richard Szeliski

## Conclusion

Unconstrained optimization is a fundamental problem in mathematics and computer science. The five methods discussed in this chapter - Method of Steepest Ascent/Descent, Newton-Raphson (NR) Method, Gradient Descent, Mini Batch Gradient Descent, and Stochastic Gradient Descent - are widely used in various fields, including machine learning, optimization problems, signal processing, and computer vision. By understanding these methods and their applications, researchers and practitioners can develop more efficient and effective optimization algorithms for solving complex problems.
