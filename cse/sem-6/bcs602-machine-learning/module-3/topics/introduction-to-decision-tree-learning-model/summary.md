# Introduction to Decision Tree Learning Model

## Overview

Decision trees are intuitive supervised learning models that partition the feature space using tree structures. Each internal node tests a feature, each branch represents an outcome, and each leaf assigns a class label (classification) or value (regression), making them highly interpretable.

## Key Points

- **Structure**: Root node (top), internal nodes (tests), branches (outcomes), leaf nodes (predictions); tree depth determines complexity
- **Splitting**: Choose feature and threshold that best separates classes; measured by impurity reduction (Gini, Entropy) or variance reduction (regression)
- **Classification**: Traverse from root to leaf based on feature tests; leaf's majority class is prediction
- **Regression**: Same traversal; leaf's mean value is prediction
- **Advantages**: Interpretable (white-box), handles categorical and numerical features, no feature scaling needed, captures non-linear relationships
- **Disadvantages**: Prone to overfitting (complex trees), unstable (small data changes alter tree), biased to features with many levels

## Important Concepts

- Top-down greedy splitting: choose best split at each node without backtracking (locally optimal, not globally)
- Stopping criteria: maximum depth, minimum samples per leaf, minimum impurity decrease
- Pruning: post-pruning (grow full tree then remove branches) reduces overfitting
- Missing values: can be handled via surrogate splits or separate branch

## Notes

- Understand tree structure: root → internal nodes (tests) → leaves (predictions)
- Splitting criteria: Gini impurity, Information Gain (entropy), Variance reduction
- Explain white-box nature: can visualize and explain every decision path
- Overfitting mitigation: pruning, max depth, min samples constraints
