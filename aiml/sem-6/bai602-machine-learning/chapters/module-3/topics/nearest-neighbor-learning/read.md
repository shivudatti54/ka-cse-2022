# K-Nearest Neighbor Learning

## Introduction to K-Nearest Neighbors

K-Nearest Neighbors (KNN) is one of the simplest and most intuitive supervised machine learning algorithms used for both classification and regression tasks. It belongs to the category of **instance-based learning** or **lazy learning** algorithms, where the function is only approximated locally and all computation is deferred until function evaluation.

The core principle behind KNN is based on the idea that similar things exist in close proximity. In other words, data points with similar features tend to belong to the same class or have similar output values.

### How KNN Works: The Basic Algorithm

The KNN algorithm operates on a simple three-step process:

1.  **Store the training data**: The algorithm memorizes the entire training dataset.
2.  **Calculate distance**: For a new, unseen data point (query instance), calculate the distance between this point and every other point in the training set.
3.  **Find nearest neighbors and predict**: Identify the `K` data points in the training set that are closest to the query instance. For classification, take a majority vote of these `K` neighbors to assign a class label. For regression, take the average of the target values of these `K` neighbors.

```
Training Phase:
+----------------+      +----------------+
| Training Data  |----->| Store in Memory|
+----------------+      +----------------+

Prediction Phase:
+----------------+      +----------------+      +-----------------+      +--------------+
| New Query Point|----->| Calculate      |----->| Find K Nearest  |----->| Predict      |
|                |      | Distances to   |      | Neighbors       |      | (Vote/Average|
+----------------+      | All Stored Pts |      +-----------------+      +--------------+
                        +----------------+
```

## Key Concepts Explained

### 1. Distance Metrics

The choice of distance metric is crucial as it defines the "closeness" of data points. Common distance metrics include:

*   **Euclidean Distance**: The straight-line distance between two points in Euclidean space. It is the most common default choice.
    *   Formula: `d(p, q) = √(Σ(qᵢ - pᵢ)²)`
*   **Manhattan Distance**: The sum of the absolute differences of their coordinates. Useful for high-dimensional data.
    *   Formula: `d(p, q) = Σ|qᵢ - pᵢ|`
*   **Minkowski Distance**: A generalized metric. Euclidean and Manhattan are specific cases of Minkowski.
    *   Formula: `d(p, q) = (Σ|qᵢ - pᵢ|^p)^(1/p)`
*   **Hamming Distance**: Used for categorical data. It measures the number of positions at which the corresponding symbols are different.

**Table: Comparison of Distance Metrics**
| Metric | Formula | Best Use Case |
| :--- | :--- | :--- |
| Euclidean | `√(Σ(qᵢ - pᵢ)²)` | Low-dimensional, continuous numerical data |
| Manhattan | `Σ|qᵢ - pᵢ|` | High-dimensional data, grid-like paths |
| Minkowski | `(Σ|qᵢ - pᵢ|^p)^(1/p)` | Generalized metric (p=1: Manhattan, p=2: Euclidean) |
| Hamming | `Σ(1 if xᵢ ≠ yᵢ else 0)` | Categorical or binary data |

### 2. The Parameter 'K'

The value `K` is a user-defined constant representing the number of neighbors to consider.

*   **Small K (e.g., K=1)**: The model becomes very complex and fits the training data very closely. It has **low bias but high variance**. It is sensitive to noise and outliers. A K=1 classifier is often called the **Nearest Neighbor** classifier.
*   **Large K (e.g., K=50)**: The model becomes smoother and more generalized. It has **higher bias but lower variance**. It makes the decision boundary less erratic but might underfit by ignoring fine details in the data.

Choosing the right `K` is a classic trade-off between bias and variance. It is typically done through techniques like cross-validation.

**ASCII Diagram: Effect of K on Decision Boundary**
```
Small K (K=1) - Complex Boundary        Large K (K=15) - Smooth Boundary

   X X         O O                         X X         O O
 X     X     O     O                      X     X     O     O
X   *   X   O   *   O                    X       X O         O
 X     X     O     O                      X       X O         O
   X X   O   O O                            X X         O O
     O O O O
```
*The asterisk (*) represents a query point. With small K, its class is determined by the single closest point, leading to a jagged boundary. With large K, its class is determined by the majority of a larger region, leading to a smoother boundary.*

### 3. Weighted KNN

In standard KNN, all `K` neighbors contribute equally to the prediction. **Weighted KNN** is an enhancement where each neighbor's contribution is weighted by the inverse of its distance to the query point. Closer neighbors have a higher influence on the prediction than more distant ones.

*   Weight: `wᵢ = 1 / d(p, query)`
*   For classification, the vote of each neighbor is multiplied by its weight.
*   For regression, the average is a weighted average.

This approach often leads to more accurate predictions, especially when the data has uneven density.

## The Nearest Centroid Classifier

This is a related, simpler algorithm often discussed alongside KNN. Instead of comparing a point to all training points, it calculates the centroid (mean) for each class in the training set.

```
For a class C, Centroid = (mean(feature_1), mean(feature_2), ...)
```

For a new query point, the algorithm calculates the distance to each class centroid and assigns the class of the **nearest centroid**.

```
+---------------------+
| Class 1 Training    |-----> Calculate Centroid 1
| Data                |
+---------------------+

+---------------------+
| Class 2 Training    |-----> Calculate Centroid 2
| Data                |
+---------------------+

+----------------+     +-----------------+     +-----------------+
| New Query Point|---->| Dist to Centroid|---->| Assign Class of|
|                |     | 1 & Centroid 2 |     | Closest Centroid|
+----------------+     +-----------------+     +-----------------+
```

*   **Pros**: Much faster prediction than KNN since it only requires a comparison to a few centroids.
*   **Cons**: Often less accurate than KNN because it ignores the detailed distribution of the class (e.g., its shape and size). It assumes each class is a simple, spherical cluster.

## Locally Weighted Regression (LWR)

LWR is an extension of the KNN idea for regression tasks. While standard KNN regression takes a simple average of the `K` nearest neighbors, LWR fits a local linear model around the query point. The contribution of each training point to this local model is weighted by its distance to the query point (typically using a kernel like Gaussian). Points closer to the query have a much higher weight than points farther away. This allows LWR to model complex, non-linear relationships without a global parametric form.

## Advantages and Disadvantages of KNN

**Table: Pros and Cons of KNN**
| Advantages | Disadvantages |
| :--- | :--- |
| Simple to understand and implement. | **Computationally expensive**: Prediction requires comparing to all training examples (O(n) for each prediction). |
| No explicit training phase (just stores data). | **Sensitive to irrelevant features**: The "curse of dimensionality" - distance becomes meaningless in very high-dimensional spaces. |
| Naturally handles multi-class problems. | **Sensitive to the scale of data**: Features on larger scales dominate the distance calculation. Requires feature scaling. |
| Can be effective with the right `K` and distance metric. | **Need to choose `K` and distance metric**: Performance is highly dependent on hyperparameter tuning. |

## Implementation Considerations

1.  **Feature Scaling**: It is **crucial** to scale features (e.g., using Standardization or Min-Max Scaling) before applying KNN. Since KNN uses distance metrics, features with larger ranges will dominate the calculation.
2.  **Curse of Dimensionality**: In high-dimensional space, the concept of "nearest neighbors" becomes less meaningful as the distance between any two points becomes similar. Dimensionality reduction techniques (from Module 2) like PCA can be helpful.
3.  **Efficiency**: For large datasets, the prediction step can be very slow. Data structures like **KD-Trees** or **Ball Trees** can be used to store the training data in a way that makes finding the nearest neighbors much more efficient than a brute-force search.

## Exam Tips

*   **Always mention that KNN is a lazy, instance-based learner**. This is its defining characteristic.
*   Understand the **bias-variance trade-off** concerning the value of `K`. Be prepared to draw a diagram or explain how the decision boundary changes.
*   Remember that KNN **requires feature scaling**. This is a very common point to forget.
*   Be able to **calculate distances** manually for a small, simple dataset (e.g., 2-3 points with 2-3 features).
*   Know the key differences between **KNN** and the **Nearest Centroid Classifier**. The centroid classifier is a model-based approach with a training phase (calculating centroids).
*   For a question on disadvantages, always cite **computational cost** and **curse of dimensionality**.
*   If asked about improving KNN, discuss **Weighted KNN**, using efficient data structures (**KD-Trees**), and **feature selection/scaling**.