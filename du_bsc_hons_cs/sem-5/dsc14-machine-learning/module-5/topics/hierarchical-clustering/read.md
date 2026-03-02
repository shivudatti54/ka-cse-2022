# Hierarchical Clustering
## Introduction

Hierarchical clustering is a type of unsupervised machine learning algorithm that groups similar data points into clusters. Unlike k-means clustering, which requires a predefined number of clusters, hierarchical clustering creates a hierarchy of clusters by merging or splitting existing ones. This technique is useful for identifying relationships between data points at different levels of granularity.

Hierarchical clustering has many applications in data analysis, such as identifying customer segments, grouping similar genes or proteins, and organizing text documents. Its ability to create a hierarchy of clusters makes it a powerful tool for exploratory data analysis.

## Key Concepts

### Types of Hierarchical Clustering

There are two main types of hierarchical clustering: agglomerative and divisive.

*   **Agglomerative Clustering**: This approach starts with each data point as its own cluster and iteratively merges the closest clusters until only one cluster remains.
*   **Divisive Clustering**: This approach starts with all data points in a single cluster and iteratively splits the cluster into smaller ones until each data point is in its own cluster.

### Distance Metrics

Hierarchical clustering relies on distance metrics to measure the similarity between data points. Common distance metrics include:

*   **Euclidean Distance**: The straight-line distance between two points in n-dimensional space.
*   **Manhattan Distance**: The sum of the absolute differences between corresponding coordinates.
*   **Cosine Similarity**: The cosine of the angle between two vectors.

### Linkage Criteria

Linkage criteria determine how clusters are merged or split. Common linkage criteria include:

*   **Single Linkage**: The distance between two clusters is the minimum distance between any two points in the clusters.
*   **Complete Linkage**: The distance between two clusters is the maximum distance between any two points in the clusters.
*   **Average Linkage**: The distance between two clusters is the average distance between all points in the clusters.

## Examples

### Example 1: Agglomerative Clustering

Suppose we have the following dataset:

| Point | X | Y |
| --- | --- | --- |
| A    | 1 | 2 |
| B    | 2 | 3 |
| C    | 4 | 5 |
| D    | 6 | 7 |

We can perform agglomerative clustering using the Euclidean distance metric and single linkage criterion. The resulting dendrogram is:

```
  +---------------+
  |         +-----+
  |         |     |
  +-----+   +-----+
  |     |   |     |
  A     B   C     D
```

### Example 2: Divisive Clustering

Suppose we have the same dataset as above. We can perform divisive clustering using the Euclidean distance metric and complete linkage criterion. The resulting dendrogram is:

```
          +---------------+
          |               |
  +---------------+       |
  |               |       |
  +-----+       +-----+   +
  |     |       |     |   |
  A     B       C     D
```

## Exam Tips

1.  Understand the difference between agglomerative and divisive clustering.
2.  Familiarize yourself with common distance metrics and linkage criteria.
3.  Practice creating dendrograms by hand for small datasets.
4.  Be able to interpret the results of hierarchical clustering, including identifying clusters and understanding the hierarchy.
5.  Understand how to choose the optimal number of clusters.
6.  Be familiar with the advantages and disadvantages of hierarchical clustering compared to other clustering algorithms.
7.  Practice implementing hierarchical clustering using popular machine learning libraries such as scikit-learn.