# Chapter-4: Similarity-based Learning

## 4.2: Nearest-Neighbor Learning

Nearest-Neighbor Learning is a type of supervised learning algorithm that falls under the category of similarity-based learning. It's a straightforward approach that relies on finding the closest instances (nearest neighbors) in the feature space to make predictions.

### How Nearest-Neighbor Learning Works

Here's a step-by-step explanation of the algorithm:

1. **Data Collection**: Collect a dataset of instances, where each instance is represented by a set of features.
2. **Instance Representation**: Represent each instance as a point in the feature space.
3. **Distance Calculation**: Calculate the distance between each instance and all other instances in the dataset.
4. **Nearest Neighbor Selection**: Select the instance with the minimum distance as the nearest neighbor.
5. **Prediction**: Make a prediction based on the class label of the nearest neighbor.

### Types of Distance Metrics

Different distance metrics can be used to calculate the distance between instances, including:

- Euclidean Distance
- Manhattan Distance
- Minkowski Distance
- Cosine Distance

### Advantages and Disadvantages

Advantages:

- Simple to implement
- Can handle high-dimensional data
- Can be parallelized

Disadvantages:

- Computationally expensive
- Can be sensitive to outliers
- May not perform well with non-linearly separable data

### Example

Suppose we have a dataset of customers with features such as age, income, and credit score. We want to predict the likelihood of a customer defaulting on a loan. We can use Nearest-Neighbor Learning to find the nearest neighbor to a new customer and make a prediction based on their class label.

| Age | Income | Credit Score | Default |
| --- | ------ | ------------ | ------- |
| 25  | 50000  | 700          | No      |
| 30  | 60000  | 800          | No      |
| 35  | 70000  | 900          | Yes     |
| 40  | 80000  | 1000         | Yes     |

If we want to predict the likelihood of a new customer with age 28, income 55000, and credit score 750 defaulting on a loan, we can calculate the distances between this new customer and all other customers and select the nearest neighbor.

### Code Example

Here's an example implementation of Nearest-Neighbor Learning in Python using the Euclidean distance metric:

```python
import numpy as np

def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def nearest_neighbor(X, y, X_new):
    distances = []
    for i in range(len(X)):
        distance = euclidean_distance(X_new, X[i])
        distances.append((i, distance))
    nearest_neighbor_index = min(distances, key=lambda x: x[1])[0]
    return y[nearest_neighbor_index]

X = np.array([[25, 50000, 700], [30, 60000, 800], [35, 70000, 900], [40, 80000, 1000]])
y = np.array([0, 0, 1, 1])

X_new = np.array([28, 55000, 750])
nearest_neighbor_prediction = nearest_neighbor(X, y, X_new)
print(nearest_neighbor_prediction)  # Output: 0
```

## 4.3: Weighted K-Nearest-Neighbor Algorithm

The Weighted K-Nearest-Neighbor Algorithm is a variation of the Nearest-Neighbor Learning algorithm that assigns weights to the nearest neighbors based on their distance from the new instance.

### How Weighted K-Nearest-Neighbor Algorithm Works

Here's a step-by-step explanation of the algorithm:

1. **Data Collection**: Collect a dataset of instances, where each instance is represented by a set of features.
2. **Instance Representation**: Represent each instance as a point in the feature space.
3. **Distance Calculation**: Calculate the distance between each instance and all other instances in the dataset.
4. **Weight Calculation**: Assign weights to the nearest neighbors based on their distance from the new instance.
5. **Weighted Nearest Neighbor Selection**: Select the instance with the highest weighted score as the nearest neighbor.
6. **Prediction**: Make a prediction based on the class label of the nearest neighbor.

### Weight Calculation

The weights are typically calculated using the following formula:

`weight = 1 / (distance + 1)`

### Advantages and Disadvantages

Advantages:

- Can handle high-dimensional data
- Can be parallelized
- Can handle non-linearly separable data

Disadvantages:

- Computationally expensive
- Can be sensitive to outliers
- May require careful tuning of hyperparameters

### Example

Suppose we have a dataset of customers with features such as age, income, and credit score. We want to predict the likelihood of a customer defaulting on a loan. We can use Weighted K-Nearest-Neighbor Algorithm to find the nearest neighbor to a new customer and make a prediction based on their class label.

| Age | Income | Credit Score | Default |
| --- | ------ | ------------ | ------- |
| 25  | 50000  | 700          | No      |
| 30  | 60000  | 800          | No      |
| 35  | 70000  | 900          | Yes     |
| 40  | 80000  | 1000         | Yes     |

If we want to predict the likelihood of a new customer with age 28, income 55000, and credit score 750 defaulting on a loan, we can calculate the distances between this new customer and all other customers, assign weights to the nearest neighbors, and select the nearest neighbor.

### Code Example

Here's an example implementation of Weighted K-Nearest-Neighbor Algorithm in Python:

```python
import numpy as np

def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def weighted_knn(X, y, X_new, k=3):
    distances = []
    for i in range(len(X)):
        distance = euclidean_distance(X_new, X[i])
        distances.append((i, distance))
    distances.sort(key=lambda x: x[1])
    weighted_scores = []
    for i in range(k):
        weight = 1 / (distances[i][1] + 1)
        weighted_score = y[distances[i][0]] * weight
        weighted_scores.append(weighted_score)
    weighted_sum = np.sum(weighted_scores)
    nearest_neighbor_index = np.argmax(weighted_sum)
    return y[nearest_neighbor_index]

X = np.array([[25, 50000, 700], [30, 60000, 800], [35, 70000, 900], [40, 80000, 1000]])
y = np.array([0, 0, 1, 1])

X_new = np.array([28, 55000, 750])
nearest_neighbor_prediction = weighted_knn(X, y, X_new)
print(nearest_neighbor_prediction)  # Output: 0
```

## 4.4: Locally Sensitive Hashing (LSH)

Locally Sensitive Hashing (LSH) is a technique for dimensionality reduction and classification that involves using random projections to map the data into a lower-dimensional space.

### How LSH Works

Here's a step-by-step explanation of the algorithm:

1. **Data Collection**: Collect a dataset of instances, where each instance is represented by a set of features.
2. **Random Projections**: Generate random projections of the data using a set of binary hash functions.
3. **Hashing**: Map the data into a lower-dimensional space using the random projections.
4. **Classification**: Classify the data in the lower-dimensional space using a classifier.

### Advantages and Disadvantages

Advantages:

- Fast and efficient
- Can handle high-dimensional data
- Can be parallelized

Disadvantages:

- May not preserve the original data structure
- May be sensitive to the choice of hyperparameters

### Example

Suppose we have a dataset of customers with features such as age, income, and credit score. We want to predict the likelihood of a customer defaulting on a loan. We can use LSH to reduce the dimensionality of the data and classify the instances in the lower-dimensional space.

| Age | Income | Credit Score | Default |
| --- | ------ | ------------ | ------- |
| 25  | 50000  | 700          | No      |
| 30  | 60000  | 800          | No      |
| 35  | 70000  | 900          | Yes     |
| 40  | 80000  | 1000         | Yes     |

We can use LSH to reduce the dimensionality of the data to 2D and classify the instances in the lower-dimensional space using a classifier.

### Code Example

Here's an example implementation of LSH in Python:

```python
import numpy as np

def random_projection(X, k):
    projections = []
    for i in range(k):
        random_projection = np.random.rand(X.shape[0], 1)
        projections.append(random_projection)
    return np.array(projections)

def hashing(X, k, m):
    projections = random_projection(X, k)
    hash_values = np.zeros((X.shape[0], m))
    for i in range(m):
        for j in range(X.shape[0]):
            hash_values[j, i] = np.dot(projections[j], X[j])
    return hash_values

X = np.array([[25, 50000, 700], [30, 60000, 800], [35, 70000, 900], [40, 80000, 1000]])
k = 2
m = 10

hash_values = hashing(X, k, m)
print(hash_values)
```

## 4.5: k-Nearest-Neighbors with Density Estimation (kNNE)

k-Nearest-Neighbors with Density Estimation (kNNE) is a variation of the k-Nearest-Neighbors algorithm that estimates the density of the data in the feature space.

### How kNNE Works

Here's a step-by-step explanation of the algorithm:

1. **Data Collection**: Collect a dataset of instances, where each instance is represented by a set of features.
2. **Density Estimation**: Estimate the density of the data in the feature space using a density estimation algorithm (e.g., Gaussian Mixture Model).
3. **Instance Representation**: Represent each instance as a point in the feature space with a density value.
4. **Distance Calculation**: Calculate the distance between each instance and all other instances in the dataset.
5. **Nearest Neighbor Selection**: Select the instance with the minimum distance as the nearest neighbor.
6. **Prediction**: Make a prediction based on the class label of the nearest neighbor.

### Advantages and Disadvantages

Advantages:

- Can handle high-dimensional data
- Can be parallelized
- Can handle non-linearly separable data

Disadvantages:

- Computationally expensive
- May be sensitive to the choice of hyperparameters

### Example

Suppose we have a dataset of customers with features such as age, income, and credit score. We want to predict the likelihood of a customer defaulting on a loan. We can use kNNE to estimate the density of the data in the feature space and select the nearest neighbor.

| Age | Income | Credit Score | Default |
| --- | ------ | ------------ | ------- |
| 25  | 50000  | 700          | No      |
| 30  | 60000  | 800          | No      |
| 35  | 70000  | 900          | Yes     |
| 40  | 80000  | 1000         | Yes     |

We can estimate the density of the data using a Gaussian Mixture Model and select the nearest neighbor based on the density value.

### Code Example

Here's an example implementation of kNNE in Python:

```python
import numpy as np
from sklearn.mixture import GaussianMixture

def knn(X, y, X_new, k=3):
    distances = []
    for i in range(len(X)):
        distance = np.sqrt(np.sum((X_new - X[i]) ** 2))
        distances.append((i, distance))
    distances.sort(key=lambda x: x[1])
    weighted_scores = []
    for i in range(k):
        weight = np.exp(-((X_new - X[distances[i][0]]) ** 2) / (2 * np.var(X) * np.std(X)))
        weighted_score = y[distances[i][0]] * weight
        weighted_scores.append(weighted_score)
    weighted_sum = np.sum(weighted_scores)
    nearest_neighbor_index = np.argmax(weighted_sum)
    return y[nearest_neighbor_index]

X = np.array([[25, 50000, 700], [30, 60000, 800], [35, 70000, 900], [40, 80000, 1000]])
y = np.array([0, 0, 1, 1])

X_new = np.array([28, 55000, 750])
nearest_neighbor_prediction = knn(X, y, X_new)
print(nearest_neighbor_prediction)  # Output: 0
```

## Further Reading

- "Pattern Recognition and Machine Learning" by Christopher Bishop
- "Nearest Neighbor Methods in Classification" by Mohammadpour and Mohammadi
- "Locally Sensitive Hashing" by Datar et al.
- "k-Nearest-Neighbors with Density Estimation" by Zhou et al.
