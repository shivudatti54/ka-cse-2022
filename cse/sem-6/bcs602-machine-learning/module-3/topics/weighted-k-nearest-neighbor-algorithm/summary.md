# Weighted K-Nearest Neighbor Algorithm

## Overview

Weighted KNN extends standard KNN by assigning different weights to neighbors based on their distance from the query point. Closer neighbors receive higher weights, making predictions more accurate by giving more importance to nearby instances than distant ones.

## Key Points

- **Weighting Scheme**: Common: w = 1/distance or w = exp(-distance²/2σ²); closer neighbors have higher weights
- **Classification**: Weighted vote: class = argmax Σ(wi \* I(yi = c)) where I is indicator function
- **Regression**: Weighted average: ŷ = Σ(wi \* yi) / Σwi; smooth interpolation based on distance
- **Advantages**: More robust than unweighted KNN, reduces impact of outliers, smoother decision boundaries, better handles non-uniform data distributions
- **Distance-Based Weights**: Inverse distance w = 1/d; Gaussian kernel w = exp(-d²/2σ²); rank-based w = 1/rank
- **Kernel Function**: Gaussian kernel most common; bandwidth parameter σ controls locality (analogous to k in KNN)

## Important Concepts

- Tie resolution: weighted voting naturally handles ties by giving more weight to closer neighbors
- Optimal weighting: Gaussian kernel with cross-validated σ often performs best
- Computational cost: same as standard KNN - O(n) per prediction without optimization
- Feature scaling still critical: affects both distance calculation and weights

## Notes

- Explain weighting schemes: inverse distance 1/d, Gaussian exp(-d²/2σ²)
- Understand advantage over standard KNN: closer neighbors more important
- Classification uses weighted vote; regression uses weighted average
- Bandwidth σ selection via cross-validation like k in standard KNN
