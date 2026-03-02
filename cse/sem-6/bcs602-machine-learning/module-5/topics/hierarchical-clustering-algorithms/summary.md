# Hierarchical Clustering Algorithms

## Overview

Hierarchical clustering builds a tree-like structure (dendrogram) representing nested groupings of data at multiple scales. It comes in two flavors: agglomerative (bottom-up merging) and divisive (top-down splitting), providing intuitive visualization of cluster relationships without requiring k specification upfront.

## Key Points

- **Agglomerative (Bottom-Up)**: Start with each point as cluster; iteratively merge closest pairs; produces dendrogram from leaves to root
- **Divisive (Top-Down)**: Start with all points in one cluster; recursively split into smaller clusters; computationally expensive, less common
- **Linkage Criteria**: Single (minimum distance between clusters), Complete (maximum distance), Average (mean distance), Ward (minimize variance increase)
- **Dendrogram**: Tree diagram showing cluster merges/splits at different heights; cut at desired height to obtain flat clustering
- **Distance Matrix**: Compute pairwise distances between all points; updated after each merge; O(n²) space complexity
- **No K Required**: Dendrogram shows clusters at all scales; analyst chooses cut height based on problem requirements

## Important Concepts

- Single linkage: tends to create long chains (sensitive to noise)
- Complete linkage: creates compact clusters but sensitive to outliers
- Average linkage: balance between single and complete
- Ward's method: minimizes within-cluster variance; often gives best results
- Complexity: O(n³) time for naive implementation; O(n²log n) with efficient methods

## Notes

- Agglomerative (merge) vs Divisive (split); agglomerative more common
- Linkage types: Single (min distance), Complete (max distance), Average, Ward (minimize variance)
- Dendrogram visualization shows cluster hierarchy; cut at height for desired number of clusters
- Advantage: no k needed upfront; Disadvantage: O(n²) or O(n³) complexity, cannot undo merges
