# Module 4: Unsupervised Learning - Machine Learning II

## Introduction

In the previous modules, we primarily dealt with **Supervised Learning**, where algorithms learn from labeled data `(X, y)` to make predictions. **Unsupervised Learning (UL)** is a paradigm shift. Here, we are only given input data `X` without any corresponding labels or target outputs. The goal is not to predict but to **discover the inherent structure, patterns, or relationships** hidden within the data itself. It's about letting the algorithm learn what is interesting or representative without explicit guidance, making it crucial for exploratory data analysis, feature discovery, and dimensionality reduction.

## Core Concepts

Unsupervised learning tasks are broadly categorized into two main types:

### 1. Clustering

The objective of clustering is to partition the dataset into groups, or **clusters**, such that data points within the same cluster are more similar to each other than to those in other clusters. It answers the question: "How is the data naturally grouped?"

*   **Key Algorithm: K-Means Clustering**
    *   **Concept:** A centroid-based algorithm that aims to partition `n` observations into `k` clusters. Each cluster is represented by the mean (centroid) of its points.
    *   **How it works:**
        1.  **Initialization:** Randomly select `k` data points as initial cluster centroids.
        2.  **Assignment:** Assign each data point to the nearest centroid (using Euclidean distance), forming `k` clusters.
        3.  **Update:** Recalculate the centroids as the mean of all data points assigned to that cluster.
        4.  **Iteration:** Repeat the Assignment and Update steps until the centroids no longer change significantly (convergence) or a maximum number of iterations is reached.

    *   **Example:** Customer segmentation for an e-commerce site. Given customer data (purchase history, time spent, etc.), K-Means can group them into clusters like "frequent high-value buyers," "bargain hunters," and "occasional shoppers" without knowing these categories beforehand.

*   **Challenge:** The value of `k` (number of clusters) is a **hyperparameter** that must be chosen by the user. Methods like the **Elbow Method** help estimate a good `k`.

### 2. Dimensionality Reduction

Real-world datasets often have a large number of features (high dimensionality), which can lead to the **curse of dimensionality**—increased computational cost, storage issues, and model overfitting. Dimensionality reduction techniques transform the data from a high-dimensional space to a lower-dimensional space while preserving as much of the meaningful information (variance) as possible.

*   **Key Algorithm: Principal Component Analysis (PCA)**
    *   **Concept:** PCA identifies the directions (called **principal components**) that maximize the variance in the data. The first principal component is the direction of maximum variance; each succeeding component is orthogonal to the previous ones and has the next highest variance.
    *   **How it works:**
        1.  **Standardize the data** (mean=0, standard deviation=1).
        2.  Compute the **covariance matrix** of the data.
        3.  Perform **eigendecomposition** on the covariance matrix to get its eigenvectors (principal components) and eigenvalues (magnitude of variance along each component).
        4.  Sort the eigenvectors by decreasing eigenvalues and choose the top `k` eigenvectors to form a projection matrix.
        5.  Transform the original data via this matrix to obtain the new `k`-dimensional representation.

    *   **Example:** Visualizing high-dimensional data in 2D or 3D. For a dataset with 50 features, PCA can project it onto its first two principal components, allowing us to plot it and potentially see clusters or trends that were impossible to perceive in the original space.

Other important unsupervised techniques include:
*   **Anomaly Detection:** Identifying rare items, events, or observations that deviate significantly from the majority of the data (e.g., fraud detection).
*   **Association Rule Learning:** Discovering interesting relations between variables in large databases (e.g., market basket analysis: " customers who buy X also tend to buy Y").

## Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Primary Goal** | To find hidden patterns or intrinsic structures in **unlabeled** data. |
| **Input Data** | `X` (Features only, no labels `y`). |
| **Common Tasks** | Clustering, Dimensionality Reduction, Anomaly Detection, Association. |
| **Key Algorithms** | K-Means (Clustering), PCA (Dimensionality Reduction), DBSCAN, Apriori. |
| **Challenges** | Determining the number of clusters (`k`), interpreting results without ground truth, evaluating performance is subjective (often using metrics like Silhouette Score). |
| **Applications** | Customer segmentation, image compression, feature extraction for supervised learning, data visualization, recommendation systems. |

**In summary,** unsupervised learning is a powerful tool for data exploration and preprocessing. It allows engineers and data scientists to make sense of vast, unlabeled datasets, reduce complexity, and gain insights that can inform further analysis and model building.