# **Text Book 2: Chap 14.2**

## **Unsupervised Learning**

### Introduction

Unsupervised learning is a type of machine learning where the algorithm is trained on a dataset without any prior knowledge of the desired output. The goal of unsupervised learning is to discover patterns, relationships, and structure in the data.

### Types of Unsupervised Learning

- **Clustering**: Grouping similar data points into clusters based on their features.
- **Dimensionality Reduction**: Reducing the number of features in a dataset while preserving the most important information.
- **Anomaly Detection**: Identifying data points that do not fit a expected pattern or distribution.

### Clustering Algorithms

#### K-Means Clustering

K-means clustering is a popular unsupervised learning algorithm that groups data points into K clusters based on their features. The algorithm works as follows:

1.  Initialize K centroids randomly.
2.  Assign each data point to the closest centroid.
3.  Update the centroids by calculating the mean of all data points assigned to each centroid.
4.  Repeat steps 2 and 3 until convergence.

Example:

Suppose we have a dataset of customers with their age and income. We want to group them into clusters based on their age and income. We can use the k-means clustering algorithm with K=3 clusters.

| Age | Income |
| --- | ------ |
| 25  | 50000  |
| 30  | 60000  |
| 35  | 70000  |
| 40  | 80000  |
| 45  | 90000  |
| 50  | 100000 |

After running the k-means algorithm, we get the following clusters:

Cluster 1:

| Age | Income |
| --- | ------ |
| 25  | 50000  |
| 30  | 60000  |

Cluster 2:

| Age | Income |
| --- | ------ |
| 35  | 70000  |
| 40  | 80000  |

Cluster 3:

| Age | Income |
| --- | ------ |
| 45  | 90000  |
| 50  | 100000 |

### Other Unsupervised Learning Algorithms

- **Hierarchical Clustering**: Builds a hierarchy of clusters by merging or splitting existing clusters.
- **DBSCAN**: Identifies clusters based on density and proximity.
- **Spectral Clustering**: Uses eigenvectors of the similarity matrix to identify clusters.

### Advantages and Disadvantages of Unsupervised Learning

Advantages:

- **Discovery of patterns and relationships**: Unsupervised learning can help discover patterns and relationships in data that may not be apparent through other methods.
- **No need for labeled data**: Unsupervised learning can be performed on unlabeled data, making it a useful technique for exploratory data analysis.

Disadvantages:

- **No clear output**: Unsupervised learning does not produce a clear output, making it challenging to evaluate the performance of the algorithm.
- **Hyperparameter tuning**: Unsupervised learning algorithms often have multiple hyperparameters that need to be tuned, which can be time-consuming and challenging.

## **Conclusion**

Unsupervised learning is a powerful technique for discovering patterns and relationships in data. Clustering algorithms, such as k-means clustering, are popular unsupervised learning algorithms that group similar data points into clusters. Other unsupervised learning algorithms, such as hierarchical clustering and DBSCAN, can also be used for clustering tasks. While unsupervised learning has many advantages, it also has some disadvantages, including the lack of clear output and the need for hyperparameter tuning.
