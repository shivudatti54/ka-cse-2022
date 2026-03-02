# Similarity-Based Learning

## Overview

Similarity-based learning makes predictions by finding training examples most similar to the query point. Unlike model-based approaches that learn global functions, similarity-based methods use local information, making them intuitive, non-parametric, and effective for complex decision boundaries.

## Key Points

- **Core Principle**: Similar instances have similar outputs; prediction based on neighbors' labels/values
- **Instance-Based**: Stores entire training set; no explicit training phase (lazy learning)
- **Distance Metrics**: Euclidean (continuous features), Manhattan, Minkowski, Hamming (categorical), Cosine (text/sparse data)
- **Applications**: K-Nearest Neighbors (KNN), Locally Weighted Regression, Case-Based Reasoning, Collaborative Filtering
- **Advantages**: No training time, adapts to new data easily, naturally handles multiclass, robust to noisy training data
- **Disadvantages**: Slow predictions (search all training data), memory-intensive, sensitive to distance metric and feature scaling

## Important Concepts

- Distance metric choice critical: Euclidean for continuous, Hamming for categorical, Cosine for text
- Feature scaling essential: features with larger ranges dominate distance calculations
- Curse of dimensionality: distances lose meaning in high dimensions; all points equidistant
- Weighted similarity: give closer neighbors more influence on prediction

## Notes

- Explain lazy learning: no training phase, all computation at prediction time
- Know multiple distance metrics and when to use each
- Understand curse of dimensionality: distances become similar in high dimensions
- Compare with model-based: no global function learned, uses local information only
