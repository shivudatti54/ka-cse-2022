# Proximity Measures

## Overview

Proximity measures quantify similarity or dissimilarity between data points, forming the foundation of clustering algorithms. Different measures are suited for different data types and contexts—Euclidean for continuous features, Cosine for text, Jaccard for sets—with the choice critically impacting clustering quality.

## Key Points

- **Euclidean Distance**: d = √Σ(xi-yi)²; most common for continuous features; sensitive to magnitude and scale
- **Manhattan Distance**: d = Σ|xi-yi|; L1 norm; robust to outliers; useful for grid-like data
- **Cosine Similarity**: sim = (x·y)/(||x||\*||y||); measures angle not magnitude; standard for text/sparse data; range [-1,1]
- **Jaccard Coefficient**: J(A,B) = |A∩B|/|A∪B|; for sets; measures overlap; useful for binary/categorical data
- **Correlation**: Pearson correlation measures linear relationship; ignores magnitude, focuses on pattern
- **Minkowski Distance**: d = (Σ|xi-yi|^p)^(1/p); p=1 Manhattan, p=2 Euclidean, p=∞ Chebyshev; generalizes distance metrics

## Important Concepts

- Feature scaling: distance metrics sensitive to scale; standardize features to [0,1] or z-scores
- Similarity vs dissimilarity: similarity (higher = more similar), distance (lower = more similar)
- Distance properties: non-negativity, identity, symmetry, triangle inequality (for metric spaces)
- Curse of dimensionality: distances become similar in high dimensions; relative contrast diminishes

## Notes

- Euclidean: continuous features, magnitude matters; Manhattan: robust to outliers, grid data
- Cosine: text/sparse data, angle not magnitude; Jaccard: sets/binary data, overlap measure
- Feature scaling critical for distance-based methods: standardize to prevent large-range features dominating
- Choice depends on data type: continuous→Euclidean/Manhattan, text→Cosine, categorical→Jaccard
