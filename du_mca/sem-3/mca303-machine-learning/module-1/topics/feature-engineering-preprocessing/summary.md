# Feature Engineering & Preprocessing - Summary

## Key Definitions and Concepts
- **Feature Engineering**: Process of creating new features from raw data
- **Data Leakage**: Using future/test data information during training
- **Cardinality**: Number of unique values in categorical feature
- **Imputation**: Replacing missing values with statistical estimates
- **Embedding**: Dense vector representation of categorical data

## Important Formulas and Theorems
- **Z-score**: \( z = \frac{x - \mu}{\sigma} \)
- **Min-Max Scaling**: \( x' = \frac{x - x_{min}}{x_{max} - x_{min}} \)
- **TF-IDF**: \( w_{i,j} = tf_{i,j} \times \log(\frac{N}{df_i}) \)
- **SMOTE**: Synthetic Minority Over-sampling Technique
- **PCA**: \( \mathbf{X} = \mathbf{U\Sigma V^T} \) (Singular Value Decomposition)

## Key Points
- Always split data before preprocessing to prevent leakage
- Tree-based models don't require feature scaling
- One-hot encoding increases dimensionality (curse of dimensionality)
- Target encoding risks overfitting - use cross-validated means
- Feature importance ≠ causality - correlation doesn't imply causation
- Automated feature engineering tools can create 1000+ features
- Temporal features require special handling (time-series cross-validation)

## Common Mistakes to Avoid
- Applying normalization to count data (use log transform instead)
- Imputing test set missing values using test set statistics
- Using accuracy as metric for imbalanced datasets
- Forgetting to encode categorical variables before model training

## Revision Tips
1. Practice implementing ColumnTransformer pipelines
2. Compare results with/without feature scaling for SVM
3. Memorize Scikit-learn's imputation class hierarchy
4. Create cheat sheet for encoding methods vs data types