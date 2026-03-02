# K-Nearest Neighbor Learning

## 1. Introduction and Theoretical Foundations

K-Nearest Neighbors (KNN) is a fundamental **instance-based learning** or **lazy learning** algorithm used for classification and regression tasks. Unlike eager learning algorithms that construct a general model during training, KNN defers all computation until query time, storing the entire training dataset and performing computations locally when a new instance is presented.

### 1.1 Formal Definition

Given a training set $\mathcal{T} = \{(\mathbf{x}_i, y_i)\}_{i=1}^{n}$ where $\mathbf{x}_i \in \mathbb{R}^d$ and $y_i \in \mathcal{Y}$ (for classification, $\mathcal{Y}$ is a finite set of classes; for regression, $\mathcal{Y} \subseteq \mathbb{R}$), the KNN classifier predicts the label of a query point $\mathbf{x}_q$ as follows:

For classification:
$$\hat{y}(\mathbf{x}_q) = \text{mode}\{y_i : \mathbf{x}_i \in \mathcal{N}_K(\mathbf{x}_q)\}$$

For regression:
$$\hat{y}(\mathbf{x}_q) = \frac{1}{K}\sum_{\mathbf{x}_i \in \mathcal{N}_K(\mathbf{x}_q)} y_i$$

where $\mathcal{N}_K(\mathbf{x}_q)$ denotes the set of $K$ nearest neighbors of $\mathbf{x}_q$ in the training data.

### 1.2 Why KNN Works: Theoretical Justification

The theoretical foundation of KNN rests on the **Bayes optimal classifier** concept. The Bayes error rate represents the minimum achievable error rate when we have complete knowledge of the underlying probability distribution $P(\mathbf{x}, y)$:

$$f^*(\mathbf{x}) = \text{argmax}_{c} P(y=c|\mathbf{x})$$

**Theorem (KNN Consistency)**: Under mild regularity conditions (finite variance, continuous probability distributions), as $n \to \infty$ with $K \to \infty$ such that $K/n \to 0$, the KNN classifier is asymptotically consistent, meaning its error rate converges to the Bayes error rate.

**Proof Sketch**: The KNN estimator can be expressed as:
$$P(\hat{y}=c|\mathbf{x}_q) = \frac{1}{K}\sum_{i=1}^{n} I(y_i = c) \cdot I(\mathbf{x}_i \in \mathcal{N}_K(\mathbf{x}_q))$$

As $n \to \infty$, the neighborhood shrinks (volume $v_K \to 0$) but still contains enough points ($K \to \infty$). By the law of large numbers and properties of kernel density estimation, this converges to $P(y=c|\mathbf{x}_q)$. $\square$

## 2. The KNN Algorithm

### 2.1 Algorithm Steps

```
TRAINING PHASE:
===============
Input: Training set D = {(\mathbf{x}_1, y_1), ..., (\mathbf{x}_n, y_n)}
Output: Stored training data

Algorithm:
    Store all (\mathbf{x}_i, y_i) in memory
    No explicit model building

PREDICTION PHASE:
=================
Input: Query point \mathbf{x}_q, integer K
Output: Predicted label \hat{y}

Algorithm:
    for each training point \mathbf{x}_i in stored data:
        Compute d(\mathbf{x}_i, \mathbf{x}_q) using selected metric

    Select K points with smallest distances → \mathcal{N}_K(\mathbf{x}_q)

    if Classification:
        \hat{y} = majority vote of {y_i : \mathbf{x}_i \in \mathcal{N}_K(\mathbf{x}_q)}
    if Regression:
        \hat{y} = mean of {y_i : \mathbf{x}_i \in \mathcal{N}_K(\mathbf{x}_q)}

    return \hat{y}
```

### 2.2 Computational Complexity Analysis

- **Training Phase**: $O(1)$ — simply stores the data
- **Prediction Phase**: $O(ndK)$ where $n$ = number of training samples, $d$ = dimensionality, $K$ = number of neighbors
  - Computing distances: $O(nd)$
  - Finding K nearest neighbors (using efficient data structures like KD-trees or ball trees): $O(n \log n)$ average case, $O(nd)$ with proper indexing
- **Space Complexity**: $O(nd)$ to store the training data

## 3. Distance Metrics

The choice of distance metric fundamentally affects the notion of "nearness" and thus the decision boundary.

### 3.1 Mathematical Definitions

**Euclidean Distance** (L2 norm):
$$d_E(\mathbf{p}, \mathbf{q}) = \sqrt{\sum_{i=1}^{d}(q_i - p_i)^2} = \|\mathbf{p} - \mathbf{q}\|_2$$

**Manhattan Distance** (L1 norm):
$$d_M(\mathbf{p}, \mathbf{q}) = \sum_{i=1}^{d}|q_i - p_i| = \|\mathbf{p} - \mathbf{q}\|_1$$

**Minkowski Distance** (Lp norm generalization):
$$d_P(\mathbf{p}, \mathbf{q}) = \left(\sum_{i=1}^{d}|q_i - p_i|^P\right)^{1/P} = \|\mathbf{p} - \mathbf{q}\|_P$$

- $P=1$: Manhattan distance
- $P=2$: Euclidean distance
- $P \to \infty$: Chebyshev distance (maximum coordinate difference)

**Hamming Distance** (for categorical/binary data):
$$d_H(\mathbf{p}, \mathbf{q}) = \sum_{i=1}^{d} \mathbb{1}(p_i \neq q_i)$$

### 3.2 Comparison Table

| Metric    | Formula                                                                | Optimal Use Case                  | Properties                                |
| --------- | ---------------------------------------------------------------------- | --------------------------------- | ----------------------------------------- |
| Euclidean | $\sqrt{\sum(q_i-p_i)^2}$                                               | Low-dim, continuous data          | Sensitive to outliers, rotation invariant |
| Manhattan | $\sum\|q_i-p_i\|$                                                      | High-dimensional data, grid paths | Less sensitive to outliers                |
| Minkowski | $(\sum\|q_i-p_i\|^p)^{1/p}$                                            | Generalized metric selection      | Flexible parameter $p$                    |
| Hamming   | $\sum\mathbb{1}(p_i \neq q_i)$                                         | Categorical/binary features       | Counts mismatches                         |
| Cosine    | $1 - \frac{\mathbf{p} \cdot \mathbf{q}}{\|\mathbf{p}\|\|\mathbf{q}\|}$ | Text, high-dim sparse data        | Angle-based similarity                    |

## 4. The Parameter K: Bias-Variance Analysis

### 4.1 Effect on Model Complexity

The parameter $K$ controls the bias-variance trade-off:

- **Small K** (e.g., $K=1$):
  - Low bias, high variance
  - Complex, jagged decision boundary
  - Sensitive to noise and outliers
  - Risk of overfitting

- **Large K** (e.g., $K=n$):
  - High bias, low variance
  - Smooth decision boundary (approaches prior probability)
  - Risk of underfitting

### 4.2 Bias-Variance Decomposition

For regression, we can formally analyze the expected prediction error:

$$E[(\hat{y} - y)^2] = \text{Bias}^2(\hat{y}) + \text{Var}(\hat{y}) + \sigma^2$$

where $\sigma^2$ is the irreducible error. As $K$ increases:

- Bias increases (neighborhoods become more homogeneous to the prior)
- Variance decreases (averaging over more points reduces fluctuation)

### 4.3 Selecting Optimal K

**Cross-Validation Method**:

1. Split data into $k$ folds
2. For each fold, train on $k-1$ folds, validate on 1 fold
3. Select $K$ that minimizes validation error

**Rule of Thumb**: $K \approx \sqrt{n}$ is a common starting point, but this must be validated empirically.

**Odd K for Classification**: Use odd values of $K$ to avoid ties in majority voting.

## 5. Weighted KNN

### 5.1 Mathematical Formulation

In weighted KNN, closer neighbors contribute more to the prediction:

$$\hat{y}(\mathbf{x}_q) = \frac{\sum_{i \in \mathcal{N}_K(\mathbf{x}_q)} w_i \cdot y_i}{\sum_{i \in \mathcal{N}_K(\mathbf{x}_q)} w_i}$$

where weights are typically inverse distance:
$$w_i = \frac{1}{d(\mathbf{x}_i, \mathbf{x}_q)^\alpha}, \quad \alpha \geq 0$$

- $\alpha = 0$: Equal weights (standard KNN)
- $\alpha = 1$: Inverse distance weighting
- $\alpha = 2$: Inverse squared distance weighting

### 5.2 Why Weighting Improves Performance

Weighting by inverse distance addresses the issue of non-uniform data density. In sparse regions, neighbors are more informative; in dense regions, we need more neighbors to establish local structure. Distance weighting naturally adapts to this.

## 6. Curse of Dimensionality

### 6.1 The Problem

In high-dimensional spaces, the Euclidean distance between any two points tends to become similar—a phenomenon known as the **curse of dimensionality**. This undermines the fundamental assumption of KNN that nearby points have similar labels.

**Mathematical Intuition**: For $n$ points uniformly distributed in a $d$-dimensional unit hypercube, the expected distance to the $k$-th nearest neighbor scales as:
$$E[d_k] \approx \left(\frac{k}{n}\right)^{1/d}$$

As $d$ increases, this distance approaches a constant, making differentiation between neighbors difficult.

### 6.2 Mitigation Strategies

1. **Dimensionality Reduction**: PCA, LDA, or feature selection before KNN
2. **Feature Scaling**: Normalize/standardize features to prevent dominance
3. **Intrinsic Dimensionality**: Work with intrinsically low-dimensional data when possible
4. **适当选择K**: Larger $K$ can help average out noise in high dimensions

## 7. Feature Scaling Requirement

Since KNN uses distance metrics, features must be on comparable scales. Without scaling, features with larger ranges dominate the distance calculation.

**Min-Max Normalization**:
$$x'_i = \frac{x_i - x_{\min}}{x_{\max} - x_{\min}}$$

**Z-Score Standardization**:
$$x'_i = \frac{x_i - \mu_i}{\sigma_i}$$

## 8. Nearest Centroid Classifier

A simpler variant that compares a query point to class centroids rather than all training points:

$$\text{centroid}_c = \frac{1}{|\mathcal{C}_c|}\sum_{\mathbf{x}_i \in \mathcal{C}_c} \mathbf{x}_i$$

**Computational Complexity**: $O(nd + Ccd)$ where $C$ is number of classes (for centroid computation + $C$ distance calculations)

**Trade-off**: Much faster prediction but assumes spherical class distributions, often less accurate than KNN.

## 9. Practical Considerations

### 9.1 Handling Ties in Voting

- Use odd $K$
- Implement distance-weighted voting
- Random tie-breaking (not recommended for consistency)
- Priority to closer neighbor

### 9.2 Outlier Sensitivity

- Use distance weighting
- Outlier detection as preprocessing
- Larger $K$ to mitigate
