# Nearest Centroid Classifier

### Definition

- A type of supervised learning algorithm that uses the concept of nearest centroid to classify data points.
- Belongs to the family of instance-based learning and similarity-based learning algorithms.

### Key Points

- **Definition:** The nearest centroid classifier assigns a new, unseen data point to the class of the centroid (mean vector) of its k-nearest neighbors.
- **Algorithm:**
  1.  Find the k nearest neighbors to the new data point.
  2.  Calculate the centroid (mean vector) of these k nearest neighbors.
  3.  Assign the new data point to the class of the centroid.

### Important Formulas

- **Distance metric:** Euclidean distance (d(x, y) = √((x1 - y1)^2 + (x2 - y2)^2))
- **Centroid (mean vector) calculation:** μ = (1/k) \* ∑(xi \* yi), where xi and yi are the i-th components of the k nearest neighbors

### Theorems

- **Nearest Centroid Theorem:** The nearest centroid classifier is a Bayes classifier when the data is normally distributed.
- **K-Nearest Neighbors Theorem:** The k-nearest neighbors algorithm is a generalization of the nearest centroid classifier when k > 1.

### Notes

- The choice of k affects the performance of the algorithm.
- The nearest centroid classifier is sensitive to outliers and noisy data.
- It is often used for classification problems in high-dimensional spaces.

### Advantages

- Simple to implement
- Robust to outliers
- Does not require any training data

### Disadvantages

- Computationally expensive for large datasets
- Sensitive to noise and outliers
- Not suitable for high-dimensional spaces without dimensionality reduction techniques.
