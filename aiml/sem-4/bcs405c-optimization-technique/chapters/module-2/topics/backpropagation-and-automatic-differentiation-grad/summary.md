# Backpropagation and Automatic Differentiation

### Key Concepts

- **Backpropagation**: A method for computing the gradient of a loss function with respect to the model's parameters in a neural network.
- **Automatic Differentiation (AD)**: A technique for computing the gradient of a function by automatically differentiating it, without explicitly computing the derivatives.
- **Gradient Descent**: An optimization algorithm that minimizes the loss function by iteratively updating the model's parameters in the direction of the negative gradient.
- **Quadratic Cost**: A cost function that represents the difference between the predicted output and the actual output.

### Important Formulas and Definitions

- **Backpropagation Formula**: $\frac{\partial L}{\partial w} = \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial w}$, where $L$ is the loss function, $w$ is the model's parameter, and $z$ is the output of the layer.
- **Automatic Differentiation Formula**: $\frac{\partial f}{\partial x} \approx \frac{f(x + \epsilon) - f(x)}{\epsilon}$, where $f$ is the function, $x$ is the input, and $\epsilon$ is a small perturbation.
- **Gradient Descent Update Rule**: $w \leftarrow w - \alpha \cdot \frac{\partial L}{\partial w}$, where $w$ is the model's parameter, $\alpha$ is the learning rate, and $\frac{\partial L}{\partial w}$ is the gradient of the loss function with respect to the parameter.
- **Quadratic Cost Formula**: $L = \frac{1}{2} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$, where $y_i$ is the actual output, $\hat{y}_i$ is the predicted output, and $n$ is the number of samples.

### Theorems and Properties

- **Chain Rule**: $\frac{\partial L}{\partial w} = \sum_{i=1}^{n} \frac{\partial L}{\partial z_i} \cdot \frac{\partial z_i}{\partial w}$, where $z_i$ is the output of the $i^{th}$ layer.
- **Linearity of Gradient Descent**: $w^{(k+1)} = w^{(k)} - \alpha \cdot \frac{\partial L}{\partial w^{(k)}}$ is a linear combination of the previous parameters and the gradients.

### Revision Notes

- Backpropagation and automatic differentiation are used to compute the gradients of the loss function with respect to the model's parameters.
- Gradient descent is an optimization algorithm that uses the gradients to update the model's parameters.
- The quadratic cost function is used to measure the difference between the predicted output and the actual output.
- The gradient of the quadratic cost function is used to update the model's parameters using gradient descent.
