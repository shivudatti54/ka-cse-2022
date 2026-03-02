# **Ch 4.2 Revision Notes**

**Topic:** Training Supervised Deep Learning Networks

**Key Points:**

- **Backpropagation Algorithm:**
  - A widely used algorithm for training supervised deep learning networks
  - Computes the gradients of the loss function with respect to the model's parameters
  - Used for optimization of the model's parameters
- **Activation Functions:**
  - Introduced non-linearity in the model
  - Examples: ReLU, sigmoid, tanh
- **Loss Functions:**
  - Measures the difference between predicted and actual outputs
  - Examples: Mean Squared Error (MSE), Cross-Entropy Loss
- **Optimization Algorithms:**
  - Examples: Stochastic Gradient Descent (SGD), Adam, RMSprop
- **Regularization Techniques:**
  - Examples: L1 Regularization, L2 Regularization

**Formulas and Definitions:**

- **Mean Squared Error (MSE):** $L = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$
- **Cross-Entropy Loss:** $L = -\sum_{i=1}^{n} y_i \log(\hat{y}_i)$
- **Activation Function:** $f(x) = \sigma(x) = \frac{1}{1+e^{-x}}$
- **Stochastic Gradient Descent (SGD):** $w_t = w_{t-1} - \alpha \frac{\partial L}{\partial w_{t-1}}$

**Theorems:**

- **Universal Approximation Theorem:** Any continuous function can be approximated by a deep neural network
- **Polyak Learning Rate Algorithm:** A variant of the Adam optimization algorithm that adapts the learning rate based on the previous step's gradient
