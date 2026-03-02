# Unconstrained Optimization Methods

## **Overview**

Unconstrained optimization is a method to find the maximum or minimum of a scalar function in a multidimensional space. Key methods include:

- Steepest Ascent/Descent
- Newton's method (NR)
- Gradient Descent
- Mini-Batch Gradient Descent
- Stochastic Gradient Descent

### Steepest Ascent/Descent

---

- **Steepest Ascent**: Update direction by maximizing the dot product of the gradient and the current direction
- **Steepest Descent**: Update direction by minimizing the dot product of the gradient and the current direction
- **Convergence**: Not guaranteed, can get stuck in local optima

### Newton's Method (NR)

---

- **Newton's Method**: Update direction by subtracting the Hessian matrix multiplied by the gradient
- **Formula**: `x_new = x_old - H^{-1} \* g`
- **Hessian Matrix**: Second derivative of the function

### Gradient Descent

---

- **Gradient Descent**: Update direction by subtracting a fraction of the gradient
- **Formula**: `x_new = x_old - \* \* (g)`, where `\*` is learning rate
- **Convergence**: Guaranteed to converge to a local minimum

### Mini-Batch Gradient Descent

---

- **Mini-Batch Gradient Descent**: Update direction using a mini-batch of data
- **Formula**: `x_new = x_old - \* \* (g)`, where `g` is the gradient averaged over the mini-batch
- **Convergence**: Faster convergence than SGD

### Stochastic Gradient Descent

---

- **Stochastic Gradient Descent**: Update direction using a single data point
- **Formula**: `x_new = x_old - \* \* (g)`, where `g` is the gradient of the data point
- **Convergence**: Slowest convergence rate

## Key Formulas and Definitions

- **Gradient**: First derivative of the function
- **Hessian Matrix**: Second derivative of the function
- **Learning Rate**: Hyperparameter that controls the step size
- **Mini-Batch Size**: Number of data points used for averaging the gradient

## Important Theorems

- **Convergence Theorem**: Gradient Descent converges to a local minimum
- **Mini-Batch Convergence Theorem**: Mini-Batch Gradient Descent converges to a local minimum
