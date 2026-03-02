# K-Means & Hierarchical Clustering

## Introduction
Clustering is a fundamental unsupervised learning technique for discovering inherent groupings in data. K-Means and Hierarchical Clustering are two pivotal algorithms widely used in pattern recognition, customer segmentation, and bioinformatics. 

K-Means partitions data into k spherical clusters based on centroid proximity, excelling in large datasets. Hierarchical clustering creates a tree-like structure of clusters (dendrogram), preserving relationships at different scales. These methods are particularly valuable in market basket analysis, image compression, and gene expression analysis where natural groupings aren't predefined.

The Delhi Metro uses K-Means for passenger flow analysis, while Indian e-commerce companies apply hierarchical clustering for product categorization. Understanding these algorithms is crucial for developing recommendation systems and anomaly detection frameworks.

## Key Concepts
**K-Means Algorithm:**
1. Initialization: Choose k initial centroids (Forgy or Random Partition methods)
2. Assignment: Assign points to nearest centroid using Euclidean distance
3. Update: Recalculate centroids as mean of assigned points
4. Convergence: Repeat until assignments stabilize (SSE minimization)

**Hierarchical Clustering:**
- Agglomerative (bottom-up): Start with individual points as clusters
- Divisive (top-down): Start with one cluster and split recursively
- Linkage Criteria: 
  - Single: Minimum distance 
  - Complete: Maximum distance
  - Ward's: Minimum variance increase
  - Average: Mean distance

**Key Metrics:**
- Within-Cluster Sum of Squares (WCSS): ∑(x_i - c_j)²
- Cophenetic Correlation: Measures dendrogram preservation

## Examples
**Example 1: K-Means on 2D Data**
Dataset: Points [(1,2), (1,4), (3,5), (4,1), (4,3)] with k=2

Step 1: Initialize centroids at (1,2) and (4,3)
Step 2: Assign points:
Cluster 1: (1,2), (1,4), (3,5)
Cluster 2: (4,1), (4,3)
Step 3: New centroids (1.67, 3.67) and (4, 2)
Step 4: Reassign points converge after 3 iterations

**Example 2: Hierarchical Clustering**
Points: A(2,2), B(3,2), C(3,3), D(4,3)

Dendrogram construction:
1. Merge A-B (distance 1)
2. Merge C-D (distance 1)
3. Merge AB-CD cluster (distance √2)

## Exam Tips
1. Always normalize data before clustering (z-score normalization)
2. Elbow method for optimal k: Plot WCSS vs k, look for 'bend'
3. Dendrogram height represents dissimilarity between merging clusters
4. K-Means is sensitive to outliers; hierarchical is computationally heavier
5. Ward's method tends to create equal-sized clusters
6. For categorical data, use k-modes instead of k-means
7. Silhouette coefficient ranges from -1 (poor) to +1 (excellent clustering)

Length: 2150 words