# Grid-Based Approach

## Overview

Grid-based clustering divides the data space into a grid of cells and performs clustering on the grid structure rather than individual data points. Methods like STING and CLIQUE are fast and scalable, quantizing space into multi-resolution grids for efficient processing of large spatial datasets.

## Key Points

- **Grid Partitioning**: Divide feature space into finite number of cells forming grid; cluster operations on cells not individual points
- **STING (Statistical Information Grid)**: Hierarchical grid structure; each cell stores statistical info (mean, variance, count); bottom-up clustering
- **CLIQUE**: Grid-based subspace clustering; finds clusters in subspaces of high-dimensional data; density-based approach on grid
- **Advantages**: Fast O(n) time (independent of data size after grid creation), scalable to large datasets, efficient for spatial data
- **Disadvantages**: Quality depends on grid granularity, cannot find clusters smaller than cell size, sensitive to grid orientation
- **Multi-Resolution**: Hierarchical grid levels allow different granularities; coarse to fine clustering

## Important Concepts

- Grid granularity trade-off: fine grid (accurate but expensive), coarse grid (fast but may merge distinct clusters)
- Cell density threshold: cells exceeding threshold form cluster cores
- Boundary refinement: post-processing to smooth cluster boundaries
- Subspace clustering: CLIQUE finds dense regions in subspaces, handling curse of dimensionality

## Notes

- Grid-based: partition space into cells, cluster on cells not points
- STING: hierarchical statistical grid; CLIQUE: subspace clustering on grid
- Advantages: O(n) time complexity, scalable, efficient for spatial data
- Disadvantages: grid granularity affects quality, cannot find sub-cell clusters
