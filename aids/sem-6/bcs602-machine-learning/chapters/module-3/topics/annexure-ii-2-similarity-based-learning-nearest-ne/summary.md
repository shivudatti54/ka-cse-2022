# **Annexure-II 2 Similarity-based Learning**

### Nearest-Neighbor Learning

- Definition: A supervised learning algorithm that makes predictions based on the majority vote of the k nearest neighbors to the new input.
- Formula: y = argmax(x_i \* w_i)
- Importance: Simple and widely used, but can be computationally expensive.

### Weighted K-Nearest-Neighbor Algorithm

- Definition: A variation of nearest-neighbor learning that assigns different weights to each neighbor based on their distance.
- Formula: y = argmax(w_i \* x_i \* w_i)
- Importance: Reduces noise in the data, but can be more complex to implement.

### Nearest Centroid Classifier

- Definition: A supervised learning algorithm that makes predictions based on the centroid of the k nearest neighbors.
- Formula: y = argmax(x_i \* w_i)
- Importance: Reduces the impact of noisy data, but can be sensitive to outliers.

### Locally Weighted

- Definition: A supervised learning algorithm that assigns varying weights to each data point based on their distance to the new input.
- Formula: y = argmax(w_i \* x_i)
- Importance: Can handle non-linear relationships and non-stationarity.

### Key Definitions

- **Distance metric**: A function that measures the distance between two data points.
- **Weight**: A scalar value assigned to each data point based on its distance to the new input.
- **Centroid**: The mean value of a set of data points.

### Important Formulas

- **Distance metric**: D(x, y) = √((x1 - y1)^2 + (x2 - y2)^2)
- **Weighted sum**: y = argmax(w_i \* x_i)

### Theorems

- **Chebyshev's Inequality**: The expected value of a function of a random variable is equal to the integral of the function of the probability density function.
- **Bayes' Theorem**: P(y|x) = P(x|y) \* P(y) / P(x)
