# K-Means Clustering

## Introduction

K-Means clustering is a type of unsupervised machine learning algorithm used to group similar data points into clusters based on their features. The goal of K-Means clustering is to identify patterns or structures in the data that are not easily visible by other methods, such as visualization or summary statistics. This algorithm is widely used in various fields, including customer segmentation, image compression, and gene expression analysis.

K-Means clustering is a simple yet powerful algorithm that can be used to identify clusters in data. The algorithm works by iteratively updating the centroids of the clusters and reassigning the data points to the closest cluster. The algorithm terminates when the centroids converge or a stopping criterion is reached.

## Key Concepts

### K-Means Algorithm

The K-Means algorithm consists of the following steps:

1. **Initialization**: Randomly initialize the centroids of the clusters.
2. **Assignment**: Assign each data point to the closest cluster based on the Euclidean distance between the data point and the centroid.
3. **Update**: Update the centroid of each cluster by calculating the mean of all data points assigned to the cluster.
4. **Repeat**: Repeat steps 2 and 3 until the centroids converge or a stopping criterion is reached.

### Distance Metrics

The most commonly used distance metric in K-Means clustering is the Euclidean distance. However, other distance metrics such as Manhattan distance and Minkowski distance can also be used.

### Choosing the Number of Clusters (K)

The choice of K is a critical parameter in K-Means clustering. A common method for choosing K is the elbow method, which involves plotting the sum of squared errors (SSE) against different values of K and selecting the value of K that corresponds to the "elbow" point in the plot.

## Examples

### Example 1: Customer Segmentation

A company wants to segment its customers based on their age and income. The company collects data on the age and income of its customers and applies K-Means clustering to identify clusters in the data.

| Age | Income |
| --- | --- |
| 25  | 50000 |
| 30  | 60000 |
| 35  | 70000 |
| 40  | 80000 |
| 45  | 90000 |

The company applies K-Means clustering with K=3 and obtains the following clusters:

Cluster 1: Age 25-30, Income 50000-60000
Cluster 2: Age 35-40, Income 70000-80000
Cluster 3: Age 45-50, Income 90000-100000

### Example 2: Image Compression

A company wants to compress images using K-Means clustering. The company collects data on the pixel values of the images and applies K-Means clustering to identify clusters in the data.

| Pixel Value |
| --- |
| 100  |
| 120  |
| 140  |
| 160  |
| 180  |

The company applies K-Means clustering with K=5 and obtains the following clusters:

Cluster 1: Pixel Value 100-120
Cluster 2: Pixel Value 120-140
Cluster 3: Pixel Value 140-160
Cluster 4: Pixel Value 160-180
Cluster 5: Pixel Value 180-200

## Exam Tips

1. Understand the K-Means algorithm and its application in clustering.
2. Know how to choose the number of clusters (K) using the elbow method.
3. Be able to interpret the results of K-Means clustering, including the centroids and cluster assignments.
4. Understand the limitations of K-Means clustering, including its sensitivity to outliers and non-spherical clusters.
5. Be able to apply K-Means clustering to real-world problems, such as customer segmentation and image compression.
6. Know how to evaluate the performance of K-Means clustering using metrics such as SSE and silhouette score.
7. Understand the difference between K-Means clustering and other clustering algorithms, such as hierarchical clustering and DBSCAN.