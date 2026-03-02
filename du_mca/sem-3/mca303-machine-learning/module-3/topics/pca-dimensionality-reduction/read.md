# PCA Dimensionality Reduction

## Introduction
Principal Component Analysis (PCA) is a fundamental unsupervised linear transformation technique in machine learning for dimensionality reduction. It identifies directions of maximum variance in high-dimensional data and projects it onto a new subspace with fewer dimensions while retaining most information.

In the era of big data, PCA addresses the "curse of dimensionality" where high-dimensional datasets lead to increased computational costs and model overfitting. Its applications span facial recognition (Eigenfaces), gene expression analysis, financial risk modeling, and data compression. For DU MCA students, understanding PCA is crucial for efficient data preprocessing and feature engineering in real-world ML pipelines.

The mathematical foundation lies in eigenvalue decomposition of the covariance matrix. PCA achieves orthogonal transformation of correlated variables into principal components (PCs) - uncorrelated directions of maximum variance. The first PC captures the largest variance, with subsequent components orthogonal to previous ones.

## Key Concepts
1. **Variance and Covariance**: 
   - Variance measures data spread: Var(X) = E[(X - μ)²]
   - Covariance measures linear relationship between variables: Cov(X,Y) = E[(X-μ_x)(Y-μ_y)]

2. **Covariance Matrix**:
   - For n-dimensional data, compute n×n matrix Σ where Σ[i,j] = Cov(X_i,X_j)
   - Symmetric positive semi-definite matrix capturing feature relationships

3. **Eigen Decomposition**:
   - Solve Σv = λv where λ = eigenvalues, v = eigenvectors
   - Eigenvectors represent principal directions, eigenvalues indicate variance magnitude

4. **Dimensionality Reduction**:
   - Sort eigenvalues in descending order
   - Choose top-k eigenvectors capturing 95% cumulative variance
   - Project data: Y = XW where W is matrix of selected eigenvectors

5. **Whitening (Standardization)**:
   - Critical preprocessing step: Standardize data to μ=0, σ=1
   - Prevents features with large scales from dominating variance

## Examples

**Example 1: 2D to 1D Reduction**
Dataset: X = [[2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0]]

Steps:
1. Standardize data (μ=0, σ=1)
2. Compute covariance matrix:
   [[0.6166, 0.6154],
    [0.6154, 0.7166]]
3. Find eigenvalues (λ1=1.284, λ2=0.049) and eigenvectors:
   v1 = [0.6779, 0.7352]
4. Project to 1D using v1:
   Y = [-0.827, 1.777, -0.992, 0.274, 0.759]

**Example 2: Image Compression (MNIST Digits)**
1. Flatten 28×28 images to 784D vectors
2. Compute 784×784 covariance matrix
3. Select top 50 PCs capturing 90% variance
4. Reconstruct images: X_approx = YW^T
Reduces storage from 784 to 50 features with minimal quality loss

**Example 3: Iris Dataset (4D to 2D)**
1. Standardize sepal/petal measurements
2. Compute PCs:
   PC1 (73% variance): 0.521*sepal_len + 0.269*sepal_wid + 0.580*petal_len + 0.565*petal_wid
   PC2 (23% variance): -0.377*sepal_len + 0.923*sepal_wid + ... 
3. 2D plot reveals clear species clusters

## Exam Tips
1. Always mention data standardization before applying PCA
2. For covariance matrix calculations, remember division by (n-1) for unbiased estimate
3. Eigenvalues sum to total variance; use cumulative sum for component selection
4. PCA is sensitive to outliers - mention Robust PCA variants if asked
5. Difference from LDA: PCA is unsupervised (max variance), LDA is supervised (max class separation)
6. Practice manual eigenvalue calculations for 2×2 matrices
7. Know limitations: Loses interpretability, assumes linear relationships