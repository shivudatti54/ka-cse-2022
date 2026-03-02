# Principal Component Analysis (PCA) - Summary

## Key Definitions and Concepts

- **Dimensionality Reduction**: The process of reducing the number of features in a dataset while preserving maximum information.
- **Principal Components**: Orthogonal linear combinations of original features that capture maximum variance in descending order.
- **Eigenvectors**: Direction vectors representing the axes of maximum variance in the transformed space.
- **Eigenvalues**: Scalar values indicating the amount of variance explained by each eigenvector.
- **Covariance Matrix**: A matrix describing how each pair of features varies together.

## Important Formulas and Theorems

- **Centered Data**: X_centered = X - μ (subtract mean from each feature)
- **Covariance Matrix**: Σ = (1/(n-1)) × X_centered^T × X_centered
- **Eigenvalue Equation**: Σv = λv
- **Variance Explained**: (λ_k / Σλ_i) × 100%
- **Data Projection**: X_reduced = X_centered × W, where W contains top k eigenvectors
- **Reconstruction**: X_reconstructed = X_reduced × W^T + μ

## Key Points

- PCA transforms correlated features into uncorrelated principal components.
- Principal components are ordered by variance explained—PC1 explains the most.
- Typically, 95-99% variance threshold determines the number of components to retain.
- Data must be standardized when features have different scales before applying PCA.
- PCA assumes linear relationships between variables.
- The number of principal components cannot exceed the number of original features.
- Principal components are always orthogonal (perpendicular) to each other.
- Scree plots help visualize where the "elbow" occurs for component selection.

## Common Mistakes to Avoid

1. **Forgetting to center data**: PCA requires centered (mean-subtracted) data; otherwise, the first component will capture the mean rather than variance.

2. **Ignoring feature scaling**: Using features with different scales will bias PCA toward high-magnitude features; always standardize when scales differ.

3. **Keeping too many components**: Retaining components that explain minimal variance adds noise without significant information.

4. **Misinterpreting PCA as feature selection**: PCA creates new composite features rather than selecting existing ones.

## Revision Tips

1. Practice computing PCA manually on simple 2×2 or 3×3 datasets to understand each step.

2. Memorize the PCA workflow: Standardize → Compute Covariance → Find Eigenvalues/Eigenvectors → Select Components → Transform Data.

3. Review sklearn PCA implementation—know how to extract explained_variance_ratio_ and components_.

4. Draw conceptual diagrams showing how data projects onto principal component axes.

5. Review previous year DU question papers for PCA-related problems and solution approaches.