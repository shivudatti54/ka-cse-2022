# Nearest Centroid Classifier

## Introduction

The Nearest Centroid Classifier (NCC), also known as the Nearest Mean Classifier or Rocchio Classifier, represents a fundamental supervised learning algorithm in pattern recognition and machine learning. Unlike instance-based learners such as k-Nearest Neighbors that store the entire training dataset, the Nearest Centroid Classifier summarizes each class by computing the centroid (mean vector) of all training samples belonging to that class. During prediction, a new data point is assigned to the class whose centroid is closest to it, typically using Euclidean distance. This approach offers significant computational advantages, as it requires minimal storage for the model and provides fast classification time, making it particularly suitable for large-scale applications and scenarios where model interpretability is important.

The Nearest Centroid Classifier operates under the assumption that classes can be effectively separated by linear decision boundaries, which are essentially the perpendicular bisectors of the line segments connecting the centroids of different classes. This assumption holds reasonably well when the class distributions are roughly spherical with similar covariances. However, when classes have significantly different variances or non-spherical shapes, the classifier's performance may degrade. The algorithm has roots in the Rocchio method from information retrieval and has been successfully applied in various domains including document classification, medical diagnosis, and customer segmentation.

## Mathematical Formulation

### Centroid Computation

Given a training set with $N$ samples, each represented as a $d$-dimensional feature vector $\mathbf{x}_i \in \mathbb{R}^d$, and corresponding class labels $y_i \in \{1, 2, ..., K\}$ for $K$ classes, the centroid for class $c$ is calculated as the mean of all feature vectors belonging to that class. Let $\mathcal{X}_c = \{\mathbf{x}_1, \mathbf{x}_2, ..., \mathbf{x}_{n_c}\}$ represent the set of $n_c$ training samples in class $c$. The centroid $\boldsymbol{\mu}_c$ is computed as:

$$\boldsymbol{\mu}_c = \frac{1}{n_c} \sum_{\mathbf{x}_i \in \mathcal{X}_c} \mathbf{x}_i$$

This process results in one centroid per class, significantly compressing the training data into a compact representation. The centroid is a $d$-dimensional vector where each component represents the mean value of the corresponding feature across all samples in that class.

### Classification Rule

For a new test point $\mathbf{x} \in \mathbb{R}^d$, the Nearest Centroid Classifier assigns it to the class with the nearest centroid. Using Euclidean distance, the classification rule is:

$$\hat{y} = \arg\min_{c \in \{1, ..., K\}} d(\mathbf{x}, \boldsymbol{\mu}_c) = \arg\min_{c} \|\mathbf{x} - \boldsymbol{\mu}_c\|_2$$

where $\|\cdot\|_2$ denotes the Euclidean norm. The decision boundary between any two classes $i$ and $j$ consists of all points $\mathbf{x}$ such that $\|\mathbf{x} - \boldsymbol{\mu}_i\|_2 = \|\mathbf{x} - \boldsymbol{\mu}_j\|_2$.

## Formal Derivation of the Decision Boundary

### Two-Class Case

Consider a binary classification problem with two classes having centroids $\boldsymbol{\mu}_1$ and $\boldsymbol{\mu}_2$. The decision boundary consists of all points $\mathbf{x}$ equidistant from both centroids:

$$\|\mathbf{x} - \boldsymbol{\mu}_1\|^2 = \|\mathbf{x} - \boldsymbol{\mu}_2\|^2$$

Expanding both sides:

$$(\mathbf{x} - \boldsymbol{\mu}_1)^T(\mathbf{x} - \boldsymbol{\mu}_1) = (\mathbf{x} - \boldsymbol{\mu}_2)^T(\mathbf{x} - \boldsymbol{\mu}_2)$$

$$\mathbf{x}^T\mathbf{x} - 2\boldsymbol{\mu}_1^T\mathbf{x} + \boldsymbol{\mu}_1^T\boldsymbol{\mu}_1 = \mathbf{x}^T\mathbf{x} - 2\boldsymbol{\mu}_2^T\mathbf{x} + \boldsymbol{\mu}_2^T\boldsymbol{\mu}_2$$

Simplifying and canceling $\mathbf{x}^T\mathbf{x}$:

$$-2\boldsymbol{\mu}_1^T\mathbf{x} + \boldsymbol{\mu}_1^T\boldsymbol{\mu}_1 = -2\boldsymbol{\mu}_2^T\mathbf{x} + \boldsymbol{\mu}_2^T\boldsymbol{\mu}_2$$

$$2(\boldsymbol{\mu}_2 - \boldsymbol{\mu}_1)^T\mathbf{x} = \boldsymbol{\mu}_2^T\boldsymbol{\mu}_2 - \boldsymbol{\mu}_1^T\boldsymbol{\mu}_1$$

This is the equation of a hyperplane. Let $\mathbf{w} = 2(\boldsymbol{\mu}_2 - \boldsymbol{\mu}_1)$ and $b = \boldsymbol{\mu}_2^T\boldsymbol{\mu}_2 - \boldsymbol{\mu}_1^T\boldsymbol{\mu}_1$, then the decision boundary is:

$$\mathbf{w}^T\mathbf{x} + b = 0$$

The normal vector $\mathbf{w}$ points from $\boldsymbol{\mu}_1$ to $\boldsymbol{\mu}_2$, and the hyperplane is the perpendicular bisector of the line segment connecting the two centroids. This proves that the Nearest Centroid Classifier is a linear classifier.

### Geometric Interpretation

The decision hyperplane is orthogonal to the vector connecting the two centroids and passes through their midpoint. For any point $\mathbf{x}$ on the decision boundary:

$$\mathbf{x} = \frac{\boldsymbol{\mu}_1 + \boldsymbol{\mu}_2}{2} + \alpha \mathbf{w}$$

where $\mathbf{w}$ is orthogonal to $(\boldsymbol{\mu}_2 - \boldsymbol{\mu}_1)$.

## Distance Metrics

### Euclidean Distance

The Euclidean distance between a test point $\mathbf{x}$ and centroid $\boldsymbol{\mu}_c$ is:

$$d_E(\mathbf{x}, \boldsymbol{\mu}_c) = \|\mathbf{x} - \boldsymbol{\mu}_c\|_2 = \sqrt{\sum_{k=1}^{d}(x_k - \mu_{ck})^2}$$

This is the default and most commonly used metric, appropriate when features are on similar scales and class covariances are approximately equal.

### Mahalanobis Distance

When classes have different covariances, Euclidean distance may lead to poor classification. The Mahalanobis distance accounts for the covariance structure of each class:

$$d_M(\mathbf{x}, \boldsymbol{\mu}_c) = \sqrt{(\mathbf{x} - \boldsymbol{\mu}_c)^T \boldsymbol{\Sigma}_c^{-1} (\mathbf{x} - \boldsymbol{\mu}_c)}$$

where $\boldsymbol{\Sigma}_c$ is the covariance matrix of class $c$. This distance measures the number of standard deviations from the centroid, making it invariant to scaling and correlated features. When $\boldsymbol{\Sigma}_c = \sigma^2 \mathbf{I}$ (spherical covariance), the Mahalanobis distance reduces to Euclidean distance scaled by $\sigma$.

## Optimality Under Gaussian Assumptions

### Theorem: Bayes Optimality for Spherical Gaussians

When class distributions are spherical Gaussian with equal covariance matrices, the Nearest Centroid Classifier achieves Bayes optimal classification.

**Proof**: Let class $c$ follow a Gaussian distribution $\mathcal{N}(\boldsymbol{\mu}_c, \sigma^2\mathbf{I})$. The posterior probability using Bayes' theorem is:

$$P(y=c|\mathbf{x}) = \frac{P(\mathbf{x}|y=c)P(y=c)}{P(\mathbf{x})}$$

For Gaussian with spherical covariance:

$$P(\mathbf{x}|y=c) = \frac{1}{(2\pi\sigma^2)^{d/2}} \exp\left(-\frac{\|\mathbf{x} - \boldsymbol{\mu}_c\|^2}{2\sigma^2}\right)$$

Taking the log-posterior and maximizing:

$$\log P(y=c|\mathbf{x}) = \log P(y=c) - \frac{d}{2}\log(2\pi\sigma^2) - \frac{\|\mathbf{x} - \boldsymbol{\mu}_c\|^2}{2\sigma^2}$$

Ignoring constants, the optimal class is:

$$\hat{y} = \arg\max_c \left[\log P(y=c) - \frac{\|\mathbf{x} - \boldsymbol{\mu}_c\|^2}{2\sigma^2}\right]$$

When priors are equal ($P(y=c)$ constant), this simplifies to minimizing $\|\mathbf{x} - \boldsymbol{\mu}_c\|^2$, which is exactly the Nearest Centroid classification rule. Hence, NCC is Bayes optimal under spherical Gaussian assumptions with equal priors.

## Shrinkage and Regularization

### Shrunk Nearest Centroid Classifier

When the number of training samples per class is small relative to the feature dimensionality, the sample centroid may be unreliable due to high variance. The shrunk Nearest Centroid Classifier introduces a regularization parameter that pulls class means toward a global mean:

$$\boldsymbol{\mu}_c^{shrunk} = \frac{n_c}{n_c + \lambda}\boldsymbol{\mu}_c + \frac{\lambda}{n_c + \lambda}\boldsymbol{\mu}_{global}$$

where $\lambda \geq 0$ is the shrinkage parameter and $\boldsymbol{\mu}_{global} = \frac{1}{N}\sum_{i=1}^{N}\mathbf{x}_i$ is the global mean. When $\lambda = 0$, we get the standard centroid; as $\lambda \to \infty$, all centroids converge to the global mean.

### Bias-Variance Trade-off

The shrinkage estimator provides a bias-variance trade-off. The unshrunk centroid $\boldsymbol{\mu}_c$ has low bias but high variance when $n_c$ is small. The shrinkage estimator increases bias but reduces variance, particularly in high-dimensional spaces with limited samples. The optimal $\lambda$ is typically determined via cross-validation.

## Algorithmic Implementation

```
Algorithm: Nearest Centroid Classifier

Input: Training data {X, y}, test point x, shrinkage parameter λ
Output: Predicted class label

1. FOR each class c in unique classes:
2.     μ_c = mean(X[y == c])        // Compute centroid
3.     μ_global = mean(X)           // Compute global mean
4.     μ_c_shrunk = (n_c / (n_c + λ)) * μ_c + (λ / (n_c + λ)) * μ_global
5. END FOR

6. FOR each class c:
7.     d_c = EuclideanDistance(x, μ_c_shrunk)
8. END FOR

9. return argmin_c(d_c)
```

## Computational Complexity

- **Training**: $O(N \cdot d)$ to compute $K$ centroids from $N$ samples with $d$ features
- **Space**: $O(K \cdot d)$ to store $K$ centroids (vs. $O(N \cdot d)$ for k-NN)
- **Prediction**: $O(K \cdot d)$ to compute distances to $K$ centroids

The classifier is significantly more efficient than k-NN for large training sets, as it reduces storage requirements and provides constant-time prediction complexity independent of $N$.

## Limitations

1. **Assumption of Spherical Classes**: Performance degrades when classes have elongated or different covariance structures
2. **Sensitivity to Outliers**: Centroids are not robust to outliers; a single extreme point can significantly shift the centroid
3. **Equal Weighting of Features**: All features contribute equally to distance calculations unless weighted
4. **Linear Boundaries**: Cannot capture non-linear decision boundaries without feature transformation

## Worked Numerical Examples

### Example 1: Two-Dimensional Binary Classification

Consider a binary classification problem with two classes in a 2D feature space:

- Class A: A₁(1, 2), A₂(2, 3), A₃(1, 3)
- Class B: B₁(5, 5), B₂(6, 4), B₃(5, 6)

**Centroid Computation**:

- $\boldsymbol{\mu}_A = \left(\frac{1+2+1}{3}, \frac{2+3+3}{3}\right) = \left(\frac{4}{3}, \frac{8}{3}\right) \approx (1.33, 2.67)$
- $\boldsymbol{\mu}_B = \left(\frac{5+6+5}{3}, \frac{5+4+6}{3}\right) = \left(\frac{16}{3}, 5\right) \approx (5.33, 5.0)$

**Decision Boundary**: The boundary is the perpendicular bisector of the line from (1.33, 2.67) to (5.33, 5.0), passing through the midpoint ((1.33+5.33)/2, (2.67+5.0)/2) = (3.33, 3.835).

**Classification of test point x(3, 4)**:

- $d(\mathbf{x}, \boldsymbol{\mu}_A) = \sqrt{(3-1.33)^2 + (4-2.67)^2} = \sqrt{2.79 + 1.77} = \sqrt{4.56} \approx 2.14$
- $d(\mathbf{x}, \boldsymbol{\mu}_B) = \sqrt{(3-5.33)^2 + (4-5.0)^2} = \sqrt{5.43 + 1.0} = \sqrt{6.43} \approx 2.54$

Since $d(\mathbf{x}, \boldsymbol{\mu}_A) < d(\mathbf{x}, \boldsymbol{\mu}_B)$, the test point is classified as Class A.

### Example 2: Multiclass with Mahalanobis Distance

Given two classes with the following parameters:

- Class 1: $\boldsymbol{\mu}_1 = (2, 3)$, $\boldsymbol{\Sigma}_1 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$
- Class 2: $\boldsymbol{\mu}_2 = (5, 6)$, $\boldsymbol{\Sigma}_2 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$

For test point $\mathbf{x} = (3, 4)$:

**Euclidean distances**:

- $d_E(\mathbf{x}, \boldsymbol{\mu}_1) = \sqrt{1^2 + 1^2} = \sqrt{2} \approx 1.41$
- $d_E(\mathbf{x}, \boldsymbol{\mu}_2) = \sqrt{(-2)^2 + (-2)^2} = \sqrt{8} \approx 2.83$

**Mahalanobis distances**:

- $d_M(\mathbf{x}, \boldsymbol{\mu}_1) = \sqrt{(1, 1) \cdot \mathbf{I}^{-1} \cdot (1, 1)^T} = \sqrt{2} \approx 1.41$
- $d_M(\mathbf{x}, \boldsymbol{\mu}_2) = \sqrt{(1, 1) \cdot (2\mathbf{I})^{-1} \cdot (1, 1)^T} = \sqrt{0.5 + 0.5} = 1.0$

Using Mahalanobis distance, the test point is closer to Class 2 when accounting for its larger variance, demonstrating how covariance affects classification.

## Comparison with Related Classifiers

| Aspect                 | Nearest Centroid | k-Nearest Neighbors | Linear Discriminant Analysis |
| ---------------------- | ---------------- | ------------------- | ---------------------------- |
| Storage                | O(Kd)            | O(Nd)               | O(Kd)                        |
| Training               | O(Nd)            | O(1)                | O(Nd + Kd³)                  |
| Prediction             | O(Kd)            | O(Nd + KlogN)       | O(Kd)                        |
| Decision Boundary      | Linear           | Non-linear          | Linear                       |
| Robustness to Outliers | Low              | High                | Medium                       |

## Summary

The Nearest Centroid Classifier is a linear classifier that assigns test points to the class with the nearest centroid. It provides an excellent balance between computational efficiency and interpretability, making it suitable for baseline classification and large-scale applications. Under the assumption of spherical Gaussian distributions with equal covariances, it achieves Bayes optimal performance. The shrunk variant introduces regularization to handle high-dimensional data with limited samples. However, its assumption of spherical classes and linear decision boundaries limits its applicability to more complex classification problems.
