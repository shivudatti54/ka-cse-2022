# **Feature Engineering and Dimensionality Reduction Techniques**

### Overview

- Feature engineering involves transforming raw data into a format that is more suitable for modeling
- Dimensionality reduction techniques reduce the number of features in a dataset while preserving most of the information

### Feature Engineering

---

- **Data normalization**
  - Scaling numeric features to a common range (e.g., 0-1)
  - Formula: `(x - mean) / std`
- **Encoding categorical variables**
  - One-hot encoding: creating a new feature for each category
  - Label encoding: assigning a unique integer value to each category
- **Feature extraction**
  - Extracting relevant features from text data (e.g., TF-IDF)
  - Extracting features from images (e.g., SIFT, Edge Detection)

### Dimensionality Reduction Techniques

---

- **1. Principal Component Analysis (PCA)**
  - Reduces dimensionality by projecting data onto principal axes
  - Formula: `X = U Σ V^T`
  - Theorem: Orthogonal transformation preserves variance
- **2. Linear Discriminant Analysis (LDA)**
  - Reduces dimensionality by projecting data onto axes that maximize class separation
  - Formula: `X = U Σ V^T`
  - Theorem: Linear transformation preserves class separation
- **3. t-Distributed Stochastic Neighbor Embedding (t-SNE)**
  - Reduces dimensionality by preserving local relationships between data points
  - Formula: `D = - \sum_{i,j} p_{ij} \log p_{ij}`
- **4. Singular Value Decomposition (SVD)**
  - Reduces dimensionality by projecting data onto singular vectors
  - Formula: `X = U Σ V^T`
  - Theorem: Orthogonal transformation preserves variance

### Other Techniques

---

- **Feature selection**
  - Selecting a subset of features that are most relevant to the problem
- **Dimensionality reduction using neural networks**
  - Using neural networks to reduce dimensionality

### Important Formulas and Definitions

---

- **Mean**: `E(x) = \sum x_i / n`
- **Variance**: `σ^2 = E(x^2) - (E(x))^2`
- **Standard deviation**: `σ = \sqrt{σ^2}`
- **Principal component**: `X = U Σ V^T`
- **Eigenvalue**: `λ`: the scalar by which a principal component is scaled
