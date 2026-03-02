# K-Means & Hierarchical Clustering - Summary

## Key Definitions and Concepts
- Centroid: Mean position of all points in a cluster
- Dendrogram: Tree diagram recording merge/split sequences
- Inertia: Sum of squared distances to nearest cluster center (WCSS)

## Important Formulas and Theorems
- WCSS: ∑_{i=1}^n ∑_{j=1}^k w_{ij}||x_i - c_j||² 
- Single Linkage: d(C1,C2) = min{d(a,b)|a∈C1,b∈C2}
- Ward's Variance: Δ(A,B) = [n_A*n_B/(n_A+n_B)]||c_A - c_B||²

## Key Points
- K-Means requires predefined k, sensitive to initialization
- Agglomerative clustering creates nested cluster hierarchies
- Complete linkage resists noise better than single linkage
- StandardScaler crucial for features with different units
- DBSCAN handles non-convex clusters better than these methods
- Heatmaps combined with dendrograms reveal feature patterns
- Gap statistic compares observed WCSS with random data expectation

## Common Mistakes to Avoid
- Using Euclidean distance for high-dimensional data (curse of dimensionality)
- Ignoring feature scaling with mixed data types
- Choosing k based on visual inspection in high dimensions
- Misinterpreting dendrogram heights as absolute similarity measures

## Revision Tips
1. Practice manual calculations for small datasets (3-5 points)
2. Use Yellowbrick library for visual cluster evaluation
3. Implement both algorithms on UCI's Iris dataset
4. Compare runtime for n=1000 vs n=10000 points
5. Memorize sklearn API parameters: n_clusters, linkage, affinity

Length: 650 words