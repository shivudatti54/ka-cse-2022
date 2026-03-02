# Feature Engineering and Dimensionality Reduction Techniques

### Overview

- Feature engineering is the process of transforming raw data into a more suitable format for modeling.
- Dimensionality reduction is the process of reducing the number of features in a dataset while preserving the most important information.

### Feature Engineering

- **Feature selection**: Selecting a subset of relevant features from the dataset.
  - Criteria: Correlation, Mutual Information, Recursive Feature Elimination (RFE)
  - Formulas:
    - Correlation coefficient: ρ(X, Y) = cov(X, Y) / (σ_X \* σ_Y)
    - Mutual Information: I(X; Y) = H(X) + H(Y) - H(X, Y)
- **Feature extraction**: Creating new features from existing ones.
  - Techniques: Principal Component Analysis (PCA), t-Distributed Stochastic Neighbor Embedding (t-SNE), Autoencoders
  - Formulas:
    - PCA: X_new = X \* V
    - t-SNE: X_new = t-SNE(X)
- **Feature scaling**: Scaling features to have similar magnitudes.
  - Techniques: Min-Max Scaler, Standard Scaler
  - Formula:
    - Min-Max Scaler: X_scaled = (X - min(X)) / (max(X) - min(X))
- **Feature transformation**: Transforming features into a more suitable format.
  - Techniques: Log transformation, Polynomial transformation

### Dimensionality Reduction

- **Principal Component Analysis (PCA)**:
  - Reduces dimensionality by finding the principal components of the data.
  - Formula: X_new = X \* V
- **t-Distributed Stochastic Neighbor Embedding (t-SNE)**:
  - Reduces dimensionality by preserving the local structure of the data.
  - Formula: X_new = t-SNE(X)
- **Autoencoders**:
  - Reduces dimensionality by learning a representation of the data.
  - Formula: X_new = Autoencoder(X)
- **Singular Value Decomposition (SVD)**:
  - Reduces dimensionality by decomposing the data into its singular values and vectors.
  - Formula: X_new = U \* Σ \* V^T
- **Curse of Dimensionality**:
  - Theoretical concept: As the number of features increases, the volume of the feature space increases exponentially.

### Important Formulas and Theorems

- **Principal Component Analysis (PCA)**:
  - X_new = X \* V
  - V = U^T \* Σ
- **t-Distributed Stochastic Neighbor Embedding (t-SNE)**:
  - X_new = t-SNE(X)
  - t-SNE is a non-linear dimensionality reduction technique
- **Singular Value Decomposition (SVD)**:
  - X_new = U \* Σ \* V^T
  - SVD is a factorization technique for matrix decomposition

Note: This is a concise summary of key points in feature engineering and dimensionality reduction techniques. For a more in-depth understanding, refer to the relevant literature and resources.
