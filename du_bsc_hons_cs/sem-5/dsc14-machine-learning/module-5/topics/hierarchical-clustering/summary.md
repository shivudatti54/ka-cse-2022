# Hierarchical Clustering - Summary

## Key Definitions and Concepts

- **Hierarchical Clustering**: An unsupervised learning technique that builds a hierarchy of clusters by recursively merging (agglomerative) or splitting (divisive) data points.
- **Dendrogram**: Tree-like visualization showing the nested clustering structure; horizontal cuts determine cluster assignments.
- **Linkage Method**: Defines how distance between clusters is calculated during merging—Single (minimum), Complete (maximum), Average (mean), Ward's (variance minimization).
- **Agglomerative Clustering**: Bottom-up approach starting with n individual clusters and merging until one cluster remains.
- **Cophenetic Correlation**: Measure of how well the dendrogram preserves original pairwise distances (closer to 1 = better).

## Important Formulas and Theorems

- **Euclidean Distance**: d(X,Y) = √(Σᵢ(Xᵢ - Yᵢ)²)
- **Manhattan Distance**: d(X,Y) = Σᵢ|Xᵢ - Yᵢ|
- **Single Linkage**: d(A,B) = min{d(a,b) : a ∈ A, b ∈ B}
- **Complete Linkage**: d(A,B) = max{d(a,b) : a ∈ A, b ∈ B}
- **Average Linkage**: d(A,B) = (1/|A||B|) Σₐ∈A Σᵦ∈B d(a,b)
- **Ward's Method**: d(A,B) = (|A||B|/|A|+|B|) × (μₐ - μᵦ)²

## Key Points

- Hierarchical clustering does not require pre-specifying the number of clusters (unlike K-means).
- Agglomerative is more commonly used due to simpler implementation; divisive is computationally expensive.
- Single linkage can create elongated clusters and is sensitive to outliers; complete linkage produces compact clusters.
- Ward's method typically yields the most balanced, spherical clusters.
- Dendrogram elbow method helps determine optimal cluster count—cut where vertical distance is largest.
- Time complexity is O(n²) for agglomerative, making it unsuitable for very large datasets.
- Results are deterministic and reproducible for the same data and parameters.

## Common Mistakes to Avoid

1. **Forgetting to scale data**: Using unscaled data with different measurement units distorts distance calculations.
2. **Choosing wrong linkage**: Applying single linkage to noisy data can produce poor, chain-like clusters.
3. **Ignoring dendrogram**: Simply taking a fixed number of clusters without analyzing the dendrogram structure.
4. **Overlooking distance metric**: Using Euclidean distance for text or high-dimensional data where cosine similarity is more appropriate.

## Revision Tips

1. Practice drawing small dendrograms by hand—start with 5-6 points and manually compute distances.
2. Memorize the characteristics of each linkage method to quickly answer comparison questions.
3. Remember: higher cuts on dendrogram = fewer clusters, lower cuts = more clusters.
4. Focus on when to use hierarchical vs. K-means: unknown k and need visualization = hierarchical; large n and known k = K-means.
5. Review the computational complexity—O(n² log n) for agglomerative is a frequently tested concept.