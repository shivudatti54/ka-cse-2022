# Module 3: Similarity-based Learning

## 1. Introduction and Theoretical Foundations

Similarity-based Learning constitutes a fundamental paradigm within machine learning, falling under the broader category of **Instance-based Learning** (IBL). Unlike model-based approaches such as Decision Trees, Support Vector Machines, or Neural Networks that construct an explicit generalized function from training data, similarity-based methods employ a radically different philosophy: they defer all computation to the prediction phase by storing the entire training dataset as the "model" itself.

**Definition (Instance-based Learning):** A learning algorithm that generalizes beyond the training data only when a new query instance is presented, using direct comparison with stored training instances rather than constructing an explicit predictive model.

The theoretical foundation of similarity-based learning rests upon the **local smoothness assumption** or **continuity assumption**, which posits that the target function exhibits gradual variation in the feature space. Formally, if two points $x_i$ and $x_j$ are close in the feature space $\mathcal{X} \subseteq \mathbb{R}^d$, their corresponding outputs $y_i$ and $y_j$ should also be close in the output space $\mathcal{Y}$. This assumption enables interpolation-based predictions using neighboring instances.

### 1.1 Formal Framework

Let $(\mathcal{X}, d)$ denote a **metric space** where $\mathcal{X} \subseteq \mathbb{R}^d$ represents the $d$-dimensional feature space and $d: \mathcal{X} \times \mathcal{X} \rightarrow \mathbb{R}^+$ is a distance metric satisfying the metric axioms:

1. **Non-negativity:** $d(x, y) \geq 0$ for all $x, y \in \mathcal{X}$
2. **Identity of Indiscernibles:** $d(x, y) = 0$ if and only if $x = y$
3. **Symmetry:** $d(x, y) = d(y, x)$ for all $x, y \in \mathcal{X}$
4. **Triangle Inequality:** $d(x, z) \leq d(x, y) + d(y, z)$ for all $x, y, z \in \mathcal{X}$

Given a training set $D = \{(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)\}$ where $x_i \in \mathcal{X}$ and $y_i \in \mathcal{Y}$, the learning algorithm stores $D$ and, upon receiving a query point $x_q$, produces a prediction $\hat{y}_q$ based on the labels $y_i$ of the $k$ nearest neighbors of $x_q$ in $D$.

## 2. The K-Nearest Neighbors (K-NN) Algorithm

The **K-Nearest Neighbors (K-NN)** algorithm stands as the quintessential similarity-based learning method, applicable to both classification and regression tasks. Its conceptual simplicity masks significant theoretical depth and practical complexity.

### 2.1 Algorithm Specification

**Algorithm: K-Nearest Neighbors (K-NN)**

```
Input: Training set D = {(x_i, y_i)}_{i=1}^n, query point x_q, integer k
Output: Prediction ŷ_q

1. For each training instance (x_i, y_i) ∈ D, compute distance d(x_q, x_i)
2. Identify the set N_k(x_q) ⊆ D containing the k points with smallest distances
3. For classification: ŷ_q = argmax_{c} Σ_{x_i ∈ N_k(x_q)} I(y_i = c)
   For regression: ŷ_q = (1/k) Σ_{x_i ∈ N_k(x_q)} y_i
4. Return ŷ_q
```

### 2.2 Mathematical Formulation

**Classification (Majority Voting):**
Given a query point $x_q$ and its $k$ nearest neighbors $N_k(x_q) = \{x_{(1)}, x_{(2)}, \ldots, x_{(k)}\}$, the predicted class $\hat{y}_q$ is obtained through:

$$\hat{y}_q = \underset{c \in \mathcal{C}}{\text{argmax}} \left| \{i : y_i = c \land x_i \in N_k(x_q)\} \right|$$

where $\mathcal{C}$ denotes the set of possible classes. For equiprobable ties when $k$ is even, conventional practice employs tie-breaking strategies such as selecting the class with minimum distance sum or using a smaller $k$.

**Regression (Mean/Median Estimation):**
$$\hat{y}_q = \frac{1}{k} \sum_{i: x_i \in N_k(x_q)} y_i$$

The median variant provides robustness to outliers:
$$\hat{y}_q = \text{median}\{y_i : x_i \in N_k(x_q)\}$$

### 2.3 Distance Metrics

The choice of distance metric fundamentally shapes the neighbor relationships and consequently the predictions. Let $x = (x_1, x_2, \ldots, x_d)$ and $q = (q_1, q_2, \ldots, q_d)$ represent two $d$-dimensional points.

**Euclidean Distance ($L_2$ norm):**
$$d_E(x, q) = \sqrt{\sum_{j=1}^{d} (x_j - q_j)^2} = \|x - q\|_2$$

**Manhattan Distance ($L_1$ norm):**
$$d_M(x, q) = \sum_{j=1}^{d} |x_j - q_j| = \|x - q\|_1$$

**Minkowski Distance ($L_p$ norm):**
$$d_p(x, q) = \left( \sum_{j=1}^{d} |x_j - q_j|^p \right)^{1/p} = \|x - q\|_p$$

Note that $p=1$ yields Manhattan distance and $p=2$ yields Euclidean distance. As $p \rightarrow \infty$, we obtain the Chebyshev distance: $d_\infty(x, q) = \max_j |x_j - q_j|$.

**Cosine Similarity (for directional data):**
$$s(x, q) = \frac{x \cdot q}{\|x\| \|q\|} = \frac{\sum_{j=1}^{d} x_j q_j}{\sqrt{\sum_{j=1}^{d} x_j^2} \sqrt{\sum_{j=1}^{d} q_j^2}}$$

Converted to distance: $d_{cos}(x, q) = 1 - s(x, q)$

**Hamming Distance (categorical/binary features):**
$$d_H(x, q) = \sum_{j=1}^{d} \mathbb{I}(x_j \neq q_j)$$

where $\mathbb{I}$ denotes the indicator function.

### 2.4 Computational Complexity Analysis

**Time Complexity:**

- **Training Phase:** $O(1)$ — the algorithm merely stores data (hence "lazy learning")
- **Prediction Phase:** $O(nd + k)$ for naive implementation
  - Computing distances: $O(nd)$ where $n$ is training size and $d$ is dimensionality
  - Finding k-smallest elements: $O(n)$ using partial sorting (or $O(n \log n)$ for full sort)
  - Aggregation: $O(k)$

For large $n$, this becomes computationally prohibitive, motivating data structures like **KD-trees** and **Ball trees** that enable nearest neighbor search in $O(\log n)$ average time for low-dimensional data ($d \leq 20$), though degradation occurs in high dimensions.

**Space Complexity:** $O(nd)$ for storing the training dataset.

## 3. Critical Considerations in K-NN

### 3.1 Choice of K: Bias-Variance Trade-off

The parameter $k$ controls the complexity of the model, directly affecting the bias-variance trade-off:

**Small $k$ (e.g., $k=1$):**

- **Low bias:** The decision boundary can be highly irregular, approximating complex decision surfaces
- **High variance:** Predictions are highly sensitive to the specific neighbors selected; noise in training data significantly impacts predictions
- **Overfitting risk:** The model memorizes training data rather than learning generalizable patterns
- As $k \rightarrow 1$, the algorithm approaches the **1-NN classifier**, which achieves the asymptotic error rate of the **Bayes optimal classifier** under certain conditions (Cover & Hart, 1967)

**Large $k$:**

- **High bias:** The decision boundary becomes smoother, potentially failing to capture fine-grained patterns
- **Low variance:** Predictions are more stable as they aggregate over more neighbors
- **Underfitting risk:** Excessive smoothing may ignore important local structure
- As $k \rightarrow n$, the classifier converges to the **prior probability** (majority class)

**Theorem (Consistency):** Under mild regularity conditions (e.g., $k \to \infty$ and $k/n \to 0$ as $n \to \infty$), the K-NN classifier is **consistent**, meaning its error rate converges to the Bayes optimal error rate.

### 3.2 The Curse of Dimensionality

The **curse of dimensionality** severely impacts distance-based methods in high-dimensional spaces. As dimensionality $d$ increases, the following phenomena occur:

1. **Distance Concentration:** For independently distributed points in $[0,1]^d$, the ratio between the maximum and minimum distances to a query point approaches 1:
   $$\lim_{d \to \infty} \frac{\max_i d(x_q, x_i)}{\min_i d(x_q, x_i)} = 1$$

This renders the concept of "nearest neighbor" meaningless as all points become approximately equidistant.

2. **Empty Space Phenomenon:** In high dimensions, most of the volume of a hypercube concentrates near its boundaries. The probability that a random point falls within distance $\epsilon$ of the origin (a "local" neighborhood) decreases exponentially: $P(\|x\| \leq \epsilon) = \epsilon^d$.

**Mitigation Strategies:**

- **Dimensionality Reduction:** PCA, t-SNE, UMAP
- **Feature Selection:** Remove irrelevant features that contribute noise to distance calculations
- **Intrinsic Dimensionality:** Many real-world datasets have lower intrinsic dimensionality embedded in higher-dimensional spaces
- **Distance Metric Learning:** Learn task-specific distance metrics (e.g., Mahalanobis distance)

### 3.3 Feature Scaling and Normalization

Features with different scales fundamentally distort distance calculations. Consider a dataset with "salary" (range: 0-100,000) and "age" (range: 0-100). A unit change in salary contributes minimally to Euclidean distance while age changes have disproportionate influence.

**Z-Score Standardization:**
$$x_j' = \frac{x_j - \mu_j}{\sigma_j}$$

where $\mu_j$ and $\sigma_j$ are the mean and standard deviation of feature $j$ computed from training data.

**Min-Max Scaling:**
$$x_j' = \frac{x_j - \min_j}{\max_j - \min_j}$$

This maps features to the $[0, 1]$ interval.

**Critical Note:** All transformations must be learned from training data and applied consistently to test data to prevent data leakage.

### 3.4 Weighted K-NN

**Distance-Weighted Voting** assigns weights to neighbors inversely proportional to their distances:

$$\hat{y}_q = \arg\max_{c \in \mathcal{C}} \sum_{x_i \in N_k(x_q)} w_i \cdot \mathbb{I}(y_i = c)$$

where $w_i = \frac{1}{d(x_q, x_i)^2}$ or $w_i = \exp(-\lambda d(x_q, x_i))$ for some $\lambda > 0$.

**For Regression:**
$$\hat{y}_q = \frac{\sum_{i: x_i \in N_k(x_q)} w_i \cdot y_i}{\sum_{i: x_i \in N_k(x_q)} w_i}$$

This formulation naturally reduces to standard K-NN when all weights equal $1/k$.

## 4. Advanced Data Structures for Efficient Retrieval

### 4.1 KD-Tree

A **KD-tree** (k-dimensional tree) is a binary space-partitioning data structure that enables efficient nearest neighbor queries in low-to-moderate dimensional spaces.

**Construction:** Recursively partition the data by alternating dimensions (or using variance-based split selection) at the median, creating a balanced tree in $O(n \log n)$ time.

**Query Complexity:** Average case $O(\log n)$ for $d \leq 20$; worst case $O(n)$ for pathological distributions or high dimensions.

**Limitations:** KD-trees become inefficient when $d > 20$ due to the "curse of dimensionality," where the tree structure provides minimal pruning capability during search.

### 4.2 Approximate Nearest Neighbor (ANN) Methods

For massive datasets where exact nearest neighbors are computationally infeasible, **Approximate Nearest Neighbor** algorithms sacrifice precision for speed:

- **Locality-Sensitive Hashing (LSH):** Hashes similar points to the same bucket with high probability
- **Hierarchical Navigable Small World (HNSW):** Graph-based approach with logarithmic query time
- **FAISS (Facebook AI Similarity Search):** Industrial-scale implementation

## 5. Summary

| Aspect                  | Description                                                                                                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Core Principle**      | Prediction based on similarity to stored training instances; "birds of a feather flock together"                                                                             |
| **Primary Algorithm**   | K-Nearest Neighbors (K-NN) for classification and regression                                                                                                                 |
| **Learner Type**        | Lazy Learner (Instance-based); no explicit training phase; computation deferred to query time                                                                                |
| **Mathematical Basis**  | Metric space theory; local smoothness assumption; convergence to Bayes optimal under consistency conditions                                                                  |
| **Distance Metrics**    | Euclidean ($L_2$), Manhattan ($L_1$), Minkowski ($L_p$), Cosine, Hamming                                                                                                     |
| **Key Hyperparameters** | $k$ (number of neighbors), distance metric, weighting scheme                                                                                                                 |
| **Complexity**          | Training: $O(1)$; Prediction: $O(nd)$ naive, $O(\log n)$ with KD-tree (low $d$)                                                                                              |
| **Advantages**          | Simple, interpretable; no training phase; naturally handles multi-class problems; no parametric assumptions; adapts locally to data                                          |
| **Limitations**         | Computationally expensive at prediction time; sensitive to irrelevant features; suffers from curse of dimensionality; requires meaningful distance metrics; memory-intensive |
| **Applications**        | Classification, regression, recommendation systems, anomaly detection, pattern recognition, image retrieval                                                                  |
