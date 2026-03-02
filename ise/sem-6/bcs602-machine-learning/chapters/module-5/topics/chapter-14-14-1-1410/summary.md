## Chapter-14 (14-1-14.10) Revision Notes

### Introduction to Clustering Algorithms

- Clustering is a type of unsupervised machine learning technique that groups similar data points into clusters.
- Clustering algorithms aim to identify patterns and structures in data without prior knowledge of the underlying distribution.
- Common clustering algorithms:
  - K-Means
  - Hierarchical Clustering
  - DBSCAN

### Proximity Measures

- **Distance Metrics:**
  - Euclidean Distance
  - Manhattan Distance
  - Minkowski Distance
- **Similarity Metrics:**
  - Cosine Similarity
  - Jaccard Similarity
  - Hamming Distance

### Hierarchical Clustering

- **Types of Hierarchical Clustering:**
  - Agglomerative Clustering
  - Divisive Clustering
- **Hierarchical Clustering Algorithm:**
  - Start with individual data points
  - Merge closest points until a desired cluster size is reached

### Important Formulas and Definitions

- **Distance Formula:**
  - $d(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + ... + (x_n - y_n)^2}$
- **Similarity Formula:**
  - $sim(x, y) = \frac{\sum x_iy_i}{\sum x_i^2}$
- **Centroid Formula:**
  - $centroid = \frac{\sum x_i}{m}$
- **DBSCAN Definition:**
  - Density-Based Spatial Clustering of Applications with Noise (DBSCAN) is a clustering algorithm that groups data points based on density and proximity.

### Important Theorems

- **K-Means Convergence Theorem:**
  - K-Means clustering algorithm converges to the global minimum of the sum of squared distances.
- **Hierarchical Clustering Theorem:**
  - Hierarchical clustering algorithm terminates when a stopping criterion is reached, such as a minimum number of clusters.
