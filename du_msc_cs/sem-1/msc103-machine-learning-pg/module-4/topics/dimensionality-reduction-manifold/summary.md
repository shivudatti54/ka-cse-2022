# Dimensionality Reduction & Manifold Learning

## Introduction

Dimensionality reduction transforms high-dimensional data into lower-dimensional representations while preserving essential structure. Manifold learning specifically exploits the assumption that high-dimensional data often lies on or near a lower-dimensional manifold—informally, a curved surface of lower intrinsic dimension embedded in higher-dimensional space.

---

## Key Concepts

### **Need for Dimensionality Reduction**
- **Curse of Dimensionality**: As dimensions increase, data becomes sparse; distances lose meaning; model performance degrades
- **Computational efficiency**: Fewer features reduce training time and memory requirements
- **Visualization**: Human interpretation requires 2D/3D representations
- **Noise reduction**: Eliminate irrelevant or redundant features

### **Linear Methods**

- **Principal Component Analysis (PCA)**
  - Projects data onto orthogonal axes (principal components) maximizing variance
  - Minimizes reconstruction error
  - Linear assumption—fails when manifold is non-linear

- **Linear Discriminant Analysis (LDA)**
  - Supervised; maximizes class separability
  - Not primarily a manifold technique

### **Manifold Learning Methods (Non-Linear)**

- **Locally Linear Embedding (LLE)**
  - Preserves local neighborhood relationships
  - Reconstructs each point from k-nearest neighbors
  - Unfolding Swiss Roll dataset effectively

- **Isomap**
  - Geodesic distances along manifold (approximated by graph distances)
  - Multi-Dimensional Scaling (MDS) on geodesic distances
  - Captures global structure

- **t-Distributed Stochastic Neighbor Embedding (t-SNE)**
  - Probabilistic approach; preserves local structure
  - Uses Student t-distribution for similarity in low-dim space
  - Best for visualization; not suitable for new data (no out-of-sample extension)

- **Uniform Manifold Approximation and Projection (UMAP)**
  - topological data analysis based
  - Faster than t-SNE; preserves both local and global structure
  - Supports out-of-sample extension

### **Key Assumptions**
- Data lies on or near a low-dimensional manifold
- Intrinsic dimension << observed dimension
- Local neighborhoods carry structural information

### **Applications**
- Image compression & face recognition (Eigenfaces)
- Gene expression analysis
- NLP (word embeddings)
- Sensor networks & IoT data

---

## Delhi University Syllabus Alignment

Covers: PCA, LDA, LLE, Isomap, t-SNE—commonly listed under "Dimensionality Reduction" and "Manifold Learning" units in DU MSc CS Machine Learning syllabus.

---

## Conclusion

Dimensionality reduction is essential for handling high-dimensional data. While linear methods like PCA are foundational, manifold learning techniques (LLE, Isomap, t-SNE, UMAP) excel at capturing non-linear structures. For exam preparation, understand when to apply each method based on data characteristics—linear vs. non-linear, supervised vs. unsupervised, and visualization vs. feature extraction needs.