# Dimensionality Reduction and Manifold Learning

## Comprehensive Study Material for MSc CS - Delhi University

---

## 1. Introduction

### What is Dimensionality Reduction?

Dimensionality reduction is a fundamental technique in machine learning and data science that aims to transform high-dimensional data into a lower-dimensional representation while preserving as much meaningful information as possible. In the context of the Delhi University MSc CS syllabus, this topic bridges theoretical foundations with practical applications.

### Why Does It Matter?

In modern computing, we frequently encounter datasets with hundreds or thousands of features—image pixels, sensor readings, gene expression data, or text embeddings. This "curse of dimensionality" creates several challenges:

- **Computational inefficiency**: Processing high-dimensional data requires significant memory and computation time
- **Statistical sparsity**: Data points become increasingly isolated as dimensions grow
- **Overfitting risk**: Models may memorize noise rather than learn generalizable patterns
- **Visualization impossibility**: Humans cannot perceive beyond 3D

### Real-World Relevance

| Application Domain | Example |
|-------------------|---------|
| Computer Vision | Reducing image dimensions for facial recognition |
| NLP | Word embedding compression for topic modeling |
| Bioinformatics | Gene expression analysis with thousands of genes |
| Finance | Portfolio optimization with many correlated assets |
| Medical Imaging | MRI/CT scan analysis and compression |

---

## 2. The Manifold Assumption

### Understanding Manifolds

A **manifold** is a topological space that locally resembles Euclidean space. In machine learning, the **manifold hypothesis** states that high-dimensional data often lies on or near a lower-dimensional manifold embedded in the high-dimensional space.

**Key Insight**: Not all dimensions are equally important. The intrinsic (true) dimensionality of data may be much lower than the observed dimensionality.

### Example: Swiss Roll Dataset

Consider the famous "Swiss Roll" dataset—a 3D dataset that unfolds onto a 2D plane:

```
Original 3D points: (x, y, z) where data lies on a coiled 2D surface
Reduced 2D representation: (u, v) representing position along the roll
```

The Euclidean distance in 3D space doesn't capture the true structure; manifold learning discovers the underlying 2D structure.

---

## 3. Mathematical Foundations

### Formal Problem Statement

Given a dataset $X = \{x_1, x_2, ..., x_n\}$ where each $x_i \in \mathbb{R}^D$ (high-dimensional space), find a mapping $f: \mathbb{R}^D \rightarrow \mathbb{R}^d$ where $d \ll D$, such that:

- **Distance Preservation**: Nearby points in high-dimensional space remain nearby in low-dimensional space
- **Structure Preservation**: Global and/or local structure is preserved
- **Information Retention**: Variance/information is maximized or reconstruction error is minimized

### Types of Dimensionality Reduction

#### Linear Methods
Methods that learn a linear projection: $y = W^T x$

- **Principal Component Analysis (PCA)**
- **Linear Discriminant Analysis (LDA)**
- **Factor Analysis**

#### Non-Linear Methods (Manifold Learning)
Methods that capture non-linear structure:

- **ISOMAP**
- **Locally Linear Embedding (LLE)**
- **t-Distributed Stochastic Neighbor Embedding (t-SNE)**
- **Spectral Methods**

---

## 4. Key Dimensionality Reduction Techniques

### 4.1 Principal Component Analysis (PCA)

#### Mathematical Formulation

PCA finds orthogonal directions (principal components) that maximize variance.

**Covariance Matrix**:
$$S = \frac{1}{n-1} \sum_{i=1}^{n}(x_i - \bar{x})(x_i - \bar{x})^T$$

**Eigenvalue Decomposition**:
Find eigenvalues $\lambda_1 \geq \lambda_2 \geq ... \geq \lambda_D$ and eigenvectors $v_1, v_2, ..., v_D$ of $S$.

**Projection**: For $d$ dimensions:
$$y_i = V_d^T (x_i - \bar{x})$$
where $V_d = [v_1, v_2, ..., v_d]$

#### Computational Complexity

- Covariance computation: $O(nD^2)$
- Eigenvalue decomposition: $O(D^3)$ for full decomposition
- For sparse data: $O(\min(n, D)^3)$

#### When to Use PCA

✅ **Appropriate when**:
- Data has linear structure
- Maximizing variance is the goal
- Need interpretable components
- Fast computation required
- Feature correlation exists

❌ **Not appropriate when**:
- Data has non-linear manifold structure
- Class separability is important (use LDA)
- Outliers significantly affect results

---

### 4.2 Linear Discriminant Analysis (LDA)

#### Mathematical Formulation

LDA finds projections that maximize class separability.

**Between-class scatter**:
$$S_B = \sum_{c} n_c (\mu_c - \mu)(\mu_c - \mu)^T$$

**Within-class scatter**:
$$S_W = \sum_{c} \sum_{x \in c} (x - \mu_c)(x - \mu_c)^T$$

**Generalized eigenvalue problem**:
$$S_B v = \lambda S_W v$$

**Projection**: $y = W^T x$ where $W$ contains top $d$ eigenvectors

#### Key Difference from PCA

- **PCA**: Unsupervised, maximizes variance
- **LDA**: Supervised, maximizes class separation

#### LDA for Dimensionality Reduction

The maximum number of components: $d \leq C-1$ where $C$ = number of classes

---

### 4.3 Multidimensional Scaling (MDS)

#### Objective

Preserve pairwise distances between all points.

**Stress Function**:
$$\min \sum_{i<j} (d_{ij} - \|y_i - y_j\|)^2$$

where $d_{ij}$ is the original distance and $\|y_i - y_j\|$ is the embedded distance.

#### Types of MDS

1. **Metric MDS**: Preserves original distances
2. **Non-metric MDS**: Preserves only the ranking of distances

#### Computational Complexity

- Distance matrix: $O(n^2 D)$
- Eigenvalue decomposition: $O(n^3)$
- Optimization: $O(k \cdot n^2)$ where k = iterations

---

### 4.4 ISOMAP (Isometric Mapping)

#### Algorithm Overview

ISOMAP approximates geodesic distances along the manifold using graph distances.

**Steps**:
1. **Construct k-NN graph**: Connect each point to its k nearest neighbors
2. **Compute geodesic distances**: Use Floyd-Warshall or Dijkstra's algorithm to compute shortest paths
3. **Apply MDS**: Apply metric MDS to the geodesic distance matrix

#### Mathematical Formulation

**Geodesic Distance Approximation**:
$$d_G(i, j) = \text{shortest path distance in k-NN graph}$$

**Double Centered Matrix**:
$$B = -\frac{1}{2} JD^{(2)}J$$
where $J = I - \frac{1}{n}\mathbf{1}\mathbf{1}^T$ and $D^{(2)}$ is squared distance matrix

**Eigenvalue Decomposition**:
$$B = V \Lambda V^T$$
Embeddings: $Y = V \Lambda^{1/2}$

#### Computational Complexity

- k-NN search: $O(n^2 D)$ or $O(n \log n \cdot D)$ with trees
- Shortest paths: $O(n^3)$ or $O(k n^2 \log n)$ with Johnson's algorithm
- MDS: $O(n^3)$

**Total**: $O(n^3)$ - computationally expensive for large datasets

---

### 4.5 Locally Linear Embedding (LLE)

#### Intuition

Each point can be reconstructed as a linear combination of its neighbors.

**Steps**:
1. Find k nearest neighbors for each point
2. Compute reconstruction weights that minimize:
$$\min \|x_i - \sum_{j \in N(i)} w_{ij} x_j\|^2$$
subject to $\sum_j w_{ij} = 1$
3. Compute low-dimensional embedding that uses the same weights:
$$\min \sum_i \|y_i - \sum_{j \in N(i)} w_{ij} y_j\|^2$$

#### Mathematical Formulation

**Weight Matrix Computation**:
$$w_{ij} = \frac{\sum_k C_{ik}^{-1}}{\sum_{l,m} C_{lm}^{-1}}$$
where $C_{ik} = (x_i - x_j) \cdot (x_i - x_k)$

**Embedding Optimization**:
$$\min Y^T M Y$$
subject to $Y^T Y = I$ and $Y^T \mathbf{1} = 0$

where $M = (I-W)^T(I-W)$

#### Computational Complexity

- k-NN search: $O(n^2 D)$
- Weight matrix: $O(k^3 n)$
- Eigenvalue decomposition: $O(n^3)$

---

### 4.6 t-Distributed Stochastic Neighbor Embedding (t-SNE)

#### Algorithm Overview

t-SNE models similarity using probability distributions and minimizes KL divergence.

**Similarity in high-dimensional space**:
$$p_{j|i} = \frac{\exp(-\|x_i - x_j\|^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-\|x_i - x_k\|^2 / 2\sigma_i^2)}$$
$$p_{ij} = \frac{p_{j|i} + p_{i|j}}{2n}$$

**Similarity in low-dimensional space**:
$$q_{ij} = \frac{(1 + \|y_i - y_j\|^2)^{-1}}{\sum_{k \neq l} (1 + \|y_k - y_l\|^2)^{-1}}$$

**Cost Function (KL Divergence)**:
$$KL(P || Q) = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$$

#### Key Parameters

- **Perplexity**: Balances local and global structure (typically 5-50)
- **Learning rate**: Usually 100-1000
- **Iterations**: Typically 1000-5000

#### Computational Complexity

- Pairwise distances: $O(n^2 D)$
- Gradient descent per iteration: $O(n^2)$
- **Total**: $O(n^2 \cdot \text{iterations})$

---

### 4.7 Spectral Methods

#### Graph-Based Approach

Spectral methods use the eigenvalue spectrum of graph Laplacian matrices.

**Steps**:
1. Construct similarity graph (k-NN or $\epsilon$-neighborhood)
2. Compute weight matrix $W$ (e.g., Gaussian kernel)
3. Compute graph Laplacian $L = D - W$ where $D$ is degree matrix
4. Solve generalized eigenvalue problem $Lv = \lambda Dv$
5. Use bottom k eigenvectors (excluding smallest) as embedding

#### Laplacian Eigenmaps

$$\min_Y \text{tr}(Y^T L Y) \quad \text{s.t.} \quad Y^T D Y = I$$

#### Computational Complexity

- Graph construction: $O(n^2 D)$
- Eigenvalue decomposition: $O(n^3)$

---

## 5. Comparison and Selection Guide

| Method | Linear | Supervised | Preserves | Complexity | Best For |
|--------|--------|------------|-----------|------------|----------|
| PCA | Yes | No | Global variance | O(D³) | Linear data, compression |
| LDA | Yes | Yes | Class separation | O(D³) | Classification |
| MDS | Yes/No | No | Global distances | O(n³) | Metric preservation |
| ISOMAP | No | No | Geodesic distances | O(n³) | Curved manifolds |
| LLE | No | No | Local geometry | O(n³) | Unwrapped manifolds |
| t-SNE | No | No | Local neighborhoods | O(n²·iter) | Visualization |
| Spectral | No | No | Graph structure | O(n³) | Clustering, manifolds |

### Decision Flowchart

```
Start
  ↓
Is data linear? → Yes → Use PCA
  ↓ No
Need class separation? → Yes → Use LDA
  ↓ No
Need visualization? → Yes → t-SNE (small n) or UMAP
  ↓ No
Large dataset? → Yes → Consider random projections or incremental PCA
  ↓ No
Has curved manifold? → Yes → ISOMAP or LLE
  ↓
End
```

---

## 6. Code Examples

### Example 1: PCA for Dimensionality Reduction

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Generate synthetic high-dimensional data
np.random.seed(42)
n_samples = 500
n_features = 50
n_informative = 5

# Create data with lower intrinsic dimensionality
X = np.random.randn(n_samples, n_features)
# Project to lower dimension and add noise
true_dim = np.random.randn(n_samples, n_informative)
loading = np.random.randn(n_informative, n_features)
X = true_dim @ loading + 0.1 * np.random.randn(n_samples, n_features)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=10)
X_pca = pca.fit_transform(X_scaled)

# Explained variance
explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

print("Explained Variance Ratio per Component:")
for i, var in enumerate(explained_variance):
    print(f"  PC{i+1}: {var:.4f} (Cumulative: {cumulative_variance[i]:.4f})")

# Find number of components for 95% variance
n_95 = np.argmax(cumulative_variance >= 0.95) + 1
print(f"\nComponents needed for 95% variance: {n_95}")

# Visualization
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.bar(range(1, 11), explained_variance, alpha=0.7, label='Individual')
plt.plot(range(1, 11), cumulative_variance, 'ro-', label='Cumulative')
plt.axhline(y=0.95, color='g', linestyle='--', label='95% threshold')
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('PCA Explained Variance')
plt.legend()

plt.subplot(1, 3, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.5, c=np.random.randn(n_samples))
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('2D Projection of Data')

plt.subplot(1, 3, 3)
plt.imshow(pca.components_[:5], aspect='auto', cmap='viridis')
plt.colorbar(label='Loading')
plt.xlabel('Original Features')
plt.ylabel('Principal Components')
plt.title('PCA Loadings (Top 5)')

plt.tight_layout()
plt.savefig('pca_example.png', dpi=150)
plt.show()
```

### Example 2: Manifold Learning with ISOMAP and t-SNE

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import ISOMAP, LocallyLinearEmbedding, TSNE
from sklearn.datasets import make_swiss_roll

# Generate Swiss Roll data
n_samples = 1500
X, color = make_swiss_roll(n_samples=n_samples, noise=0.1)

# Apply different manifold learning methods
# 1. ISOMAP
isomap = ISOMAP(n_neighbors=10, n_components=2)
X_isomap = isomap.fit_transform(X)

# 2. Locally Linear Embedding
lle = LocallyLinearEmbedding(n_neighbors=10, n_components=2)
X_lle = lle.fit_transform(X)

# 3. t-SNE
tsne = TSNE(n_components=2, perplexity=30, random_state=42, n_iter=1000)
X_tsne = tsne.fit_transform(X)

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Original 3D data
ax = fig.add_subplot(2, 2, 1, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap='viridis', s=10)
ax.set_title('Original Swiss Roll (3D)')
ax.view_init(10, 70)

# ISOMAP
axes[0, 1].scatter(X_isomap[:, 0], X_isomap[:, 1], c=color, cmap='viridis', s=10)
axes[0, 1].set_title('ISOMAP (2D) - Preserves Geodesic Distances')
axes[0, 1].set_xlabel('Component 1')
axes[0, 1].set_ylabel('Component 2')

# LLE
axes[1, 0].scatter(X_lle[:, 0], X_lle[:, 1], c=color, cmap='viridis', s=10)
axes[1, 0].set_title('Locally Linear Embedding (2D)')
axes[1, 0].set_xlabel('Component 1')
axes[1, 0].set_ylabel('Component 2')

# t-SNE
axes[1, 1].scatter(X_tsne[:, 0], X_tsne[:, 1], c=color, cmap='viridis', s=10)
axes[1, 1].set_title('t-SNE (2D) - Preserves Local Structure')
axes[1, 1].set_xlabel('Component 1')
axes[1, 1].set_ylabel('Component 2')

plt.tight_layout()
plt.savefig('manifold_learning.png', dpi=150)
plt.show()

# Print reconstruction errors
print(f"ISOMAP reconstruction error: {isomap.reconstruction_error():.6f}")
print(f"LLE reconstruction error: {lle.reconstruction_error():.6f}")
```

---

## 7. Exam Tips and Important Points

### For Delhi University Examination

1. **Understand the core difference**: Linear methods (PCA, LDA) project data onto linear subspaces, while manifold learning captures non-linear structure.

2. **Know when to use what**:
   - PCA for compression and feature extraction
   - LDA for supervised dimensionality reduction (classification)
   - ISOMAP for curved manifolds (geodesic distance preservation)
   - LLE when data can be reconstructed from neighbors
   - t-SNE for visualization (not downstream tasks)

3. **Mathematical formulations are important**: Be prepared to derive or explain:
   - PCA objective function and eigenvalue solution
   - LDA's Fisher criterion
   - MDS stress function
   - t-SNE KL divergence

4. **Computational complexity matters**: Know the scalability trade-offs for each method.

5. **Practical considerations**:
   - Always standardize/normalize before PCA
   - Choose appropriate perplexity for t-SNE (5-50)
   - ISOMAP and LLE are sensitive to k (number of neighbors)
   - t-SNE is stochastic—results vary across runs

### Common Exam Questions

1. Explain the curse of dimensionality and how dimensionality reduction addresses it.
2. Derive the solution for PCA using eigenvalue decomposition.
3. Compare PCA and LDA for dimensionality reduction.
4. Explain the manifold assumption in machine learning.
5. Describe the ISOMAP algorithm and its advantages over linear methods.
6. Discuss the computational complexity of various dimensionality reduction techniques.
7. When would you choose t-SNE over PCA? Justify your answer.
8. Explain the concept of geodesic distance in manifold learning.

---

## 8. Multiple Choice Questions (MCQs)

### Complete Set

**Question 1**: In PCA, the principal components are:
- A) Linear combinations of original features that maximize variance
- B) Linear combinations that maximize class separation
- C) Non-linear transformations of data
- D) Selected original features with highest variance

**Answer**: A) Linear combinations of original features that maximize variance

---

**Question 2**: Which method is best suited for visualization of high-dimensional data?
- A) PCA
- B) LDA
- C) t-SNE
- D) Factor Analysis

**Answer**: C) t-SNE

---

**Question 3**: LDA is different from PCA because:
- A) LDA is unsupervised
- B) LDA maximizes between-class variance relative to within-class variance
- C) LDA cannot be used for dimensionality reduction
- D) LDA requires more features than samples

**Answer**: B) LDA maximizes between-class variance relative to within-class variance

---

**Question 4**: In ISOMAP, geodesic distance is computed by:
- A) Euclidean distance in original space
- B) Shortest path in k-NN graph
- C) Mahalanobis distance
- D) Cosine similarity

**Answer**: B) Shortest path in k-NN graph

---

**Question 5**: The curse of dimensionality refers to:
- A) Too few features in the dataset
- B) Exponential growth in volume with increasing dimensions
- C) Loss of information during reduction
- D) Computational efficiency in high dimensions

**Answer**: B) Exponential growth in volume with increasing dimensions

---

**Question 6**: t-SNE uses which distribution in the low-dimensional space?
- A) Gaussian
- B) Student's t (heavy-tailed)
- C) Uniform
- D) Exponential

**Answer**: B) Student's t (heavy-tailed)

---

**Question 7**: LLE (Locally Linear Embedding) assumes that:
- A) Data lies on a global linear subspace
- B) Each point can be reconstructed from its k-nearest neighbors
- C) Data follows a Gaussian distribution
- D) Dimensions are statistically independent

**Answer**: B) Each point can be reconstructed from its k-nearest neighbors

---

**Question 8**: The maximum number of components in LDA for C classes is:
- A) C
- B) C - 1
- C) C + 1
- D) Unlimited

**Answer**: B) C - 1

---

**Question 9**: Which method is NOT suitable for large datasets (>10,000 samples)?
- A) Incremental PCA
- B) ISOMAP
- C) Random Projections
- D) t-SNE

**Answer**: B) ISOMAP (O(n³) complexity)

---

**Question 10**: Spectral methods use which matrix for embedding?
- A) Covariance matrix
- B) Graph Laplacian
- C) Correlation matrix
- D) Distance matrix

**Answer**: B) Graph Laplacian

---

## 9. Flashcards

### Key Terms and Definitions

| Term | Definition |
|------|------------|
| **Intrinsic Dimensionality** | The true, minimal number of dimensions needed to represent the data structure |
| **Manifold** | A topological space that locally resembles Euclidean space; the underlying structure of high-dimensional data |
| **Geodesic Distance** | The shortest path along the manifold surface between two points |
| **Curse of Dimensionality** | Phenomena that arise when analyzing data in high-dimensional spaces |
| **Eigenvalue Decomposition** | Factorization of a matrix into eigenvectors and eigenvalues |
| **Fisher Criterion** | LDA's objective: maximize (between-class variance) / (within-class variance) |
| **Perplexity** | Parameter in t-SNE representing effective number of neighbors |
| **Reconstruction Error** | Measure of how well the low-dimensional representation preserves original structure |
| **Kernel PCA** | Extension of PCA using kernel trick for non-linear dimensionality reduction |
| **Isomap** | Manifold learning method that preserves geodesic distances |

---

## 10. Key Takeaways

### Core Concepts

1. **Dimensionality reduction** transforms high-dimensional data into lower dimensions while preserving important structure.

2. **Linear methods** (PCA, LDA) assume data lies on or near a linear subspace:
   - **PCA**: Unsupervised, maximizes variance, O(D³) complexity
   - **LDA**: Supervised, maximizes class separation, maximum C-1 components

3. **Manifold learning** captures non-linear structure:
   - **ISOMAP**: Preserves geodesic distances using shortest path in k-NN graph
   - **LLE**: Preserves local reconstruction weights
   - **t-SNE**: Excellent for visualization, uses t-distribution in low-dimensional space

4. **Computational complexity** varies significantly:
   - Fast: PCA (O(D³)), Random Projections
   - Moderate: t-SNE (O(n² × iterations))
   - Slow: ISOMAP, LLE, Spectral (O(n³))

### Practical Guidelines

- **Start with PCA** for baseline and understanding data structure
- **Use t-SNE** for visualization of clusters (small to medium datasets)
- **Use ISOMAP/LLE** when you know data lies on a curved manifold
- **Use LDA** when class separability is important
- **Consider scalability**: For large datasets, use incremental PCA, random projections, or UMAP

### Delhi University Syllabus Alignment

This content covers:
- ✅ Linear Dimensionality Reduction (PCA, LDA)
- ✅ Non-linear Manifold Methods (ISOMAP, LLE, t-SNE)
- ✅ Mathematical formulations and derivations
- ✅ Computational complexity analysis
- ✅ Practical implementation with Python
- ✅ Comparison and selection criteria
- ✅ Examination preparation materials

---

## References for Further Study

1. Jolliffe, I. T. (2002). Principal Component Analysis. Springer.
2. Roweis, S. T., & Saul, L. K. (2000). Nonlinear Dimensionality Reduction by Locally Linear Embedding. Science.
3. Tenenbaum, J. B., et al. (2000). A Global Geometric Framework for Nonlinear Dimensionality Reduction. Science.
4. Van der Maaten, L., & Hinton, G. (2008). Visualizing Data using t-SNE. JMLR.
5. Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer.

---

*Study material prepared for MSc CS, Delhi University - July 2025*