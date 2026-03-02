# **Revisions Notes: Clustering Algorithms**

### Partitional Clustering Algorithm

- **Definition:** A partitioning technique where data points are divided into distinct clusters based on their similarity.
- **Examples:**
  - K-Means Clustering
  - Hierarchical Clustering (e.g., Agglomerative Clustering)
- **Key Formulas:**
  - K-Means: Centroid-based clusters
  - Hierarchical Clustering: Linkage distance (e.g., Euclidean distance)
- **Theorems:**
  - K-Means: Optimality theorem ( guarantees optimal solution for a given number of clusters)

### Density-based Methods

- **Definition:** Clustering algorithms that group data points based on their density and proximity to each other.
- **Examples:**
  - DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
  - OPTICS (Ordering Points To Identify the Clustering Structure)
- **Key Formulas:**
  - DBSCAN: ε (neighborhood radius), ρ (density threshold)
  - OPTICS: Reachability distance, Density-based spacing
- **Theorems:**
  - DBSCAN: Density-based spatial clustering theorem ( guarantees cluster formation for a given density threshold)

### Grid-based Approach

- **Definition:** A spatial partitioning technique that divides the data space into cells or grids.
- **Examples:**
  - Grid-based clustering algorithms (e.g., k-means++, grid-based hierarchical clustering)
  - Spatial autocorrelation analysis
- **Key Formulas:**
  - Grid-based clustering: Cell size, number of clusters
- **Theorems:**
  - Spatial autocorrelation: Pearson correlation coefficient (ρ) ( measures correlation between neighboring data points)

### Important Terms

- **Cluster:** A group of data points that are similar to each other.
- **Density:** The number of data points per unit area.
- **Proximity:** The distance between two data points.
- **Noise:** Unwanted data points that do not belong to any cluster.
