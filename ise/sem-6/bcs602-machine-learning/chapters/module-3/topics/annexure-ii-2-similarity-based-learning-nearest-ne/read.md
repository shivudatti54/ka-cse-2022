# Similarity-based Learning

=====================================

## Nearest-Neighbor Learning

---

Nearest-Neighbor Learning is a type of supervised learning algorithm where the new data point is classified based on its similarity to the existing data points in the training set.

**Definition:** Nearest-Neighbor Learning is a type of supervised learning algorithm where the new data point is classified based on its similarity to the existing data points in the training set.

**How it works:**

1.  Train the model on a dataset of labeled examples.
2.  When a new, unseen data point is presented, the model finds the k most similar data points in the training set.
3.  The new data point is then classified based on the majority vote of the k most similar data points.

**Example:**

Suppose we want to classify a new data point as either "class A" or "class B" based on a dataset of labeled examples. If the training set contains the following data points:

| Feature 1 | Feature 2 | Class |
| --------- | --------- | ----- |
| 1.2       | 3.4       | A     |
| 2.1       | 3.5       | B     |
| 1.5       | 3.2       | A     |
| 2.2       | 3.3       | B     |

If the new data point has the following features: 1.3, 3.4, we would find the k most similar data points as follows:

- The distance between the new data point and the first data point (1.2, 3.4) is sqrt((1.3-1.2)^2 + (3.4-3.4)^2) = 0.1.
- The distance between the new data point and the second data point (2.1, 3.5) is sqrt((1.3-2.1)^2 + (3.4-3.5)^2) = 0.4.
- The distance between the new data point and the third data point (1.5, 3.2) is sqrt((1.3-1.5)^2 + (3.4-3.2)^2) = 0.1.
- The distance between the new data point and the fourth data point (2.2, 3.3) is sqrt((1.3-2.2)^2 + (3.4-3.3)^2) = 0.3.

We would then find the k most similar data points as the first and third data points (1.2, 3.4) and (1.5, 3.2) respectively.

**Classification:**

Based on the majority vote of the k most similar data points, the new data point would be classified as "class A".

### Code

```python
import numpy as np
from scipy.spatial import distance

def nearest_neighbor(data, new_point, k=3):
    # Calculate the distance between the new point and each data point
    distances = [distance.euclidean(new_point, point) for point in data]

    # Get the indices of the k most similar data points
    indices = np.argsort(distances)[:k]

    # Get the labels of the k most similar data points
    labels = [data[i][2] for i in indices]

    # Classify the new point based on the majority vote
    if len(set(labels)) == 1:
        return labels[0]
    else:
        return "Unclassified"

# Example usage
data = np.array([[1.2, 3.4, 0], [2.1, 3.5, 1], [1.5, 3.2, 0], [2.2, 3.3, 1]])

new_point = np.array([1.3, 3.4])
print(nearest_neighbor(data, new_point))
```

## Weighted K-Nearest-Neighbor Algorithm

---

The Weighted K-Nearest-Neighbor Algorithm is a variation of the Nearest-Neighbor Learning algorithm where the distance between the new data point and each data point is weighted based on the confidence of the data point.

**Definition:** The Weighted K-Nearest-Neighbor Algorithm is a variation of the Nearest-Neighbor Learning algorithm where the distance between the new data point and each data point is weighted based on the confidence of the data point.

**How it works:**

1.  Train the model on a dataset of labeled examples.
2.  When a new, unseen data point is presented, the model finds the k most similar data points in the training set.
3.  For each data point, calculate the weight based on the confidence of the data point.
4.  Calculate the weighted sum of the distances between the new data point and each data point.
5.  Classify the new data point based on the class of the data point with the minimum weighted sum.

**Example:**

Suppose we want to classify a new data point as either "class A" or "class B" based on a dataset of labeled examples. If the training set contains the following data points:

| Feature 1 | Feature 2 | Class | Confidence |
| --------- | --------- | ----- | ---------- |
| 1.2       | 3.4       | A     | 0.8        |
| 2.1       | 3.5       | B     | 0.6        |
| 1.5       | 3.2       | A     | 0.9        |
| 2.2       | 3.3       | B     | 0.7        |

If the new data point has the following features: 1.3, 3.4, we would find the k most similar data points as follows:

- The distance between the new data point and the first data point (1.2, 3.4) is sqrt((1.3-1.2)^2 + (3.4-3.4)^2) = 0.1.
- The distance between the new data point and the second data point (2.1, 3.5) is sqrt((1.3-2.1)^2 + (3.4-3.5)^2) = 0.4.
- The distance between the new data point and the third data point (1.5, 3.2) is sqrt((1.3-1.5)^2 + (3.4-3.2)^2) = 0.1.
- The distance between the new data point and the fourth data point (2.2, 3.3) is sqrt((1.3-2.2)^2 + (3.4-3.3)^2) = 0.3.

We would then calculate the weights as follows:

- The weight of the first data point is 0.8 x 0.1 = 0.08.
- The weight of the second data point is 0.6 x 0.4 = 0.24.
- The weight of the third data point is 0.9 x 0.1 = 0.09.
- The weight of the fourth data point is 0.7 x 0.3 = 0.21.

We would then calculate the weighted sum of the distances as follows:

- The weighted sum of the first data point is 0.08 x 0.1 = 0.008.
- The weighted sum of the second data point is 0.24 x 0.4 = 0.096.
- The weighted sum of the third data point is 0.09 x 0.1 = 0.009.
- The weighted sum of the fourth data point is 0.21 x 0.3 = 0.063.

We would then classify the new data point based on the class of the data point with the minimum weighted sum as follows:

- The minimum weighted sum is 0.009, which corresponds to the third data point (1.5, 3.2).
- Therefore, the new data point would be classified as "class A".

### Code

```python
import numpy as np
from scipy.spatial import distance

def weighted_knn(data, new_point, k=3):
    # Calculate the distance between the new point and each data point
    distances = [distance.euclidean(new_point, point) for point in data]

    # Calculate the weights based on the confidence of each data point
    weights = [point[2] * distance for point, distance in zip(data, distances)]

    # Calculate the weighted sum of the distances
    weighted_sums = [weight * distance for weight, distance in zip(weights, distances)]

    # Get the indices of the k most similar data points
    indices = np.argsort(weighted_sums)[:k]

    # Get the labels of the k most similar data points
    labels = [data[i][2] for i in indices]

    # Classify the new point based on the majority vote
    if len(set(labels)) == 1:
        return labels[0]
    else:
        return "Unclassified"

# Example usage
data = np.array([[1.2, 3.4, 0], [2.1, 3.5, 1], [1.5, 3.2, 0], [2.2, 3.3, 1]])

new_point = np.array([1.3, 3.4])
print(weighted_knn(data, new_point))
```

## Nearest Centroid Classifier

---

The Nearest Centroid Classifier is a type of supervised learning algorithm where the new data point is classified based on the similarity between its feature vector and the centroids of the classes.

**Definition:** The Nearest Centroid Classifier is a type of supervised learning algorithm where the new data point is classified based on the similarity between its feature vector and the centroids of the classes.

**How it works:**

1.  Train the model on a dataset of labeled examples.
2.  When a new, unseen data point is presented, the model finds the closest centroid to the feature vector of the new data point.
3.  Classify the new data point based on the class of the closest centroid.

**Example:**

Suppose we want to classify a new data point as either "class A" or "class B" based on a dataset of labeled examples. If the training set contains the following data points:

| Feature 1 | Feature 2 | Class |
| --------- | --------- | ----- |
| 1.2       | 3.4       | A     |
| 2.1       | 3.5       | B     |
| 1.5       | 3.2       | A     |
| 2.2       | 3.3       | B     |

We would first calculate the centroids of the classes as follows:

- Centroid of class A: (1.2 + 1.5) / 2 = 1.35
- Centroid of class B: (2.1 + 2.2) / 2 = 2.15

We would then find the closest centroid to the feature vector of the new data point as follows:

- Distance between the new data point (1.3, 3.4) and the centroid of class A (1.35) is sqrt((1.3-1.35)^2 + (3.4-3.4)^2) = 0.015.
- Distance between the new data point (1.3, 3.4) and the centroid of class B (2.15) is sqrt((1.3-2.15)^2 + (3.4-3.15)^2) = 0.665.

We would then classify the new data point based on the class of the closest centroid as follows:

- The closest centroid is the centroid of class A.
- Therefore, the new data point would be classified as "class A".

### Code

```python
import numpy as np

def nearest_centroid(data, new_point):
    # Calculate the centroids of the classes
    centroids = [np.mean(data[data[:, 2] == i]) for i in np.unique(data[:, 2])]

    # Calculate the distance between the new point and each centroid
    distances = [np.linalg.norm(new_point - centroid) for centroid in centroids]

    # Get the index of the closest centroid
    index = np.argmin(distances)

    # Classify the new point based on the class of the closest centroid
    if index == 0:
        return "class A"
    else:
        return "class B"

# Example usage
data = np.array([[1.2, 3.4, 0], [2.1, 3.5, 1], [1.5, 3.2, 0], [2.2, 3.3, 1]])

new_point = np.array([1.3, 3.4])
print(nearest_centroid(data, new_point))
```

## Locally Weighted

---

Locally Weighted is a type of supervised learning algorithm where the new data point is classified based on the weighted average of the labels of the nearest data points.

**Definition:** Locally Weighted is a type of supervised learning algorithm where the new data point is classified based on the weighted average of the labels of the nearest data points.

**How it works:**

1.  Train the model on a dataset of labeled examples.
2.  When a new, unseen data point is presented, the model finds the k nearest data points in the training set.
3.  For each nearest data point, calculate the weight based on the distance between the new data point and the data point.
4.  Calculate the weighted sum of the labels of the nearest data points.
5.  Classify the new data point based on the class of the data point with the minimum weighted sum.

**Example:**

Suppose we want to classify a new data point as either "class A" or "class B" based on a dataset of labeled examples. If the training set contains the following data points:

| Feature 1 | Feature 2 | Class |
| --------- | --------- | ----- |
| 1.2       | 3.4       | A     |
| 2.1       | 3.5       | B     |
| 1.5       | 3.2       | A     |
| 2.2       | 3.3       | B     |

If the new data point has the following features: 1.3, 3.4, we would find the k nearest data points as follows:

- The distance between the new data point and the first data point (1.2, 3.4) is sqrt((1.3-1.2)^2 + (3.4-3.4)^2) = 0.1.
- The distance between the new data point and the second data point (2.1, 3.5) is sqrt((1.3-2.1)^2 + (3.4-3.5)^2) = 0.4.
- The distance between the new data point and the third data point (1.5, 3.2) is sqrt((1.3-1.5)^2 + (3.4-3.2)^2) = 0.1.
- The distance between the new data point and the fourth data point (2.2, 3.3) is sqrt((1.3-2.2)^2 + (3.4-3.3)^2) = 0.3.

We would then calculate the weights as follows:

- The weight of the first data point is 0.1 x 1 = 0.1.
- The weight of the second data point is 0.4 x 0.5 = 0.2.
- The weight of the third data point is 0.1 x 1 = 0.1.
- The weight of the fourth data point is 0.3 x 0.4 = 0.12.

We would then calculate the weighted sum of the labels as follows:

- The weighted sum of the first data point is 0.1 x 0 = 0.
- The weighted sum of the second data point is 0.2 x 1 = 0.2.
- The weighted sum of the third data point is 0.1 x 0 = 0.
- The weighted sum of the fourth data point is 0.12 x 0 = 0.

We would then classify the new data point based on the class of the data point with the minimum weighted sum as follows:

- The minimum weighted sum is 0, which corresponds to the first data point (1.2, 3.4).
- Therefore, the new data point would be classified as "class A".

### Code

```python
import numpy as np

def locally_weighted(data, new_point, k=3):
    # Calculate the distances between the new point and each data point
    distances = [np.linalg.norm(new_point - point) for point in data]

    # Calculate the weights based on the distances
    weights = [distance ** -1 for distance in distances]

    # Calculate the weighted sum of the labels
    weighted_sums = [weights[i] * data[i][2] for i in range(k)]

    # Classify the new point based on the class of the data point with the minimum weighted sum
    if np.max(weighted_sums) == 0:
        return "class A"
    else:
        return "class B"

# Example usage
data = np.array([[1.2, 3.4, 0], [2.1, 3.5, 1], [1.5, 3.2, 0], [2.2, 3.3, 1]])

new_point = np.array([1.3, 3.4])
print(locally_weighted(data, new_point))
```
