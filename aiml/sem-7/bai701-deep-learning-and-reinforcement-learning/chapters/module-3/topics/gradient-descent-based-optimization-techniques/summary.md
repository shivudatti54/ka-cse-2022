# Gradient Descent-Based Optimization Techniques

**Definition and Importance**

- Gradient Descent (GD) is an optimization algorithm used to minimize the loss function of a model.
- GD-based techniques are widely used in supervised deep learning networks for training.

**Key Concepts**

- **Loss Function**: A function that measures the difference between the model's predictions and the actual outputs.
- **Gradient**: The rate of change of the loss function with respect to the model's parameters.
- **Optimization Algorithm**: An algorithm that iteratively updates the model's parameters to minimize the loss function.

**Gradient Descent Algorithm**

- **GD**: Minimize the loss function by iteratively updating the parameters using the gradient descent update rule:
  - `w_new = w_old - α * ∇L / ||∇L||`
- **Stochastic Gradient Descent (SGD)**: An variant of GD that uses a single data point to update the parameters at a time.
- **Mini-Batch Gradient Descent**: Uses a mini-batch of data points to update the parameters.

**Important Formulas and Theorems**

- **GD update rule**: `w_new = w_old - α * ∇L / ||∇L||`
- **Convergence Theorem**: If the loss function is convex, GD will converge to the global minimum.
- **Gradient Descent Acceleration**: Techniques like Nesterov Acceleration and Momentum can be used to accelerate the convergence of GD.

**Key Techniques**

- **Regularization**: Techniques like L1 and L2 regularization can be used to prevent overfitting.
- **Gradient Clipping**: Clips the gradients to prevent exploding gradients.
- **Learning Rate Schedulers**: Adjusts the learning rate during training to improve convergence.

**Important Theorems and Definitions**

- **Chain Rule**: Used to compute the gradient of the loss function with respect to the model's parameters.
- **Gradient Descent Convergence Theorem**: If the loss function is convex, GD will converge to the global minimum.
