# Feature Engineering and Dimensionality Reduction Techniques

### Definition

- Feature Engineering: The process of selecting, transforming, and combining raw data features to improve model performance and interpretability.
- Dimensionality Reduction: The process of reducing the number of features in a dataset while preserving the most important information.

### Feature Engineering Techniques

- **Data Cleaning**: Handling missing values, outliers, and errors in the data.
- **Data Transformation**: Scaling, normalization, and feature scaling.
- **Feature Selection**: Combining multiple features into a single feature (e.g., principal component analysis).
- **Feature Extraction**: Creating new features from existing ones (e.g., polynomial features).
- **Feature Engineering using Domain Knowledge**: Using domain knowledge to create relevant features (e.g., sentiment analysis).

### Dimensionality Reduction Techniques

- **Principal Component Analysis (PCA)**:
  - Formula: $X = U\Sigma V^T$
  - Definition: Reduces data to its principal components, retaining most of the variance.
- **Linear Discriminant Analysis (LDA)**:
  - Formula: $X = U\Sigma V^T$
  - Definition: Reduces data to its linearly independent components, retaining most of the variance.
- **t-Distributed Stochastic Neighbor Embedding (t-SNE)**:
  - Formula: $Z = \epsilon(A - \mu)^2 \cdot \sigma^{-2}$
  - Definition: Reduces high-dimensional data to a lower-dimensional representation.
- **Singular Value Decomposition (SVD)**:
  - Formula: $X = U\Sigma V^T$
  - Definition: Reduces data to its singular values and vectors.

### Theorems and Formulas

- **Covariance Matrix**: $Cov(X) = E[(X - \mu)(X - \mu)^T]$
- **Eigenvalue**: $\lambda$ is an eigenvalue of $C$ if $Cx = \lambda x$
- **Singular Value Decomposition (SVD)**: $X = U\Sigma V^T$

### Key Points

- Feature engineering and dimensionality reduction techniques can improve model performance and interpretability.
- PCA, LDA, t-SNE, and SVD are popular dimensionality reduction techniques.
- Domain knowledge and feature engineering can improve feature selection and extraction.
- Understanding the limitations and assumptions of each technique is crucial for effective application.
