# Density-Based Methods

## Overview

Density-based clustering identifies clusters as high-density regions separated by low-density regions. DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is the most popular algorithm, discovering clusters of arbitrary shape while automatically identifying outliers as noise points.

## Key Points

- **DBSCAN Algorithm**: Define epsilon (ε) neighborhood radius and minPts threshold; classify points as core (≥minPts neighbors), border (in core's neighborhood), or noise
- **Core Point**: Has at least minPts points within ε radius (including itself); cluster centers
- **Border Point**: Within ε of core point but has < minPts neighbors; cluster periphery
- **Noise Point**: Not core or border; outliers automatically identified
- **Cluster Formation**: Core points form clusters; border points assigned to nearby cores; connected core points in same cluster
- **Advantages**: Finds arbitrary shapes, robust to outliers, automatically determines cluster count, no centroid assumption

## Important Concepts

- Parameters: epsilon ε (neighborhood radius) and minPts (density threshold); critical for performance
- Parameter selection: k-distance plot for ε; minPts typically 2×dimensions or domain knowledge
- Reachability: point p density-reachable from q if path of core points connects them
- Complexity: O(n²) naive implementation; O(n log n) with spatial indexing (KD-tree, R-tree)

## Notes

- DBSCAN parameters: epsilon (neighborhood radius), minPts (minimum points for core)
- Point types: Core (≥minPts neighbors), Border (near core, <minPts neighbors), Noise (outliers)
- Advantages: arbitrary shapes, auto cluster count, outlier detection, no spherical assumption
- K-distance plot helps choose epsilon: plot sorted distance to k-th nearest neighbor, look for elbow
