# Feature Scaling and Selection - Summary

## Key Definitions and Concepts

- **Feature Scaling**: Preprocessing technique to normalize the range of independent features, essential for distance-based and gradient descent algorithms.

- **Min-Max Scaling**: Transforms features to [0,1] range using formula (X - Xmin) / (Xmax - Xmin); sensitive to outliers.

- **Standardization (Z-score)**: Rescales to zero mean and unit variance using (X - μ) / σ; preferred for normally distributed data.

- **Robust Scaling**: Uses median and IQR: (X - Q2) / (Q3 - Q1); resistant to outliers.

- **Feature Selection**: Process of selecting relevant features to improve model performance, reduce overfitting, and decrease computational cost.

- **Filter Methods**: Feature selection using statistical tests independent of ML algorithms (Correlation, Chi-square, ANOVA, Mutual Information).

- **Wrapper Methods**: Use ML model to evaluate feature subsets (Forward Selection, Backward Elimination, RFE).

- **Embedded Methods**: Perform selection during model training (Lasso, Ridge, Tree-based importance).

## Important Formulas and Theorems

| Method | Formula | Best For |
|--------|---------|----------|
| Min-Max | (X - Xmin) / (Xmax - Xmin) | Bounded data, Neural Networks |
| Standardization | (X - μ) / σ | Normal distribution, Linear models |
| Robust | (X - Q2) / (Q3 - Q1) | Data with outliers |

## Key Points

1. Always scale for: KNN, SVM, K-Means, Neural Networks, Logistic Regression, Linear Regression
2. No scaling needed for: Tree-based algorithms (Random Forest, Decision Trees, XGBoost)
3. Lasso (L1) performs automatic feature selection by zeroing coefficients
4. Correlation > 0.7 between features indicates multicollinearity
5. Filter methods are fast but ignore feature interactions; Wrapper methods capture interactions but are computationally expensive
6. Chi-square test is for categorical features; ANOVA F-test is for continuous features
7. PCA creates new components rather than selecting existing features
8. Forward selection adds features one-by-one; backward elimination removes features iteratively

## Common Mistakes to Avoid

1. Applying Min-Max scaling when outliers are present (use Robust scaling instead)
2. Scaling tree-based models unnecessarily (they are scale-invariant)
3. Using correlation for non-linear relationships (use Mutual Information instead)
4. Selecting too many features leading to overfitting
5. Not considering feature interactions when using filter methods alone

## Revision Tips

1. Practice coding all three scaling methods on sample datasets to understand their effects
2. Remember the algorithm classification: scale for distance/gradient methods, not for trees
3. Create a decision tree for selection method choice: Filter (fast, preliminary) → Wrapper (accurate, slow) → Embedded (balanced)
4. Focus on practical exam scenarios: identify whether scaling/selection is needed based on the algorithm specified
5. Understand when to use which selection method based on data type (categorical vs continuous) and problem type (classification vs regression)