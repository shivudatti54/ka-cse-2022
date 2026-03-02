# **Training Convolution Neural Networks**

**Definition:** Convolutional Neural Networks (CNNs) are a type of neural network designed for image and video processing.

**Key Formulas and Theorems:**

- **Convolutional Layer:** $C(x) = \sum_{k=0}^{K-1} W_k \odot f(W_{k-1}x + b_{k-1})$
- **Activation Function:** $\sigma(z) = \frac{1}{1+e^{-z}}$ (ReLU)
- **Backpropagation:** $\frac{\partial L}{\partial W} = \frac{\partial L}{\partial y} \odot \frac{\partial y}{\partial W}$
- **Convolutional Layer:**
  - **Forward Pass:**

    $y = \sum_{k=0}^{K-1} W_k \odot f(W_{k-1}x + b_{k-1})$

  - **Backward Pass:**

    $\frac{\partial L}{\partial W} = \frac{\partial L}{\partial y} \odot \frac{\partial y}{\partial W}$

- **Pooling Layer:**
  - **Forward Pass:**

    $y = \max\_{i,j} (x_{i,j})$

  - **Backward Pass:**

    $\frac{\partial L}{\partial x} = \frac{\partial L}{\partial y} \odot \frac{\partial y}{\partial x}$

**Key Concepts:**

- **Filter Sizes:** Larger filter sizes capture more contextual information
- **Stride:** Larger stride reduces spatial dimensions
- **Padding:** Larger padding reduces border effects
- **Dilation:** Larger dilation rate increases receptive field without increasing filter size
- **Batch Normalization:** Normalizes input data for each mini-batch

**Training Strategies:**

- **Stochastic Gradient Descent (SGD):** Optimizes parameters using gradient descent
- **Mini-Batches:** Divides data into smaller batches for training
- **Learning Rate Schedulers:** Adjusts learning rate during training
- **Regularization Techniques:** L1 and L2 regularization for preventing overfitting

**Important Theorems:**

- **Boltzmann's Hierarchy:** Describes the probability distribution of a multivariate probability distribution
- **Entropy:** Measures the amount of uncertainty in a probability distribution
