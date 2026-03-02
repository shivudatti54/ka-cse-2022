# Partitional Clustering Algorithm

## Overview

Partitional clustering algorithms divide data into non-overlapping subsets (partitions) where each data point belongs to exactly one cluster. K-Means is the most popular partitional algorithm, iteratively refining cluster assignments to minimize within-cluster variance, making it efficient for large datasets with spherical clusters.

## Key Points

- **K-Means Algorithm**: (1) Initialize k centroids randomly, (2) Assign each point to nearest centroid, (3) Recalculate centroids as cluster means, (4) Repeat steps 2-3 until convergence
- **Objective Function**: Minimize inertia (within-cluster sum of squared distances): J = ΣΣ||xi - μk||² where μk is centroid of cluster k
- **Convergence**: Guaranteed to converge but to local optimum (not necessarily global); multiple runs with different initializations recommended
- **K-Means++**: Smart initialization that spreads initial centroids; improves convergence speed and quality
- **Computational Complexity**: O(n*k*i\*d) where n=points, k=clusters, i=iterations, d=dimensions; efficient for large datasets
- **Limitations**: Assumes spherical clusters, sensitive to outliers, requires k specification, cannot find clusters of arbitrary shape

## Important Concepts

- Elbow method: plot inertia vs k; elbow point suggests optimal k
- Silhouette analysis: measures cluster quality; helps select k
- Mini-batch K-Means: uses random samples for faster training on very large datasets
- Hard clustering: each point assigned to exactly one cluster (vs soft clustering with probabilities)

## Notes

- K-Means algorithm steps: initialize → assign → update centroids → repeat until convergence
- Objective: minimize within-cluster sum of squared distances (inertia)
- K selection methods: elbow method (plot inertia vs k), silhouette analysis
- Limitations: spherical clusters assumption, sensitive to initialization and outliers, requires k
