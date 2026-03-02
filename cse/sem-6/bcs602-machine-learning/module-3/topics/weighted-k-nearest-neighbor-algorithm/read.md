# Weighted K-Nearest-Neighbor (WKNN) Algorithm

## 1. Introduction and Theoretical Foundations

The K-Nearest Neighbors (KNN) algorithm represents a fundamental instance-based learning approach in supervised machine learning, utilized extensively for both classification and regression tasks. The underlying principle asserts that similar instances tend to cluster in proximity within the feature space. However, the standard KNN algorithm employs uniform weighting, wherein each of the K neighbors contributes equally to the prediction regardless of their distances from the query point. This uniformity introduces a significant limitation when the nearest neighbors exhibit substantially higher similarity than distant ones.

The **Weighted K-Nearest-Neighbor (WKNN)** algorithm addresses this limitation by introducing a distance-dependent weighting mechanism. The fundamental hypothesis underlying WKNN states that the influence of a neighbor should be inversely proportional to its distance from the query instance, thereby assigning greater predictive authority to more similar instances.

## 2. Mathematical Formulation

### 2.1 Distance Metrics

Let the feature space be defined as $\mathbb{R}^d$, where $d$ represents the number of features. For a query instance $\mathbf{x}_q \in \mathbb{R}^d$ and a training instance $\mathbf{x}_i \in \mathbb{R}^d$, the commonly employed distance metrics include:

**Euclidean Distance:**
$$d(\mathbf{x}_q, \mathbf{x}_i) = \sqrt{\sum_{j=1}^{d}(x_{qj} - x_{ij})^2} = \|\mathbf{x}_q - \mathbf{x}_i\|_2$$

**Manhattan Distance:**
$$d(\mathbf{x}_q, \mathbf{x}_i) = \sum_{j=1}^{d}|x_{qj} - x_{ij}| = \|\mathbf{x}_q - \mathbf{x}_i\|_1$$

**Minkowski Distance (Generalized):**
$$d(\mathbf{x}_q, \mathbf{x}_i) = \left(\sum_{j=1}^{d}|x_{qj} - x_{ij}|^p\right)^{1/p}$$

### 2.2 Weighting Functions

The weight assigned to the $i$-th neighbor is computed as a function of distance, denoted as $w_i = f(d_i)$. Several weighting schemes exist in literature:

**Inverse Distance Weighting:**
$$w_i = \frac{1}{d_i^p}, \quad p \in \mathbb{N}$$

When $p = 2$, this becomes the popular inverse-square weighting: $w_i = \frac{1}{d_i^2}$.

**Gaussian Kernel Weighting:**
$$w_i = \exp\left(-\frac{d_i^2}{2\sigma^2}\right)$$

where $\sigma$ represents the bandwidth parameter controlling the kernel width.

**Tricube Weighting:**
$$w_i = \left(1 - \left(\frac{d_i}{d_K}\right)^3\right)^3$$

where $d_K$ denotes the distance to the $K$-th nearest neighbor, ensuring $w_i \in [0, 1]$.

### 2.3 Theoretical Justification: Bias-Variance Analysis

The superiority of distance-weighted voting over uniform voting can be demonstrated through bias-variance decomposition. Let $\hat{f}(\mathbf{x})$ denote the KNN predictor and $f(\mathbf{x})$ denote the true underlying function. The expected prediction error at query point $\mathbf{x}_q$ is:

$$E[(Y - \hat{f}(\mathbf{x}_q))^2] = \text{Var}(\hat{f}) + [\text{Bias}(\hat{f})]^2 + \text{Irreducible Error}$$

For uniform weighting, all neighbors contribute equally, resulting in higher variance when neighbors at varying distances are included. Distance weighting reduces variance by concentrating probability mass on nearby neighbors. Formally, under inverse-distance weighting with $p=2$, the effective neighborhood size decreases, thereby reducing variance at the cost of potentially increased bias—a classic bias-variance trade-off.

## 3. WKNN Algorithm for Classification

**Input:** Training set $D = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$, query point $\mathbf{x}_q$, parameters $K$ and power parameter $p$

**Output:** Predicted class $\hat{y}$

**Algorithm:**

```
1. FOR each training instance x_i in D:
2.     Compute d_i = distance(x_q, x_i)
3. END FOR
4. Sort distances in ascending order
5. Select K nearest neighbors: N_K = { (x_i, y_i, d_i) | i = 1,...,K }
6. FOR each neighbor (x_i, y_i, d_i) in N_K:
7.     Compute weight w_i = 1 / (d_i^p)  [or use Gaussian/Tricube]
8.     If y_i == c, then accumulated_weight[c] += w_i
9. END FOR
10. Compute predicted class: ŷ = argmax_c accumulated_weight[c]
11. RETURN ŷ
```

## 4. WKNN Algorithm for Regression

For continuous target variables, the prediction is computed as the weighted average:

$$\hat{y} = \frac{\sum_{i=1}^{K} w_i \cdot y_i}{\sum_{i=1}^{K} w_i} = \frac{\sum_{i=1}^{K} \frac{y_i}{d_i^p}}{\sum_{i=1}^{K} \frac{1}{d_i^p}}$$

This formulation ensures that the predicted value lies within the range of observed $y$ values and gives higher influence to closer neighbors.

## 5. Computational Complexity Analysis

| Operation                   | Time Complexity                                                 | Space Complexity             |
| --------------------------- | --------------------------------------------------------------- | ---------------------------- |
| Distance Computation        | $O(N \cdot d)$                                                  | $O(N)$ for storing distances |
| Finding K Nearest Neighbors | $O(N \log N)$ with sorting, $O(N + K)$ with selection algorithm | $O(K)$                       |
| Weight Computation          | $O(K)$                                                          | $O(C)$ for class accumulator |
| **Total**                   | $O(N \cdot d + N \log N)$                                       | $O(N)$                       |

Compared to standard KNN, WKNN incurs minimal additional computational overhead—approximately $O(K)$ extra operations for weight computation and weighted summation. The dominant factor remains distance computation, which is identical to standard KNN.

## 6. Important Considerations

### 6.1 Feature Scaling Requirement

Distance-based algorithms are highly sensitive to feature scales. Features with larger magnitudes dominate the distance calculation, rendering features with smaller scales effectively irrelevant. Therefore, **feature normalization** (e.g., z-score standardization or min-max scaling) is mandatory prior to applying WKNN.

### 6.2 Curse of Dimensionality

In high-dimensional spaces ($d \gg$), the distance between any query point and its nearest neighbors approaches the distance to farthest neighbors, effectively eliminating the locality assumption. This phenomenon, known as the **curse of dimensionality**, significantly degrades WKNN performance. Dimensionality reduction techniques (PCA, t-SNE) or feature selection methods should be employed when $d$ is large.

### 6.3 Selection of Parameters

- **K:** Smaller values increase sensitivity to noise; larger values provide smoother decision boundaries but may include dissimilar neighbors.
- **Power Parameter (p):** Higher values (e.g., p=2 or p=3) sharply decrease the influence of distant neighbors, while p=1 provides linear decay.

## 7. Numerical Problem

**Problem:** Given the following training data for a binary classification problem with features $X_1$ and $X_2$:

| Instance | $X_1$ | $X_2$ | Class |
| -------- | ----- | ----- | ----- |
| A        | 1.0   | 2.0   | +1    |
| B        | 2.0   | 1.0   | +1    |
| C        | 4.0   | 4.0   | -1    |
| D        | 5.0   | 5.0   | -1    |
| E        | 6.0   | 4.0   | -1    |

For query point $\mathbf{x}_q = (3.0, 3.0)$ using Euclidean distance and $K=3$ with inverse-square weighting ($p=2$), determine the predicted class.

**Solution:**

1. Distances: $d(A)=\sqrt{5}\approx2.236$, $d(B)=\sqrt{5}\approx2.236$, $d(C)=\sqrt{2}\approx1.414$, $d(D)=\sqrt{8}\approx2.828$, $d(E)=\sqrt{10}\approx3.162$
2. Three nearest neighbors: C (-1, d=1.414), A (+1, d=2.236), B (+1, d=2.236)
3. Weights: $w_C = 1/(1.414)^2 = 0.5$, $w_A = 1/(2.236)^2 \approx 0.2$, $w_B \approx 0.2$
4. Weighted sum: Class +1: 0.4, Class -1: 0.5
5. **Prediction: Class -1**

## 8. Summary

The Weighted K-Nearest-Neighbor algorithm extends standard KNN by incorporating distance-based influence, assigning higher weights to closer neighbors. This modification enhances prediction accuracy, mitigates voting ties, and provides a confidence measure through weighted sums. Key parameters include the choice of $K$, power parameter $p$, distance metric, and weighting function. WKNN finds extensive applications in recommendation systems, pattern recognition, and forecasting, though practitioners must address feature scaling and high-dimensionality challenges for optimal performance.
