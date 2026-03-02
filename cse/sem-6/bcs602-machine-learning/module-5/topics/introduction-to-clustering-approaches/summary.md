# Introduction to Clustering Approaches

## Overview

Clustering is an unsupervised learning technique that groups similar data points together without predefined labels. It discovers natural structures in data by organizing instances into clusters where intra-cluster similarity is high and inter-cluster similarity is low, enabling pattern discovery and data exploration.

## Key Points

- **Unsupervised Nature**: No labeled data required; algorithm discovers patterns automatically
- **Core Objective**: Maximize intra-cluster similarity (points within cluster are similar) and minimize inter-cluster similarity (clusters are distinct)
- **Applications**: Customer segmentation, Image segmentation, Document organization, Anomaly detection, Gene expression analysis, Social network analysis
- **Clustering Approaches**: Partitional (K-Means), Hierarchical (Agglomerative/Divisive), Density-based (DBSCAN), Grid-based (STING), Model-based (GMM)
- **Similarity Measures**: Euclidean distance (continuous features), Cosine similarity (text), Jaccard coefficient (sets), Correlation (patterns)
- **Evaluation**: Silhouette score, Davies-Bouldin index, Dunn index, Inertia/within-cluster sum of squares (for K-Means)

## Important Concepts

- Hard clustering: each point belongs to exactly one cluster (K-Means)
- Soft clustering: each point has membership probability for all clusters (Fuzzy C-Means, GMM)
- No universal best algorithm: effectiveness depends on data distribution, cluster shape, density
- Curse of dimensionality: distance-based methods struggle in high dimensions

## Notes

- Unsupervised: no labels needed, discovers patterns automatically
- Main approaches: partitional (K-Means), hierarchical (dendrogram), density (DBSCAN)
- Evaluation metrics: Silhouette (higher better, [-1,1]), Davies-Bouldin (lower better)
- Know applications: customer segmentation, image segmentation, anomaly detection
