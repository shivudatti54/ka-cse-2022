# Decision Tree Induction Algorithms

## Overview

Decision tree induction algorithms systematically construct trees from training data using different splitting criteria and strategies. Major algorithms include ID3 (Information Gain), C4.5 (Gain Ratio), and CART (Gini Index), each with distinct characteristics for handling data types and preventing overfitting.

## Key Points

- **ID3 (Iterative Dichotomiser 3)**: Uses Information Gain (entropy-based); handles categorical features; prone to overfitting; no pruning; bias toward many-valued attributes
- **C4.5 (Successor to ID3)**: Uses Gain Ratio (normalized IG); handles continuous and categorical; includes pruning; handles missing values; produces classification rules
- **CART (Classification and Regression Trees)**: Uses Gini Index (classification) or Variance Reduction (regression); produces binary trees; includes cost-complexity pruning; handles numerical and categorical
- **Splitting Criteria**: ID3/C4.5 use Entropy, C4.5 uses Gain Ratio, CART uses Gini; Gain Ratio reduces bias to many-valued features
- **Pruning**: ID3 (none), C4.5 (error-based), CART (cost-complexity); pruning reduces overfitting by removing branches
- **Tree Type**: ID3/C4.5 produce multi-way splits; CART produces binary splits only

## Important Concepts

- Gain Ratio = Information Gain / Split Information; penalizes features with many values
- Binary vs multi-way trees: CART always binary, ID3/C4.5 can have multiple branches per node
- Continuous features: C4.5 and CART find optimal split threshold; ID3 requires discretization
- Missing value handling: C4.5 uses probabilistic approach; CART uses surrogate splits

## Notes

- Compare algorithms: ID3 (basic, categorical only), C4.5 (improved, handles continuous), CART (binary, regression capable)
- Memorize splitting criteria: ID3 (IG), C4.5 (Gain Ratio), CART (Gini)
- Understand Gain Ratio advantage: reduces bias toward features with many distinct values
- Know pruning methods: error-based (C4.5), cost-complexity (CART)
