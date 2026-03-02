# **Pattern Classification by Prototype Matching (Minimum Distance Classifier Only)**

## **Definitions and Notations**

- **Prototype**: A pre-defined template of a pattern or feature.
- **Feature space**: The space where patterns are represented.
- **Distance metric**: A function that measures the similarity between two objects (e.g., Euclidean distance).
- **Minimum Distance Classifier**: A classifier that assigns a class label to a pattern based on the minimum distance between the pattern and the prototypes of the known classes.

## **Key Concepts and Formulas**

- **Distance Function**:
  - Euclidean Distance: $d(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + ... + (x_n - y_n)^2}$
  - Mahalanobis Distance: $d(x, y) = \sqrt{(x - y)^T \Sigma^{-1} (x - y)}$
- **Minimum Distance Classifier**:
  - Assigns a class label to a pattern $x$ based on the minimum distance between $x$ and the prototypes of the known classes.
  - Formula: $y = \argmin_{y \in C} d(x, y)$
- **Optimization Problem**:
  - Minimize the sum of distances between all patterns and their assigned prototypes.
  - Formula: $\min_{y \in C} \sum_{x \in X} d(x, y)$

## **Theoretical Background**

- **Prototype Matching**: A pattern classification method that uses pre-defined templates (prototypes) to represent patterns.
- **Bayes' Theorem**: $P(y|x) = \frac{P(x|y)P(y)}{P(x)}$
- **Maximum Likelihood Estimation**: $P(x|y) = \frac{f(x|y)}{P(x)}$

## **Revision Tips**

- Understand the concept of prototype matching and minimum distance classifier.
- Familiarize yourself with the distance functions (Euclidean and Mahalanobis).
- Review the optimization problem and its relationship to the minimum distance classifier.
- Practice applying the minimum distance classifier to different patterns and prototypes.
