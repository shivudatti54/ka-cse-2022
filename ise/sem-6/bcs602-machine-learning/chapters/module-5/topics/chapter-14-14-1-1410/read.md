# **Chapter-14: Clustering Algorithms**

### Introduction to Clustering Approaches

---

Clustering is a fundamental concept in machine learning that involves grouping similar data points into clusters. The primary objective of clustering is to identify patterns, structures, or groupings in the data that are not inherently present.

## **Types of Clustering Algorithms**

There are two primary types of clustering algorithms:

- **Hierarchical Clustering**: This approach builds a hierarchy of clusters by merging or splitting existing clusters. Hierarchical clustering is useful for exploring the data structure and identifying clusters at different levels of granularity.
- **Non-Hierarchical Clustering**: This approach groups data points into clusters without building a hierarchy. Non-hierarchical clustering algorithms, such as k-means and k-medoids, are commonly used for large datasets.

### Proximity Measures

---

Proximity measures are used to determine the similarity between data points. The most common proximity measures are:

- **Euclidean Distance**: This measures the straight-line distance between two points in n-dimensional space.
- **Minkowski Distance**: A generalization of Euclidean distance that allows for different distance metrics.
- **Manhattan Distance**: Also known as the L1 distance, this measures the sum of the absolute differences between corresponding coordinates.
- **Cosine Similarity**: This measures the cosine of the angle between two vectors.

### Hierarchical Clustering

---

Hierarchical clustering algorithms build a hierarchy of clusters by merging or splitting existing clusters. There are two primary hierarchical clustering algorithms:

- **Agglomerative Clustering**: This algorithm starts with individual data points and merges them into clusters based on similarity.
- **Divisive Clustering**: This algorithm starts with a single cluster and splits it into smaller clusters based on similarity.

### k-Means Clustering

---

k-means clustering is a popular non-hierarchical clustering algorithm. It works by:

1.  Initializing k centroids randomly
2.  Assigning each data point to the nearest centroid
3.  Updating the centroids as the mean of all assigned data points
4.  Repeating steps 2-3 until convergence

### k-Medoids Clustering

---

k-medoids clustering is a variant of k-means clustering that uses medoids instead of centroids. Medoids are objects that are representative of their respective clusters.

### Example Use Case

---

Suppose we have a dataset of customers with their purchase history, and we want to group them into clusters based on their purchasing behavior. We can use k-means clustering to identify three clusters:

- Cluster 1: Frequent buyers with high purchase values
- Cluster 2: Occasional buyers with low purchase values
- Cluster 3: Non-buyers with zero purchase values

By applying k-means clustering, we can identify the underlying patterns in the customer data and tailor marketing strategies to each cluster.

### Code Implementation

---

Here is an example implementation of k-means clustering in Python:

```python
import numpy as np
from sklearn.cluster import KMeans

# Generate sample data
np.random.seed(0)
data = np.random.rand(100, 2)

# Initialize k-means model
kmeans = KMeans(n_clusters=3)

# Fit model to data
kmeans.fit(data)

# Predict cluster labels
labels = kmeans.labels_

# Print cluster centers
print(kmeans.cluster_centers_)
```

This code generates sample data, initializes a k-means model, fits the model to the data, predicts cluster labels, and prints the cluster centers.
