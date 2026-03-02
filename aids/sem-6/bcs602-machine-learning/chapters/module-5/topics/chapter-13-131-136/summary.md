# Chapter 13: Clustering Algorithms

### 13.1 Introduction to Clustering

- Clustering is a type of unsupervised learning algorithm that groups similar data points into clusters.
- Clustering is used to identify patterns, structure, and relationships in data.

### 13.2 Proximity Measures

- **Distance Measures:**
  - Euclidean Distance: √((x2 - x1)² + (y2 - y1)²)
  - Manhattan Distance: |x2 - x1| + |y2 - y1|
  - Minkowski Distance: (∑|xi - xj|p)^(1/p)
- **Similarity Measures:**
  - Cosine Similarity: (a · b) / (|a| |b|)
  - Jaccard Similarity: |A ∩ B| / |A ∪ B|

### 13.3 Hierarchical Clustering

- **Types of Hierarchical Clustering:**
  - Agglomerative Clustering: Merge clusters until only one remains.
  - Divisive Clustering: Split clusters until they are too small to merge.
- **Hierarchical Clustering Algorithms:**
  - Single Linkage: Minimum distance between two clusters.
  - Complete Linkage: Maximum distance between two clusters.
  - Average Linkage: Average distance between two clusters.

### 13.4 Density-Based Clustering

- **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
  - ε: Nearest neighbor distance.
  - ρ: Minimum number of points required to form a cluster.
  - Noise point: Point not part of any cluster.

### 13.5 K-Means Clustering

- **K-means Algorithm:**
  - Initialize centroids randomly.
  - Assign each data point to the closest centroid.
  - Update centroids as the mean of their assigned data points.
  - Repeat until convergence.

### 13.6 Clustering Evaluation Metrics

- **Silhouette Coefficient:** Measures the separation between clusters and the cohesion within clusters.
- **Calinski-Harabasz Index:** Measures the ratio of between-cluster variance to within-cluster variance.
- **Davies-Bouldin Index:** Measures the ratio of within-cluster variance to between-cluster variance.
