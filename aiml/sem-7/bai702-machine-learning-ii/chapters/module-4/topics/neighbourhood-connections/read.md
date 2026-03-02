# Module 4: Neighbourhood Connections in Machine Learning

## Introduction

Welcome to Module 4 of Machine Learning II. This module shifts focus from models that make global assumptions about data (like linear regression) to powerful algorithms that base their predictions on the local **neighbourhood** of a data point. The core idea is simple yet profound: similar things exist in close proximity. This principle forms the foundation of a major class of algorithms known as **Instance-Based** or **Lazy Learners**, where the model doesn't learn a discriminative function from the training data upfront. Instead, it memorizes the training instances and defers the computation until a prediction is required.

## Core Concepts

### 1. The "Lazy Learner" Paradigm

Unlike "eager learners" (e.g., Decision Trees, SVMs) that construct a general model during training, lazy learners simply store the training dataset. When a new, unseen data point (query point) needs to be classified or predicted, the algorithm computes the relationship between the query point and *every* stored training instance to make a localized prediction. This makes training very fast (just storing data) but prediction potentially slower, especially with large datasets.

### 2. Distance Metrics: The Measure of "Neighbourhood"

The entire concept hinges on defining "closeness" or similarity. This is quantified using a **distance metric**. The choice of metric is critical and depends on the data type.

*   **Euclidean Distance:** The most common, "straight-line" distance between two points in Euclidean space.
    *   Formula (2D): $d(p, q) = \sqrt{(q_x - p_x)^2 + (q_y - p_y)^2}$
*   **Manhattan Distance:** The sum of the absolute differences of their coordinates. Useful for grid-like movements or high-dimensional sparse data.
    *   Formula (2D): $d(p, q) = |q_x - p_x| + |q_y - p_y|$
*   **Minkowski Distance:** A generalized form. Euclidean (p=2) and Manhattan (p=1) are special cases.
*   **Cosine Similarity:** Measures the cosine of the angle between two vectors. Ideal for text data or high-dimensional data where magnitude is less important than orientation.

### 3. Key Algorithms Based on Neighbourhood

#### a) k-Nearest Neighbours (k-NN)

This is the quintessential neighbourhood-based algorithm.

*   **Classification:** For a new query point, find the `k` training examples that are closest to it (its neighbourhood). The predicted class label is the **majority vote** among these `k` neighbours.
    *   *Example:* If `k=5` and 3 of a point's nearest neighbours are 'Class A' and 2 are 'Class B', the point is classified as 'Class A'.
*   **Regression:** Similarly, find the `k` nearest neighbours. The predicted value is the **mean** (or sometimes median) of the target values of these neighbours.

**The Hyperparameter `k`:** The choice of `k` controls the bias-variance trade-off.
*   A **small `k`** (e.g., 1) makes the model very flexible, capturing fine-grained patterns (low bias) but is highly sensitive to noise (high variance). It leads to a complex, wiggly decision boundary.
*   A **large `k`** (e.g., 20) smooths out the model, making it more robust to noise (low variance) but might oversimplify the problem and miss important details (high bias). It leads to a smoother, simpler decision boundary.

#### b) Radius Neighbours

A variant of k-NN where instead of specifying the number of neighbours `k`, you specify a fixed distance `r`. All training instances within this radius of the query point get to vote. This is particularly useful when the data density is uneven, as it adapts the number of neighbours used based on local density.

### 4. The Curse of Dimensionality

This is a significant challenge for neighbourhood-based methods. As the number of features (dimensions) grows, the volume of the space increases so fast that the available data becomes **extremely sparse**.

*   **Consequence:** The concept of "distance" becomes meaningless. In very high-dimensional space, every data point is approximately equidistant from every other point, making it impossible to find a useful neighbourhood.
*   **Mitigation:** Dimensionality reduction (e.g., PCA) and careful feature selection are essential pre-processing steps.

### 5. Importance of Preprocessing

Since these algorithms rely entirely on distance calculations, they are highly sensitive to the scale of features.

*   A feature with a large range (e.g., salary) will dominate the distance calculation compared to a feature with a small range (e.g., age).
*   **Solution:** **Feature scaling** (Standardization or Normalization) is **mandatory** before applying k-NN or similar algorithms to ensure all features contribute equally to the distance metric.

## Key Points & Summary

*   **Core Idea:** Predict based on the local neighbourhood of similar instances ("lazy learning").
*   **Main Algorithm:** **k-Nearest Neighbours (k-NN)** is the foundational algorithm for both classification (majority vote) and regression (mean value).
*   **Critical Choice:** The hyperparameter **`k`** controls the model's flexibility and directly manages the **bias-variance trade-off**.
*   **Fundamental Requirement:** A **distance metric** (Euclidean, Manhattan, etc.) must be chosen to define "neighbourhood."
*   **Non-Negotiable Preprocessing:** **Feature scaling is essential** to prevent features on larger scales from dominating the distance calculation.
*   **Major Challenge:** These methods suffer from the **curse of dimensionality**, making dimensionality reduction a key consideration.
*   **Pros:** Simple, intuitive, no training time, effective for non-linear problems.
*   **Cons:** Prediction can be slow with big data, sensitive to irrelevant features, requires careful preprocessing.