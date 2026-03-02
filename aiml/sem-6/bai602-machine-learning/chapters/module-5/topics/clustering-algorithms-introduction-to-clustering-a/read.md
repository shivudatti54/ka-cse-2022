# Clustering Algorithms

=====================

## Introduction to Clustering Approaches

---

Clustering is a fundamental concept in machine learning, where unsupervised learning algorithms group similar data points into clusters based on their proximity to each other. The primary goal of clustering is to identify patterns, relationships, and groupings within the data.

### Types of Clustering Approaches

- **Hierarchical Clustering**: Builds a hierarchy of clusters by merging or splitting existing clusters.
- **Partitional Clustering**: Divides the data into a fixed number of clusters, with no overlap between clusters.
- **Density-Based Clustering**: Groups data points based on density and proximity to each other.

## Proximity Measures

---

Proximity measures are used to calculate the distance between data points. Common proximity measures include:

- **Euclidean Distance**: Measures the straight-line distance between two points in n-dimensional space.
- **Manhattan Distance**: Measures the sum of the absolute differences between corresponding coordinates.
- **Minkowski Distance**: A generalized distance metric that can handle different types of distances.
- **Cosine Similarity**: Measures the cosine of the angle between two vectors.

### Example: Calculating Euclidean Distance

Suppose we have two data points: A = (3, 4) and B = (6, 8). The Euclidean distance between A and B is:

√((6 - 3)² + (8 - 4)²) = √(9 + 16) = √25 = 5

## Hierarchical Clustering Algorithms

---

Hierarchical clustering algorithms build a hierarchy of clusters by merging or splitting existing clusters.

### Types of Hierarchical Clustering

- **Agglomerative Clustering**: Starts with individual data points and merges them into clusters based on proximity.
- **Divisive Clustering**: Starts with a single cluster and splits it into smaller clusters based on proximity.

### Example: Calculating Distance Matrix

Suppose we have a dataset with 5 data points: A, B, C, D, and E. The distance matrix is:

|     | A   | B   | C   | D   | E   |
| --- | --- | --- | --- | --- | --- |
| A   | 0   | 5   | 7   | 10  | 12  |
| B   | 5   | 0   | 3   | 8   | 11  |
| C   | 7   | 3   | 0   | 6   | 9   |
| D   | 10  | 8   | 6   | 0   | 7   |
| E   | 12  | 11  | 9   | 7   | 0   |

## Partitional Clustering Algorithms

---

Partitional clustering algorithms divide the data into a fixed number of clusters, with no overlap between clusters.

### Types of Partitional Clustering

- **K-Means Clustering**: Assigns each data point to the closest cluster based on the mean vector of the cluster.
- **K-Medoids Clustering**: Similar to K-Means, but uses medoids (data points with the same number of closest neighbors as the mean) instead of means.

### Example: Calculating Cluster Centers

Suppose we have a dataset with 5 data points: A, B, C, D, and E. We want to cluster them into 3 clusters using K-Means. The cluster centers are calculated as follows:

Cluster 1: (A, 3), (B, 5)
Cluster 2: (C, 8), (D, 10)
Cluster 3: (E, 12)

The data points are assigned to the closest cluster based on the mean vector of the cluster.
