# Unconstrained Optimization

### Overview

Unconstrained optimization is a subfield of optimization that deals with finding the maximum or minimum of a scalar-valued function subject to no constraints on the variables. In this study material, we will cover five popular methods for unconstrained optimization: Method of Steepest Ascent/Descent, Newton's Method, Gradient Descent, Mini-batch Gradient Descent, and Stochastic Gradient Descent.

### Method of Steepest Ascent/Descent

The Method of Steepest Ascent/Descent is an iterative method that uses the gradient of the objective function to update the parameters. The algorithm starts with an initial guess for the parameters and iteratively updates them in the direction of the negative gradient.

**Formula:**

Let `f(x)` be the objective function and `x` be the parameters. The gradient of `f(x)` is denoted by `∇f(x)`.

**Stepest Ascent:**

`x(t+1) = x(t) - α ∇f(x(t))`

where `α` is the step size.

**Descent:**

`x(t+1) = x(t) - β ∇f(x(t))`

where `β = α / 2`.

### Example:

Suppose we want to find the maximum of the function `f(x) = x^2` on the interval `[0, 1]`. We start with an initial guess `x = 0.5`.

```
Iteration 1:
f(x) = 0.25
∇f(x) = [0]
x(1) = x(0) - α ∇f(x(0)) = 0.5 - α [0] = 0.5

Iteration 2:
f(x) = 0.25
∇f(x) = [0]
x(2) = x(1) - β ∇f(x(1)) = 0.5 - β [0] = 0.5
```

### Newton's Method

Newton's Method is an iterative method that uses the Hessian matrix of the objective function to update the parameters. The algorithm starts with an initial guess for the parameters and iteratively updates them in the direction of the negative Hessian matrix.

**Formula:**

Let `f(x)` be the objective function and `x` be the parameters. The Hessian matrix of `f(x)` is denoted by `H(x)`.

**Newton's Method:**

`x(t+1) = x(t) - H^-1(t) ∇f(x(t))`

where `H^-1(t)` is the inverse of the Hessian matrix at iteration `t`.

### Example:

Suppose we want to find the minimum of the function `f(x) = x^2` on the interval `[0, 1]`. We start with an initial guess `x = 0.5`.

```
Iteration 1:
f(x) = 0.25
∇f(x) = [0]
H(x) = [[2]]
x(1) = x(0) - H^-1(0) ∇f(x(0)) = 0.5 - H^-1(0) [0] = 0.5

Iteration 2:
f(x) = 0.25
∇f(x) = [0]
H(x) = [[2]]
x(2) = x(1) - H^-1(1) ∇f(x(1)) = 0.5 - H^-1(1) [0] = 0.5
```

### Gradient Descent

Gradient Descent is an iterative method that uses the gradient of the objective function to update the parameters. The algorithm starts with an initial guess for the parameters and iteratively updates them in the direction of the negative gradient.

**Formula:**

Let `f(x)` be the objective function and `x` be the parameters. The gradient of `f(x)` is denoted by `∇f(x)`.

**Gradient Descent:**

`x(t+1) = x(t) - α ∇f(x(t))`

where `α` is the step size.

### Example:

Suppose we want to find the minimum of the function `f(x) = x^2` on the interval `[0, 1]`. We start with an initial guess `x = 0.5`.

```
Iteration 1:
f(x) = 0.25
∇f(x) = [0]
x(1) = x(0) - α ∇f(x(0)) = 0.5 - α [0] = 0.5

Iteration 2:
f(x) = 0.25
∇f(x) = [0]
x(2) = x(1) - α ∇f(x(1)) = 0.5 - α [0] = 0.5
```

### Mini-batch Gradient Descent

Mini-batch Gradient Descent is a variation of Gradient Descent that uses a mini-batch of data to update the parameters. The algorithm starts with an initial guess for the parameters and iteratively updates them in the direction of the negative gradient.

**Formula:**

Let `f(x)` be the objective function and `x` be the parameters. The gradient of `f(x)` is denoted by `∇f(x)`.

**Mini-batch Gradient Descent:**

`x(t+1) = x(t) - α ∇f(x(t)) / m`

where `m` is the mini-batch size.

### Example:

Suppose we want to find the minimum of the function `f(x) = x^2` on the interval `[0, 1]`. We start with an initial guess `x = 0.5` and use a mini-batch size of 10.

```
Iteration 1:
f(x) = 0.25
∇f(x) = [0]
x(1) = x(0) - α ∇f(x(0)) / m = 0.5 - α [0] / 10 = 0.5 - α / 10

Iteration 2:
f(x) = 0.25
∇f(x) = [0]
x(2) = x(1) - α ∇f(x(1)) / m = 0.5 - α [0] / 10 = 0.5 - α / 10
```

### Stochastic Gradient Descent

Stochastic Gradient Descent is a variation of Gradient Descent that uses a single data point to update the parameters. The algorithm starts with an initial guess for the parameters and iteratively updates them in the direction of the negative gradient.

**Formula:**

Let `f(x)` be the objective function and `x` be the parameters. The gradient of `f(x)` is denoted by `∇f(x)`.

**Stochastic Gradient Descent:**

`x(t+1) = x(t) - α ∇f(x(t))`

where `α` is the step size and `x(t)` is sampled from the data.

### Example:

Suppose we want to find the minimum of the function `f(x) = x^2` on the interval `[0, 1]`. We start with an initial guess `x = 0.5` and use a single data point to update the parameters.

```
Iteration 1:
f(x) = 0.25
∇f(x) = [0]
x(1) = x(0) - α ∇f(x(0)) = 0.5 - α [0] = 0.5

Iteration 2:
f(x) = 0.25
∇f(x) = [0]
x(2) = x(1) - α ∇f(x(1)) = 0.5 - α [0] = 0.5
```

## Key Concepts

- **Gradient**: The derivative of a function with respect to a variable.
- **Hessian**: The second derivative of a function with respect to a variable.
- **Step size**: The amount by which the parameters are updated at each iteration.
- **Mini-batch**: A small subset of data used to update the parameters.
- **Stochastic**: Using a single data point to update the parameters.

## Conclusion

Unconstrained optimization is a crucial technique in machine learning and optimization. We have covered five popular methods for unconstrained optimization: Method of Steepest Ascent/Descent, Newton's Method, Gradient Descent, Mini-batch Gradient Descent, and Stochastic Gradient Descent. Understanding these methods and their applications is essential for successful optimization in machine learning and other fields.
