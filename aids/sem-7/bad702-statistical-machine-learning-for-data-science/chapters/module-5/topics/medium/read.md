# Module 5: Clustering Algorithms

## Introduction

In the previous modules, we focused on **supervised learning**, where algorithms learn from labeled data (e.g., data with a known target variable like `price` or `species`). This module introduces **unsupervised learning**, specifically **clustering**. Clustering is the task of grouping a set of objects in such a way that objects in the same group (called a **cluster**) are more similar to each other than to those in other groups. It is a fundamental tool for exploratory data analysis, customer segmentation, image compression, and anomaly detection.

## Core Concepts

### 1. The Goal of Clustering

The primary goal is to discover the inherent grouping structure within unlabeled data. Since there are no labels to guide the learning process, clustering is often subjective; the "correct" clustering depends on the context and the specific measure of similarity used.

### 2. Key Terminology

*   **Cluster:** A collection of data points that are similar to each other.
*   **Centroid:** The geometric center or mean point of a cluster (used in algorithms like K-Means).
*   **Similarity/Dissimilarity Measure:** A metric that quantifies how alike two data points are. The most common measure is the **Euclidean Distance**. Other metrics include Manhattan, Cosine Similarity, and Hamming Distance.
*   **Within-Cluster Variation:** A measure of how compact or tightly grouped the points inside a single cluster are. A primary objective of many algorithms is to minimize this variation.

## Major Clustering Algorithms

### 1. K-Means Clustering

K-Means is a centroid-based, iterative partitioning algorithm. It is simple, efficient, and one of the most widely used clustering algorithms.

**How it works:**
1.  **Initialization:** Choose the number of clusters, `k`. Randomly initialize `k` centroids in the feature space.
2.  **Assignment:** Assign each data point to its nearest centroid, forming `k` clusters.
3.  **Update:** Recalculate the centroids as the mean of all data points assigned to that cluster.
4.  **Iteration:** Repeat the Assignment and Update steps until the centroids no longer change significantly (i.e., convergence is reached).

**Example:** Segmenting customers based on annual income and spending score. `k=3` might yield clusters for "Budget," "Average," and "Premium" customers.

**Key Limitation:** The user must specify `k`, and the results can be highly sensitive to the initial random centroid placement.

### 2. Hierarchical Clustering

Unlike K-Means, this algorithm does not require a pre-specified `k`. It builds a hierarchy of clusters, which can be visualized as a **dendrogram**.

There are two main types:
*   **Agglomerative (Bottom-Up):** Starts by treating each data point as its own cluster. It then iteratively merges the two most similar clusters until all points are in one single cluster.
*   **Divisive (Top-Down):** Starts with all points in one cluster and recursively splits them.

**How to choose the number of clusters (`k`):** After building the dendrogram, you draw a horizontal line. The number of vertical lines it intersects is your number of clusters. You choose a cut-off point that provides the most distinct, meaningful grouping.

**Advantage:** The dendrogram provides a rich visual summary of the data's grouping structure at all levels.

## Determining the Optimal Number of Clusters

Since clustering is unsupervised, evaluating results and choosing the right `k` is crucial. Two common techniques are:

1.  **Elbow Method (for K-Means):** Plot the Within-Cluster Sum of Squares (WCSS) against the number of clusters (`k`). WCSS decreases as `k` increases. The "elbow" point, where the rate of decrease sharply changes, is a good candidate for the optimal `k`.
2.  **Silhouette Analysis:** Computes a silhouette score for each data point, which measures how similar an object is to its own cluster compared to other clusters. The average score across all data points for a given `k` can be used to evaluate the clustering quality. A score close to 1 indicates excellent clustering.

## Key Points & Summary

| **Aspect** | **Description** |
| :--- | :--- |
| **Goal** | To find inherent, natural groupings in unlabeled data. |
| **Supervised vs. Unsupervised** | Clustering is an **unsupervised** learning technique (no labels are provided). |
| **Main Algorithms** | **K-Means:** Efficient, requires pre-defined `k`, sensitive to initialization. <br> **Hierarchical:** Creates a dendrogram, does not require pre-defined `k`. |
| **Key Input** | A measure of **similarity or distance** between data points (e.g., Euclidean Distance). |
| **Choosing `k`** | Use the **Elbow Method** (plot WCSS) or **Silhouette Analysis** (higher average score is better). |
| **Applications** | Customer segmentation, document clustering, image segmentation, anomaly detection. |
| **Challenge** | There is no single "correct" answer; interpretation is subjective and domain-dependent. |