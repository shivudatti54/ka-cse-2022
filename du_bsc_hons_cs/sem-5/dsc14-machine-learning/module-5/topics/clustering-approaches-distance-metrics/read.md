# Clustering Approaches and Distance Metrics

## Introduction

Clustering is a type of unsupervised machine learning algorithm that groups similar data points into clusters. It is a widely used technique in data analysis and pattern recognition. Clustering approaches can be categorized into two main types: hierarchical and non-hierarchical. Hierarchical clustering builds a hierarchy of clusters, while non-hierarchical clustering partitions the data into a fixed number of clusters. Distance metrics play a crucial role in clustering, as they measure the similarity between data points.

Clustering has numerous applications in real-world problems, such as customer segmentation, image segmentation, and gene expression analysis. For instance, in customer segmentation, clustering can help identify distinct customer groups based on their demographic and behavioral characteristics. In image segmentation, clustering can help separate objects from the background.

## Key Concepts

### Clustering Approaches

1. **Hierarchical Clustering**: Hierarchical clustering builds a hierarchy of clusters by merging or splitting existing clusters. It can be further divided into two types:
	* **Agglomerative Clustering**: Agglomerative clustering starts with each data point as a separate cluster and merges them into larger clusters.
	* **Divisive Clustering**: Divisive clustering starts with all data points in a single cluster and splits them into smaller clusters.
2. **Non-Hierarchical Clustering**: Non-hierarchical clustering partitions the data into a fixed number of clusters. The most common type of non-hierarchical clustering is **K-Means Clustering**.

### Distance Metrics

1. **Euclidean Distance**: Euclidean distance measures the straight-line distance between two points in n-dimensional space.
2. **Manhattan Distance**: Manhattan distance measures the sum of the absolute differences between corresponding coordinates.
3. **Minkowski Distance**: Minkowski distance is a generalization of Euclidean and Manhattan distances.
4. **Cosine Similarity**: Cosine similarity measures the cosine of the angle between two vectors.

## Examples

### Example 1: Hierarchical Clustering

Suppose we have a dataset of customers with their age and income. We want to cluster them using hierarchical clustering.

| Age | Income |
| --- | --- |
| 25  | 50000 |
| 30  | 60000 |
| 35  | 70000 |
| 40  | 80000 |
| 45  | 90000 |

We start with each customer as a separate cluster and merge them into larger clusters based on their Euclidean distance.

### Example 2: K-Means Clustering

Suppose we have a dataset of images with their pixel values. We want to cluster them into two clusters using K-Means clustering.

| Pixel Value |
| --- |
| 100 |
| 120 |
| 140 |
| 160 |
| 180 |

We initialize two centroids randomly and assign each image to the closest centroid. We then update the centroids and repeat the process until convergence.

## Exam Tips

1. Understand the difference between hierarchical and non-hierarchical clustering.
2. Know the types of hierarchical clustering (agglomerative and divisive).
3. Be familiar with the different distance metrics (Euclidean, Manhattan, Minkowski, and cosine similarity).
4. Practice solving clustering problems using hierarchical and non-hierarchical clustering.
5. Understand the importance of choosing the right distance metric for a given problem.
6. Be able to interpret the results of clustering algorithms.
7. Know how to evaluate the performance of clustering algorithms.