# Bias-Variance Tradeoff and Regularization

## Introduction

In the realm of deep learning and machine learning, building models that generalize well to unseen data is the fundamental challenge. The bias-variance tradeoff is a critical concept that helps us understand and diagnose the performance of machine learning models. Introduced from classical statistical learning theory, this tradeoff explains the tension between a model's ability to fit training data (low bias) and its sensitivity to fluctuations in the training data (low variance).

When we train a deep neural network, we often encounter two common problems: underfitting and overfitting. Underfitting occurs when the model is too simple to capture the underlying patterns in the data, resulting in poor performance on both training and test data. Overfitting happens when the model learns the training data too well, including noise and random fluctuations, leading to excellent training performance but poor generalization to new data. The bias-variance decomposition provides a mathematical framework to understand these phenomena.

Regularization techniques are the primary tools we use to navigate the bias-variance tradeoff. These methods add constraints or penalties to the learning process, discouraging overly complex models that tend to overfit. In deep learning, regularization has become even more crucial given the massive number of parameters in modern neural networks. Understanding these concepts is essential for any computer science student at Delhi University, as they form the foundation for building robust, generalizable machine learning systems.

## Key Concepts

### Bias

Bias represents the error introduced by approximating a real-world problem with a simplified model. A high-bias model makes strong assumptions about the data and tends to underfit. Linear regression applied to non-linear data is a classic example of a high-bias model. Mathematically, bias is the difference between the expected prediction of our model and the true function we are trying to learn.

**Key characteristic:** High bias models have fewer parameters or overly restrictive assumptions, failing to capture important patterns in the data.

### Variance

Variance measures how much the model's predictions change when trained on different subsets of the training data. High-variance models are overly sensitive to the specific training samples and tend to overfit. Decision trees with unlimited depth exemplify high-variance models.

**Key characteristic:** High variance models have many parameters and can fit almost any training data, including noise.

### The Bias-Variance Decomposition

For a regression problem with squared error loss, the expected prediction error can be decomposed as:

**Expected Error = Bias² + Variance + Irreducible Error**

Where:
- **Bias²** = (E[prediction] - true value)² — measures systematic error
- **Variance** = E[(prediction - E[prediction])²] — measures sensitivity to training data
- **Irreducible Error** — inherent noise in the data that no model can eliminate

This decomposition shows that we cannot minimize both bias and variance simultaneously; we must find an optimal balance.

### The Tradeoff Visualized

As model complexity increases:
- **Bias decreases** — the model becomes more flexible and can fit training data better
- **Variance increases** — the model becomes more sensitive to training data fluctuations

The optimal model complexity minimizes the total error at the "sweet spot" where bias² and variance are balanced.

### Regularization Techniques

**L1 Regularization (Lasso):** Adds a penalty term proportional to the sum of absolute values of weights: λ∑|wᵢ|. This promotes sparsity, driving some weights to exactly zero, effectively performing feature selection.

**L2 Regularization (Ridge):** Adds a penalty term proportional to the sum of squared weights: λ∑wᵢ². This shrinks weights toward zero but rarely makes them exactly zero, providing better numerical stability.

**Elastic Net:** Combines L1 and L2 regularization: λ₁∑|wᵢ| + λ₂∑wᵢ², capturing benefits of both methods.

**Dropout:** During training, randomly sets a fraction of neuron outputs to zero with probability p. This prevents co-adaptation of neurons and acts as an ensemble of many sub-networks.

**Early Stopping:** Monitors validation error during training and stops when it starts increasing, preventing overfitting by limiting the number of training iterations.

**Data Augmentation:** Increases effective training set size through transformations (rotation, flipping, cropping for images), making the model robust to variations.

**Batch Normalization:** Normalizes layer inputs to have zero mean and unit variance, acting as a regularizer by adding slight noise through mini-batch statistics.

## Examples

### Example 1: Polynomial Regression Bias-Variance

Consider fitting a polynomial to data generated from y = sin(x) + noise.

**Scenario A (Underfitting):** Using a linear model (degree 1)
- The model cannot capture the sinusoidal pattern
- Training Error: 0.45, Test Error: 0.52
- High bias, low variance

**Scenario B (Optimal):** Using polynomial degree 5
- Captures the sinusoidal pattern without fitting noise
- Training Error: 0.08, Test Error: 0.09
- Balanced bias and variance

**Scenario C (Overfitting):** Using polynomial degree 15
- Passes through every training point including noise
- Training Error: 0.001, Test Error: 0.85
- Low bias, very high variance

### Example 2: Implementing L2 Regularization in Neural Networks

Consider a simple neural network with one hidden layer. Without regularization, the loss function is:

**L = (1/N)∑(yᵢ - ŷᵢ)²**

With L2 regularization (weight decay), we add:

**L_reg = L + (λ/2N)∑w²**

In PyTorch, this is implemented using the weight_decay parameter:

```python
# Without regularization
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# With L2 regularization (weight_decay = λ)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=0.01)
```

The weight_decay parameter automatically applies λw to the gradient during each update step, effectively shrinking weights toward zero.

### Example 3: Dropout in Practice

For a fully connected layer with 512 neurons, applying dropout with p=0.5:

```python
import torch.nn as nn

# During training: 50% of neurons are randomly dropped
self.dropout = nn.Dropout(p=0.5)
x = self.dropout(x)  # Randomly zeros out elements

# During inference: all neurons active (scale by p)
# PyTorch automatically handles this in eval() mode
```

At inference time, dropout is disabled, but the remaining active neurons receive scaled outputs (divided by p during training) to maintain the same expected output magnitude.

## Exam Tips

1. **Remember the bias-variance decomposition formula:** Expected Error = Bias² + Variance + Irreducible Error. This is frequently asked in DU exams.

2. **Distinguish underfitting from overfitting:** Underfitting shows high training and high test error; overfitting shows low training error but high test error.

3. **Know when to use L1 vs L2:** Use L1 (Lasso) for feature selection and sparsity; use L2 (Ridge) for general weight shrinkage and multicollinearity.

4. **Dropout is only active during training:** Remember that dropout is automatically disabled during evaluation/inference in frameworks like PyTorch and TensorFlow.

5. **Early stopping monitors validation error:** The key is to stop when validation error stops improving, not when training error is minimized.

6. **Regularization strength (λ) matters:** Too small λ provides little regularization (overfitting); too large λ causes underfitting by shrinking weights too much.

7. **Batch Normalization provides implicit regularization:** The stochasticity from computing mean/variance over mini-batches adds noise, acting as a regularizer.