# Dimensionality Reduction and Principal Component Analysis (PCA)

## Table of Contents

- [Dimensionality Reduction and Principal Component Analysis (PCA)](#dimensionality-reduction-and-principal-component-analysis-pca)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The Curse of Dimensionality](#the-curse-of-dimensionality)
  - [Principal Component Analysis (PCA) - Mathematical Foundation](#principal-component-analysis-pca---mathematical-foundation)
  - [Steps in PCA](#steps-in-pca)
  - [Variance Explained](#variance-explained)
  - [Difference Between PCA and Factor Analysis](#difference-between-pca-and-factor-analysis)
- [Examples](#examples)
  - [Example 1: PCA on 2D Data](#example-1-pca-on-2d-data)
  - [Example 2: Selecting Number of Components](#example-2-selecting-number-of-components)
  - [Example 3: PCA for Image Compression](#example-3-pca-for-image-compression)
- [Exam Tips](#exam-tips)

## Introduction

In modern data science and machine learning applications, we often encounter datasets with hundreds or thousands of features (dimensions). While having rich feature information seems advantageous, it frequently leads to computational challenges, overfitting, and difficulty in visualizing data. Dimensionality reduction techniques address these problems by transforming high-dimensional data into a lower-dimensional representation while preserving essential information.

Principal Component Analysis (PCA) is the most widely used unsupervised dimensionality reduction technique in linear algebra and machine learning. Developed by Karl Pearson in 1901, PCA transforms correlated variables into a set of uncorrelated variables called principal components. These components are ordered by the amount of variance they explain, with the first principal component capturing the maximum variance in the data.

The importance of PCA in the university's Linear Algebra curriculum cannot be overstated. It serves as a practical application of eigenvalues, eigenvectors, covariance matrices, and matrix decomposition concepts. Understanding PCA enables students to handle real-world data analysis problems in fields ranging from image processing to financial modeling.

## Key Concepts

### The Curse of Dimensionality

As the number of dimensions increases, the volume of the feature space expands exponentially. This creates several problems:

1. **Data Sparsity**: Data points become increasingly isolated in high-dimensional spaces, making statistical inference unreliable.
2. **Computational Complexity**: Algorithms become slower and require more memory as dimensions increase.
3. **Overfitting**: Models may learn noise in high-dimensional data rather than meaningful patterns.
4. **Visualization**: Humans cannot visualize data beyond 3 dimensions effectively.

Dimensionality reduction mitigates these issues by reducing the number of features while retaining most of the important information.

### Principal Component Analysis (PCA) - Mathematical Foundation

PCA is a linear transformation technique that finds new axes (principal components) oriented along the directions of maximum variance in the data. The key mathematical concepts include:

**Eigenvalues and Eigenvectors**: For a square matrix A, if there exists a non-zero vector v and scalar λ such that Av = λv, then λ is an eigenvalue and v is the corresponding eigenvector. In PCA, the eigenvectors of the covariance matrix represent the directions of maximum variance (principal component axes), and eigenvalues represent the magnitude of variance in those directions.

**Covariance Matrix**: The covariance matrix summarizes the relationships between all pairs of variables. For a dataset with n features, the covariance matrix is an n×n symmetric matrix where element (i,j) represents the covariance between features i and j. The diagonal elements represent variances of individual features.

**Variance and Covariance**:

- Variance measures how much a single variable varies: Var(x) = Σ(xi - x̄)²/(n-1)
- Covariance measures how two variables vary together: Cov(x,y) = Σ(xi - x̄)(yi - ȳ)/(n-1)

### Steps in PCA

**Step 1: Standardize the Data**
Given a dataset with m samples and n features, first standardize each feature to have zero mean and unit variance. This ensures all features contribute equally to the analysis.

Z = (X - μ) / σ

where μ is the mean and σ is the standard deviation.

**Step 2: Compute the Covariance Matrix**
Calculate the n×n covariance matrix:
Σ = (1/(m-1)) × ZTZ

**Step 3: Find Eigenvalues and Eigenvectors**
Compute the eigenvalues and corresponding eigenvectors of the covariance matrix. The eigenvectors (principal component directions) form an orthogonal basis.

**Step 4: Sort and Select Components**
Sort eigenvalues in descending order. The eigenvector corresponding to the largest eigenvalue is the first principal component (PC1), and so on. Select the top k eigenvectors to retain k principal components.

**Step 5: Transform the Data**
Project the standardized data onto the selected eigenvectors:
Y = Z × Wk

where Wk is the n×k matrix of selected eigenvectors, and Y is the m×k transformed dataset.

### Variance Explained

The proportion of variance explained by each principal component is calculated as:

Variance explained by PCi = λi / Σλj

Cumulative variance explained by first k components = Σ(λi for i=1 to k) / Σλj

Typically, we select enough components to explain 80-95% of the total variance.

### Difference Between PCA and Factor Analysis

While both are dimensionality reduction techniques, they differ in their objectives:

- **PCA**: Focuses on explaining maximum variance with minimum number of components; the components are linear combinations of observed variables.
- **Factor Analysis**: Attempts to identify underlying latent factors that explain correlations between variables; more suitable when we believe hidden factors exist.

## Examples

### Example 1: PCA on 2D Data

Consider a 2D dataset with 5 points:
X = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]

**Step 1: Standardize**
Mean of column 1: (2+3+4+5+6)/5 = 4
Mean of column 2: (3+4+5+6+7)/5 = 5
Standardized: Z = [[-1.265, -1.265], [-0.632, -0.632], [0, 0], [0.632, 0.632], [1.265, 1.265]]

**Step 2: Covariance Matrix**
Since the data is perfectly correlated (y = x + 1), the covariance matrix will have equal off-diagonal elements.

**Step 3 & 4: Eigenvalues and Eigenvectors**
For perfectly correlated 2D data, one eigenvalue will be large (representing variance along the line) and one will be near zero (perpendicular to the line).

**Step 5: Transformation**
Since one eigenvalue is near zero, we can reduce from 2D to 1D by keeping only the first principal component.

### Example 2: Selecting Number of Components

Given eigenvalues: λ1 = 4.2, λ2 = 0.8, λ3 = 0.3, λ4 = 0.1

Total variance = 4.2 + 0.8 + 0.3 + 0.1 = 5.4

Variance explained by each component:

- PC1: 4.2/5.4 = 77.78%
- PC2: 0.8/5.4 = 14.81%
- PC3: 0.3/5.4 = 5.56%
- PC4: 0.1/5.4 = 1.85%

Cumulative variance:

- 1 component: 77.78%
- 2 components: 92.59%
- 3 components: 98.15%
- 4 components: 100%

If we want 90% variance explained, we need 2 principal components.

### Example 3: PCA for Image Compression

A 100×100 grayscale image can be treated as a 10,000-dimensional dataset (each pixel is a dimension). Using PCA:

- Original dimensions: 10,000
- If top 50 components explain 95% variance, we can represent the image using only 50 dimensions
- Compression ratio: 10,000/50 = 200:1 in terms of dimensions
- Storage reduction: instead of 10,000 values, we store 50 eigenvalues + 50 eigenvectors × 100 + 50 coefficients per image

## Exam Tips

1. **Remember the PCA objective**: PCA finds directions of maximum variance to reduce dimensionality while preserving maximum information.

2. **Eigenvalue-eigenvector relationship**: In PCA, larger eigenvalues indicate more important principal components. The eigenvector shows the direction, eigenvalue shows the variance magnitude.

3. **Standardization is crucial**: Always standardize data before PCA; otherwise, features with larger scales will dominate the analysis.

4. **Variance calculation**: Remember that variance explained by each PC = eigenvalue of that PC / sum of all eigenvalues.

5. **Orthogonality property**: Principal components are always orthogonal (perpendicular) to each other, making them linearly independent.

6. **PCA is unsupervised**: Unlike LDA (Linear Discriminant Analysis), PCA doesn't use class labels—it's an unsupervised technique.

7. **Cumulative variance rule**: For most applications, retain principal components that explain 80-95% of total variance.

8. **Matrix operations**: Be familiar with computing Z-score, covariance matrix (ZTZ/(n-1)), and matrix multiplication for transformation.

9. **Interpret first PC**: The first principal component represents the direction in which the data varies the most.

10. **Applications knowledge**: Know real-world applications like face recognition (Eigenfaces), image compression, and data visualization.
