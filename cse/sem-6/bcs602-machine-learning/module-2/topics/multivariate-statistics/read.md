# Multivariate Statistics

## Introduction

Multivariate statistics provides the mathematical framework for analyzing data where each observation consists of measurements on multiple variables simultaneously. While univariate and bivariate analyses examine individual variables or pairwise relationships, multivariate techniques enable the simultaneous consideration of p ≥ 3 variables, capturing complex interdependencies that simpler methods cannot detect. These techniques constitute the foundational mathematics underlying numerous machine learning algorithms, including principal component analysis (PCA), linear discriminant analysis (LDA), Gaussian mixture models (GMM), and Gaussian processes.

## Mean Vector

For a dataset with p variables measured on n observations, the **mean vector** serves as the multivariate analogue of the univariate sample mean. Given observations $\mathbf{x}_1, \mathbf{x}_2, ..., \mathbf{x}_n$ where each $\mathbf{x}_i \in \mathbb{R}^p$, the sample mean vector is defined as:

$$\boldsymbol{\bar{x}} = \frac{1}{n}\sum_{i=1}^{n}\mathbf{x}_i$$

This yields a p-dimensional column vector:
$$\boldsymbol{\bar{x}} = [\bar{x}_1, \bar{x}_2, ..., \bar{x}_p]^T$$

where $\bar{x}_j = \frac{1}{n}\sum_{i=1}^{n}x_{ij}$ is the arithmetic mean of the j-th variable.

**Example**: For a dataset of n=100 observations with p=3 variables (height in cm, weight in kg, age in years):
$$\boldsymbol{\mu} = \begin{bmatrix} 170.5 \\ 68.3 \\ 25.1 \end{bmatrix}$$

The mean vector represents the centroid of the data cloud in p-dimensional space and serves as the location parameter in multivariate distributions.

## Covariance Matrix

The **covariance matrix** (or variance-covariance matrix) is the multivariate analogue of variance, capturing both the variability of individual variables and the pairwise relationships between variables.

### Definition

For a p-dimensional random vector $\mathbf{X} = [X_1, X_2, ..., X_p]^T$, the covariance matrix is defined as:

$$\boldsymbol{\Sigma} = \text{Cov}(\mathbf{X}) = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T]$$

where $\boldsymbol{\mu} = E[\mathbf{X}]$ is the mean vector. The (i,j)-th element is:

$$\Sigma_{ij} = \text{Cov}(X_i, X_j) = E[(X_i - \mu_i)(X_j - \mu_j)]$$

For sample data, the **sample covariance matrix** uses (n-1) in the denominator (Bessel's correction):

$$\mathbf{S} = \frac{1}{n-1}\sum_{i=1}^{n}(\mathbf{x}_i - \boldsymbol{\bar{x}})(\mathbf{x}_i - \boldsymbol{\bar{x}})^T$$

### Matrix Representation

$$\boldsymbol{\Sigma} = \begin{bmatrix} \text{Var}(X_1) & \text{Cov}(X_1,X_2) & \cdots & \text{Cov}(X_1,X_p) \\ \text{Cov}(X_2,X_1) & \text{Var}(X_2) & \cdots & \text{Cov}(X_2,X_p) \\ \vdots & \vdots & \ddots & \vdots \\ \text{Cov}(X_p,X_1) & \text{Cov}(X_p,X_2) & \cdots & \text{Var}(X_p) \end{bmatrix}$$

### Critical Properties

**Property 1: Symmetry**
$$\Sigma_{ij} = \Sigma_{ji} \implies \boldsymbol{\Sigma} = \boldsymbol{\Sigma}^T$$

_Proof_: $\text{Cov}(X_i, X_j) = E[(X_i - \mu_i)(X_j - \mu_j)] = E[(X_j - \mu_j)(X_i - \mu_i)] = \text{Cov}(X_j, X_i)$

**Property 2: Positive Semi-Definiteness**
The covariance matrix is always positive semi-definite: $\mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a} \geq 0$ for all $\mathbf{a} \in \mathbb{R}^p$.

_Proof_: Consider the variance of any linear combination $Y = \mathbf{a}^T\mathbf{X}$:
$$\text{Var}(Y) = \text{Var}(\mathbf{a}^T\mathbf{X}) = \mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a}$$
Since variance is always non-negative, $\mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a} \geq 0$. If $\mathbf{a} \neq \mathbf{0}$ yields $\mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a} > 0$, then $\boldsymbol{\Sigma}$ is positive definite.

**Property 3: Trace Property**
$\text{tr}(\boldsymbol{\Sigma}) = \sum_{i=1}^{p}\text{Var}(X_i)$ represents the total variance.

### Worked Numerical Example

Given bivariate data (X, Y) with n=4 observations:

| i   | X   | Y   |
| --- | --- | --- |
| 1   | 2   | 1   |
| 2   | 4   | 3   |
| 3   | 6   | 4   |
| 4   | 8   | 6   |

**Step 1**: Compute means
$$\bar{x} = \frac{2+4+6+8}{4} = 5, \quad \bar{y} = \frac{1+3+4+6}{4} = 3.5$$

**Step 2**: Compute deviations and cross-products

| i   | $x_i - \bar{x}$ | $y_i - \bar{y}$ | $(x_i-\bar{x})^2$ | $(y_i-\bar{y})^2$ | $(x_i-\bar{x})(y_i-\bar{y})$ |
| --- | --------------- | --------------- | ----------------- | ----------------- | ---------------------------- |
| 1   | -3              | -2.5            | 9                 | 6.25              | 7.5                          |
| 2   | -1              | -0.5            | 1                 | 0.25              | 0.5                          |
| 3   | 1               | 0.5             | 1                 | 0.25              | 0.5                          |
| 4   | 3               | 2.5             | 9                 | 6.25              | 7.5                          |

**Step 3**: Compute variances and covariance (sample, using n-1=3):
$$s_x^2 = \frac{20}{3} = 6.67, \quad s_y^2 = \frac{13}{3} = 4.33$$
$$s_{xy} = \frac{16}{3} = 5.33$$

**Step 4**: Covariance matrix:
$$\mathbf{S} = \begin{bmatrix} 6.67 & 5.33 \\ 5.33 & 4.33 \end{bmatrix}$$

### ML Applications

In machine learning, the covariance matrix is fundamental to:

- **Linear Discriminant Analysis (LDA)**: Computing within-class and between-class scatter matrices
- **Gaussian Naive Bayes**: Modeling feature dependencies
- **Principal Component Analysis (PCA)**: Eigenvalue decomposition of $\mathbf{S}$
- **Mahalanobis distance**: Used in anomaly detection and classification

## Correlation Matrix

The **correlation matrix** standardizes covariances to a [-1,1] scale, facilitating comparison across variables with different units.

### Definition

The Pearson correlation coefficient between $X_i$ and $X_j$ is:
$$r_{ij} = \frac{\text{Cov}(X_i, X_j)}{\sqrt{\text{Var}(X_i)\text{Var}(X_j)}} = \frac{\sigma_{ij}}{\sigma_i\sigma_j}$$

The correlation matrix is:
$$\mathbf{R} = \begin{bmatrix} 1 & r_{12} & \cdots & r_{1p} \\ r_{21} & 1 & \cdots & r_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ r_{p1} & r_{p2} & \cdots & 1 \end{bmatrix}$$

### Relationship to Covariance

$$\mathbf{R} = \mathbf{D}^{-1}\boldsymbol{\Sigma}\mathbf{D}^{-1}$$

where $\mathbf{D} = \text{diag}(\sigma_1, \sigma_2, ..., \sigma_p)$ is the standard deviation matrix.

### Properties

1. **Unit diagonal**: $r_{ii} = 1$ for all i
2. **Symmetry**: $\mathbf{R} = \mathbf{R}^T$
3. **Bounded entries**: $-1 \leq r_{ij} \leq 1$
4. **Positive semi-definite**: $\mathbf{R}$ has non-negative eigenvalues
5. **Multicollinearity detection**: $|r_{ij}| > 0.9$ indicates problematic correlation

## Mahalanobis Distance

The **Mahalanobis distance** provides a scale-invariant measure of distance from a point to a distribution, accounting for correlations between variables.

### Definition

For an observation vector $\mathbf{x} \in \mathbb{R}^p$, the Mahalanobis distance from the center $\boldsymbol{\mu}$ with covariance $\boldsymbol{\Sigma}$ is:

$$D_M(\mathbf{x}) = \sqrt{(\mathbf{x} - \boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})}$$

### Derivation from Multivariate Normal

Starting from the multivariate normal density:
$$f(\mathbf{x}) = \frac{1}{(2\pi)^{p/2}|\boldsymbol{\Sigma}|^{1/2}}\exp\left(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right)$$

The quadratic form $Q(\mathbf{x}) = (\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})$ is the **Mahalanobis squared distance**. Taking the square root yields $D_M(\mathbf{x})$.

### Comparison with Euclidean Distance

| Aspect                 | Euclidean Distance                                                    | Mahalanobis Distance                                                                          |
| ---------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Formula                | $\sqrt{(\mathbf{x}-\boldsymbol{\mu})^T(\mathbf{x}-\boldsymbol{\mu})}$ | $\sqrt{(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})}$ |
| Scale sensitivity      | Affected by variable scales                                           | Scale-invariant                                                                               |
| Correlation handling   | Ignores correlations                                                  | Accounts for correlations                                                                     |
| Equal-distance contour | Hyper-sphere                                                          | Hyper-ellipsoid                                                                               |
| ML applications        | K-means clustering                                                    | Anomaly detection, classification                                                             |

### Geometric Interpretation

The matrix $\boldsymbol{\Sigma}^{-1}$ "whitens" the transformation: applying $(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}$ stretches space along directions of high variance and compresses along directions of low variance. Thus, a point far along a high-variance direction is considered less unusual than an equal distance along a low-variance direction.

### Worked Example

For the bivariate data above with $\boldsymbol{\mu} = [5, 3.5]^T$ and $\boldsymbol{\Sigma} = \begin{bmatrix} 6.67 & 5.33 \\ 5.33 & 4.33 \end{bmatrix}$:

**Step 1**: Compute $\boldsymbol{\Sigma}^{-1}$

First, compute the determinant: $|\boldsymbol{\Sigma}| = (6.67)(4.33) - (5.33)^2 = 28.88 - 28.41 = 0.47$

Inverse:
$$\boldsymbol{\Sigma}^{-1} = \frac{1}{0.47}\begin{bmatrix} 4.33 & -5.33 \\ -5.33 & 6.67 \end{bmatrix} = \begin{bmatrix} 9.21 & -11.34 \\ -11.34 & 14.19 \end{bmatrix}$$

**Step 2**: For point $\mathbf{x} = [7, 5]^T$, compute deviation: $\mathbf{x} - \boldsymbol{\mu} = [2, 1.5]^T$

**Step 3**: Compute squared distance:
$$D_M^2 = \begin{bmatrix} 2 & 1.5 \end{bmatrix} \begin{bmatrix} 9.21 & -11.34 \\ -11.34 & 14.19 \end{bmatrix} \begin{bmatrix} 2 \\ 1.5 \end{bmatrix}$$
$$= \begin{bmatrix} 2 & 1.5 \end{bmatrix} \begin{bmatrix} 18.42 - 17.01 \\ -22.68 + 21.29 \end{bmatrix} = \begin{bmatrix} 2 & 1.5 \end{bmatrix} \begin{bmatrix} 1.41 \\ -1.39 \end{bmatrix}$$
$$= 2(1.41) + 1.5(-1.39) = 2.82 - 2.09 = 0.73$$

**Step 4**: $D_M = \sqrt{0.73} = 0.85$

For comparison, the Euclidean distance is $\sqrt{2^2 + 1.5^2} = \sqrt{6.25} = 2.5$. The Mahalanobis distance is smaller because the point lies along a direction of higher variance.

### ML Applications

- **Anomaly detection**: Points with $D_M > \sqrt{\chi^2_{p,0.975}}$ (97.5th percentile) are outliers
- **Classification**: Mahalanobis classifier assumes class-conditional multivariate normals
- **Clustering**: Modified K-means using Mahalanobis distance for elliptical clusters

## Eigenvalue Decomposition of Covariance Matrix

The spectral decomposition of the covariance matrix is fundamental to dimensionality reduction techniques.

### Theorem (Spectral Decomposition)

For a symmetric positive semi-definite matrix $\boldsymbol{\Sigma} \in \mathbb{R}^{p \times p}$, there exists an orthogonal matrix $\mathbf{Q} = [\mathbf{q}_1, \mathbf{q}_2, ..., \mathbf{q}_p]$ such that:

$$\boldsymbol{\Sigma} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^T = \sum_{i=1}^{p}\lambda_i\mathbf{q}_i\mathbf{q}_i^T$$

where $\boldsymbol{\Lambda} = \text{diag}(\lambda_1, \lambda_2, ..., \lambda_p)$ contains eigenvalues $\lambda_1 \geq \lambda_2 \geq ... \geq \lambda_p \geq 0$, and $\mathbf{q}_i$ are orthonormal eigenvectors ($\mathbf{q}_i^T\mathbf{q}_j = \delta_{ij}$).

### Properties

1. **Variance decomposition**: $\text{tr}(\boldsymbol{\Sigma}) = \sum_{i=1}^{p}\lambda_i$ (total variance)
2. **Variance explained**: The proportion of variance explained by the i-th component is $\lambda_i / \sum_{j=1}^{p}\lambda_j$
3. **Principal directions**: Eigenvectors $\mathbf{q}_i$ define the principal axes of the data ellipsoid

### ML Connection: PCA

PCA projects data onto the eigenvectors corresponding to the k largest eigenvalues, achieving dimensionality reduction while maximizing retained variance.

## Multivariate Normal Distribution

The **multivariate normal (MVN) distribution** is the most important distribution in multivariate statistics and machine learning.

### Definition

A p-dimensional random vector $\mathbf{X}$ follows a multivariate normal distribution $\mathbf{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ if its probability density function is:

$$f(\mathbf{x}) = \frac{1}{(2\pi)^{p/2}|\boldsymbol{\Sigma}|^{1/2}}\exp\left(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right)$$

where:

- $\boldsymbol{\mu} \in \mathbb{R}^p$ is the mean vector (location parameter)
- $\boldsymbol{\Sigma} \in \mathbb{R}^{p \times p}$ is the covariance matrix (positive definite)

### Key Properties

**Property 1: Linear combinations**
If $\mathbf{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ and $\mathbf{A} \in \mathbb{R}^{q \times p}$, then:
$$\mathbf{A}\mathbf{X} \sim \mathcal{N}_q(\mathbf{A}\boldsymbol{\mu}, \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^T)$$

**Property 2: Marginal distributions**
Any subset of variables follows a multivariate normal with the corresponding sub-covariance matrix.

**Property 3: Independence via diagonal covariance**
If $\boldsymbol{\Sigma}$ is diagonal, then the p variables are statistically independent.

**Property 4: Elliptical contours**
The set of points where $f(\mathbf{x}) = c$ forms an ellipsoid determined by $(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}) = k^2$.

### ML Applications

- **Gaussian Mixture Models (GMM)**: Clustering via mixture of MVN distributions
- **Gaussian Process Regression**: Prior over functions with MVN finite-dimensional distributions
- **Linear Gaussian models**: Kalman filtering, factor analysis
- **Regularization**: L2 regularization corresponds to MAP estimation with MVN prior on weights

## Principal Component Analysis (PCA)

PCA is a linear dimensionality reduction technique that transforms correlated variables into uncorrelated principal components ordered by variance.

### Mathematical Formulation

Given centered data $\mathbf{X} \in \mathbb{R}^{n \times p}$ (n observations, p variables), PCA finds orthonormal directions $\mathbf{w}_1, \mathbf{w}_2, ..., \mathbf{w}_p$ such that:

$$\mathbf{w}_i = \arg\max_{\mathbf{w}} \mathbf{w}^T\mathbf{S}\mathbf{w} \quad \text{subject to} \quad \mathbf{w}^T\mathbf{w} = 1, \mathbf{w}^T\mathbf{w}_j = 0 \forall j < i$$

where $\mathbf{S}$ is the sample covariance matrix.

### Solution via Eigenvalue Decomposition

The solution satisfies the eigenvalue equation:
$$\mathbf{S}\mathbf{w}_i = \lambda_i\mathbf{w}_i$$

The i-th principal component score for observation $\mathbf{x}_j$ is:
$$z_{ji} = \mathbf{x}_j^T\mathbf{w}_i$$

### Variance Explained

The total variance is $\text{tr}(\mathbf{S}) = \sum_{i=1}^{p}\lambda_i$. The proportion of variance explained by the first k components is:
$$\text{PVE}_k = \frac{\sum_{i=1}^{k}\lambda_i}{\sum_{i=1}^{p}\lambda_i}$$

Typically, we retain components such that $\text{PVE}_k \geq 0.95$ (95% variance retained).

### ML Applications

- **Dimensionality reduction**: Reduce feature space from p to k < p
- **Feature extraction**: Create uncorrelated features for downstream models
- **Visualization**: Project to 2D/3D for visualization
- **Noise reduction**: Retain only components with significant variance
- **Preprocessing**: Decorrelate features for algorithms sensitive to multicollinearity

## Hotelling's T² Test

Hotelling's T² is the multivariate generalization of Student's t-test for comparing multivariate means.

### Definition

For testing $H_0: \boldsymbol{\mu} = \boldsymbol{\mu}_0$ against $H_1: \boldsymbol{\mu} \neq \boldsymbol{\mu}_0$:

$$T^2 = n(\boldsymbol{\bar{x}} - \boldsymbol{\mu}_0)^T\mathbf{S}^{-1}(\boldsymbol{\bar{x}} - \boldsymbol{\mu}_0)$$

### Relationship to F-distribution

Under $H_0$, with n > p:
$$T^2 \cdot \frac{n-p}{p(n-1)} \sim F(p, n-p)$$

This enables hypothesis testing for multivariate means.

### ML Connection

Used in statistical process control, quality assurance, and change detection in ML model monitoring.
