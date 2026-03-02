# Unconstrained Optimization Techniques

### Introduction

Unconstrained optimization is a fundamental problem in optimization techniques, where the goal is to find the optimal solution to a function without any constraints on its inputs. In this section, we will explore several unconstrained optimization techniques, including the method of steepest ascent/descent, Non-Linear Regresssion (NR) method, Gradient Descent, Mini-batch Gradient Descent, and Stochastic Gradient Descent.

### Method of Steepest Ascent/Descent

The method of steepest ascent/descent is a simple and intuitive technique for finding the optimal solution to a function. The basic idea is to start at an initial point and move in the direction of the negative gradient of the function at each step.

**How it works:**

- Choose an initial point `x_0`
- Compute the gradient of the function at `x_0`, denoted as `∇f(x_0)`
- Move in the direction of `-∇f(x_0)` by a step size `α`
- Update the point to `x_1 = x_0 + α * -∇f(x_0)`
- Repeat steps 2-4 until convergence

**Example:**

Suppose we want to minimize the function `f(x) = x^2` using the method of steepest ascent/descent. We start at `x_0 = 1` and compute the gradient at `x_0`:

`∇f(x_0) = ∂f/∂x = 2x_0 = 2`

We move in the direction of `-∇f(x_0)` by a step size `α = 0.1`:

`x_1 = x_0 + α * -∇f(x_0) = 1 + 0.1 * (-2) = 0.8`

We repeat this process until convergence:

|x_2| = x_1 - α _ ∇f(x_1) = 0.8 - 0.1 _ 1.6 = 0.72

|...|

The optimal solution is `x_star = 0` where `f(x_star) = 0^2 = 0`.

### Non-Linear Regresssion (NR) Method

The Non-Linear Regresssion (NR) method is another technique for unconstrained optimization. The basic idea is to minimize the sum of the squared errors between the function and its target value.

**How it works:**

- Choose an initial point `x_0`
- Compute the target value `y_star`
- Compute the sum of the squared errors `S = (f(x) - y_star)^2`
- Move in the direction of `-∇S` by a step size `α`
- Update the point to `x_1 = x_0 + α * -∇S`
- Repeat steps 2-4 until convergence

**Example:**

Suppose we want to minimize the function `f(x) = x^2 + 3x + 2` using the NR method. We start at `x_0 = 1` and compute the target value `y_star = 0`:

`S = (x^2 + 3x + 2 - 0)^2 = (1^2 + 3*1 + 2)^2 = 36`

We move in the direction of `-∇S` by a step size `α = 0.1`:

`x_1 = x_0 + α * -∇S = 1 + 0.1 * (-6) = 0.9`

We repeat this process until convergence:

|x_2| = x_1 - α _ ∇S = 0.9 - 0.1 _ (-6) = 0.99

|...|

The optimal solution is `x_star = -1.5` where `f(x_star) = (-1.5)^2 + 3*(-1.5) + 2 = 0`.

### Gradient Descent

Gradient Descent is a popular technique for unconstrained optimization. The basic idea is to move in the direction of the negative gradient of the function at each step.

**How it works:**

- Choose an initial point `x_0`
- Compute the gradient of the function at `x_0`, denoted as `∇f(x_0)`
- Move in the direction of `-∇f(x_0)` by a step size `α`
- Update the point to `x_1 = x_0 + α * -∇f(x_0)`
- Repeat steps 2-4 until convergence

**Example:**

Suppose we want to minimize the function `f(x) = x^2` using Gradient Descent. We start at `x_0 = 1` and compute the gradient at `x_0`:

`∇f(x_0) = ∂f/∂x = 2x_0 = 2`

We move in the direction of `-∇f(x_0)` by a step size `α = 0.1`:

`x_1 = x_0 + α * -∇f(x_0) = 1 + 0.1 * (-2) = 0.8`

We repeat this process until convergence:

|x_2| = x_1 - α _ ∇f(x_1) = 0.8 - 0.1 _ 1.6 = 0.72

|...|

The optimal solution is `x_star = 0` where `f(x_star) = 0^2 = 0`.

### Mini-batch Gradient Descent

Mini-batch Gradient Descent is an extension of Gradient Descent that uses a mini-batch of data points to compute the gradient.

**How it works:**

- Choose an initial point `x_0`
- Choose a mini-batch size `k`
- Choose a random mini-batch of `k` data points
- Compute the gradient of the function at the mini-batch, denoted as `∇f(x_i)` for each data point `x_i`
- Move in the direction of `-∑∇f(x_i)` by a step size `α`
- Update the point to `x_1 = x_0 + α * -∑∇f(x_i)`
- Repeat steps 2-4 until convergence

**Example:**

Suppose we want to minimize the function `f(x) = x^2` using Mini-batch Gradient Descent. We start at `x_0 = 1` and choose a mini-batch size `k = 10`. We choose a random mini-batch of 10 data points `{x_1, x_2, ..., x_10}`:

`∇f(x_i) = ∂f/∂x_i = 2x_i` for each data point `x_i`

We compute the gradient at the mini-batch:

`∑∇f(x_i) = ∑(2x_i) = 2 * (x_1 + x_2 + ... + x_10)`

We move in the direction of `-∑∇f(x_i)` by a step size `α = 0.1`:

`x_1 = x_0 + α * -∑∇f(x_i) = 1 + 0.1 * (-2 * (x_1 + x_2 + ... + x_10))`

We repeat this process until convergence:

|x_2| = x_1 - α _ ∑∇f(x_1) = 0.8 - 0.1 _ (-2 \* (x_1 + x_2 + ... + x_10))

|...|

The optimal solution is `x_star = 0` where `f(x_star) = 0^2 = 0`.

### Stochastic Gradient Descent

Stochastic Gradient Descent is an extension of Gradient Descent that uses only one data point at a time to compute the gradient.

**How it works:**

- Choose an initial point `x_0`
- Choose a step size `α`
- Choose a random data point `x_i`
- Compute the gradient of the function at `x_i`, denoted as `∇f(x_i)`
- Move in the direction of `-∇f(x_i)` by a step size `α`
- Update the point to `x_1 = x_0 + α * -∇f(x_i)`
- Repeat steps 2-4 until convergence

**Example:**

Suppose we want to minimize the function `f(x) = x^2` using Stochastic Gradient Descent. We start at `x_0 = 1` and choose a step size `α = 0.1`. We choose a random data point `x_i`:

`∇f(x_i) = ∂f/∂x_i = 2x_i` for each data point `x_i`

We compute the gradient at `x_i`:

`∇f(x_i) = 2x_i`

We move in the direction of `-∇f(x_i)` by a step size `α`:

`x_1 = x_0 + α * -∇f(x_i) = 1 + 0.1 * (-2x_i)`

We repeat this process until convergence:

|x_2| = x_1 - α _ ∇f(x_1) = 0.8 - 0.1 _ 2x_1

|...|

The optimal solution is `x_star = 0` where `f(x_star) = 0^2 = 0`.

## Conclusion

In this section, we have explored several unconstrained optimization techniques, including the method of steepest ascent/descent, Non-Linear Regresssion (NR) method, Gradient Descent, Mini-batch Gradient Descent, and Stochastic Gradient Descent. Each technique has its strengths and weaknesses, and the choice of technique depends on the specific problem and data.
