# Clustering Algorithms

## Introduction

Clustering is an unsupervised learning technique that groups similar data points together without predefined labels. Different clustering algorithms use different strategies to discover natural groupings in data. This topic provides an overview of the major categories.

## What is Clustering?

**Goal**: Partition data into groups (clusters) such that:

- Points within a cluster are similar to each other (high intra-cluster similarity)
- Points in different clusters are dissimilar (low inter-cluster similarity)

**Key distinction from classification**: Clustering has no predefined labels. The algorithm discovers groups purely from data structure.

## Categories of Clustering Algorithms

### 1. Partitional Clustering

**Approach**: Divides data into K non-overlapping clusters simultaneously.

**K-Means Algorithm**:

1. Initialize K centroids randomly
2. Assign each point to the nearest centroid
3. Recalculate centroids as the mean of assigned points
4. Repeat steps 2-3 until convergence

**Characteristics**:

- Requires K to be specified in advance
- Converges to local optima (result depends on initialization)
- Assumes spherical, equally-sized clusters
- Time complexity: O(n·K·t), where t is iterations
- Sensitive to outliers

**K-Medoids (PAM)**:

- Uses actual data points as centers (medoids) instead of means
- More robust to outliers
- Higher computational cost than K-Means

### 2. Hierarchical Clustering

**Approach**: Builds a tree-like hierarchy of clusters.

**Agglomerative (Bottom-Up)**:

1. Start with each point as its own cluster
2. Find the two closest clusters
3. Merge them into one cluster
4. Repeat until only one cluster remains

**Divisive (Top-Down)**:

1. Start with all points in one cluster
2. Split the most heterogeneous cluster
3. Repeat until each point is its own cluster

**Linkage Methods**:

- **Single linkage**: Minimum distance between clusters
- **Complete linkage**: Maximum distance between clusters
- **Average linkage**: Average distance between all pairs
- **Ward's method**: Minimizes increase in total within-cluster variance

**Dendrogram**: Tree diagram showing the merging/splitting history. Cut at a specific height to get K clusters.

**Characteristics**:

- Does not require specifying K in advance
- Produces interpretable dendrograms
- Time complexity: O(n³) or O(n² log n) with optimizations
- Not suitable for very large datasets

### 3. Density-Based Clustering

**Approach**: Groups points in high-density regions separated by low-density areas.

**DBSCAN Algorithm**:

- Parameters: ε (neighborhood radius), MinPts (minimum points for core)
- **Core point**: Has at least MinPts within ε-neighborhood
- **Border point**: Within ε of a core point but has fewer than MinPts
- **Noise point**: Neither core nor border

**Algorithm**:

1. Find all core points
2. Connect core points within ε of each other
3. Assign border points to the nearest core point's cluster
4. Mark remaining points as noise

**Characteristics**:

- Discovers clusters of arbitrary shape
- Automatically determines number of clusters
- Robust to outliers (marks them as noise)
- Struggles with clusters of varying densities
- Sensitive to ε and MinPts parameters

**OPTICS**: Extension of DBSCAN that handles varying densities.

### 4. Grid-Based Clustering

**Approach**: Divides the data space into a grid of cells and performs clustering on the grid structure.

**STING (Statistical Information Grid)**:

- Divides space into rectangular cells at different resolutions
- Stores statistical summaries in each cell
- Top-down approach through grid levels

**CLIQUE (Clustering in Quest)**:

- Identifies dense subspaces in high-dimensional data
- Combines grid-based and density-based approaches

**Characteristics**:

- Very fast: independent of number of data points
- Depends on grid granularity
- Good for spatial data mining
- May miss irregular cluster shapes

## Choosing the Right Algorithm

| Criterion        | K-Means   | Hierarchical             | DBSCAN                 | Grid-based     |
| ---------------- | --------- | ------------------------ | ---------------------- | -------------- |
| K required?      | Yes       | No (dendrogram)          | No                     | No             |
| Cluster shapes   | Spherical | Any (depends on linkage) | Arbitrary              | Grid-dependent |
| Outlier handling | Poor      | Moderate                 | Good (noise detection) | Moderate       |
| Scalability      | Good      | Poor (large n)           | Moderate               | Very good      |
| Data type        | Numerical | Any                      | Numerical              | Numerical      |

## Evaluation Metrics

### Internal Metrics (No ground truth)

**Silhouette Score**:
s(i) = (b(i) - a(i)) / max(a(i), b(i))

- a(i): Average distance to points in same cluster
- b(i): Average distance to points in nearest other cluster
- Range: [-1, 1], higher is better

**Davies-Bouldin Index**:
DB = (1/K) Σ max\_{j≠i} [(σᵢ + σⱼ) / d(cᵢ, cⱼ)]

- Lower values indicate better clustering
- Measures ratio of within-cluster scatter to between-cluster separation

**Dunn Index**:
D = min(inter-cluster distance) / max(intra-cluster diameter)

- Higher values indicate better clustering

### External Metrics (With ground truth)

- **Rand Index**: Measures agreement between clustering and ground truth
- **Adjusted Rand Index**: Corrects for chance agreement
- **Normalized Mutual Information**: Information-theoretic measure

## The Elbow Method

For K-Means, selecting K:

1. Run K-Means for K = 1, 2, 3, ..., max_K
2. Plot WCSS (Within-Cluster Sum of Squares) vs K
3. Look for the "elbow" - where the rate of decrease sharply changes
4. The K at the elbow is a good choice

## Applications

| Domain           | Application               | Common Algorithm |
| ---------------- | ------------------------- | ---------------- |
| Marketing        | Customer segmentation     | K-Means          |
| Biology          | Gene expression grouping  | Hierarchical     |
| Astronomy        | Star classification       | DBSCAN           |
| Geography        | Spatial pattern detection | Grid-based       |
| Social Networks  | Community detection       | Various          |
| Image Processing | Image segmentation        | K-Means, DBSCAN  |

## Exam Tips

- Know the four main categories and their representative algorithms
- Be able to compare K-Means, Hierarchical, and DBSCAN
- Understand the Elbow Method and Silhouette Score
- Know when to use each type of clustering
- Be prepared to explain DBSCAN's core/border/noise classification
