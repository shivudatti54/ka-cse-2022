# Clustering Algorithms

## Overview

Clustering algorithms automatically group similar data points using various strategies and distance metrics. Major algorithms include K-Means (partition-based), hierarchical methods (agglomerative/divisive), DBSCAN (density-based), and Gaussian Mixture Models (probabilistic), each with distinct characteristics and use cases.

## Key Points

- **K-Means**: Partition data into k clusters by minimizing within-cluster variance; iteratively update centroids; simple and fast but requires k specification
- **Hierarchical Agglomerative**: Bottom-up merging; starts with individual points, merges closest pairs; produces dendrogram; no k needed upfront
- **Hierarchical Divisive**: Top-down splitting; starts with all points in one cluster, recursively splits; computationally expensive
- **DBSCAN**: Density-based; finds clusters of arbitrary shape; identifies noise points; requires epsilon (neighborhood radius) and minPts (density threshold)
- **Gaussian Mixture Model (GMM)**: Probabilistic soft clustering; assumes data from mixture of Gaussians; EM algorithm for parameter estimation
- **Fuzzy C-Means**: Soft clustering; each point has membership degree [0,1] for all clusters; generalizes K-Means

## Important Concepts

- K-Means limitations: assumes spherical clusters, sensitive to initialization, requires k specification
- Hierarchical advantages: no k needed, produces dendrogram showing cluster relationships at all scales
- DBSCAN advantages: finds arbitrary shapes, robust to outliers, auto-determines cluster count
- GMM advantages: probabilistic interpretation, soft clustering, captures cluster overlap

## Notes

- K-Means algorithm: initialize k centroids, assign points to nearest, update centroids, repeat until convergence
- Hierarchical produces dendrogram; cut at desired height for clusters
- DBSCAN parameters: epsilon (neighborhood radius), minPts (minimum points for core)
- Compare: K-Means (fast, spherical), Hierarchical (dendrogram, no k), DBSCAN (arbitrary shape, outliers)
