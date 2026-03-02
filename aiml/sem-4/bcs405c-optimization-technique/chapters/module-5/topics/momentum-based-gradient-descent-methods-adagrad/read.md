# **Momentum-based Gradient Descent Methods: Adagrad**

## **Table of Contents**

- [Introduction](#introduction)
- [Defining Gradient Descent](#defining-gradient-descent)
- [Momentum-based Gradient Descent Methods](#momentum-based-gradient-descent-methods)
- [Adagrad Algorithm](#adagrad-algorithm)
- [Key Concepts](#key-concepts)
- [Example Use Cases](#example-use-cases)

## **Introduction**

Gradient Descent (GD) is a widely used optimization technique to minimize the loss function in machine learning models. However, GD can converge slowly or get stuck in local minima, especially when the learning rate is too high. Momentum-based gradient descent methods, such as Adagrad, are designed to address these issues.

## **Defining Gradient Descent**

Gradient Descent is an optimization algorithm that iteratively updates the model parameters to minimize the loss function. The update rule is given by:

`w_new = w_old - α * ∇L(w_old)`

where `w_old` is the previous weight, `α` is the learning rate, and `∇L(w_old)` is the gradient of the loss function with respect to the weight.

## **Momentum-based Gradient Descent Methods**

Momentum-based gradient descent methods add a momentum term to the update rule to help the algorithm escape local minima. The momentum term is a fraction of the previous update, which helps the algorithm to converge faster.

## **Adagrad Algorithm**

Adagrad is a popular momentum-based gradient descent method that adapts the learning rate for each parameter individually. The update rule is given by:

`w_new = w_old - α * ∇L(w_old) / ||∇L(w_old)||^2`

where `w_old` is the previous weight, `α` is the learning rate, `∇L(w_old)` is the gradient of the loss function with respect to the weight, and `||∇L(w_old)||^2` is the squared norm of the gradient.

The key innovation of Adagrad is that it adapts the learning rate for each parameter individually, which helps to prevent overfitting and improve convergence.

## **Key Concepts**

- **Momentum**: a fraction of the previous update that helps the algorithm to converge faster
- **Adaptive learning rate**: adjusts the learning rate for each parameter individually
- **Squared norm**: the squared value of the gradient, used to normalize the update rule

## **Example Use Cases**

Adagrad is widely used in deep learning models, such as neural networks and word embeddings. Here are a few examples:

- **Language Modeling**: Adagrad is used to train language models, such as word2vec and BERT.
- **Image Classification**: Adagrad is used to train convolutional neural networks (CNNs) for image classification tasks.

## **Code Example**

Here is an example of how to implement Adagrad in Python:

```python
import numpy as np

def adagrad(X, y, learning_rate=0.01, max_iter=1000):
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    gradients = np.zeros(n_features)

    for _ in range(max_iter):
        for i in range(n_features):
            # Compute gradient
            gradient = np.mean((X * weights) - y)
            gradients[i] += gradient ** 2

            # Update weights
            weights[i] -= learning_rate * gradient / np.sqrt(gradients[i] + 1e-8)

    return weights
```

Note that this is a simplified example and in practice, you would need to handle more complex scenarios, such as regularization, batch normalization, and more.
