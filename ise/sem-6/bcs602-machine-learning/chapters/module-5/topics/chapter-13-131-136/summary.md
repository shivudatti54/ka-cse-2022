# Chapter 13 Revision Notes

### 13.1: Introduction to Clustering Approaches

- Definition: Clustering is the process of dividing a set of objects into subsets such that objects in the same subset (cluster) are more similar than to those in other subsets.
- Types of Clustering:
  - Hierarchical Clustering: builds clusters from small subsets of data points
  - Non-Hierarchical Clustering: builds clusters from the entire dataset

### 13.2: Proximity Measures

- Distance Measures:
  - Euclidean Distance: measures the straight-line distance between two points
  - Manhattan Distance: measures the sum of the absolute differences in coordinates
  - Minkowski Distance: generalizes Euclidean and Manhattan distances
- Similarity Measures:
  - Cosine Similarity: measures the cosine of the angle between two vectors
  - Jaccard Similarity: measures the size of the intersection divided by the size of the union

### 13.3: Hierarchical Clustering Algorithms

- Definition: Hierarchical clustering algorithms build clusters from small subsets of data points
- Types of Hierarchical Clustering:
  - Agglomerative Clustering: merges clusters until a stopping criterion is reached
  - Divisive Clustering: splits clusters until a stopping criterion is reached

### 13.4: Agglomerative Clustering Algorithms

- Definition: Agglomerative clustering algorithms merge clusters until a stopping criterion is reached
- Examples:
  - Single Linkage Algorithm: merges clusters based on the minimum distance between points
  - Complete Linkage Algorithm: merges clusters based on the maximum distance between points

### 13.5: Divisive Clustering Algorithms

- Definition: Divisive clustering algorithms split clusters until a stopping criterion is reached
- Examples:
  - Single Linkage Algorithm: splits clusters based on the maximum distance between points
  - Complete Linkage Algorithm: splits clusters based on the minimum distance between points

### 13.6: Evaluation Metrics for Clustering

- Definition: Evaluation metrics assess the quality of clustering results
- Examples:
  - Silhouette Coefficient: measures the separation between clusters
  - Calinski-Harabasz Index: measures the ratio of between-cluster variance to within-cluster variance
