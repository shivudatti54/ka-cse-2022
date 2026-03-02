# **Backpropagation and Automatic Differentiation, Gradients in a Deep Network**

### Key Points

- **Backpropagation**: An optimization technique used in neural networks to minimize the loss function by propagating the error gradients backwards through the network.
- **Automatic Differentiation**: A method to compute the derivative of a function with respect to its inputs, used to compute gradients in deep networks.
- **Gradients in Deep Networks**: The derivative of the loss function with respect to the model's parameters, used to update the parameters during optimization.
- **Gradient of Quadratic Cost**: The gradient of the quadratic cost function with respect to the model's parameters, used to update the parameters during optimization.
- **Descending the Gradient of Cost**: Updating the model's parameters by moving in the opposite direction of the gradient, used to minimize the loss function.
- **Gradi**: The gradient of the loss function with respect to the model's parameters, used to update the parameters during optimization.

### Important Formulas and Definitions

- **Backpropagation Formula**: `dy/dx = dLoss/dx`
- **Automatic Differentiation Formula**: `dLoss/dx = dLoss/dy \* dy/dx`
- **Gradient Descent Formula**: `x_new = x_old - learning_rate \* dy/dx`
- **Quadratic Cost Function**: `J(x) = (x - y)^2`

### Theorems

- **Chain Rule Theorem**: `dLoss/dx = dLoss/dy \* dy/dx`
- **Sum Rule Theorem**: `dLoss/dx = dLoss/dx1 + dLoss/dx2`

### Quick Revision

- Understand the concept of backpropagation and automatic differentiation.
- Know the formulas for computing gradients in deep networks.
- Understand the gradient descent algorithm.
- Be familiar with the quadratic cost function and its derivative.
- Review the chain rule and sum rule theorems.
