# **Clustering Algorithms Revision Notes**

## **Introduction to Clustering Approaches**

- Clustering is a type of unsupervised machine learning algorithm that groups similar data points into clusters.
- Cluster analysis is a technique used to categorize data points into clusters based on their similarity.
- Types of clustering:
  - Hierarchical clustering
  - Partitional clustering
  - Density-based clustering

## **Proximity Measures**

- **Distance**: measures the difference between two data points.
  - Euclidean distance: √((x2-x1)^2 + (y2-y1)^2)
  - Manhattan distance: |x2-x1| + |y2-y1|
  - Minkowski distance: (|x2-x1|^p + |y2-y1|^p)^(1/p)
- **Similarity**: measures the similarity between two data points.
  - Cosine similarity: dot product / (|vector1| \* |vector2|)
  - Jaccard similarity: |intersection| / |union|

## **Hierarchical Clustering Algorithms**

- **Agglomerative Clustering**:
  - Start with each data point as a separate cluster.
  - Merge the two closest clusters until all points are in one cluster.
- **Divisive Clustering**:
  - Start with all data points in one cluster.
  - Split the cluster into two smaller clusters until each point is in its own cluster.

## **Partitional Clustering Algorithm**

- **K-Means Clustering**:
  - Assign each data point to the closest centroid (mean of its cluster).
  - Update centroids and repeat until convergence.
- **K-Medoids Clustering**:
  - Assign each data point to the closest medoid (most similar point).
  - Update medoids and repeat until convergence.

## **Important Formulas and Definitions**

- **Cluster coefficient**: measures the strength of connectivity within a cluster.
- **Silhouette coefficient**: measures the separation between clusters.
- **Calinski-Harabasz index**: evaluates the ratio of between-cluster variance to within-cluster variance.

## **Important Theorems**

- **Birkhoff's theorem**: states that a clustering algorithm can be represented as a graph.
- **Kruskal's algorithm**: a popular algorithm for finding the minimum spanning tree of a graph.
