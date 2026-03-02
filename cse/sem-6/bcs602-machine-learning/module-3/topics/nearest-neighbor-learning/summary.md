# Nearest Neighbor Learning

## Overview

Nearest Neighbor learning predicts by finding the most similar training instances and using their labels or values. K-Nearest Neighbors (KNN) extends this by using k closest neighbors, providing robustness through majority voting (classification) or averaging (regression).

## Key Points

- **Algorithm**: For query x, find k closest training points, predict via majority vote (classification) or average (regression)
- **K Selection**: Small k → low bias, high variance (overfitting); Large k → high bias, low variance (underfitting); use cross-validation for optimal k
- **Distance Metrics**: Euclidean d = √Σ(xi-yi)²; Manhattan d = Σ|xi-yi|; choice affects decision boundaries
- **Decision Boundary**: Non-linear, piecewise; can be arbitrarily complex; Voronoi diagram for k=1
- **Lazy Learning**: No training phase; stores all data; prediction O(n) per query
- **Feature Scaling**: Critical - standardize features to [0,1] or z-scores; prevents large-range features from dominating

## Important Concepts

- Odd k prevents ties in binary classification
- Weighted KNN: weight neighbors by inverse distance (closer neighbors more influence)
- Efficient search: KD-trees, Ball trees reduce prediction time from O(n) to O(log n)
- Curse of dimensionality: performance degrades in high dimensions; dimensionality reduction helps

## Notes

- Memorize KNN algorithm steps: compute distances, find k nearest, majority vote/average
- K selection via cross-validation - plot error vs k to find optimal
- Feature scaling essential - explain impact with example (age in years vs salary in dollars)
- Understand k=1 (Voronoi diagram) vs k>1 (smoother boundaries)
- Compare time complexity: training O(1), prediction O(n) without optimization
