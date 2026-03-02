# Principal Component Analysis (PCA) - Dimensionality Reduction

## Introduction

In the era of big data, machine learning algorithms often encounter datasets with hundreds or thousands of features. This high-dimensional data presents significant challenges: increased computational complexity, the curse of dimensionality, and the risk of overfitting. Principal Component Analysis (PCA) stands as one of the most fundamental and widely used techniques for dimensionality reduction in unsupervised machine learning.

PCA was originally developed by Karl Pearson in 1901 and independently by Harold Hotelling in the 1930s. It remains a cornerstone technique in data science, computer vision, finance, and bioinformatics. The core idea behind PCA is remarkably elegant: it transforms the original correlated features into a new set of uncorrelated variables called principal components, ordered by the amount of variance they explain in the data.

For University of Delhi students preparing for examinations, PCA represents a critical topic that bridges linear algebra, statistics, and machine learning. Understanding PCA not only helps in solving practical data science problems but also demonstrates how mathematical concepts like eigenvectors and eigenvalues find real-world applications. This technique is particularly relevant when dealing with image data, sensor data, and financial time series where feature correlations are prevalent.

## Key Concepts

### The Need for Dimensionality Reduction

Consider a dataset with 1000 features. While all features might contain some information, many are likely redundant or correlated. High-dimensional data suffers from the "curse of dimensionality," where data points become increasingly sparse, making pattern discovery difficult. PCA addresses this by identifying the directions (principal components) along which data varies the most and projecting the data onto these directions while retaining maximum information.

### Mathematical Foundation of PCA

**1. Centering the Data**

The first step in PCA is to center the data by subtracting the mean of each feature. If X is an n×p data matrix with n samples and p features, the centered data X_centered = X - μ, where μ is the mean vector of each column. This ensures that the data is distributed around the origin.

**2. Covariance Matrix**

The covariance matrix captures how features vary together. For centered data, it is computed as:
$$Σ = \frac{1}{n-1} X_{centered}^T X_{centered}$$

The covariance matrix is a p×p symmetric positive semi-definite matrix. Its diagonal elements represent variances of individual features, while off-diagonal elements represent covariances between feature pairs.

**3. Eigenvalue Decomposition**

The heart of PCA involves computing eigenvalues and eigenvectors of the covariance matrix. If λ₁, λ₂, ..., λₚ are eigenvalues (arranged in descending order) and v₁, v₂, ..., vₚ are corresponding eigenvectors, then:
$$Σ v_i = λ_i v_i$$

Eigenvectors (principal component directions) represent the axes of maximum variance, while eigenvalues indicate the magnitude of variance in those directions.

**4. Principal Components**

The k-th principal component is a linear combination of original features:
$$PC_k = v_k^T X = v_{k1}X_1 + v_{k2}X_2 + ... + v_{kp}X_p$$

Principal components are orthogonal to each other, meaning they capture independent information. The first principal component explains the maximum variance, the second explains the maximum remaining variance, and so on.

### Variance Explained and Component Selection

The proportion of variance explained by the k-th principal component is:
$$\text{Variance Explained}_k = \frac{λ_k}{\sum_{i=1}^{p} λ_i}$$

A common approach is to select components that explain 95% or 99% of the total variance. The scree plot, which displays eigenvalues against component numbers, helps visualize this threshold.

### Dimensionality Reduction Process

To reduce dimensions from p to k:
1. Select top k eigenvectors (based on k largest eigenvalues)
2. Form projection matrix W = [v₁, v₂, ..., vₖ]
3. Transform data: X_reduced = X_centered × W
4. For reconstruction (optional): X_reconstructed = X_reduced × W^T + μ

### Relationship with SVD

PCA is computationally equivalent to Singular Value Decomposition (SVD). If X = UΣV^T, then V's columns are eigenvectors of X^TX, and Σ²/(n-1) contains eigenvalues. SVD is often preferred in practice due to better numerical stability.

## Examples

### Example 1: Simple 2D Data Reduction

Given a 2D dataset with features X1 and X2:
X = [[2, 3], [4, 5], [6, 7], [8, 9]]

**Step 1: Compute Mean**
μ₁ = (2+4+6+8)/4 = 5
μ₂ = (3+5+7+9)/4 = 6

**Step 2: Center the Data**
X_centered = [[-3, -3], [-1, -1], [1, 1], [3, 3]]

**Step 3: Compute Covariance Matrix**
Since data is perfectly correlated (each point lies on line X2 = X1 + 1):
Σ = [[4, 4], [4, 4]] (simplified, using n instead of n-1)

**Step 4: Find Eigenvalues and Eigenvectors**
Solving |Σ - λI| = 0:
(4-λ)² - 16 = 0
λ² - 8λ = 0
λ(λ - 8) = 0
λ₁ = 8, λ₂ = 0

Eigenvectors:
For λ₁ = 8: (Σ - 8I)v = 0 → [-4, 4]v = 0 → v₁ = [1/√2, 1/√2]
For λ₂ = 0: v₂ = [1/√2, -1/√2]

**Step 5: Reduce to 1 Dimension**
Select v₁ = [0.707, 0.707]
Project: X_reduced = X_centered × v₁ = [-4.24, -1.41, 1.41, 4.24]

This single component captures 100% of variance (since λ₁/(λ₁+λ₂) = 8/8 = 1).

### Example 2: Iris Dataset Dimensionality Reduction

For the famous Iris dataset (150 samples, 4 features), suppose after PCA we get:
- PC1: explains 72.77% variance
- PC2: explains 23.03% variance
- PC3: explains 3.68% variance
- PC4: explains 0.52% variance

Using first two components captures 95.8% of total variance. This 4D → 2D reduction makes visualization possible while retaining most information.

### Example 3: Image Compression Application

Consider a 100×100 grayscale image (10,000 features). Applying PCA:
- With 50 components: retains ~90% variance, compression ratio = 10000/50 = 200:1
- With 100 components: retains ~95% variance, compression ratio = 100:1
- With 200 components: retains ~99% variance, compression ratio = 50:1

This demonstrates PCA's utility in image compression and face recognition (Eigenfaces).

## Exam Tips

1. **Remember the Step-by-Step Procedure**: Always center data first, then compute covariance matrix, find eigenvalues/eigenvectors, and project onto principal components.

2. **Interpretation of Eigenvalues**: Larger eigenvalues indicate directions of greater variance—these are your most important principal components.

3. **Orthogonality Property**: Principal components are always orthogonal (perpendicular) to each other, a key property that distinguishes them from other techniques.

4. **Variance Calculation**: Know how to calculate the percentage of variance explained: (eigenvalue of component / sum of all eigenvalues) × 100.

5. **When to Use PCA**: Know the applications—visualization, noise reduction, feature extraction, and avoiding overfitting in classification problems.

6. **Standardization vs Centering**: Remember that if features have different scales, standardization (mean=0, std=1) should be applied before PCA, not just centering.

7. **Limitation - Linearity Assumption**: PCA can only find linear relationships. For non-linear dimensionality reduction, consider t-SNE or UMAP (advanced topic, but good to know exists).

8. **Reconstruction Error**: The reconstruction error (original vs. back-projected data) increases as you use fewer components. This is minimized when retaining more variance.

9. **Scree Plot Usage**: In exams, you may be asked to suggest the optimal number of components—refer to the elbow point in a scree plot where the curve flattens.

10. **Python Implementation**: Be familiar with sklearn's PCA class: `from sklearn.decomposition import PCA`, `pca = PCA(n_components=2)`, `X_transformed = pca.fit_transform(X)`.