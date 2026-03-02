# Unsupervised Learning: The K-MEANS Algorithm

=====================================================

## Introduction

---

Unsupervised learning is a type of machine learning where the algorithm discovers patterns and relationships in the data without prior knowledge of the correct output. One popular algorithm used in unsupervised learning is K-MEANS, a clustering algorithm that groups similar data points into clusters. In this study material, we will delve into the K-MEANS algorithm, dealing with noise, building a k-MEANS neural network, normalization, and a better weight update rule.

## What is K-MEANS?

---

K-MEANS is an unsupervised learning algorithm that groups similar data points into K clusters based on their features. The algorithm iteratively updates the cluster centroids until convergence. The goal is to minimize the sum of squared distances between each data point and its nearest centroid.

### How K-MEANS Works

1.  Initialize K centroids randomly.
2.  Assign each data point to the closest centroid.
3.  Update the centroid of each cluster by taking the mean of all data points assigned to it.
4.  Repeat steps 2-3 until convergence.

### Key Concepts

- **Centroids**: The central point of each cluster.
- **Distance**: The measure of how close a data point is to a centroid.
- **Assignment**: The process of assigning a data point to a cluster based on its distance to the centroid.

## Dealing with Noise

---

Noise is a common issue in K-MEANS, where the algorithm struggles to converge due to the presence of outliers or misaligned clusters. To deal with noise, we can use the following techniques:

- **Robust initialization**: Initialize the centroids using a robust method such as the median or interquartile range.
- **Weighted distance**: Use a weighted distance metric that gives more importance to closer data points.
- **Randomized initialization**: Randomly initialize the centroids and reassign data points to the closest centroid.

### Example: Handling Noise with Robust Initialization

Suppose we have a dataset with noisy outliers. We can use robust initialization to ensure the centroids are not affected by these outliers.

```python
import numpy as np

# Noisy dataset
data = np.array([[1, 2], [3, 4], [5, 6], [100, 100]])

# Robust initialization
centroids = np.array([np.median(data[:, 0]), np.median(data[:, 1])])
```

## The k-MEANS Neural Network

---

A k-MEANS neural network is a type of neural network that uses the K-MEANS algorithm to cluster data points. The network consists of an input layer, hidden layers, and an output layer.

### Architecture

- **Input Layer**: Takes in the input data
- **Hidden Layers**: Apply non-linear transformations to the input data
- **Output Layer**: Produces the cluster assignments

### Example: Building a k-MEANS Neural Network

```python
import numpy as np
import torch
import torch.nn as nn

class kMEANS(nn.Module):
    def __init__(self, k, input_dim):
        super(kMEANS, self).__init__()
        self.k = k
        self.input_dim = input_dim
        self.fc1 = nn.Linear(input_dim, 10)  # Hidden layer 1
        self.fc2 = nn.Linear(10, self.k)  # Hidden layer 2
        self.fc3 = nn.Linear(self.k, self.input_dim)  # Output layer

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # Activation function for hidden layer 1
        x = torch.relu(self.fc2(x))  # Activation function for hidden layer 2
        x = self.fc3(x)
        return x
```

## Normalization

---

Normalization is a technique used to scale the features of the data to a common range, usually between 0 and 1. This is useful for K-MEANS as it helps to ensure that all features are treated equally.

### Types of Normalization

- **Standardization**: Subtracts the mean and divides by the standard deviation for each feature.
- **Min-Max Scaler**: Scales the features to a common range, usually between 0 and 1.

### Example: Normalizing a Dataset

```python
import numpy as np

# Dataset
data = np.array([[1, 2], [3, 4], [5, 6]])

# Standardization
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
data_std = (data - mean) / std

# Min-Max Scaler
data_min_max = (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))
```

## A Better Weight Update Rule

---

The traditional weight update rule for K-MEANS uses the Euclidean distance between data points and centroids. However, this rule can be biased towards data points that are far away from the centroids. A better weight update rule is the **mean squared distance**, which takes into account the squared distances.

### Example: Using the Mean Squared Distance

```python
import numpy as np

# Dataset
data = np.array([[1, 2], [3, 4], [5, 6]])

# Mean squared distance
distances = np.sqrt(((data - centroids[:, np.newaxis]) ** 2).sum(axis=2))
w = 1 / (1 + distances ** 2)
```

## Using Comp

---

**Comp** stands for **Connected Components**. It is a technique used to group connected data points into clusters. **Comp** is useful when the clusters are not spherical or when the data is not linearly separable.

### Example: Using Comp

```python
import numpy as np

# Dataset
data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

# Comp
def comp(data):
    max_val = np.max(data, axis=1)
    min_val = np.min(data, axis=1)
    for i in range(len(max_val)):
        if data[:, i] == min_val[i]:
            return i
    return -1

comp_result = comp(data)
print(comp_result)
```

This concludes the study material on unsupervised learning: the K-MEANS algorithm, dealing with noise, building a k-MEANS neural network, normalization, and a better weight update rule.
