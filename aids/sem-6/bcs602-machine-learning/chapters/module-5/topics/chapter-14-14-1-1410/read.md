# Chapter-14: Clustering Algorithms: Introduction to Clustering Approaches, Proximity Measures, Hierarchical Clustering

=====================================================

## Introduction to Clustering

---

Clustering is a fundamental concept in Machine Learning that involves grouping similar data points into clusters based on their characteristics. The goal of clustering is to identify patterns, structures, and relationships in the data by partitioning it into distinct groups.

## Types of Clustering

---

There are several types of clustering algorithms, including:

- **Hierarchical Clustering**: This approach builds a hierarchy of clusters by merging or splitting existing clusters.
- **K-Means Clustering**: This is a widely used algorithm that partitions the data into K clusters based on the mean distance of the features.
- **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**: This algorithm groups data points into clusters based on their density and proximity to each other.
- **Gaussian Mixture Model (GMM) Clustering**: This approach represents the data as a mixture of Gaussian distributions and clusters the data based on the probability of each point belonging to a particular cluster.

## Proximity Measures

---

Proximity measures are used to define the similarity or dissimilarity between data points. Some common proximity measures include:

- **Euclidean Distance**: This is a measure of the straight-line distance between two points in n-dimensional space.
- **Manhattan Distance**: This is a measure of the sum of the absolute differences between corresponding coordinates of two points.
- **Minkowski Distance**: This is a generalized version of the Euclidean and Manhattan distances that can be used to define different types of distances.
- **Cosine Similarity**: This is a measure of the cosine of the angle between two vectors, which can be used to define similarity between text documents or images.

## Hierarchical Clustering

---

Hierarchical clustering is a type of clustering algorithm that builds a hierarchy of clusters by merging or splitting existing clusters. The process of hierarchical clustering can be divided into two stages:

### **Agglomerative Clustering**

In agglomerative clustering, the algorithm starts by creating a single cluster that contains all the data points. Then, it repeatedly merges the two closest clusters until a stopping criterion is reached.

### **Divisive Clustering**

In divisive clustering, the algorithm starts with a single cluster that contains all the data points. Then, it repeatedly splits the cluster into two sub-clusters until a stopping criterion is reached.

### **Examples of Hierarchical Clustering Algorithms**

- **Single Linkage Clustering**: This algorithm merges the two closest clusters in the agglomerative approach.
- **Complete Linkage Clustering**: This algorithm merges the two farthest clusters in the agglomerative approach.
- **Ward's Minimum Variance Clustering**: This algorithm minimizes the variance of the clusters in the divisive approach.

### **Advantages and Disadvantages of Hierarchical Clustering**

- **Advantages**: Hierarchical clustering can handle both categorical and numerical data, and it can identify clusters of varying densities.
- **Disadvantages**: Hierarchical clustering can be computationally expensive, and it can be sensitive to the choice of linkage function.

## Example Use Case

---

Suppose we have a dataset of customers with their age, income, and purchase history. We want to cluster these customers based on their demographic characteristics and purchase behavior. A hierarchical clustering algorithm can be used to identify clusters of customers with similar characteristics, such as age and income, as well as clusters of customers with similar purchase behavior.

```python
import numpy as np
from sklearn.cluster import AgglomerativeClustering

# Generate some sample data
np.random.seed(0)
data = np.random.rand(100, 3)

# Create an AgglomerativeClustering object
model = AgglomerativeClustering(n_clusters=5)

# Fit the model to the data
model.fit(data)

# Get the cluster labels
labels = model.labels_

# Print the cluster labels
print(labels)
```

This code generates some sample data, creates an AgglomerativeClustering object, fits the model to the data, and prints the cluster labels. The output will be a vector of integers where each integer represents the cluster label for a particular data point.
