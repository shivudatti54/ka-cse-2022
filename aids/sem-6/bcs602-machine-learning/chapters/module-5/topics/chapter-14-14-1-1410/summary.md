# Chapter-14 (14-1-14.10) Clustering Algorithms

### Definition

- Clustering: Grouping similar data points into clusters based on their characteristics.

### Proximity Measures

- Distance Metrics:
  - Euclidean Distance
  - Manhattan Distance
  - Minkowski Distance
- Proximity Functions:
  - Inner Product Space
  - Cosine Similarity

### Hierarchical Clustering

- Types:
  - Agglomerative Clustering
  - Divisive Clustering
- Methods:
  - Single Linkage
  - Complete Linkage
  - Average Linkage
  - Ward's Minimum Variance

### Important Formulas

- Euclidean Distance: $d(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + ... + (x_n - y_n)^2}$
- Manhattan Distance: $d(x, y) = \sum_{i=1}^{n} |x_i - y_i|$
- Cosine Similarity: $\cos(\theta) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}$

### Theorems

- Clustering Theorem: The clustering obtained by a particular algorithm is not unique.
- Completeness Theorem: If a clustering algorithm is complete, it will always find a clustering.
