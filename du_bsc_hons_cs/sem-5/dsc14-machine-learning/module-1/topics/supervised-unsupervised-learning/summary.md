# Supervised and Unsupervised Learning - Summary

## Key Definitions and Concepts

- **Machine Learning**: A subset of AI that enables systems to learn from data and improve performance without explicit programming.

- **Supervised Learning**: Learning from labeled data (input-output pairs) to predict outputs for new data. Requires ground truth labels during training.

- **Unsupervised Learning**: Learning from unlabeled data to discover hidden patterns, structures, or relationships. No predefined outputs are provided.

## Important Formulas and Theorems

- **Linear Regression**: y = β₀ + β₁x + ε (predicts continuous values using a straight line)
- **Logistic Regression**: P(y=1|x) = 1/(1 + e^-(β₀ + β₁x)) (transforms to probability using sigmoid)
- **K-Means**: Minimize within-cluster sum of squares (WCSS) by iteratively updating centroids
- **PCA**: Maximize variance while reducing dimensionality through eigenvector decomposition

## Key Points

- Supervised learning has two main types: **Classification** (discrete labels) and **Regression** (continuous values)
- Unsupervised learning has two main types: **Clustering** (grouping similar points) and **Dimensionality Reduction** (reducing features)
- Common supervised algorithms: Linear Regression, Logistic Regression, Decision Trees, Random Forests, SVM, Naive Bayes
- Common unsupervised algorithms: K-Means, Hierarchical Clustering, DBSCAN, PCA
- Supervised needs labeled data; unsupervised works with raw, unlabeled data
- Classification metrics: Accuracy, Precision, Recall, F1-Score; Regression metrics: MSE, RMSE, R²

## Common Mistakes to Avoid

1. **Confusing Logistic Regression with Regression**: Despite its name, Logistic Regression is a classification algorithm, not regression.
2. **Using classification algorithms for regression problems**: Linear Regression outputs continuous values; don't use it for categorical outputs.
3. **Ignoring feature scaling**: Many algorithms (especially K-Means and PCA) are sensitive to feature scales—always normalize or standardize data.
4. **Choosing wrong K in K-Means**: Not validating the number of clusters; use methods like elbow method or silhouette score.

## Revision Tips

1. Create a comparison table between supervised and unsupervised learning covering data type, output, algorithms, and applications.
2. Practice mapping real-world problems to appropriate ML paradigms—spam detection = classification, customer segmentation = clustering.
3. Remember the axis of distinction: labeled vs unlabeled data is the fundamental difference.
4. Review algorithm characteristics—know which algorithms belong to which paradigm and why.