# **Challenges in Training Deep Networks**

### Introduction

- Deep learning models consist of multiple layers, leading to increased computational complexity and training difficulties.
- Challenges in training deep networks can be categorized into three main areas: model capacity, optimization, and regularization.

### Model Capacity

- **The Curse of Dimensionality**: As the number of layers and units increases, the capacity of the model grows exponentially, leading to overfitting.
- ** vanishing gradients**: Gradient gradients are multiplied together during backpropagation, causing gradients to approach zero, making optimization challenging.

### Optimization

- **Mini-batch gradient descent**: Gradient descent updates the model parameters using a small batch of data, which can be insufficient for deep networks.
- **Stochastic gradient descent**: SGD updates the model parameters using a single sample, which can be inaccurate.

### Regularization

- **L1 and L2 regularization**: Regularization techniques, such as L1 and L2 regularization, can reduce overfitting by penalizing large weights.
- **Dropout**: Regularization technique that randomly sets a fraction of units to zero during training.

### Important Formulas

- **Backpropagation update rule**: `w_new = w_old - α * ∇L / ∇w`
- **Gradient descent update rule**: `w_new = w_old - α * ∇L`
- **Dropout formula**: `p = (1 - dropout_rate) * x + dropout_rate * 0`

### Key Definitions

- **Overfitting**: Model that fits the training data too closely, generalizing poorly to new data.
- **Underfitting**: Model that fails to capture the underlying patterns in the training data.

### Theorems

- **Theorem:** If the number of layers is too large, the model capacity can outgrow the available training data, leading to overfitting.
- **Theorem:** Regularization techniques, such as L1 and L2 regularization, can be used to reduce overfitting by penalizing large weights.

### Important Concepts

- **Model capacity**: Ability of the model to learn and represent complex patterns.
- **Optimization**: Algorithm used to update the model parameters to minimize the loss function.
- **Regularization**: Techniques used to prevent overfitting by penalizing large weights or complex models.
