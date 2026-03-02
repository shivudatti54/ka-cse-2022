# Annexure-II 2 Similarity-based Learning

=====================================

## Introduction

---

Similarity-based learning techniques are used in machine learning for classification and regression tasks.

## 1. Nearest-Neighbor Learning

---

- **Definition:** Nearest-Neighbor (NN) learning is a type of supervised learning algorithm that makes predictions based on the majority vote of its k-nearest neighbors.
- **Formula:** For classification, the prediction is made as the class of the majority vote among the k-nearest neighbors.
- **Advantages:** Easy to implement, fast and simple.
- **Disadvantages:** Sensitive to noise, may not generalize well.

## 2. Weighted K-Nearest-Neighbor Algorithm

---

- **Definition:** Weighted K-Nearest Neighbor (WKNN) is an extension of traditional K-NN that assigns weights to the neighbors based on their distances.
- **Formula:** Predict the class of the instance as the class of the instance with the lowest weighted sum of distances.
- **Advantages:** Can handle noisy data, can assign more importance to closer neighbors.
- **Disadvantages:** Computationally expensive.

## 3. Nearest Centroid Classifier

---

- **Definition:** Nearest Centroid Classifier is a type of supervised learning algorithm that makes predictions based on the class of the centroid of the nearest neighbors.
- **Formula:** The prediction is made as the class of the instance that is closest to the centroid of the k-nearest neighbors.
- **Advantages:** Robust to noise, can handle non-linear relationships.
- **Disadvantages:** Computationally expensive, may not work well with high-dimensional data.

## 4. Locally Weighted

---

- **Definition:** Locally Weighted (LW) is a type of supervised learning algorithm that assigns weights to the neighbors based on the density of the data.
- **Formula:** Predict the class of the instance as the class of the instance with the highest weighted density.
- **Advantages:** Can handle complex relationships, can handle high-dimensional data.
- **Disadvantages:** Computationally expensive, may not work well with sparse data.

### Important Formulas:

- Euclidean Distance: √((x2 - x1)² + (y2 - y1)²)
- Manhattan Distance: |x2 - x1| + |y2 - y1|
- Weighted Sum: ∑wᵢ \* xᵢ

### Important Definitions:

- **K-Nearest Neighbor:** The k instances that are closest to the instance being classified.
- **Centroid:** The mean of the k-nearest neighbors.

### Important Theorems:

- **Bayes' Theorem:** P(y|x) = P(y) \* P(x|y) / P(x)
- **Cauchy-Schwarz Inequality:** (a \* b)² ≤ (a² + b²) \* (c² + d²)
