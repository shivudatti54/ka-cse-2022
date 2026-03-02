# Chapter-4, 5, and 6 Revision Notes (Machine Learning)

=============================================

### Chapter 4 (4.2-4.5)

- **Definitions:**
  - Overfitting: When a model is too complex and performs well on training data but poorly on new data.
  - Regularization: Techniques to prevent overfitting, such as L1 and L2 regularization.
- **Theorems:**
  - Theorem 4.1: The bias-variance tradeoff states that a model's accuracy is determined by its bias (how far it misses the true mean) and variance (how much it wavers around the mean).
- **Important Formulas:**
  - L1 Regularization: `L1 = ||w||1 = ∑|w_i|`
  - L2 Regularization: `L2 = ||w||2 = (∑w_i^2)`

### Chapter 5 (5.1-5.3, 5.5-5.7)

- **Definitions:**
  - Supervised Learning: A type of learning where the model is trained on labeled data to predict outputs.
  - Unsupervised Learning: A type of learning where the model is trained on unlabeled data to identify patterns.
  - Deep Learning: A subfield of machine learning that uses neural networks with multiple layers.
- **Theorems:**
  - Theorem 5.1: The perceptron learning rule states that the weight update rule for a single neuron is `w_new = w_old + α * δ * x`
- **Important Formulas:**
  - Perceptron Learning Rule: `w_new = w_old + α * δ * x`
  - Bias correction: `y_new = sigmoid(w_new * x + b)`

### Chapter 6 (6.1, 6.2)

- **Definitions:**
  - Gradient Descent: An optimization algorithm used to minimize loss functions.
  - Stochastic Gradient Descent: A variant of gradient descent that uses a single sample from the training data to compute the gradient.
- **Theorems:**
  - Theorem 6.1: The convergence rate of gradient descent depends on the learning rate `α` and the size of the training dataset.
- **Important Formulas:**
  - Gradient Descent Update Rule: `w_new = w_old - α * ∇L(w)`
  - Stochastic Gradient Descent Update Rule: `w_new = w_old - α * ∇L(w) + (1 - α) * x * δ`
