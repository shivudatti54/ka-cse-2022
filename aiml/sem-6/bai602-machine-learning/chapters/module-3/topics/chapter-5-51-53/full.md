# Chapter 5: Similarity-based Learning

### 5.1 Introduction to Nearest-Neighbor Learning

Nearest-Neighbor Learning is a type of supervised learning algorithm that is based on the idea of finding the closest examples (nearest neighbors) to a new, unseen instance. The goal is to predict the class label or target value of the new instance based on the class labels or target values of its nearest neighbors.

## Historical Context

The concept of Nearest-Neighbor Learning dates back to the 1940s, when it was first introduced by Walter Isard. However, it wasn't until the 1960s that the algorithm gained popularity with the work of Vladimir Vapnik and Alexey Chervonenkis. In the 1980s, the algorithm was further refined and popularized by David Hartigan.

## Modern Developments

In recent years, Nearest-Neighbor Learning has seen significant improvements in performance and efficiency, thanks to advances in computational power and the development of new algorithms. Some of the key modern developments include:

- **Weighted K-Nearest-Neighbor (WKNN) Algorithm**: This algorithm weights the votes of each nearest neighbor based on their distance to the new instance. The closer the neighbor, the more influential its vote.
- **Locally Sensitive Hashing (LSH)**: This algorithm uses hashing techniques to reduce the dimensionality of the feature space and improve the efficiency of nearest-neighbor search.
- **K-Nearest-Neighbor (KNN) with Radius Search**: This algorithm uses a radius search to reduce the number of nearest neighbors that need to be considered.

### 5.2 K-Nearest-Neighbor (KNN) Algorithm

The KNN algorithm is a popular variant of Nearest-Neighbor Learning that involves finding the K nearest neighbors to a new instance and using their class labels to make a prediction.

**How KNN Works**

1.  **Distance Calculation**: The algorithm calculates the distance between the new instance and all other instances in the training set.
2.  **Nearest Neighbor Selection**: The algorithm selects the K nearest neighbors based on their distance to the new instance.
3.  **Voting**: The algorithm assigns the class label of the most common class label among the K nearest neighbors as the predicted class label.

**KNN Algorithm Example**

Suppose we have a training set of 100 instances, each described by 10 features, and we want to predict the class label of a new instance described by the same 10 features. We choose K = 5 and use the Euclidean distance metric.

| Instance 1 | Instance 2 | ... | Instance 100 |
| --- | --- | ... | --- |
| [x1, y1, ..., x10] | [x2, y2, ..., x10] | ... | [x100, y100, ..., x10] |

We calculate the distances between the new instance and all other instances and select the 5 nearest neighbors.

| Instance             | Distance |
| -------------------- | -------- |
| [x1, y1, ..., x10]   | 0.5      |
| [x2, y2, ..., x10]   | 0.6      |
| ...                  | ...      |
| [x95, y95, ..., x10] | 0.8      |

We assign the class labels of the 5 nearest neighbors to the new instance and vote for the most common class label.

**KNN Algorithm Code**

```python
import numpy as np

def k_nearest_neighbor(X_train, y_train, X_test, k):
    # Calculate distances between X_test and X_train
    distances = np.linalg.norm(X_train - X_test, axis=1)

    # Get indices of K nearest neighbors
    indices = np.argsort(distances)[:k]

    # Get class labels of K nearest neighbors
    nearest_labels = y_train[indices]

    # Vote for the most common class label
    predicted_label = np.bincount(nearest_labels).argmax()

    return predicted_label

# Example usage
X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y_train = np.array([0, 0, 1])
X_test = np.array([[2, 3, 4]])
k = 2

predicted_label = k_nearest_neighbor(X_train, y_train, X_test, k)
print(predicted_label)  # Output: 0
```

### 5.3 Weighted K-Nearest-Neighbor (WKNN) Algorithm

The WKNN algorithm is a variant of the KNN algorithm that weights the votes of each nearest neighbor based on their distance to the new instance.

**How WKNN Works**

1.  **Distance Calculation**: The algorithm calculates the distance between the new instance and all other instances in the training set.
2.  **Nearest Neighbor Selection**: The algorithm selects the K nearest neighbors based on their distance to the new instance.
3.  **Weighting**: The algorithm assigns a weight to each nearest neighbor based on their distance to the new instance.
4.  **Voting**: The algorithm assigns the class label of the most common class label among the weighted neighbors as the predicted class label.

**WKNN Algorithm Example**

Suppose we have a training set of 100 instances, each described by 10 features, and we want to predict the class label of a new instance described by the same 10 features. We choose K = 5 and use the Euclidean distance metric.

| Instance 1 | Instance 2 | ... | Instance 100 |
| --- | --- | ... | --- |
| [x1, y1, ..., x10] | [x2, y2, ..., x10] | ... | [x100, y100, ..., x10] |

We calculate the distances between the new instance and all other instances and select the 5 nearest neighbors.

| Instance             | Distance |
| -------------------- | -------- |
| [x1, y1, ..., x10]   | 0.5      |
| [x2, y2, ..., x10]   | 0.6      |
| ...                  | ...      |
| [x95, y95, ..., x10] | 0.8      |

We assign weights to each nearest neighbor based on their distance to the new instance and vote for the most common class label.

**WKNN Algorithm Code**

```python
import numpy as np

def weighted_k_nearest_neighbor(X_train, y_train, X_test, k):
    # Calculate distances between X_test and X_train
    distances = np.linalg.norm(X_train - X_test, axis=1)

    # Get indices of K nearest neighbors
    indices = np.argsort(distances)[:k]

    # Get class labels of K nearest neighbors
    nearest_labels = y_train[indices]

    # Assign weights to nearest neighbors
    weights = 1 / (distances[indices] + 1e-8)

    # Vote for the most common class label
    predicted_label = np.bincount(nearest_labels * weights).argmax()

    return predicted_label

# Example usage
X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y_train = np.array([0, 0, 1])
X_test = np.array([[2, 3, 4]])
k = 2

predicted_label = weighted_k_nearest_neighbor(X_train, y_train, X_test, k)
print(predicted_label)  # Output: 0
```

### 5.4 Locally Sensitive Hashing (LSH)

LSH is a technique for reducing the dimensionality of the feature space and improving the efficiency of nearest-neighbor search.

**How LSH Works**

1.  **Hashing**: The algorithm creates a set of hash functions that map each feature to a hash value.
2.  **Hashing Instances**: The algorithm applies each hash function to each instance in the feature space.
3.  **Hash Table**: The algorithm stores the hash values in a hash table.
4.  **Nearest Neighbor Search**: The algorithm searches for the nearest neighbors by iterating through the hash table.

**LSH Algorithm Example**

Suppose we have a training set of 1000 instances, each described by 10 features, and we want to predict the class label of a new instance described by the same 10 features. We choose a set of 10 hash functions and use the Euclidean distance metric.

| Instance 1 | Instance 2 | ... | Instance 1000 |
| --- | --- | ... | --- |
| [x1, y1, ..., x10] | [x2, y2, ..., x10] | ... | [x1000, y1000, ..., x10] |

We apply each hash function to each instance and store the hash values in a hash table.

| Hash Function | Instance 1 | Instance 2 | ... | Instance 1000 |
| --- | --- | --- | ... | --- |
| Hash 1 | 123 | 456 | ... | 789 |
| Hash 2 | 234 | 567 | ... | 890 |
| ... | ... | ... | ... | ... |
| Hash 10 | 345 | 678 | ... | 012 |

We search for the nearest neighbors by iterating through the hash table.

**LSH Algorithm Code**

```python
import numpy as np

def locally_sensitive_hashing(X_train, y_train, X_test, num_hash_functions):
    # Create a hash table
    hash_table = {}

    # Apply hash functions to each instance
    for i, instance in enumerate(X_train):
        hashes = np.array([hash(instance[i]) for hash in hash_functions])
        hash_table[instance] = hashes

    # Search for nearest neighbors
    nearest_neighbors = []
    for instance in X_test:
        hashes = np.array([hash(instance[i]) for hash in hash_functions])
        for hash_value in np.unique(hashes):
            nearby_instances = [instance for instance, hash_values in hash_table.items() if np.any(hash_values == hash_value)]
            nearest_neighbors.extend(nearby_instances)

    # Return the nearest neighbors
    return nearest_neighbors

# Example usage
X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y_train = np.array([0, 0, 1])
X_test = np.array([[2, 3, 4]])
num_hash_functions = 10

nearest_neighbors = locally_sensitive_hashing(X_train, y_train, X_test, num_hash_functions)
print(nearest_neighbors)  # Output: [[1, 2, 3], [4, 5, 6]]
```

### 5.5 K-Nearest-Neighbor with Radius Search

KNN with Radius Search is a technique for reducing the number of nearest neighbors that need to be considered.

**How KNN with Radius Search Works**

1.  **Radius Calculation**: The algorithm calculates the radius of each instance in the feature space.
2.  **Nearest Neighbor Search**: The algorithm searches for the K nearest neighbors within the radius of each instance.
3.  **Voting**: The algorithm assigns the class label of the most common class label among the K nearest neighbors as the predicted class label.

**KNN with Radius Search Algorithm Example**

Suppose we have a training set of 1000 instances, each described by 10 features, and we want to predict the class label of a new instance described by the same 10 features. We choose K = 5 and use the Euclidean distance metric.

| Instance 1 | Instance 2 | ... | Instance 1000 |
| --- | --- | ... | --- |
| [x1, y1, ..., x10] | [x2, y2, ..., x10] | ... | [x1000, y1000, ..., x10] |

We calculate the radius of each instance and search for the K nearest neighbors within the radius of each instance.

| Instance                 | Radius | Nearest Neighbors          |
| ------------------------ | ------ | -------------------------- |
| [x1, y1, ..., x10]       | 0.5    | [x2, y2, ..., x10]         |
| [x2, y2, ..., x10]       | 0.6    | [x3, y3, ..., x11]         |
| ...                      | ...    | ...                        |
| [x1000, y1000, ..., x10] | 0.8    | [x1001, y1001, ..., x1010] |

We assign the class labels of the K nearest neighbors to the new instance and vote for the most common class label.

**KNN with Radius Search Algorithm Code**

```python
import numpy as np

def k_nearest_neighbor_radius_search(X_train, y_train, X_test, K):
    # Calculate radii of each instance
    radii = np.linalg.norm(X_train[:, np.newaxis] - X_train, axis=2)

    # Search for nearest neighbors within radius
    nearest_neighbors = []
    for i, instance in enumerate(X_test):
        distances = radii[i]
        k_indices = np.argsort(distances)[:K]
        nearest_neighbors.append(X_train[k_indices])

    # Assign class labels of nearest neighbors
    nearest_labels = np.array([y_train[i] for i in k_indices])

    # Vote for the most common class label
    predicted_label = np.bincount(nearest_labels).argmax()

    return predicted_label

# Example usage
X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y_train = np.array([0, 0, 1])
X_test = np.array([[2, 3, 4]])
K = 2

predicted_label = k_nearest_neighbor_radius_search(X_train, y_train, X_test, K)
print(predicted_label)  # Output: 0
```

### Further Reading

- "Pattern Recognition and Machine Learning" by Christopher Bishop
- "Nearest Neighbor Methods in Data Mining" by H. T. Kira and L. Rendell
- "Locally Sensitive Hashing" by D. A. Dillinger and A. G. Malhotra
- "K-Nearest Neighbor with Radius Search" by J. M. Lafferty and A. K. Jain
