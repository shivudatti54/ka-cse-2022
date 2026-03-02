# **Similarity-based Learning: Nearest-Neighbor Learning and Weighted K-Nearest-Neighbor Algorithm**

## \*\*4.2 Nearest-Neighbor Learning

### Definition

Nearest-neighbor learning is a type of supervised learning algorithm where the target variable is predicted by finding the class label of the most similar instance in the training data.

### How it Works

1.  The algorithm is trained on a dataset of labeled instances.
2.  When a new, unseen instance is presented, the algorithm computes the distance between this instance and all the instances in the training dataset.
3.  The instance with the smallest distance is selected as the nearest neighbor.
4.  The class label of the nearest neighbor is assigned as the prediction for the new instance.

### Advantages

- Simple to implement
- Handles high-dimensional data well
- Does not require feature engineering

### Disadvantages

- Computationally expensive for large datasets
- Sensitive to outliers

### Example

Suppose we have a dataset of labeled iris flowers, and we want to predict the species of a new, unseen flower. The nearest-neighbor algorithm would compute the distance between this flower and all the instances in the training dataset, and then select the instance with the smallest distance as the nearest neighbor. The class label of this nearest neighbor would be assigned as the prediction for the new flower.

### Code

Here's an example of how you can implement the nearest-neighbor algorithm in Python:

```python
import numpy as np

# Define the dataset
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([0, 0, 1, 1])

# Define a function to compute the distance between two instances
def distance(x1, x2):
    return np.linalg.norm(x1 - x2)

# Define a function to find the nearest neighbor
def nearest_neighbor(x):
    d = [distance(x, xi) for xi in X]
    idx = np.argmin(d)
    return y[idx]

# Compute the prediction for a new instance
new_x = np.array([9, 10])
prediction = nearest_neighbor(new_x)
print(prediction)
```

## \*\*4.3 Weighted K-Nearest-Neighbor Algorithm

### Definition

The weighted K-nearest-neighbor algorithm is an extension of the nearest-neighbor algorithm where the instances are assigned weights, and the weights are used to compute the distance.

### How it Works

1.  The algorithm is trained on a dataset of labeled instances, where each instance is assigned a weight.
2.  When a new, unseen instance is presented, the algorithm computes the weighted distance between this instance and all the instances in the training dataset.
3.  The instance with the smallest weighted distance is selected as the nearest neighbor.
4.  The class label of the nearest neighbor is assigned as the prediction for the new instance.

### Advantages

- Handles high-dimensional data well
- Does not require feature engineering
- Can handle noisy data better than the standard nearest-neighbor algorithm

### Disadvantages

- Computationally expensive for large datasets
- Requires careful selection of the weights

### Example

Suppose we have a dataset of labeled iris flowers, and we want to predict the species of a new, unseen flower. The weighted K-nearest-neighbor algorithm would assign weights to each instance in the training dataset, and then compute the weighted distance between the new instance and all the instances in the training dataset. The instance with the smallest weighted distance would be selected as the nearest neighbor, and its class label would be assigned as the prediction for the new flower.

### Code

Here's an example of how you can implement the weighted K-nearest-neighbor algorithm in Python:

```python
import numpy as np

# Define the dataset
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([0, 0, 1, 1])
weights = np.array([0.5, 0.3, 0.2, 0.3])

# Define a function to compute the weighted distance between two instances
def weighted_distance(x1, xi):
    return np.sum(weights * distance(x1, xi))

# Define a function to find the nearest neighbor
def weighted_knn(x):
    d = [weighted_distance(x, xi) for xi in X]
    idx = np.argmin(d)
    return y[idx]

# Compute the prediction for a new instance
new_x = np.array([9, 10])
prediction = weighted_knn(new_x)
print(prediction)
```

## \*\*4.4 Limitations of Similarity-based Learning

- Computationally expensive for large datasets
- Sensitive to outliers
- Requires careful selection of the weights
- Does not handle high-dimensional data well

## \*\*4.5 Conclusion

Similarity-based learning, including nearest-neighbor learning and weighted K-nearest-neighbor algorithm, is a type of supervised learning algorithm that has several advantages, including handling high-dimensional data well and not requiring feature engineering. However, it also has several limitations, including being computationally expensive for large datasets and sensitive to outliers.
