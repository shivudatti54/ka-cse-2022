# Feature Engineering and Dimensionality Reduction Techniques

## **Introduction**

Feature engineering constitutes a fundamental pillar in the machine learning pipeline, encompassing the systematic process of transforming raw data into meaningful representations that enhance algorithmic learning. The discipline integrates domain expertise with statistical techniques to extract discriminative information from heterogeneous data sources. Dimensionality reduction, as a complementary paradigm, addresses the inherent challenges posed by high-dimensional data through systematic feature space transformation while preserving critical structural properties. This module examines the theoretical foundations, mathematical formulations, and practical considerations underlying contemporary feature engineering and dimensionality reduction methodologies, with particular emphasis on the formal derivations and optimization perspectives essential for rigorous understanding.

## **1. Feature Engineering Techniques**

### **1.1 Data Preprocessing and Cleaning**

Data quality significantly influences model performance, necessitating systematic preprocessing pipelines.

**Handling Missing Values**: The treatment of missing data requires careful consideration of the missingness mechanism. Mean imputation assumes missingness at random (MAR) and preserves variable means but distorts variance structures. Multiple imputation and expectation-maximization (EM) algorithms provide more robust estimates by accounting for uncertainty in missing value estimation. For categorical variables, mode imputation or the introduction of a separate "missing" category may be appropriate.

**Outlier Detection and Treatment**: Outliers arise from measurement errors, sampling anomalies, or genuine extreme observations. Statistical methods include z-score analysis (assuming normality) and the interquartile range (IQR) method. Robust techniques such as winsorization replace extreme values with percentiles, while isolation forests and DBSCAN provide algorithmic approaches for high-dimensional outlier detection.

### **1.2 Feature Selection Methods**

Feature selection enhances model interpretability, reduces computational complexity, and mitigates overfitting by eliminating irrelevant or redundant features.

**Filter Methods**: These techniques evaluate feature relevance independently of the learning algorithm. Pearson correlation identifies linear relationships, while Spearman correlation captures monotonic associations. Mutual information measures non-linear dependencies by quantifying the reduction in uncertainty about the target variable given feature knowledge:

$$I(X; Y) = \sum_{x \in X} \sum_{y \in Y} p(x, y) \log\left(\frac{p(x, y)}{p(x)p(y)}\right)$$

**Wrapper Methods**: Recursive Feature Elimination (RFE) employs backward selection, iteratively removing the least important features based on model performance. Embedded methods such as LASSO (Least Absolute Shrinkage and Selection Operator) perform feature selection during model training through L1 regularization:

$$\hat{\beta}_{LASSO} = \arg\min_\beta \sum_{i=1}^n (y_i - X_i\beta)^2 + \lambda \sum_{j=1}^p |\beta_j|$$

## **2. Dimensionality Reduction: Theoretical Foundations**

### **2.1 Principal Component Analysis (PCA)**

PCA represents a cornerstone technique for linear dimensionality reduction,transforming correlated variables into a set of uncorrelated principal components.

**Mathematical Formulation**: Given a data matrix $X \in \mathbb{R}^{n \times p}$ with $n$ samples and $p$ features, PCA seeks orthogonal directions maximizing variance. The optimization objective is formulated as:

$$\max_{\mathbf{w}} \mathbf{w}^T \Sigma \mathbf{w} \quad \text{subject to} \quad \mathbf{w}^T \mathbf{w} = 1$$

where $\Sigma = \frac{1}{n-1}X^TX$ denotes the sample covariance matrix.

**Solution via Eigenvalue Decomposition**: Applying Lagrangian multipliers yields the generalized eigenvalue problem $\Sigma \mathbf{w} = \lambda \mathbf{w}$. The eigenvectors of $\Sigma$ define the principal directions, with corresponding eigenvalues representing the variance explained along each direction. Ordering eigenvectors by descending eigenvalues yields the principal components capturing maximum variance.

**Variance Explained**: The proportion of total variance explained by the first $k$ components is:

$$\text{Variance Explained} = \frac{\sum_{i=1}^k \lambda_i}{\sum_{j=1}^p \lambda_j}$$

The scree plot facilitates component selection by identifying the elbow point where incremental variance explanation diminishes significantly.

**Computational Complexity**: Standard PCA requires $O(p^3)$ time for eigenvalue decomposition, limiting applicability to moderate-dimensional data. Stochastic PCA and incremental approaches provide scalable alternatives for large datasets.

### **2.2 Linear Discriminant Analysis (LDA)**

Unlike PCA (unsupervised), LDA incorporates class label information to find projections maximizing class separability.

**Fisher's Linear Discriminant**: LDA seeks projections maximizing the ratio of between-class variance to within-class variance:

$$J(\mathbf{w}) = \frac{\mathbf{w}^T S_B \mathbf{w}}{\mathbf{w}^T S_W \mathbf{w}}$$

where $S_B$ (between-class scatter) and $S_W$ (within-class scatter) are defined as:

$$S_B = \sum_{c=1}^C n_c (\mu_c - \mu)(\mu_c - \mu)^T$$
$$S_W = \sum_{c=1}^C \sum_{x_i \in c} (x_i - \mu_c)(x_i - \mu_c)^T$$

The optimal projection vectors correspond to the generalized eigenvectors solving $S_B \mathbf{w} = \lambda S_W \mathbf{w}$. For $C$ classes, LDA yields at most $C-1$ discriminant functions.

**Assumptions**: LDA assumes multivariate normality, equal class covariance matrices (homoscedasticity), and independence of features. Violations may necessitate regularized LDA or quadratic discriminant analysis (QDA).

### **2.3 t-Distributed Stochastic Neighbor Embedding (t-SNE)**

t-SNE enables non-linear dimensionality reduction for visualization, preserving local neighborhood structure.

**Probabilistic Formulation**: t-SNE models pairwise similarities in high-dimensional and low-dimensional spaces using Gaussian and t-distributions respectively. The high-dimensional similarity is:

$$p_{j|i} = \frac{\exp(-||x_i - x_j||^2 / 2\sigma_i^2)}{\sum_{k \neq i} \exp(-||x_i - x_k||^2 / 2\sigma_i^2)}$$

The low-dimensional embedding $y_i$ minimizes the Kullback-Leibler divergence:

$$KL(P || Q) = \sum_{i \neq j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$$

where $q_{ij} = \frac{(1 + ||y_i - y_j||^2)^{-1}}{\sum_{k \neq l} (1 + ||y_k - y_l||^2)^{-1}}$

**Perplexity**: This parameter balances local and global structure, roughly representing the effective number of neighbors considered. Typical values range from 5 to 50, with sensitivity analysis recommended.

### **2.4 Autoencoders**

Autoencoders learn compressed representations through neural network encoder-decoder architectures.

**Architecture**: The encoder maps input $x \in \mathbb{R}^p$ to latent representation $h = f(W^{(1)}x + b^{(1)})$, while the decoder reconstructs $\hat{x} = g(W^{(2)}h + b^{(2)})$. Training minimizes reconstruction error:

$$\mathcal{L} = \frac{1}{n} \sum_{i=1}^n ||x_i - \hat{x}_i||^2$$

**Variants**: Variational autoencoders (VAEs) impose probabilistic structure on the latent space, enabling generative modeling. Denoising autoencoders (DAEs) learn robust representations by reconstructing from corrupted inputs.

## **3. Comparative Analysis**

| Technique   | Linear/Non-linear | Supervised | Computational Complexity | Use Case                            |
| ----------- | ----------------- | ---------- | ------------------------ | ----------------------------------- |
| PCA         | Linear            | No         | $O(p^3)$                 | Compression, preprocessing          |
| LDA         | Linear            | Yes        | $O(p^3)$                 | Classification, feature extraction  |
| t-SNE       | Non-linear        | No         | $O(n^2 \log n)$          | Visualization, clustering           |
| Autoencoder | Non-linear        | No         | $O(n \cdot d \cdot e)$   | Feature learning, anomaly detection |

## **4. Practical Considerations**

**When to Use PCA**: PCA excels when data exhibits linear correlations and the primary objective is variance preservation or noise reduction. It assumes Gaussian-like distributions and is sensitive to scaling.

**When to Use LDA**: LDA is preferred for classification tasks where class separation is paramount. The technique is limited by its linear nature and assumption of equal class covariances.

**When to Use t-SNE**: t-SNE is optimal for exploratory visualization of high-dimensional data, particularly in clustering analysis. It is computationally intensive and non-deterministic.

**Curse of Dimensionality**: As dimensionality increases, data points become equidistant, compromising distance-based algorithms. Dimensionality reduction mitigates this phenomenon while preserving geometric structure.
