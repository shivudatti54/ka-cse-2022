# **Dimensionality Reduction – Principal Component Analysis**

## **Introduction**

Dimensionality reduction is a crucial step in data preprocessing, where we reduce the number of features or variables in a dataset while retaining the most important information. This technique is essential in various applications, such as image compression, data analysis, and machine learning. In this section, we will explore Principal Component Analysis (PCA), a widely used dimensionality reduction technique.

## **What is Principal Component Analysis (PCA)?**

PCA is a linear dimensionality reduction technique that transforms a set of correlated variables into a new set of uncorrelated variables, called principal components. The goal of PCA is to capture the most important features or patterns in the data, while ignoring the less important ones.

## **How does PCA work?**

The PCA algorithm works as follows:

1. **Standardization**: The dataset is standardized by subtracting the mean and dividing by the standard deviation for each feature.
2. **Covariance Matrix**: The covariance matrix is computed from the standardized data.
3. **Eigenvalue Decomposition**: The covariance matrix is decomposed into its eigenvalues and eigenvectors.
4. **Principal Components**: The eigenvectors corresponding to the largest eigenvalues are selected as the principal components.
5. **Transformation**: The original data is transformed into a new dataset using the principal components.

## **Key Concepts**

- **Variance**: The amount of spread or dispersion of a set of data.
- **Covariance**: A measure of how much two variables change together.
- **Eigenvalue**: A scalar value that represents the amount of variance explained by an eigenvector.
- **Eigenvector**: A vector that represents the direction of the maximum variance.

## **Mathematical Formulation**

Let X be the original dataset with n samples and p features. The covariance matrix Σ can be computed as:

Σ = (X - μ)T (X - μ) / (n - 1)

where μ is the mean vector and n is the number of samples.

The eigenvalue decomposition of Σ is:

Σ = UΛU^T

where U is the matrix of eigenvectors and Λ is the diagonal matrix of eigenvalues.

## **Example**

Suppose we have a dataset with 10 samples and 5 features, and we want to apply PCA to reduce the dimensionality to 2 features.

| Sample 1 | Sample 2 | ... | Sample 10 |
| --- | --- | ... | --- |
| 1 | 2 | ... | 10 |
| 3 | 4 | ... | 12 |
| ... | ... | ... | ... |

First, we standardize the data:

| Sample 1 | Sample 2 | ... | Sample 10 |
| --- | --- | ... | --- |
| 0 | 0 | ... | 0 |
| 1 | 1 | ... | 1 |
| ... | ... | ... | ... |

Next, we compute the covariance matrix:

Σ = [1.2 0.5 0.3 0.1 0.8]
[0.5 1.1 0.2 0.9 0.1]
[0.3 0.2 1.3 0.6 0.4]
[0.1 0.9 0.6 1.2 0.3]
[0.8 0.1 0.4 0.3 1.1]

The eigenvalue decomposition of Σ is:

Σ = UΛU^T

where U is the matrix of eigenvectors and Λ is the diagonal matrix of eigenvalues:

Λ = [2.3 0.2 0.1]
[0.2 1.8 0.1]
[0.1 0.1 1.3]

The principal components are the eigenvectors corresponding to the largest eigenvalues. In this case, the first two principal components are:

PC1 = [0.5 0.3 0.1]
PC2 = [0.3 0.2 0.9]

The original data is transformed into a new dataset using the principal components:

| Sample 1 | Sample 2 | ... | Sample 10 |
| --- | --- | ... | --- |
| 1.5 | 0.6 | ... | 1.1 |
| 1.3 | 0.5 | ... | 1.0 |
| ... | ... | ... | ... |

## **Advantages and Disadvantages**

Advantages:

- Reduces the dimensionality of the data
- Captures the most important features or patterns in the data
- Can be used for data visualization and feature selection

Disadvantages:

- Assumes linearity and normality of the data
- Can be sensitive to outliers and noise
- May not capture non-linear relationships between variables

## **Conclusion**

Principal Component Analysis is a widely used dimensionality reduction technique that transforms a set of correlated variables into a new set of uncorrelated variables. It captures the most important features or patterns in the data while ignoring the less important ones. However, it assumes linearity and normality of the data and can be sensitive to outliers and noise.
