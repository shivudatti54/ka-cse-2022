# Gradient Descent-Based Optimization Techniques

### Introduction

Gradient Descent is a popular optimization algorithm used to find the minimum of a function. It is widely used in supervised deep learning networks, particularly for training models.

### Key Concepts

- **Gradient Descent**: An optimization algorithm that iteratively updates the model parameters to minimize the loss function.
- **Cost Function/Loss Function**: The function that measures the difference between the model's predictions and the actual labels.
- **Gradient**: The rate of change of the cost function with respect to the model parameters.
- **Hessian Matrix**: The matrix of second derivatives of the cost function with respect to the model parameters.

### Key Formulas

- **Gradient Descent Update Rule**: `w_new = w_old - α \* ∇L(w_old)`
- **Gradient Descent with Momentum**: `w_new = w_old - α \* γ \* ∇L(w_old) + β \* w_old`
- **Hessian Matrix**: `H = ∇²L(w_old)`

### Important Theorems

- **The Gradient Descent Algorithm Converges**: The gradient descent algorithm will converge to a minimum of the cost function if the learning rate α is smaller than 1 and the Hessian matrix is positive semi-definite.
- **The Convergence Speed of Gradient Descent**: The convergence speed of gradient descent is influenced by the learning rate α and the Hessian matrix.

### Types of Gradient Descent

- **Stochastic Gradient Descent (SGD)**: Uses a single example from the training dataset to update the model parameters.
- **Mini-Batch Gradient Descent**: Uses a small batch of examples from the training dataset to update the model parameters.
- **Batch Gradient Descent**: Uses the entire training dataset to update the model parameters.

### Advantages and Disadvantages

- **Advantages**:
  - Simple to implement.
  - Fast convergence.
  - Robust to non-convex optimization problems.
- **Disadvantages**:
  - May converge to a local minimum.
  - Requires careful choice of hyperparameters.
  - May not work well for large-scale optimization problems.
